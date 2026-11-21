---
type: claim
title: Few-shot prompting substantially improves Talk Move classification for some models (Claude 4.5 Opus κ 0.48→0.58; Gemini 2.5 Pro 0.38→0.57) but yields minimal gains for GPT-5 and o3
description: Few-shot prompting substantially improves Talk Move classification for some models (Claude 4.5 Opus κ 0.48→0.58; Gemini 2.5 Pro 0.38→0.57) but yields minimal gains for GPT-5 and o3
id: few-shot-prompting-gains-heterogeneous-llm
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: kirk-vanacore-and-rené-f-kizilcec-2026
    resource: "https://doi.org/10.1145/3774398.3811605"
    title: "Kirk Vanacore and René F. Kizilcec. (2026). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. Originally published 2025. [doi:10.1145/3774398.3811605](https://doi.org/10.1145/3774398.3811605)"
    author: Kirk Vanacore and René F. Kizilcec
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: kirk-vanacore-and-rené-f-kizilcec-2026-2
    resource: "https://doi.org/10.1145/3774398.3811605"
    title: "Kirk Vanacore and René F. Kizilcec. (2026). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. Originally published 2025. [doi:10.1145/3774398.3811605](https://doi.org/10.1145/3774398.3811605)"
    author: Kirk Vanacore and René F. Kizilcec
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Few-shot prompting substantially improves Talk Move classification for some models (Claude 4.5 Opus κ 0.48→0.58; Gemini 2.5 Pro 0.38→0.57) but yields minimal gains for GPT-5 and o3

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Claude 4.5 Opus and Gemini 2.5 Pro showed large κ gains from zero-shot to few-shot (all examples) prompting, indicating latent capacity unlocked by extensive examples. [→ Kirk Vanacore and René F. Kizilcec 2026](#kirk-vanacore-and-rene-f-kizilcec-2026)
`q2 i?` GPT-5 and o3 showed minimal sensitivity to prompting strategy, maintaining relatively stable performance across conditions. [→ Kirk Vanacore and René F. Kizilcec 2026 (2)](#kirk-vanacore-and-rene-f-kizilcec-2026-2)

## Evidence

### Kirk Vanacore and René F. Kizilcec 2026

Kirk Vanacore and René F. Kizilcec. (2026). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. Originally published 2025. [doi:10.1145/3774398.3811605](https://doi.org/10.1145/3774398.3811605)

`q2 · i?` · `causal · r2`

Prompting-strategy comparison in the results section of the benchmark experiment. The article reports this κ gain for Claude 4.5 Opus and adds that Gemini 2.5 Pro improved from 0.38 to 0.57; no standardized effect size is printed.

> "Claude 4.5 Opus demonstrated the most profound improvement, rising from a baseline κ of 0.48 (Zero Shot) to 0.58 in the Few Shot (All Examples) condition."

### Kirk Vanacore and René F. Kizilcec 2026 (2)

Kirk Vanacore and René F. Kizilcec. (2026). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. Originally published 2025. [doi:10.1145/3774398.3811605](https://doi.org/10.1145/3774398.3811605)

`q2 · i?` · `causal · r2`

Same results-section comparison of prompting strategies across the six models. The article reports that GPT-5 and o3 were minimally sensitive to prompting strategies, making the prompting benefit non-uniform; no standardized effect size is printed.

> "In contrast, GPT-5 and o3 showed minimal sensitivity to prompting strategies, maintaining relatively stable performance across conditions."

## Discussion


## Related Claims
- [Unadjusted foundation models achieve only moderate agreement (Cohen's κ = 0.38–0.58) with expert annotations when classifying instructional moves in authentic classroom transcripts](llm-baseline-moderate-kappa-talk-moves.md) — a broader claim this one bears on
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
- [Reasoning-based misclassification detection is robust across LLM annotators but detectability varies by source model, with errors from o3 and GPT-5 easiest to detect and Claude 4.5 Sonnet errors hardest](verification-signal-varies-by-source-llm.md) — related
