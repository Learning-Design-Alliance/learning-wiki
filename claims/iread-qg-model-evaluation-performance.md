---
type: claim
title: The IRead question generation model, fine-tuned on in-text OpenStax questions, matched reference questions in human ratings and outperformed zero-shot GPT-4 on automatic metrics
description: The IRead question generation model, fine-tuned on in-text OpenStax questions, matched reference questions in human ratings and outperformed zero-shot GPT-4 on automatic metrics
id: iread-qg-model-evaluation-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: xiaoyu-zhang-2025
    resource: "https://doi.org/10.1007/s40593-025-00515-4"
    title: "Xiaoyu Zhang, Vincent Dörig, Peng Cui, Vilém Zouhar, Torbjørn Netland, Mrinmaya Sachan. (2025). Harmonizing Assistance: Moderating Visual and Textual Aids in AI-Enhanced Textbook Reading with IRead. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00515-4"
    author: Xiaoyu Zhang, Vincent Dörig, Peng Cui, Vilém Zouhar, Torbjørn Netland, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The IRead question generation model, fine-tuned on in-text OpenStax questions, matched reference questions in human ratings and outperformed zero-shot GPT-4 on automatic metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In human evaluation, model-generated questions received scores of 4.2, 4.3, and 4.2 on relevance, positioning, and importance, comparable to reference questions written by textbook authors. [→ Xiaoyu Zhang 2025](#xiaoyu-zhang-2025)

## Evidence

### Xiaoyu Zhang 2025

Xiaoyu Zhang, Vincent Dörig, Peng Cui, Vilém Zouhar, Torbjørn Netland, Mrinmaya Sachan. (2025). Harmonizing Assistance: Moderating Visual and Textual Aids in AI-Enhanced Textbook Reading with IRead. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00515-4

`q2 · i?` · `design · r2`

Human evaluation with 15 annotators rating 32 model-generated questions from five textbook chapters on relevance, appropriate positioning, and importance, against 15 other annotators rating 32 reference questions. Model scores were "comparable to those for the reference questions"; annotator consistency was Krippendorff's Alpha of 0.66.

> "On a scale of 1 to 5, the model-generated questions received scores of 4.2, 4.3, and 4.2 for the three criteria, respectively. These scores are comparable to those for the reference questions, which received 4.0, 4.2, and 4.4."

## Discussion


## Related Claims
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B](finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics.md) — related
