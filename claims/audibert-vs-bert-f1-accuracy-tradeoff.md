---
type: claim
title: AudiBERT outperformed BERT on F1 in both dimensions, while BERT performed better on accuracy, precision and recall in the affective dimension
description: AudiBERT outperformed BERT on F1 in both dimensions, while BERT performed better on accuracy, precision and recall in the affective dimension
id: audibert-vs-bert-f1-accuracy-tradeoff
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: kester-wong-2025
    resource: "https://doi.org/10.1007/978-3-031-98417-4_2"
    title: "Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. [doi:10.1007/978-3-031-98417-4_2](https://doi.org/10.1007/978-3-031-98417-4_2)"
    author: Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# AudiBERT outperformed BERT on F1 in both dimensions, while BERT performed better on accuracy, precision and recall in the affective dimension

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly
> **Design limits** · Kester Wong 2025: no comparison group; groups were assigned but students were analysed as independent (read from the study by two models, 2026-11-21)

## Subclaims
`q2 i?` The multimodal AudiBERT model achieved higher F1 than unimodal BERT in both social-cognitive and affective dimensions, but BERT achieved better accuracy, precision and recall in the affective dimension. [→ Kester Wong 2025](#kester-wong-2025)

## Evidence

### Kester Wong 2025

Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. [doi:10.1007/978-3-031-98417-4_2](https://doi.org/10.1007/978-3-031-98417-4_2)

`q2 · i?` · `causal · r2`

Model comparison on the CPS test sets (Table 2): "AudiBERT is observed to outperform BERT on F1 scores for classifications in both social-cognitive and affective dimensions", while "BERT was observed to perform better in accuracy, precision and recall" in the affective dimension. No effect sizes are printed.

> "AudiBERT is observed to outperform BERT on F1 scores for classifications in both social-cognitive and affective dimensions. However, BERT was observed to perform better in accuracy, precision and recall compared to AudiBERT for classifications in the affective dimension."

## Discussion


## Related Claims
- [AudiBERT improved classification of five specific social-cognitive CPS classes: SS1 sense-making, SS3 formulating a solution, SS5 reaching a solution, SS6 maintaining roles and responsibilities, and SC1 using scripting](audibert-improves-specific-social-cognitive-classes.md) — related
- [Transformer-based models outperformed traditional machine learning models for detecting CPS classes, with higher performance in the affective than the social-cognitive dimension](transformer-models-outperform-traditional-cps-detection.md) — related
- [Models made few or no predictions on underrepresented social-cognitive classes, though AudiBERT improved classification of the sparse AS3 affect state](audibert-improves-sparse-as3-classification.md) — related
