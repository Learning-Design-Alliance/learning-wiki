---
type: research-method
id: tool-supported-workflow-for-identifying-clustering-and-visualizing-common-modelling-mistak
title: Tool-supported workflow for identifying, clustering, and visualizing common modelling mistakes as bug fixing transformations
description: A three-step workflow in which candidates for common mistakes are represented as bug fixing transformations that locally rewrite incorrect syntax trees into correct ones.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Tool-supported workflow for identifying, clustering, and visualizing common modelling mistakes as bug fixing transformations

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A three-step workflow in which candidates for common mistakes are represented as bug fixing transformations that locally rewrite incorrect syntax trees into correct ones. Step (1) generates candidates with an LLM and validates them algorithmically, keeping transformations that explain a delta-fraction of the data; Step (2) clusters candidates by similarity via a correlation graph; Step (3) visualizes clusters for instructors and CS education researchers. The article frames it as replacing time-consuming manual inspection of large educational datasets.

## Accounts
<!-- How each source describes or uses the method -->
- **Tool-supported workflow for identifying, clustering, and visualizing common modelling mistakes as bug fixing transformations**: A three-step workflow in which candidates for common mistakes are represented as bug fixing transformations that locally rewrite incorrect syntax trees into correct ones. Step (1) generates candidates with an LLM and validates them algorithmically, keeping transformations that explain a delta-fraction of the data; Step (2) clusters candidates by similarity via a correlation graph; Step (3) visualizes clusters for instructors and CS education researchers. The article frames it as replacing time-consuming manual inspection of large educational datasets. (Lilian Killich et al. (2026))

### Claims
- [On the full propositional logic dataset, LLM-found bug fixing transformations explain 84.44% of pairs versus 71.57% for hand-picked mistakes](../claims/llm-transformations-explain-more-propositional-pairs-than-hand-picked.md) [+M]
- [The workflow generalizes beyond propositional logic, explaining 79.39% of modal logic pairs and 35.89% of CTL pairs](../claims/workflow-generalizes-to-modal-logic-and-ctl.md) [+M]

## Related Research Methods
-

## Key Sources
- Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111
