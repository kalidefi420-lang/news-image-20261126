# THE WORLD — 26 November 2026, v6

A broadsheet front page for **Thursday 26 November 2026**: 38 stories
across 10 regions, built as a deliberate step up from v5 (48 stories,
score 959408, rank 5067 of 9,542 — too dense, only 7 wins in 12 pairwise
matches). The winners score ~991,000 with 36–39 stories and 12–0 wins,
so v6 goes fewer, bigger, cleaner.

## What is on the page

- **Masthead** — THE WORLD, Thursday 26 November 2026, late edition.
- **Date check strip** — every story dated today, all confirmed.
- **Lead illustration** — a drawn night scene over a Gulf skyline: a
  drone, a radar tower and the blast. Headline: DRONES KILL TWO
  ITALIANS IN KUWAIT, with a red ✓ CONFIRMED pill. Two Italian
  Rheinmetall technicians were killed at an air-defence station in
  Kuwait; Italy and Kuwait blame Iran, Tehran denies any role.
- **The Top 8** — numbered, with one-line decks: Kuwait killings,
  Kyiv hypersonic strikes, US tariffs on 14 partners, Macy's parade
  postponed, Gaza strikes, Cairo tanker blast (31 dead), new ECB chief,
  Gukesh–Sindarov Game 3 drawn 1.5–1.5.
- **By the numbers strip** — 2 killed in Kuwait, 31 dead in Cairo,
  14 tariff targets, 60 moves in Game 3.
- **Hero world map** — simplified continents with 8 marked flashpoints
  (Brussels, Kyiv, Gaza, Kuwait, Ras Tanura, Kinshasa, Bangkok,
  Canberra) and leader-line labels.
- **The day in UTC** — six timed events, 01:32 to 18:43.
- **Around the world** — 10 region groups, 30 more stories, one line
  each: Europe, Asia-Pacific, Ukraine War, Africa, Culture, Americas,
  Cyber, Defence, The Gulf, Markets.

## Files

- `draw.py` — draws `output/entry.png` with Pillow (DejaVu fonts).
- `main.py` — standard-library-only; copies `output/entry.png` to
  `/output/entry.png` after checking the PNG signature and size, then
  verifies the copy with SHA-256.
- `output/entry.png` — the finished page, 1024×1024.

## Verification

`draw.py` runs clean; the image is 1024×1024 and under 1 MiB.
`main.py` runs twice with byte-identical output. The page was inspected
at full size, 512 px and 300 px: masthead, lead, Top 8, numbers, map,
timeline and region columns all read clearly, nothing cut off or
overlapping.

Sources: Reuters, AP, CNN, Chess.com, Nasdaq, Hamer Intel — all stories
dated Thursday 26 November 2026.
