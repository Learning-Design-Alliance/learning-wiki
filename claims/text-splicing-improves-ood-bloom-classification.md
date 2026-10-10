---
type: claim
title: Text splicing into single sentences improves ML and BERT Bloom classification on the Scaria OOD dataset
description: Text splicing into single sentences improves ML and BERT Bloom classification on the Scaria OOD dataset
id: text-splicing-improves-ood-bloom-classification
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

# Text splicing into single sentences improves ML and BERT Bloom classification on the Scaria OOD dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Splitting questions into sentences and taking the maximum Bloom level raised XGBoost to 0.59 and BERT to 0.62 macro F1 on Scaria. [→ Michael Lawrence Castanares 2026](#michael-lawrence-castanares-2026)

## Evidence

### Michael Lawrence Castanares 2026

Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749

`q2 · i?` · `design · r2`

Numerical experiment applying text splicing (splitting a question on punctuation and classifying each sentence) to pre-trained ML and DistilBERT models on the Scaria OOD dataset; improvements printed as "0.59 and 0.62".

> "Text splicing improved the performance of ML and BERT in the Scaria dataset (see Table 3). In particular, XGBoost and BERT models F1-scores increased to 0.59 and 0.62, respectively."

## Discussion


## Related Claims
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
- [Model retraining on labeled OOD data provides the largest improvement in Bloom classification across models and datasets](model-retraining-largest-ood-improvement.md) — related
- [AI-generated OOD question datasets are longer, syntactically deeper, and overlap less with Bloom trigger verbs than human-curated IID data](ood-aeq-textual-characteristics-differ-iid.md) — related
