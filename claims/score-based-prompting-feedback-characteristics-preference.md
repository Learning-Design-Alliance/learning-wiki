---
type: claim
title: Score-based prompting generates more negative, straightforward, direct, and extensive feedback, and experts prefer it
description: Score-based prompting generates more negative, straightforward, direct, and extensive feedback, and experts prefer it
id: score-based-prompting-feedback-characteristics-preference
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: jieun-han-2024
    resource: "https://doi.org/10.18653/v1/2024.customnlp4u-1.21"
    title: "Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh. (2024). LLM-as-a-tutor in EFL Writing Education: Focusing on Evaluation of Student-LLM Interaction. arXiv. Originally published 2023. [doi:10.18653/v1/2024.customnlp4u-1.21](https://doi.org/10.18653/v1/2024.customnlp4u-1.21)"
    author: Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Score-based prompting generates more negative, straightforward, direct, and extensive feedback, and experts prefer it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Score-based prompting produces more negative, straightforward, direct, and extensive feedback than standard prompting across all rubrics, and 74.38% of teacher annotators prefer it versus 12.50% favoring standard prompting (Chi-squared test, p < 0.05, Fleiss Kappa 0.22). [→ Jieun Han 2024](#jieun-han-2024)

## Evidence

### Jieun Han 2024

Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh. (2024). LLM-as-a-tutor in EFL Writing Education: Focusing on Evaluation of Student-LLM Interaction. arXiv. Originally published 2023. [doi:10.18653/v1/2024.customnlp4u-1.21](https://doi.org/10.18653/v1/2024.customnlp4u-1.21)

`q2 · i?` · `causal · r1`

Expert annotation of feedback characteristics (Figure 1, lower section) on five dimensions showed score-based prompting more negative, straightforward, direct, and extensive across all rubrics. Its feedback was more concise (70.46 vs. 79.19 tokens; 4.20 vs. 5.04 sentences). Annotator preference was statistically significant at p < 0.05 (Chi-squared test) with fair agreement (Fleiss Kappa 0.22); 13.12% reported no difference.

> "As a result, 74.38% of teacher annotators prefer feedback from score-based prompting, compared to only 12.50% who favor feedback from standard prompting"

## Discussion


## Related Claims
- [Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive](llm-logical-inconsistency-scoring-feedback.md) — related
- [Different LLMs rely on different subsets of rubric traits when assigning essay scores](llms-weight-rubric-traits-differently.md) — related
- [Score-based prompting outperforms standard prompting on feedback accuracy, relevance, and helpfulness across all rubrics](score-based-prompting-outperforms-standard-quality.md) — related
- [gpt-3.5-turbo with standard prompting generates overly positive, indirect, and unhelpful essay feedback for EFL writing](gpt35-standard-prompting-overly-positive-feedback.md) — related
