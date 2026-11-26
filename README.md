# Thursday 26 November 2026 — world news in one image (v2)

A second, stronger variant of the 26 November 2026 news image entry.

## The image

`output/entry.png` — 1024×1024, a newspaper front page, "THE WORLD IN ONE
PAGE", dated THURSDAY 26 NOVEMBER 2026, with 39 stories:

- **Lead:** the Board of Peace warns the UN Security Council that the Gaza
  truce is "on the brink of collapse" — a report published at 00:01 UTC on
  26 November, the freshest story of the day.
- **Markets strip:** the day's closing numbers (Dow +0.33%, Nasdaq −0.62%,
  S&P 500 −0.25%, Brent $90.05, WTI $80.70).
- **Three top cards:** Trump's new tariffs on 14 partners, the Hormuz
  tanker mine attacks, and Russia's overnight strikes on Ukraine's energy
  grid.
- **Three columns:** War & diplomacy, The Americas, Science & life.
- **In brief:** 14 more stories, from the Shanghai graft probe to the
  Cairo tanker fire.

How it differs from v1: v1 led with the tariffs and had 27 stories in two
columns. This version leads with the Gaza Board of Peace warning, carries
39 stories (12 more), adds a markets data strip, uses three columns instead
of two, and reports the markets' final closes (the Dow actually ended
higher after the intraday rout) rather than the midday plunge.

## How it runs

`main.py` is standard-library-only. It copies the pre-built
`output/entry.png` to `/output/entry.png` — the grading container installs
nothing, so the program must not import any third-party package. Run it
twice and the output is byte-identical to the source image.

## Sources

See `NEWS.md` for the full story list with sources (Reuters, AP, Al
Jazeera, Sharecast, ESA/JAXA, and others).
