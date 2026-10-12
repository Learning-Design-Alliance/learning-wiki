---
type: claim
title: "Prompt specificity changes AI tutor pedagogy: a no-direct-answer guardrail alone produces uniform questioning, while a detailed guided protocol produces varied, impasse-sensitive responses"
description: "Prompt specificity changes AI tutor pedagogy: a no-direct-answer guardrail alone produces uniform questioning, while a detailed guided protocol produces varied, impasse-sensitive responses"
id: prompt-specificity-shapes-tutor-pedagogy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: ahtisham-2026
    resource: "https://arxiv.org/abs/2609.38346"
    title: "Ahtisham, B., Vanacore, K., Napoli, A., Arens, J., Ionova, K., Cohn, C., Salehi, S., & Kizilcec, R. (2026). Examining Variation in How Guided AI Tutors Resolve Student Impasses. arXiv. https://arxiv.org/abs/2609.38346"
    author: "Ahtisham, B., Vanacore, K., Napoli, A., Arens, J., Ionova, K., Cohn, C., Salehi, S., & Kizilcec, R."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Prompt specificity changes AI tutor pedagogy: a no-direct-answer guardrail alone produces uniform questioning, while a detailed guided protocol produces varied, impasse-sensitive responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` For the same 150 impasses, the baseline tutor gave direct answers in 50.7% of responses, the no-direct-answer tutor asked a follow-up question in 100% of responses, and the guided tutor used the broadest repertoire (response entropy 5.13 bits vs 3.11 and 1.25). [→ Ahtisham 2026](#ahtisham-2026)

## Evidence

### Ahtisham 2026

Ahtisham, B., Vanacore, K., Napoli, A., Arens, J., Ionova, K., Cohn, C., Salehi, S., & Kizilcec, R. (2026). Examining Variation in How Guided AI Tutors Resolve Student Impasses. arXiv. https://arxiv.org/abs/2609.38346

`q2 · i?` · `causal · r2`

Simulation study replaying a stratified sample of 150 impasse turns (n=50 per type) through three tutor conditions generated with GPT 5.6, coded with the same move set. All nine moves differed across conditions (Bonferroni-corrected p<.001; Cramér's V=.20–.56); response diversity entropies were 5.13 (Guided), 3.11 (Baseline), and 1.25 bits (No-Direct-Answer).

> "The Baseline AI Tutor provided direct answers in 50.7% of responses (vs. 19.3% for the Guided AI Tutor and 0% for the No-Direct-Answer Baseline AI Tutor)."

## Discussion


## Related Claims
- [Student impasses in LLM chemistry tutoring concentrate in the relevant-concepts planning phase, and impasse type depends strongly on problem-solving practice](impasses-concentrate-relevant-concepts-practice.md) — related
- [The association between tutor questioning and impasse recovery decays as impasses persist, while addressing the student's error becomes more beneficial](questioning-benefit-decays-with-impasse-depth.md) — related
- [Some classroom discussion approaches improve text comprehension, but gains are not uniform across approaches and more student talk alone does not produce them](structured-discussion-methods-improve-comprehension.md) — related
- [Next-turn recovery from impasses declines steadily as impasse depth increases, with help-seeking impasses declining most sharply](recovery-declines-with-impasse-depth.md) — related
- [Explicit no-direct-answers guardrails in teacher prompts reduced the AI's final-answer provision rate by 8.5 percentage points (16.2% to 7.7%)](no-direct-answers-guardrail-reduces-ai-answers.md) — related
