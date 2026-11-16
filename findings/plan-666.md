# 6/6/6 plan

**Done on 2026-11-16.** The answers are in [results-666.md](results-666.md). The run changed two
of the controls below on purpose: most maps were at area level 77–78 rather than tier 16, and a
new atlas passive (map mod effect per Thread type) was allocated. This page is kept as written
before the run.

## Controls

- **Keep the atlas tree fixed and free of league content** for every map in the run. After
  `analyze.py` runs, check that `map_active_atlas_passive_tree_index` reads the same in every map.
- **Use the same map base** (Dunes) **at the same tier** (16), so the only thing that changes
  between maps is the Threads.
- **Make sure each map's log line is final.** Altars and monoliths change a map's stats
  part-way through, and the logger writes a new version each time. `analyze.py` uses the last
  version.
- **Check every map is logged.** The log's record count should go up after each map.

## Questions 6/6/6 can answer

1. **The stat set at 6 in a mix.** Is it 20 / 210 / 7000 for each league, the same as solo Legion
   at 6?
2. **What 6 Threads give a league on its own:**
   - Legion's extra spawns go from 2 to 4. Do the other leagues scale the same way?
   - Does Blight still get exactly 1 extra blight encounter?
   - Does Breach still get either the hive or extra unstable breaches?
3. **Do juice mods scale with Thread count?** Compare juice per map and per league against the
   3/3/3 figures of 4.6 per map and 0–4 per league. In particular, does Ultimatum still roll
   exactly one?
4. **Do the never-seen juice mods start appearing?** There are 28 of them, listed in
   [juice-mods.md](juice-mods.md).
5. **Can a juice mod roll more than once?** Look for stat values that are a whole number of
   rolls of one juice mod's range. The best evidence is a value no single roll can reach, like
   the 33 research chest clusters.
6. **Pair effects.** One more sample per pair either backs up the 3/3/3 finding of "no pair
   effect" or turns up something it missed.

## Tooling (ready)

- **Repeat rolls.** `analyze.py` counts how many times each juice mod rolled and shows repeats as
  `xk`.
- **Thread-only stats.** A new "Thread-only stats" section lists, for each league and Thread
  count, the stats that never appear without that league. Once a 6-Thread value is known for a
  stat a juice mod also uses, add it to `THREAD_BASE` in `analyze.py`. Legion's 6-Thread value is
  in already: 4 extra spawns.
- **Coverage goal.** `GOAL_SPLIT` is now 6, so `permutations.md` tracks pair coverage for 6/6/6.
  The current plan needs 17 maps.
