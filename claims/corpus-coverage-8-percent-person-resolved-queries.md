---
type: claim
title: "Only 8.0% of queries reaching a person duplicated existing corpus content, suggesting the knowledge base was already well used"
description: "Only 8.0% of queries reaching a person duplicated existing corpus content, suggesting the knowledge base was already well used"
id: corpus-coverage-8-percent-person-resolved-queries
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: gupta-2026
    resource: "https://doi.org/10.48550/arxiv.2609.38967"
    title: "Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S. (2026). What Students Actually Ask: Demand Structure and Automation Potential in a Hybrid Support System. arXiv:2609.38967. https://arxiv.org/abs/2609.38967 [doi:10.48550/arxiv.2609.38967](https://doi.org/10.48550/arxiv.2609.38967)"
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

Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S. (2026). What Students Actually Ask: Demand Structure and Automation Potential in a Hybrid Support System. arXiv:2609.38967. https://arxiv.org/abs/2609.38967 [doi:10.48550/arxiv.2609.38967](https://doi.org/10.48550/arxiv.2609.38967)

`q2 · i?` · `design · r2`

TF-IDF cosine-similarity coverage estimation over the deployment record, comparing unlinked person-resolved query text against a proxy corpus built from the 871 corpus-linked queries. Of 213 matched queries, 45 were status enquiries, leaving 6.3% of candidates.

> "Excluding control tokens, 2,664 queries resolved by a person carried no corpus link. At a cosine similarity threshold of 0.70, 8.0% of these matched an existing corpus linked query, at a manually validated match precision of 14 of 15."

## Discussion


## Related Claims
- [At least 20.4% of queries in an online internship programme are status enquiries about pending submissions, which a corpus-grounded AI assistant served only 1.3% of the time](status-enquiries-pending-submissions-assistant-1-3-percent.md) — related
- [Corpus reuse in the deployed support system is concentrated on a single process step: three certificate/offer-letter entries account for 56.8% of 871 resolutions, with a Gini of 0.586 across entries](corpus-reuse-concentrated-single-process-step-gini-0-586.md) — related
- [Operational resolution records require workflow-semantic checks before interpretation: one administrator accounts for 72.7% of attributed human resolutions, most administrative closures occur in synchronous bulk events, and the accepted_derived field encodes resolver identity rather than acceptance](resolution-record-semantics-attribution-and-coding-caveats.md) — related
- [Peer answering in the hybrid support system was fast where it occurred: 70.3% of peer-answered queries closed within one hour, against 1.9% of administrator-answered and 14.8% of script-closed queries](peer-answering-fast-70-percent-within-one-hour.md) — related
