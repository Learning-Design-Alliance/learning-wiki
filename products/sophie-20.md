---
type: product
id: sophie-20
title: SOPHIE 2.0
description: SOPHIE 2.0 is a browser-based platform developed by Masum Hasan and colleagues that uses audiovisual virtual patients, LLM-generated dialogue, and automated feedback to support clinical communication practice for healthcare learners.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# SOPHIE 2.0

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 2 studies (1 causal, 1 design), `q2` · 1 of 2 report an effect size · 5 claims rest on one study

## Description
SOPHIE 2.0 is a browser-based platform developed by Masum Hasan and colleagues that uses audiovisual virtual patients, LLM-generated dialogue, and automated feedback to support clinical communication practice for healthcare learners.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **SOPHIE: Standardized Online Patient for Healthcare Interaction Education**: SOPHIE (Standardized Online Patient for Healthcare Interaction Education) is a generative AI-powered virtual patient for serious illness communication training. It features a high-fidelity virtual patient (a 60-year-old woman with incurable stage 4 lung cancer) built with Unreal Engine MetaHuman, speech-to-text and text-to-speech via Microsoft Azure Speech SDK, and a hybrid dialogue manager combining a schema-based system with an LLM (GPT-3.5 Turbo). The schema "grounds the dialogue and provides guardrails" while the LLM generates natural responses within structured templates. After each module, users receive personalized feedback on effective behaviors, missed opportunities, and suggested alternatives. (Haut KG et al. (2026))
- **MVP framework and 3E communication skills for serious illness conversations**: The MVP (medical situation, values, and plan) communication framework and its 3 core skills—Empathize, Be Explicit, and Empower (3Es)—ground both the SOPHIE system and the study's outcome measures. The Empathize skill focuses on responding to emotional distress, Be Explicit on clearly communicating prognosis and uncertainty, and Empower on eliciting values and supporting a patient-centered care plan. The framework was converted into a structured Likert-scale questionnaire to quantify communication behaviors on a numeric scale, normalized to between 0 and 1. (Haut KG et al. (2026))
- **MVP framework and 3E skill classification (Empathize, be Explicit, Empower) for serious illness conversations**: The MVP (Medical situation, Values, Planning) framework is described as "a structured yet flexible approach for serious illness conversations (SICs)" supported by three essential communication skills, the 3Es. Empower means ensuring patient autonomy and shared decision-making; Be Explicit means communicating clearly, directly, and concisely; Empathize means validating and exploring emotions as the patient desires. SOPHIE adopts this framework from the ACT course at URMC as its training model and quantifies feedback on the three skills. (Kurtis Haut et al. (2025))
- **SOPHIE: AI-powered virtual standardized patient with hybrid schema-guided LLM dialogue manager, avatar, and automated 3E feedback**: SOPHIE (Standardized Online Patient for Healthcare Interaction Education) simulates a 60-year-old woman with terminal lung cancer via a lifelike Unreal Engine 5.1 Metahuman avatar engaging in real-time spoken dialogue with emotion-tagged facial expressions and vocal tone. The authors "developed a hybrid schema-guided LLM-based dialogue manager that combines the controllability of rule-based systems with the versatility of LLMs," using a rule-based plus BERT skill classifier to tag user statements with 3E skills. After each encounter it generates personalized, actionable feedback with quantified metrics for Empowerment, Empathy, and Explicitness. (Kurtis Haut et al. (2025))
- **Released SOPHIE evaluation dataset: 506 professional ratings and analysis code on GitHub**: Alongside the paper the authors release the 506 ratings provided by professional raters, together with their analysis code at https://github.com/ROC-HCI/SOPHIE-1.0. The ratings cover 102 recorded standardized patient conversations, each rated by one standardized patient and four blinded third-party reviewers. Videos and timestamped transcripts are available to researchers on a case-by-case basis contingent on IRB approval. (Kurtis Haut et al. (2025))

### Claims
- [An automated LLM assessor rates 3E clinical communication skills with agreement comparable to individual human raters](../claims/llm-assessor-agrees-with-human-raters-3e.md) [+M]
- [Participants rated SOPHIE 2.0 as engaging, easy to use, and clinically relevant in a self-service format](../claims/sophie2-high-perceived-usability-and-value.md) [+M]
- [HAL's text-based human-likeness advantage did not transfer to embodied audiovisual interaction, and measured 3E performance was virtually identical between models](../claims/hal-human-likeness-did-not-transfer-embodied.md) [~W]
- [In a randomized controlled trial, SOPHIE training produced significantly greater pre-post gains in serious illness communication skills than a written reading module, with large effect sizes for the SOPHIE arm](../claims/sophie-rct-greater-sic-gains-than-reading-control.md) [+M]
- [Qualitative interviews identified a judgment-free practice environment and specific actionable feedback as key mechanisms of SOPHIE's training value](../claims/sophie-qualitative-judgment-free-actionable-feedback.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Masum Hasan, Ron Epstein, Thomas Carroll, Ehsan Hoque. (2026). Scalable AI-based clinical communication training and automated assessment. https://arxiv.org/abs/2609.22517
- Haut KG, Hasan M, Carroll T, Epstein RM, Sen T, Hoque E. (2026). Effects of a Generative AI Virtual Patient on Serious Illness Communication Skills: Randomized Controlled Trial. JMIR Medical Education. https://doi.org/10.2196/93034
- Kurtis Haut, Masam Hasan, Thomas Carroll, Ronald Epstein, Taylan Sen, Ehsan Hoque. (2025). AI Standardized Patient Improves Human Conversations in Advanced Cancer Care. https://arxiv.org/abs/2505.02694
