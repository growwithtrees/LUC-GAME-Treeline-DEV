# Field Guide Challenge — Build & Facilitation Pack

Companion to the app in this repo. The **app is the engine** (it gates the codes and sends crews into the Let Grow app); this doc is the human side: what to build in Let Grow, the trainer scripts, the plant wall, the physical setup, and the answer key.

**Client:** Liberty Utilities (LUC), central Missouri ROW · **Delivery:** conference icebreaker, ~100 people, up to 12 teams, all at once, 15–25 min, expect ~50% to sit out.

---

## 1. The app

- Live: `https://growwithtrees.github.io/LUC-GAME-Treeline-DEV/` · one page per team slug, opened by that team's QR code (no picker). **The repo was renamed from `LUC-GAME-FieldChallenge-DEV` some time after 28 Sep, and GitHub does not redirect the old Pages URL**, so anything printed before the 23 Oct rebuild points at a 404.
- Teams are plain **numbers**, 1 to 12. No name can collide with a puzzle answer, and every plant stays free for the wall.
- Six stops, each a real Let Grow feature. Enter the code the app gives you, unlock the next stop. Finish → that team's own 4-digit **finish code**, which they bring to the facilitator table. **No team ever waits on another** (Lindsey, 23 Oct: the old paired boxes let a slow partner hold up a fast team).

| Team | Slug | Finish code | Trainer | Reply word | Starts at |
|---|---|---|---|---|---|
| Team 1 | `/team-1` | `4712` | Hannah | `CORRIDOR` | Messages |
| Team 2 | `/team-2` | `5836` | Hannah | `COMPATIBLE` | Field Guide |
| Team 3 | `/team-3` | `2964` | Hannah | `SELECTIVE` | Scan |
| Team 4 | `/team-4` | `8153` | Hannah | `CLEARANCE` | Field Clips |
| Team 5 | `/team-5` | `7026` | Hannah | `FOLIAR` | ChatTrain |
| Team 6 | `/team-6` | `3591` | Hannah | `BASAL` | Field Bites |
| Team 7 | `/team-7` | `6247` | Hannah | `FLASHOVER` | Messages |
| Team 8 | `/team-8` | `1938` | Hannah | `CONDUCTOR` | Field Guide |
| Team 9 | `/team-9` | `9405` | Hannah | `SAPLING` | Scan |
| Team 10 | `/team-10` | `2679` | Hannah | `ENCROACH` | Field Clips |
| Team 11 | `/team-11` | `8314` | Hannah | `EASEMENT` | ChatTrain |
| Team 12 | `/team-12` | `5162` | Hannah | `CANOPY` | Field Bites |

**Every team walks all six stops, but each STARTS on a different one and wraps around.** Team 3 goes
Scan → Field Clips → ChatTrain → Field Bites → Messages → Field Guide, and so on. The stops are
independent puzzles, so order changes nothing about the answers — it only stops the whole room
messaging Hannah in the same minute and then queueing at the plant wall together. With twelve teams over
six stops, two teams share each entry point. The `start` field in `app.js` sets it per team.

**Team count does not depend on headcount.** All 12 pages are built. Hand out as many QR cards as there are teams, in any order. The facilitator checks each finish code against the team number and writes down the order teams arrive; what that order earns (prize, points) is Lindsey's call and changes nothing in the game.

---

## 2. The six stops (content + answer)

**Numbered in canonical order, which is NOT the order most teams meet them** — see the staggered start above. Nothing here depends on order.

1. **Messages** — team opens Messages, finds their trainer, sends `TEAM <n> CHECKING IN` (e.g. `TEAM 3 CHECKING IN`); trainer replies their word. **Answer = the trainer's word.**
2. **Field Guide / Search** — clue only (low compatible shrub, coral-pink berry clusters, heavy deer browse). Search the field guide to name it. **Answer = `CORALBERRY`** (`BUCKBRUSH` and `INDIAN CURRANT` also accepted).
   > **CONFIRMED loaded — plant ids 143 (WZC-BZS) and 455 (WZS-BZS), filed as “Coralberry.”** Note LUC's own 26-species compatible list and the shipped *Ozark Buckbrush vs Multiflora Rose* Field Bite both call it **Buckbrush**, so crews may type the name their own training taught them. Both accepted; the facilitator should not correct anyone who says buckbrush.
3. **Plant Identify / Scan** — on the plant wall, find the shrub that grows **with its feet in the water** and carries a **creamy white pincushion flowerhead** (buttonbush), scan it, open its entry, read its **max height**. **Answer = `12`** (`144` also accepted as a safety net). Reads real entry data, no planted code — see [design note](#7-design-notes).
   > **CONFIRMED loaded — plant ids 75 (WZD-BZS) and 380 (LET_GROW), *Cephalanthus occidentalis*, max height `144`.** The database stores inches; the learner app runs it through `inchToFeet()` and renders **feet + inches**, so the entry reads **12 ft 0 in**. The answer is therefore `12`, as written.
4. **Field Clips** — play **“What’s the Tree.”** Johnny reads one tree part by part (2:06, vertical) and **never names it**, on screen or in audio. The team names it from the field marks. **Answer = `CALLERY PEAR`** (`BRADFORD PEAR` and bare `PEAR` also accepted).
   > **The published title must not contain the species.** Mike cut a dedicated version for this, `2026.09.14 Treeline - What's the Tree.mp4` — publish that one, not the original `…Botany In A Blink - Callery Pear.mp4`, whose filename gives the answer away. The in-app clue says **“What’s the Tree,”** so keep that phrase in the Field Clips title.
5. **ChatTrain** — reassure landowner **Mrs. Webb** about spraying; pass the beat for the phrase. **Answer = `COMPATIBLE COVER`.**
6. **Field Bites** — complete the microlearning *What Makes a Plant Compatible?*; enter the keyword it ends on. **Answer = `BIOLOGICAL CONTROL`.** The keyword only appears once all three knowledge checks are answered, so the stop cannot be skipped by swiping to the last card.

---

## 3. Trainer cards (print one per trainer)

**One trainer: Hannah.** Every team messages the same person, so there is nothing to staff and nothing to brief beyond one card. Each team still gets its **own** reply word, and the team's name is right there in the message they send, so Hannah just reads the name and looks up the row.

**Hannah's card (print the table from §1 on the back):**
> **Teams will message you `TEAM 1 CHECKING IN`, `TEAM 2 CHECKING IN` and so on.** Read the number, find it on your card, reply with **that team's one word** and nothing else. One message per team. Wrong message? Reply: *"Say again — send me your team name and CHECKING IN."*
>
> `TEAM 1`→CORRIDOR · `TEAM 2`→COMPATIBLE · `TEAM 3`→SELECTIVE · `TEAM 4`→CLEARANCE · `TEAM 5`→FOLIAR · `TEAM 6`→BASAL · `TEAM 7`→FLASHOVER · `TEAM 8`→CONDUCTOR · `TEAM 9`→SAPLING · `TEAM 10`→ENCROACH

**Every reply word is a single word on purpose** — an earlier draft had WIRE ZONE / BORDER ZONE / LOW GROWING, and a space in Hannah's reply would have failed the match. The matcher is now spacing-tolerant either way, but keep the words single. Per-team words are what stop one team shouting the answer across the room. **If twelve lookups under pressure turns out to be too much on the day, the fallback is one shared word for everybody** — set every `word` in `app.js` to the same string and reprint the card. Swapping Hannah for Lindsey is a one-line find-and-replace in `app.js`.

> **Confirmed (Mike, 14 Sep): participants can message other people in the app**, so stop 1 works as designed. Hannah just needs to be watching her inbox during the icebreaker.

---

## 4. Content to build in Let Grow (admin)

| Stop | Feature | Build |
|---|---|---|
| 2, 3 | Plantdex | **BOTH CONFIRMED LOADED, no build needed.** Coralberry (ids 143/455) and Buttonbush (ids 75/380, 144 in = **12 ft**). Verified against the exported LUC plant list, `GWT/GWT Let Grow/PlantDex/LUC plant list .csv` + `2023.06.01 Let Grow Plant List.csv`. **Each is duplicated** under two ids/growth zones (and id 380 is `"Buttonbush "` with a trailing space) — harmless here, since both buttonbush rows carry the same 144 and stop 2 only needs the name, but expect two hits in search. |
| 4 | Field Clips | **CUT AND FILED** — `2026.09.14 Treeline - What's the Tree.mp4` (93 MB, 2:06, 608×1080, in `LUC Training/Environmental Tailgates/2025 Johnny videos/!Completed/`). Verified on the export: no species name in the audio, no opening title card, lower-thirds are trait labels only (LEAF / SMELL / …), generic *Botany In A Blink* outro. **Publish under a title containing “What’s the Tree”** to match the in-app clue. |
| 5 | ChatTrain | The **Mrs. Webb** flow (spec below). |
| 6 | Field Bites | **BUILT AND IN A REPO** — *What Makes a Plant Compatible?* (`luc-what-makes-a-plant-compatible`), `growwithtrees/LUC-LG-FB-CompatibleSpecies-DEV` (private). Still has to be **loaded into Field Bites in the app**. |

**Footnote on the clip, for non-game use.** Johnny *did* record a reveal — `November Videos/Johnny Voice Audio/callery pear pt 3.mp3`: *"What do you think it is? …this is Callery pear. A problem tree, invasive… obviously this can't grow in the line… I take it out."* It was cut from the published 2:10 edit. For the escape room that cut is what makes the stop work, so leave it out. If a straight training version is ever wanted, that audio is the ending.

### ChatTrain — "Mrs. Webb — the spraying question" (single beat)
- **Persona:** Mrs. Webb, a landowner. Concerned, not hostile. (Approved LUC persona surname.)
- **Opening (Mrs. Webb):** *"I saw your crew out there spraying by my fence. Are you killing everything? I've got some good brush the deer use — I don't want it gone."*
- **Score these behaviors (not vocabulary):** (1) reassures her the crew is **selective**, not clearing everything; (2) names that the target is **tall incompatible trees** near the lines, not her low shrubs; (3) affirms the **compatible / wildlife plants (coralberry) stay**.
- **Fail-1/2 coaching** if she isn't reassured (dismissive or over-technical) — brief redirect from the coach.
- **Eval / reveal on pass:** *"That makes me feel a lot better. Thank you for explaining."* → shows **Pass phrase: COMPATIBLE COVER**.
- **Prompt lengths** per house rule: roleplay ~30–50 words, coaching ~50–80, eval ~120–150.

---

## 5. The plant wall

**Ten sheets, one plant each, numbered but deliberately UNLABELLED** — naming them gives away stops
3 and 4. The key is §3 of the facilitator sheet.

**The photos are a deliberate mix of flower, fruit, leaf and bark.** Identify asks the learner which
one they are photographing, and getting that selector right is the real skill the stop teaches — a
team that leaves it on the wrong setting gets poor matches and concludes the app is broken. Stop 3's
clue now says so outright. Mix as built: 2 flower, 2 fruit, 4 leaf, 2 bark.

| # | Plant | Photo | Role |
|---|---|---|---|
| 1 | Buttonbush | flower | **Stop 3's answer** — the creamy white pincushion ball the clue names |
| 2 | Coralberry / buckbrush | fruit | Stop 2's answer — the coral-pink berries the clue names |
| 3 | Roughleaf dogwood | flower | Flat white cluster, the contrast with sheet 1's ball |
| 4 | Blackberry | leaf | Compatible near-miss |
| 5 | Callery pear | fruit | **Stop 4's answer** — the little pears Johnny points at |
| 6 | Eastern redcedar | bark | Reddish fibrous bark peeling in strips, foliage in frame |
| 7 | Black locust | leaf | Pinnate, rounded leaflets, isolated on white |
| 8 | Tree of heaven | leaf | Pinnate with samaras |
| 9 | Elderberry | leaf | **The decoy** — see below |
| 10 | Common hackberry | bark | Corky warts — **tested and confirmed in the app** |

**Pages match each photo's orientation** so every print is as large as letter allows. Print at full
size, no scaling.

**The elderberry hazard.** Its Plantdex entry is a clone of buttonbush's on every field stop 3 reads
— same growth zone (WZD-BZS), same Opposite branching, same MEDIUM growth speed, **same 144 in /
12 ft max height**. They differ only in name, Latin name and family, so there is no other field to
read. A team that scans elderberry therefore clears stop 3 on the wrong plant, invisibly. That is why
the clue leads on the **pincushion flowerhead**, which nothing else on the wall has.
**Seven plants on LUC's list sit at 144 in** (False Indigo Bush, Elderberry, Hazelnut, Glossy
Buckthorn, Japanese Knotweed, Mountain Pepperbush, Buttonbush) — check any new wall plant against
that before it goes up.

**Roughleaf dogwood reads as red osier dogwood** in the app. Harmless: red osier is also a wet-site
shrub so a team may try it, but its entry is **120 in / 10 ft**, so the game rejects the answer and
they look again. Elderberry is the only decoy that passes silently.

**Not on the wall:** osage orange and sweetgum. The library has no usable image for either — every
osage file is the same dormant bud-and-thorn macro. Tree of heaven took osage's slot.

**Bark is the fragile mode.** Black locust bark came back as **salt cedar** when Mike tested it —
both are deeply furrowed reddish-brown, and that generic-furrow category is where the model struggles.
Black locust moved back to its leaf (isolated on white, already confirmed), and the second bark is
now **Eastern redcedar**, whose bark is fibrous and peels in strips, with cedar foliage in frame to
give the model context. **Common hackberry bark is confirmed working.**

If redcedar bark also fails, the next candidates in the library, best first: **eastern hop hornbeam**
(fine shreddy strips, though it is a *compatible* species and not currently on the wall), **black
cherry** (curling plates and lenticels), **silver maple** (shaggy plates), **tree of heaven**
(smooth grey-green with pale striations). Avoid anything merely furrowed — American elm, Siberian
elm, green ash and black locust all share the failure mode.

**Testing status: ALL TEN SHEETS CONFIRMED IN THE APP** (Mike, 15 Sep) — every organ mode reads
correctly off the printed sheet, redcedar bark included. The wall is done.

One shared wall serves every team (they photograph images, not each other).

## 6. Finale, physical setup, roles

- **Finish:** each team's last screen shows its own 4-digit finish code. They bring it to the facilitator table; the facilitator checks it against the team number (facilitator sheet §1) and records the finishing order. No boxes or locks needed.
- **Roles (print one card per team):** Scanner (drives the app), Scribe (runs the screen), Navigator (reads the clues) — forces ≥2 people hands-on.
- **On-site setup, target ≤30 min:** tape up the plant wall · set one QR card per team on tables · hand Hannah her reply-word card. All Let Grow content + all printing is done ahead.

---

## 7. Design notes

- **Stop 3 reads real content, not a planted code.** Entries are all structured the same, so a hidden keyword is gameable; filtering by a trait then reading a real field (buttonbush height) tests the actual skill and needs no admin change.
- **No hints.** Directions say exactly what to do; a wrong answer just shakes with a plain retry. (See the `feedback_interactive_build_design` memory.)

---

## 8. Answer key (facilitator cheat sheet)

| Stop | Feature | Answer |
|---|---|---|
| 1 | Messages | Hannah's per-team word (see §1 table) |
| 2 | Field Guide / Search | `CORALBERRY` (app name) / `BUCKBRUSH` (LUC's name) — both accepted |
| 3 | Plant Identify / Scan | `12` (buttonbush max height) |
| 4 | Field Clips | `CALLERY PEAR` (or `BRADFORD PEAR`) |
| 5 | ChatTrain | `COMPATIBLE COVER` |
| 6 | Field Bites | `BIOLOGICAL CONTROL` |
| — | Finale | team's own finish code (see §1 table) |

---

### Open items before the event

**In the app — nothing here is blocked:**
1. **Upload `2026.09.14 Treeline - What's the Tree.mp4` to Field Clips**, titled to contain **“What’s the Tree.”** Not the original Callery Pear file — the video never names the tree, so the listing title is the only thing that can kill this stop.
2. Have **Hannah watching her Messages inbox** during the icebreaker, reply-word card in hand.

**On us:**
3. **Load the Field Bite into Field Bites in the app.** Repo is live: `growwithtrees/LUC-LG-FB-CompatibleSpecies-DEV` (private, like every other FB repo). Ship it as a **package**, not a paste — `./make-package.sh` builds the zip, and the app truncates pasted HTML at ~64 KB while this deck is ~60 KB standalone / 1.7 MB packaged.
4. **Print:** one QR card per team (against the `LUC-GAME-Treeline-DEV` URL, rebuilt 23 Oct) · the 10-page plant wall · the facilitator sheet for Lindsey · **Hannah's own one-page card** (she gets that, NOT the facilitator sheet, which carries every answer) · **role cards, 3 up, one page per team, cut**. All built, in `$GWT Info/LUC/Projects/Field Guide Challenge/Deliverables/`, and mirrored by the build script to `1. GWT Clients/LUC/LUC Presentations and Projects/2026 Treeline USA/Field Guide Challenge/`.
5. **Buy:** prizes, if Lindsey keeps them. No locks or boxes since 23 Oct.
6. Callery pear **must** be on the wall (stop 4's answer). Buttonbush is the scan target — read the elderberry note in §5 before adding any other wet-site shrub.

**Nothing is blocked on a Liberty answer any more.** Everything above is ours to do.

**Before printing: walk one team through all six stops end to end.** Every piece has been verified on
its own, but the whole chain has never been run, and stop 5 (the Mrs. Webb ChatTrain) has never been
exercised in this configuration.

**Closed:** ~~trainer names~~ (Hannah, all teams) · ~~can a participant message a trainer?~~ (yes, 14 Sep) · ~~redcedar clip must be shot~~ (Callery pear clip exists, verified it never names the tree) · ~~team count waits on headcount~~ (12 pages, each team finishes on its own) · ~~are the plants in Plantdex?~~ (Coralberry 143/455 · Buttonbush 75/380 at 144 in = 12 ft) · ~~Mrs. Webb ChatTrain~~ (trainer 62, `https://chattrain.org/play/252ffb2cf73a`) · ~~Field Bite keyword~~ (`BIOLOGICAL CONTROL`).
