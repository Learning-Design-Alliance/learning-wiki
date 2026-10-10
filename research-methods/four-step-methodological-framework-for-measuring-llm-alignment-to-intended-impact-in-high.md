---
type: research-method
id: four-step-methodological-framework-for-measuring-llm-alignment-to-intended-impact-in-high
title: Four-step methodological framework for measuring LLM alignment to intended impact in high-noise contexts
description: The article proposes a general framework for evaluating whether LLM judgments align with real-world outcomes when experimental control is infeasible.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Four-step methodological framework for measuring LLM alignment to intended impact in high-noise contexts

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes a general framework for evaluating whether LLM judgments align with real-world outcomes when experimental control is infeasible. It comprises (1) correlating behaviors across the space of generalization with dCor2n dependence measures, (2) measuring best-proxy alignment on downstream tasks using Kendall's tau, described as "a simple, strong option that can be estimated with any datatype", (3) establishing real-world baselines such as teacher experience or prior VAM, and (4) decomposing misalignment error variance via Generalizability Theory. It was applied to classroom-transcript scoring against expert ratings and value-added measures.

## Accounts
<!-- How each source describes or uses the method -->
- **A four-step methodological framework for measuring LLM alignment to intended impact in high-noise contexts**: The article proposes a general framework for evaluating whether LLM judgments align with real-world outcomes when experimental control is infeasible. It comprises (1) correlating behaviors across the space of generalization with dCor2n dependence measures, (2) measuring best-proxy alignment on downstream tasks using Kendall's tau, described as "a simple, strong option that can be estimated with any datatype", (3) establishing real-world baselines such as teacher experience or prior VAM, and (4) decomposing misalignment error variance via Generalizability Theory. It was applied to classroom-transcript scoring against expert ratings and value-added measures. (Michael Hardy (2026))

### Claims
- [Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions](../claims/variance-decomposition-model-prompt-weak-levers.md) [+M]
- [LLM alignment with expert teaching ratings does not predict, and is often negatively associated with, alignment with student learning gains](../claims/proxy-alignment-not-impact-alignment-llm-classroom.md) [+M]

## Related Research Methods
-

## Key Sources
- Michael Hardy, Yunsung Kim. (2026). Knowledge without Wisdom: Measuring Misalignment between LLMs and Intended Impact. arXiv. https://arxiv.org/abs/2603.00883
