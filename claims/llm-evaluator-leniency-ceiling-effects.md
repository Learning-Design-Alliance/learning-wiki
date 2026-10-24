---
type: claim
title: Independent LLM evaluators agreed on agent rankings but differed markedly in leniency, with ceiling effects compressing between-agent discrimination
description: Independent LLM evaluators agreed on agent rankings but differed markedly in leniency, with ceiling effects compressing between-agent discrimination
id: llm-evaluator-leniency-ceiling-effects
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhang-hui-2026
    resource: "https://doi.org/10.2196/96819"
    title: "Zhang Hui, Qu Lihui, Zheng Jianmin, Xiong Yi, Bai Hongbo, Ji Ruiying, Liu Guohui, Chen Wanling, Cheng Zirui, Chen Youbang, Yang Chun-tao. (2026). What Platform Scores Miss: Multidimensional Evaluation of AI Teaching Agents in Medical Education. JMIR Medical Education. https://doi.org/10.2196/96819"
    author: Zhang Hui, Qu Lihui, Zheng Jianmin, Xiong Yi, Bai Hongbo, Ji Ruiying, Liu Guohui, Chen Wanling, Cheng Zirui, Chen Youbang, Yang Chun-tao
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Independent LLM evaluators agreed on agent rankings but differed markedly in leniency, with ceiling effects compressing between-agent discrimination

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Claude, DeepSeek, and Qwen agreed broadly on agent rankings (Spearman ρ=0.64 and 0.71) but Qwen scored above 90% of dialogues at ceiling on three dimensions, yielding low discrimination (agent-total SD 4.0 and 7.3 vs Claude's 11.6). [→ Zhang Hui 2026](#zhang-hui-2026)

## Evidence

### Zhang Hui 2026

Zhang Hui, Qu Lihui, Zheng Jianmin, Xiong Yi, Bai Hongbo, Ji Ruiying, Liu Guohui, Chen Wanling, Cheng Zirui, Chen Youbang, Yang Chun-tao. (2026). What Platform Scores Miss: Multidimensional Evaluation of AI Teaching Agents in Medical Education. JMIR Medical Education. https://doi.org/10.2196/96819

`q2 · i?` · `design · r2`

Robustness check in which 3 LLMs each scored all 167 dialogues 4 times under the identical rubric; the article reports rank agreement "Spearman ρ=0.64 and 0.71" alongside large differences in ceiling rates and agent-total SDs.

> "The 3 models agreed broadly on the relative ranking of agents (Spearman ρ=0.64 and 0.71 for Claude vs DeepSeek and Qwen) but differed substantially in discrimination."

## Discussion


## Related Claims
- [Small language models used as automated judges exhibit severe leniency bias against tutoring responses](slm-judges-show-severe-leniency-bias.md) — related
- [Judge and crowd broadly agree on which criteria matter, but the judge's near-identical top scores make its ranking of strong systems essentially random](judge-crowd-agree-on-criteria-but-scores-separate-nothing.md) — related
- [LLM-as-a-judge ratings found only small, incremental differences between systems, with ceiling effects on several criteria](llm-judge-small-incremental-differences-ceiling.md) — related
- [Platform-generated scores and rubric-based teaching quality produced substantially divergent rankings of the same AI teaching agents](platform-rubric-rankings-diverge-ai-teaching-agents.md) — related
- [The LLM-judge separates weak submissions but its ranking of the strongest systems has almost no agreement with crowd ranking (Spearman ρ = −0.17)](llm-judge-ranks-strongest-systems-poorly.md) — related
- [Survey items show good discrimination overall, but several items exhibit ceiling effects that limit measuring change over time](survey-item-discrimination-and-ceiling-effects.md) — related
- [RAG prompting shows systematic leniency, over-scoring relative to teacher mean scores in all four rubric dimensions (total bias = 1.787)](rag-systematic-leniency-overscoring.md) — related
- [Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)](judge-anchoring-raises-human-agreement.md) — related
