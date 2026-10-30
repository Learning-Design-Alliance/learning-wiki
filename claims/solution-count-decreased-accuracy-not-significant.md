---
type: claim
title: Increased solution count correlated with decreased LLM accuracy, falling short of statistical significance except at solution count 5
description: Increased solution count correlated with decreased LLM accuracy, falling short of statistical significance except at solution count 5
id: solution-count-decreased-accuracy-not-significant
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
---

# Increased solution count correlated with decreased LLM accuracy, falling short of statistical significance except at solution count 5

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For adjusted accuracy the decrease reached significance only at solution counts of 5 (OR = 3.95, 95% CI [1.11, 18.6], p = 0.048). [→ Cadiente 2024](#cadiente-2024)

## Evidence

### Cadiente 2024

Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B. (2024). Large Language Models take on the AAMC Situational Judgment Test: Evaluating Dilemma-Based Scenarios. Research Square preprint. https://doi.org/10.21203/rs.3.rs-4560463/v1

`q2 · i?` · `associational · r2`

Ordinal logistic regression of adjusted accuracy on solution count. Table III prints OR = 3.95 (95% CI 1.11, 18.6; p = 0.048) for solution count 5 versus 4; the authors caution the isolated value needs further study.

> "Likewise, across all 3 platforms summatively, as solution count increases, the odds of being accurate using adjusted scores also decreases with statistical signi cance only noted in solution counts of 5 (Table II)."

## Discussion


## Related Claims
- [ChatGPT-4.0 outperformed ChatGPT-3.5 and Bard on the AAMC SJT in both raw and adjusted accuracy](chatgpt-4-outperforms-3-5-and-bard-aamc-sjt.md) — related
- [LLM accuracy increases monotonically with prompt sophistication across semantically equivalent medical questions, with Low Literacy users scoring significantly below Prompt Engineer users](prompt-privilege-monotonic-accuracy-gap-medqa.md) — related
