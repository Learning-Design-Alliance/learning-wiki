---
type: claim
title: Knowledge-aware Editing Distance correlates most strongly with human editing duration among evaluated metrics
description: Knowledge-aware Editing Distance correlates most strongly with human editing duration among evaluated metrics
id: ked-strongest-correlation-editing-duration
status: review
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
    i: 3
    kind: associational
    rigour: 1
---

# Knowledge-aware Editing Distance correlates most strongly with human editing duration among evaluated metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2` · `i3` large

## Subclaims
`q2 i3` KED achieves the highest Pearson (r = 0.686) and Spearman (rho = 0.786) correlations with observed editing duration, exceeding edit-distance and similarity baselines. [→ Youqing Fang 2026](#youqing-fang-2026)

## Evidence

### Youqing Fang 2026

Youqing Fang, Yinhao Tang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Bin Liu, Weiming Zhang, Kuikun Liu, Wenwei Zhang, Kai Chen. (2026). MindCopilot: Towards Formalizing and Evaluating Granular Human-LLM Co-Writing. arXiv preprint. https://arxiv.org/abs/2605.23535 [doi:10.48550/arxiv.2605.23535](https://doi.org/10.48550/arxiv.2605.23535)

`q2 · i3` · `associational · r1`

Correlational evaluation of KED using writing logs from the CoAuthor dataset, which records human revisions to AI-generated suggestions with timestamps, with editing duration as a behavioral proxy for cognitive effort. Table 2 prints KED's Pearson r = 0.686 and Spearman rho = 0.786, the highest among evaluated metrics including Levenshtein, ROUGE-L, BLEU, and BERTScore.

> "KED achieves the high- est Pearson and Spearman coefficients among all evaluated metrics, demonstrating both sensitivity to absolute editing ef- fort and consistency in ranking instances by difficulty. All reported correlations are statistically significant."

## Discussion


## Related Claims
- [Behavioral interaction metrics are weakly or inconsistently correlated with task performance in AI-assisted programming](interaction-metrics-weakly-correlated-task-performance.md) — related
