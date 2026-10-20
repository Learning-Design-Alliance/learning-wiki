---
type: claim
title: A guardrailed GPT-4 tutor with teacher-designed hints improves assisted practice performance more than a standard GPT-4 interface
description: A guardrailed GPT-4 tutor with teacher-designed hints improves assisted practice performance more than a standard GPT-4 interface
id: gpt-tutor-improves-practice-more-than-gpt-base
status: review
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
---

# A guardrailed GPT-4 tutor with teacher-designed hints improves assisted practice performance more than a standard GPT-4 interface

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r3` · `q3`

## Subclaims
`q3 i?` GPT Tutor raised assisted practice scores by 0.361 (out of 1) relative to control, a 127% improvement, exceeding GPT Base's 0.137. [→ Bastani Hamsa 2025](#bastani-hamsa-2025)

## Evidence

### Bastani Hamsa 2025

Bastani Hamsa, Bastani Osbert, Sungu Alp, Ge Haosen, Kabakcı Özge, Mariman Rei. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2422633122

`q3 · i?` · `causal · r3`

Same intention-to-treat regression; the GPT Tutor coefficient was 0.361 (P < 0.01). The article says "the gap between GPT Tutor and GPT Base illustrates the added benefits of problem-specific teacher inputs in the prompt." No standardized effect size is printed.

> "GPT Base and GPT Tutor substantially increased student scores in the GPT-assisted practice sessions by 0.137 and 0.361 (out of 1), respectively, relative to the control arm that only had access to textbooks (mean performance of 0.28)."

## Discussion

## Related Claims

- [Learners receiving ChatGPT-generated hints showed statistically significant learning gains compared to a no-hint control in an online mathematics tutoring experiment](chatgpt-hints-significant-gains-versus-control.md) — the general claim this finding bears on, with the studies behind it

- [In one experiment with 256 undergraduates, computer-based lesson versions that included practice produced significantly higher posttest scores than versions without practice](practice-presence-raises-cbi-posttest-achievement.md) — the general claim this finding bears on, with the studies behind it
- [Access to a standard GPT-4 chat tutor during practice substantially improves practice performance in high school mathematics](gpt-base-improves-assisted-practice-performance.md) — related
- [Review reports a field experiment in which GPT access improved supported practice but was followed by poorer unaided test performance, mitigated by a guarded tutor](gpt4-access-harms-learning-after-withdrawal.md) — related
- [Among GPT-assisted students, proactive and critical engagement patterns are associated with higher exam scores while limited engagement shows little benefit relative to control](proactive-critical-ai-engagement-higher-exam-scores.md) — related
- [Unfettered GPT-4 access during practice harms subsequent unassisted exam performance in high school mathematics](gpt-base-harms-unassisted-exam-performance.md) — related
- [AI-generated homework hints were positively associated with exam performance only when exam questions closely matched the homework content](ai-hints-aligned-exam-performance-only.md) — related
- [Guardrails in the GPT Tutor largely eliminate the negative exam effect, though no positive exam effect is observed](gpt-tutor-exam-effect-null.md) — related
- [Students use standard GPT-4 access as a crutch—copying answers rather than engaging with the material—which explains the harm to learning](gpt-base-crutch-mechanism.md) — related
- [Students do not perceive the learning harm from copying GPT solutions and overestimate their exam performance](students-unaware-of-ai-learning-harm.md) — related
- [During development testing, Taklif.AI guardrails rejected roughly 12% of interests, 8% of input documents, and 3% of generated assignments](guardrails-rejection-rates-development-testing.md) — related
