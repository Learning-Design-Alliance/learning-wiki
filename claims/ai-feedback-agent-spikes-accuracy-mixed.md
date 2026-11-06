---
type: claim
title: The AI feedback agent reliably detected empathy, reassurance, clarity, and tone balance but inconsistently assessed SPIKES adherence, improving when SPIKES was spelled out as a 6-step bulleted list
description: The AI feedback agent reliably detected empathy, reassurance, clarity, and tone balance but inconsistently assessed SPIKES adherence, improving when SPIKES was spelled out as a 6-step bulleted list
id: ai-feedback-agent-spikes-accuracy-mixed
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: mixed
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mavragani-a-2025
    resource: "https://doi.org/10.2196/65670"
    title: "Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS. (2025). Development of a GPT-4–Powered Virtual Simulated Patient and Communication Training Platform for Medical Students to Practice Discussing Abnormal Mammogram Results With Patients: Multiphase Study. JMIR Formative Research. https://doi.org/10.2196/65670"
    author: Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: mavragani-a-2025-2
    resource: "https://doi.org/10.2196/65670"
    title: "Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS. (2025). Development of a GPT-4–Powered Virtual Simulated Patient and Communication Training Platform for Medical Students to Practice Discussing Abnormal Mammogram Results With Patients: Multiphase Study. JMIR Formative Research. https://doi.org/10.2196/65670"
    author: Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The AI feedback agent reliably detected empathy, reassurance, clarity, and tone balance but inconsistently assessed SPIKES adherence, improving when SPIKES was spelled out as a 6-step bulleted list

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The AI feedback agent consistently and accurately detected empathy, reassurance, clarity, and balance of seriousness and uncertainty in learner responses. [→ Mavragani A 2025](#mavragani-a-2025)
`q2 i?` The agent did not consistently assess SPIKES adherence accurately until the prompt broke SPIKES into 6 steps with bulleted look-for guidelines. [→ Mavragani A 2025 (2)](#mavragani-a-2025-2)

## Evidence

### Mavragani A 2025

Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS. (2025). Development of a GPT-4–Powered Virtual Simulated Patient and Communication Training Platform for Medical Students to Practice Discussing Abnormal Mammogram Results With Patients: Multiphase Study. JMIR Formative Research. https://doi.org/10.2196/65670

`q2 · i?` · `design · r2`

Study-team evaluation of the exploratory AI feedback feature during the Evaluation phase, reviewing generated feedback against saved conversations. The team judged that the agent "consistently provided feedback that accurately detected" the four named qualities; no statistics are printed.

> "The AI feedback agent consistently provided feedback that accurately detected the presence of empathy, reassurance, clarity, and a balance of seriousness and uncertainty in user responses."

### Mavragani A 2025 (2)

Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS. (2025). Development of a GPT-4–Powered Virtual Simulated Patient and Communication Training Platform for Medical Students to Practice Discussing Abnormal Mammogram Results With Patients: Multiphase Study. JMIR Formative Research. https://doi.org/10.2196/65670

`q2 · i?` · `design · r2`

Iterative prompt-refinement testing after the agent initially "did not consistently assess the user's adherence to SPIKES accurately," crediting summaries the tester had excluded. Repeated testing of successive prompt iterations showed the bulleted 6-step format produced more consistently accurate assessments; no effect sizes are printed.

> "Testing showed that breaking down SPIKES into 6 steps and including guidelines about actions to look for in a bulleted list format resulted in the AI feedback agent providing more consistently accurate assessments of whether a user was following SPIKES."

## Discussion


## Related Claims
- [In preliminary testing, the VSP's emotional responses tracked learner adherence to the SPIKES protocol, becoming calmer when learners followed it and irate enough to hang up when they did not](vsp-responses-track-spikes-adherence.md) — related
- [Accurate LLM solution diagnosis does not reliably produce pedagogically actionable feedback, with lowest rubric scores on error identification and actionability](accurate-diagnosis-not-actionable-feedback.md) — related
- [Judge-condition verification did not consistently improve LLM feedback quality and often propagated Peer agents' errors](judge-verification-propagates-peer-errors.md) — related
- [Students perceive AI scoring as accurate for grammar, mechanics, and organization but skeptical of its ability to evaluate diverse styles, complex writing, tone, and emotion](ai-scoring-perceptions-lower-vs-higher-order.md) — related
- [Making trustworthiness metrics and visualizations explicit increased inter-rater reliability among learning engineers evaluating LLM responses](trustworthiness-metrics-visualizations-increase-expert-agreement.md) — related
- [The VSP was consistently more cooperative with unempathetic-but-clear learners than with empathetic-and-clear learners, revealing a prompt-weighting bias](vsp-cooperation-bias-clarity-over-empathy.md) — related
