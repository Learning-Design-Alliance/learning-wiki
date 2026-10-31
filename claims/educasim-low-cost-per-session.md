---
type: claim
title: Simulated role play sessions cost $0.05-$0.10 each in the EducaSim deployment
description: Simulated role play sessions cost $0.05-$0.10 each in the EducaSim deployment
id: educasim-low-cost-per-session
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: cameron-mohne-2026
    resource: "https://doi.org/10.48550/arxiv.2603.11444"
    title: "Cameron Mohne, Nicholas Vo, Dora Demszky, Chris Piech. (2026). EducaSim: Interactive Simulacra for CS1 Instructional Practice. https://arxiv.org/abs/2603.11444 [doi:10.48550/arxiv.2603.11444](https://doi.org/10.48550/arxiv.2603.11444)"
    author: Cameron Mohne, Nicholas Vo, Dora Demszky, Chris Piech
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Simulated role play sessions cost $0.05-$0.10 each in the EducaSim deployment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: local conditions change quickly

## Subclaims
`q2 i?` Using GPT 4.1-mini for text generation and Whisper-1 for transcription, per-session costs ranged from $0.05 to $0.10, with total hosting and API costs under $5 for 150 users. [→ Cameron Mohne 2026](#cameron-mohne-2026)

## Evidence

### Cameron Mohne 2026

Cameron Mohne, Nicholas Vo, Dora Demszky, Chris Piech. (2026). EducaSim: Interactive Simulacra for CS1 Instructional Practice. https://arxiv.org/abs/2603.11444 [doi:10.48550/arxiv.2603.11444](https://doi.org/10.48550/arxiv.2603.11444)

`q2 · i?` · `design · r2`

Cost accounting from the deployment's methodology section: the platform uses GPT 4.1-mini and Whisper-1, and "The cost-per-session currently can range from $0.05 - $0.10 depending on duration"; hosting and LLM API calls totaled less than $5 for 150 users at the time of writing.

> "EducaSim utilizes GPT 4.1-mini and Whisper-1 for text generation and audio transcription respectively. The cost-per-session currently can range from $0.05 - $0.10 depending on duration."

## Discussion


## Related Claims
- [Teachers who engaged with EducaSim generally viewed it as a positive experience](educasim-positive-teacher-sentiment-254-sessions.md) — related
- In a real academic pilot, AISSA processed 90 presentations reliably at 1–3 minutes per submission and an estimated cost of $0.06–0.07 USD per evaluation — related
- [A deployment-hardening rehearsal with 50 distinct learner accounts recorded 50 completed sessions, 50 successful board pulls and 50 denials of student analytics access, with a median API session time of 3.064 s](hardening-rehearsal-50-sessions-and-access-denials.md) — related
- [Running the Socrates playground and grader incurred low cost, with even gpt-4o consuming only $169.90](socrates-low-operational-cost.md) — related
- [Video review sessions impose substantial time costs, with review sessions lasting roughly 30–90 minutes, and monetary costs are rarely reported](video-review-time-cost-sessions.md) — related
