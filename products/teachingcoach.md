---
type: product
id: teachingcoach
title: TeachingCoach
description: TeachingCoach is an AI-based conversational coaching system developed by Isabel Molnar and colleagues to help higher-education instructors diagnose teaching challenges, develop strategies, plan next steps, and reflect through evidence-grounded multi-turn dialogue.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# TeachingCoach

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
TeachingCoach is an AI-based conversational coaching system developed by Isabel Molnar and colleagues to help higher-education instructors diagnose teaching challenges, develop strategies, plan next steps, and reflect through evidence-grounded multi-turn dialogue.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **TeachingCoach data-centric pipeline: rule extraction, synthetic dialogue generation, expert filtering, and fine-tuning**: TeachingCoach is built through a pipeline in which experts extract pedagogical rules from authoritative education resources, GPT-4o generates teacher profiles, teaching challenges, and multi-turn synthetic dialogues, human experts filter the dialogues, and the curated data fine-tune a LLaMA-2-13B-Chat model. The article states that "experts extract 36 core instructional rules and encode them as structured system prompts," anchoring conversations in evidence-based practices. Dialogues progress through clarifying the challenge, exploring strategies, planning next steps, and reflecting. (Isabel Molnar et al. (2026))

### Claims
- [Expert raters rate TeachingCoach higher than a GPT-4o baseline on clarity, tone, reflection, and acknowledgment of user input](../claims/teachingcoach-outperforms-gpt4o-expert-ratings.md) [+M]

## Related Products and Programmes

- [TeachingCoach synthetic dialogue dataset (406,183 training examples)](teachingcoach-synthetic-dialogue-dataset-406183-training-examples.md)

## Key Sources
- Isabel Molnar, Peiyu Li, Si Chen, Sugana Chawla, James Lang, Ronald Metoyer, Ting Hua, Nitesh V. Chawla. (2026). TeachingCoach: A Fine-Tuned Scaffolding Chatbot for Instructional Guidance to Instructors. https://arxiv.org/abs/2603.18189
