---
type: claim
title: Optional IBM Quantum hardware execution supplied extra evidence but did not remove substantial AI assistance, as ChatGPT generated the code and could interpret returned noisy data
description: Optional IBM Quantum hardware execution supplied extra evidence but did not remove substantial AI assistance, as ChatGPT generated the code and could interpret returned noisy data
id: hardware-execution-did-not-eliminate-llm-assistance
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
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Optional IBM Quantum hardware execution supplied extra evidence but did not remove substantial AI assistance, as ChatGPT generated the code and could interpret returned noisy data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In exploratory QPE, QFT, and Deutsch–Jozsa runs on IBM backends, the theoretically expected bitstring remained dominant despite noise, but the workflow stayed LLM-assisted from code generation through interpretation. [→ Alexei Kaltchenko and Gurnivaj Tiwana 2026](#alexei-kaltchenko-and-gurnivaj-tiwana-2026)

## Evidence

### Alexei Kaltchenko and Gurnivaj Tiwana 2026

Alexei Kaltchenko and Gurnivaj Tiwana. (2026). ChatGPT Solves All Tested Qiskit Homework Assignments. arXiv. https://arxiv.org/abs/2608.19707

`q2 · i?` · `design · r2`

Secondary exploratory evidence from earlier QPE, QFT, and Deutsch–Jozsa notebooks run on real devices, reported separately from the 150-session completion count. Table III shows expected counts such as 3709/4096 (90.55%) on ibm_kingston for QFT, with transpilation substantially increasing depth while results remained interpretable.

> "It did not eliminate the minimally engaged workflow: ChatGPT generated the code, the operator ran it, and the resulting data could be returned for interpretation."

## Discussion


## Related Claims
- [ChatGPT produced executed, grader-accepted submissions for all three fixed personalized Qiskit assignment instances in 150 of 150 sessions](chatgpt-completes-all-150-qiskit-homework-sessions.md) — related
- [Reviewed literature reports risks of overreliance, AI errors in complex tasks, and students' uncritical acceptance of AI-generated outputs](ai-math-risks-overreliance-errors-uncritical-trust.md) — a broader claim this one bears on
- [Personalized ChatGPT-supported feedback in an augmented-reality quantum physics laboratory improved learning outcomes and directed visual attention](chatgpt-ar-lab-feedback-improves-outcomes.md) — related
