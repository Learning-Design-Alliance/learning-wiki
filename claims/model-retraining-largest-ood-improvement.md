---
type: claim
title: Model retraining on labeled OOD data provides the largest improvement in Bloom classification across models and datasets
description: Model retraining on labeled OOD data provides the largest improvement in Bloom classification across models and datasets
id: model-retraining-largest-ood-improvement
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

# Model retraining on labeled OOD data provides the largest improvement in Bloom classification across models and datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Retraining raised XGBoost to 0.82 (out-performing BERT at 0.77) on Scaria and BERT to 0.50 on AF, at par with the best LLM (0.51). [→ Michael Lawrence Castanares 2026](#michael-lawrence-castanares-2026)

## Evidence

### Michael Lawrence Castanares 2026

Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749

`q2 · i?` · `design · r2`

Retraining experiment on labeled OOD datasets reported in Results Section 5.4 (Tables 4-5); XGBoost reached "0.82 versus 0.77" on Scaria and BERT "0.50 versus 0.30" on AF. No effect sizes printed.

> "With retraining, XGBoost model also out-perform BERT model (0.82 versus 0.77). With the AF dataset, BERT was better performing than XGBoost. BERT performance improved following retraining (0.50 versus 0.30) at par with the best performing LLMs for AF dataset (0.51, GPT4.1 - ZS)."

## Discussion


## Related Claims
- [Retrained BERT relies on high-impact nouns, verbs, and adjectives for correct predictions, but this reliance is muted on the AF dataset](lime-pos-reliance-varies-by-dataset.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Text splicing into single sentences improves ML and BERT Bloom classification on the Scaria OOD dataset](text-splicing-improves-ood-bloom-classification.md) — related
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
- [Appending learning objectives to questions improves Bloom classification on the AF dataset](learning-objectives-anchor-bloom-classification.md) — related
