# Field Guide Challenge — Build & Facilitation Pack

Companion to the app in this repo. The **app is the engine**: it asks the questions and checks the answers. This doc is the human side: the plant wall, setup, and what to check before the day.

**Client:** Liberty Utilities (LUC), central Missouri ROW · **Delivery:** Tree Line USA icebreaker, Thu 29 Oct 2026, ~100 people, up to 12 teams, inside Lindsey's 45-minute slot with her slides.

---

## 1. What changed on 27 Oct (Mike and Lindsey's call)

Lindsey's goal: get everyone logged in to Let Grow and show them the resources already there. So every stop now uses content Liberty already has in the app, and the game teaches the features GWT wants crews to use.

- **Messages stop removed.** GWT no longer uses in-app messages (notifications have their own buttons, and FirstEnergy saw unmonitored chat as a negative). Hannah no longer has a job in the game.
- **ChatTrain (Mrs. Webb) removed.**
- **Field Guide stop is now Search**, with a homeowner scenario Lindsey ran live and Mike rechecked 27 Oct: wire zone no / border zone yes, slow growing, host plant and bird food, 15 ft or less gives **holly** only.
- **Plant ID is per team.** Each team hunts its own plant on the wall and reads its max height. Lindsey's version: "go scan the blackberry and enter the maximum height."
- **Field Clips, Field Notes and Field Bites** each ask for a detail only that resource gives. Experts are spread across teams, so a question they could answer from memory would let them skip the resource.
- **Team names** come from Lindsey's badge set (Oak Titans to Thorn Guard). No name is a puzzle answer.
- **Prizes:** everybody gets PPE (gloves, safety glasses, hard hat stickers). The bragging-rights line came off the player screens on 28 Oct (Lindsey); the facilitator sheet still has a blank Finished # column if she wants it.
- **No role cards** (Lindsey: "that's too much").

## 2. The teams

| Team | Slug | Finish code | Wall plant | Stop order |
|---|---|---|---|---|
| Oak Titans | `/team-1` | `4712` | Callery pear (5) | Search > Bite > Note > Clip > Plant ID |
| Pine Patrol | `/team-2` | `5836` | Buttonbush (1) | Clip > Plant ID > Note > Bite > Search |
| Cedar Command | `/team-3` | `2964` | Black locust (7) | Bite > Note > Clip > Plant ID > Search |
| Maple Marauders | `/team-4` | `8153` | Blackberry (4) | Plant ID > Bite > Clip > Note > Search |
| Root Raiders | `/team-5` | `7026` | Tree of heaven (8) | Bite > Clip > Plant ID > Search > Note |
| Bark Brigade | `/team-6` | `3591` | Coralberry (2) | Note > Clip > Search > Bite > Plant ID |
| Dogwood Legion | `/team-7` | `6247` | Burning bush (6) | Plant ID > Note > Search > Bite > Clip |
| Walnut Force | `/team-8` | `1938` | Dogwood (3) | Plant ID > Note > Bite > Search > Clip |
| Sassafras Wardens | `/team-9` | `9405` | Smooth sumac (12) | Search > Plant ID > Bite > Clip > Note |
| Redbud Rangers | `/team-10` | `2679` | Hackberry (10) | Clip > Search > Plant ID > Note > Bite |
| Sycamore Syndicate | `/team-11` | `8314` | Autumn olive (11) | Search > Clip > Bite > Note > Plant ID |
| Thorn Guard | `/team-12` | `5162` | Elderberry (9) | Bite > Search > Plant ID > Clip > Note |

Every team walks the stops in its own order. The 12 orders came from a random search over all 120 orders of five stops, keeping a set where no two teams match and no stop ever has more than three teams on it at the same step (Mike, 27 Oct: "make sure they don't go all in the same order"). Slugs stayed `team-1` to `team-12`, so the URLs did not change; only the cards were reprinted. No team got its namesake plant (Dogwood Legion is not on the dogwood).

## 3. The stops and their sources

| # | Feature | Question | Answer | Source |
|---|---|---|---|---|
| 1 | Search | Bird-friendly replacement shrub, four filters | `HOLLY` | Lindsey's live search, 27 Oct |
| 2 | Plant ID | Find your plant, read max height | per team | `PLANTS` in `app.js` |
| 3a | Field Clips (odd teams) | Invasive rose leaf base "covered in like ___" | `EYELASHES` | Roses clip (2026.03.13), about two-thirds in |
| 3b | Field Clips (even teams) | Virginia creeper's tendrils end in sticky ___ | `PADS` | Poison Ivy vs Virginia Creeper clip |
| 4a | Field Notes (teams 1, 4, 7, 10) | How far can Johnsongrass rhizomes travel from the mother plant, in feet? | `200` | Johnsongrass tailgate, Reproduction box |
| 4b | Field Notes (teams 2, 5, 8, 11) | Elderberry flowers feed bees, flies and ___ | `BEETLES` | Elderberry Bloom BOLO, main paragraph |
| 4c | Field Notes (teams 3, 6, 9, 12) | Wanted dead or ___ | `CONTROLLED` | Wanted: Autumn Olive poster headline |
| 5 | Field Bites | Indigo bush flowers look like little purple ___ | `FOXTAILS` | Black Locust vs False Indigo Bush (field-bites/7), flowers card |

Clips and notes vary by team (Mike, 27 Oct) so neighbouring teams are not chasing the same answer. No team's field note is about its own wall plant. The spare Field Bite is *Yarrow vs Poison Hemlock*. A *Tree of Heaven vs Sumac* Field Bite was mentioned but is not in the FieldBites repos or on S3 (field-bites 6 to 19).

## 4. The plant wall

**Twelve sheets, one per team, numbered but deliberately UNLABELLED.** The key is section 4 of the facilitator sheet.

The photos are a mix of flower, fruit, leaf and bark. Plant ID asks which one you are photographing, and setting that correctly is the skill the stop teaches. Mix: 2 flower, 3 fruit, 6 leaf, 1 bark.

- **Sheets 1 to 10** were all confirmed in the app by Mike on 15 Sep, except sheet 6, which became burning bush on 27 Oct and was confirmed then.
- **Sheets 11 (autumn olive fruit) and 12 (smooth sumac leaf)** were added 27 Oct and confirmed in the app by Mike the same day. All 12 sheets now scan.
- **Buttonbush (1) and elderberry (9) both read 12 ft**, so Pine Patrol and Thorn Guard pass even if they scan the other. Harmless now that each team is told its plant by name.
- **Roughleaf dogwood (3) reads as red osier dogwood**, 10 ft. Walnut Force is told to find "dogwood", so either name is right.
- **Bark is the fragile mode.** Black locust bark read as salt cedar, so its leaf went up instead. Hackberry bark works. Redcedar bark scanned, but the LUC app has no redcedar page, so it came off the wall.

### Heights

All twelve confirmed on 27 Oct. Six came from the LUC plant export; Mike read Callery pear (40), black locust (100), tree of heaven (60), coralberry (5) and hackberry (60) off the app. **Eastern redcedar has no page in the LUC app** (only creeping juniper, 1 ft), so sheet 6 became **burning bush** (LUC list, 20 ft), leaf on white, confirmed in the app at 20 ft. All 12 sheets scan.

Pairs that share a height, so a team scanning the other one still passes: buttonbush and elderberry (12 ft), tree of heaven and hackberry (60 ft).

## 5. Setup and finale

- **On site, under 30 minutes:** tape up the plant wall, set one QR card per team on the tables, hand Lindsey the facilitator sheet.
- **Finish:** each team's last screen shows its finish code. They bring it to Lindsey, who checks it against the team name.

## 6. Before printing

Walk one team through all five stops in the real Let Grow app. The browser walk-through covers the game page, not the app: confirm the Search filters still give only holly, and that the rose clip, the Johnsongrass note and the Black Locust bite are all visible to a Liberty login.

## 7. Adversarial QA, October 27

Two read-only reviewer passes (source alignment; strict editor plus first-time player plus facilitator) and an edge-case browser test. Fixed:
- **Double tap on Unlock skipped stops** (three taps went from stop 1 to stop 4). Unlock now ignores taps during the animation.
- **Inches matched across plants**: coralberry's 5 ft = 60 in passed on tree of heaven's or hackberry's 60 ft. Feet only now; the first number is read from what was typed, so 12'0" is 12.
- **Typing every answer at once** unlocked every word stop. Word answers are capped at four words.
- **Guessable questions**: poison ivy ROPE (field rhyme) became PADS; Johnsongrass 20 years (guessable by stepping 10, 15, 20) became 200 feet.
- Blackberry is named "blackberry (Rubus)", since Let Grow files it as Rubus species. "hollies" accepted.
- Copy: "Welcome, the Sassafras Wardens" bug; intro now says to keep this page open and switch to Let Grow; ranking is "for bragging rights"; hero says "Crack the Let Grow app" (the Field Guide section is no longer a stop); app section names used throughout; "Start over" asks to confirm.
- Print pack: page 1 is a check-in table with a write-in "Finished #" column; stops are named by section, not number (each team counts in its own order); answer key lists every accepted alternate instead of "see app.js"; QR card says "Have Let Grow open and signed in" and the URL is darker; folders renumbered 1 to 3; US spelling and dates.

Rejected: answer-key heading order (an artifact of the reviewer's text export, the .docx is in order); unused SVG icons in app.js (never shown); "tap the match to open its page" (the app's exact UI is unverified).

## 8. Lindsey's text changes, October 28

Sent by text after the review call, applied as she wrote them:
1. The plant wall stop now uses her wording, including the "How to use Plant ID" steps. The stop is labeled **Plant ID** (the app's own button name) everywhere: game, facilitator sheet and answer key.
2. Search filters are listed in the app's order: growth speed, growth zone, special characteristics, mature size.
3. "Welcome, the Thorn Guard" is now "Welcome, Thorn Guard".
4. "Facilitator table" is now "Lindsey" on the intro and finish screens.
5. "We note the order teams finish, for bragging rights. Nobody waits for another team." removed. The finish screen line about writing down the finish stays; the check-in table still has its blank "Finished #" column if she wants it.

## 9. Final adversarial pass, October 28

Two fresh reviewers (consistency and sources; first-time player and Lindsey on the day). No blockers; every answer, code, order, height and sheet number matched across all surfaces. Fixed:
- **Stops opened scrolled down** (focus() jumped to the answer box, so Plant ID opened below the team's plant name). Each stop now opens at the top.
- Long team names were clipped in the top bar at 320-390 px; they wrap now.
- Wrong-answer message: "Check the app, then type just the word or number" (a correct answer typed as a sentence was rejected with no hint why).
- Facilitator sheet: "plant part" instead of "selector"; a dead-end "won't match" fallback now says to give the height and move on; new row for a team on another team's page; sharper Field Bites and vine-clip nudges; "blackberry (Rubus), sheet 4" instead of double brackets.
- Intro card "Finish fast" renamed "Your finish code"; answer key says "Number only" instead of "None" for Johnsongrass.

## 10. Sheets 4 and 10 pulled, October 29 (morning of the event)

Lindsey tested every photo the night before: sheet 4 (blackberry, which she called raspberry) and sheet 10 (hackberry bark) did not scan reliably. Both came off the wall. The remaining sheets keep their numbers so the wall already taped up stays right. Maple Marauders now share coralberry (sheet 2, 5 ft) with Bark Brigade; Redbud Rangers share burning bush (sheet 6, 20 ft) with Dogwood Legion. Both new plants had their heights read off the app. Each pair reaches Plant ID at least two steps apart (Marauders first, Brigade last; Legion first, Rangers third).
