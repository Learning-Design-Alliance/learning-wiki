---
type: research-method
id: multi-dimensional-fidelity-framework-for-llm-student-simulation
title: Multi-dimensional fidelity framework for LLM student simulation
description: "The article names competency bias as \"the inherent tendency of preference-tuned models to produce correct solutions even when prompted to simulate novice students\", and frames simulating learners as a multi-dimensional fidelity problem with behavioral, epistemic, and perceptual components."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Multi-dimensional fidelity framework for LLM student simulation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 3 claims rest on one study

## Description
The article names competency bias as "the inherent tendency of preference-tuned models to produce correct solutions even when prompted to simulate novice students", and frames simulating learners as a multi-dimensional fidelity problem with behavioral, epistemic, and perceptual components. Behavioral infidelity is the linear construction trap avoiding iterative trial-and-error; epistemic infidelity is the curse of incompetence, where LLMs act as masked experts who diagnose errors before execution; perceptual infidelity is RLHF-flattened output diversity. BEAGLE is designed explicitly against these three objectives.

## Accounts
<!-- How each source describes or uses the method -->
- **Competency bias and the multi-dimensional fidelity problem for LLM student simulation**: The article names competency bias as "the inherent tendency of preference-tuned models to produce correct solutions even when prompted to simulate novice students", and frames simulating learners as a multi-dimensional fidelity problem with behavioral, epistemic, and perceptual components. Behavioral infidelity is the linear construction trap avoiding iterative trial-and-error; epistemic infidelity is the curse of incompetence, where LLMs act as masked experts who diagnose errors before execution; perceptual infidelity is RLHF-flattened output diversity. BEAGLE is designed explicitly against these three objectives. (Hanchen David Wang et al. (2026))

### Claims
- [BEAGLE achieves higher behavioral fidelity to real student cognitive-behavior distributions than LLM prompting and agent baselines on a Particle Simulator task (DKL = 0.31 vs. baselines ≥ 0.53)](../claims/beagle-behavioral-fidelity-beats-baselines.md) [+M]
- [BEAGLE's error recurrence rate (86.2%) falls within the realistic novice envelope, far above vanilla LLMs (7.8%) and below rule-based SimStudent's mechanical saturation (92.0%)](../claims/beagle-error-recurrence-novice-envelope.md) [+M]
- [In a human Turing test, participants could not reliably distinguish BEAGLE traces from real student data (52.8% accuracy; d′ = 0.15 within the ±0.3 equivalence bound, pTOST = 0.038)](../claims/beagle-traces-turing-test-indistinguishable.md) [+M]

## Related Research Methods
-

## Key Sources
- Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280
