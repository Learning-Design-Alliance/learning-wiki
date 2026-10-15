---
type: claim
title: Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs
description: Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs
id: reasoning-prompting-improves-llm-distractor-match
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yanick-zengaffinen-2026
    resource: "https://doi.org/10.48550/arxiv.2603.15547"
    title: "Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547 [doi:10.48550/arxiv.2603.15547](https://doi.org/10.48550/arxiv.2603.15547)"
    author: Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Moving from direct prompting to CoT or reasoning prompting significantly improves proportional match for both models and both datasets. [→ Yanick Zengaffinen 2026](#yanick-zengaffinen-2026)

## Evidence

### Yanick Zengaffinen 2026

Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547 [doi:10.48550/arxiv.2603.15547](https://doi.org/10.48550/arxiv.2603.15547)

`q2 · i?` · `causal · r2`

Output-level evaluation of DEEPSEEK-V3.2 and GLM-4.7 across direct, CoT, and reasoning prompting on Eedi and SciQ; Table 2 reports e.g. DS-V3.2 on Eedi rising from 0.34±0.03 (direct) to 0.52±0.03 (reasoning). The article reports the improvement as "significant" with no effect size.

> "We find that proportional match improves significantly when moving from direct prompting to either CoT or reasoning for both LLMs and datasets (Table 2)."

## Discussion


## Related Claims
- [Providing the correct solution in the prompt improves LLM alignment with human-authored distractors, confirming correct-solution recovery as a primary bottleneck](correct-solution-in-prompt-bottleneck.md) — related
- [LLM distractor-generation strategies differ by domain: error description and simulation dominate on math while conceptual linking and discriminability checks dominate on science](domain-shift-link-versus-error-strategies.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- Chain-of-thought prompting improved LLM multistep reasoning, operationalized via decomposition and interleaved planning approaches — related
- [Reasoning-capable model variants and chain-of-thought prompting yield no measurable improvement in either alignment axis for classroom evaluation](reasoning-variants-no-alignment-improvement.md) — related
- [Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage](cot-effect-varies-model-stage-kc-planning.md) — related
- [Chain-of-Thought rationale quality shows no direct correlation with the accuracy of simulated student responses](cot-rationale-quality-no-correlation-simulated-accuracy.md) — related
- [The two targeted ablations produce small, partially counter-directional effects: removing the construct map does not materially change the composite score (p = 0.34 on equivalence)](varia-ablation-null-effects.md) — related
