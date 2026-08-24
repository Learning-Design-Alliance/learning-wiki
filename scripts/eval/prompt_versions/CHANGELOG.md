# Extraction prompt changelog

Each version is the complete `SYSTEM_PROMPT` text used for a set of runs.
`eval_harness.py run --prompt-version vN` picks one explicitly; omitting the
flag uses the latest. Every result JSON records which version produced it,
so `eval_harness.py history` can show the trend across versions, and
`compare` can diff two runs on different versions directly.

## v1

Original prompt. Used for `do-batch-1`. Produced (see do-batch-1's failure
analysis): fabricated DOIs for sources that don't have one, near-duplicate
contributions (a single finding multiplied into matching principle/element/
pattern/strategy entries), evidence descriptions that dropped reported
statistics, and `CL001`-style ids missing the required hyphen.

## v2

Manually tightened in response to v1's do-batch-1 results:
- Explicit "many sources have no DOI, don't invent one" rule with a
  concrete example (conference papers), replacing the too-general "never
  hallucinate a citation" wording that wasn't preventing fabrication.
- Stronger anti-duplication guidance: one finding is usually one claim, not
  a bundle of contribution types restating it.
- Evidence descriptions must keep the article's actual reported numbers.
- Concrete right/wrong example for the `CL-<shortcode>` id format.
- Explicit "evidence_ref must never be null" rule.
- Closing self-check line pointing back at the highest-value rules.
