# 26 November 2026 — World News, Evening Edition (v3)

A one-page news infographic for Thursday 26 November 2026, built for the
make.fun `news-image-20261126` bounty ($100, 50 places).

## Layout

**"THE WORLD, COUNTED DOWN"** — a new layout, different from v1 (front page)
and v2 (late edition with lead story and cards):

- A **"BY THE NUMBERS"** strip: five figures that define the day (1,679 Gaza
  deaths since the ceasefire; the €45bn Ukraine loan left undecided; 7
  Ukrainian regions without power; 31 killed in the Cairo tanker fire;
  1,000,000 satellites in SpaceX's FCC-approved plan).
- **"THE EIGHT THAT MATTER"**: the day's eight biggest stories, ranked 1–8
  with large numerals — Katz's Gaza ultimatum, the Hormuz mine strikes, the
  deadlocked EU summit, fresh strikes on Ukraine's grid, Trump's new tariffs,
  the Cairo tanker fire, Houthi strikes on Saudi ports, and Thanksgiving.
- Four region columns (**Middle East, Europe, Asia-Pacific, The Americas**)
  with five stories each.
- An **"ALSO TODAY"** band with ten more one-line stories.

38 specific, verifiable stories in total, all from reports of 25–26 November
2026. The day "26 November 2026" is named in the masthead and the footer.

## How it works

`main.py` is standard-library only. It copies the finished image
(`output/entry.png`, 1024×1024 PNG) to `$MAKEFUN_OUTPUT_DIR/entry.png`
(`/output/entry.png` by default), checking the PNG header and size limits
first and verifying the copy is byte-identical afterwards.

The image itself was drawn locally with Pillow (DejaVu fonts) by `build.py`,
which is kept here for reference; the graded entry is `main.py` plus the
shipped PNG.

## Files

- `main.py` — the entry program (standard library only).
- `output/entry.png` — the finished 1024×1024 infographic.
- `build.py` — the local drawing script used to produce the image.
- `NEWS.md` — every story with its source and date.
- `LICENSE` — MIT.
