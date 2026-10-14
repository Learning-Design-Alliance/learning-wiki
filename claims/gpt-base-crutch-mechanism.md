---
type: claim
title: Students use standard GPT-4 access as a crutch—copying answers rather than engaging with the material—which explains the harm to learning
description: Students use standard GPT-4 access as a crutch—copying answers rather than engaging with the material—which explains the harm to learning
id: gpt-base-crutch-mechanism
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: bastani-hamsa-2025
    resource: "https://doi.org/10.1073/pnas.2422633122"
    title: "Bastani Hamsa, Bastani Osbert, Sungu Alp, Ge Haosen, Kabakcı Özge, Mariman Rei. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2422633122"
    author: Bastani Hamsa, Bastani Osbert, Sungu Alp, Ge Haosen, Kabakcı Özge, Mariman Rei
    q: 3
    i: "?"
    kind: causal
    rigour: 3
  - id: bastani-hamsa-2025-2
    resource: "https://doi.org/10.1073/pnas.2422633122"
    title: "Bastani Hamsa, Bastani Osbert, Sungu Alp, Ge Haosen, Kabakcı Özge, Mariman Rei. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2422633122"
    author: Bastani Hamsa, Bastani Osbert, Sungu Alp, Ge Haosen, Kabakcı Özge, Mariman Rei
    q: 2
    i: "?"
    kind: causal
    rigour: 3
---

# Students use standard GPT-4 access as a crutch—copying answers rather than engaging with the material—which explains the harm to learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r3` · `q2`–`q3`

## Subclaims
`q3 i?` GPT Base's logical errors hurt practice performance but did not spill over to corresponding exam problems, and arithmetic and logical errors had similar practice effects—patterns the authors read as answer copying. [→ Bastani Hamsa 2025](#bastani-hamsa-2025)
`q3 i?` Message analysis shows GPT Base students most often simply ask for the answer, while GPT Tutor students increasingly ask for help and attempt answers independently. [→ Bastani Hamsa 2025 (2)](#bastani-hamsa-2025-2)

## Evidence

### Bastani Hamsa 2025

Bastani Hamsa, Bastani Osbert, Sungu Alp, Ge Haosen, Kabakcı Özge, Mariman Rei. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2422633122

`q3 · i?` · `causal · r3`

Problem-level regression with GPT Base error-rate interaction terms (13,484 practice / 11,392 exam observations). The "GPT Base × Logical Error Rate" interaction was −0.448 (P < 0.01) for practice but not significant for exams, supporting the crutch interpretation.

> "while GPT Base’s logical errors affect performance on the practice problems, we find no evidence that this effect spills over to the corresponding exam problems"

### Bastani Hamsa 2025 (2)

Bastani Hamsa, Bastani Osbert, Sungu Alp, Ge Haosen, Kabakcı Özge, Mariman Rei. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2422633122

`q2 · i?` · `causal · r3`

NLP clustering of student messages with the tutors, shown in Fig. 3 and SI Appendix Fig. C.4; GPT Base conversations were largely superficial (asking for answers) while GPT Tutor conversations were substantially more often nonsuperficial.

> "students in GPT Base most often simply ask for the answer; in contrast, students in GPT Tutor learn to interact more substantively with the tutoring tool over time by asking for help and independently attempting to solve the problem."

## Discussion


## Related Claims
- [Students do not perceive the learning harm from copying GPT solutions and overestimate their exam performance](students-unaware-of-ai-learning-harm.md) — related
- [Persistence and performance costs concentrate among participants who used the AI to obtain direct solutions, while hint-users resemble controls](persistence-costs-concentrated-among-direct-solution-users.md) — related
- [How a user engages with AI matters more than whether: structured, deliberate engagement can mitigate or reverse offloading effects](engagement-style-matters-more-than-whether.md) — related
- [Unguarded answer-giving AI harmed unaided exam performance while a guarded version of the same model erased the harm (Bastani et al., 2025, as reported)](gpt4-access-harms-learning-after-withdrawal.md) — related
- [Unrestricted GPT-4 access improved practice performance but harmed later exam performance, and a guardrailed hint-based version mitigated the harm, as reported by the whitepaper citing Bastani et al.](unrestricted-gpt4-practice-gains-exam-decline-guardrail-mitigates.md) — related
- [Greater answer offloading during learning is associated with lower subsequent unaided performance (exploratory)](answer-offloading-associated-lower-unaided-performance-exploratory.md) — related
