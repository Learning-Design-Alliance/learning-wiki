---
type: claim
title: Augmenting BKT with learned auxiliary KCs improves its AUC across all four datasets and outperforms standard DKT on ASSISTments2009 and riiid2020
description: Augmenting BKT with learned auxiliary KCs improves its AUC across all four datasets and outperforms standard DKT on ASSISTments2009 and riiid2020
id: bkt-aux-improves-bkt
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
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

# Augmenting BKT with learned auxiliary KCs improves its AUC across all four datasets and outperforms standard DKT on ASSISTments2009 and riiid2020

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` BKT enhanced with auxiliary KCs outperforms the standard DKT on the ASSISTments2009 and riiid2020 datasets. [→ Yahya Badran and Christine Preisach 2026](#yahya-badran-and-christine-preisach-2026)

## Evidence

### Yahya Badran and Christine Preisach 2026

Yahya Badran and Christine Preisach. (2026). Representation Learning of Auxiliary Concepts for Improved Student Modeling and Exercise Recommendation. Originally published 2025. [doi:10.1007/978-3-032-39106-3_8](https://doi.org/10.1007/978-3-032-39106-3_8)

`q2 · i?` · `design · r2`

Downstream-task evaluation (Table 3) in which unaltered BKT is trained with added pretrained auxiliary KCs and compared by AUC against standard DKT on the same data. The article reports BKT+aux "outperforms the standard DKT" on the two named datasets.

> "The results indicate that BKT enhanced with auxiliary KCs (BKT+aux) outperforms the standard DKT on the ASSISTments2009 and Riiid2020 datasets."

## Discussion


## Related Claims
- [Augmenting DKT with auxiliary KCs improves AUC on all datasets except Algebra2005, where it performs slightly worse than original DKT](dkt-aux-mixed-gains.md) — related
- [The quantization layer is important to SBRKT: removing it (dense variant) underperforms significantly, and auxiliary KCs from quantized variants transfer better](quantization-layer-ablation.md) — related
