---
type: claim
title: "On real student responses, the synthetic-data-trained agent outperformed GPT-4o on Top1 accuracy (44.2% vs 40.8%) and Top3 F1 (0.731 vs 0.706)"
description: "On real student responses, the synthetic-data-trained agent outperformed GPT-4o on Top1 accuracy (44.2% vs 40.8%) and Top3 F1 (0.731 vs 0.706)"
id: agent-outperforms-gpt4o-top1-top3
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
    kind: design
    rigour: 2
---

# On real student responses, the synthetic-data-trained agent outperformed GPT-4o on Top1 accuracy (44.2% vs 40.8%) and Top3 F1 (0.731 vs 0.706)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the real-world Top1 task the agent's overall accuracy of 44.2% exceeded GPT4o's 40.8%. [→ Zhang 2025](#zhang-2025)
`q2 i?` In the Top3 task the agent's overall F1 of 0.731 surpassed GPT4o's 0.706, with precision and recall both 0.731. [→ Zhang 2025 (2)](#zhang-2025-2)

## Evidence

### Zhang 2025

Zhang, L., Zhang, M., Wang, W. L., & Luo, Y. (2025). Simulation as Reality? The Effectiveness of LLM-Generated Data in Open-ended Question Assessment. [doi:10.48550/arXiv.2502.06371](https://doi.org/10.48550/arXiv.2502.06371)

`q2 · i?` · `design · r2`

Phase II evaluation of the agent against GPT4o on 60 university students' answers to a 10-question open-ended science exam, ranked by three independent science teachers. The agent showed "an overall accuracy of 44.2%" versus 40.8%; no effect size printed.

> "In the Top1 task, which assesses the accuracy of predicting the best option, our model achieves an overall accuracy of 44.2%, significantly outperforming GPT4o's 40.8%."

### Zhang 2025 (2)

Zhang, L., Zhang, M., Wang, W. L., & Luo, Y. (2025). Simulation as Reality? The Effectiveness of LLM-Generated Data in Open-ended Question Assessment. [doi:10.48550/arXiv.2502.06371](https://doi.org/10.48550/arXiv.2502.06371)

`q2 · i?` · `design · r2`

Same Phase II comparison, Top3 binary classification of responses as within or outside the top three. The agent's "overall F1 score reaches 0.731" with balanced precision and recall; no effect size printed.

> "The overall F1 score reaches 0.731, surpassing GPT4o's 0.706, indicating that our model is more accurate in identifying high-quality options."

## Discussion


## Related Claims
- [GPT-4o outperformed the agent on Theories and Relationships Top1 accuracy and NDCG, the agent's weakest real-world category](theories-relationships-gpt4o-advantage.md) — related
- [The agent's largest Top1 advantage over GPT-4o appeared in the Applications and Rules question type (53.3% vs 43.3% accuracy)](applications-rules-top1-advantage.md) — a narrower finding that bears on this claim
- [On overall ranking, the agent achieved higher NDCG (0.920 vs 0.914) and MAP (0.660 vs 0.627) than GPT-4o, with its largest MAP gain on Phenomena and Effects questions](ranking-ndcg-map-advantage.md) — related
- [GPT-4o shows a clear advantage in complex question formats, exceeding 85% accuracy on case analysis (A3/A4) and matching (B1) questions](gpt4o-advantage-complex-question-formats.md) — related
