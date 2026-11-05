---
type: design
id: ai-vsp-segue-training-system
title: AI-based communication training system with speech recognition, SEGUE-aligned semantic analysis, and automated feedback reports
description: A web-based software system built on the DeepSeek-chat large language model (R1 version, accessed via cloud API, not fine-tuned) that simulates patients for SEGUE-based communication training.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-05
sources:
  - id: sun-ning-2026
    resource: "https://doi.org/10.3389/fpubh.2026.1768518"
    title: "Sun Ning, Zhou Xintong, Yang Zhongqian, Zhou Yu, Ma Ruihang, Wang Zhong. (2026). Application of AI-based virtual standardized patients in physician-patient communication training: a study based on the SEGUE framework. Frontiers in Public Health. https://doi.org/10.3389/fpubh.2026.1768518"
    author: Sun Ning, Zhou Xintong, Yang Zhongqian, Zhou Yu, Ma Ruihang, Wang Zhong
---

# AI-based communication training system with speech recognition, SEGUE-aligned semantic analysis, and automated feedback reports

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
A web-based software system built on the DeepSeek-chat large language model (R1 version, accessed via cloud API, not fine-tuned) that simulates patients for SEGUE-based communication training. It "integrated an automatic speech recognition engine (e.g., iFlytek) with a semantic analysis module aligned with the five SEGUE dimensions", transcribes spoken dialogue, scores SEGUE behaviors, and generates a structured post-encounter feedback report with dimension scores and example response formulations. Interaction is text/voice only, without visual avatars, and the AI-VSP acts solely as a patient without instructional prompts.

## Design Implications

### Context
#### Requirements
- Stable internet connectivity for cloud-based model access
- Structured prompt engineering with rule-based SEGUE constraints and manual iterative adjustment validated by expert voting
#### Constraints
- No visual avatars, facial animation, or synthesized imagery; lacks nonverbal and affective variability of human SPs
- Case materials restricted to a limited set of cases (10 per SP)

### Target Learners
- Senior undergraduate clinical medicine students

### Learning Goals
- Physician-patient communication behaviors assessed by the SEGUE framework

### Claims
- [Ai Vsp More Training Cycles](../claims/ai-vsp-more-training-cycles.md) [+M]
- [Ai Vsp Higher Total Content Segue Scores](../claims/ai-vsp-higher-total-content-segue-scores.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Sun Ning, Zhou Xintong, Yang Zhongqian, Zhou Yu, Ma Ruihang, Wang Zhong. (2026). Application of AI-based virtual standardized patients in physician-patient communication training: a study based on the SEGUE framework. Frontiers in Public Health. https://doi.org/10.3389/fpubh.2026.1768518
