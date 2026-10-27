import json, docx
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

TEAMS = json.load(open("_teams.json"))
HEAD, BODY = "Plus Jakarta Sans", "Inter"
INK, MUTE, GREEN = RGBColor(0x11,0x11,0x11), RGBColor(0x6b,0x72,0x80), RGBColor(0x2E,0x7D,0x46)

doc = Document()
for s in doc.sections:
    s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Inches(0.5)
st = doc.styles["Normal"]; st.font.name = BODY; st.font.size = Pt(10); st.font.color.rgb = INK
st.paragraph_format.space_after = Pt(4); st.paragraph_format.line_spacing = 1.12
st.element.rPr.rFonts.set(qn('w:eastAsia'), BODY)

def shade(cell, hexcolor):
    el = OxmlElement('w:shd'); el.set(qn('w:val'),'clear'); el.set(qn('w:fill'), hexcolor)
    cell._tc.get_or_add_tcPr().append(el)

def h(text, size=20, color=INK, before=10, after=4):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after); p.paragraph_format.keep_with_next = True
    r = p.add_run(text); r.font.name = HEAD; r.font.size = Pt(size); r.font.bold = True; r.font.color.rgb = color
    r._element.rPr.rFonts.set(qn('w:eastAsia'), HEAD)
    return p

def para(text, size=10, color=INK, italic=False, bold=False, after=4, space_before=0):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.space_before = Pt(space_before)
    r = p.add_run(text); r.font.size = Pt(size); r.font.color.rgb = color
    r.font.italic = italic; r.font.bold = bold
    return p

def table(headers, rows, widths, header_fill="1C5230"):
    t = doc.add_table(rows=1, cols=len(headers)); t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    # LibreOffice ignores cell widths unless autofit is off and the grid columns carry them too.
    t.autofit = False
    for col, w in zip(t.columns, widths):
        col.width = Inches(w)
    for i, (c, w) in enumerate(zip(t.rows[0].cells, widths)):
        c.width = Inches(w); shade(c, header_fill)
        c.paragraphs[0].paragraph_format.space_after = Pt(2)
        r = c.paragraphs[0].add_run(headers[i]); r.font.bold = True; r.font.size = Pt(9)
        r.font.name = HEAD; r.font.color.rgb = RGBColor(0xff,0xff,0xff)
    for row in rows:
        cells = t.add_row().cells
        for i, (c, val) in enumerate(zip(cells, row)):
            c.width = Inches(widths[i])
            c.paragraphs[0].paragraph_format.space_after = Pt(2)
            txt, bold, fill = (val if isinstance(val, tuple) else (val, False, None))
            if fill: shade(c, fill)
            r = c.paragraphs[0].add_run(txt); r.font.size = Pt(9); r.font.bold = bold
            if fill: r.font.color.rgb = RGBColor(0xff,0xff,0xff)
    return t

# ── header ────────────────────────────────────────────────────────────────
h("Field Guide Challenge — Facilitator Sheet", 22, GREEN, before=0, after=2)
para("Liberty Utilities Central · Tree Line USA, October 2026 · keep this sheet face down",
     9, MUTE, italic=True, after=10)

# ── the teams ─────────────────────────────────────────────────────────────
h("1. Teams and finish codes", 14)
para(f"Up to {len(TEAMS)} teams. Every team finishes on its own: their last screen shows a 4-digit "
     "finish code. They bring it to you, you check it against their team name below and write "
     "down the order teams arrive. Nobody waits on another team. Use as many QR cards as you have "
     "teams, in any order.", 9.5, after=4)
para("Every team does all five stops, each in its own order, so the whole room is never at the "
     "plant wall at once: at any point no stop has more than three teams on it. Stops 2 to 4 differ by team: each team hunts its "
     "own plant on the wall, and gets one of two field clips and one of three field notes, so "
     "neighbouring teams are not chasing the same answer.", 9.5, after=6)
rows = []
for t in TEAMS:
    rows.append([(t["name"], True, None), (t["code"], True, None),
                 "%s (sheet %d): %s" % (t["plantname"], t["sheet"],
                                        t["height"] if t["checked"] else "any number"),
                 "%s: %s" % (t["cliplabel"], t["clipanswer"]),
                 "%s: %s" % (t["notelabel"], t["noteanswer"]),
                 t["ordernames"]])
table(["Team", "Finish code", "Plant (sheet): height", "Field clip: answer", "Field note: answer",
       "Their order"],
      rows, [1.2, 0.6, 1.55, 1.5, 1.4, 1.25])
para("A code that doesn't match the team means they read it off another team's screen.",
     9, MUTE, space_before=4, after=8)

# ── the five stops ────────────────────────────────────────────────────────
doc.add_page_break()          # the team table fills page 1; a stop table split across pages is unreadable
h("2. The five stops: answers, and how to unstick a team", 14, before=0)
para("Numbered for reference only; each team meets them in its own order (last column above). Teams type the "
     "answer into their own page. If one has been stuck a few minutes, give the nudge, not the "
     "answer. The answer column is your backstop only.", 9.5, after=6)

STOPS = [
 ("1", "Search",
  "Homeowner wants a bird-friendly replacement shrub. Filter Search: wire zone no / border zone yes, slow growing, host plant and bird food, 15 ft or less. One plant fits.",
  "HOLLY",
  "“Did you set all four filters?” Leaving one off brings up more than one plant. The zone filter is one choice: wire zone no, border zone yes."),
 ("2", "Identify",
  "Find their own plant on the wall (named on their screen) by scanning photos with Identify, then read its MAX HEIGHT off its Let Grow page.",
  "That team's height (table above)",
  "First ask what they set the leaf/flower/fruit/bark selector to; most bad matches are the wrong setting. Feet or inches both work. If they truly cannot find it, tell them the sheet number."),
 ("3", "Field Clips",
  "Rose clip: at the base of each leaf, the invasive rose's little leaflet is covered in what?\nVine clip: poison ivy's hairy roots make the vine look fuzzy, or like a what?",
  "Rose: EYELASHES\nVine: ROPE",
  "Rose: “Watch the part about the base of the leaf, near the end.”\nVine: “Listen for how poison ivy climbs.”"),
 ("4", "Field Notes",
  "Johnsongrass: how many years can its seeds stay alive in the soil?\nElderberry Bloom: its flowers feed bees, flies and what?\nAutumn Olive: wanted dead or what?",
  "Johnsongrass: 20\nElderberry: BEETLES\nAutumn Olive: CONTROLLED",
  "Johnsongrass: “Look in the Reproduction box.”\nElderberry: “Read the paragraph under the name.”\nAutumn Olive: “It's the headline.”"),
 ("5", "Field Bites",
  "Work through Black Locust vs False Indigo Bush. False indigo bush flowers look like little purple what?",
  "FOXTAILS",
  "“It's on the card about flowers.”"),
]
table(["#", "Feature", "What they have to do", "Answer", "If they’re stuck"],
      [[(s[0], True, None), s[1], s[2], (s[3], True, None), s[4]] for s in STOPS],
      [0.3, 1.0, 2.5, 1.45, 2.25])
para("Answers are not case sensitive and ignore punctuation.", 9, MUTE, space_before=4, after=8)

doc.add_page_break()

# ── plant wall ────────────────────────────────────────────────────────────
h("3. Plant wall key", 14, before=0)
para(f"{len(TEAMS)} sheets, one plant each, numbered but deliberately NOT labelled. Each sheet is "
     "one team's target. This is the only key.", 9.5, after=4)
para("The photos are a MIX of flower, fruit, leaf and bark, because Identify asks which one you are "
     "photographing. Getting that selector right is the skill this stop teaches. The \u201cPhoto is "
     "a\u201d column is what they should select.", 9.5, after=6)
owner = {t["sheet"]: t["name"] for t in TEAMS}
WALL = json.load(open("_wallkey.json"))
table(["Sheet", "What it is", "Photo is a", "Whose plant", "Notes"],
      [[(str(w["n"]), True, None), (w["name"], True, None), (w["organ"], True, None),
        owner.get(w["n"], ""), w.get("note", "")] for w in WALL],
      [0.5, 1.5, 0.85, 1.5, 3.15])
para("", 6, after=6)

# ── if it goes wrong ──────────────────────────────────────────────────────
h("4. If something goes wrong", 14)
for problem, fix in [
  ("A team's QR won't scan", "Type the address on the bottom of their card straight into the browser."),
  ("They closed the page / phone died", "Reopening the same link puts them back where they were; progress is saved on that phone. If they switch phones they start over, so keep one phone driving."),
  ("The app won't identify a printed plant", "Nine times out of ten the flower/fruit/leaf/bark selector is on the wrong setting. Check that first. If it still will not match, tell them which sheet is theirs; the stop only needs the height off the plant's page."),
  ("They're not logged in to Let Grow", "That is the point of the game. Get them logged in before they start."),
  ("A team is miles behind", "Give them the answer to a stop and move them on. Finishing together matters more than every team solving every clue."),
  ("Two teams arrive at once", "Check both codes and write them down in the order they reached you."),
]:
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(3)
    r = p.add_run(problem + " — "); r.font.bold = True; r.font.size = Pt(9.5)
    r2 = p.add_run(fix); r2.font.size = Pt(9.5)

para("Everything the teams need is inside the Let Grow app. If the app is down, the game is down, "
     "so check it the morning of.", 9, MUTE, space_before=8)

doc.save("Facilitator Sheet.docx")
print("built Facilitator Sheet.docx")
