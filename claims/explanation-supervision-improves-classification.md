---
type: claim
title: Training with textual explanations improves classification over label-only training
description: Training with textual explanations improves classification over label-only training
id: explanation-supervision-improves-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: anqi-li-2026
    resource: "https://doi.org/10.48550/arXiv.2602.21638"
    title: "Anqi Li, Ruihan Wang, Zhaoming Chen, Yuqian Chen, Yu Lu, Yi Zhu, Yuan Xie, Zhenzhong Lan. (2026). Multi-dimensional Assessment and Explainable Feedback for Counselor Responses to Client Resistance in Text-based Counseling with LLMs. [doi:10.48550/arXiv.2602.21638](https://doi.org/10.48550/arXiv.2602.21638)"
    author: Anqi Li, Ruihan Wang, Zhaoming Chen, Yuqian Chen, Yu Lu, Yi Zhu, Yuan Xie, Zhenzhong Lan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Training with textual explanations improves classification over label-only training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Models fine-tuned with explanation-augmented supervision score at least 4 F1 points higher than models trained only on dimension-level ratings. [→ Anqi Li 2026](#anqi-li-2026)

## Evidence

### Anqi Li 2026

Anqi Li, Ruihan Wang, Zhaoming Chen, Yuqian Chen, Yu Lu, Yi Zhu, Yuan Xie, Zhenzhong Lan. (2026). Multi-dimensional Assessment and Explainable Feedback for Counselor Responses to Client Resistance in Text-based Counseling with LLMs. [doi:10.48550/arXiv.2602.21638](https://doi.org/10.48550/arXiv.2602.21638)

`q2 · i?` · `causal · r2`

Ablation study fully fine-tuning the Llama-3.1-8B-Instruct backbone with only dimension-level ratings versus ratings plus explanations, evaluated under the same five-fold cross-validation protocol. The article reports "improvements of at least 4 F1 points" for explanation-augmented training.

> "Compared with models trained solely on numerical scores, those incorporating textual ex- planations achieve higher performance across all four com- munication mechanisms, with improvements of at least 4 F1 points."

## Discussion


## Related Claims
- [AI-generated feedback significantly improves counselors' responses to client resistance in a controlled experiment](ai-feedback-improves-counselor-responses-experiment.md) — related
- [Fine-tuning BERT-based classifiers on LLM-augmented student-response data outperforms unaugmented training for all tested concepts](llm-augmentation-beats-unaugmented-small-education-data.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
