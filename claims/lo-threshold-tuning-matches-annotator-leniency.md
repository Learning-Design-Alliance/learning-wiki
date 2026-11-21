---
type: claim
title: "Adjusting the lo_threshold parameter aligns the model's credit decisions with either lenient or strict human annotators"
description: "Adjusting the lo_threshold parameter aligns the model's credit decisions with either lenient or strict human annotators"
id: lo-threshold-tuning-matches-annotator-leniency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
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

# Adjusting the lo_threshold parameter aligns the model's credit decisions with either lenient or strict human annotators

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` With lo_threshold set at 0.33 and 0.66, the model achieved 85% agreement with the most lenient annotator and the most strict annotator, respectively. [→ Dhivya Chandrasekaran and Vijay Mago 2022](#dhivya-chandrasekaran-and-vijay-mago-2022)

## Evidence

### Dhivya Chandrasekaran and Vijay Mago 2022

Dhivya Chandrasekaran and Vijay Mago. (2022). Automating Transfer Credit Assessment in Student Mobility - A Natural Language Processing-based Approach. Originally published 2021. [doi:10.32604/cmc.2022.027236](https://doi.org/10.32604/cmc.2022.027236)

`q2 · i?` · `design · r2`

Experiment reported in the Results section: the proposed model was re-run varying lo_threshold (0.33, 0.66) on the seven-pair benchmark to demonstrate flexibility, matching the most lenient and most strict annotator at "an agreement of 85%" in each direction.

> "for the lenient setting the lo_threshold parameter is set at 0.33 and 0.66 and the model achieves an agreement of 85% with the most lenient annotator and the most strict annotator, respectively."

## Discussion


## Related Claims
- [Human annotators converge on a similarity threshold above 7 of 10 before offering transfer credit](annotators-require-similarity-above-7-for-credit.md) — related
- [Combining taxonomic and semantic similarity of learning outcomes yields higher agreement with human transfer-credit decisions than semantic similarity alone](nlp-transfer-credit-model-outperforms-semantic-only.md) — related
- [Multi-label annotation of toxic text yields higher alignment with external ML classifiers than forced single-label consensus, though not always higher inter-annotator agreement](multi-label-annotation-higher-classifier-alignment.md) — related
