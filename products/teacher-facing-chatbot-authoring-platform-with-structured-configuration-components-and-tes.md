---
type: product
id: teacher-facing-chatbot-authoring-platform-with-structured-configuration-components-and-tes
title: Teacher-facing chatbot authoring platform with structured configuration components and testing features
description: A web-based no-code platform developed by Riahi et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# Teacher-facing chatbot authoring platform with structured configuration components and testing features

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
A web-based no-code platform developed by Riahi et al. for teachers to configure, test, and refine classroom chatbots using instructional purposes, behavioral rules, language-model selection, retrieval, and persona traits.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **ASATA authoring pipeline for RegExp/LSA conversation-based assessments**: The AutoTutor Script Authoring Tool for Assessment (ASATA) implemented earlier CBAs by converting conversation diagrams into XML scripts, using LSA and RegExp to parse student responses and determine agent reactions. Conversations included one or two virtual agents interacting with the student and lasted between 2-5 turns. The authors describe this as an expensive methodology requiring time and various expertise: "This process took weeks for conversations to go from the initial descriptions to conversation diagrams to actual script conversations implemented into ASATA and tested with user data." Automated script-based testing of regular expressions with sample responses reduced iterations and testing time but remained limited by the time needed to develop and change regular expressions. (Diego Zapata-Rivera et al. (2024))

### Claims
- [Log-based evaluation showed chatbot alignment was stronger for responsiveness (88.9%) and persona (81.5%) than for rules (70.4%) and purpose (59.3%)](../claims/log-based-alignment-responsiveness-persona-rules-purpose.md) [+M]
- [Teachers used the Purpose field primarily for instructional goals and content focus while Rules specified pedagogical behavior, guardrails, and learner-specific adaptations](../claims/purpose-field-goals-rules-field-pedagogical-behavior.md) [+M]
- [In a case study, LLM-generated assessment conversations handled common student speech acts more naturalistically than RegExp/LSA conversations](../claims/llm-cba-more-naturalistic-than-regexp-lsa.md) [+M]

## Related Products and Programmes

- [AutoTutor Script Authoring Tool (ASAT) and generic AutoTutor Conversation Engine (ACE)](autotutor-script-authoring-tool-asat-and-generic-autotutor-conversation-engine-ace.md)

## Key Sources
- Riahi, B., Ozturk, D., Guth, A., Li, J., Singh, D. P., Tian, X., Chiu, J., Lytle, N., Barnes, T., & Cateté, V. (2026). Will It Teach as Intended? How Teachers Configure Educational AI Chatbots. https://arxiv.org/abs/2609.29993. [doi:10.48550/arxiv.2609.29993](https://doi.org/10.48550/arxiv.2609.29993)
- Diego Zapata-Rivera, Carol Forsyth, Edith Aurora Graf and Yang Jiang. (2024). Designing and Evaluating Evidence-Centered Design based Conversations for Assessment with LLMs. Leveraging Large Language Models for Next Generation Educational Technologies, CEUR Workshop Proceedings. https://ceur-ws.org
