---
type: claim
title: Solution sentiment showed no meaningful individual relationship with LLM accuracy despite a small statistically significant collective trend
description: Solution sentiment showed no meaningful individual relationship with LLM accuracy despite a small statistically significant collective trend
id: sentiment-no-meaningful-relationship-llm-sjt-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: cadiente-2024
    resource: "https://doi.org/10.21203/rs.3.rs-4560463/v1"
    title: "Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B. (2024). Large Language Models take on the AAMC Situational Judgment Test: Evaluating Dilemma-Based Scenarios. Research Square preprint. https://doi.org/10.21203/rs.3.rs-4560463/v1"
    author: "Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: cadiente-2024-2
    resource: "https://doi.org/10.21203/rs.3.rs-4560463/v1"
    title: "Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B. (2024). Large Language Models take on the AAMC Situational Judgment Test: Evaluating Dilemma-Based Scenarios. Research Square preprint. https://doi.org/10.21203/rs.3.rs-4560463/v1"
    author: "Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Solution sentiment showed no meaningful individual relationship with LLM accuracy despite a small statistically significant collective trend

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across all three platforms, increased sentiment was associated with a statistically significant but negligible increase in odds of raw accuracy (OR = 1.00, 95% CI [1.00,1.01]). [→ Cadiente 2024](#cadiente-2024)
`q2 i?` For adjusted accuracy, the sentiment trend fell short of significance (p = 0.0537). [→ Cadiente 2024 (2)](#cadiente-2024-2)

## Evidence

### Cadiente 2024

Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B. (2024). Large Language Models take on the AAMC Situational Judgment Test: Evaluating Dilemma-Based Scenarios. Research Square preprint. https://doi.org/10.21203/rs.3.rs-4560463/v1

`q2 · i?` · `associational · r2`

Exploratory multivariable logistic regression of raw accuracy on MonkeyLearn sentiment scores across all three LLMs' 558 solution ratings. The article reports the significant collective trend with OR = 1.00 and p = 0.028, shown in Fig. 1.

> "As sentiment increased across all three platforms, there was a signi cant increase in the odds of being correct (using raw scores) (OR = 1.00, 95%CI [1.00,1.01], p = 0.028, Fig. 1)."

### Cadiente 2024 (2)

Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B. (2024). Large Language Models take on the AAMC Situational Judgment Test: Evaluating Dilemma-Based Scenarios. Research Square preprint. https://doi.org/10.21203/rs.3.rs-4560463/v1

`q2 · i?` · `design · r2`

Ordinal logistic regression of adjusted accuracy on sentiment across the three LLMs. The article reports only a non-significant trend (p = 0.0537); no individual LLM-by-sentiment interaction was significant.

> "As sentiment analysis increased, there was a trend towards increased odds of being correct (using adjusted scores) (OR = 1.00, 95% CI [1.00, 1.01], p = 0.0537)."

## Discussion


## Related Claims
- [ChatGPT-4.0 outperformed ChatGPT-3.5 and Bard on the AAMC SJT in both raw and adjusted accuracy](chatgpt-4-outperforms-3-5-and-bard-aamc-sjt.md) — related
- [The three LLMs showed fair inter-model agreement on the AAMC SJT, agreeing most strongly on incorrect answers](llm-fair-agreement-same-errors-aamc-sjt.md) — related
- [LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise](llm-feedback-sentiment-tracks-scores.md) — related
