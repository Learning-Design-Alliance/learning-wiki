---
type: claim
title: In an evaluation with eight experienced users, most utterances were correctly classified by the NLP components, with only certain utterance types always routed to the human supervisor
description: In an evaluation with eight experienced users, most utterances were correctly classified by the NLP components, with only certain utterance types always routed to the human supervisor
id: eight-user-evaluation-utterance-routing
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

# In an evaluation with eight experienced users, most utterances were correctly classified by the NLP components, with only certain utterance types always routed to the human supervisor

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across eight users with teaching experience conversing with the system twice, certain utterances were always sent to the supervisor, but for most cases the NLP components correctly classified the utterances. [→ Debajyoti Datta 2021](#debajyoti-datta-2021)

## Evidence

### Debajyoti Datta 2021

Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown. (2021). Evaluation of mathematical questioning strategies using data collected through weak supervision. NeurIPS 2021 Workshop on Math AI for Education (MATHAI4ED). [doi:10.48550/arXiv.2112.00985](https://doi.org/10.48550/arXiv.2112.00985)

`q2 · i?` · `design · r2`

Analysis of user utterances from the evaluation, in which "The evaluation included eight users with teaching experience (ages 24-60), each conversing with the system twice." Table 3 categorizes utterances as always supervisor (e.g., chit-chat, out-of-domain), always AI (e.g., questions about dimensions, greetings), or a mix, with occurrence counts printed per category.

> "Certain utterances were always sent to the supervisor. However for most cases, the NLP components could correctly classify the utterances."

## Discussion


## Related Claims
- [NLP models classify factual (knowledge transmitter) learner questions well but face challenges distinguishing higher-order facilitator and co-learner questions](nlp-models-excel-factual-struggle-higher-order-questions.md) — related
