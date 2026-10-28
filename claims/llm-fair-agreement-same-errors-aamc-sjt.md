---
type: claim
title: The three LLMs showed fair inter-model agreement on the AAMC SJT, agreeing most strongly on incorrect answers
description: The three LLMs showed fair inter-model agreement on the AAMC SJT, agreeing most strongly on incorrect answers
id: llm-fair-agreement-same-errors-aamc-sjt
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
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
    kind: design
    rigour: 2
---

# The three LLMs showed fair inter-model agreement on the AAMC SJT, agreeing most strongly on incorrect answers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Fleiss kappa indicated fair agreement among the three LLMs on raw accuracy (0.29) and adjusted accuracy (0.36). [→ Cadiente 2024](#cadiente-2024)
`q2 i?` Agreement was moderate for incorrect answers on adjusted accuracy (Fleiss kappa = 0.53), implying the models best agree when repeating the same errors. [→ Cadiente 2024 (2)](#cadiente-2024-2)

## Evidence

### Cadiente 2024

Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B. (2024). Large Language Models take on the AAMC Situational Judgment Test: Evaluating Dilemma-Based Scenarios. Research Square preprint. https://doi.org/10.21203/rs.3.rs-4560463/v1

`q2 · i?` · `design · r2`

Fleiss Kappa computed across ChatGPT-3.5, ChatGPT-4.0, and Bard ratings of the 186 exam solutions, for both raw and adjusted accuracy. The article reports fair agreement for both metrics with the printed kappa values.

> "There was fair agreement among the three LLMs on raw accuracy (Fleiss kappa = 0.29; p < 0.001). There was fair agreement among the three LLMs on adjusted accuracy (Fleiss kappa = 0.36; p < 0.001)."

### Cadiente 2024 (2)

Cadiente, A., Chen, J., Kasselman, L., & Pilkington, B. (2024). Large Language Models take on the AAMC Situational Judgment Test: Evaluating Dilemma-Based Scenarios. Research Square preprint. https://doi.org/10.21203/rs.3.rs-4560463/v1

`q2 · i?` · `design · r2`

Fleiss Kappa restricted to incorrect answers under adjusted scoring. The article interprets this as the models tending towards making the same inaccuracies, and warns users to beware of complex social situations where all three LLMs made similar mistakes.

> "For adjusted accuracy, moderate agreement was perceived among the three LLMs on incorrect answers (Fleiss kappa = 0.53, p < 0.001)."

## Discussion


## Related Claims
- [ChatGPT-4.0 outperformed ChatGPT-3.5 and Bard on the AAMC SJT in both raw and adjusted accuracy](chatgpt-4-outperforms-3-5-and-bard-aamc-sjt.md) — related
- [Solution sentiment showed no meaningful individual relationship with LLM accuracy despite a small statistically significant collective trend](sentiment-no-meaningful-relationship-llm-sjt-accuracy.md) — related
