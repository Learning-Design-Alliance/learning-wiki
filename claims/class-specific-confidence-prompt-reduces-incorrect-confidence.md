---
type: claim
title: A class-specific confidence prompt reduces LLM confidence in incorrect bias judgments but also lowers confidence in correct ones, without changing accuracy
description: A class-specific confidence prompt reduces LLM confidence in incorrect bias judgments but also lowers confidence in correct ones, without changing accuracy
id: class-specific-confidence-prompt-reduces-incorrect-confidence
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: arronte-alvarez-2026
    resource: "https://doi.org/10.1007/978-3-032-29773-0_22"
    title: "Arronte Alvarez, A., and Xie Fincham, N. (2026). Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents. Accepted for AIED 2026. [doi:10.1007/978-3-032-29773-0_22](https://doi.org/10.1007/978-3-032-29773-0_22)"
    author: Arronte Alvarez, A., and Xie Fincham, N.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A class-specific confidence prompt reduces LLM confidence in incorrect bias judgments but also lowers confidence in correct ones, without changing accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Prompt 2 (class-specific confidence) achieves the greatest reduction in confidence for incorrect responses, but also produces decreases in correct assessments, with model accuracy unchanged. [→ Arronte Alvarez 2026](#arronte-alvarez-2026)

## Evidence

### Arronte Alvarez 2026

Arronte Alvarez, A., and Xie Fincham, N. (2026). Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents. Accepted for AIED 2026. [doi:10.1007/978-3-032-29773-0_22](https://doi.org/10.1007/978-3-032-29773-0_22)

`q2 · i?` · `causal · r2`

Computational Experiment #1 comparing two confidence elicitation prompts across three LLMs; significant differences in confidence means across prompts (p <0.05), Prompt 1 eliciting higher confidence (92.4% vs. 86.4% on average), mean confidence remaining high overall (84.4%).

> "In particular, Prompt 2 (the class-specific confidence prompt) achieves the greatest reduction in confidence for incorrect responses, which is a desirable property, however, it also produces decreases in correct assessments."

## Discussion


## Related Claims
- [A brief metacognitive reflection prompt reduces acceptance of incorrect AI advice compared with open ChatGPT support alone](reflection-reduces-incorrect-ai-advice-acceptance.md) — related
- [Warning labels alone did not improve performance or reduce reliance on GenAI advice, and students sometimes adopted incorrect AI answers](genai-warning-labels-insufficient-reliance.md) — related
- [Automation bias toward fluent LLM output surrenders learners' epistemic agency](automation-bias-surrenders-epistemic-agency.md) — related
- [State-of-the-art LLMs are overconfident in incorrect judgments of stereotypical bias in tutoring conversations, with most errors made at high or very high confidence](llm-overconfidence-incorrect-bias-judgments-tutoring.md) — related
