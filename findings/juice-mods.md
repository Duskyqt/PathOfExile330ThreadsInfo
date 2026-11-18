# Juice mods

## What they are

- The game hides some modifiers from the UI. In Mods.dat they're the 70 `RandomJuiceMod<League>*`
  rows, 5 to 9 per league.
- **Domain:** Area (5).
- **Generation type:** 3.
- **Spawn weights:** none, so the server picks them and the client can't predict which.
- **On the map:** a rolled one appears only as map stats.
- **Exclusive pairs:** two pairs share a mod family, so a map can roll at most one mod from each
  pair:
  - Blight Miniboss and Blight Pantheon;
  - Ultimatum Inscribed Only and Ultimatum Catalyst Only.

The full list, with stats and roll ranges, is in [`data/juice-mods.json`](../data/juice-mods.json).

## How we detect them

A juice mod counts as **matched** when every one of its stats is on the map with a value inside
its roll range. It's a **partial** match when some of its stats are there but not all, or the
values fall outside the range.

The method has two known weaknesses:
- **Shared stats.** Extra Red Beasts (2–4) and Red Beast Invasion (18–20) both use
  `map_additional_red_beasts`, and their rolls add up. `analyze.py` fits the two together and
  takes the fewest rolls that reach the value, so 28 reads as one Invasion plus two Extra Red
  Beasts. They're the only two mods that share a stat.
- **Values that add up.** A juice stat that some other source also adds to can push the total
  out of range. Legion's 3 Threads already give 2 extra spawns, so a roll of Additional Legion
  (+1) reads as 3. `analyze.py` subtracts what each league's Threads give on their own first.
  Those amounts are entered by hand in `THREAD_BASE`. At 6 and 8 Legion Threads the amount varies
  (1 to 4 at 6, 3 to 4 at 8, 4 to 5 at 10), so Additional Legion can't be detected there.

Negative ranges are matched like any other: Blight FreeTowers sets tower cost to -100%, and
`analyze.py` treats only a value of 0 as "didn't roll".

## Hypothesis: a juice mod can roll more than once

Scarabs no longer exist, and the atlas tree used for the non-Legion maps had no league content.
Even so, five stat values came out above any single juice roll. Each one fits a whole number of
rolls of the juice mod that uses that stat:

| Map | Stat | Value | One roll | Fits |
|---|---|---|---|---|
| Abyss/Betrayal/Breach | `map_betrayal_spawn_research_chest_clusters` | 33 | 14–18 | 2 rolls (28–36) |
| Abyss/Betrayal/Breach | `map_num_extra_abysses` | 3 | 1 | 3 rolls |
| Abyss/Expedition/Ritual | `map_num_extra_abysses` | 3 | 1 | 3 rolls |
| Bestiary/Blight/Ultimatum | `map_additional_red_beasts` | 5 | 2–4 | 2 rolls (4–8) |
| Bestiary/Breach/Ritual | `map_additional_red_beasts` | 10 | 2–4 | 3 rolls (6–12) |

- Each value comes from a different set of leagues, so this doesn't look like an effect of
  mixing particular leagues.
- The strongest single case is 33 chest clusters. One roll can't reach it.
- `analyze.py` now works out each mod's roll count. It finds the smallest k that fits every
  stat (k × min ≤ value ≤ k × max), after removing what the league's own Threads give. A mod
  that rolled more than once is shown as `xk`.
- Repeat rolls only show up as a higher value on mods with a counted stat. A mod whose stats
  are all on/off flags can't reveal a second roll.

## How often each one rolled

All maps together: 17 at 3/3/3, 17 at 6/6/6, 14 at 8/8/8 (Bestiary / Incursion / Ultimatum,
Betrayal / Expedition / Incursion and Abyss / Blight / Legion), 5 at Breach / Ritual 8/8, 5 solo
10-Legion maps and the five maps of the [level test](levels.md). Counts are
"maps that rolled it / maps that league was in". `xN` is the total number of rolls when that's
higher. The per-run comparisons are in
[results-666.md](results-666.md#juice-grows-with-thread-count) and
[results-888.md](results-888.md#juice-keeps-growing).

- **Juice per map:** 5.8 rolls at 3/3/3 and 7.6 at 6/6/6, over the same 17 league combinations,
  and 10.2 in the fourteen 8/8/8 maps. Two-league 8/8 maps rolled 6.6: about the same per league.
  Solo 10-Legion maps rolled about 2.
- **Repeat rolls:** mostly mods that add more of a content type (abysses, red beasts, chest
  clusters). AdditionalUnstableBreaches' apparent repeats are uncertain (see below). Betrayal MonsterMod also repeated once at 8 Threads, so a mod with
  any counted stat may be able to repeat.

| League | Mods seen |
|---|---|
| Abyss | ExtraAbysses 16/20 (x28), Mortars 11/20, MonsterMods 7/20, ElitePairs 4/20, Consort 2/20 |
| Bestiary | ExtraRedBeasts 12/14 (x20), YellowBeastsReplacedWithAzmeriHulks 11/14, BeastsHaveWisps 4/14, BeastsEinharBloodAura 4/14, RedBeastInvasion 2/14 |
| Betrayal | ChestClusters 11/15 (x15), Buffs 10/15, MonsterMod 6/15 (x7), Catarina 4/15, Sculpture 3/15, Fracture 3/15 |
| Blight | Pustules 13/17, Supercharge 13/17, ExileLane 10/17, CurrencyLane 9/17, Miniboss 5/17, FreeTowers 3/17, Pantheon 1/17 |
| Breach | EmpoweredAilithSkills 8/18, GuaranteedFortress 7/18, EstablishedSpreadCoffers 7/18, AdditionalUnstableBreaches 6/18 (x18, but see below), GenesisSaplingTree 5/18, GuaranteedBoss 3/18, RareMonstersBreachMonsterMods 2/18, WombgiftRareDrops 1/18 |
| Expedition | Scale 11/15, ReviveObelisk 8/15, RunicLieutenants 6/15, LogbookChest 4/15, RunicRares 3/15 |
| Incursion | ContainsFleshMerchant 15/19, ContainsCursedTreasure 10/19, GoldenDoors 9/19, DoorUnlockingObject 8/19, ContainsGoldPiles 8/19, ContainsVaalVessels 4/19 |
| Legion | BothLegionsHaveGenerals 12/20, SmallCrystals 10/20, AllChestsAreWarHoards 7/20, EternalConflict 6/20, MonstersRankHigher 4/20, InvertedLegion 3/20, AdditionalLegion 2/20 (only detectable at 3 Threads) |
| Ritual | WildwoodWisp 13/18, TributeBoss 11/18, BloodShrines 9/18, Bodach 5/18, Nameless 2/18 |
| Ultimatum | Hearts 7/14, CursedCurrency 6/14, SoulCore 5/14, SecondaryStats 5/14, InscribedOnly 3/14, DoubleDown 2/14, CatalystOnly 1/14, Trialmaster 1/14, Oversouls 1/14 |

Breach's juice depends on its Thread branch: a map gets either a hive or unstable breaches,
never both. GuaranteedFortress and EstablishedSpreadCoffers only roll on hive maps, GuaranteedBoss
only on unstable-breach maps. The unstable-breach count (2 to 4) may come partly from the Threads,
so AdditionalUnstableBreaches' repeat rolls are uncertain. See
[results-888.md](results-888.md#breach-hive-or-unstable-breaches).

**Correction (2026-11-16 afternoon maps):** the two lists below record where each mod was first
seen, not a Thread count it needs. SmallCrystals later rolled at 2 Legion Threads, and Fracture,
Sculpture, FreeTowers and InvertedLegion at 6. These mods are rare, and about 5 maps per league per
Thread count was too few to catch them lower. See
[results-1116-mixed.md](results-1116-mixed.md#the-only-at-8-mods-rolled-lower).

## Working explanation: fixed odds, more rolls

Every juice mod can roll at any Thread count with the same chance per roll; the exceptions are
the mods given a minimum area level in the hotfix. Higher Thread counts roll more juice per league,
so rare mods simply turn up more often. The pre-patch data fits this.

- **More rolls.** Juice per league slot was 1.6 at 3 Threads, 2.2 at 4–7 and 3.1 at 8 or more
  (tree 1 and 3 maps, not counting AdditionalLegion and AdditionalUnstableBreaches).
- **Common mods get used up.** A league mostly rolls each mod at most once per map, so the more
  it rolls, the more of its picks fall on the rare mods. With fixed odds, the 18 mods "first seen
  at 6 or 8" should make up 14% of a league's mods at 3 Threads and 18% at 8 or more, from the roll
  count alone.
- **Few maps.** At about 5 maps per league per Thread count, a mod with roughly a 5% chance often
  misses all of them.

**The test.** Each mod got one fixed weight, from how often it rolled across all maps. Each
league slot then drew as many distinct mods as it really rolled, from its own pool, weighted and
without repeats. Simulating the whole dataset 1,500 times gave the expected count for every mod at
3, 4–7 and 8+ Threads. The real data's mismatch from those counts was 70, against a median of 115
and a 95th percentile of 144 across 400 simulated datasets. No league stood out (each scored 3 to
10).

**Caveats.**
- Fitting holds, but proving is beyond this data: with about 20 maps per league, only a large
  Thread-count effect would have shown up.
- The weights were taken from the same data the test checks, which makes the fit look somewhat
  better than it is.
- Picking the 18 "rare" mods by where they were first seen guarantees they look absent at 3, so
  the comparison of rare shares (2% observed at 3 against 14% expected) is biased and isn't the
  evidence. The test over every mod is.
- The area-level-floor mods weren't treated separately. Nearly every map was area level 77–83.

## First seen at 6 Threads (10)

Ultimatum CatalystOnly, Trialmaster, DoubleDown and Oversouls; Breach GuaranteedFortress and
RareMonstersBreachMonsterMods; Legion SmallCrystals; Expedition RunicRares; Bestiary
RedBeastInvasion; Abyss Consort (first at Abyss 10 in the level test). Abyss Mortars never rolled
at 3 Threads but rolled in every Abyss map at 6.

## First seen at 8 Threads (8)

| League | Mods |
|---|---|
| Betrayal | Fracture (3/5), Sculpture (3/5) |
| Legion | InvertedLegion (3/5), MonstersRankHigher (2/5) |
| Blight | FreeTowers (3/5), Pantheon (1/5) |
| Ritual | Nameless (2/5) |
| Breach | WombgiftRareDrops (1/5) |

None of them rolled in any map at 3 or 6 Threads. Legion SmallCrystals went 0/5 at 3, 2/5 at 6
and 5/5 at 8. Details are in [results-888.md](results-888.md#juice-mods-first-seen-at-8).

## Never matched yet (7 of 70)

| League | Mods |
|---|---|
| Bestiary | BlackMorrigan, ExtraHarvestBeasts |
| Blight | GigaLane |
| Expedition | SpecialRemnants |
| Incursion | ReplacePacksWithArchitects, ContainsTempests |
| Legion | InstantBreakout |

Every league has now been run at 8 Threads, so these are either very rare or don't come from
Threads.
