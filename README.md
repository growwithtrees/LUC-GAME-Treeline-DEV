# Liberty ROW Field Guide Challenge

A digital escape room for the Let Grow app, built for the Liberty Utilities Central (LUC) icebreaker at Tree Line USA 2026, central Missouri. Each team scans a QR code that opens its own quest. Every stop hides a code inside a Let Grow app feature; enter the code, unlock the next stop. Finish all six and the page shows that team's own 4-digit **finish code**, which they bring to the facilitator table. No team waits on another.

Live: https://growwithtrees.github.io/LUC-GAME-Treeline-DEV/ (organizer hub). The repo was renamed from `LUC-GAME-FieldChallenge-DEV`; GitHub does not redirect the old Pages URL.

## Structure

- `index.html` — organizer hub listing every team link
- `app.css`, `app.js` — shared engine (one source of truth)
- `team-N/index.html` — one thin page per team; sets `window.TEAM_ID` and loads the shared engine
- `tools/build-deliverables.py` — regenerates the whole print pack and the answer key from `app.js`
- `docs/build-pack.md` — the human side: Let Grow content, Hannah, the plant wall, setup

Teams are plain numbers, 1 to 12, so no team name can collide with a puzzle answer. Each team has its own Hannah reply word, finish code and starting stop; all of it is the `TEAMS` block in `app.js`.

## The six stops

1. **Messages** — message Hannah `TEAM <n> CHECKING IN`; she replies that team's word
2. **Field Guide / Search** — name coralberry (buckbrush) from field notes
3. **Plant Identify / Scan** — find buttonbush on the plant wall, read its max height (12 ft)
4. **Field Clips** — name the tree Johnny describes in "What's the Tree" (Callery pear)
5. **ChatTrain** — reassure Mrs. Webb, earn the pass phrase (`COMPATIBLE COVER`)
6. **Field Bites** — finish the microlearning, enter the keyword from its last card (`BIOLOGICAL CONTROL`)

Every team does all six but starts at a different one and wraps around, so the room is never all at Hannah or all at the wall. Progress is saved per team in `localStorage`, so a refresh or dropped signal keeps their place. Answers match case- and punctuation-insensitively and accept common variants.

## Changing teams

1. Edit the `TEAMS` block in `app.js` (slug, trainer, word, code, start).
2. Add or remove the matching `team-N/index.html` and its row in `index.html`.
3. Run `python3 tools/build-deliverables.py`. It rebuilds every printed piece and the answer key into the project Deliverables folder and mirrors the lot to the LUC client folder (`1. GWT Clients/LUC/LUC Presentations and Projects/2026 Treeline USA/Field Guide Challenge/`). Never hand-edit either copy.
4. Decode the QR PDF and curl every URL before printing (command in the script's docstring).
