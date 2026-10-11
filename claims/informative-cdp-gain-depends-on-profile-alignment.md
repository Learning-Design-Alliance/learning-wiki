---
type: claim
title: "The further gain from informative CDP depends on profile-level alignment: where within-profile behavior is inaccurate, adding pattern prevalences brings little or negative gain"
description: "The further gain from informative CDP depends on profile-level alignment: where within-profile behavior is inaccurate, adding pattern prevalences brings little or negative gain"
id: informative-cdp-gain-depends-on-profile-alignment
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: wenjie-zhou-2026
    resource: "https://osf.io/p6fam/"
    title: "Wenjie Zhou, Yunting Liu, Renjiao Tang, & Mark Wilson. (2026). Aligning LLM-Simulated and Human Examinees for Psychometric Calibration: A Cognitive Diagnostic Profiling Approach. https://osf.io/p6fam/"
    author: "Wenjie Zhou, Yunting Liu, Renjiao Tang, & Mark Wilson"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The further gain from informative CDP depends on profile-level alignment: where within-profile behavior is inaccurate, adding pattern prevalences brings little or negative gain

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` DeepSeek V3.2 (Thinking) overshot the human expectation within profiles (weighted bias +2.78), so the informative prior amplified the overshoot and overlap fell from 0.84 to 0.71. [→ Wenjie Zhou 2026](#wenjie-zhou-2026)

## Evidence

### Wenjie Zhou 2026

Wenjie Zhou, Yunting Liu, Renjiao Tang, & Mark Wilson. (2026). Aligning LLM-Simulated and Human Examinees for Psychometric Calibration: A Cognitive Diagnostic Profiling Approach. https://osf.io/p6fam/

`q2 · i?` · `causal · r2`

Authors' interpretation, in the Discussion, of the DeepSeek V3.2 (Thinking) exception cell in the simulation study: the printed weighted bias of +2.78 and the overlap drop "from 0.84 to 0.71" illustrate the dependence of the C3 gain on profile-level fidelity.

> "DeepSeek V3.2 (Thinking) illustrates this: its examinees overshot the human expectation within profiles (weighted bias +2.78), so a prior concentrating a third of the pool at full mastery amplified the overshoot, and overlap fell from 0.84 to 0.71."

## Discussion


## Related Claims
- [Cognitive Diagnostic Profiling raises distribution-level overlap between simulated and human examinee ability distributions, with the informative condition highest for seven of eight configurations](cdp-improves-distribution-level-alignment.md) — related
- [CDP improves item-difficulty recovery in both rank order and absolute alignment, with the largest gains for reasoning-enabled Gemini configurations](cdp-improves-item-difficulty-recovery.md) — related
