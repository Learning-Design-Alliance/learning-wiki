---
type: claim
title: A page-by-page, rubric-guided multimodal LLM workflow graded an authentic handwritten exam in about three hours at roughly $100 in token costs, versus about $3,500 in TA time
description: A page-by-page, rubric-guided multimodal LLM workflow graded an authentic handwritten exam in about three hours at roughly $100 in token costs, versus about $3,500 in TA time
id: ai-grading-workflow-feasibility-cost
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: jan-cvengros-and-gerd-kortemeyer-2026
    resource: "https://doi.org/10.1007/s44163-026-01606-4"
    title: "Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4"
    author: Jan Cvengros and Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: jan-cvengros-and-gerd-kortemeyer-2026-2
    resource: "https://doi.org/10.1007/s44163-026-01606-4"
    title: "Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4"
    author: Jan Cvengros and Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A page-by-page, rubric-guided multimodal LLM workflow graded an authentic handwritten exam in about three hours at roughly $100 in token costs, versus about $3,500 in TA time

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Each page submission took between 50 and 60 seconds; running up to 30 agents in parallel allowed grading the exams in about three hours. [→ Jan Cvengros and Gerd Kortemeyer 2026](#jan-cvengros-and-gerd-kortemeyer-2026)
`q2 i?` The workflow used 32.15 million tokens costing approximately $100, compared to about $3,500 for TA grading of the whole exam for all 459 students. [→ Jan Cvengros and Gerd Kortemeyer 2026 (2)](#jan-cvengros-and-gerd-kortemeyer-2026-2)

## Evidence

### Jan Cvengros and Gerd Kortemeyer 2026

Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4

`q2 · i?` · `design · r2`

Operational workflow report (Sect. 3.2) mirroring an intended production deployment: page images of student work plus rubric pages were submitted one page at a time to gpt-o4-mini/high-vision via ephemeral URLs, producing structured JSON output per part.

> "Each submission took between 50  and 60  s. At times we ran 30  agents in parallel, allowing us to grade the exams in about three hours"

### Jan Cvengros and Gerd Kortemeyer 2026 (2)

Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4

`q2 · i?` · `design · r2`

Cost accounting in Sect. 3.2 compares the token cost with 16 TAs × 5 h × $44/h ≈ $3,500 for grading the whole exam for all 459 students, using the ETH-stipulated gross hourly income of CHF 30.70 plus employer contributions.

> "We used 32.15 million tokens, costing approximately $100 in total"

## Discussion


## Related Claims
- [In a real academic pilot, AISSA processed 90 presentations reliably at 1–3 minutes per submission and an estimated cost of $0.06–0.07 USD per evaluation](aissa-pilot-reliable-low-cost-processing.md) — related
- [Human scoring and feedback for HDR takes about 11 minutes 30 seconds per learner, while GPT-based scoring and feedback is nearly instant](hdr-human-scoring-time-burden.md) — related
- [Structure and layout of the exam pages strongly contribute to the success of the multimodal grading method and, for now, appear to be required](structure-and-layout-required-for-ai-grading.md) — related
