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

| Team | Slug | Finish code | Wall plant | Stop order |
|---|---|---|---|---|
| Oak Titans | `/team-1` | `4712` | Callery pear (5) | Search > Bite > Note > Clip > Identify |
| Pine Patrol | `/team-2` | `5836` | Buttonbush (1) | Clip > Identify > Note > Bite > Search |
| Cedar Command | `/team-3` | `2964` | Black locust (7) | Bite > Note > Clip > Identify > Search |
| Maple Marauders | `/team-4` | `8153` | Blackberry (4) | Identify > Bite > Clip > Note > Search |
| Root Raiders | `/team-5` | `7026` | Tree of heaven (8) | Bite > Clip > Identify > Search > Note |
| Bark Brigade | `/team-6` | `3591` | Coralberry (2) | Note > Clip > Search > Bite > Identify |
| Dogwood Legion | `/team-7` | `6247` | Burning bush (6) | Identify > Note > Search > Bite > Clip |
| Walnut Force | `/team-8` | `1938` | Dogwood (3) | Identify > Note > Bite > Search > Clip |
| Sassafras Wardens | `/team-9` | `9405` | Smooth sumac (12) | Search > Identify > Bite > Clip > Note |
| Redbud Rangers | `/team-10` | `2679` | Hackberry (10) | Clip > Search > Identify > Note > Bite |
| Sycamore Syndicate | `/team-11` | `8314` | Autumn olive (11) | Search > Clip > Bite > Note > Identify |
| Thorn Guard | `/team-12` | `5162` | Elderberry (9) | Bite > Search > Identify > Clip > Note |

Every team walks the stops in its own order. The 12 orders came from a random search over all 120 orders of five stops, keeping a set where no two teams match and no stop ever has more than three teams on it at the same step (Mike, 27 Oct: "make sure they don't go all in the same order"). Slugs stayed `team-1` to `team-12`, so the URLs did not change; only the cards were reprinted. No team got its namesake plant (Dogwood Legion is not on the dogwood).

## 3. The stops and their sources

| # | Feature | Question | Answer | Source |
|---|---|---|---|---|
| 1 | Search | Bird-friendly replacement shrub, four filters | `HOLLY` | Lindsey's live search, 27 Oct |
| 2 | Identify | Find your plant, read max height | per team | `PLANTS` in `app.js` |
| 3a | Field Clips (odd teams) | Invasive rose leaf base "covered in like ___" | `EYELASHES` | Roses clip (2026.03.13), ~1:17 |
| 3b | Field Clips (even teams) | Poison ivy's roots make the vine look fuzzy or ___-like | `ROPE` | Poison Ivy vs Virginia Creeper clip, ~1:08 |
| 4a | Field Notes (teams 1, 4, 7, 10) | Johnsongrass seeds stay viable up to how many years? | `20` | Johnsongrass tailgate, Reproduction box |
| 4b | Field Notes (teams 2, 5, 8, 11) | Elderberry flowers feed bees, flies and ___ | `BEETLES` | Elderberry Bloom BOLO, main paragraph |
| 4c | Field Notes (teams 3, 6, 9, 12) | Wanted dead or ___ | `CONTROLLED` | Wanted: Autumn Olive poster headline |
| 5 | Field Bites | Indigo bush flowers look like little purple ___ | `FOXTAILS` | Black Locust vs False Indigo Bush (field-bites/7), flowers card |

Clips and notes vary by team (Mike, 27 Oct) so neighbouring teams are not chasing the same answer. No team's field note is about its own wall plant. The spare Field Bite is *Yarrow vs Poison Hemlock*. A *Tree of Heaven vs Sumac* Field Bite was mentioned but is not in the FieldBites repos or on S3 (field-bites 6 to 19).

## 4. The plant wall

**Twelve sheets, one per team, numbered but deliberately UNLABELLED.** The key is section 3 of the facilitator sheet.

The photos are a mix of flower, fruit, leaf and bark. Identify asks which one you are photographing, and setting that correctly is the skill the stop teaches. Mix: 2 flower, 3 fruit, 6 leaf, 1 bark.

- **Sheets 1 to 10** were all confirmed in the app by Mike on 15 Sep.
- **Sheets 11 (autumn olive fruit) and 12 (smooth sumac leaf)** were added 27 Oct and confirmed in the app by Mike the same day. All 12 sheets now scan.
- **Buttonbush (1) and elderberry (9) both read 12 ft**, so Pine Patrol and Thorn Guard pass even if they scan the other. Harmless now that each team is told its plant by name.
- **Roughleaf dogwood (3) reads as red osier dogwood**, 10 ft. Walnut Force is told to find "dogwood", so either name is right.
- **Bark is the fragile mode.** Black locust bark read as salt cedar, so its leaf went up instead. Hackberry bark works. Redcedar bark scanned, but the LUC app has no redcedar page, so it came off the wall.

### Heights

All twelve confirmed on 27 Oct. Six came from the LUC plant export; Mike read Callery pear (40), black locust (100), tree of heaven (60), coralberry (5) and hackberry (60) off the app. **Eastern redcedar has no page in the LUC app** (only creeping juniper, 1 ft), so sheet 6 became **burning bush** (LUC list, 20 ft), leaf on white, confirmed in the app at 20 ft. All 12 sheets scan.

Pairs that share a height, so a team scanning the other one still passes: buttonbush and elderberry (12 ft), tree of heaven and hackberry (60 ft).

## 5. Setup and finale

- **On site, under 30 minutes:** tape up the plant wall, set one QR card per team on the tables, hand Lindsey the facilitator sheet.
- **Finish:** each team's last screen shows its finish code. They bring it to the facilitator table; the facilitator checks it against the team name and writes down the order.

## 6. Before printing

Walk one team through all five stops in the real Let Grow app. The browser walk-through covers the game page, not the app: confirm the Search filters still give only holly, and that the rose clip, the Johnsongrass note and the Black Locust bite are all visible to a Liberty login.
