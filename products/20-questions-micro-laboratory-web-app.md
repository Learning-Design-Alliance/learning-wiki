---
type: product
id: 20-questions-micro-laboratory-web-app
title: 20 Questions micro-laboratory web app
description: A Python-based Hugging Face Spaces web application with a companion Google Colab notebook that lets learners investigate stochastic LLM behaviour through a constrained 20 Questions game, rewind and re-sampling controls, and temperature adjustment.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# 20 Questions micro-laboratory web app

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A Python-based Hugging Face Spaces web application with a companion Google Colab notebook that lets learners investigate stochastic LLM behaviour through a constrained 20 Questions game, rewind and re-sampling controls, and temperature adjustment.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **20 Questions micro-laboratory web app with rewind and re-sample controls exposing LLM probabilistic mechanics**: A Python-based web application hosted on Hugging Face Spaces (with a companion Google Colab Notebook) implementing a reduced 10-question "20 Questions" game restricted to physical objects, with Yes/No answers plus short justifications. The interface is split into phases: a linear gameplay phase that hides experimental controls to preserve the "illusion" of determinism, then a "Laboratory" mode unlocking a dropdown to select a bifurcation point, restart from that question, and a Re-sample button to repeat the same question against the same antecedent history. Users can also set the Temperature via a slider to adjust response variance. (Tufino (2026))

### Claims
- [Re-sampling the same question against a fixed interaction history produces diverging LLM answers, revealing stochastic flips and trajectory bifurcation](../claims/llm-resampling-reveals-stochastic-flips.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Tufino, E. (2026). Demystifying the oracle: A "20 Questions" game to promote AI ethics and literacy. https://github.com/etufino/AI-20-questions-game. [doi:10.48550/arxiv.2602.01254](https://doi.org/10.48550/arxiv.2602.01254)
