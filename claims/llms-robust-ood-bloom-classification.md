---
type: claim
title: LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models
description: LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models
id: llms-robust-ood-bloom-classification
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: michael-lawrence-castanares-2026
    resource: "https://arxiv.org/abs/2609.27749"
    title: "Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749"
    author: Michael Lawrence Castanares, Princess Ventures, and Allan Tan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` GPT-4.1 and Gemini Flash 3.1 achieved OOD macro F1-scores from 0.41 to 0.79, the strongest OOD baseline performance. [→ Michael Lawrence Castanares 2026](#michael-lawrence-castanares-2026)

## Evidence

### Michael Lawrence Castanares 2026

Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749

`q2 · i?` · `design · r2`

Zero- and few-shot prompting evaluation of GPT-4.1 and Gemini Flash 3.1 on the OOD Scaria and AF datasets, reported in Results Section 5.2; F1-scores ranged "0.41 to 0.79" with no effect sizes printed.

> "LLMs (GPT4.1 and Gemini-Flash 3.1 lite) showed robust classification performance with the OOD datasets, F1-scores from 0.41 to 0.79."

## Discussion


## Related Claims
- [Model accuracy on Bloom classification drops with question text length, with LLMs degrading least](bloom-signal-dilution-with-text-length.md) — related
- [Text splicing into single sentences improves ML and BERT Bloom classification on the Scaria OOD dataset](text-splicing-improves-ood-bloom-classification.md) — related
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
- [Model retraining on labeled OOD data provides the largest improvement in Bloom classification across models and datasets](model-retraining-largest-ood-improvement.md) — related
- [Appending learning objectives to questions improves Bloom classification on the AF dataset](learning-objectives-anchor-bloom-classification.md) — related
