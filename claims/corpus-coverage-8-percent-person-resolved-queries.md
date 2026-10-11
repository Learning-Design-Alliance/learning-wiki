---
type: claim
title: "Only 8.0% of queries reaching a person duplicated existing corpus content, suggesting the knowledge base was already well used"
description: "Only 8.0% of queries reaching a person duplicated existing corpus content, suggesting the knowledge base was already well used"
id: corpus-coverage-8-percent-person-resolved-queries
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: gupta-2026
    resource: "https://arxiv.org/abs/2609.38967"
    title: "Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S. (2026). What Students Actually Ask: Demand Structure and Automation Potential in a Hybrid Support System. arXiv:2609.38967. https://arxiv.org/abs/2609.38967"
    author: Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Only 8.0% of queries reaching a person duplicated existing corpus content, suggesting the knowledge base was already well used

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Of 2,664 person-resolved queries with no corpus link, 8.0% matched existing corpus-linked queries at a cosine similarity threshold of 0.70, at a manually validated match precision of 14 of 15; the estimate falls to 6.5% at threshold 0.85. [→ Gupta 2026](#gupta-2026)

## Evidence

### Gupta 2026

Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S. (2026). What Students Actually Ask: Demand Structure and Automation Potential in a Hybrid Support System. arXiv:2609.38967. https://arxiv.org/abs/2609.38967

`q2 · i?` · `design · r2`

TF-IDF cosine-similarity coverage estimation over the deployment record, comparing unlinked person-resolved query text against a proxy corpus built from the 871 corpus-linked queries. Of 213 matched queries, 45 were status enquiries, leaving 6.3% of candidates.

> "Excluding control tokens, 2,664 queries resolved by a person carried no corpus link. At a cosine similarity threshold of 0.70, 8.0% of these matched an existing corpus linked query, at a manually validated match precision of 14 of 15."

## Discussion


## Related Claims
- [At least 20.4% of queries in an online internship programme are status enquiries about pending submissions, which a corpus-grounded AI assistant served only 1.3% of the time](status-enquiries-pending-submissions-assistant-1-3-percent.md) — related
