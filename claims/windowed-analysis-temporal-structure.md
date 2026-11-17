---
type: claim
title: A windowed percent-correct analysis shows an optimal window length only in the Knewton dataset, indicating nontrivial temporal structure there
description: A windowed percent-correct analysis shows an optimal window length only in the Knewton dataset, indicating nontrivial temporal structure there
id: windowed-analysis-temporal-structure
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: weak
newest_evidence: 2016
sources:
  - id: kevin-h-wilson-2016
    resource: "https://doi.org/10.48550/arXiv.1604.02336"
    title: "Kevin H. Wilson, Yan Karklin, Bojian Han, Chaitanya Ekanadham. (2016). Back to the basics: Bayesian extensions of IRT outperform neural networks for proficiency estimation. arXiv:1604.02336v2 [cs.AI]. [doi:10.48550/arXiv.1604.02336](https://doi.org/10.48550/arXiv.1604.02336)"
    author: Kevin H. Wilson, Yan Karklin, Bojian Han, Chaitanya Ekanadham
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A windowed percent-correct analysis shows an optimal window length only in the Knewton dataset, indicating nontrivial temporal structure there

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Predicting from a majority vote over the previous w responses degraded for windows too short or too long on Knewton, while on ASSISTments and KDD longer windows performed equal or better, suggesting static models suffice there. [→ Kevin H. Wilson 2016](#kevin-h-wilson-2016)

## Evidence

### Kevin H. Wilson 2016

Kevin H. Wilson, Yan Karklin, Bojian Han, Chaitanya Ekanadham. (2016). Back to the basics: Bayesian extensions of IRT outperform neural networks for proficiency estimation. arXiv:1604.02336v2 [cs.AI]. [doi:10.48550/arXiv.1604.02336](https://doi.org/10.48550/arXiv.1604.02336)

`q2 · i?` · `design · r2`

Diagnostic analysis (Figure 2) computing accuracy of a naive windowed majority-vote predictor as a function of window length 1–16 on each dataset. On ASSISTments and KDD, "longer window lengths perform equal or better than shorter window lengths".

> "The Knewton data set has a clear optimal window length – integrating over windows too short or too long degraded performance, which is indicative of nontrivial temporal structure."

## Discussion


## Related Claims
- [Hierarchical IRT, which exploits item grouping structure, was the best-performing model across the board except on one metric](hirt-best-performing-item-grouping.md) — related
- [Simple IRT-based models do as well or significantly better than DKT across all three evaluated datasets on online response prediction](irt-models-match-or-beat-dkt-online-prediction.md) — related
- [Temporal IRT improved prediction only on the dataset with non-trivial temporal structure, while DKT lagged regardless](tirt-improves-only-with-temporal-structure.md) — a broader claim this one bears on
- [MBP-KT performance is optimal with sliding-window size N between 2 and 4 and is not sensitive to pattern-set length K (variation within 2%)](mbp-kt-hyperparameter-sensitivity-n-k.md) — related
- [Performance is best at moderate difficulty granularity and a limited recent window for domain transitions](moderate-difficulty-granularity-window-optimal.md) — related
