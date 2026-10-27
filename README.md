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

1. **Search**: a homeowner wants a bird-friendly replacement shrub. Filters: border zone, slow growing, host plant and bird food, 15 ft or less. Answer `HOLLY`. Lindsey ran the filters live on the 27 Oct call and only holly came up.
2. **Identify**: each team gets **its own plant** on the plant wall, finds it by scanning the unlabelled photos, and types its max height from the Let Grow entry.
3. **Field Clips**: the multiflora rose vs native rose clip. The invasive rose's leaf base is "covered in like eyelashes." Answer `EYELASHES`.
4. **Field Notes**: the Johnsongrass tailgate. Seeds stay viable "up to 20 years." Answer `20`.
5. **Field Bites**: *Black Locust vs False Indigo Bush*. Indigo bush flowers are "like little purple foxtails." Answer `FOXTAILS`.

Questions 3 to 5 ask for a detail only the resource gives, so a team of expert botanists still has to open it (Lindsey's ask: trainers and advanced ID people are spread across the teams).

Every team does all five but starts at a different one and wraps around. Progress is saved per team in `localStorage` (key `luc-escape-v2-N`), so a refresh or dropped signal keeps their place. Words match case- and punctuation-insensitively. **Numbers match whole**: the first number typed must equal the answer in feet or inches, so 120 never passes for 12.

### Plant heights

`PLANTS` in `app.js` holds each wall plant's max height in feet. Six are confirmed from the LUC plant export. The other six (Callery pear, black locust, tree of heaven, coralberry, eastern redcedar, hackberry) are `checked: false`: they are not in any LUC export, so somebody has to read them off the app. Until they are, **the game accepts any number** for those teams, so nobody gets stuck on the day. The build prints a warning while any remain.

## Changing teams

1. Edit the `TEAMS` block in `app.js` (slug, name, badge, plant, code, start). Each plant needs a matching `PLANTS` entry and a sheet in `tools/plant-wall.json`; the build refuses to run if two teams share a plant.
2. Add or remove the matching `team-N/index.html` and its row in `index.html`.
3. Run `python3 tools/build-deliverables.py`. It rebuilds every printed piece and the answer key into the project Deliverables folder and mirrors the lot to the LUC client folder (`1. GWT Clients/LUC/LUC Presentations and Projects/2026 Treeline USA/Field Guide Challenge/`). Never hand-edit either copy.
4. Decode the QR PDF and curl every URL before printing (command in the script's docstring).
