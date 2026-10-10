---
type: claim
title: Of 100 human-audited claims, 39 are fully verifiable, 55 partially verifiable, and 6 not verifiable, with main responses showing stronger provenance than follow-ups
description: Of 100 human-audited claims, 39 are fully verifiable, 55 partially verifiable, and 6 not verifiable, with main responses showing stronger provenance than follow-ups
id: human-audit-claim-verifiability
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: dana-rezazadegan-2026
    resource: "https://arxiv.org/abs/2606.27619"
    title: "Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619"
    author: Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: dana-rezazadegan-2026-2
    resource: "https://arxiv.org/abs/2606.27619"
    title: "Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619"
    author: Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Of 100 human-audited claims, 39 are fully verifiable, 55 partially verifiable, and 6 not verifiable, with main responses showing stronger provenance than follow-ups

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Human assessors verified 39 of 100 claims fully, 55 partially, and 6 not at all due to missing citation or source evidence. [→ Dana Rezazadegan 2026](#dana-rezazadegan-2026)
`q2 i?` Main research-question responses had stronger provenance than follow-up responses: 10 of 11 audited main-response rows were fully verifiable while 56 of 89 follow-up rows were only partially verifiable. [→ Dana Rezazadegan 2026 (2)](#dana-rezazadegan-2026-2)

## Evidence

### Dana Rezazadegan 2026

Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619

`q2 · i?` · `design · r2`

Structured human assessment of 100 claims (51 with stronger and 49 with weaker RAGAS scores) across three audit dimensions: evidence verification, support strength, and interpretative utility, with adjudication for categorical labels.

> "As shown in Fig. 4, 39 claims are fully verifiable, 55 were partially verifiable, and 6 are not verifiable due to missing citation or source evidence."

### Dana Rezazadegan 2026 (2)

Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619

`q2 · i?` · `design · r2`

The human-grounded audit comparing provenance quality between main research-question responses and follow-up responses, attributing partial verifiability to export of full retrieved chunks rather than short exact evidence phrases.

> "Among the audited main-response rows, 10 of 11 were fully verifiable. In contrast, 56 of 89 follow-up rows were only partially verifiable, mainly because several follow-up rows exported the full retrieved chunk rather than a short exact evidence phrase."

## Discussion


## Related Claims
- [DysLexLens achieves a mean Answer Relevancy of 0.75 across 30 responses to research questions and follow-ups on dyslexia-AI Reddit data](dyslexlens-mean-answer-relevancy-075.md) — related
- [LLM-judge evaluation of tutoring sycophancy shows systematic self-judge blind spots and missed sycophancy even under judge consensus](llm-judge-reliability-tutoring-sycophancy.md) — related
- [In a documented exploratory audit, one human-authored manuscript received materially different classifications from five commercial detectors, spanning 0% human to Human Generated](multi-tool-audit-cross-tool-inconsistency.md) — related
- [Of 30 verified hallucinated references, 13 appeared entirely fabricated and 17 were hybrid references combining a real title with fabricated authorship or metadata](hybrid-hallucinated-references-real-title-fake-authors.md) — related
- [Verified hallucinated references at SIGCSE TS increased from 3 in the 2025 proceedings to 17 in the 2026 proceedings, appearing in 2.3% of 2026 papers](sigcse-ts-hallucinations-increased-2025-2026.md) — related
- [Research-question responses score higher Answer Relevancy (0.87) than follow-ups (0.72), while Faithfulness, Context Relevance and Response Groundedness are lower](rq-higher-relevancy-lower-grounding.md) — related
