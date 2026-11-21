---
type: claim
title: Gradient-based token importance analysis shows the fine-tuned model assigns high importance to semantically meaningful tokens such as explanation, research-quality, and Bloom
description: Gradient-based token importance analysis shows the fine-tuned model assigns high importance to semantically meaningful tokens such as explanation, research-quality, and Bloom
id: anveshanai-xai-token-importance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: rakesh-thakur-2025
    resource: "https://doi.org/10.48550/arXiv.2509.23811"
    title: "Rakesh Thakur, Diksha Khandelwal, Shreya Tiwari. (2025). ANVESHANAAI: A MULTIMODAL PLATFORM FOR ADAPTIVE AI/ML EDUCATION THROUGH AUTOMATED QUESTION GENERATION AND INTERACTIVE ASSESSMENT. arXiv preprint. [doi:10.48550/arXiv.2509.23811](https://doi.org/10.48550/arXiv.2509.23811)"
    author: Rakesh Thakur, Diksha Khandelwal, Shreya Tiwari
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Gradient-based token importance analysis shows the fine-tuned model assigns high importance to semantically meaningful tokens such as explanation, research-quality, and Bloom

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Explainability analysis via gradient-based token importance indicates the model's predictions are guided by contextually relevant information, supporting interpretability of generated questions. [→ Rakesh Thakur 2025](#rakesh-thakur-2025)

## Evidence

### Rakesh Thakur 2025

Rakesh Thakur, Diksha Khandelwal, Shreya Tiwari. (2025). ANVESHANAAI: A MULTIMODAL PLATFORM FOR ADAPTIVE AI/ML EDUCATION THROUGH AUTOMATED QUESTION GENERATION AND INTERACTIVE ASSESSMENT. arXiv preprint. [doi:10.48550/arXiv.2509.23811](https://doi.org/10.48550/arXiv.2509.23811)

`q1 · i?` · `design · r2`

Explainable AI analysis (Section 5.3) performing token importance analysis based on gradients on research-style prompts, with the top ten most influential tokens visualized as a heatmap (Figure 12). The paper reports high attribution to "explanation, research-quality, and Bloom" tokens.

> "The model consistently assigned high importance to semantically meaningful tokens such asex- planation,research-quality, andBloom(Bloom, 1956; Ghosh et al., 2024), confirming that its pre- dictions are guided by contextually relevant information."

## Discussion


## Related Claims
- [The AnveshanaAI dataset shows high annotation quality, including 97% effective utilization of Bloom's taxonomy levels](anveshanai-annotation-quality-metrics.md) — related
- [Attribution analysis identifies interpretable input features for BERT's classification decisions, including subjunctive verbs in alternatives and appraisal words in evaluation](attribution-analysis-identifies-bert-classification-features.md) — related
