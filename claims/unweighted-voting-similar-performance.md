---
type: claim
title: Unweighted voting simplifies processing when underlying techniques have similar performance
description: Unweighted voting simplifies processing when underlying techniques have similar performance
id: unweighted-voting-similar-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-30
evidence_strength: weak
newest_evidence: 2009
sources:
  - id: automatic-summary-assessment-for-intelligent-tutoring-systems-2009
    resource: "https://doi.org/10.1016/j.compedu.2009.05.008"
    title: "Automatic Summary Assessment for Intelligent Tutoring Systems. (2009). Preprint submitted to Elsevier February 26, 2009. https://doi.org/10.1016/j.compedu.2009.05.008"
    author: Automatic Summary Assessment for Intelligent Tutoring Systems
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Unweighted voting simplifies processing when underlying techniques have similar performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Because LSA and n-gram co-occurrence have roughly the same performance, unweighted voting simplifies the ensemble's processing. [→ Automatic Summary Assessment for Intelligent Tutoring Systems 2009](#automatic-summary-assessment-for-intelligent-tutoring-systems-2009)

## Evidence

### Automatic Summary Assessment for Intelligent Tutoring Systems 2009

Automatic Summary Assessment for Intelligent Tutoring Systems. (2009). Preprint submitted to Elsevier February 26, 2009. https://doi.org/10.1016/j.compedu.2009.05.008

`q1 · i?` · `design · r2`

Authors' design rationale (analytical argument, not a tested result): since the two techniques have "roughly the same performance", their weights would be similar, so unweighted voting "will simplify the amount of processing required".

> "Furthermore, as the LSA and n-gram co-occurrence techniques have roughly the same performance, both techniques will have very similar weights if the weighted approach is used. Since the weights are similar, the use of the unweighted approach will simplify the amount of processing required by the ensemble approach."

## Discussion


## Related Claims
- [An unweighted ensemble of LSA and n-gram co-occurrence achieves 96% overall accuracy in summary content assessment, outperforming LSA, n-gram, BLEU and ROUGE on five of six tests](ensemble-lsa-ngram-96-percent-accuracy.md) — a broader claim this one bears on
- [Both pedagogy-expertise-weighted and unanimous-vote ensembles frequently worsen LLM alignment with student learning](ensembling-worsens-llm-alignment-with-learning.md) — reports the opposite
