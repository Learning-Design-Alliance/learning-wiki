---
type: claim
title: Augmenting DKT with auxiliary KCs improves AUC on all datasets except Algebra2005, where it performs slightly worse than original DKT
description: Augmenting DKT with auxiliary KCs improves AUC on all datasets except Algebra2005, where it performs slightly worse than original DKT
id: dkt-aux-mixed-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yahya-badran-and-christine-preisach-2026
    resource: "https://doi.org/10.1007/978-3-032-39106-3_8"
    title: "Yahya Badran and Christine Preisach. (2026). Representation Learning of Auxiliary Concepts for Improved Student Modeling and Exercise Recommendation. Originally published 2025. [doi:10.1007/978-3-032-39106-3_8](https://doi.org/10.1007/978-3-032-39106-3_8)"
    author: Yahya Badran and Christine Preisach
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Augmenting DKT with auxiliary KCs improves AUC on all datasets except Algebra2005, where it performs slightly worse than original DKT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` DKT augmented with auxiliary KCs shows improved performance on all datasets except Algebra2005, where it performs slightly worse than the original DKT. [→ Yahya Badran and Christine Preisach 2026](#yahya-badran-and-christine-preisach-2026)

## Evidence

### Yahya Badran and Christine Preisach 2026

Yahya Badran and Christine Preisach. (2026). Representation Learning of Auxiliary Concepts for Improved Student Modeling and Exercise Recommendation. Originally published 2025. [doi:10.1007/978-3-032-39106-3_8](https://doi.org/10.1007/978-3-032-39106-3_8)

`q2 · i?` · `design · r2`

Table 3 downstream evaluation of DKT trained with pretrained auxiliary KCs versus original DKT across the four benchmark datasets, measured by AUC. The effect does not hold on Algebra2005, so the article's own summary calls the DKT gains dataset-dependent.

> "On the other hand, DKT augmented with auxiliary KCs (DKT+aux) shows improved performance on all datasets except Algebra2005, where it performs slightly worse than the original DKT."

## Discussion


## Related Claims
- [Augmenting BKT with learned auxiliary KCs improves its AUC across all four datasets and outperforms standard DKT on ASSISTments2009 and riiid2020](bkt-aux-improves-bkt.md) — related
- [The quantization layer is important to SBRKT: removing it (dense variant) underperforms significantly, and auxiliary KCs from quantized variants transfer better](quantization-layer-ablation.md) — related
- [SBRKT achieves the highest AUC on several knowledge tracing benchmarks and ranks second on the others, despite sparse discrete representations](sbrkt-auc-vs-baselines.md) — related
