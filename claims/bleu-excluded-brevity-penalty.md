---
type: claim
title: BLEU produced low scores when ensembled with other techniques, possibly due to brevity penalty over-penalization, so it was excluded from the ensemble
description: BLEU produced low scores when ensembled with other techniques, possibly due to brevity penalty over-penalization, so it was excluded from the ensemble
id: bleu-excluded-brevity-penalty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-30
evidence_strength: weak
newest_evidence: 2009
recheck_by: 2012
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

# BLEU produced low scores when ensembled with other techniques, possibly due to brevity penalty over-penalization, so it was excluded from the ensemble

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2012**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` BLEU was dropped from the ensemble after producing low scores, attributed to possible brevity penalty over-penalization. [→ Automatic Summary Assessment for Intelligent Tutoring Systems 2009](#automatic-summary-assessment-for-intelligent-tutoring-systems-2009)

## Evidence

### Automatic Summary Assessment for Intelligent Tutoring Systems 2009

Automatic Summary Assessment for Intelligent Tutoring Systems. (2009). Preprint submitted to Elsevier February 26, 2009. https://doi.org/10.1016/j.compedu.2009.05.008

`q1 · i?` · `design · r2`

Authors' interpretation of their evaluation of four techniques: BLEU "produced low scores in its performance when ensembled with other techniques", attributed to "the brevity penalty over penalization". This is an author interpretation rather than a tested result.

> "However, we found that BLEU produced low scores in its perfor- mance when ensembled with other techniques. This might due to the brevity penalty over penalization."

## Discussion


## Related Claims
- [An unweighted ensemble of LSA and n-gram co-occurrence achieves 96% overall accuracy in summary content assessment, outperforming LSA, n-gram, BLEU and ROUGE on five of six tests](ensemble-lsa-ngram-96-percent-accuracy.md) — related
