---
type: claim
title: "Expected OPIs are significantly biased less often than hard-boundary OPIs when annotations are noisy (49.37% vs 56.63% of steps)"
description: "Expected OPIs are significantly biased less often than hard-boundary OPIs when annotations are noisy (49.37% vs 56.63% of steps)"
id: expected-opis-biased-less-often-than-hard-boundary
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: li-ye-2026
    resource: "https://doi.org/10.1371/journal.pone.0355276"
    title: "Li Ye, Kamabattula Sreeram, Bhattacharyya Kiran, Berniker Max. (2026). Validation of expected objective performance indicators in surgical data analysis. PLoS One. https://doi.org/10.1371/journal.pone.0355276"
    author: Li Ye, Kamabattula Sreeram, Bhattacharyya Kiran, Berniker Max
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Expected OPIs are significantly biased less often than hard-boundary OPIs when annotations are noisy (49.37% vs 56.63% of steps)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across five OPIs and seven procedure types, a smaller percentage of expected OPI sample means were significantly distinct from nominal values (49.37%) than hard-boundary OPI sample means (56.63%). [→ Li Ye 2026](#li-ye-2026)

## Evidence

### Li Ye 2026

Li Ye, Kamabattula Sreeram, Bhattacharyya Kiran, Berniker Max. (2026). Validation of expected objective performance indicators in surgical data analysis. PLoS One. https://doi.org/10.1371/journal.pone.0355276

`q2 · i?` · `design · r2`

Retrospective analysis of 1,016 da Vinci Xi cases across seven procedure types; for each of 5,408 single-instance steps, 500 start/stop pairs were resampled and one-sample t-tests compared sampled means to nominal values. The expected OPIs were "more often indistinguishable from their nominal values" than hard-boundary OPIs.

> "Averaging across the five OPIs and seven procedure types, the percentage of steps whose sample means were significantly distinct from their nominal OPI values were 56.63% and 49.37%, for the hard-boundary and expected OPIs, respectively."

## Discussion


## Related Claims
- [Expected OPI bias magnitudes are smaller than hard-boundary bias in every procedure-type-by-OPI comparison, significant in all but three scenarios](expected-opi-bias-magnitudes-smaller.md) — related
- [Normalized standard deviations of expected OPIs are significantly smaller than hard-boundary OPIs in all procedure-type-by-OPI conditions](expected-opi-standard-deviations-significantly-smaller.md) — related
- [Expected OPIs are less variable under annotator noise: 40.56% of steps showed larger hard-boundary variance versus 8.52% with larger expected variance](expected-opis-less-variable-annotator-noise.md) — related
- [For kinematic OPIs (tool path length and angular path length), expected OPIs show a consistent and substantial accuracy improvement across procedure types](kinematic-opis-accuracy-improvement-expected-method.md) — a narrower finding that bears on this claim
