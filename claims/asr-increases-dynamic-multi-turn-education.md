---
type: claim
title: LLM attack success rates increase consistently from single-turn to static multi-turn and dynamic multi-turn interactions in educational settings
description: LLM attack success rates increase consistently from single-turn to static multi-turn and dynamic multi-turn interactions in educational settings
id: asr-increases-dynamic-multi-turn-education
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

# LLM attack success rates increase consistently from single-turn to static multi-turn and dynamic multi-turn interactions in educational settings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across all evaluated models, ASR rises from 29.9% (single-turn) to 38.3% (static multi-turn) to 53.6% (dynamic multi-turn), with the dynamic setting nearly 1.8× the single-turn rate. [→ Park 2026](#park-2026)

## Evidence

### Park 2026

Park, J., Han, J., Yoo, H., Ahn, S.-Y., Yoon, J., & Oh, A. (2026). EduZone: A Framework for Evaluating LLM Safety for K-12 Students and Teachers. arXiv preprint. https://arxiv.org/abs/2608.02024

`q2 · i?` · `design · r2`

Evaluation of ten LLMs across three interaction settings in EduZone. Average ASR increases monotonically with interaction complexity, and "the gap between the best and worst models increases from 42.9 to 67.3 pp", better differentiating model robustness.

> "Across all models, ASR increases consistently from single-turn to static multi-turn and dynamic multi-turn interactions (29.9% < 38.3% < 53.6%), with the dynamic setting achieving nearly 1.8×the ASRofsingle-turnevaluation."

## Discussion


## Related Claims
- [Adaptive multi-turn interactions substantially amplify LLM vulnerabilities to conventional safety risks in educational contexts](dynamic-multi-turn-amplifies-conventional-risks.md) — related
- [Current LLMs are more vulnerable to education-specific risks such as academic misconduct and excessive cognitive load than to conventional safety risks in K-12 educational interactions](eduzone-education-specific-risk-vulnerability.md) — related
- [Risk category explains the largest share of variation in educational attack success, far more than LLM usage context or curriculum topic](risk-category-dominates-educational-safety-variance.md) — related
- [Taxonomy-augmented guardrail classifiers reduce educational attack success more than general-purpose jailbreak defenses](taxonomy-augmented-guardrails-education-specific-risks.md) — related
- [No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation](no-llm-tutor-reliably-safe-60-percent-harm.md) — related
