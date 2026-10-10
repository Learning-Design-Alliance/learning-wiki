---
type: product
id: colearn-deployable-containerised-web-system
title: CoLearn deployable containerised web system
description: CoLearn is a containerised web application developed by Kailai He et al.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# CoLearn deployable containerised web system

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · no claims cited

## Description
CoLearn is a containerised web application developed by Kailai He et al. for adaptive diagnostic Biology and Chemistry practice with LLM-generated questions and misconception feedback.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **CoLearn deployable containerised web system (Vite/React SPA, FastAPI backend, provider-selectable LLM)**: CoLearn is a container-deployed web application whose frontend is a Vite + React + TypeScript single-page app and whose backend is FastAPI with an async MongoDB store, JWT/bcrypt authentication, and SSE streaming for live generation and grading. The LLM backend is provider-selectable (AWS Bedrock with Claude Sonnet 4.5 as the live default; an OpenAI-compatible path is also supported). "The whole stack starts with one command via Docker Compose", and the backend ships with a test suite covering BKT, grading, generation, streaming, RBAC, and the A/B analytics. (Kailai He et al. (2026))

### Claims

## Related Products and Programmes
-

## Key Sources
- Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154
