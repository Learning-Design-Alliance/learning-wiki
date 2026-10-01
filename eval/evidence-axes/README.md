# Evidence axes — pilot (2026-09-30)

A claim says "worked examples help novices". A design needs to know more: for *these* learners,
working on a goal of *this* kind, under *these* conditions, what does changing one design variable do
to each outcome, and how sure is that? This pilot codes the evidence behind the ten pages with
`## Design Decisions` as **cells** and renders them as a map a designer can reason with.

    ΔO = f(L, G, C, do(D))      L learners · G goal properties · C conditions · D design variable · O outcome

`do(D)` is the point of the `design` field: a randomised or within-subject result, or a synthesis of
experiments, says what *changing* D does; a correlational or non-random result says what goes with it.

## Files

- The closed vocabularies are in `evidence-dimensions.json` at the wiki root, shared with the impact comparison record and the principle–pattern affordances, read through `scripts/evidence_dimensions.py`. `?` always means "the study's text available here does not say".
- `profiles/S1.json` … — a designer's learners, goal and conditions on the same dimensions, plus the outcomes aimed at.
- `scripts/code_evidence_axes.py` — codes each evidence entry into up to four cells, from the study's own
  text (fetched article, else OpenAlex abstract, else the entry, flagged). Runs go to
  `eval/runs/evidence-axes/<run>.ndjson` (ignored); `cells` is the store, the others are re-codings for
  agreement checks. **Every batch adds to it** (`run_scrape_batch.py`, after kind and rigour: `--new --code`,
  then `--contrasts`), as a call separate from extraction, about $0.0025 an entry.
- `scripts/render_evidence_map.py <page> --profile profiles/S1.json` — the map.
- `pilot/` — the maps rendered for the pilot.

## Rules the coding keeps

- **Blank is not zero.** `0` needs an equivalence test or reported power; a non-significant result without it
  is `ns`, inconclusive. A result nobody tested is a dot in the map.
- **Every cell quotes the study for its direction**, and the quote is checked against the text (letters and
  digits only, so PDF line breaks do not fail it), the whole article and not the 30,000 characters the coder
  is shown: the entry carries its own verbatim quote, often from a Results section past that cut, and the
  coder reuses it. Checking the cut text had wrongly failed 35 of the pilot's 528 cells. A cell whose quote is not in the text is kept in the record
  and left out of the map.
- **A learner difference is not a design variable.** "High vs low achievers" is coded `learner-difference`
  so it is not lost, and the map shows it as such.
- **Where the coder could not read the design**, the map uses the entry's recorded kind (`causal` →
  experimental, marked with `?` in the record), never a guess.

## Why a map and not a score

An `argmax` over designs would need three things the evidence cannot supply yet: comparable effect sizes
(most entries are `i?`), a weight for each outcome (retention against time is the designer's choice, not the
evidence's), and a judgement of how far a study's learners are from the designer's (extrapolation). So the
map gives a person the inputs to that calculation in the shape a person can run it:

- **one table per design decision**, options as rows and outcomes as columns, the outcomes the designer aims
  at starred — a trade-off shows as `+` in one column and `-` in another, and is never summed away;
- **four signals per cell, kept apart**: status (◆ known · ◇ extrapolated · △ associational · ◌ hypothesized),
  the directions found, the impact bin, and how many results are experimental;
- **fit to the designer's learners, one mark per result** (● match, ◎ matches where reported but mostly
  unreported, ◐ one axis differs, ○ two or more, ? none reported) — the extrapolation judgement stays with the
  reader, who can see which results are near their learners;
- **who was studied**, under each table, including how often each axis was not reported;
- **no ranking**: rows are ordered by how much evidence they have, not by how good they look.
