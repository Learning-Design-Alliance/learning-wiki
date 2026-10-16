---
type: claim
title: Removing explicit mastery information from learner profiles mainly degrades Adaptivity
description: Removing explicit mastery information from learner profiles mainly degrades Adaptivity
id: mastery-information-needed-for-adaptivity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yu-liu-2026
    resource: "https://doi.org/10.48550/arxiv.2609.18861"
    title: "Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861 [doi:10.48550/arxiv.2609.18861](https://doi.org/10.48550/arxiv.2609.18861)"
    author: Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Removing explicit mastery information from learner profiles mainly degrades Adaptivity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Omitting the Mastery field reduces Adaptivity by 26.1 percentage points for Qwen3-30B-A3B (CoT) while Validity changes much less. [→ Yu Liu 2026](#yu-liu-2026)

## Evidence

### Yu Liu 2026

Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861 [doi:10.48550/arxiv.2609.18861](https://doi.org/10.48550/arxiv.2609.18861)

`q2 · i?` · `design · r2`

Ablation on Basic Education personas (Table 6) in which the Mastery field is removed while goal and curriculum context are held fixed, turning the input into a coarse learner description. The article reports the printed percentage-point drops in Adaptivity across models; no effect size is printed.

> "Removing mastery information reduces Adaptivity by 26.1 percentage points for Qwen3-30B-A3B (CoT), while Validity changes much less."

## Discussion


## Related Claims
- [Contextual noise from irrelevant textbooks broadly degrades KC planning, most in Validity and Efficiency](contextual-noise-degrades-kc-planning.md) — related
- [Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage](cot-effect-varies-model-stage-kc-planning.md) — related
- [Adaptivity to individual learners is the primary bottleneck for LLMs in KC path planning](adaptivity-bottleneck-llm-path-planning.md) — a broader claim this one bears on
- [Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation](skg-dpm-complementary-ablation-deeptutor.md) — related
