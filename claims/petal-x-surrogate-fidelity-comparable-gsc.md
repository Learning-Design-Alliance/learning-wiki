---
type: claim
title: The linear-regression surrogate of SCORE2 and its Petal-X approximation achieve fidelity comparable to or slightly higher than SCORE2 graphical score charts
description: The linear-regression surrogate of SCORE2 and its Petal-X approximation achieve fidelity comparable to or slightly higher than SCORE2 graphical score charts
id: petal-x-surrogate-fidelity-comparable-gsc
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: diego-rojo-2024
    resource: "https://doi.org/10.48550/arXiv.2406.18690"
    title: "Diego Rojo, Houda Lamqaddam, Lucija Gosak, and Katrien Verbert. (2024). Petal-X: Human-Centered Visual Explanations to Improve Cardiovascular Risk Communication. [doi:10.48550/arXiv.2406.18690](https://doi.org/10.48550/arXiv.2406.18690)"
    author: Diego Rojo, Houda Lamqaddam, Lucija Gosak, and Katrien Verbert
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: diego-rojo-2024-2
    resource: "https://doi.org/10.48550/arXiv.2406.18690"
    title: "Diego Rojo, Houda Lamqaddam, Lucija Gosak, and Katrien Verbert. (2024). Petal-X: Human-Centered Visual Explanations to Improve Cardiovascular Risk Communication. [doi:10.48550/arXiv.2406.18690](https://doi.org/10.48550/arXiv.2406.18690)"
    author: Diego Rojo, Houda Lamqaddam, Lucija Gosak, and Katrien Verbert
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# The linear-regression surrogate of SCORE2 and its Petal-X approximation achieve fidelity comparable to or slightly higher than SCORE2 graphical score charts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r?` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the Framingham-derived dataset, the male (Sp. Corr. = 0.969) and female (Sp. Corr. = 0.964) surrogate models slightly exceed the fidelity of the male (0.947) and female (0.949) SCORE2 graphical score charts. [→ Diego Rojo 2024](#diego-rojo-2024)
`q2 i?` The Petal-X coefficient approximations (N=10 male, N=11 female) retain Spearman correlations slightly higher than the GSCs, with no notable differences in R2, RMSE, or MAE. [→ Diego Rojo 2024 (2)](#diego-rojo-2024-2)

## Evidence

### Diego Rojo 2024

Diego Rojo, Houda Lamqaddam, Lucija Gosak, and Katrien Verbert. (2024). Petal-X: Human-Centered Visual Explanations to Improve Cardiovascular Risk Communication. [doi:10.48550/arXiv.2406.18690](https://doi.org/10.48550/arXiv.2406.18690)

`q2 · i?` · `design · r2`

Numerical validation on 1762 Framingham Heart Study individuals (713 male, 1049 female) comparing surrogate-model predictions to SCORE2 outputs using Spearman's correlation as the fidelity metric.

> "The results showed that the Spearman's correlation of our male (Sp. Corr. = 0.969) and female (Sp. Corr. = 0.964) linear regression global surrogate models is slightly higher than that of the male (Sp. Corr. = 0.947) and female (Sp. Corr. = 0.949) SCORE2 graphi- cal score chart."

### Diego Rojo 2024 (2)

Diego Rojo, Houda Lamqaddam, Lucija Gosak, and Katrien Verbert. (2024). Petal-X: Human-Centered Visual Explanations to Improve Cardiovascular Risk Communication. [doi:10.48550/arXiv.2406.18690](https://doi.org/10.48550/arXiv.2406.18690)

`q2 · i?` · `causal · r?`

Numerical comparison (Table 2) of Petal-X approximations against GSCs on the same dataset across four fidelity metrics: Spearman's correlation, R2, RMSE, and MAE.

> "The fidelity of the male and female linear regression surrogate models represented by Petal-X was deemed adequate, as their Spearman correlation is slightly higher than that of the SCORE2 graphical score charts for each sex, and there are no notable differences in any of the other fidelity metrics (see Table 2)."

## Discussion


## Related Claims
- [No statistically significant difference between Petal-X and graphical score charts in perceived transparency, trust, or intent to use, with Bayes factors favoring the null](petal-x-no-subjective-difference.md) — related
- [Healthcare students using Petal-X complete risk-factor contribution (T1) and what-if comparison (T2) tasks significantly faster than those using graphical score charts](petal-x-faster-contribution-whatif-tasks.md) — related
