---
type: claim
title: "ML-based question selection (SELECT) lowers learners' normalized empirical forgetting rate relative to difficulty-ordered and random selection after controlling for review time and number of reviews"
description: "ML-based question selection (SELECT) lowers learners' normalized empirical forgetting rate relative to difficulty-ordered and random selection after controlling for review time and number of reviews"
id: select-algorithm-lower-forgetting-rate-rct
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: utkarsh-upadhyay-2021
    resource: "https://doi.org/10.1038/s41539-021-00105-8"
    title: "Utkarsh Upadhyay, Graham Lancashire, Christoph Moser and Manuel Gomez-Rodriguez. (2021). Large-scale randomized experiments reveals that machine learning-based instruction helps people memorize more effectively. npj Science of Learning 6:26. https://doi.org/10.1038/s41539-021-00105-8"
    author: Utkarsh Upadhyay, Graham Lancashire, Christoph Moser and Manuel Gomez-Rodriguez
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# ML-based question selection (SELECT) lowers learners' normalized empirical forgetting rate relative to difficulty-ordered and random selection after controlling for review time and number of reviews

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` After controlling for review time and number of reviews, learners whose questions were chosen by the ML algorithm had lower median normalized empirical forgetting rate than the difficulty and random groups in 83.5% of cases, with statistically significant decreases in 66.7% of cases. [→ Utkarsh Upadhyay 2021](#utkarsh-upadhyay-2021)

## Evidence

### Utkarsh Upadhyay 2021

Utkarsh Upadhyay, Graham Lancashire, Christoph Moser and Manuel Gomez-Rodriguez. (2021). Large-scale randomized experiments reveals that machine learning-based instruction helps people memorize more effectively. npj Science of Learning 6:26. https://doi.org/10.1038/s41539-021-00105-8

`q3 · i?` · `causal · r2`

Randomized controlled trial comparing 'select', 'difficulty' and 'random' groups on normalized empirical forgetting rate (Fig. 1), using Matt–Whitney U-tests with Bonferroni correction (p-value = 0.05/36). The 'select' group's "decrease was statistically signiﬁcant" in 66.7% of cases; no standardized effect size is printed.

> "After controlling for review time and number of reviews, the median normalized empirical forgetting rate for the learners in the ‘select’group was lower than that of the learners in the ‘difﬁculty’ and ‘random’groups in 83.5% of the cases and the decrease was statistically signiﬁcant"

## Discussion


## Related Claims
- [The selection algorithm affects engagement: select and difficulty groups were more likely to return within 4–7 days than the random group, but select-group learners were more likely to stop using the app in the initial 2 days](select-algorithm-engagement-effects.md) — related
- [Regression analysis shows the spacing effect holds in aggregate and the select group's advantage over other groups increases with number of reviews](spacing-effect-and-advantage-grows-with-reviews.md) — related
- [Algorithm-selected learners remember content over ~69% longer, with median half-life increases of ~92% vs random and ~40% vs difficulty groups](select-group-longer-retention-half-life.md) — possibly the same claim (merge candidate)
- [A small randomized controlled study found adaptive problem selection improved learning compared with random problem selection](adaptive-problem-selection-improves-learning.md) — related
