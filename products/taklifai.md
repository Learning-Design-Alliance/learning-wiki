---
type: product
id: taklifai
title: Taklif.AI
description: Taklif.AI is an LLM-powered platform developed by Kurdya et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Taklif.AI

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
Taklif.AI is an LLM-powered platform developed by Kurdya et al. for automatically generating personalized college assignments based on students' extracurricular interests and cultural context.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Six specialized role-assigned prompts sharing a four-part structure for assignment generation and guardrails**: Taklif.AI's prompt engineering pipeline assigns distinct LLM roles and tasks across six prompts (personalize-assignment, simplify-assignment, assignment-guardrails, interest-guardrails, output-guardrails, pdf-ocr). The article states: "We employ six specialized prompts, each assigned a distinct LLM role and task (Table 3). All prompts follow a consistent four-part structure": role definition, task specification, context and constraints, and output formatting. Zero-shot prompting is adopted to maximize generalizability, with prompts iteratively refined using LangSmith evaluation tools. (Zaki Kurdya et al. (2026))

### Claims

- [In preliminary user acceptance testing, 84% of participants rated Taklif.AI's personalization feature as beneficial](../claims/uat-84-percent-rate-personalization-beneficial.md) [+W]
- [Under a simulated load of 100 concurrent users, Taklif.AI averaged 30 seconds end-to-end response time per request](../claims/load-test-100-concurrent-users-30-second-response.md) [~W]
- [During development testing, Taklif.AI guardrails rejected roughly 12% of interests, 8% of input documents, and 3% of generated assignments](../claims/guardrails-rejection-rates-development-testing.md) [+W]
- [91% of UAT participants rated the Taklif.AI user interface as intuitive](../claims/uat-91-percent-rate-interface-intuitive.md) [+W]

## Related Products and Programmes

- [Waterproof](waterproof.md)

## Key Sources
- Zaki Kurdya, Mohammed Zuqlam, Salem Amassi, Shady Telbany, Motaz Saad. (2026). Taklif.AI: LLM-Powered Platform for Interest-Based Personalized College Assignments. https://arxiv.org/abs/2605.05842
