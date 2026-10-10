---
type: claim
title: Learner-side gains from curiosity modulation persist even when tutor-side instructional quality remains unchanged or degrades, suggesting curiosity operates as a partially independent interaction-level mechanism
description: Learner-side gains from curiosity modulation persist even when tutor-side instructional quality remains unchanged or degrades, suggesting curiosity operates as a partially independent interaction-level mechanism
id: learner-gains-persist-despite-tutor-quality-degradation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: ganganath-2026
    resource: "https://arxiv.org/abs/2606.22349"
    title: "Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T. (2026). Curiosity as Linguistic Intervention: Using LLM Tutoring Dialogues to Influence Exploratory Learning Behavior. https://arxiv.org/abs/2606.22349"
    author: "Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: ganganath-2026-2
    resource: "https://arxiv.org/abs/2606.22349"
    title: "Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T. (2026). Curiosity as Linguistic Intervention: Using LLM Tutoring Dialogues to Influence Exploratory Learning Behavior. https://arxiv.org/abs/2606.22349"
    author: "Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Learner-side gains from curiosity modulation persist even when tutor-side instructional quality remains unchanged or degrades, suggesting curiosity operates as a partially independent interaction-level mechanism

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` The dissociation between learner-side and tutor-side outcomes is most visible in the Gemini condition, where learner curiosity and conversational agency improve significantly while instructional quality and cognitive load management degrade. [→ Ganganath 2026](#ganganath-2026)
`q2 i?` Pearson correlations between learner-side and tutor-side dimensions weaken consistently across nearly all interaction pairs under CURIOBOT compared to Baseline. [→ Ganganath 2026 (2)](#ganganath-2026-2)

## Evidence

### Ganganath 2026

Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T. (2026). Curiosity as Linguistic Intervention: Using LLM Tutoring Dialogues to Influence Exploratory Learning Behavior. https://arxiv.org/abs/2606.22349

`q2 · i?` · `causal · r2`

Dissociation analysis (§5.3) drawing on the Table 3 dimension-wise scores. In the Gemini condition, learner-side dimensions improve significantly while tutor-side instructional quality (T1) and cognitive load management (T3) decrease significantly; only p-values printed, no effect sizes.

> "From Table 3, we can see that the dissociation between learner-side and tutor-side outcomes is most visible in the Gemini results."

### Ganganath 2026 (2)

Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T. (2026). Curiosity as Linguistic Intervention: Using LLM Tutoring Dialogues to Influence Exploratory Learning Behavior. https://arxiv.org/abs/2606.22349

`q2 · i?` · `causal · r2`

Decoupling analysis (§5.3) using Pearson correlations between learner-side and tutor-side evaluation dimensions under Baseline and CURIOBOT (Figure 5). Correlation values are printed in the figure but no inferential tests on the difference are reported.

> "Under CURIOBOT, correlations between learner-side and tutor-side dimensions weaken consistently across nearly all interaction pairs"

## Discussion


## Related Claims
- [Curiosity-oriented linguistic interventions via CURIOBOT consistently improve all learner-side exploratory dimensions relative to baseline LLM tutoring across model families](curiosity-interventions-increase-exploratory-learner-behaviors.md) — related
- [Curiosity-modulated tutoring produces roughly 2.4× more conversational turns than baseline under fixed time budgets](curiosity-modulation-increases-conversational-turns.md) — related
- [Interactive dialogue with the AI tool, available only in some sites, promoted deeper engagement and student agency during revision](interactive-genai-dialogue-promotes-engagement.md) — related
- [Learner-side gains from curiosity modulation generalize across model families, academic domains, and topic complexity levels](curiosity-gains-generalize-across-models-domains-complexity.md) — related
- [Users alter expectations and behavior based on perceived AI capabilities even when actual AI performance is unchanged (the placebo effect of AI)](placebo-effect-of-ai-perceived-capabilities.md) — related
- [Curiosity gains depend on operator sequencing: how operators are ordered across turns, not only which operator is applied, shapes curiosity induction](operator-sequencing-affects-curiosity-gains.md) — related
- [Commercially optimized study-oriented modes achieve higher learner-side scores than baseline, and CURIOBOT shifts general-purpose LLM behavior toward those patterns via prompting alone](study-oriented-modes-upper-bound-reference.md) — related
- [Family-side evidence on GenAI guidance is thin, largely descriptive, and centered on parental beliefs and mediation strategies](family-side-parental-mediation-genai.md) — related
