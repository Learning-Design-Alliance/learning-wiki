---
type: claim
title: DC estimates tend to be lowest when the cut score is set at the peak of the score distribution, where inconsistent decisions are most likely
description: DC estimates tend to be lowest when the cut score is set at the peak of the score distribution, where inconsistent decisions are most likely
id: dc-lowest-at-score-distribution-peak
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
evidence_strength: moderate
sources:
  - id: wolkowitz-2024
    resource: "https://pareonline.net/getvn.asp?v=29&n=6"
    title: "Wolkowitz, A. A., & Smith, R. (2024). A Practical Comparison of Decision Consistency Estimates. Practical Assessment, Research & Evaluation, 29(6). https://pareonline.net/getvn.asp?v=29&n=6"
    author: "Wolkowitz, A. A., & Smith, R."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DC estimates tend to be lowest when the cut score is set at the peak of the score distribution, where inconsistent decisions are most likely

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Evidence quality** · No study behind this claim is a peer-reviewed article with a DOI: it rests on a source with no registered publication record (a web page, book or unpublished report). It is kept because 2 design pages cite it; treat it as a lead to check, not an established finding.

## Subclaims
`q2 i?` DC values tend to be lowest at the peak of a score distribution because that is where the chance of an inconsistent decision is highest. [→ Wolkowitz 2024](#wolkowitz-2024)

## Evidence

### Wolkowitz 2024

Wolkowitz, A. A., & Smith, R. (2024). A Practical Comparison of Decision Consistency Estimates. Practical Assessment, Research & Evaluation, 29(6). https://pareonline.net/getvn.asp?v=29&n=6

`q2 · i?` · `design · r2`

Observed in the Sim 1 results (Figure 2 and Table 7), where the lowest DC estimate for all three methods occurred at the mode (cut score of 100). The article explains that a high density of scores at or near the cut score increases possible inconsistent decisions.

> "This is an expected result since the DC values tend to be the lowest at the peak of a score distribution because this is the location of the highest chance of an inconsistent decision."

## Studies bearing on this claim

<!-- synthesis:start -->
*How far can a pass/fail or grade decision near a cut score be trusted, and how should its consistency be reported?* This table gathers the studies behind this claim and the 3 narrower claims that bear on it: **3 distinct studies** (1 design, 1 theoretical, 1 review), `q1`–`q2`, 0 of 3 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| Wolkowitz 2024 | q1 / q2 · design · r2 | i? | this claim; [Cohen's kappa exhibits a paradox in which high observed agreement yields low kappa, making](cohens-kappa-paradox-decision-consistency.md) (qualifies) |
| Gentile 1971 | q1 · theoretical · r1 | i? | [Grade cutoffs are arbitrary because adjacent scores receiving different grades are not sig](grade-cutoffs-arbitrary-adjacent-scores.md) (supports) |
| May 2009 | q2 · review · r2 | i? | [Reliability of state test scores is highest near cut-scores or the mean and much lower for](conditional-reliability-low-at-score-tails.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

## Related Claims

- [Criterion-referenced tests require empirically-based construct validation studies](criterion-referenced-tests-need-construct-validation.md) — the general claim this finding bears on, with the studies behind it
- [The greatest differences among the three DC estimates occur when the cut score is set at the mode of a skewed score distribution](dc-estimate-differences-largest-at-mode.md) — a narrower finding that bears on this claim
- [For skewed datasets, W-DC and LL-DC produce similar and preferred estimates, while PS-DC diverges at high-frequency scores](dc-methods-skewed-data-w-dc-ll-dc-preferred.md) — related
- [The LL-DC, PS-DC, and W-DC methods produce similar decision consistency estimates (within 0.044) for normally or close to normally distributed datasets](dc-methods-similar-normal-distributions.md) — related
- [Cohen's kappa exhibits a paradox in which high observed agreement yields low kappa, making it unsuitable for pass/fail decision consistency](cohens-kappa-paradox-decision-consistency.md) — related
- [Reliability of state test scores is highest near cut-scores or the mean and much lower for very high- or low-performing students](conditional-reliability-low-at-score-tails.md) — related
- [Measurement precision is strongest for students in the middle of the Spanish score distribution, with CSEM near the 3.3 RIT target](spanish-csem-middle-deciles-most-precise.md) — related
