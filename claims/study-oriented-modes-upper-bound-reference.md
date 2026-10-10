---
type: claim
title: Commercially optimized study-oriented modes achieve higher learner-side scores than baseline, and CURIOBOT shifts general-purpose LLM behavior toward those patterns via prompting alone
description: Commercially optimized study-oriented modes achieve higher learner-side scores than baseline, and CURIOBOT shifts general-purpose LLM behavior toward those patterns via prompting alone
id: study-oriented-modes-upper-bound-reference
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: ganganath-2026
    resource: "https://arxiv.org/abs/2606.22349"
    title: "Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T. (2026). Curiosity as Linguistic Intervention: Using LLM Tutoring Dialogues to Influence Exploratory Learning Behavior. https://arxiv.org/abs/2606.22349"
    author: "Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Commercially optimized study-oriented modes achieve higher learner-side scores than baseline, and CURIOBOT shifts general-purpose LLM behavior toward those patterns via prompting alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Study-oriented modes consistently achieve higher learner-side scores than Baseline across Gemini and Claude, and CURIOBOT, relying solely on inference-time prompting, shifts learner-side behavior toward the patterns observed in these commercially optimized systems on L1–L4. [→ Ganganath 2026](#ganganath-2026)

## Evidence

### Ganganath 2026

Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T. (2026). Curiosity as Linguistic Intervention: Using LLM Tutoring Dialogues to Influence Exploratory Learning Behavior. https://arxiv.org/abs/2606.22349

`q2 · i?` · `causal · r2`

Approximate upper-bound reference analysis (§5.4, Appendix J Table 16). GPT is excluded since OpenAI does not provide a study-oriented mode; these modes were not treated as formal experimental baselines because they expose no API-level controllable prompting.

> "study-oriented modes consistently achieve higher learner-side scores than Baseline across Gemini and Claude"

## Discussion


## Related Claims
- [Curiosity-oriented linguistic interventions via CURIOBOT consistently improve all learner-side exploratory dimensions relative to baseline LLM tutoring across model families](curiosity-interventions-increase-exploratory-learner-behaviors.md) — related
- [Learner-side gains from curiosity modulation persist even when tutor-side instructional quality remains unchanged or degrades, suggesting curiosity operates as a partially independent interaction-level mechanism](learner-gains-persist-despite-tutor-quality-degradation.md) — related
- [Learner-side gains from curiosity modulation generalize across model families, academic domains, and topic complexity levels](curiosity-gains-generalize-across-models-domains-complexity.md) — related
