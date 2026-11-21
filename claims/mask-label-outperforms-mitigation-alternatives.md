---
type: claim
title: The MASK label method outperforms alternative leakage-mitigation strategies across most KT benchmark datasets
description: The MASK label method outperforms alternative leakage-mitigation strategies across most KT benchmark datasets
id: mask-label-outperforms-mitigation-alternatives
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yahya-badran-and-christine-preisach-2026
    resource: "https://doi.org/10.1007/s42979-026-05344-3"
    title: "Yahya Badran and Christine Preisach. (2026). Enhancing Knowledge Tracing through Leakage-Free and Recency-Aware Embeddings. Originally published 2025. [doi:10.1007/s42979-026-05344-3](https://doi.org/10.1007/s42979-026-05344-3)"
    author: Yahya Badran and Christine Preisach
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The MASK label method outperforms alternative leakage-mitigation strategies across most KT benchmark datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` MASK-based models (e.g., DKT-ML and AKT-ML) outperform other mitigation strategies (DKT-AD, DKT-Fuse, AKT-QM, AKT-Fuse) across most datasets, with especially large AUC gains for AKT. [→ Yahya Badran and Christine Preisach 2026](#yahya-badran-and-christine-preisach-2026)

## Evidence

### Yahya Badran and Christine Preisach 2026

Yahya Badran and Christine Preisach. (2026). Enhancing Knowledge Tracing through Leakage-Free and Recency-Aware Embeddings. Originally published 2025. [doi:10.1007/s42979-026-05344-3](https://doi.org/10.1007/s42979-026-05344-3)

`q2 · i?` · `causal · r2`

Benchmark comparison of mitigation methods (Table 3) across Algebra05, Riiid20 and Duolingo18. The article reports "MASK-based models (e.g., DKT-ML and AKT-ML) outperform other mitigation strategies across most datasets". AUC values are printed in the table but no standardised effect size, so impact is coded i? (no magnitude reported; not a null effect).

> "As shown in Table 3,MASK-based models (e.g., DKT-ML and AKT-ML) outperform other mitigation strategies across most datasets. The performance gain is especially significant for AKT, where the AUC improvements are consistently larger."

## Discussion


## Related Claims
- [AKT-MLd achieves the best overall performance across benchmarks, with gains most pronounced on high-KC datasets](akt-mld-best-overall-benchmarks.md) — related
- [KC-sequence expansion causes label leakage that degrades KT model performance, shown by sharp drops on a correlated-KC dataset](kt-label-leakage-degrades-correlated-kc-performance.md) — related
