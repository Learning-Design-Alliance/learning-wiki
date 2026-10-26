---
type: claim
title: "Regression analysis shows the spacing effect holds in aggregate and the select group's advantage over other groups increases with number of reviews"
description: "Regression analysis shows the spacing effect holds in aggregate and the select group's advantage over other groups increases with number of reviews"
id: spacing-effect-and-advantage-grows-with-reviews
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: weak
newest_evidence: 2021
sources:
  - id: utkarsh-upadhyay-2021
    resource: "https://doi.org/10.1038/s41539-021-00105-8"
    title: "Utkarsh Upadhyay, Graham Lancashire, Christoph Moser and Manuel Gomez-Rodriguez. (2021). Large-scale randomized experiments reveals that machine learning-based instruction helps people memorize more effectively. npj Science of Learning 6:26. https://doi.org/10.1038/s41539-021-00105-8"
    author: Utkarsh Upadhyay, Graham Lancashire, Christoph Moser and Manuel Gomez-Rodriguez
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Regression analysis shows the spacing effect holds in aggregate and the select group's advantage over other groups increases with number of reviews

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Huber regression coefficients indicate that more spaced reviews yield lower final normalized empirical forgetting rate, and that w_difficulty > 0 and w_random > 0 across all #reviews, with coefficients for other groups increasing with number of reviews. [→ Utkarsh Upadhyay 2021](#utkarsh-upadhyay-2021)

## Evidence

### Utkarsh Upadhyay 2021

Utkarsh Upadhyay, Graham Lancashire, Christoph Moser and Manuel Gomez-Rodriguez. (2021). Large-scale randomized experiments reveals that machine learning-based instruction helps people memorize more effectively. npj Science of Learning 6:26. https://doi.org/10.1038/s41539-021-00105-8

`q2 · i?` · `causal · r2`

Huber regression (Table 1) of normalized empirical forgetting rate on review time and group indicators for a fixed number of reviews. The article states the spacing effect "holds true in aggregate" and that coefficients "seem to increase with number of reviews"; no standardized effect size is printed.

> "The results also suggest that, since wdifﬁculty > 0 and wrandom > 0 across all #reviews, learners in the ‘select’group have lower forgetting rate and, since the coef ﬁcients for the other groups seem to increase with number of reviews, the competitive advantage offered by our machine learning algorithm increases with the number of reviews."

## Discussion


## Related Claims
- [The selection algorithm affects engagement: select and difficulty groups were more likely to return within 4–7 days than the random group, but select-group learners were more likely to stop using the app in the initial 2 days](select-algorithm-engagement-effects.md) — related
- [ML-based question selection (SELECT) lowers learners' normalized empirical forgetting rate relative to difficulty-ordered and random selection after controlling for review time and number of reviews](select-algorithm-lower-forgetting-rate-rct.md) — related
- [Algorithm-selected learners remember content over ~69% longer, with median half-life increases of ~92% vs random and ~40% vs difficulty groups](select-group-longer-retention-half-life.md) — related
- [Number of retrieval exposures moderates the expanding-versus-uniform schedule benefit: more tests favour the expanding schedule](exposures-moderate-expanding-schedule-benefit.md) — related
- [The classroom testing effect increases with the number of test repetitions on the same content.](test-repetitions-positive-relationship-classroom.md) — a broader claim this one bears on
