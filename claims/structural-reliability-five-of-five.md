---
type: claim
title: In the first full round on version 8, routing, summary-line consistency, and the own-example question were each correct in 5 of 5 runs, and all three prompt-injection attempts were refused
description: In the first full round on version 8, routing, summary-line consistency, and the own-example question were each correct in 5 of 5 runs, and all three prompt-injection attempts were refused
id: structural-reliability-five-of-five
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: byungmoon-cho-2026
    resource: "https://doi.org/10.48550/arXiv.2610.22949"
    title: "Byungmoon Cho. (2026). Designing an AI Agent That Does Not Tutor: Design Rules for Socratic Probing in Introductory Physics. [doi:10.48550/arXiv.2610.22949](https://doi.org/10.48550/arXiv.2610.22949)"
    author: Byungmoon Cho
    q: 1
    i: "?"
    kind: design
    rigour: 3
---

# In the first full round on version 8, routing, summary-line consistency, and the own-example question were each correct in 5 of 5 runs, and all three prompt-injection attempts were refused

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` On version 8 (October 4), routing including retake shifts, summary-line matching, and asking the own-example question were each correct in 5 of 5 runs; the agent refused all three prompt-injection attempts across the version history. [→ Byungmoon Cho 2026](#byungmoon-cho-2026)

## Evidence

### Byungmoon Cho 2026

Byungmoon Cho. (2026). Designing an AI Agent That Does Not Tutor: Design Rules for Socratic Probing in Introductory Physics. [doi:10.48550/arXiv.2610.22949](https://doi.org/10.48550/arXiv.2610.22949)

`q1 · i?` · `design · r3`

Structural-reliability checks in the first full round on version 8: the article states these results check Rules 5.9 and 5.10 and "are not a performance claim". The round was five runs out of more than 40, and every persona was written by the author.

> "routing, including retake shifts, was correct in 5 of 5 runs; the summary line matched the conversation text in 5 of 5; and the own-example question was asked in 5 of 5."

## Discussion


## Related Claims
- [Delimiting Untrusted Learner Text Largely Blocked Authority-Claim Injection on One Model](delimiting-untrusted-learner-text-defeats-authority-claim-injection.md) — related
- [Adding conflict probes cut the answer-paster persona's scores from 4/6 + 1 to 0–1/6 in most later runs](conflict-probes-cut-answer-paster-scores.md) — related
