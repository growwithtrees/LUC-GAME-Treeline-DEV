# Field Guide Challenge — Build & Facilitation Pack

Companion to the app in this repo. The **app is the engine**: it asks the questions and checks the answers. This doc is the human side: the plant wall, setup, and what to check before the day.

**Client:** Liberty Utilities (LUC), central Missouri ROW · **Delivery:** Tree Line USA icebreaker, Thu 29 Oct 2026, ~100 people, up to 12 teams, inside Lindsey's 45-minute slot with her slides.

---

## 1. What changed on 27 Oct (Mike and Lindsey's call)

Lindsey's goal: get everyone logged in to Let Grow and show them the resources already there. So every stop now uses content Liberty already has in the app, and the game teaches the features GWT wants crews to use.

- **Messages stop removed.** GWT no longer uses in-app messages (notifications have their own buttons, and FirstEnergy saw unmonitored chat as a negative). Hannah no longer has a job in the game.
- **ChatTrain (Mrs. Webb) removed.**
- **Field Guide stop is now Search**, with a homeowner scenario Lindsey ran live: border zone, slow growing, host plant and bird food, 15 ft or less gives **holly** only.
- **Identify is per team.** Each team hunts its own plant on the wall and reads its max height. Lindsey's version: "go scan the blackberry and enter the maximum height."
- **Field Clips, Field Notes and Field Bites** each ask for a detail only that resource gives. Experts are spread across teams, so a question they could answer from memory would let them skip the resource.
- **Team names** come from Lindsey's badge set (Oak Titans to Thorn Guard). No name is a puzzle answer.
- **Prizes:** everybody gets PPE (gloves, safety glasses, hard hat stickers). Finish order is kept for bragging rights; nobody has to keep score in the background.
- **No role cards** (Lindsey: "that's too much").

## 2. The teams

| Team | Slug | Finish code | Wall plant | Starts at |
|---|---|---|---|---|
| Oak Titans | `/team-1` | `4712` | Callery pear (5) | Search |
| Pine Patrol | `/team-2` | `5836` | Buttonbush (1) | Identify |
| Cedar Command | `/team-3` | `2964` | Black locust (7) | Field Clips |
| Maple Marauders | `/team-4` | `8153` | Blackberry (4) | Field Notes |
| Root Raiders | `/team-5` | `7026` | Tree of heaven (8) | Field Bites |
| Bark Brigade | `/team-6` | `3591` | Coralberry (2) | Search |
| Dogwood Legion | `/team-7` | `6247` | Eastern redcedar (6) | Identify |
| Walnut Force | `/team-8` | `1938` | Dogwood (3) | Field Clips |
| Sassafras Wardens | `/team-9` | `9405` | Smooth sumac (12) | Field Notes |
| Redbud Rangers | `/team-10` | `2679` | Hackberry (10) | Field Bites |
| Sycamore Syndicate | `/team-11` | `8314` | Autumn olive (11) | Search |
| Thorn Guard | `/team-12` | `5162` | Elderberry (9) | Identify |

Slugs stayed `team-1` to `team-12`, so the URLs did not change; only the cards were reprinted. No team got its namesake plant (Cedar Command is not on the redcedar, Dogwood Legion is not on the dogwood).

## 3. The stops and their sources

| # | Feature | Question | Answer | Source |
|---|---|---|---|---|
| 1 | Search | Bird-friendly replacement shrub, four filters | `HOLLY` | Lindsey's live search, 27 Oct |
| 2 | Identify | Find your plant, read max height | per team | `PLANTS` in `app.js` |
| 3 | Field Clips | Invasive rose leaf base "covered in like ___" | `EYELASHES` | Roses clip (2026.03.13), ~1:17 |
| 4 | Field Notes | Johnsongrass seeds stay viable up to how many years? | `20` | Johnsongrass tailgate, Reproduction box |
| 5 | Field Bites | Indigo bush flowers look like little purple ___ | `FOXTAILS` | Black Locust vs False Indigo Bush (field-bites/7), flowers card |

The two clips Lindsey downloaded were both transcribed. The poison ivy vs Virginia creeper clip is the spare: poison ivy's aerial roots give the vine "a fuzzy or rope-like appearance" (`ROPE`). The spare Field Bite is *Yarrow vs Poison Hemlock*. A *Tree of Heaven vs Sumac* Field Bite was mentioned but is not in the FieldBites repos or on S3 (field-bites 6 to 19).

## 4. The plant wall

**Twelve sheets, one per team, numbered but deliberately UNLABELLED.** The key is section 3 of the facilitator sheet.

The photos are a mix of flower, fruit, leaf and bark. Identify asks which one you are photographing, and setting that correctly is the skill the stop teaches. Mix: 2 flower, 3 fruit, 5 leaf, 2 bark.

- **Sheets 1 to 10** were all confirmed in the app by Mike on 15 Sep.
- **Sheets 11 (autumn olive fruit) and 12 (smooth sumac leaf) were added 27 Oct and are not yet tested.** Scan both off the printed sheet before the day.
- **Buttonbush (1) and elderberry (9) both read 12 ft**, so Pine Patrol and Thorn Guard pass even if they scan the other. Harmless now that each team is told its plant by name.
- **Roughleaf dogwood (3) reads as red osier dogwood**, 10 ft. Walnut Force is told to find "dogwood", so either name is right.
- **Bark is the fragile mode.** Black locust bark read as salt cedar, so its leaf went up instead. Redcedar and hackberry bark both work.

### Heights still to read off the app

Six wall plants are not in any LUC plant export, so their heights are unconfirmed: **Callery pear, black locust, tree of heaven, coralberry, eastern redcedar, hackberry.** Until they are set in `PLANTS` with `checked: true`, the game accepts any number for those six teams. To finish it: scan each sheet, read the max height, update `app.js`, rerun the build, push.

## 5. Setup and finale

- **On site, under 30 minutes:** tape up the plant wall, set one QR card per team on the tables, hand Lindsey the facilitator sheet.
- **Finish:** each team's last screen shows its finish code. They bring it to the facilitator table; the facilitator checks it against the team name and writes down the order.

## 6. Before printing

Walk one team through all five stops in the real Let Grow app. The browser walk-through covers the game page, not the app: confirm the Search filters still give only holly, and that the rose clip, the Johnsongrass note and the Black Locust bite are all visible to a Liberty login.
