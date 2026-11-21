---
type: claim
title: The automatic bug-description evaluation metric agrees strongly with human evaluators
description: The automatic bug-description evaluation metric agrees strongly with human evaluators
id: automatic-bug-description-metric-human-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhenlong-dai-2026
    resource: "https://doi.org/10.1609/aaai.v40i36.40300"
    title: "Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen. (2026). Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement. [doi:10.1609/aaai.v40i36.40300](https://doi.org/10.1609/aaai.v40i36.40300)"
    author: Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# The automatic bug-description evaluation metric agrees strongly with human evaluators

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i3` In a human study of 189 GPT-4o-generated samples (1,390 description pairs judged by two evaluators), the automatic metric matched human judgments in 67.72% of cases at sample level, 93.02% at point level, with Pearson correlation r = 0.848. [→ Zhenlong Dai 2026](#zhenlong-dai-2026)

## Evidence

### Zhenlong Dai 2026

Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen. (2026). Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement. [doi:10.1609/aaai.v40i36.40300](https://doi.org/10.1609/aaai.v40i36.40300)

`q2 · i3` · `design · r2`

Human study (RQ3, Table 4): two experienced evaluators independently judged 1,390 generated-versus-ground-truth description pairs from 189 GPT-4o samples, with disagreements resolved by discussion. The article reports "obtaining r= 0.848" between the automatic metric and human evaluation.

> "Then, we calculate the Pearson correlation coefficientr(Zhou et al. 2024), obtaining r= 0.848, which indicates a significant linear correlation between the automatic metric and the human evaluation."

## Discussion


## Related Claims
- [LLM-as-a-Judge scores correlate with blinded human expert judgments, more strongly for Medical Narrative Generation than Story Direction](llm-judge-correlates-human-experts-medgame.md) — related
- [Using AI to evaluate AI outputs was often challenging because AI act as yes people and humans struggled to agree on evaluation rubrics](ai-evaluating-ai-outputs-challenging.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [LSGEN outperforms program-repair baselines on LPR-Bench in code accuracy and bug-description F1](lsgen-outperforms-lpr-baselines.md) — related
