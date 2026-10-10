---
type: claim
title: "Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive"
description: "Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive"
id: llm-logical-inconsistency-scoring-feedback
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: cohn-2026
    resource: "https://arxiv.org/abs/2504.02323"
    title: "Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G. (2026). CoTAL: Human-in-the-Loop Prompt Engineering for Generalizable Formative Assessment Scoring and Feedback. arXiv preprint. https://arxiv.org/abs/2504.02323"
    author: "Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G."
    q: 1
    i: "?"
    kind: qualitative
    rigour: 1
---

# Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r1` · `q1`

## Subclaims
`q1 i?` In the Rules Task evaluation, the LLM sometimes cited the relevant student text and applicable rubric directive yet still failed to award the appropriate point, a case the authors term logical inconsistency. [→ Cohn 2026](#cohn-2026)

## Evidence

### Cohn 2026

Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G. (2026). CoTAL: Human-in-the-Loop Prompt Engineering for Generalizable Formative Assessment Scoring and Feedback. arXiv preprint. https://arxiv.org/abs/2504.02323

`q1 · i?` · `qualitative · r1`

Qualitative constant comparative analysis of GPT-4's reasoning chains during the Rules Task evaluation, examining scoring justifications. The authors present an example where the LLM "acknowledged the applicable rubric directive, yet still failed to award the appropriate point," labeling it "a clear case oflogical inconsistency."

> "The LLM correctly cited the relevant portion of the student’s response, acknowledged the applicable rubric directive, yet still failed to award the appropriate point. This is a clear case oflogical inconsistency"

## Discussion


## Related Claims
- [CoTAL improves GPT-4 scoring agreement with human scorers on the Rules Task, raising average subscore QWK from 0.826 to 0.916 (a 10.9% gain) over a non-prompt-engineered baseline](cotal-rules-task-qwk-gain.md) — related
- [Rubric-enhanced prompting (Variant 2) raises LLM assigned scores relative to the no-rubric baseline, with model-specific gaps at particular taxonomy levels](rubric-prompting-raises-llm-assigned-scores.md) — related
- [All four evaluated LLMs produce strongly bimodal item-level score distributions on bash exams, and rubric-enhanced prompts amplify the near-perfect-score peak](llm-bash-score-distributions-bimodal-v2-amplifies.md) — related
- [Using AI to evaluate AI outputs was often challenging because AI act as yes people and humans struggled to agree on evaluation rubrics](ai-evaluating-ai-outputs-challenging.md) — related
