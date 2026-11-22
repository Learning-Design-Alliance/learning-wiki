---
type: claim
title: Expected OPI bias magnitudes are smaller than hard-boundary bias in every procedure-type-by-OPI comparison, significant in all but three scenarios
description: Expected OPI bias magnitudes are smaller than hard-boundary bias in every procedure-type-by-OPI comparison, significant in all but three scenarios
id: expected-opi-bias-magnitudes-smaller
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

# Expected OPI bias magnitudes are smaller than hard-boundary bias in every procedure-type-by-OPI comparison, significant in all but three scenarios

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Normalized percent biases of expected OPIs were smaller than hard-boundary counterparts in every example, and Wilcoxon signed-rank tests found the expected bias significantly smaller in all but three scenarios. [→ Li Ye 2026](#li-ye-2026)

## Evidence

### Li Ye 2026

Li Ye, Kamabattula Sreeram, Bhattacharyya Kiran, Berniker Max. (2026). Validation of expected objective performance indicators in surgical data analysis. PLoS One. https://doi.org/10.1371/journal.pone.0355276

`q2 · i?` · `design · r2`

Biases were computed as unsigned percentages of nominal OPI values and compared by Wilcoxon signed-rank test (Table 3); the article reports significance "in all but three scenarios", with p-values of 0.120, 0.301 and 0.344 for hand clutch rate in three procedure types.

> "As can be seen, the biases are all less than 10%, and the biases of the expected OPIs are smaller than their hard-boundary counterparts in every single example."

## Discussion


## Related Claims
- [Normalized standard deviations of expected OPIs are significantly smaller than hard-boundary OPIs in all procedure-type-by-OPI conditions](expected-opi-standard-deviations-significantly-smaller.md) — related
- [Expected OPIs are significantly biased less often than hard-boundary OPIs when annotations are noisy (49.37% vs 56.63% of steps)](expected-opis-biased-less-often-than-hard-boundary.md) — related
- [Expected OPIs are less variable under annotator noise: 40.56% of steps showed larger hard-boundary variance versus 8.52% with larger expected variance](expected-opis-less-variable-annotator-noise.md) — related
- [For kinematic OPIs (tool path length and angular path length), expected OPIs show a consistent and substantial accuracy improvement across procedure types](kinematic-opis-accuracy-improvement-expected-method.md) — related
