---
type: research-method
id: explainable-by-design-framework-coupling-dual-lens-hierarchical-attention-trust-gated-infe
title: Explainable-by-design framework coupling dual-lens hierarchical attention, trust-gated inference, and on-the-spot explanation generation
description: The framework is an LLM-based teacher assessment architecture in which trustworthiness and explainability are built into inference rather than appended afterward.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# Explainable-by-design framework coupling dual-lens hierarchical attention, trust-gated inference, and on-the-spot explanation generation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The framework is an LLM-based teacher assessment architecture in which trustworthiness and explainability are built into inference rather than appended afterward. It couples "a global lens aligned to curriculum standards and a local lens aligned to subject-specific rubrics" with a Trust-Gated Inference module combining Monte-Carlo-dropout calibration and adversarial debiasing, and an On-the-Spot Explanation generator that shares the same fused representation and predicted score used for decision making, so explanations are decision-consistent and curriculum-anchored. Trust gating exposes uncertainty and bias alerts and can output Reject with reason.

## Accounts
<!-- How each source describes or uses the method -->
- **Explainable-by-design framework coupling dual-lens hierarchical attention, trust-gated inference, and on-the-spot explanation generation**: The framework is an LLM-based teacher assessment architecture in which trustworthiness and explainability are built into inference rather than appended afterward. It couples "a global lens aligned to curriculum standards and a local lens aligned to subject-specific rubrics" with a Trust-Gated Inference module combining Monte-Carlo-dropout calibration and adversarial debiasing, and an On-the-Spot Explanation generator that shares the same fused representation and predicted score used for decision making, so explanations are decision-consistent and curriculum-anchored. Trust gating exposes uncertainty and bias alerts and can output Reject with reason. (Li et al. (2025))

### Claims
- [The proposed framework outperforms fine-tuned BERT, Instructor-LM, GPT-4, and RAPT on TeacherEval-2023 across consistency, credibility, calibration, and fairness metrics](../claims/llm-teacher-assessment-outperforms-baselines-teachereval.md) [+M]
- [Ablations show the trustworthiness module contributes most to performance, and the explanation generator cuts human review time by 41%](../claims/ablation-trust-module-largest-contribution.md) [+M]

## Related Research Methods
-

## Key Sources
- Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882
