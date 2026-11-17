---
type: claim
title: Hierarchical IRT, which exploits item grouping structure, was the best-performing model across the board except on one metric
description: Hierarchical IRT, which exploits item grouping structure, was the best-performing model across the board except on one metric
id: hirt-best-performing-item-grouping
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
    kind: associational
    rigour: 2
---

# Hierarchical IRT, which exploits item grouping structure, was the best-performing model across the board except on one metric

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` HIRT achieved the best accuracy and AUC on all three datasets except MAP accuracy on Knewton, where TIRT slightly outperformed it, suggesting grouping structure is useful for predicting student responses. [→ Kevin H. Wilson 2016](#kevin-h-wilson-2016)

## Evidence

### Kevin H. Wilson 2016

Kevin H. Wilson, Yan Karklin, Bojian Han, Chaitanya Ekanadham. (2016). Back to the basics: Bayesian extensions of IRT outperform neural networks for proficiency estimation. arXiv:1604.02336v2 [cs.AI]. [doi:10.48550/arXiv.1604.02336](https://doi.org/10.48550/arXiv.1604.02336)

`q2 · i?` · `associational · r2`

Five-fold cross-validated comparison across the three datasets (Figure 1). HIRT had access to both item and group identifiers per interaction; printed AUCs were 0.7740 (ASSISTments), 0.8597 (KDD), and 0.8189 (Knewton), each the highest of the four models.

> "The fact that HIRT is the best-performing model across the board (except for MAP accuracy on the Knewton dataset where TIRT slightly outperforms it) suggests that grouping structure is useful information to exploit when predicting student responses."

## Discussion


## Related Claims
- [Simple IRT-based models do as well or significantly better than DKT across all three evaluated datasets on online response prediction](irt-models-match-or-beat-dkt-online-prediction.md) — related
- [Temporal IRT improved prediction only on the dataset with non-trivial temporal structure, while DKT lagged regardless](tirt-improves-only-with-temporal-structure.md) — related
- [A windowed percent-correct analysis shows an optimal window length only in the Knewton dataset, indicating nontrivial temporal structure there](windowed-analysis-temporal-structure.md) — related
