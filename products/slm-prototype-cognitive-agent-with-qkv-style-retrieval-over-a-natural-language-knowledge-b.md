---
type: product
id: slm-prototype-cognitive-agent-with-qkv-style-retrieval-over-a-natural-language-knowledge-b
title: SLM prototype Cognitive Agent with QKV-style retrieval over a natural-language Knowledge Base
description: A research prototype developed by Hyeongdon Moon et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# SLM prototype Cognitive Agent with QKV-style retrieval over a natural-language Knowledge Base

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
A research prototype developed by Hyeongdon Moon et al. that uses a small language model, retrieval over a structured natural-language knowledge base, and a teacher language model to support multi-step problem solving.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->

### Claims

- [Model size defines a core trade-off: too-large SLMs answer without the cognitive structure while too-small SLMs break instruction-following coherence](../claims/curse-of-prior-knowledge-size-tradeoff.md) [+W]
- [An SLM executor under tight constraints can drive a Cognitive Agent through formatted outputs and logit-based action selection, yielding partial rather than full explainability](../claims/slm-executor-partial-explicit-control.md) [+W]
- [The CAC proof of concept compiled 27 biology problems successfully, accumulating 188 Declarative Memory entries, but failed on the 28th problem](../claims/cac-proof-of-concept-27-problems-188-dms.md) [+W]
- [Similarity-based retrieval degrades as the Knowledge Base grows, consistent with the fan effect, stalling the agent](../claims/fan-effect-kb-growth-retrieval-degradation.md) [+W]
- [A 4-bit quantized 27B local Teacher LLM generated knowledge in the required format, suggesting accessible-resource implementations may be feasible](../claims/quantized-local-teacher-llm-feasible.md) [+W]
- [Instances occurred where the Teacher LLM directly provided the final answer, bypassing the intended cognitive process, and can be programmatically filtered](../claims/collaborative-cheating-teacher-provides-answer.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040
