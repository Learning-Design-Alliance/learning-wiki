---
type: claim
title: All surveyed automatic question difficulty prediction studies frame the task as supervised learning, mostly as classification of pre-defined difficulty categories
description: All surveyed automatic question difficulty prediction studies frame the task as supervised learning, mostly as classification of pre-defined difficulty categories
id: difficulty-prediction-supervised-dominant
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: samah-alkhuzaey-2023
    resource: "https://doi.org/10.1007/s40593-023-00362-1"
    title: "Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma. (2023). Text-based Question Difficulty Prediction: A Systematic Review of Automatic Approaches. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00362-1"
    author: Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma
    q: 2
    i: "?"
    kind: review
    rigour: 3
---

# All surveyed automatic question difficulty prediction studies frame the task as supervised learning, mostly as classification of pre-defined difficulty categories

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r3` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The reviewed studies address question difficulty estimation as a supervised problem trained on ground-truth-labelled questions, predominantly as binary or multi-class classification. [→ Samah AlKhuzaey 2023](#samah-alkhuzaey-2023)

## Evidence

### Samah AlKhuzaey 2023

Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma. (2023). Text-based Question Difficulty Prediction: A Systematic Review of Automatic Approaches. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00362-1

`q2 · i?` · `review · r3`

The review's synthesis of its 55 included studies reports that every study treated difficulty prediction as supervised learning with labelled ground truth, and that most framed it as binary or multi-class classification of pre-defined difficulty categories. The review attributes this dominance to pre-defined categories, scarce training data, and alignment with expert difficulty perceptions.

> "all of the studies we considered had addressed the task of question difficulty estimation as a supervised problem, whereby a dataset containing questions labelled with difficulty levels (i.e. ground truth) was used to train a model to predict the difficulty level of new questions."

## Discussion


## Related Claims
- [Ground-truth difficulty labels in reviewed studies come roughly equally from expert/annotator labelling (34%), Classical Test Theory (34%), and Item Response Theory (26%)](ground-truth-labelling-methods-distribution.md) — a narrower finding that bears on this claim
- [Model retraining on labeled OOD data provides the largest improvement in Bloom classification across models and datasets](model-retraining-largest-ood-improvement.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
