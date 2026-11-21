---
type: claim
title: "The agent's largest Top1 advantage over GPT-4o appeared in the Applications and Rules question type (53.3% vs 43.3% accuracy)"
description: "The agent's largest Top1 advantage over GPT-4o appeared in the Applications and Rules question type (53.3% vs 43.3% accuracy)"
id: applications-rules-top1-advantage
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
---

# The agent's largest Top1 advantage over GPT-4o appeared in the Applications and Rules question type (53.3% vs 43.3% accuracy)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the Applications and Rules category the agent reached 53.3% Top1 accuracy versus GPT4o's 43.3%. [→ Zhang 2025](#zhang-2025)

## Evidence

### Zhang 2025

Zhang, L., Zhang, M., Wang, W. L., & Luo, Y. (2025). Simulation as Reality? The Effectiveness of LLM-Generated Data in Open-ended Question Assessment. [doi:10.48550/arXiv.2502.06371](https://doi.org/10.48550/arXiv.2502.06371)

`q2 · i?` · `design · r2`

Phase II category-level analysis on the four clustered question types. In the Applications and Rules set the agent's Top1 accuracy was "an accuracy of 53.3%" against GPT4o's 43.3%; no effect size printed.

> "Notably, in the "Applications and Rules" category, our model performs particularly well in the Top1 task, with an accuracy of 53.3%, far exceeding GPT4o's 43.3%, which demonstrates the model's advantage in practical application scenarios."

## Discussion


## Related Claims
- [On real student responses, the synthetic-data-trained agent outperformed GPT-4o on Top1 accuracy (44.2% vs 40.8%) and Top3 F1 (0.731 vs 0.706)](agent-outperforms-gpt4o-top1-top3.md) — a broader claim this one bears on
- [GPT-4o outperformed the agent on Theories and Relationships Top1 accuracy and NDCG, the agent's weakest real-world category](theories-relationships-gpt4o-advantage.md) — related
- [On overall ranking, the agent achieved higher NDCG (0.920 vs 0.914) and MAP (0.660 vs 0.627) than GPT-4o, with its largest MAP gain on Phenomena and Effects questions](ranking-ndcg-map-advantage.md) — related
