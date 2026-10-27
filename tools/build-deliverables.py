#!/usr/bin/env python3
"""Regenerate every printable Field Guide Challenge deliverable from this repo.

WHY THIS EXISTS
    The wall sheets, QR cards, facilitator sheet and answer key all restate data that
    lives in app.js — team names, badges, slugs, finish codes, each team's wall plant and
    its height, and which stop each team starts on. Hand-maintaining them guarantees the printed pack eventually
    disagrees with the live game. Everything here is derived from app.js and
    tools/plant-wall.json, so a change to the game is one rerun away from a correct
    print pack. Never hand-edit the generated PDFs.

WHEN TO RUN
    After ANY change to the TEAMS or PLANTS block in app.js (names, plants, heights, finish
    codes, `start` offsets), or to tools/plant-wall.json (which plant, which photo, which organ).

WHERE IT WRITES
    The project Deliverables folder, then an identical copy into every folder in MIRRORS
    (the LUC client folder for Tree Line USA 2026). Both copies are generated; never edit
    either by hand. Pass --no-mirror to skip the copy.

USAGE
    python3 tools/build-deliverables.py              # -> the OneDrive Deliverables folder
    python3 tools/build-deliverables.py --out DIR    # -> somewhere else
    python3 tools/build-deliverables.py --only wall  # wall | qr | facilitator | key

REQUIREMENTS
    pip install qrcode img2pdf pillow python-docx      (all installed as of 2026-09-18)
    ImageMagick (`magick`) and LibreOffice (`soffice`) on PATH.

GOTCHAS THAT COST REAL TIME — see [[gwt_print_deliverables_toolchain]]
  * img2pdf with NO layout_fun sizes each page from that image's embedded DPI, which is
    what gives landscape pages for landscape photos. Passing a fixed `pagesize` forces
    one orientation and letterboxes everything else onto a portrait page.
  * `magick -annotate` dies with "unable to read font ''" unless you pass an explicit
    -font path. There is no usable default.
  * Verify QR codes by DECODING THE RENDERED PDF, not the source images:
        pdftoppm -r 200 -png "Team QR Cards.pdf" z && zbarimg -q --raw z-*.png
    then curl each decoded URL. A wrong QR is only discoverable after printing.
  * Always render the .docx to PDF and LOOK at it. Reading the old facilitator sheet as
    the person holding it is what caught reply words that were two words jammed together.
"""

import argparse, json, os, re, subprocess, sys, glob, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DEFAULT_OUT = os.path.expanduser(
    "~/Library/CloudStorage/OneDrive-GrowWithTrees/GWT Shortcuts/$GWT Info/"
    "LUC/Projects/Field Guide Challenge/Deliverables")
# Follows the repo name. GitHub does NOT redirect a Pages URL after a repo rename: the
# FieldChallenge -> Treeline rename left every printed QR card pointing at a 404.
BASE_URL = "https://growwithtrees.github.io/LUC-GAME-Treeline-DEV"
MIRRORS = [os.path.expanduser(
    "~/Library/CloudStorage/OneDrive-GrowWithTrees/1. GWT Clients/LUC/"
    "LUC Presentations and Projects/2026 Treeline USA/Field Guide Challenge")]
FONT_R = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
GREEN = "#2E7D46"
STOP_NAMES = ["Search", "Identify", "Field Clips", "Field Notes", "Field Bites"]
SHORT = ["Search", "Identify", "Clip", "Note", "Bite"]
BADGES = os.path.join(REPO, "badges")


def read_teams():
    """Parse TEAMS and PLANTS out of app.js. Single source of truth for every artifact."""
    src = open(os.path.join(REPO, "app.js"), encoding="utf-8").read()
    block = re.search(r"var TEAMS = \{(.*?)\n  \};", src, re.S).group(1)
    pat = (r'"(\d+)":\s*\{ slug: "([\w-]+)",\s*name: "([^"]+)",\s*badge: "([\w-]+)",\s*'
           r'plant: "(\w+)",\s*clip: "(\w+)",\s*note: "(\w+)",\s*code: "(\d{4})", order: "([0-4]{5})"')
    teams = [dict(zip(["num", "slug", "name", "badge", "plant", "clip", "note", "code", "order"], m.groups()))
             for m in re.finditer(pat, block)]
    pblock = re.search(r"var PLANTS = \{(.*?)\n  \};", src, re.S).group(1)
    plants = {m.group(1): {"name": m.group(2), "ft": int(m.group(3)), "checked": m.group(4) == "true"}
              for m in re.finditer(r'(\w+):\s*\{ name: "([^"]+)",\s*ft: (\d+),\s*checked: (true|false)', pblock)}
    if not teams or not plants:
        sys.exit("ERROR: could not parse TEAMS/PLANTS out of app.js — did its formatting change?")
    wall = {p["key"]: p["n"] for p in json.load(open(os.path.join(HERE, "plant-wall.json")))}
    for t in teams:
        if t["plant"] not in plants or t["plant"] not in wall:
            sys.exit("ERROR: team %s's plant '%s' is missing from PLANTS or plant-wall.json" % (t["name"], t["plant"]))
        p = plants[t["plant"]]
        if sorted(t["order"]) != list("01234"):
            sys.exit("ERROR: team %s's order %s is not each stop once" % (t["name"], t["order"]))
        t["startname"] = STOP_NAMES[int(t["order"][0])]
        t["ordernames"] = ", ".join(SHORT[int(i)] for i in t["order"])
        t["plantname"], t["sheet"] = p["name"], wall[t["plant"]]
        t["height"] = ("%d ft" % p["ft"]) if p["checked"] else "READ IN APP (game takes any number)"
        t["checked"] = p["checked"]
    variants = read_variants(src)
    for t in teams:
        for k in ("clip", "note"):
            if t[k] not in variants[k]:
                sys.exit("ERROR: team %s's %s '%s' is not in app.js" % (t["name"], k, t[k]))
            t[k + "label"], t[k + "answer"] = variants[k][t[k]]
    unchecked = [t["plantname"] for t in teams if not t["checked"]]
    if unchecked:
        print("  WARNING: heights not yet read off the LUC app, game accepts any number: "
              + ", ".join(unchecked))
    return teams


# What each clip and note is called on the printed sheets. The answers come from app.js.
VARIANT_LABELS = {
    "clip": {"roses": "Multiflora rose vs native rose", "ivy": "Poison ivy vs Virginia creeper"},
    "note": {"johnson": "Johnsongrass", "elder": "Elderberry Bloom", "olive": "Wanted: Autumn Olive"},
}


def read_variants(src):
    """{'clip': {key: (label, ANSWER)}, 'note': {...}} from the CLIPS and NOTES blocks of app.js."""
    out = {}
    for kind, var in (("clip", "CLIPS"), ("note", "NOTES")):
        block = re.search(r"var %s = \{(.*?)\n  \};" % var, src, re.S).group(1)
        out[kind] = {}
        for key, body in re.findall(r"\n    (\w+): \{(.*?)\n    \}", block, re.S):
            num = re.search(r"number: (\d+)", body)
            acc = re.findall(r'"([^"]+)"', re.search(r"accept: \[([^\]]*)\]", body).group(1))
            out[kind][key] = (VARIANT_LABELS[kind].get(key, key), (num.group(1) if num else acc[0]).upper())
    return out


def build_wall(out):
    """One page per plant, numbered, deliberately UNLABELLED, orientation-matched.
    Each sheet is one team's target, so the wall needs exactly one sheet per team."""
    from PIL import Image
    import img2pdf
    plants = json.load(open(os.path.join(HERE, "plant-wall.json")))
    tmp = os.path.join(HERE, "_wall"); os.makedirs(tmp, exist_ok=True)
    missing = [p["src"] for p in plants if not os.path.exists(os.path.expanduser(p["src"]))]
    if missing:
        sys.exit("ERROR: wall source image(s) not found:\n  " + "\n  ".join(missing))
    for p in plants:
        src = os.path.expanduser(p["src"])
        w, h = Image.open(src).size
        land = w > h
        canvas = "1650x1275" if land else "1275x1650"      # letter at 150dpi
        fit = "1560x1185" if land else "1185x1560"          # 0.3in margins, maximised
        subprocess.run(["magick", src, "-auto-orient", "-resize", fit,
                        "-background", "white", "-gravity", "center", "-extent", canvas,
                        "-font", FONT_R, "-pointsize", "80", "-fill", "#444444", "-undercolor", "white",
                        "-gravity", "southeast", "-annotate", "+55+45", str(p["n"]),
                        "-density", "150", "-units", "PixelsPerInch", "-quality", "94",
                        os.path.join(tmp, "%02d.jpg" % p["n"])], check=True)
        p["orient"] = "landscape" if land else "portrait"
    files = sorted(glob.glob(os.path.join(tmp, "*.jpg")))
    dest = os.path.join(out, "2 Print - Plant Wall")
    os.makedirs(os.path.join(dest, "Individual Sheets"), exist_ok=True)
    # NO layout_fun: each page takes its own image's orientation. See module docstring.
    with open(os.path.join(dest, "Plant Wall - Print Sheets.pdf"), "wb") as f:
        f.write(img2pdf.convert(files))
    for old in glob.glob(os.path.join(dest, "Individual Sheets", "*.jpg")):
        os.remove(old)
    for p in plants:
        extra = ""
        shutil.copy(os.path.join(tmp, "%02d.jpg" % p["n"]),
                    os.path.join(dest, "Individual Sheets",
                                 "%02d %s - %s%s [%s].jpg"
                                 % (p["n"], p["name"].split(" /")[0], p["organ"], extra, p["orient"])))
    json.dump(plants, open(os.path.join(HERE, "_wallkey.json"), "w"), indent=1)
    shutil.rmtree(tmp)
    print("  wall: %d sheets" % len(files))


def build_qr(teams, out):
    """One card per team: badge, name, QR, and the plain URL as a fallback."""
    import qrcode, img2pdf
    from PIL import Image, ImageDraw, ImageFont
    tmp = os.path.join(HERE, "_qr"); os.makedirs(tmp, exist_ok=True)
    W, H = 1275, 825                                   # half-letter at 150dpi
    for i, t in enumerate(teams, 1):
        url = "%s/%s/" % (BASE_URL, t["slug"])
        q = qrcode.QRCode(box_size=10, border=2,
                          error_correction=qrcode.constants.ERROR_CORRECT_M)
        q.add_data(url); q.make(fit=True)
        qi = q.make_image(fill_color="black", back_color="white").convert("RGB") \
              .resize((560, 560), Image.NEAREST)
        card = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(card)
        d.rectangle([0, 0, W, 18], fill=GREEN)
        card.paste(qi, (70, 120))
        badge = Image.open(os.path.join(BADGES, t["badge"] + ".png")).convert("RGBA") \
                     .resize((300, 300), Image.LANCZOS)
        cx = 700 + (W - 60 - 700) // 2                # centre of the right-hand column
        card.paste(badge, (cx - 150, 70), badge)
        fb = ImageFont.truetype(FONT_B, 54)
        d.text((cx, 405), t["name"], font=fb, fill="#111111", anchor="mt")
        d.text((cx, 495), "Scan to start your quest.",
               font=ImageFont.truetype(FONT_R, 36), fill="#374151", anchor="mt")
        d.text((cx, 550), "One phone drives; everyone helps.",
               font=ImageFont.truetype(FONT_R, 30), fill="#6b7280", anchor="mt")
        d.text((70, 745), url, font=ImageFont.truetype(FONT_R, 26), fill="#9ca3af")
        card.save(os.path.join(tmp, "%02d.jpg" % i), quality=92, dpi=(150, 150))
    pages = []
    for i in range(0, len(teams), 2):
        p = Image.new("RGB", (1275, 1650), "white")
        p.paste(Image.open(os.path.join(tmp, "%02d.jpg" % (i + 1))), (0, 0))
        if i + 2 <= len(teams):
            p.paste(Image.open(os.path.join(tmp, "%02d.jpg" % (i + 2))), (0, 825))
        ImageDraw.Draw(p).line([(0, 824), (1275, 824)], fill="#cccccc", width=2)
        fn = os.path.join(tmp, "page%d.jpg" % (i // 2 + 1))
        p.save(fn, quality=92, dpi=(150, 150)); pages.append(fn)
    lay = img2pdf.get_layout_fun(pagesize=(img2pdf.in_to_pt(8.5), img2pdf.in_to_pt(11)),
                                 fit=img2pdf.FitMode.into)
    dest = os.path.join(out, "3 Print - Team QR Cards"); os.makedirs(dest, exist_ok=True)
    with open(os.path.join(dest, "Team QR Cards.pdf"), "wb") as f:
        f.write(img2pdf.convert(pages, layout_fun=lay))
    shutil.rmtree(tmp)
    print("  qr: %d cards" % len(teams))
    print("  VERIFY BEFORE PRINTING: pdftoppm -r 200 -png 'Team QR Cards.pdf' z && "
          "zbarimg -q --raw z-*.png   (then curl each URL)")


def _docx_to_pdf(path, dest):
    subprocess.run(["/Applications/LibreOffice.app/Contents/MacOS/soffice", "--headless",
                    "--convert-to", "pdf", "--outdir", dest, path],
                   check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def build_facilitator(teams, out):
    """Lindsey's 4-page sheet. Delegates to _facilitator_sheet.py, which holds the layout."""
    dest = os.path.join(out, "4 Print - Facilitator"); os.makedirs(dest, exist_ok=True)
    json.dump(teams, open(os.path.join(HERE, "_teams.json"), "w"), indent=1)
    subprocess.run([sys.executable, os.path.join(HERE, "_facilitator_sheet.py")],
                   cwd=HERE, check=True)
    src = os.path.join(HERE, "Facilitator Sheet.docx")
    shutil.copy(src, os.path.join(dest, "Facilitator Sheet.docx"))
    _docx_to_pdf(src, dest)
    os.remove(src)
    print("  facilitator: Facilitator Sheet.docx + .pdf")


def read_stops():
    """Feature name and accepted answers per stop, in canonical order, straight from app.js."""
    src = open(os.path.join(REPO, "app.js"), encoding="utf-8").read()
    body = src[src.index("function buildStops"):src.index("function ordered")]
    stops = []
    for chunk in body.split("icon: ")[1:]:
        feat = re.search(r'feat: "([^"]+)"', chunk).group(1)
        acc = re.search(r'accept: \[([^\]]*)\]', chunk)  # absent for per-team stops
        num = re.search(r'number: (\d+)', chunk)
        stops.append((feat, re.findall(r'"([^"]+)"', acc.group(1)) if acc else [],
                      num.group(1) if num else None))
    if len(stops) != len(STOP_NAMES):
        sys.exit("ERROR: expected %d stops in app.js, found %d" % (len(STOP_NAMES), len(stops)))
    return stops


def build_key(teams, out):
    """The one-page answer key Lindsey keeps. Lives beside Deliverables, not inside it."""
    from docx import Document
    from docx.shared import Pt
    stops = read_stops()
    doc = Document()
    st = doc.styles["Normal"]; st.font.name = "Arial"; st.font.size = Pt(10.5)
    doc.add_heading("Field Guide Challenge: Answer Key", 1)
    doc.add_paragraph("LUC Tree Line USA icebreaker. Facilitator eyes only. Answers are not "
                      "case-sensitive and spaces are ignored.")
    doc.add_heading("Stops", 2)
    t = doc.add_table(rows=1, cols=4); t.style = "Table Grid"
    for c, h in zip(t.rows[0].cells, ["#", "Let Grow feature", "Answer", "Also accepted"]):
        c.text = h
    for i, (feat, acc, num) in enumerate(stops):
        if feat == "Identify":
            ans, also = "That team's plant height (see the team table)", "Feet or inches"
        elif feat in ("Field Clips", "Field Notes"):
            ans, also = "Depends on the team's %s (see the team table)" % (
                "clip" if feat == "Field Clips" else "field note"), "See app.js"
        else:
            words = [a for a in acc]
            ans = (num if num else words[0]).upper()
            also = ", ".join(w for w in words if w.upper() != ans) or "None"
        for c, v in zip(t.add_row().cells, [str(i + 1), feat, ans, also]):
            c.text = v
    doc.add_heading("Teams", 2)
    doc.add_paragraph("Every team walks all five stops in its own order. Stops 2 to 4 differ by team: each team hunts its own plant on the "
                      "wall and gets one of two field clips and one of three field notes. Check each finish code against the team name and write down the order "
                      "teams arrive.")
    t = doc.add_table(rows=1, cols=6); t.style = "Table Grid"
    for c, h in zip(t.rows[0].cells, ["Team", "Their plant (wall sheet) and height", "Field clip",
                                      "Field note", "Stop order", "Finish code"]):
        c.text = h
    for tm in teams:
        for c, v in zip(t.add_row().cells, [tm["name"],
                                             "%s (sheet %d): %s" % (tm["plantname"], tm["sheet"], tm["height"]),
                                             "%s: %s" % (tm["cliplabel"], tm["clipanswer"]),
                                             "%s: %s" % (tm["notelabel"], tm["noteanswer"]),
                                             tm["ordernames"],
                                             tm["code"]]):
            c.text = v
    doc.add_heading("Watch for", 2)
    for b in ["Buttonbush (sheet 1) and elderberry (sheet 9) both read 12 ft, and tree of heaven "
              "(sheet 8) and hackberry (sheet 10) both read 60 ft, so those teams pass even if they "
              "scan the other one of the pair.",
              "Scan mismatches. If a scan returns the wrong plant, check the leaf / flower / fruit / "
              "bark selector first. The roughleaf dogwood photo reads as red osier dogwood; either "
              "name is fine.",
              "Source. Generated from app.js in LUC-GAME-Treeline-DEV by "
              "tools/build-deliverables.py. Do not edit by hand; rerun the script."]:
        doc.add_paragraph(b, style="List Bullet")
    path = os.path.join(os.path.dirname(out.rstrip("/")), "Field Guide Challenge Answer Key.docx")
    doc.save(path)
    print("  key: %s" % path)


def mirror(out):
    """Copy the whole Field Guide Challenge folder (Deliverables + answer key) to each MIRROR."""
    root = os.path.dirname(out.rstrip("/"))
    for m in MIRRORS:
        if not os.path.isdir(m):
            print("  mirror SKIPPED, folder missing: %s" % m); continue
        dst = os.path.join(m, os.path.basename(out.rstrip("/")))
        # copytree only adds. Clear the generated wall sheets first, or a plant taken off the
        # wall lingers in the mirror (the 27 Oct redcedar -> burning bush swap did exactly that).
        stale = os.path.join(dst, "2 Print - Plant Wall", "Individual Sheets")
        for old in glob.glob(os.path.join(stale, "*.jpg")):
            os.remove(old)
        shutil.copytree(out, dst, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".DS_Store"))
        shutil.copy(os.path.join(root, "Field Guide Challenge Answer Key.docx"), m)
        print("  mirrored -> %s" % m)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=DEFAULT_OUT, help="deliverables folder")
    ap.add_argument("--only", choices=["wall", "qr", "facilitator", "key"],
                    help="build just one artifact")
    ap.add_argument("--no-mirror", action="store_true", help="skip copying to MIRRORS")
    a = ap.parse_args()
    teams = read_teams()
    print("Read %d teams from app.js: %s" % (len(teams), ", ".join(t["name"] for t in teams)))
    wall = json.load(open(os.path.join(HERE, "plant-wall.json")))
    if len({t["order"] for t in teams}) != len(teams):
        sys.exit("ERROR: two teams share a stop order")
    if len(wall) != len(teams) or len({t["plant"] for t in teams}) != len(teams):
        sys.exit("ERROR: the wall needs exactly one sheet per team and no two teams on one plant")
    os.makedirs(a.out, exist_ok=True)
    want = (lambda k: a.only in (None, k))
    if want("wall"): build_wall(a.out)
    if want("qr"): build_qr(teams, a.out)
    if want("facilitator"): build_facilitator(teams, a.out)
    if want("key"): build_key(teams, a.out)
    if not a.no_mirror and a.out == DEFAULT_OUT:
        mirror(a.out)
    print("Done -> %s" % a.out)


if __name__ == "__main__":
    main()
