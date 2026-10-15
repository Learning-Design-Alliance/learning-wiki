---
type: claim
title: Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage
description: Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage
id: cot-effect-varies-model-stage-kc-planning
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: mixed
sources:
  - id: yu-liu-2026
    resource: "https://doi.org/10.48550/arxiv.2609.18861"
    title: "Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861 [doi:10.48550/arxiv.2609.18861](https://doi.org/10.48550/arxiv.2609.18861)"
    author: Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` In Basic Education, CoT raises Qwen3-30B-A3B's Final Pass from 10.0% to 27.7% and Qwen3-4B-2507's from 3.2% to 20.8%, but Llama-3.1-8B's Validity declines from 19.2% to 14.6%. [→ Yu Liu 2026](#yu-liu-2026)

## Evidence

### Yu Liu 2026

Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861 [doi:10.48550/arxiv.2609.18861](https://doi.org/10.48550/arxiv.2609.18861)

`q2 · i?` · `causal · r2`

Within-model comparison of Zero-shot versus CoT prompting on PersonaPath reported in Table 4 and the Results section. The article reports the Qwen gains and separately that Llama-3.1-8B shows Validity declining from 19.2% to 14.6% and Final Pass from 1.3% to 0.8% under CoT in Basic Education. No effect size is printed.

> "In Basic Education, Qwen3-30B-A3B’s Final Pass rises from 10.0% under Zero-shot prompting to 27.7% with CoT, and Qwen3-4B-2507’s rises from 3.2% to 20.8%."

## Discussion


## Related Claims
- [Strongest LLMs reach only about 29.5% final pass rate on Basic Education KC planning and drop to 14.6% on Higher Education](llm-low-final-pass-kc-planning.md) — related
- [Adaptivity to individual learners is the primary bottleneck for LLMs in KC path planning](adaptivity-bottleneck-llm-path-planning.md) — related
- [Contextual noise from irrelevant textbooks broadly degrades KC planning, most in Validity and Efficiency](contextual-noise-degrades-kc-planning.md) — related
- [One-shot path generation raises Validity but lowers Adaptivity and Efficiency relative to step-by-step interaction](one-shot-generation-lowers-adaptivity.md) — related
- [Removing explicit mastery information from learner profiles mainly degrades Adaptivity](mastery-information-needed-for-adaptivity.md) — related
- Chain-of-thought prompting improved LLM multistep reasoning, operationalized via decomposition and interleaved planning approaches — a broader claim this one bears on
- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](reasoning-prompting-improves-llm-distractor-match.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Retrieval augmentation raises path Validity but not the joint Final Pass rate](rag-raises-validity-not-final-pass.md) — related
- [The two targeted ablations produce small, partially counter-directional effects: removing the construct map does not materially change the composite score (p = 0.34 on equivalence)](varia-ablation-null-effects.md) — related
