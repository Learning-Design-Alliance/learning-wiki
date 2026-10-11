---
type: research-method
id: fsm-based-evaluation-of-interactivity-in-ai-generated-educational-materials-ee-eval
title: FSM-based evaluation of interactivity in AI-generated educational materials (EE-Eval)
description: "The article conceptualizes interactivity as \"a finite space of learner-controllable states and transitions\", represented as a directed graph G = (V, E, M) where V denotes semantic interaction states, E transitions, and M task-level metadata such as pedagogical intent."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# FSM-based evaluation of interactivity in AI-generated educational materials (EE-Eval)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The article conceptualizes interactivity as "a finite space of learner-controllable states and transitions", represented as a directed graph G = (V, E, M) where V denotes semantic interaction states, E transitions, and M task-level metadata such as pedagogical intent. Interaction logic is operationalized with a JSON-based schema capturing states, events, transitions, and components, extracted from generated HTML via a few-shot LLM strategy and validated against schema constraints. Evaluation compares extracted FSMs to semi-automatically constructed ideal FSMs using structural (node/edge counts, degree distributions, density), semantic (embedding-based comparison of state labels, actions, events, metadata), and behavioral-coherence (isomorphism score) metrics, weighted 0.4/0.4/0.2 after a constrained grid search.

## Accounts
<!-- How each source describes or uses the method -->
- **FSM-based representation of interactivity as learner-controllable states and transitions (EE-Eval)**: The article conceptualizes interactivity as "a finite space of learner-controllable states and transitions", represented as a directed graph G = (V, E, M) where V denotes semantic interaction states, E transitions, and M task-level metadata such as pedagogical intent. Interaction logic is operationalized with a JSON-based schema capturing states, events, transitions, and components, extracted from generated HTML via a few-shot LLM strategy and validated against schema constraints. Evaluation compares extracted FSMs to semi-automatically constructed ideal FSMs using structural (node/edge counts, degree distributions, density), semantic (embedding-based comparison of state labels, actions, events, metadata), and behavioral-coherence (isomorphism score) metrics, weighted 0.4/0.4/0.2 after a constrained grid search. (Xiaozao Wang et al. (2026))

### Claims
- [FSM-based evaluation aligns with human judgments of interactivity, functional correctness, and visual quality more strongly than VLM and unit-test baselines on balanced data](../claims/fsm-eval-aligns-with-human-interactivity-judgments.md) [+M]
- [FSM-based evaluation discriminates interactive quality across models, with GPT-5 Mini scoring highest and most tiers significantly separated](../claims/fsm-eval-discriminates-model-quality.md) [+M]

## Related Research Methods
-

## Key Sources
- Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012
