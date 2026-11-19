---
type: claim
title: Combining taxonomic and semantic similarity of learning outcomes yields higher agreement with human transfer-credit decisions than semantic similarity alone
description: Combining taxonomic and semantic similarity of learning outcomes yields higher agreement with human transfer-credit decisions than semantic similarity alone
id: nlp-transfer-credit-model-outperforms-semantic-only
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
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

# Combining taxonomic and semantic similarity of learning outcomes yields higher agreement with human transfer-credit decisions than semantic similarity alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` At a neutral parameter setting, the proposed combined model achieved 85.74% agreement with human annotation of seven course pairs, while a semantic-similarity-only model achieved 54.75% agreement. [→ Dhivya Chandrasekaran and Vijay Mago 2022](#dhivya-chandrasekaran-and-vijay-mago-2022)

## Evidence

### Dhivya Chandrasekaran and Vijay Mago 2022

Dhivya Chandrasekaran and Vijay Mago. (2022). Automating Transfer Credit Assessment in Student Mobility - A Natural Language Processing-based Approach. Originally published 2021. [doi:10.32604/cmc.2022.027236](https://doi.org/10.32604/cmc.2022.027236)

`q2 · i?` · `design · r2`

Results section comparison of the proposed three-pass model against a semantic-similarity-only baseline on the seven-pair benchmark dataset annotated by five domain experts. The combined model reached "85.74% agreement" versus 54.75% for semantic similarity only; no effect size or significance test is printed.

> "The proposed model at a neutral setting achieves 85.74% agreement with the human annotation obtained during the survey while the semantic similarity model achieves only 54.75% agreement."

## Discussion


## Related Claims
- [Human annotators converge on a similarity threshold above 7 of 10 before offering transfer credit](annotators-require-similarity-above-7-for-credit.md) — related
- [Expert annotation of learning outcome similarity is expensive and learning outcomes are often not publicly available](expert-annotation-of-learning-outcomes-is-expensive.md) — related
- [Adjusting the lo_threshold parameter aligns the model's credit decisions with either lenient or strict human annotators](lo-threshold-tuning-matches-annotator-leniency.md) — related
