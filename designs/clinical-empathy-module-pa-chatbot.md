---
type: design
id: clinical-empathy-module-pa-chatbot
title: Clinical Empathy Module for PA coaching chatbots
description: The Clinical Empathy Module is a pipeline attached to the Empathetic chatbot variant that identifies Empathy Opportunities in user messages and generates clinically informed empathetic responses.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: li-siyan-2026
    resource: "https://arxiv.org/abs/2606.26641"
    title: "Li Siyan, Kai-Hui Liang, Shopnil Shahriar, Yilin Ye, Shiyoh Goetsu, Wei-Wei Du, Masahiro Yoshida, Tsunayuki Ohwa, Xuhai Xu, and Zhou Yu. (2026). Invisible Impact of Empathy on Behavioral Change: Isolating the Effect of Empathy in Long-term Physical Activity Coaching Chatbot Interactions. https://arxiv.org/abs/2606.26641"
    author: Li Siyan, Kai-Hui Liang, Shopnil Shahriar, Yilin Ye, Shiyoh Goetsu, Wei-Wei Du, Masahiro Yoshida, Tsunayuki Ohwa, Xuhai Xu, and Zhou Yu
---

# Clinical Empathy Module for PA coaching chatbots

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The Clinical Empathy Module is a pipeline attached to the Empathetic chatbot variant that identifies Empathy Opportunities in user messages and generates clinically informed empathetic responses. It consists of three submodules: an "Empathy Opportunity Classifier", a "Strategy Sampler", and an "Instruction Generator". The classifier is a GPT-4o-mini-based model with "a top-three classification accuracy of 85.3%"; the sampler draws from EO-specific strategy distributions built from statistics in Rey Velasco et al.; the generator produces system instructions for GPT-4o describing the chosen strategies. Only the Empathetic chatbot variant has access to this module.

## Design Implications

### Context
#### Requirements
- A GPT-4o base model and WhatsApp/Twilio delivery infrastructure
- EO-to-strategy mappings derived from the healthcare-professional response data of Rey Velasco et al.
- Check-in questions designed to elicit negative self-disclosure so that naturalistic Empathy Opportunities arise
#### Constraints
- The module is not activated in the initial consultation session; it operates only in maintenance sessions
- The chatbot does not retain every single past conversation, since summaries are condensed and only the top 3-5 relevant bullets are retrieved

### Target Learners
- Inactive but motivated adults seeking to increase physical activity

### Learning Goals
- Sustained physical activity behavior change
- Increased intention to follow coaching advice and self-efficacy

### Claims
- [Llm Epitome Scores Differentiate Nonempathetic](../claims/llm-epitome-scores-differentiate-nonempathetic.md) [+M]
- [Empathetic Chatbot Faster Intention Selfefficacy Growth](../claims/empathetic-chatbot-faster-intention-selfefficacy-growth.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Li Siyan, Kai-Hui Liang, Shopnil Shahriar, Yilin Ye, Shiyoh Goetsu, Wei-Wei Du, Masahiro Yoshida, Tsunayuki Ohwa, Xuhai Xu, and Zhou Yu. (2026). Invisible Impact of Empathy on Behavioral Change: Isolating the Effect of Empathy in Long-term Physical Activity Coaching Chatbot Interactions. https://arxiv.org/abs/2606.26641
