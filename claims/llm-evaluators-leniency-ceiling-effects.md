---
type: claim
title: LLM evaluators converged on agent rankings but differed markedly in leniency and discrimination
description: LLM evaluators converged on agent rankings but differed markedly in leniency and discrimination
id: llm-evaluators-leniency-ceiling-effects
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhang-hui-mm-2026
    resource: "https://doi.org/10.2196/96819"
    title: "Zhang Hui MM, Qu Lihui PHD, Zheng Jianmin MMgmt, Xiong Yi MSc, Bai Hongbo MSc, Ji Ruiying MSc, Liu Guohui MSc, Chen Wanling MD, Cheng Zirui MD, Chen Youbang MSc, Yang Chun-tao PhD. (2026). What Platform Scores Miss: Multidimensional Evaluation of AI Teaching Agents in Medical Education. JMIR Medical Education. https://doi.org/10.2196/96819"
    author: Zhang Hui MM, Qu Lihui PHD, Zheng Jianmin MMgmt, Xiong Yi MSc, Bai Hongbo MSc, Ji Ruiying MSc, Liu Guohui MSc, Chen Wanling MD, Cheng Zirui MD, Chen Youbang MSc, Yang Chun-tao PhD
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# LLM evaluators converged on agent rankings but differed markedly in leniency and discrimination

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The 3 LLM evaluators agreed broadly on relative rankings (Spearman ρ=0.64 and 0.71) but DeepSeek and Qwen showed pronounced leniency and ceiling effects, yielding low discrimination (agent-total SD 4.0 and 7.3 vs Claude's 11.6). [→ Zhang Hui MM 2026](#zhang-hui-mm-2026)

## Evidence

### Zhang Hui MM 2026

Zhang Hui MM, Qu Lihui PHD, Zheng Jianmin MMgmt, Xiong Yi MSc, Bai Hongbo MSc, Ji Ruiying MSc, Liu Guohui MSc, Chen Wanling MD, Cheng Zirui MD, Chen Youbang MSc, Yang Chun-tao PhD. (2026). What Platform Scores Miss: Multidimensional Evaluation of AI Teaching Agents in Medical Education. JMIR Medical Education. https://doi.org/10.2196/96819

`q3 · i?` · `design · r2`

Each of 3 LLMs independently scored all 167 dialogues 4 times under the identical rubric with high within-model reproducibility (mean within-model SD≤0.36). "DeepSeek and Qwen showed pronounced leniency, scoring large proportions of dialogues at the ceiling."

> "The 3 models agreed broadly on the relative ranking of agents (Spearman ρ=0.64 and 0.71 for Claude vs DeepSeek and Qwen) but differed substantially in discrimination."

## Discussion


## Related Claims
- [Independent LLM evaluators agreed on agent rankings but differed markedly in leniency, with ceiling effects compressing between-agent discrimination](llm-evaluator-leniency-ceiling-effects.md) — possibly the same claim (merge candidate)
- [Small language models used as automated judges exhibit severe leniency bias against tutoring responses](slm-judges-show-severe-leniency-bias.md) — related
- [LLM-as-a-judge ratings found only small, incremental differences between systems, with ceiling effects on several criteria](llm-judge-small-incremental-differences-ceiling.md) — related
- [RAG prompting shows systematic leniency, over-scoring relative to teacher mean scores in all four rubric dimensions (total bias = 1.787)](rag-systematic-leniency-overscoring.md) — related
