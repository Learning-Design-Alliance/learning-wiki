---
type: research-method
id: cognitive-diagnostic-profiling-cdp
title: Cognitive Diagnostic Profiling (CDP)
description: "CDP is a zero-shot framework that draws on cognitive diagnostic models \"to represent each simulated examinee as a binary attribute-mastery profile and prompts an LLM to generate item responses consistent with that profile.\" It proceeds in six steps: construct decomposition into binary attributes, ma"
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Cognitive Diagnostic Profiling (CDP)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
CDP is a zero-shot framework that draws on cognitive diagnostic models "to represent each simulated examinee as a binary attribute-mastery profile and prompts an LLM to generate item responses consistent with that profile." It proceeds in six steps: construct decomposition into binary attributes, mastery-pattern formation over 2^K patterns, natural-language rendering of mastered and unmastered skills, simulated pool assembly under an uninformative (uniform) or informative (population-prevalence) sampling distribution, response generation, and standard psychometric analysis. It applies the generative logic of assessment design traditions in the opposite direction: it generates examinees rather than items.

## Accounts
<!-- How each source describes or uses the method -->
- **Cognitive Diagnostic Profiling (CDP): a six-step zero-shot framework for simulating examinees with binary attribute-mastery profiles**: CDP is a zero-shot framework that draws on cognitive diagnostic models "to represent each simulated examinee as a binary attribute-mastery profile and prompts an LLM to generate item responses consistent with that profile." It proceeds in six steps: construct decomposition into binary attributes, mastery-pattern formation over 2^K patterns, natural-language rendering of mastered and unmastered skills, simulated pool assembly under an uninformative (uniform) or informative (population-prevalence) sampling distribution, response generation, and standard psychometric analysis. It applies the generative logic of assessment design traditions in the opposite direction: it generates examinees rather than items. (Wenjie Zhou et al. (2026))

### Claims
- [Cognitive Diagnostic Profiling raises distribution-level overlap between simulated and human examinee ability distributions, with the informative condition highest for seven of eight configurations](../claims/cdp-improves-distribution-level-alignment.md) [+M]
- [CDP improves item-difficulty recovery in both rank order and absolute alignment, with the largest gains for reasoning-enabled Gemini configurations](../claims/cdp-improves-item-difficulty-recovery.md) [+M]

## Related Research Methods
-

## Key Sources
- Wenjie Zhou, Yunting Liu, Renjiao Tang, & Mark Wilson. (2026). Aligning LLM-Simulated and Human Examinees for Psychometric Calibration: A Cognitive Diagnostic Profiling Approach. https://osf.io/p6fam/
