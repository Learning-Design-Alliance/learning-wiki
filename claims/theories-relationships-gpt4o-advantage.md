---
type: claim
title: "GPT-4o outperformed the agent on Theories and Relationships Top1 accuracy and NDCG, the agent's weakest real-world category"
description: "GPT-4o outperformed the agent on Theories and Relationships Top1 accuracy and NDCG, the agent's weakest real-world category"
id: theories-relationships-gpt4o-advantage
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: zhang-2025
    resource: "https://doi.org/10.48550/arXiv.2502.06371"
    title: "Zhang, L., Zhang, M., Wang, W. L., & Luo, Y. (2025). Simulation as Reality? The Effectiveness of LLM-Generated Data in Open-ended Question Assessment. [doi:10.48550/arXiv.2502.06371](https://doi.org/10.48550/arXiv.2502.06371)"
    author: "Zhang, L., Zhang, M., Wang, W. L., & Luo, Y."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o outperformed the agent on Theories and Relationships Top1 accuracy and NDCG, the agent's weakest real-world category

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For Theories and Relationships questions GPT4o scored higher than the agent on Top1 accuracy (53.3% vs 40.0%) and NDCG (0.946 vs 0.932). [→ Zhang 2025](#zhang-2025)

## Evidence

### Zhang 2025

Zhang, L., Zhang, M., Wang, W. L., & Luo, Y. (2025). Simulation as Reality? The Effectiveness of LLM-Generated Data in Open-ended Question Assessment. [doi:10.48550/arXiv.2502.06371](https://doi.org/10.48550/arXiv.2502.06371)

`q2 · i?` · `design · r2`

Phase II ranking evaluation by question type. The article reports GPT4o "slightly outperforms our model in the NDCG metric" (0.946 vs 0.932) for Theories and Relationships; Table 2 also shows GPT4o ahead on Top1 accuracy there. No effect size printed.

> "Although GPT4o slightly outperforms our model in the NDCG metric for "Theories and Relationships" type questions (0.946 vs 0.932), our model still maintains a high level of performance, indicating that it remains competitive when addressing abstract theoretical relationships."

## Discussion


## Related Claims
- [On real student responses, the synthetic-data-trained agent outperformed GPT-4o on Top1 accuracy (44.2% vs 40.8%) and Top3 F1 (0.731 vs 0.706)](agent-outperforms-gpt4o-top1-top3.md) — related
- [The agent's largest Top1 advantage over GPT-4o appeared in the Applications and Rules question type (53.3% vs 43.3% accuracy)](applications-rules-top1-advantage.md) — related
- [On overall ranking, the agent achieved higher NDCG (0.920 vs 0.914) and MAP (0.660 vs 0.627) than GPT-4o, with its largest MAP gain on Phenomena and Effects questions](ranking-ndcg-map-advantage.md) — related
- [Agents trained exclusively on synthetic data perform well in simulated environments but show measurable gaps against human assessments in real-world settings](synthetic-real-performance-gap.md) — related
