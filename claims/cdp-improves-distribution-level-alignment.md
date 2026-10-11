---
type: claim
title: Cognitive Diagnostic Profiling raises distribution-level overlap between simulated and human examinee ability distributions, with the informative condition highest for seven of eight configurations
description: Cognitive Diagnostic Profiling raises distribution-level overlap between simulated and human examinee ability distributions, with the informative condition highest for seven of eight configurations
id: cdp-improves-distribution-level-alignment
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

# Cognitive Diagnostic Profiling raises distribution-level overlap between simulated and human examinee ability distributions, with the informative condition highest for seven of eight configurations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Under the informative CDP condition, the overlapping coefficient with the human ability distribution was highest for seven of the eight LLM configurations, compared with the no-profile baseline. [→ Wenjie Zhou 2026](#wenjie-zhou-2026)

## Evidence

### Wenjie Zhou 2026

Wenjie Zhou, Yunting Liu, Renjiao Tang, & Mark Wilson. (2026). Aligning LLM-Simulated and Human Examinees for Psychometric Calibration: A Cognitive Diagnostic Profiling Approach. https://osf.io/p6fam/

`q2 · i?` · `causal · r2`

Simulation study comparing eight LLM configurations under three prompting conditions against 536 human examinees on the 15-item fraction-subtraction test. The informative condition "improved alignment further for seven of the eight configurations", with OVL for Gemini 3.1 Pro rising from 0.52 to 0.81. No effect size is printed.

> "The informative condition (C3) improved alignment further for seven of the eight configurations. OVL was highest under C3 (for Gemini 3.1 Pro it rose from 0.52 at C1 to 0.77 at C2 and 0.81 at C3; for Gemini 3.0 Flash (Thinking), from 0.36 to 0.81 to 083"

## Discussion


## Related Claims
- [The further gain from informative CDP depends on profile-level alignment: where within-profile behavior is inaccurate, adding pattern prevalences brings little or negative gain](informative-cdp-gain-depends-on-profile-alignment.md) — related
- [Without cognitive profiles, LLM-simulated response patterns collapse toward a single pattern; profile conditioning multiplies response-pattern diversity](profile-conditioning-increases-response-diversity.md) — related
