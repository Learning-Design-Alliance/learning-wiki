---
type: claim
title: On the LearnArena benchmark, GPT-4o achieves the best average win rate (0.77), and learning ability improves with model scale but with diminishing gains
description: On the LearnArena benchmark, GPT-4o achieves the best average win rate (0.77), and learning ability improves with model scale but with diminishing gains
id: learnarena-gpt4o-best-scale-diminishing-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: zhengyu-hu-2025
    resource: "https://doi.org/10.52202/085713-5760"
    title: "Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Seraphina Zhang, Tianfu Wang, Nicholas Jing Yuan, Xing Xie, Hui Xiong. (2025). Unveiling the Learning Mind of Language Models: A Cognitive Framework and Empirical Study. NeurIPS 2025. [doi:10.52202/085713-5760](https://doi.org/10.52202/085713-5760)"
    author: Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Seraphina Zhang, Tianfu Wang, Nicholas Jing Yuan, Xing Xie, Hui Xiong
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: zhengyu-hu-2025-2
    resource: "https://doi.org/10.52202/085713-5760"
    title: "Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Seraphina Zhang, Tianfu Wang, Nicholas Jing Yuan, Xing Xie, Hui Xiong. (2025). Unveiling the Learning Mind of Language Models: A Cognitive Framework and Empirical Study. NeurIPS 2025. [doi:10.52202/085713-5760](https://doi.org/10.52202/085713-5760)"
    author: Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Seraphina Zhang, Tianfu Wang, Nicholas Jing Yuan, Xing Xie, Hui Xiong
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# On the LearnArena benchmark, GPT-4o achieves the best average win rate (0.77), and learning ability improves with model scale but with diminishing gains

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4o achieves an average win rate of 0.77 across the eight LearnArena tasks, outperforming all other evaluated models. [→ Zhengyu Hu 2025](#zhengyu-hu-2025)
`q2 i?` Within the Qwen2.5 series, performance increases steadily from 7B (0.34) to 14B (0.47) to 32B (0.51), but the gains diminish with scale; newer Qwen3 models outperform other open-source models, indicating architectural and training advancements matter beyond scale. [→ Zhengyu Hu 2025 (2)](#zhengyu-hu-2025-2)

## Evidence

### Zhengyu Hu 2025

Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Seraphina Zhang, Tianfu Wang, Nicholas Jing Yuan, Xing Xie, Hui Xiong. (2025). Unveiling the Learning Mind of Language Models: A Cognitive Framework and Empirical Study. NeurIPS 2025. [doi:10.52202/085713-5760](https://doi.org/10.52202/085713-5760)

`q2 · i?` · `design · r2`

LearnArena benchmark evaluation of ten models across eight environments (Checkers, Stratego, Tic Tac Toe, Truth and Deception, SpellingBee, SpiteAndMalice, Tak, WordChains), 20 matches per model-environment pair. The article reports GPT-4o "achiev- ing an average win rate of 0.77 across the eight tasks"; no effect size printed.

> "First, GPT-4o sets a new state-of-the-art, achiev- ing an average win rate of 0.77 across the eight tasks, significantly outper- forming all other models."

### Zhengyu Hu 2025 (2)

Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Seraphina Zhang, Tianfu Wang, Nicholas Jing Yuan, Xing Xie, Hui Xiong. (2025). Unveiling the Learning Mind of Language Models: A Cognitive Framework and Empirical Study. NeurIPS 2025. [doi:10.52202/085713-5760](https://doi.org/10.52202/085713-5760)

`q2 · i?` · `causal · r1`

Same LearnArena evaluation, comparing Qwen2.5 series scales and Qwen3 models. The article reports "performance increases steadily from 7B (0.34) to 14B (0.47) and 32B (0.51)" with diminishing gains, and Qwen3-14B reaching 0.60; no effect size printed.

> "within the Qwen2.5 series, we observe scale-driven improvement: performance increases steadily from 7B (0.34) to 14B (0.47) and 32B (0.51), confirming that learning ability benefits from increased capacity, but only up to a point. The gains diminish with scale."

## Discussion


## Related Claims
- [The reasoning model o3-mini/low wins most often among judge models but does not significantly outperform the non-reasoning GPT-4o models](reasoning-model-no-significant-judge-advantage.md) — related
- [GPT-4 achieves passing accuracy on USMLE Steps 1–3 (mean 86%), significantly exceeding GPT-3.5 (mean 56%)](gpt4-usme-passing-accuracy-exceeds-gpt35.md) — related
- [Full-scale LLM versions consistently achieve higher agreement with human grades than their mini and nano counterparts](full-scale-llms-outperform-mini-nano-grading.md) — related
