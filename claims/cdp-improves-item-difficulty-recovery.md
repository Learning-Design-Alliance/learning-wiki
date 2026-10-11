---
type: claim
title: CDP improves item-difficulty recovery in both rank order and absolute alignment, with the largest gains for reasoning-enabled Gemini configurations
description: CDP improves item-difficulty recovery in both rank order and absolute alignment, with the largest gains for reasoning-enabled Gemini configurations
id: cdp-improves-item-difficulty-recovery
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

# CDP improves item-difficulty recovery in both rank order and absolute alignment, with the largest gains for reasoning-enabled Gemini configurations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` The informative CDP condition lowered absolute bias and RMSE and raised Spearman correlations for item difficulty for most configurations, with Gemini 3.1 Pro (Thinking) reaching a 1PL difficulty RMSE of 0.73 under C3. [→ Wenjie Zhou 2026](#wenjie-zhou-2026)

## Evidence

### Wenjie Zhou 2026

Wenjie Zhou, Yunting Liu, Renjiao Tang, & Mark Wilson. (2026). Aligning LLM-Simulated and Human Examinees for Psychometric Calibration: A Cognitive Diagnostic Profiling Approach. https://osf.io/p6fam/

`q2 · i?` · `causal · r2`

Item-level recovery analysis of the simulation study across eight LLM configurations and three conditions, comparing CTT pass rates and 1PL difficulty parameters against human-data values. The printed statistics include a 1PL RMSE falling "from 1.40 to 0.73" for Gemini 3.1 Pro (Thinking).

> "C3 improved absolute alignment further for most configurations, lowering the absolute bias and RMSE and raising the Spearman correlation on both indices (for Gemini 3.1 Pro, the RMSE for the CTT pass rate fell from 0.22 at C2 to 0.09 at C3, and the bias in the 1PL difficulty parameter moved from +1.16 to −0.20, with its RMSE falling from 1.40 to 0.73)."

## Discussion


## Related Claims
- [Reasoning-enabled (thinking) configurations recover item difficulty better than their non-thinking counterparts, with the advantage clearest at the item level](thinking-mode-advantage-item-recovery.md) — related
- [LLM-generated difficulty ratings show only moderate rank alignment with empirical student performance on basic arithmetic items](llm-difficulty-moderate-rank-alignment-arithmetic.md) — related
- [The further gain from informative CDP depends on profile-level alignment: where within-profile behavior is inaccurate, adding pattern prevalences brings little or negative gain](informative-cdp-gain-depends-on-profile-alignment.md) — related
- [Frontier-model choice affects LecturaAgents performance, with Gemini 3 Pro ranking first at 80.4% AAR](lecturaagents-frontier-model-evaluation-aar.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — related
