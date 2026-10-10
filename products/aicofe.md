---
type: product
id: aicofe
title: AICoFe
description: AICoFe is a human-centered AI collaborative feedback system developed by Alvaro Becerra and colleagues that supports peer, self-, and teacher assessment through customized rubrics, multimodal performance recording, dashboards, and mediated AI-generated feedback.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# AICoFe

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · no claims cited

## Description
AICoFe is a human-centered AI collaborative feedback system developed by Alvaro Becerra and colleagues that supports peer, self-, and teacher assessment through customized rubrics, multimodal performance recording, dashboards, and mediated AI-generated feedback.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Multi-LLM feedback generation pipeline combining three independently fine-tuned models**: AICoFe's Feedback Generation Module extends prior single-model work to a multi-model setting in which "three independent feedback instances are generated, one per LLM" (GPT-4.1-mini, Gemini 2.5 Flash, Llama 3.1). Each model receives the same structured prompt built from average rubric scores, validated qualitative observations, rubric level descriptions, and instructional materials. Using three distinct models is argued to enrich feedback with diverse perspectives while reducing the risk of single-model biases or systematic errors reaching students. Each instance follows a three-paragraph structure: strengths, areas for improvement, and an action plan. (Alvaro Becerra et al. (2026))
- **Hybrid SQL and MongoDB data infrastructure for traceability of feedback versions**: AICoFe's Management Module integrates two complementary database technologies: a relational SQL database managing structured academic data such as courses, rubric definitions, user accounts, and evaluators' scores and comments; and a MongoDB document store for semi-structured data that varies in shape across evaluation instances, including multiple LLM feedback versions, teacher drafts and curations, per-sentence metadata with source LLM, and coherence/usefulness ratings. A File Service manages audiovisual recordings linked to evaluation instances. (Alvaro Becerra et al. (2026))

### Claims

## Related Products and Programmes
-

## Key Sources
- Alvaro Becerra, Alejandra Palma and Ruth Cobos. (2026). AICoFe: Implementation and Deployment of an AI-Based Collaborative Feedback System for Higher Education. LASI Spain 26: Learning Analytics Summer Institute Spain 2026. https://orcid.org/0009-0003-7793-2682
