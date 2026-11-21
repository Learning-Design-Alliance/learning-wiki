---
type: claim
title: On overall ranking, the agent achieved higher NDCG (0.920 vs 0.914) and MAP (0.660 vs 0.627) than GPT-4o, with its largest MAP gain on Phenomena and Effects questions
description: On overall ranking, the agent achieved higher NDCG (0.920 vs 0.914) and MAP (0.660 vs 0.627) than GPT-4o, with its largest MAP gain on Phenomena and Effects questions
id: ranking-ndcg-map-advantage
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
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
  - id: zhang-2025-2
    resource: "https://doi.org/10.48550/arXiv.2502.06371"
    title: "Zhang, L., Zhang, M., Wang, W. L., & Luo, Y. (2025). Simulation as Reality? The Effectiveness of LLM-Generated Data in Open-ended Question Assessment. [doi:10.48550/arXiv.2502.06371](https://doi.org/10.48550/arXiv.2502.06371)"
    author: "Zhang, L., Zhang, M., Wang, W. L., & Luo, Y."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# On overall ranking, the agent achieved higher NDCG (0.920 vs 0.914) and MAP (0.660 vs 0.627) than GPT-4o, with its largest MAP gain on Phenomena and Effects questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The agent beat GPT4o on overall ranking quality (NDCG 0.920 vs 0.914; MAP 0.660 vs 0.627). [→ Zhang 2025](#zhang-2025)
`q2 i?` For Phenomena and Effects questions the agent's MAP of 0.631 exceeded GPT4o's 0.514. [→ Zhang 2025 (2)](#zhang-2025-2)

## Evidence

### Zhang 2025

Zhang, L., Zhang, M., Wang, W. L., & Luo, Y. (2025). Simulation as Reality? The Effectiveness of LLM-Generated Data in Open-ended Question Assessment. [doi:10.48550/arXiv.2502.06371](https://doi.org/10.48550/arXiv.2502.06371)

`q2 · i?` · `design · r2`

Phase II overall ranking task comparing the agent with GPT4o against teacher-derived rankings of student responses. The agent "achieves better results on two key metrics, NDCG and MAP"; no effect size printed.

> "From a general performance perspective, our model achieves better results on two key metrics, NDCG and MAP (NDCG: 0.920 vs 0.914, MAP: 0.660 vs 0.627), indicating that our model excels in both ranking quality and retrieval accuracy."

### Zhang 2025 (2)

Zhang, L., Zhang, M., Wang, W. L., & Luo, Y. (2025). Simulation as Reality? The Effectiveness of LLM-Generated Data in Open-ended Question Assessment. [doi:10.48550/arXiv.2502.06371](https://doi.org/10.48550/arXiv.2502.06371)

`q2 · i?` · `causal · r1`

Phase II category-level ranking result for Phenomena and Effects questions, where the agent's MAP was 0.631 versus GPT4o's 0.514; no effect size printed.

> "The notable improvement in the MAP metric (0.631 vs 0.514) suggests that the model exhibits better judgment ability when dealing with complex phenomenon explanations."

## Discussion


## Related Claims
- [On real student responses, the synthetic-data-trained agent outperformed GPT-4o on Top1 accuracy (44.2% vs 40.8%) and Top3 F1 (0.731 vs 0.706)](agent-outperforms-gpt4o-top1-top3.md) — related
- [The agent's largest Top1 advantage over GPT-4o appeared in the Applications and Rules question type (53.3% vs 43.3% accuracy)](applications-rules-top1-advantage.md) — related
- [GPT-4o outperformed the agent on Theories and Relationships Top1 accuracy and NDCG, the agent's weakest real-world category](theories-relationships-gpt4o-advantage.md) — related
