---
type: claim
title: Models made few or no predictions on underrepresented social-cognitive classes, though AudiBERT improved classification of the sparse AS3 affect state
description: Models made few or no predictions on underrepresented social-cognitive classes, though AudiBERT improved classification of the sparse AS3 affect state
id: audibert-improves-sparse-as3-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: kester-wong-2025
    resource: "https://doi.org/10.1007/978-3-031-98417-4_2"
    title: "Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. [doi:10.1007/978-3-031-98417-4_2](https://doi.org/10.1007/978-3-031-98417-4_2)"
    author: Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: kester-wong-2025-2
    resource: "https://doi.org/10.1007/978-3-031-98417-4_2"
    title: "Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. [doi:10.1007/978-3-031-98417-4_2](https://doi.org/10.1007/978-3-031-98417-4_2)"
    author: Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Models made few or no predictions on underrepresented social-cognitive classes, though AudiBERT improved classification of the sparse AS3 affect state

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Unimodal and multimodal models made predictions predominantly on the same classes, with few or no predictions on the underrepresented classes SS6, SS7 and SS8. [→ Kester Wong 2025](#kester-wong-2025)
`q2 i?` AudiBERT improved classification of AS3 compared to BERT despite AS3 having significantly fewer training data than the other affective classes. [→ Kester Wong 2025 (2)](#kester-wong-2025-2)

## Evidence

### Kester Wong 2025

Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. [doi:10.1007/978-3-031-98417-4_2](https://doi.org/10.1007/978-3-031-98417-4_2)

`q2 · i?` · `design · r2`

Confusion-matrix analysis (Figure 1) of model predictions on the CPS test sets: predictions concentrated on the same classes, "with few or no predictions on "SS6", "SS7", or "SS8" which were underrepresented in the dataset".

> "Figure 1 showed that unimodal and multimodal models made predictions predominantly on the same classes, with few or no predictions on "SS6", "SS7", or "SS8" which were underrepresented in the dataset (refer to Table 1)."

### Kester Wong 2025 (2)

Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. [doi:10.1007/978-3-031-98417-4_2](https://doi.org/10.1007/978-3-031-98417-4_2)

`q2 · i?` · `design · r2`

Same confusion-matrix analysis (Figure 1): "AudiBERT was able to improve the classification of "AS3" compared to BERT", despite AS3 having significantly fewer training data than other affective classes.

> "However, AudiBERT was able to improve the classification of "AS3" compared to BERT, despite having significantly fewer training data than the other classes in the affective dimension."

## Discussion


## Related Claims
- [AudiBERT improved classification of five specific social-cognitive CPS classes: SS1 sense-making, SS3 formulating a solution, SS5 reaching a solution, SS6 maintaining roles and responsibilities, and SC1 using scripting](audibert-improves-specific-social-cognitive-classes.md) — related
- [Transformer-based models outperformed traditional machine learning models for detecting CPS classes, with higher performance in the affective than the social-cognitive dimension](transformer-models-outperform-traditional-cps-detection.md) — related
- [AudiBERT outperformed BERT on F1 in both dimensions, while BERT performed better on accuracy, precision and recall in the affective dimension](audibert-vs-bert-f1-accuracy-tradeoff.md) — related
