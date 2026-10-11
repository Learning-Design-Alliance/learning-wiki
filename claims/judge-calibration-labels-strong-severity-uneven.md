---
type: claim
title: "The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain"
description: "The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain"
id: judge-calibration-labels-strong-severity-uneven
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: yubo-li-2026
    resource: "https://arxiv.org/abs/2607.22606"
    title: "Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606"
    author: Yubo Li, Rema Padman, Ramayya Krishnan
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: yubo-li-2026-2
    resource: "https://arxiv.org/abs/2607.22606"
    title: "Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606"
    author: Yubo Li, Rema Padman, Ramayya Krishnan
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` On the 146 pairs where both annotators agree, judge agreement is 87.7% (κ = 0.842; macro-F1 0.841). [→ Yubo Li 2026](#yubo-li-2026)
`q2 i?` Severity agreement is less settled: judge agreement is 65.3% with annotator A (κ = 0.385) but 93.9% with annotator B (κ = 0.827), with medium-tier boundaries particularly uncertain. [→ Yubo Li 2026 (2)](#yubo-li-2026-2)

## Evidence

### Yubo Li 2026

Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606

`q2 · i?` · `associational · r2`

Human-annotation study of 200 pairs stratified 40 per judge label, independently labelled by two annotators with judge outputs hidden. Inter-annotator agreement is 73.0% (κ = 0.655); the article notes the subset score is unsuitable as population accuracy.

> "On the 146 pairs where A and B agree, judge agreement is 87.7% (κ= 0.842 ; macro-F1 0.841). Per-label F1 on this subset is 1.00 for ABSENT, 0.83 CONSISTENT, 0.70 COMPLEMENTARY, 0.69 DIVERGENT, and 0.99 CONTRADICTORY."

### Yubo Li 2026 (2)

Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606

`q2 · i?` · `associational · r2`

Severity-calibration subset of the same 200-pair annotation study, summarized in Table 1 showing medium-tier matches are particularly uncertain. The article therefore uses severity only as a review flag, without treating either annotator as an adjudicated clinical reference.

> "Among 49 pairs with shared relationship labels and three available severity ratings, A–B agreement is 67.3% ( κ= 0.425 ); judge agreement is 65.3% with A (κ= 0.385 ) and 93.9% with B (κ= 0.827 )."

## Discussion


## Related Claims
-
