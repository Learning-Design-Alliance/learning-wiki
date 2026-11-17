---
type: claim
title: Simple IRT-based models do as well or significantly better than DKT across all three evaluated datasets on online response prediction
description: Simple IRT-based models do as well or significantly better than DKT across all three evaluated datasets on online response prediction
id: irt-models-match-or-beat-dkt-online-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: moderate
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

# Simple IRT-based models do as well or significantly better than DKT across all three evaluated datasets on online response prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across ASSISTments, KDD Cup, and Knewton data, IRT-based models matched or outperformed DKT on accuracy and AUC in five-fold cross-validated online prediction. [→ Kevin H. Wilson 2016](#kevin-h-wilson-2016)

## Evidence

### Kevin H. Wilson 2016

Kevin H. Wilson, Yan Karklin, Bojian Han, Chaitanya Ekanadham. (2016). Back to the basics: Bayesian extensions of IRT outperform neural networks for proficiency estimation. arXiv:1604.02336v2 [cs.AI]. [doi:10.48550/arXiv.1604.02336](https://doi.org/10.48550/arXiv.1604.02336)

`q2 · i?` · `design · r2`

Evaluation of 1PO IRT, HIRT, TIRT, and DKT on three datasets with five-fold cross validation by student. Printed AUCs: ASSISTments HIRT 0.7740 vs DKT 0.7429; KDD HIRT 0.8597 vs DKT 0.8110; Knewton HIRT 0.8189 vs DKT 0.7756 — "do as well or signiﬁcantly better than DKT".

> "The results clearly indicate that simple IRT-based models do as well or signiﬁcantly better than DKT across all data sets."

## Discussion


## Related Claims
- [Hierarchical IRT, which exploits item grouping structure, was the best-performing model across the board except on one metric](hirt-best-performing-item-grouping.md) — related
- [Temporal IRT improved prediction only on the dataset with non-trivial temporal structure, while DKT lagged regardless](tirt-improves-only-with-temporal-structure.md) — related
- [A windowed percent-correct analysis shows an optimal window length only in the Knewton dataset, indicating nontrivial temporal structure there](windowed-analysis-temporal-structure.md) — related
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
