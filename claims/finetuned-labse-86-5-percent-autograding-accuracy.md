---
type: claim
title: "Fine-tuned LaBSE achieves about 86.5% accuracy classifying all answers as correct or incorrect on a large multilingual dataset"
description: "Fine-tuned LaBSE achieves about 86.5% accuracy classifying all answers as correct or incorrect on a large multilingual dataset"
id: finetuned-labse-86-5-percent-autograding-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: johannes-schneider-2023
    resource: "https://doi.org/10.1007/s40593-022-00289-z"
    title: "Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z"
    author: Johannes Schneider, Robin Richner, Micha Riser
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned LaBSE achieves about 86.5% accuracy classifying all answers as correct or incorrect on a large multilingual dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A hyperparameter-tuned LaBSE model classifies about 86.5% of question-answer pairs correctly as correct or incorrect when grading all samples. [→ Johannes Schneider 2023](#johannes-schneider-2023)

## Evidence

### Johannes Schneider 2023

Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z

`q2 · i?` · `design · r2`

Numerical evaluation on the held-out test dataset DV of the Classtime corpus, with the single similarity threshold T* chosen to maximize accuracy. Overall accuracy of the tuned LaBSE model is "maximized for a threshold T∗ = 0.76 leading to an accuracy of C∗ = 86.5%".

> "For the dataset DV overall accuracy is maximized for a threshold T∗ = 0.76 leading to an accuracy of C∗ = 86.5% ."

## Discussion


## Related Claims
- [Deferring difficult question-answer pairs to humans raises grading accuracy, with 62% of samples classified at 92% accuracy](deferring-difficult-answers-raises-accuracy-92-percent.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [The fine-tuned BERT model generalizes to an external dataset collected by a different research team, maintaining almost perfect agreement with human coders](bert-generalizes-external-self-affirmation-dataset.md) — related
- [Autograding is most accurate for numeric answers, and error rates vary less than 8% across languages](numeric-answers-most-accurate-language-variation-under-8.md) — related
- [Under unseen-answers evaluation, the German Transformer model's F-Scores are numerically similar to state-of-the-art Transformer results for English](german-english-fscore-comparable.md) — related
