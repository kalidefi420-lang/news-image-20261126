# THE WORLD — Thursday 26 November 2026 (version 8)

Magazine-style front page, a radical redesign after v6 (38 stories,
rank pending) and v5 (score 959408, rank 5067 of 9,542 — the top
entries score ~991,000 with 36–39 stories and 12–0 pairwise wins).

## What's different from v6

- **One dominant drawn scene** takes the whole top half: Kuwait City
  at night — skyline, Kuwait Towers, a radar tower, drones with red
  trails, and the explosion glow at the air-defence site. Not a small
  box, but the page's hero.
- **36 stories** (v6 had 38, v5 had 48) — fewer, bigger, cleaner.
- **Top 6** instead of Top 8, with one-line decks.
- **Very large type everywhere** — the masthead, the giant lead
  headline ("DRONES KILL TWO ITALIANS IN KUWAIT", with a red
  ✓ CONFIRMED pill), the numbers strip, and the section headers are
  all readable at 300 px at a glance. Lots of white space, nothing
  crowded.
- 8 region groups (The Gulf, Europe, Ukraine War, Asia-Pacific,
  Africa, Americas, Markets & Tech, Culture & Sport) plus an Also
  Today box, a "THE DAY IN UTC" timeline (6 timed events, 01:32–
  19:45), and a compact world-map strip with the day's flashpoints.

## Stories

All 36 stories are specific and dated 26 November 2026, researched
fresh via web search this session. Lead: Iranian drones kill two
Italian Rheinmetall technicians at a Kuwait air-defence site (Italy
and Kuwait blame Iran; Tehran denies). Also: Cairo Ring Road tanker
blast (31 dead), Kyiv shopping-centre strike (7 hurt), US tariffs on
14 economies, Gaza strikes kill a Hamas deputy minister, IRGC mine
claim on a supertanker, Congo Ebola past 12,021 cases, Macy's parade
postponed for the first time in 100 years.

## Files

- `draw.py` — draws `output/entry.png` locally with Pillow
  (deterministic, fixed random seed).
- `main.py` — standard-library-only; copies `output/entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`, checks the PNG signature and
  1024×1024 size, verifies the copy with SHA-256.
- `output/entry.png` — 1024×1024 PNG, 149,020 bytes.

## Verification

`main.py` was run twice with different output directories; both
outputs are byte-identical to each other and to `output/entry.png`.
