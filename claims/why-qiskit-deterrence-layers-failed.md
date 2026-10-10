---
type: claim
title: Deterrence layers failed because seeds changed parameters rather than task structure, scaffolding exposed solution steps, and hidden grading verified output consistency rather than authorship or understanding
description: Deterrence layers failed because seeds changed parameters rather than task structure, scaffolding exposed solution steps, and hidden grading verified output consistency rather than authorship or understanding
id: why-qiskit-deterrence-layers-failed
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: alexei-kaltchenko-and-gurnivaj-tiwana-2026
    resource: "https://arxiv.org/abs/2608.19707"
    title: "Alexei Kaltchenko and Gurnivaj Tiwana. (2026). ChatGPT Solves All Tested Qiskit Homework Assignments. arXiv. https://arxiv.org/abs/2608.19707"
    author: Alexei Kaltchenko and Gurnivaj Tiwana
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: alexei-kaltchenko-and-gurnivaj-tiwana-2026-2
    resource: "https://arxiv.org/abs/2608.19707"
    title: "Alexei Kaltchenko and Gurnivaj Tiwana. (2026). ChatGPT Solves All Tested Qiskit Homework Assignments. arXiv. https://arxiv.org/abs/2608.19707"
    author: Alexei Kaltchenko and Gurnivaj Tiwana
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Deterrence layers failed because seeds changed parameters rather than task structure, scaffolding exposed solution steps, and hidden grading verified output consistency rather than authorship or understanding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`

## Subclaims
`q1 i?` Deterministic personalization allowed ChatGPT to produce parameterized solutions because seeds altered parameters rather than creating new reasoning problems. [→ Alexei Kaltchenko and Gurnivaj Tiwana 2026](#alexei-kaltchenko-and-gurnivaj-tiwana-2026)
`q1 i?` Grader acceptance established consistency with expected outputs, not independent authorship or understanding, because graders checked fields and reflection presence without semantic validation of notebook circuits. [→ Alexei Kaltchenko and Gurnivaj Tiwana 2026 (2)](#alexei-kaltchenko-and-gurnivaj-tiwana-2026-2)

## Evidence

### Alexei Kaltchenko and Gurnivaj Tiwana 2026

Alexei Kaltchenko and Gurnivaj Tiwana. (2026). ChatGPT Solves All Tested Qiskit Homework Assignments. arXiv. https://arxiv.org/abs/2608.19707

`q1 · i?` · `design · r2`

The authors' interpretive analysis of the observed failure mode, not a tested comparison. For HW1, bit flips, the measurement map, and the expected count key were deterministic functions of student-visible data, so ChatGPT could construct both the exact output and the required circuit once it parsed those functions.

> "A deterministic seed prevents every student from receiving exactly the same numeric configuration. It does not necessarily create a new reasoning problem."

### Alexei Kaltchenko and Gurnivaj Tiwana 2026 (2)

Alexei Kaltchenko and Gurnivaj Tiwana. (2026). ChatGPT Solves All Tested Qiskit Homework Assignments. arXiv. https://arxiv.org/abs/2608.19707

`q1 · i?` · `design · r2`

The authors' analysis of the grading layers: hidden deterministic references made assignments autogradable but did not prevent ChatGPT from deriving correct answers from the public specification; optional QPY export was not a mandatory gate.

> "Consequently, grader acceptance established consistency with expected outputs, not independent authorship or understanding."

## Discussion


## Related Claims
- [ChatGPT produced executed, grader-accepted submissions for all three fixed personalized Qiskit assignment instances in 150 of 150 sessions](chatgpt-completes-all-150-qiskit-homework-sessions.md) — a narrower finding that bears on this claim
- [Moral Unease, reported by 190 participants, reflects authorship guilt and a gap between AI output quality and actual understanding](moral-unease-authorship-guilt-understanding-gap.md) — related
- [Reviewed literature reports risks of overreliance, AI errors in complex tasks, and students' uncritical acceptance of AI-generated outputs](ai-math-risks-overreliance-errors-uncritical-trust.md) — related
