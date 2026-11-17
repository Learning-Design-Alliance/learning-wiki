---
type: claim
title: Temporal IRT improved prediction only on the dataset with non-trivial temporal structure, while DKT lagged regardless
description: Temporal IRT improved prediction only on the dataset with non-trivial temporal structure, while DKT lagged regardless
id: tirt-improves-only-with-temporal-structure
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: weak
newest_evidence: 2016
recheck_by: 2019
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

# Temporal IRT improved prediction only on the dataset with non-trivial temporal structure, while DKT lagged regardless

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` TIRT yielded higher accuracy on the Knewton dataset but not on ASSISTments or KDD, and the RNN-based DKT did not benefit from temporal structure in any dataset. [→ Kevin H. Wilson 2016](#kevin-h-wilson-2016)

## Evidence

### Kevin H. Wilson 2016

Kevin H. Wilson, Yan Karklin, Bojian Han, Chaitanya Ekanadham. (2016). Back to the basics: Bayesian extensions of IRT outperform neural networks for proficiency estimation. arXiv:1604.02336v2 [cs.AI]. [doi:10.48550/arXiv.1604.02336](https://doi.org/10.48550/arXiv.1604.02336)

`q2 · i?` · `design · r2`

Cross-validated online prediction across three datasets. On Knewton, TIRT accuracy was 0.7481 vs IRT 0.7292; on ASSISTments 0.7224 vs 0.7219 and on KDD identical to IRT (AUC 0.8542), consistent with "higher accuracy on the Knewton dataset, but not on the other two".

> "The temporal IRT model yielded higher accuracy on the Knewton dataset, but not on the other two data sets."

## Discussion


## Related Claims
- [Hierarchical IRT, which exploits item grouping structure, was the best-performing model across the board except on one metric](hirt-best-performing-item-grouping.md) — related
- [Simple IRT-based models do as well or significantly better than DKT across all three evaluated datasets on online response prediction](irt-models-match-or-beat-dkt-online-prediction.md) — related
- [A windowed percent-correct analysis shows an optimal window length only in the Knewton dataset, indicating nontrivial temporal structure there](windowed-analysis-temporal-structure.md) — a narrower finding that bears on this claim
