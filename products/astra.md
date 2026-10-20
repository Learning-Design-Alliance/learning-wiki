---
type: product
id: astra
title: ASTRA
description: ASTRA is an end-to-end air-traffic-control training simulator developed by Ethan Chew and colleagues that automates the simpilot role through speech recognition, response generation, and geospatial scenario visualization.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# ASTRA

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
ASTRA is an end-to-end air-traffic-control training simulator developed by Ethan Chew and colleagues that automates the simpilot role through speech recognition, response generation, and geospatial scenario visualization.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **ASTRA Synthetic Benchmark Dataset: an open synthetic trace dataset for collaborative programming evaluation**: An openly archived synthetic dataset mirroring the ASTRA logging schema, encoding a prespecified between-subjects design across three conditions (alone_tutor, pair_tutor, pair_multiagent) and a bank of 20 short Python tasks. It provides turn-level dialogue traces with speaker roles, task-level artefacts (submitted code, correctness, retries, time-to-correct, verification indicators), and a derived-metrics table with precomputed summaries. The article states it is "best interpreted as simulated evidence that supports benchmarking and method development". (Solomon Sunday Oyelere (2026))
- **ASTRA prototype: open-source multi-agent tutoring web application with JSONL trace logging**: A Python Streamlit web application wrapping a multi-agent backend around an LLM API (gpt-4o-mini by default). It instantiates a Pedagogical Tutor Agent (PTA) for conceptual and metacognitive support and a Collaborative Group Agent (CGA) for participation balance and coordination, maintains a lightweight CASM learner-state profile inferred as JSON after each student message, and writes turn-level and solution records to JSON Lines files. The article states the implementation and logging schema are released "as open-source software (Oyelere, 2026b), enabling replication, stress-testing, and extension of trace-based analyses". (Solomon Sunday Oyelere (2026))
- **ASTRA social–cognitive framework for multi-agent tutoring**: A framework formalising how social, cognitive, and regulatory information guides multi-agent tutoring in collaborative programming. It models a session as a partially observable multi-agent process in which "ASTRA instantiates the latent state z_t using a structured Cognitive–Affective–Social Model (CASM)" with cognitive, metacognitive, socio-emotional, and group-regulation components. Role-differentiated agents (Tutor, Facilitator, optional Coordinator) condition policies on a belief state over this latent state, and support is framed as optimising a multi-objective reward over task progress, metacognitive quality, and participation-oriented equity proxies. (Solomon Sunday Oyelere (2026))

### Claims

- [XTTS and Orpheus achieve the highest human-rated MOS for Singaporean-accented ATC speech synthesis (3.71 and 3.70), with female voices preferred across models](../claims/astra-tts-mos-xtts-orpheus-best.md) [+W]
- [DSPy prompt optimization improves all radiotelephony evaluators, with the largest gain in accuracy (+7.9%)](../claims/dspy-optimization-communication-evaluator-gains.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim. (2026). ASTRA: A Scalable Next-Generation ATCO Training Simulator with Autonomous Simpilots. https://arxiv.org/abs/2606.18319
- Solomon Sunday Oyelere. (2026). ASTRA: A synthetic benchmark for trace-based evaluation of socially intelligent multi-agent tutoring and participation-balanced collaboration in introductory programming. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100633
