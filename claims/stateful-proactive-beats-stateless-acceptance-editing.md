---
type: claim
title: Stateful proactive collaboration (L2) yields higher acceptance and lower editing effort than stateless proactive collaboration (L1), with lower acceptance in creative than scientific domains
description: Stateful proactive collaboration (L2) yields higher acceptance and lower editing effort than stateless proactive collaboration (L1), with lower acceptance in creative than scientific domains
id: stateful-proactive-beats-stateless-acceptance-editing
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: youqing-fang-2026
    resource: "https://doi.org/10.48550/arxiv.2605.23535"
    title: "Youqing Fang, Yinhao Tang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Bin Liu, Weiming Zhang, Kuikun Liu, Wenwei Zhang, Kai Chen. (2026). MindCopilot: Towards Formalizing and Evaluating Granular Human-LLM Co-Writing. arXiv preprint. https://arxiv.org/abs/2605.23535 [doi:10.48550/arxiv.2605.23535](https://doi.org/10.48550/arxiv.2605.23535)"
    author: Youqing Fang, Yinhao Tang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Bin Liu, Weiming Zhang, Kuikun Liu, Wenwei Zhang, Kai Chen
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: youqing-fang-2026-2
    resource: "https://arxiv.org/abs/2605.23535"
    title: "Youqing Fang, Yinhao Tang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Bin Liu, Weiming Zhang, Kuikun Liu, Wenwei Zhang, Kai Chen. (2026). MindCopilot: Towards Formalizing and Evaluating Granular Human-LLM Co-Writing. arXiv preprint. https://arxiv.org/abs/2605.23535"
    author: Youqing Fang, Yinhao Tang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Bin Liu, Weiming Zhang, Kuikun Liu, Wenwei Zhang, Kai Chen
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Stateful proactive collaboration (L2) yields higher acceptance and lower editing effort than stateless proactive collaboration (L1), with lower acceptance in creative than scientific domains

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r1`–`r2` · `q2`

## Subclaims
`q2 i?` Moving from L1 stateless to L2 stateful proactive collaboration yields systematic gains in acceptance rate and reduced editing effort across evaluated models. [→ Youqing Fang 2026](#youqing-fang-2026)
`q2 i?` Acceptance rates are consistently lower in Creative than Scientific domains across models and interaction settings. [→ Youqing Fang 2026 (2)](#youqing-fang-2026-2)

## Evidence

### Youqing Fang 2026

Youqing Fang, Yinhao Tang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Bin Liu, Weiming Zhang, Kuikun Liu, Wenwei Zhang, Kai Chen. (2026). MindCopilot: Towards Formalizing and Evaluating Granular Human-LLM Co-Writing. arXiv preprint. https://arxiv.org/abs/2605.23535 [doi:10.48550/arxiv.2605.23535](https://doi.org/10.48550/arxiv.2605.23535)

`q2 · i?` · `causal · r2`

Controlled simulation evaluating multiple language models under L1 and L2 paradigms using 60 human-authored articles across 16 domains, segmented into 1,688 continuation queries with fixed ground-truth continuations to isolate the effect of interaction structure. Table 4 prints, for example, GPT-5.1 overall HAR rising from 17.59 (L1) to 19.61 (L2).

> "Moving from L1 to L2 further yields systematic gains in acceptance and reduced editing effort, underscoring the value of stateful intent modeling."

### Youqing Fang 2026 (2)

Youqing Fang, Yinhao Tang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Bin Liu, Weiming Zhang, Kuikun Liu, Wenwei Zhang, Kai Chen. (2026). MindCopilot: Towards Formalizing and Evaluating Granular Human-LLM Co-Writing. arXiv preprint. https://arxiv.org/abs/2605.23535

`q2 · i?` · `causal · r1`

The same controlled simulation across 16 writing domains shows the domain contrast in Table 4; the article attributes the pattern to "the higher semantic openness of creative writing." For example, GPT-5.1 L1 HAR is 21.47 scientific versus 12.25 creative.

> "Acceptance rates are consistently lower in Creative than Scientific domains.This pattern is consistently observed across models and interaction settings (Table4) and is characteristic of the higher semantic openness of creative writing."

## Discussion


## Related Claims
- [Acceptance rates increase with writing progress, with the L2-over-L1 advantage widening in later stages](acceptance-increases-with-writing-progress.md) — related
- [In a 30-participant user study, proactive paradigms are preferred over user-initiated interaction, with lower workload, fewer window switches, shorter editing time, and higher acceptance](user-study-proactive-paradigms-preferred.md) — related
