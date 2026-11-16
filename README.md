# What Threads Actually Do to Your Maps

_Path of Exile 3.30 · data collected 2026-11-15 and 2026-11-16_

Threads replaced scarabs in 3.30, and the game won't tell you what they do. The tooltip is
blank, the map device shows nothing, and the client's own data files have empty slots where
the effects should be.

So we went and found out. We read the numbers straight out of game memory while running
63 maps with known Thread setups: every league pairing at 3/3/3, every pairing again at
6/6/6, fourteen maps at 8/8/8, five two-league maps at 8/8, five solo 10-Thread Legion maps,
and a ladder from 1 to 10 Threads.
Here's what turned up.

---

## The short version

**Threads are a trade.** Each one you slot makes that league mechanic's monsters hit harder and
take longer to die. In return you get better loot from those monsters, and more hidden bonus
modifiers ("juice") on the map.

**The juice is the real prize.** Rarity alone never keeps up with the tankiness. But juice
climbs with every Thread count: about 6 mods per map at 3/3/3, 7.6 at 6/6/6 and 10.2 at
8/8/8. Some mods only turned up at higher counts (anecdotal, based on our small sample size,
we're poor and throwing away at least 20c per map to do 8/8/8 runs).

**So add Threads until the next one costs too much.** The early steps are cheap, the late ones
are brutal. Here's how much tankiness each extra Thread adds:

| Going from | 2→3  | 3→4  | 4→5  | 5→6  |  6→7  |  7→8  |
| ---------- | :--: | :--: | :--: | :--: | :---: | :---: |
| Tankiness  | +15% | +30% | +50% | +90% | +170% | +320% |
| Damage     | +5%  | +5%  | +5%  | +5%  |  +8%  | +12%  |

Up to about 5 or 6, each step is small enough that the extra juice is worth a look. From 6
on, a single extra Thread adds more tankiness than the first five put together. Where you stop
depends on where your build hits that wall: 3/3/3 if you're starting out, 6/6/6 for small budgets, 8/8/8 if you are an actual giga blaster because it's extremely rippy.

**A few rules of thumb:**

- **Always fill all three slots.** Juice is rolled per league mechanic, so an empty slot just
  means a third less juice. Adding Threads to one mechanic also doesn't appear to make the
  other mechanics harder. (This is an assumption based on the way the affix names are worded.
  The actual work is done on the server, so it's unclear.)
- **Spread your Threads out.** 3/3/3 beats stacking 9 into one league mechanic by a mile. Even
  if you have the DPS for a 10 thread single league mechanic, don't bother: solo 10 Legion
  rolled about 2 juice mods per map (sample size: 5 maps), against about 10 for 8/8/8, and if you can solo a 10 legion, you can easily solo 8/8/8 with 3 league mechanics.
- **Never slot just one.** A single Thread does nothing only adds the mechanic to the map, so you are better off adding atleast 2 so you get some extra rarity.
- **Nothing else changes the numbers.** They depend only on how many Threads a league mechanic
  has. It doesn't matter which league mechanic it is, what else you've slotted next to it, what
  level the map is, or what your atlas tree looks like (assumption, it's possible that the
  atlas + x threads can do something extra, but no confirmation, also there are non-modifier related interactions that are not verifiable via this memory reading method, a good example is the "Blighted chest" interaction).

If you want to know why, read on.

---

## The trade: rarity for tankiness

Every league mechanic you slot Threads into gets three hidden stats on the map:

1. **Monster damage.** That league mechanic's monsters hit harder.
2. **Monster tankiness.** That league mechanic's monsters take longer to kill.
3. **Item rarity.** Better drops, but _only from that league mechanic's monsters_.

Here's how it scales:

| Threads |  Damage  | Tankiness |  Rarity   |
| :-----: | :------: | :-------: | :-------: |
|    1    | nothing  |  nothing  |  nothing  |
|    2    |   +0%    |   +25%    |   +15%    |
|  **3**  | **+5%**  | **+40%**  | **+25%**  |
|    4    |   +10%   |   +70%    |   +38%    |
|    5    |   +15%   |   +120%   |   +52%    |
|  **6**  | **+20%** | **+210%** | **+70%**  |
|    7    |   +28%   |   +380%   |   +93%    |
|  **8**  | **+40%** | **+700%** | **+125%** |
|   9\*   |   +45%   |  +1050%   |   +145%   |
|  10\*   |   +50%   |  +1400%   |   +160%   |

\* _Only possible with the atlas passive that lifts the cap to 10, and only when a single
league mechanic is slotted._

Look at the gap between the last two columns. At 3 Threads, monsters get 40% tankier for 25%
more rarity. That's a fair trade. At 8 Threads they're **seven times** as tanky for barely more
than double the rarity.

The bold rows are the most solid in the table. 3 and 6 were each measured on 52 league slots
across 18 maps, and 8 on 53 slots across 20 maps. Every one of them matched.

> **A single Thread does nothing.** One Thread marks the league mechanic as present, and that's it: no
> damage, no tankiness, no rarity. If you're slotting a league mechanic, slot at least two.

---

## So which level should you run?

It depends on what's slowing you down. On rarity alone, more Threads always cost you something. 3 is where you get the most rarity for the least pain, and 4 is the last step that's still cheap. From 5 on, each extra Thread
adds 5 to 23 times more tankiness than rarity. Budget builds will be able to do 5 or 6 thread comfortably, barring outside influences like searing exarch.

**Rarity isn't the whole story, though.** Higher Thread counts also roll more juice mods, and
a wider pool of them (\*more on that below). Going from 3/3/3 to 8/8/8 took juice from about 6
mods per map to about 10. That's the case for running more Threads: you're paying tankiness for
extra content, not just for rarity.

**Either way, spread them out, and use all three slots.** Compare:

- **3/3/3:** three league mechanics at +25% rarity each, with monsters +40% tankier.
- **6/6/6:** three league mechanics at +70% rarity each, with monsters +210% tankier.
- **8/8/8:** three league mechanics at +125% rarity each, with monsters +700% tankier.
- **Solo 9:** one league mechanic at +145% rarity, with monsters **+1050%** tankier.
- **Solo 10:** one league mechanic at +160% rarity, with monsters **+1400%** tankier, and only
  about 2 juice mods per map.

> **Where the extra league content comes from.** Slotting a league mechanic switches it on, and
> that doesn't grow with the Thread count. But more Threads mean more juice, and several juice
> mods add more of the league activity itself: Extra Abysses, Additional Legion, Extra Red
> Beasts, Research Chest Clusters. So more Threads do bring more league content. It just
> arrives through the juice rolls, not as a fixed bonus.

---

## The hidden bonus mods ("juice")

On top of the stat trade, every map quietly rolls a handful of extra modifiers from the
league mechanics you've slotted. In the game files they're called `RandomJuiceMod`, and there are 70 of
them, 5 to 9 per league mechanic.

The game doesn't show you which ones you got. The server picks them; your client can't predict
or display them. We only spotted them by matching each map's hidden stats against every juice
mod's possible values.

### More Threads, more juice

|                       | 3/3/3 | 6/6/6 | 8/8/8 |
| --------------------- | :---: | :---: | :---: |
| Maps                  |  17   |  17   |  14   |
| Juice rolls per map   |  5.8  |  7.6  | 10.2  |
| Most juice in one map |   9   |  11   |  12   |

The 3/3/3 and 6/6/6 runs used the exact same 17 league combinations. The 8/8/8 maps only
covered three combinations (Bestiary / Incursion / Ultimatum, Betrayal / Expedition /
Incursion and Abyss / Blight / Legion), so that column compares against averages rather than
twins.

Per league mechanic:

| League mechanic | At 3 | At 6  |  At 8   |
| --------------- | :--: | :---: | :-----: |
| Blight          | 2.2  |  3.0  | **4.6** |
| Betrayal        | 2.0  |  1.8  | **4.6** |
| Ritual          | 2.0  |  1.8  |  3.6†   |
| Bestiary        | 2.8  |  2.6  |   3.5   |
| Legion          | 1.6  | 1.8\* |  3.4\*  |
| Ultimatum       | 1.0  |  2.6  |  3.25   |
| Breach          | 2.0‡ | 3.2‡  |  3.0†   |
| Incursion       | 2.4  |  3.2  |   2.9   |
| Expedition      | 1.2  |  2.4  |   2.8   |
| Abyss           | 2.2§ | 2.8§  |  2.4§   |

\* _Probably an undercount. Above 3 Threads we can't detect Legion's Additional Legion mod (see
Legion's extra spawns below)._

§ _Probably a slight undercount. Similar to legion._

† _From the five two-league Breach / Ritual 8/8 maps._

‡ _Uncertain. Breach's unstable breaches may come partly from the Threads rather than juice,
which would make these counts too high._

Most league mechanics climb steadily. Blight, Betrayal and Legion roughly doubled between 6
and 8. **Abyss and Incursion appear to level off.** Both have few juice mods to choose from,
and Abyss had already rolled every one of its mods by 6. For Abyss at least, that may partly be
our counting rather than the game.

**Ultimatum has climbed at every step.** At 3 Threads it rolled exactly one juice mod in every
map. At 6 it averaged 2.6, and at 8 it rolled 3 or 4 every time.

Keep in mind that the 8-Thread numbers rest on 4 to 5 maps per league mechanic (9 for
Incursion). The direction is clear, the exact averages less so.

### It's the Threads, not the map

We changed the maps on purpose. If juice depended on the map rather than the Threads, mixing
up map levels and affixes would show it.

- **3/3/3:** every map was tier 16 (area level 83).
- **6/6/6:** most maps were dropped to area level 77–78, with almost no map affixes. They still
  rolled more juice than 3/3/3, not less.
- **8/8/8:** mostly back to tier 16, with and without affixes, plus a tier-11 map and two special
  maps with citadel and influence stats.

The juice followed the Threads every time. The tier-11 map rolled 10, exactly like its tier-16
siblings. Maps with and without affixes rolled the same. The two special maps rolled 11 and 9.
Map tier and affixes don't seem to move the juice. The Thread count does.

### Two league mechanics or three?

We ran five maps with only Breach and Ritual slotted, at 8/8, to see whether an empty slot
helps the other two.

|                                        | 3 league mechanics at 8 | 2 league mechanics at 8 |
| -------------------------------------- | :---------------------: | :---------------------: |
| Juice rolls per map                    |          10.2           |           6.6           |
| Juice rolls per league                 |           3.4           |           3.3           |
| Damage / tankiness / rarity per league |  +40% / +700% / +125%   |  +40% / +700% / +125%   |

**It doesn't help them.** Each league mechanic rolls its own juice, whatever else is slotted.
Drop a league mechanic and you lose its share. The upside is that you also lose one group of
tankier monsters, since each league mechanic's tankiness only applies to its own monsters. If
you can handle the third one, slot it.

That's one pair over five maps, so treat it as a strong hint rather than a rule.

### Solo 10: the worst setup we measured

With the atlas passive that lifts the cap, you can put 10 Threads into a single league
mechanic. We ran five tier-16 maps with 10 Legion Threads and nothing else.

| Legion Threads       | Rarity | Tankiness | Legion juice rolls per map |
| -------------------- | :----: | :-------: | :------------------------: |
| 8 (in 8/8/8 maps)    | +125%  |   +700%   |            3.4             |
| 10 (solo)            | +160%  |  +1400%   |            2.0             |

In our small test, **Legion rolled less juice at 10 Threads than at 8**: 2.0 per map against
3.4. You pay double the tankiness for a little more rarity, and get _fewer_ Legion juice mods,
not more. One map at 10 rolled none at all. Inverted Legion, which rolled in 3 of 5 maps at
8, didn't roll once at 10.

And that's before counting what you give up by leaving two slots empty. A whole 8/8/8 map
rolled about 10 juice mods. A solo 10 map rolled about 2.

Keep the sample size in mind: five maps on each side, all of them Legion, and neither number
can count the Additional Legion mod (see Legion's extra spawns below). The single 10-Abyss map from the level ladder
rolled 5 Abyss juice mods, so 10 Threads may not cap juice for everything. But nothing we've
seen makes solo 10 worth it.

### Mods that show up at higher Thread counts

As the Thread count went up, mods we'd never seen before started rolling.

**First seen at 6** (none in any 3/3/3 map):

- **Ultimatum:** Catalyst Only, Trialmaster, Double Down, Oversouls
- **Breach:** Guaranteed Fortress, Rare Monsters with Breach mods
- **Legion:** Small Crystals
- **Expedition:** Runic Rares
- **Bestiary:** Red Beast Invasion
- **Abyss:** Consort (also seen once at 10 Threads)

**First seen at 8** (none in any map at 3 or 6):

| League mechanic | Mod                           | What it does                                  |
| --------------- | ----------------------------- | --------------------------------------------- |
| Betrayal        | Fracture (3 of 5 maps)        | Veiled items drop with fractured veiled mods  |
| Betrayal        | Sculpture (3 of 5)            | A corpse sculpture spawns                     |
| Legion          | Inverted Legion (3 of 5)      | 50% chance of an inverted legion              |
| Legion          | Monsters Rank Higher (2 of 5) | 50% chance for legion monsters to rank up     |
| Blight          | Free Towers (3 of 5)          | Towers cost nothing                           |
| Blight          | Pantheon (1 of 5)             | The blight core is replaced by a pantheon god |
| Ritual          | Nameless (2 of 5)             | The ritual is Nameless                        |
| Breach          | Wombgift Rare Drops (1 of 5)  | Breach rares can drop an extra wombgift       |

Two mods show the trend especially clearly:

- **Abyss Mortars:** 0 of 5 Abyss maps at 3 Threads, 5 of 5 at 6.
- **Legion Small Crystals:** 0 of 5 Legion maps at 3, 2 of 5 at 6, 5 of 5 at 8.

Any single mod on these lists could still be bad luck. Each league mechanic only appeared in
about 5 maps per Thread count, and a mod that rolls once in ten maps can easily miss five in a
row. But 18 mods all showing up for the first time as the Thread count rose is a lot harder to
wave away. It looks like each mod has a Thread count it needs, or at least one where it
becomes much more common. We can't tell those two apart yet.

**Only 7 of the 70 have never shown up:** Bestiary Black Morrigan and Extra Harvest Beasts,
Blight GigaLane, Incursion Architects and Tempests, Expedition Special Remnants and Legion
Instant Breakout. Every league mechanic has now been run at 8, so these are more rare than the others, persumably. Although again, the total number of maps run is small ( about 20 per mechanic as of 16/11/2026 )

### The ones that came up most often

Across every map we ran:

| League mechanic | Mods that rolled most                                                                    |
| --------------- | ---------------------------------------------------------------------------------------- |
| Abyss           | Extra Abysses (16 of 20 maps), Mortars (11 of 20)                                        |
| Bestiary        | Extra Red Beasts (12 of 14), Azmeri Hulks (11 of 14)                                     |
| Betrayal        | Research Chest Clusters (11 of 15), Buffs (10 of 15)                                     |
| Blight          | Pustules, Supercharge (13 of 17 each), Exile Lane (10 of 17)                             |
| Breach          | Empowered Ailith Skills (8 of 18), Guaranteed Fortress and Spread Coffers (7 of 18 each) |
| Expedition      | Scale (11 of 15), Revive Obelisk (8 of 15)                                               |
| Incursion       | Flesh Merchant (15 of 19), Cursed Treasure (10 of 19)                                    |
| Legion          | Both Legions Have Generals (12 of 20), Small Crystals (10 of 20)                         |
| Ritual          | Wildwood Wisp (13 of 18), Tribute Boss (11 of 18)                                        |
| Ultimatum       | Hearts (7 of 14), Cursed Currency (6 of 14)                                              |

---

## What _doesn't_ matter

We ran all 45 possible league mechanic pairs, twice: once at 3/3/3 and once at 6/6/6. We were looking for combinations that do something
special together. **None did.** Every stat on every map traced back to the Threads, a juice
mod, the map's own affixes, an altar or the atlas tree. Abyss next to Breach behaves exactly
like Abyss next to Ritual.\*\*

The atlas tree doesn't change the Thread numbers either. 10 Abyss Threads without any Abyss
passives gave the same stats as 10 Legion Threads with Legion passives.

**Neither does map level.** The Thread numbers were identical at area level 77, 78, 82 and 83.
What the map level _does_ change is a separate hidden monster life bonus (+55% at 77, +61% at
78, +98% at 82, +109% at 83). That's the map's own scaling, and it stacks on top of whatever the
Threads add. Map affixes don't change it.

**And juice doesn't need a juiced map.** Maps with no affixes, lower tiers and special maps
all rolled juice just as well, with values in their normal ranges.

That's two maps per pair now, so a small pair effect could still be hiding. But nothing big is.

\*\* _There are in-game interactions that are not tied to modifiers, such as the "Blighted Strongbox", among others, our findings are just related to what was readable in the game's process memory and data files_

## Legion's extra spawns

| Legion Threads | Extra spawns seen |
| :------------: | ----------------- |
|       3        | 2, 2, 2, 3, 3     |
|       6        | 1, 2, 3, 4, 4, 4  |
|       8        | 3, 3, 3, 4, 4     |
|       10       | 4, 4, 4, 4, 4, 5  |

The extra legions come from the **Additional Legion** juice mod, which adds one legion per
roll. As the Thread count goes up, the number of juice mods goes up with it, and Additional
Legion looks like the one Legion rolls most often: by 8 and 10 Threads, every map had at least
3 extra legions. That would mean it rolls more than once per map. We haven't been able to
confirm that, though, because the Threads add to the same stat.

Our detection can't count Additional Legion rolls directly above 3 Threads, which is why it
doesn't appear in the "most common" table above and why Legion's juice numbers are an
undercount.

---

## A side note on the "per Thread type" passive

The 6/6/6 and 8/8/8 maps were run with a new atlas passive that adds 5% map modifier effect
per different Thread type: +15% with three league mechanics, +10% with two, +5% with one. It doesn't seem to
touch juice: research chest clusters still landed inside their normal single-roll range.

---

## What's still open

1. **How much is a juice mod worth?** We can count them, but whether 10 juice mods at 8/8/8
   beat 6 at 3/3/3 once you factor in the extra clear time depends on your build and which mods
   you get.
2. **Do mods really unlock at a Thread count, or just get more common?** More maps at 3 and 6
   would tell the difference.
3. **Legion above 3.** We need more maps to pin down how its extra spawns roll.
4. **Does solo 10 starve every league mechanic, or just Legion?** One 10-Abyss map rolled 5
   juice mods. A few more solo 10 maps on other league mechanics would tell.

Until then: **3/3/3 for the best rarity per point of tankiness, 6/6/6 or 8/8/8 for more juice
if your build can take it, always fill all three slots, and skip solo 10.**

---

## The raw data

Everything above comes from the research notes in [`findings/`](findings/). That's where to
look for the per-map numbers, how each juice mod was detected, the full juice tables, and the
map log and analyzer if you want to check our work.
