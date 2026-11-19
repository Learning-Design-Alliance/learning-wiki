---
type: claim
title: "Select reduces median empirical forgetting rate 48% below random selection and 40% below difficulty-based selection, with significant differences in 75% of comparisons"
description: "Select reduces median empirical forgetting rate 48% below random selection and 40% below difficulty-based selection, with significant differences in 75% of comparisons"
id: select-lower-forgetting-rate-than-difficulty-and-random
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: utkarsh-upadhyay-2021
    resource: "https://doi.org/10.1038/s41539-021-00105-8"
    title: "Utkarsh Upadhyay, Graham Lancashire, Christoph Moser, and Manuel Gomez-Rodriguez. (2021). Large-scale randomized experiment reveals machine learning helps people learn and remember more effectively. arXiv. Originally published 2020. [doi:10.1038/s41539-021-00105-8](https://doi.org/10.1038/s41539-021-00105-8)"
    author: Utkarsh Upadhyay, Graham Lancashire, Christoph Moser, and Manuel Gomez-Rodriguez
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Select reduces median empirical forgetting rate 48% below random selection and 40% below difficulty-based selection, with significant differences in 75% of comparisons

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` The median empirical forgetting rate of select-group learners is 48% lower than random-group learners and 40% lower than difficulty-group learners, with statistically significant decreases in 75% of cases. [→ Utkarsh Upadhyay 2021](#utkarsh-upadhyay-2021)

## Evidence

### Utkarsh Upadhyay 2021

Utkarsh Upadhyay, Graham Lancashire, Christoph Moser, and Manuel Gomez-Rodriguez. (2021). Large-scale randomized experiment reveals machine learning helps people learn and remember more effectively. arXiv. Originally published 2020. [doi:10.1038/s41539-021-00105-8](https://doi.org/10.1038/s41539-021-00105-8)

`q3 · i?` · `causal · r2`

Comparison of normalized empirical forgetting rate across the three randomized groups, grouped by number of reviews and retention interval (Figure 1), tested with the Matt-Whitney U-test at p-value = 0.05. The article states the forgetting rate for the select group is lower "in 83.5% of the cases". No standardized effect size is printed.

> "The results show that, in 83.5% of the cases, the empirical forgetting rate for the learners in the 'select' group is lower than that of the learners in the 'diﬃculty' and 'random' groups and, in 75% of cases, the decrease is statistically significant."

## Discussion


## Related Claims
- [ML-based question selection (SELECT) lowers learners' normalized empirical forgetting rate relative to difficulty-ordered and random selection after controlling for review time and number of reviews](select-algorithm-lower-forgetting-rate-rct.md) — possibly the same claim (merge candidate)
- [Algorithm-selected learners remember content over ~69% longer, with median half-life increases of ~92% vs random and ~40% vs difficulty groups](select-group-longer-retention-half-life.md) — possibly the same claim (merge candidate)
- [Regression analysis shows the spacing effect holds in aggregate and the select group's advantage over other groups increases with number of reviews](spacing-effect-and-advantage-grows-with-reviews.md) — related
- [The selection algorithm affects engagement: select and difficulty groups were more likely to return within 4–7 days than the random group, but select-group learners were more likely to stop using the app in the initial 2 days](select-algorithm-engagement-effects.md) — related
- [A small randomized controlled study found adaptive problem selection improved learning compared with random problem selection](adaptive-problem-selection-improves-learning.md) — related
