---
type: claim
title: "Adding audio features lowered the traditional RF model's CPS classification performance"
description: "Adding audio features lowered the traditional RF model's CPS classification performance"
id: audio-features-lower-traditional-model-performance
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
---

# Adding audio features lowered the traditional RF model's CPS classification performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The RF TF-IDF+A model, which concatenated 11 openSMILE audio features with the TF-IDF vector, performed worse than the text-only RF TF-IDF model. [→ Kester Wong 2025](#kester-wong-2025)

## Evidence

### Kester Wong 2025

Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. [doi:10.1007/978-3-031-98417-4_2](https://doi.org/10.1007/978-3-031-98417-4_2)

`q2 · i?` · `design · r2`

Comparison of RF TF-IDF and RF TF-IDF+A on the CPS test sets (Table 2): "the RF TF-IDF+A model had lower performance than the TF-IDF model"; the authors suggest the audio features "could have introduced variability and noise to the dataset". No effect sizes are printed.

> "It is observed in Table 2 that the RF TF-IDF+A model had lower performance than the TF-IDF model. Including audio features could have introduced variability and noise to the dataset, making it difficult for the model to distinguish relevant patterns."

## Discussion


## Related Claims
- [Transformer-based models outperformed traditional machine learning models for detecting CPS classes, with higher performance in the affective than the social-cognitive dimension](transformer-models-outperform-traditional-cps-detection.md) — related
