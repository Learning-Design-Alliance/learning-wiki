---
type: claim
title: Transformer-based models outperformed traditional machine learning models for detecting CPS classes, with higher performance in the affective than the social-cognitive dimension
description: Transformer-based models outperformed traditional machine learning models for detecting CPS classes, with higher performance in the affective than the social-cognitive dimension
id: transformer-models-outperform-traditional-cps-detection
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

# Transformer-based models outperformed traditional machine learning models for detecting CPS classes, with higher performance in the affective than the social-cognitive dimension

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Transformer-based models (BERT, AudiBERT) achieved better weighted precision, recall and F1 than traditional RF TF-IDF models for CPS class detection in both social-cognitive and affective dimensions. [→ Kester Wong 2025](#kester-wong-2025)
`q2 i?` Detection performance was higher for the small number of affective-dimension classes (metric values above 0.8) than for social-cognitive-dimension classes (metric values below 0.6). [→ Kester Wong 2025 (2)](#kester-wong-2025-2)

## Evidence

### Kester Wong 2025

Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. [doi:10.1007/978-3-031-98417-4_2](https://doi.org/10.1007/978-3-031-98417-4_2)

`q2 · i?` · `design · r2`

Model comparison on the study's CPS classification test sets (Table 2), evaluating BERT and AudiBERT against RF TF-IDF baselines with weighted precision, recall and F1. The results report that "transformer-based models demonstrated better performance on weighted precision, recall, and F1 scores over traditional models" in both dimensions.

> "In terms of detecting CPS classes using audio data, transformer-based models demonstrated better performance on weighted precision, recall, and F1 scores over traditional models for classification on classes in both social-cognitive and affective dimensions (refer to Table 2)."

### Kester Wong 2025 (2)

Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. [doi:10.1007/978-3-031-98417-4_2](https://doi.org/10.1007/978-3-031-98417-4_2)

`q2 · i?` · `design · r2`

Same model-comparison experiment, reporting Table 2 metrics by dimension: "a higher performance in detecting the small number of classes in the affective dimension" (metrics > 0.8) than the social-cognitive dimension (metrics < 0.6). No effect sizes are printed.

> "Overall, there was a higher performance in detecting the small number of classes in the affective dimension (i.e., metric values > 0.8) than in the social-cognitive dimension (i.e., metric values < 0.6)."

## Discussion


## Related Claims
- [Models made few or no predictions on underrepresented social-cognitive classes, though AudiBERT improved classification of the sparse AS3 affect state](audibert-improves-sparse-as3-classification.md) — related
- [AudiBERT outperformed BERT on F1 in both dimensions, while BERT performed better on accuracy, precision and recall in the affective dimension](audibert-vs-bert-f1-accuracy-tradeoff.md) — related
- [Adding audio features lowered the traditional RF model's CPS classification performance](audio-features-lower-traditional-model-performance.md) — related
- [T-tests show no significant shallow-vs-transformer difference in accuracy, weighted F1 or macro-F1, but a significant ROC-AUC advantage for the shallow model](ttest-roc-auc-advantage-shallow.md) — reports the opposite
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
