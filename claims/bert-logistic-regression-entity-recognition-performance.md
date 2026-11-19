---
type: claim
title: A BERT-representation logistic regression entity recognizer reached precision 0.84, recall 0.82 and F1 0.83 on the mathematical questioning dataset
description: A BERT-representation logistic regression entity recognizer reached precision 0.84, recall 0.82 and F1 0.83 on the mathematical questioning dataset
id: bert-logistic-regression-entity-recognition-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: debajyoti-datta-2021
    resource: "https://doi.org/10.48550/arXiv.2112.00985"
    title: "Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown. (2021). Evaluation of mathematical questioning strategies using data collected through weak supervision. NeurIPS 2021 Workshop on Math AI for Education (MATHAI4ED). [doi:10.48550/arXiv.2112.00985](https://doi.org/10.48550/arXiv.2112.00985)"
    author: Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A BERT-representation logistic regression entity recognizer reached precision 0.84, recall 0.82 and F1 0.83 on the mathematical questioning dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The entity recognition module, a logistic regression classifier trained on pre-trained BERT sentence representations, achieved precision 0.84, recall 0.82 and F1 0.83. [→ Debajyoti Datta 2021](#debajyoti-datta-2021)

## Evidence

### Debajyoti Datta 2021

Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown. (2021). Evaluation of mathematical questioning strategies using data collected through weak supervision. NeurIPS 2021 Workshop on Math AI for Education (MATHAI4ED). [doi:10.48550/arXiv.2112.00985](https://doi.org/10.48550/arXiv.2112.00985)

`q2 · i?` · `design · r2`

Reported performance of the entity recognition module, which used Spacy rule-based matchers to create a dataset that was then used to train the logistic regression classifier; the printed metrics are "precision: 0.84, recall: 0.82, f1: 0.83".

> "We used pre-trained BERT sentence representations to train the logistic regression classiﬁer (precision: 0.84, recall: 0.82, f1: 0.83)."

## Discussion


## Related Claims
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
- [A DistilBERT dialogue-act classifier trained on weakly supervised data reached an average F1 score of 0.71 for the mathematical questioning scenario](distilbert-dialogue-act-f1-0-71-weak-supervision.md) — related
