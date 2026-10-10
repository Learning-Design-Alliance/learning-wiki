---
type: claim
title: AI self-reported confidence flags identify parts with smaller grading differences, but some high-confidence parts still differ from official scores by more than one point
description: AI self-reported confidence flags identify parts with smaller grading differences, but some high-confidence parts still differ from official scores by more than one point
id: confidence-flags-triage-human-review
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
    kind: design
    rigour: 3
  - id: praveen-pathak-2026-2
    resource: "https://arxiv.org/abs/2608.20521"
    title: "Praveen Pathak, Siddharth Tiwary, Charudatt Kadolkar, Vijay Singh, David Rakestraw, Shirish Pathare, and Anwesh Mazumdar. (2026). Large-scale AI grading of handwritten physics assessments: Score agreement and Olympiad team selection outcomes. https://arxiv.org/abs/2608.20521"
    author: Praveen Pathak, Siddharth Tiwary, Charudatt Kadolkar, Vijay Singh, David Rakestraw, Shirish Pathare, and Anwesh Mazumdar
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# AI self-reported confidence flags identify parts with smaller grading differences, but some high-confidence parts still differ from official scores by more than one point

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r3` · `q2`

## Subclaims
`q2 i?` In every available comparison, high-confidence question parts had much lower MAD than medium- or low-confidence parts (e.g., OE1 RII 6.0% vs 17.0%; QM RII 9.8% vs 28.2%). [→ Praveen Pathak 2026](#praveen-pathak-2026)
`q2 i?` Accepting all high-confidence OE2 parts without review would still have accepted 87 parts differing from official scores by more than one point, so flags suit triage rather than final acceptance. [→ Praveen Pathak 2026 (2)](#praveen-pathak-2026-2)

## Evidence

### Praveen Pathak 2026

Praveen Pathak, Siddharth Tiwary, Charudatt Kadolkar, Vijay Singh, David Rakestraw, Shirish Pathare, and Anwesh Mazumdar. (2026). Large-scale AI grading of handwritten physics assessments: Score agreement and Olympiad team selection outcomes. https://arxiv.org/abs/2608.20521

`q2 · i?` · `design · r3`

RII confidence-flag analysis across all examinations (Fig. 12); OE2 theory showed 5.3% versus 27.1% and experiment 6.9% versus 25.6%. The article reports "6.0% for high-confidence parts and 17.0% for medium- or low-confidence parts"; no effect size is printed.

> "OE1 RII had MAD% values of 6.0% for high-confidence parts and 17.0% for medium- or low-confidence parts. QM RII had 9.8% versus 28.2%."

### Praveen Pathak 2026 (2)

Praveen Pathak, Siddharth Tiwary, Charudatt Kadolkar, Vijay Singh, David Rakestraw, Shirish Pathare, and Anwesh Mazumdar. (2026). Large-scale AI grading of handwritten physics assessments: Score agreement and Olympiad team selection outcomes. https://arxiv.org/abs/2608.20521

`q2 · i?` · `design · r3`

OE2 confidence analysis over 1898 official question parts (1482 theory, 416 experiment). The article reports that "87 of these still differed from the official human score by more than one point"; no effect size is printed.

> "Accepting every high-confidence part with no review flag would have accepted 1724 parts; 87 of these still differed from the official human score by more than one point."

## Discussion


## Related Claims
- [AI total scores correlate strongly with official human scores on handwritten physics assessments (r = 0.91–0.97 in Round I; 0.93–0.96 in Round II)](ai-human-total-score-correlation-handwritten-physics.md) — related
- [Round II raised exact question-part agreement from about 63% to about 70% and cut parts differing by more than one point from about 13% to 7%, while exact partial-credit scoring remained hardest](question-part-agreement-partial-credit-limits.md) — related
- [Focused rubric refinement that made required physics and scoring conditions explicit reduced AI–official disagreements on targeted questions (e.g., Grover item MAD 1.1 to 0.4 marks, r 0.70 to 0.82)](explicit-rubric-conditions-reduce-ai-disagreement.md) — related
