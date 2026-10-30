---
type: claim
title: "An unweighted ensemble of LSA and n-gram co-occurrence achieves 96% overall accuracy in summary content assessment, outperforming LSA, n-gram, BLEU and ROUGE on five of six tests"
description: "An unweighted ensemble of LSA and n-gram co-occurrence achieves 96% overall accuracy in summary content assessment, outperforming LSA, n-gram, BLEU and ROUGE on five of six tests"
id: ensemble-lsa-ngram-96-percent-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-30
evidence_strength: moderate
newest_evidence: 2009
sources:
  - id: automatic-summary-assessment-for-intelligent-tutoring-systems-2009
    resource: "https://doi.org/10.1016/j.compedu.2009.05.008"
    title: "Automatic Summary Assessment for Intelligent Tutoring Systems. (2009). Preprint submitted to Elsevier February 26, 2009. https://doi.org/10.1016/j.compedu.2009.05.008"
    author: Automatic Summary Assessment for Intelligent Tutoring Systems
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# An unweighted ensemble of LSA and n-gram co-occurrence achieves 96% overall accuracy in summary content assessment, outperforming LSA, n-gram, BLEU and ROUGE on five of six tests

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The ensemble approach outperforms all base techniques in all tests except the content test, with overall accuracy of 96% versus 87% for BLEU. [→ Automatic Summary Assessment for Intelligent Tutoring Systems 2009](#automatic-summary-assessment-for-intelligent-tutoring-systems-2009)

## Evidence

### Automatic Summary Assessment for Intelligent Tutoring Systems 2009

Automatic Summary Assessment for Intelligent Tutoring Systems. (2009). Preprint submitted to Elsevier February 26, 2009. https://doi.org/10.1016/j.compedu.2009.05.008

`q2 · i?` · `design · r2`

Numerical comparison of the ensemble against LSA, n-gram co-occurrence, BLEU and ROUGE on six tests over 50 student summaries, reported in Table 1 and Figure 5. The article states the ensemble is "able to outperform all the base techniques in all the tests except for the content test".

> "It can be observed that the ensemble system is able to outperform all the base techniques in all the tests except for the content test. For the other tests, the ensemble approach is capable of outperforming the other techniques by at least 0.003 and at most 0.774 in terms of accuracy."

## Discussion


## Related Claims
- [BLEU produced low scores when ensembled with other techniques, possibly due to brevity penalty over-penalization, so it was excluded from the ensemble](bleu-excluded-brevity-penalty.md) — related
- [Unweighted voting simplifies processing when underlying techniques have similar performance](unweighted-voting-similar-performance.md) — a narrower finding that bears on this claim
- [ROUGE overall performance is quite poor compared with LSA, BLEU and n-gram co-occurrence for summary assessment](rouge-poor-summary-assessment.md) — related
- [Ensemble modeling of multiple LLM scorers yields performance gains in automated divergent thinking scoring](ensemble-models-performance-gains-llm-scoring.md) — a broader claim this one bears on
