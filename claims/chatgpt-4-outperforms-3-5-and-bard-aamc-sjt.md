---
type: claim
title: ChatGPT-4.0 outperformed ChatGPT-3.5 and Bard on the AAMC SJT in both raw and adjusted accuracy
description: ChatGPT-4.0 outperformed ChatGPT-3.5 and Bard on the AAMC SJT in both raw and adjusted accuracy
id: chatgpt-4-outperforms-3-5-and-bard-aamc-sjt
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: cadiente-2024
    resource: "https://doi.org/10.21203/rs.3.rs-4560463/v1"
    title: "Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B. (2024). Large Language Models take on the AAMC Situational Judgment Test: Evaluating Dilemma-Based Scenarios. Research Square preprint. https://doi.org/10.21203/rs.3.rs-4560463/v1"
    author: "Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: cadiente-2024-2
    resource: "https://doi.org/10.21203/rs.3.rs-4560463/v1"
    title: "Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B. (2024). Large Language Models take on the AAMC Situational Judgment Test: Evaluating Dilemma-Based Scenarios. Research Square preprint. https://doi.org/10.21203/rs.3.rs-4560463/v1"
    author: "Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# ChatGPT-4.0 outperformed ChatGPT-3.5 and Bard on the AAMC SJT in both raw and adjusted accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ChatGPT-3.5 and Bard had significantly lower odds of raw accuracy than ChatGPT-4.0 (OR = 0.52 and OR = 0.42). [→ Cadiente 2024](#cadiente-2024)
`q2 i?` ChatGPT-3.5 and Bard also had significantly lower odds of being fully or partially correct than ChatGPT-4.0 (OR = 0.58 and OR = 0.48). [→ Cadiente 2024 (2)](#cadiente-2024-2)

## Evidence

### Cadiente 2024

Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B. (2024). Large Language Models take on the AAMC Situational Judgment Test: Evaluating Dilemma-Based Scenarios. Research Square preprint. https://doi.org/10.21203/rs.3.rs-4560463/v1

`q2 · i?` · `design · r2`

Logistic regression of raw accuracy across the three LLMs' responses to the 2021 AAMC SJT practice exam (186 solutions per model). The article reports "ChatGPT-3.5 and Bard had signi cantly lower odds of being accurate" than ChatGPT-4.0, with the printed ORs and CIs.

> "ChatGPT-3.5 and Bard had signi cantly lower odds of being accurate (using raw scores) compared to ChatGPT-4.0 (ChatGPT3.5 OR = 0.52, 95% CI [0.34,0.78], p = 0.002; Bard OR = 0.42, 95%CI [0.28,0.64], p < 0.001, Table I.)"

### Cadiente 2024 (2)

Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B. (2024). Large Language Models take on the AAMC Situational Judgment Test: Evaluating Dilemma-Based Scenarios. Research Square preprint. https://doi.org/10.21203/rs.3.rs-4560463/v1

`q2 · i?` · `associational · r1`

Ordinal logistic regression of adjusted accuracy (full or partial credit) on the same 186-solution exam. The article reports significantly lower odds for ChatGPT-3.5 and Bard "compared to ChatGPT-4.0" with the printed ORs and CIs.

> "ChatGPT-3.5 and Bard had signi cantly lower odds of being fully correct or partially correct compared to ChatGPT-4.0 (ChatGPT-3.5 OR = 0.58, 95% CI [0.39,0.85], p = 0.006; Bard OR = 0.48, 95% CI [0.33,0.72], p < 0.001, Table III.)"

## Discussion


## Related Claims
- [Bard unexpectedly cited references including the 2021 AAMC SJT practice exam booklet, suggesting potential use as a reference manager despite its inaccuracy](bard-citation-behavior-reference-manager-potential.md) — related
- [The three LLMs showed fair inter-model agreement on the AAMC SJT, agreeing most strongly on incorrect answers](llm-fair-agreement-same-errors-aamc-sjt.md) — related
- [Solution sentiment showed no meaningful individual relationship with LLM accuracy despite a small statistically significant collective trend](sentiment-no-meaningful-relationship-llm-sjt-accuracy.md) — related
- [Increased solution count correlated with decreased LLM accuracy, falling short of statistical significance except at solution count 5](solution-count-decreased-accuracy-not-significant.md) — related
- [No significant difference in accuracy between ChatGPT 3.5 and Bard 1.0 generated MCQs](chatgpt-35-bard-accuracy-no-difference.md) — related
