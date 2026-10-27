# Liberty ROW Field Guide Challenge

A digital escape room for the Let Grow app, built for the Liberty Utilities Central (LUC) icebreaker at Tree Line USA 2026, central Missouri. Each team scans a QR code that opens its own quest. Every stop sends the team into a part of the Let Grow app they already have, asks one question, and unlocks the next stop when they type the answer. Finish all five and the page shows that team's own 4-digit **finish code**, which they bring to the facilitator table. No team waits on another.

Lindsey's goal for the game (27 Oct call): get every attendee logged in to Let Grow and show them the resources already in it. Nothing in the game needs new app content.

Live: https://growwithtrees.github.io/LUC-GAME-Treeline-DEV/ (organizer hub). The repo was renamed from `LUC-GAME-FieldChallenge-DEV`; GitHub does not redirect the old Pages URL.

## Structure

- `index.html`: organizer hub listing every team link
- `app.css`, `app.js`: shared engine (one source of truth)
- `team-N/index.html`: one thin page per team; sets `window.TEAM_ID` and loads the shared engine
- `badges/`: the 12 team badges, cut from Lindsey's *Forest Badge Emblem Collection* PNG
- `tools/build-deliverables.py`: regenerates the whole print pack and the answer key from `app.js`
- `docs/build-pack.md`: the human side (the plant wall, setup, what to check before the day)

## The five stops

1. **Search**: a homeowner wants a bird-friendly replacement shrub. Filters: wire zone no / border zone yes (the zone filter is a single choice, Mike 27 Oct), slow growing, host plant and bird food, 15 ft or less. Answer `HOLLY`. Lindsey ran the filters live on the 27 Oct call and only holly came up.
2. **Identify**: each team gets **its own plant** on the plant wall, finds it by scanning the unlabelled photos, and types its max height from the Let Grow entry.
3. **Field Clips**, one of two by team (`clip` in `TEAMS`, alternating):
   - multiflora rose vs native rose: the invasive rose's leaf base is "covered in like eyelashes." Answer `EYELASHES`.
   - poison ivy vs Virginia creeper: Virginia creeper's tendrils "end in sticky pads." Answer `PADS`. (Not the rope-like roots: "hairy rope, don't be a dope" lets an expert answer without watching.)
4. **Field Notes**, one of three by team (`note` in `TEAMS`, cycling):
   - Johnsongrass: rhizomes "can travel up to 200 feet from the mother plant." Answer `200`. (Not the 20-year seed figure: a team could guess its way there.)
   - Elderberry Bloom BOLO: flowers feed "bees, flies, and beetles." Answer `BEETLES`.
   - Wanted: Autumn Olive: "Dead or Controlled." Answer `CONTROLLED`.
5. **Field Bites**: *Black Locust vs False Indigo Bush*. Indigo bush flowers are "like little purple foxtails." Answer `FOXTAILS`.

Six clip-and-note combinations, each used by two teams, so neighbouring teams are not chasing the same answer, and no team's field note is about its own wall plant. Questions 3 to 5 ask for a detail only the resource gives, so a team of expert botanists still has to open it (Lindsey's ask: trainers and advanced ID people are spread across the teams).

Every team walks the five stops in **its own order** (`order` in `TEAMS`). No two teams share an order, and at any step no stop has more than three teams on it. Progress is saved per team in `localStorage` (key `luc-escape-v3-N`), so a refresh or dropped signal keeps their place. Words match case- and punctuation-insensitively. **Numbers match whole**: the first number typed must equal the answer in feet, so 120 never passes for 12. Inches are not accepted (coralberry's 60 in would have matched tree of heaven's and hackberry's 60 ft). Unlock is locked during the unlock animation, so a double tap cannot skip a stop.

### Plant heights

`PLANTS` in `app.js` holds each wall plant's max height in feet, all confirmed as of 27 Oct: six from the LUC plant export, the rest read off the app by Mike. Eastern redcedar has no page in the LUC app, so sheet 6 became burning bush (20 ft). A plant with `checked: false` makes the game take any number for that team, and the build prints a warning; use it only as a stopgap.

## Changing teams

1. Edit the `TEAMS` block in `app.js` (slug, name, badge, plant, clip, note, code, order). Each plant needs a matching `PLANTS` entry and a sheet in `tools/plant-wall.json`; the build refuses to run if two teams share a plant.
2. Add or remove the matching `team-N/index.html` and its row in `index.html`.
3. Run `python3 tools/build-deliverables.py`. It rebuilds every printed piece and the answer key into the project Deliverables folder and mirrors the lot to the LUC client folder (`1. GWT Clients/LUC/LUC Presentations and Projects/2026 Treeline USA/Field Guide Challenge/`). Never hand-edit either copy.
4. Decode the QR PDF and curl every URL before printing (command in the script's docstring).
