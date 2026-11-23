---
type: claim
title: Learning effects model estimates were robust to missing experience data and to overly influential observations from sparse peripheral experience regions
description: Learning effects model estimates were robust to missing experience data and to overly influential observations from sparse peripheral experience regions
id: rolarr-learning-model-robustness-checks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: corrigan-neil-2018
    resource: "https://doi.org/10.1186/s13063-018-2726-0"
    title: "Corrigan Neil, Marshall Helen, Croft Julie, Copeland Joanne, Jayne David, Brown Julia. (2018). Exploring and adjusting for potential learning effects in ROLARR: a randomised controlled trial comparing robotic-assisted vs. standard laparoscopic surgery for rectal cancer resection. Trials. https://doi.org/10.1186/s13063-018-2726-0"
    author: Corrigan Neil, Marshall Helen, Croft Julie, Copeland Joanne, Jayne David, Brown Julia
    q: 2
    i: "?"
    kind: causal
    rigour: 3
  - id: corrigan-neil-2018-2
    resource: "https://doi.org/10.1186/s13063-018-2726-0"
    title: "Corrigan Neil, Marshall Helen, Croft Julie, Copeland Joanne, Jayne David, Brown Julia. (2018). Exploring and adjusting for potential learning effects in ROLARR: a randomised controlled trial comparing robotic-assisted vs. standard laparoscopic surgery for rectal cancer resection. Trials. https://doi.org/10.1186/s13063-018-2726-0"
    author: Corrigan Neil, Marshall Helen, Croft Julie, Copeland Joanne, Jayne David, Brown Julia
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Learning effects model estimates were robust to missing experience data and to overly influential observations from sparse peripheral experience regions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2`–`r3` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Re-fitting the model 625 times under imputed experience values for two patients with missing data yielded estimates not notably different from the original model. [→ Corrigan Neil 2018](#corrigan-neil-2018)
`q2 i?` A model restricted to patients within the lower quartiles of surgeon experience yielded very similar estimates to the full model, addressing concern about influential observations in sparse data regions. [→ Corrigan Neil 2018 (2)](#corrigan-neil-2018-2)

## Evidence

### Corrigan Neil 2018

Corrigan Neil, Marshall Helen, Croft Julie, Copeland Joanne, Jayne David, Brown Julia. (2018). Exploring and adjusting for potential learning effects in ROLARR: a randomised controlled trial comparing robotic-assisted vs. standard laparoscopic surgery for rectal cancer resection. Trials. https://doi.org/10.1186/s13063-018-2726-0

`q2 · i?` · `causal · r3`

Brute-force missing-data sensitivity analysis of the ROLARR learning effects model, re-fitting under all combinations of imputed experience values. The article reports that "None of the re-fitted models yielded estimates that were notably different"; no effect size is printed.

> "In total this was done 625 times to cover all possible combinations of number of previous laparoscopic operations in {10, 45, 91, 180, 500} and number of previous robotic operations in {10, 30, 50, 101, 183} for each patient. None of the re-fitted models yielded estimates that were notably different to the model which excluded these two patients."

### Corrigan Neil 2018 (2)

Corrigan Neil, Marshall Helen, Croft Julie, Copeland Joanne, Jayne David, Brown Julia. (2018). Exploring and adjusting for potential learning effects in ROLARR: a randomised controlled trial comparing robotic-assisted vs. standard laparoscopic surgery for rectal cancer resection. Trials. https://doi.org/10.1186/s13063-018-2726-0

`q2 · i?` · `causal · r2`

Influence diagnostics for the ROLARR learning effects model identified overly influential observations at experience extremities; the article reports the quartile-restricted refit "yielded very similar estimates". No effect size is printed for this robustness finding.

> "This limited model yielded very similar estimates. The estimated relationships of robotic experience vs. treatment effect and laparoscopic experience vs. treatment effect from this re-fitted model are presented in Figs. 6 and 7, and are clearly very similar to the relationships seen from the full model in Figs. 4 and 5."

## Discussion


## Related Claims
- [Imputing missing predictor values without conditioning on the outcome variable biases estimates toward zero even when data are missing completely at random](imputation-omitting-outcome-biases-toward-zero.md) — related
- [The competency-rating–prescribing association is consistent across sensitivity analyses using raw ratings, individual domains, imputed counts, and inverse-probability weighting](sensitivity-analyses-competency-prescribing-robust.md) — related
- [The game-based learning treatment effects remain statistically significant under worst-case attrition imputation scenarios](gbl-effects-robust-to-attrition.md) — related
