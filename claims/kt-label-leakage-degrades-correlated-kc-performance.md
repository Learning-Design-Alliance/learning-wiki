---
type: claim
title: KC-sequence expansion causes label leakage that degrades KT model performance, shown by sharp drops on a correlated-KC dataset
description: KC-sequence expansion causes label leakage that degrades KT model performance, shown by sharp drops on a correlated-KC dataset
id: kt-label-leakage-degrades-correlated-kc-performance
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
    rigour: 1
---

# KC-sequence expansion causes label leakage that degrades KT model performance, shown by sharp drops on a correlated-KC dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Original KT models (e.g., DKT, AKT) suffer significant performance degradation on CorrAS09 due to duplicated and correlated KCs, revealing susceptibility to leakage, while mask-label variants maintain consistent performance. [→ Yahya Badran and Christine Preisach 2026](#yahya-badran-and-christine-preisach-2026)

## Evidence

### Yahya Badran and Christine Preisach 2026

Yahya Badran and Christine Preisach. (2026). Enhancing Knowledge Tracing through Leakage-Free and Recency-Aware Embeddings. Originally published 2025. [doi:10.1007/s42979-026-05344-3](https://doi.org/10.1007/s42979-026-05344-3)

`q2 · i?` · `causal · r1`

Comparison of models trained with and without mitigation strategies on ASSISTments2009 and the synthetic CorrAS09 dataset (Table 2, AUC mean±std). The article reports that "the original models (e.g., DKT, AKT) suffer significant performance degradation on CorrAS09" while mask-label variants stay consistent. No effect size is printed, so impact is coded i? (no magnitude reported; not a null effect).

> "the original models (e.g., DKT, AKT) suffer significant perfor- mance degradation on CorrAS09 due to duplicated and correlated KCs, revealing their susceptibility to leakage. This contrasts with variants such as DKT-ML, AKT-ML, SAKT-ML, and DKT-ML+, which maintain high and consistent performance across both datasets."

## Discussion


## Related Claims
- [The MASK label method outperforms alternative leakage-mitigation strategies across most KT benchmark datasets](mask-label-outperforms-mitigation-alternatives.md) — related
- [AKT-MLd achieves the best overall performance across benchmarks, with gains most pronounced on high-KC datasets](akt-mld-best-overall-benchmarks.md) — related
- [Error injection validation shows each SLATE dimension selectively degrades under its targeted corruption, and answer leakage inflates posttest scores while destroying far-transfer performance](slate-error-injection-construct-validity.md) — related
