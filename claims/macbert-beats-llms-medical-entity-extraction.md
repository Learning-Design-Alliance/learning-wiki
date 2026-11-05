---
type: claim
title: Fine-tuned MacBERT outperformed fine-tuned LLMs on medical entity extraction while requiring far fewer computational resources
description: Fine-tuned MacBERT outperformed fine-tuned LLMs on medical entity extraction while requiring far fewer computational resources
id: macbert-beats-llms-medical-entity-extraction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: pang-xiao-2026
    resource: "https://doi.org/10.2196/83785"
    title: "Pang Xiao, Liu Chang, Huang Yan, Liu MingYou, Liu Jiyuan. (2026). An Entity-Based Visual Analytics System Enhancing Medical Expertise Acquisition: Development and Verification Study. JMIR Medical Informatics. https://doi.org/10.2196/83785"
    author: Pang Xiao, Liu Chang, Huang Yan, Liu MingYou, Liu Jiyuan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned MacBERT outperformed fine-tuned LLMs on medical entity extraction while requiring far fewer computational resources

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a comparative model evaluation, the fine-tuned MacBERT model achieved the highest F1-score (0.605), surpassing fine-tuned DeepSeek-70B (0.535) and Qwen-32B (0.561), with much lower fine-tuning and inference times. [→ Pang Xiao 2026](#pang-xiao-2026)

## Evidence

### Pang Xiao 2026

Pang Xiao, Liu Chang, Huang Yan, Liu MingYou, Liu Jiyuan. (2026). An Entity-Based Visual Analytics System Enhancing Medical Expertise Acquisition: Development and Verification Study. JMIR Medical Informatics. https://doi.org/10.2196/83785

`q2 · i?` · `design · r2`

Comparative benchmark evaluation of DeepSeek-70B, Qwen-32B, and MacBERT on medical entity extraction; Table 2 reports F1-scores of 0.535, 0.561, and 0.605 after fine-tuning, and Table 1 shows MacBERT fine-tuning took 0.77 hours on 2 A10 GPUs versus 167.23 and 101.46 hours for the LLMs.

> "the fine-tuned MacBERT model achieves the highest F1-score (0.605), surpassing both LLMs, and its precision approaches human annotation levels [41]."

## Discussion


## Related Claims
- [LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance](llms-more-stable-cross-dataset-than-supervised.md) — related
- [DeepSeek-MoE (Ours) achieves the strongest overall balance of accuracy among tested configurations, reaching 78.6% overall and 81.2% multi-hop reasoning accuracy on a 300-query OER evaluation set](deepseek-moe-ours-strongest-accuracy-balance.md) — related
