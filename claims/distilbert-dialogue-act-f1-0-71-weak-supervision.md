---
type: claim
title: A DistilBERT dialogue-act classifier trained on weakly supervised data reached an average F1 score of 0.71 for the mathematical questioning scenario
description: A DistilBERT dialogue-act classifier trained on weakly supervised data reached an average F1 score of 0.71 for the mathematical questioning scenario
id: distilbert-dialogue-act-f1-0-71-weak-supervision
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

# A DistilBERT dialogue-act classifier trained on weakly supervised data reached an average F1 score of 0.71 for the mathematical questioning scenario

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The intent classification stage for dialogue acts achieved an average F1 score of 0.71 on the dataset collected through weak supervision. [→ Debajyoti Datta 2021](#debajyoti-datta-2021)

## Evidence

### Debajyoti Datta 2021

Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown. (2021). Evaluation of mathematical questioning strategies using data collected through weak supervision. NeurIPS 2021 Workshop on Math AI for Education (MATHAI4ED). [doi:10.48550/arXiv.2112.00985](https://doi.org/10.48550/arXiv.2112.00985)

`q2 · i?` · `design · r2`

Performance of the dialogue act module of the conversational agent, reported in the section on the uncertainty-based dialogue system. Uncertainty was measured with Active Dropout, and the model used was DistilBERT; the printed result is "The average F1 score was 0.71".

> "The average F1 score was 0.71 for the dataset collected through weak supervision. The model used was DistilBERT [Sanh et al., 2019]."

## Discussion


## Related Claims
- [A BERT-representation logistic regression entity recognizer reached precision 0.84, recall 0.82 and F1 0.83 on the mathematical questioning dataset](bert-logistic-regression-entity-recognition-performance.md) — related
- [Weakly supervised concept acquisition reaches F1 of 0.861 for concept extraction and 0.905 for prerequisite discovery on an expert-annotated evaluation set](mooccubex-concept-acquisition-f1-quality.md) — related
