---
type: product
id: leap-learning-with-ai-about-physics
title: LEAP (Learning with AI about Physics)
description: LEAP is a web platform developed for teachers to author physics tasks with tailored LLM instructions and deliver automated formative feedback to students.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-16
---

# LEAP (Learning with AI about Physics)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
LEAP is a web platform developed for teachers to author physics tasks with tailored LLM instructions and deliver automated formative feedback to students.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **LEAP: a web platform where teachers pre-prompt LLMs to assign tasks with formative feedback**: LEAP (Learning with AI about Physics) is a web-based application that lets teachers create physics tasks and set instructions for the LLM without programming skills. Teachers complete four fields (task name, question, instructions for the LLM, correct answer) and share a link with students, who submit answers and receive LLM-generated formative feedback. The article states LEAP "empowers educators to create content and formulate prompts for the LLM" so that feedback types can be tailored without technical expertise. The platform uses Flask, SQLAlchemy, MariaDB, Gunicorn and Nginx, and currently offers OpenAI models, with GPT-4o mini free. (Steinert et al. (2024))

### Claims

- [Systematic prompting of an LLM can generate cognitively activating formative feedback aligned with research-based scaffold types (demonstrated, not yet empirically validated)](../claims/leap-prompt-design-generates-cognitively-activating-feedback.md) [+W]
- [Teacher-provided correct answers and pre-prompting reduce erroneous LLM output and hallucinations compared with open chatbot use](../claims/leap-pre-prompting-reduces-hallucinations.md) [+W]
- [More complex prompts tend to elicit superior results with advanced LLM versions (authors' observation)](../claims/complex-prompts-elicit-better-llm-results.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Steinert, S., Avila, K. E., Ruzika, S., Kuhn, J., & Küchemann, S. (2024). Harnessing large language models to develop research-based learning assistants for formative feedback. Smart Learning Environments. https://doi.org/10.1186/s40561-024-00354-1
