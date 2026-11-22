---
type: claim
title: "Expected OPIs are less variable under annotator noise: 40.56% of steps showed larger hard-boundary variance versus 8.52% with larger expected variance"
description: "Expected OPIs are less variable under annotator noise: 40.56% of steps showed larger hard-boundary variance versus 8.52% with larger expected variance"
id: expected-opis-less-variable-annotator-noise
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: mixed
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
  - id: li-ye-2026-2
    resource: "https://doi.org/10.1371/journal.pone.0355276"
    title: "Li Ye, Kamabattula Sreeram, Bhattacharyya Kiran, Berniker Max. (2026). Validation of expected objective performance indicators in surgical data analysis. PLoS One. https://doi.org/10.1371/journal.pone.0355276"
    author: Li Ye, Kamabattula Sreeram, Bhattacharyya Kiran, Berniker Max
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Expected OPIs are less variable under annotator noise: 40.56% of steps showed larger hard-boundary variance versus 8.52% with larger expected variance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A weighted average across OPIs and procedure types found 40.56% of steps had larger hard-boundary variance while only 8.52% had larger expected variance. [→ Li Ye 2026](#li-ye-2026)
`q2 i?` Angular path length was an exception, with a moderate share of steps showing larger expected OPI variance (23.30%) than hard-boundary variance (20.28%). [→ Li Ye 2026 (2)](#li-ye-2026-2)

## Evidence

### Li Ye 2026

Li Ye, Kamabattula Sreeram, Bhattacharyya Kiran, Berniker Max. (2026). Validation of expected objective performance indicators in surgical data analysis. PLoS One. https://doi.org/10.1371/journal.pone.0355276

`q2 · i?` · `design · r2`

Robustness analysis comparing sample variances of resampled hard-boundary and expected OPI values with Levene's test across seven procedure types and five OPIs; the probabilistic approach was superior when averaging across the five OPIs.

> "a weighted average (taking into account the differing steps per procedure) across OPIs and procedure types found that 40.56% of the steps had larger hard-boundary variance, whereas only 8.52% of the steps had larger expected variances."

### Li Ye 2026 (2)

Li Ye, Kamabattula Sreeram, Bhattacharyya Kiran, Berniker Max. (2026). Validation of expected objective performance indicators in surgical data analysis. PLoS One. https://doi.org/10.1371/journal.pone.0355276

`q2 · i?` · `design · r2`

Levene's test comparison for the angular path length OPI alone, where the variance advantage of the probabilistic method did not hold; the article reports this exception explicitly in the Results.

> "Angular path length was the exception, where there were a moderate amount of steps with larger expected OPI variance (23.30% of steps, relative to 20.28% of the steps with the hard-boundary approach)."

## Discussion


## Related Claims
- [Expected OPI bias magnitudes are smaller than hard-boundary bias in every procedure-type-by-OPI comparison, significant in all but three scenarios](expected-opi-bias-magnitudes-smaller.md) — related
- [Normalized standard deviations of expected OPIs are significantly smaller than hard-boundary OPIs in all procedure-type-by-OPI conditions](expected-opi-standard-deviations-significantly-smaller.md) — related
- [Expected OPIs are significantly biased less often than hard-boundary OPIs when annotations are noisy (49.37% vs 56.63% of steps)](expected-opis-biased-less-often-than-hard-boundary.md) — related
- [For kinematic OPIs (tool path length and angular path length), expected OPIs show a consistent and substantial accuracy improvement across procedure types](kinematic-opis-accuracy-improvement-expected-method.md) — related
