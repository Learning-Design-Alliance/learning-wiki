---
type: claim
title: Human annotators converge on a similarity threshold above 7 of 10 before offering transfer credit
description: Human annotators converge on a similarity threshold above 7 of 10 before offering transfer credit
id: annotators-require-similarity-above-7-for-credit
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
sources:
  - id: dhivya-chandrasekaran-and-vijay-mago-2022
    resource: "https://doi.org/10.32604/cmc.2022.027236"
    title: "Dhivya Chandrasekaran and Vijay Mago. (2022). Automating Transfer Credit Assessment in Student Mobility - A Natural Language Processing-based Approach. Originally published 2021. [doi:10.32604/cmc.2022.027236](https://doi.org/10.32604/cmc.2022.027236)"
    author: Dhivya Chandrasekaran and Vijay Mago
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human annotators converge on a similarity threshold above 7 of 10 before offering transfer credit

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Four of five annotators offered credit only when course similarity fell above 7 on a 1-10 scale, despite differing in overall leniency. [→ Dhivya Chandrasekaran and Vijay Mago 2022](#dhivya-chandrasekaran-and-vijay-mago-2022)

## Evidence

### Dhivya Chandrasekaran and Vijay Mago 2022

Dhivya Chandrasekaran and Vijay Mago. (2022). Automating Transfer Credit Assessment in Student Mobility - A Natural Language Processing-based Approach. Originally published 2021. [doi:10.32604/cmc.2022.027236](https://doi.org/10.32604/cmc.2022.027236)

`q2 · i?` · `design · r2`

Analysis of the expert survey used to build the benchmark dataset, in which instructors at a Canadian research university annotated seven sending-receiving course pairs. The article reports "4 out of 5 annotators" required similarity above 7; annotators still varied in leniency (e.g., one offered credit for 6 of 7 courses, another for 1 of 7).

> "4 out of 5 annotators oﬀered credit only if they considered the similarity between the courses falls above 7 on the given scale of 1 to 10."

## Discussion


## Related Claims
- [Adjusting the lo_threshold parameter aligns the model's credit decisions with either lenient or strict human annotators](lo-threshold-tuning-matches-annotator-leniency.md) — related
- [Combining taxonomic and semantic similarity of learning outcomes yields higher agreement with human transfer-credit decisions than semantic similarity alone](nlp-transfer-credit-model-outperforms-semantic-only.md) — related
- [Raters differed significantly in severity/leniency in the MFRM analysis](raters-differed-severity-mfrm.md) — related
- [Expert annotation of learning outcome similarity is expensive and learning outcomes are often not publicly available](expert-annotation-of-learning-outcomes-is-expensive.md) — related
