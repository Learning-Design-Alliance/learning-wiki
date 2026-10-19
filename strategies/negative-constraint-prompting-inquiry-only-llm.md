---
type: strategy
id: negative-constraint-prompting-inquiry-only-llm
title: Constrain an LLM to inquiry-only questioning via negative system-prompt constraints plus strict JSON schemas
description: "The article's constraint methodology combines three mechanisms: system prompts with explicit negative constraints (\"Do NOT rewrite the student's text\", \"Avoid yes/no questions\"), a specified internal reasoning protoco..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: ran-bi-2026
    resource: "https://arxiv.org/abs/2605.05598"
    title: "Ran Bi, Shiyao Wei, Yuanyiyi Zhou. (2026). Prober.ai: Gated Inquiry-Based Feedback via LLM-Constrained Personas for Argumentative Writing Development. https://arxiv.org/abs/2605.05598"
    author: Ran Bi, Shiyao Wei, Yuanyiyi Zhou
---

# Constrain an LLM to inquiry-only questioning via negative system-prompt constraints plus strict JSON schemas

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's constraint methodology combines three mechanisms: system prompts with explicit negative constraints ("Do NOT rewrite the student's text", "Avoid yes/no questions"), a specified internal reasoning protocol the model executes without outputting (argument segmentation, issue detection, epistemic state classification, trigger prioritization), and OpenAI Structured Outputs with strict: true so the model is constrained at decode time to emit only conformant JSON. Returned excerpts are verified as exact substrings of the essay and silently dropped otherwise, so hallucinated quotations cannot drive contextual highlighting.

## Design Implications

### Context
#### Requirements
- Access to an API supporting decode-time schema enforcement (OpenAI Responses API Structured Outputs)
- A pedagogy guide document injected as internal context codifying question module taxonomy and templates
#### Constraints
- Structured Outputs guarantees output form but not pedagogical quality; the system lacks a post-generation quality filter or rubric-based validation layer

### Target Learners
- K–12 argumentative writing students

### Target Learning Goals
- inquiry-based feedback on argument structure

## Claims

- [Schema-constrained Structured Outputs eliminated parse failures: every /challenge and /unlock call returned a valid, fully-typed object during development testing](../claims/structured-outputs-eliminate-parse-failure-class.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Ran Bi, Shiyao Wei, Yuanyiyi Zhou. (2026). Prober.ai: Gated Inquiry-Based Feedback via LLM-Constrained Personas for Argumentative Writing Development. https://arxiv.org/abs/2605.05598
