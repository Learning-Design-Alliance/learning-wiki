---
type: claim
title: Score-based prompting outperforms standard prompting on feedback accuracy, relevance, and helpfulness across all rubrics
description: Score-based prompting outperforms standard prompting on feedback accuracy, relevance, and helpfulness across all rubrics
id: score-based-prompting-outperforms-standard-quality
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: jieun-han-2024
    resource: "https://doi.org/10.18653/v1/2024.customnlp4u-1.21"
    title: "Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh. (2024). LLM-as-a-tutor in EFL Writing Education: Focusing on Evaluation of Student-LLM Interaction. arXiv. Originally published 2023. [doi:10.18653/v1/2024.customnlp4u-1.21](https://doi.org/10.18653/v1/2024.customnlp4u-1.21)"
    author: Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Score-based prompting outperforms standard prompting on feedback accuracy, relevance, and helpfulness across all rubrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Expert evaluation shows score-based prompting feedback is rated significantly higher than standard prompting on accuracy, relevance, and helpfulness across all rubrics, with statistically significant differences (paired T-test, p < 0.05). [→ Jieun Han 2024](#jieun-han-2024)

## Evidence

### Jieun Han 2024

Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh. (2024). LLM-as-a-tutor in EFL Writing Education: Focusing on Evaluation of Student-LLM Interaction. arXiv. Originally published 2023. [doi:10.18653/v1/2024.customnlp4u-1.21](https://doi.org/10.18653/v1/2024.customnlp4u-1.21)

`q2 · i?` · `causal · r2`

Expert evaluation of feedback quality (Figure 1, top row) compared standard and score-based prompting across content, organization, and language rubrics on 7-point Likert scales, tested with paired T-tests. Score-based prompting achieved "statistical sig- nificance across all rubrics" on accuracy, relevance, and helpfulness; standard prompting's level of detail varied (4.16–5.28) while score-based stayed consistent (4.48–4.86).

> "Score-based prompting outper- forms standard prompting in terms of accuracy, relevance, and helpfulness, achieving statistical sig- nificance across all rubrics."

## Discussion


## Related Claims
- [Score-based prompting generates more negative, straightforward, direct, and extensive feedback, and experts prefer it](score-based-prompting-feedback-characteristics-preference.md) — related
- [Three education experts rate PsyScore feedback significantly higher than all LLM baselines on every dimension (p < .001), with the No-IRT ablation declining in Adaptivity and Accuracy (p < .05)](psyscore-expert-evaluation-outperforms-baselines.md) — related
- [Artifact-grounded agent responses are rated significantly higher than transcript-only responses on groundedness, analytical depth, helpfulness, relevance, and overall quality](artifact-grounded-responses-rated-higher.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Few-shot with chain-of-thought prompting achieves the best concordance with human expert ratings for all tested LLMs](few-shot-cot-best-concordance-human-experts.md) — related
