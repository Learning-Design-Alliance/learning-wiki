---
type: claim
title: GRPO pedagogical alignment of a reasoning LLM lowers actual student learning while raising judge-rated helpfulness (a multi-dimensional alignment tax)
description: GRPO pedagogical alignment of a reasoning LLM lowers actual student learning while raising judge-rated helpfulness (a multi-dimensional alignment tax)
id: grpo-pedagogical-alignment-tax-lowers-learning
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: alignment-tax-1
    title: alignment-tax-1
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# GRPO pedagogical alignment of a reasoning LLM lowers actual student learning while raising judge-rated helpfulness (a multi-dimensional alignment tax)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` GRPO alignment of DeepSeek-R1-8B drops Δ Solve Rate from +.180 to −.012, cuts thinking length by −93.3%, and reduces OpenLearnLM CK/PK accuracy by −71%/−80% relative, while judge-rated helpfulness rises from .220 to .416. [→ alignment-tax-1](#alignment-tax-1)

## Evidence

### alignment-tax-1

Shim Jaechang and Unggi Lee. 2026. The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals. In Proceedings of The 35th ACM International Conference on Information and Knowledge Management (CIKM '26). https://arxiv.org/abs/2605.30666

`q2 · i?` · `causal · r1`

Comparison of base vs. GRPO-aligned DeepSeek-R1-8B across in-domain tutoring scenarios and the OpenLearnLM OOD suite (Table 7): thinking length 1,764→119 words/turn, visible length 194→21, ΔSol −.192, helpful_rate +.196. No standardised effect size printed.

> "Pedagogical alignment cuts thinking length by an order of magnitude and visible length by nearly the same amount; the visible mathematical content density drops from25.5%to9 .5%; the student’s post-tutoring solve rate actually falls below the pre-tutoring rate (Δ=−. 012)."

## Discussion


## Related Claims
- [GRPO alignment collapses Mathematical-Knowledge-for-Teaching utterances and surges Socratic-style Exploratory questions in tutor output](alignment-shifts-mkt-collapse-exploratory-surge.md) — related
- [DTR (Deep-Thinking Ratio) does not predict tutoring quality despite predicting math accuracy](dtr-does-not-predict-tutoring-quality.md) — related
