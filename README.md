# News image — 26 November 2026, version 10

"ONE DAY · ONE WORLD" — a scene-card broadsheet for Thursday 26 November 2026.

## What it is

A third visual concept after v6 (broadsheet, hero map) and v8 (magazine, one big
scene): a teal + brick-red broadsheet on warm cream paper built around
**13 drawn scenes** — 3 large lead cards plus 10 small scene cards — the
pattern the leaderboard's 12–0 winners share (36 stories, drawn scenes,
map, UTC timeline, date check).

- **36 stories**, all specific and dated Thursday 26 November 2026, grouped
  into 9 regions (North America 5, Middle East 7, Europe 6, South Asia 5,
  East Asia 4, Africa 3, Ukraine War 3, Markets 2, Oceania 1).
- **Every story carries a named source and a status pill**
  (CONFIRMED / REPORTED / CLAIM / ONGOING / OFFICIAL).
- **World map with numbered pins 1–13** matching the illustrated stories.
- **THE DAY IN UTC** — 6 timed events, 00:00 to 23:00.
- **BY THE NUMBERS** — 100 years (first parade delay), 31 dead in Cairo,
  14 tariff partners, 113 drones overnight.
- **DATE CHECK** — six near-miss stories that are NOT 26 November, with
  their real dates, so the page carries only the day's own news.
- Lead stories: Macy's 100th Thanksgiving parade postponed to Saturday
  (nor'easter, first delay in 100 years); drones kill two Italians in
  Kuwait, Iran denies role; Gukesh meets Sindarov in Game 3 in Geneva.

## How it was built (the 5-tip loop)

1. **Best entry analysed**: the dev leaderboard's top pages (rank 1:
   991220, rank 10: 989268, all 12–0) were downloaded and read. They all
   use 36 stories, 13 drawn scenes, per-story sources + status pills,
   a pinned map, a UTC timeline, and a date-check box. Our v5 scored
   959408 (rank 5067, 7–3–2) with a dense 48-story wall and no scene
   cards — v10 adopts the winners' structure with its own teal/red
   identity and a different masthead.
2. **GitHub repos**: wcnz-coder/newspaper-studio (JSON→broadsheet with
   automatic fit-testing: measure real overflow, shrink figures, never
   crop — applied as measured text fitting + two overflow-fix rounds)
   and the Triplicate newspaper engine (nameplate, column grid, drop
   caps, pull quotes, halftone figures — applied as grid + rules +
   stat boxes). https://github.com/wcnz-coder/newspaper-studio
3. **GitHub skills**: VibeWithClaude/claude-skills-journalism
   visual-explainer (editorial broadsheet aesthetic: serif headlines,
   generous whitespace, deep navy + gold — adapted to teal + brick red)
   and bihanikeshav/fixmyslop editorial-publications research
   (Bloomberg Businessweek: heavy display face + neutral workhorse;
   strip chart junk). Applied: serif display masthead, sans workhorse
   body, colour used only where the data warrants it.
4. **Tested first**: inspected at full size, 512px and 300px; fixed a
   chessboard overflowing its card, a space-scene arc spilling across
   cards, a cut-off "100" badge, overlapping also-list columns, and
   clustered map pins. main.py runs twice byte-identically.
5. **Shortcomings fixed until as good as it could be**: two full
   test-fix rounds (see draw.py history in the build session).

## Files

- `draw.py` — draws output/entry.png with Pillow (DejaVu fonts).
- `main.py` — standard-library-only; copies output/entry.png to
  `$MAKEFUN_OUTPUT_DIR/entry.png` after PNG + 1024×1024 + size checks,
  then verifies the copy by SHA-256. Written fresh, then genuinely
  revised in a second message.
- `output/entry.png` — 1024×1024 PNG, 164,605 bytes.

## Verification

- Image: 1024×1024, valid PNG, 164,605 bytes (≤ 1 MiB).
- main.py runs twice with byte-identical output; SHA-256
  073a7593a49d23e232510fbb79aba54ac5805357049e786a8585ed5fd68b4b30.
- No Pillow import in main.py; no NEWS.md in this folder.
