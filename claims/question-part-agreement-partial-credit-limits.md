---
type: claim
title: "Round II raised exact question-part agreement from about 63% to about 70% and cut parts differing by more than one point from about 13% to 7%, while exact partial-credit scoring remained hardest"
description: "Round II raised exact question-part agreement from about 63% to about 70% and cut parts differing by more than one point from about 13% to 7%, while exact partial-credit scoring remained hardest"
id: question-part-agreement-partial-credit-limits
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: praveen-pathak-2026
    resource: "https://arxiv.org/abs/2608.20521"
    title: "Praveen Pathak, Siddharth Tiwary, Charudatt Kadolkar, Vijay Singh, David Rakestraw, Shirish Pathare, and Anwesh Mazumdar. (2026). Large-scale AI grading of handwritten physics assessments: Score agreement and Olympiad team selection outcomes. https://arxiv.org/abs/2608.20521"
    author: Praveen Pathak, Siddharth Tiwary, Charudatt Kadolkar, Vijay Singh, David Rakestraw, Shirish Pathare, and Anwesh Mazumdar
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: praveen-pathak-2026-2
    resource: "https://arxiv.org/abs/2608.20521"
    title: "Praveen Pathak, Siddharth Tiwary, Charudatt Kadolkar, Vijay Singh, David Rakestraw, Shirish Pathare, and Anwesh Mazumdar. (2026). Large-scale AI grading of handwritten physics assessments: Score agreement and Olympiad team selection outcomes. https://arxiv.org/abs/2608.20521"
    author: Praveen Pathak, Siddharth Tiwary, Charudatt Kadolkar, Vijay Singh, David Rakestraw, Shirish Pathare, and Anwesh Mazumdar
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Round II raised exact question-part agreement from about 63% to about 70% and cut parts differing by more than one point from about 13% to 7%, while exact partial-credit scoring remained hardest

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`

## Subclaims
`q2 i?` Across 7058 official question parts, exact agreement rose from about 63% (RI) to about 70% (RII), and parts differing by more than one point fell from about 13% to 7%. [→ Praveen Pathak 2026](#praveen-pathak-2026)
`q2 i?` Exact partial-credit agreement on human-partial parts rose only from 24.6% to 32.8%, and exact partial-credit scoring remained the most difficult case. [→ Praveen Pathak 2026 (2)](#praveen-pathak-2026-2)

## Evidence

### Praveen Pathak 2026

Praveen Pathak, Siddharth Tiwary, Charudatt Kadolkar, Vijay Singh, David Rakestraw, Shirish Pathare, and Anwesh Mazumdar. (2026). Large-scale AI grading of handwritten physics assessments: Score agreement and Olympiad team selection outcomes. https://arxiv.org/abs/2608.20521

`q2 · i?` · `causal · r1`

Question-part-level comparison of AI versus official scores using d = |AI−Human| in raw points across OE1, OE2, and QM. The article reports exact agreement rising "from about 63% of parts" to "about 70%"; no effect size is printed.

> "Across all 7058 official question parts, RI matched the human score exactly in about 63% of parts. RII increased exact agreement to about 70%, and reduced parts differing by more than one point from about 13% to 7%."

### Praveen Pathak 2026 (2)

Praveen Pathak, Siddharth Tiwary, Charudatt Kadolkar, Vijay Singh, David Rakestraw, Shirish Pathare, and Anwesh Mazumdar. (2026). Large-scale AI grading of handwritten physics assessments: Score agreement and Olympiad team selection outcomes. https://arxiv.org/abs/2608.20521

`q2 · i?` · `design · r3`

Subset analysis of the 1834 human-partial question parts in RII (Fig. 4). The article reports "exact agreement rose from 24.6% in RI to 32.8% in RII"; among both-partial cases MAD fell from 0.92 to 0.72 raw marks. No effect size is printed.

> "For human-partial parts, exact agreement rose from 24.6% in RI to 32.8% in RII."

## Discussion


## Related Claims
- [AI total scores correlate strongly with official human scores on handwritten physics assessments (r = 0.91–0.97 in Round I; 0.93–0.96 in Round II)](ai-human-total-score-correlation-handwritten-physics.md) — related
- [AI self-reported confidence flags identify parts with smaller grading differences, but some high-confidence parts still differ from official scores by more than one point](confidence-flags-triage-human-review.md) — related
- [Focused rubric refinement that made required physics and scoring conditions explicit reduced AI–official disagreements on targeted questions (e.g., Grover item MAD 1.1 to 0.4 marks, r 0.70 to 0.82)](explicit-rubric-conditions-reduce-ai-disagreement.md) — a narrower finding that bears on this claim
- [The revised Round II grading workflow reduced AI over-awarding and total-score MAD, most clearly for OE1 (7.1% to 4.8%) and QM (9.4% to 3.8%)](revised-workflow-reduces-overawarding-mad.md) — related
