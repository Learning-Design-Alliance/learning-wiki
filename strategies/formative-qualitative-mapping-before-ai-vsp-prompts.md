---
type: strategy
id: formative-qualitative-mapping-before-ai-vsp-prompts
title: Collect qualitative formative data and map likely conversation paths before developing AI-powered VSP prompts
description: The authors recommend preserving the conceptual discipline of branching-path design even when building generative-AI simulations.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
sources:
  - id: mavragani-a-2025
    resource: "https://doi.org/10.2196/65670"
    title: "Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS. (2025). Development of a GPT-4–Powered Virtual Simulated Patient and Communication Training Platform for Medical Students to Practice Discussing Abnormal Mammogram Results With Patients: Multiphase Study. JMIR Formative Research. https://doi.org/10.2196/65670"
    author: Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS
---

# Collect qualitative formative data and map likely conversation paths before developing AI-powered VSP prompts

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The authors recommend preserving the conceptual discipline of branching-path design even when building generative-AI simulations. They "recommend that developers start building virtual scenarios by collecting qualitative data from relevant clinicians and patients in the spirit of a BPS and map out likely conversation paths before developing AI-powered VSP prompts." Interview-informed mapping of plausible PCP-patient conversations informed the VSP prompt and provided a benchmark for judging whether GPT-4 responses matched expected patient behavior.

## Design Implications

### Context
#### Requirements
- Access to relevant clinicians and patients as knowledge users for in-depth interviews
- Team consensus on interview themes before translating them into prompt content
#### Constraints
- The mapped conversation paths serve as evaluation benchmarks and design input, not as scripted dialogue, since the AI-driven design generates responses in real time

### Target Learners
- medical students

### Target Learning Goals
- authentic clinical communication scenario design

## Claims

- [In-depth interviews with 5 medical students, 5 PCPs, and 5 breast cancer survivors identified gaps in communication skills training and shaped the scenario's timing, mode, and SPIKES-based protocol](../claims/formative-interviews-informed-vsp-design.md) [+W]
- [The AI feedback agent reliably detected empathy, reassurance, clarity, and tone balance but inconsistently assessed SPIKES adherence, improving when SPIKES was spelled out as a 6-step bulleted list](../claims/ai-feedback-agent-spikes-accuracy-mixed.md) [+W]
- [The VSP was consistently more cooperative with unempathetic-but-clear learners than with empathetic-and-clear learners, revealing a prompt-weighting bias](../claims/vsp-cooperation-bias-clarity-over-empathy.md) [+W]
- [In preliminary testing, the VSP's emotional responses tracked learner adherence to the SPIKES protocol, becoming calmer when learners followed it and irate enough to hang up when they did not](../claims/vsp-responses-track-spikes-adherence.md) [+W]

## Related Strategies

- [Use the DOT Framework's Empathize and Test/Feedback stages as practical checklists, and build professional learning communities around shared prompting and critique practices](dot-empathize-test-checklist-plc-strategy.md)
- [Using Empathy Interviews for Family Engagement](using_empathy_interviews_for_family_engagement.md)
- [Interactive Storytelling](interactive_storytelling.md)

## Examples
-

## Key Sources
- Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS. (2025). Development of a GPT-4–Powered Virtual Simulated Patient and Communication Training Platform for Medical Students to Practice Discussing Abnormal Mammogram Results With Patients: Multiphase Study. JMIR Formative Research. https://doi.org/10.2196/65670
