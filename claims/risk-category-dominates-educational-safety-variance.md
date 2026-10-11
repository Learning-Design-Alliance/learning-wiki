---
type: claim
title: Risk category explains the largest share of variation in educational attack success, far more than LLM usage context or curriculum topic
description: Risk category explains the largest share of variation in educational attack success, far more than LLM usage context or curriculum topic
id: risk-category-dominates-educational-safety-variance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: park-2026
    resource: "https://arxiv.org/abs/2608.02024"
    title: "Park, J., Han, J., Yoo, H., Ahn, S.-Y., Yoon, J., & Oh, A. (2026). EduZone: A Framework for Evaluating LLM Safety for K-12 Students and Teachers. arXiv preprint. https://arxiv.org/abs/2608.02024"
    author: "Park, J., Han, J., Yoo, H., Ahn, S.-Y., Yoon, J., & Oh, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Risk category explains the largest share of variation in educational attack success, far more than LLM usage context or curriculum topic

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In a binomial GLM of conversation-level attack success, risk category accounts for 77.4% of explained deviance and interaction setting 22.9%, while usage context (7.7%) and curriculum topic (0.9%) contribute relatively little. [→ Park 2026](#park-2026)

## Evidence

### Park 2026

Park, J., Han, J., Yoo, H., Ahn, S.-Y., Yoon, J., & Oh, A. (2026). EduZone: A Framework for Evaluating LLM Safety for K-12 Students and Teachers. arXiv preprint. https://arxiv.org/abs/2608.02024

`q2 · i?` · `design · r2`

Binomial GLM fitted with conversation-level attack success as the binary outcome to identify main factors influencing educational safety. The authors focus subsequent analysis on risk category and interaction setting given the other factors' small shares.

> "Risk category accounts for the largest share of the explained deviance (77.4%), followed by interaction setting (22.9%)"

## Discussion


## Related Claims
- [LLM attack success rates increase consistently from single-turn to static multi-turn and dynamic multi-turn interactions in educational settings](asr-increases-dynamic-multi-turn-education.md) — related
- [Current LLMs are more vulnerable to education-specific risks such as academic misconduct and excessive cognitive load than to conventional safety risks in K-12 educational interactions](eduzone-education-specific-risk-vulnerability.md) — related
- [No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation](no-llm-tutor-reliably-safe-60-percent-harm.md) — related
