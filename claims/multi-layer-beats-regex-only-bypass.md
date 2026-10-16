---
type: claim
title: "Multi-layer defense significantly reduces bypass relative to regex-only filtering (69.65% to 46.34%), confirmed by exact McNemar test"
description: "Multi-layer defense significantly reduces bypass relative to regex-only filtering (69.65% to 46.34%), confirmed by exact McNemar test"
id: multi-layer-beats-regex-only-bypass
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: alexandre-cristovão-maiorano-2026
    resource: "https://doi.org/10.48550/arxiv.2605.06669"
    title: "Alexandre Cristovão Maiorano. (2026). Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs. https://arxiv.org/abs/2605.06669 [doi:10.48550/arxiv.2605.06669](https://doi.org/10.48550/arxiv.2605.06669)"
    author: Alexandre Cristovão Maiorano
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: alexandre-cristovão-maiorano-2026-2
    resource: "https://arxiv.org/abs/2605.06669"
    title: "Alexandre Cristovão Maiorano. (2026). Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs. https://arxiv.org/abs/2605.06669"
    author: Alexandre Cristovão Maiorano
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Multi-layer defense significantly reduces bypass relative to regex-only filtering (69.65% to 46.34%), confirmed by exact McNemar test

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` The complete four-layer pipeline yields a lower bypass rate (46.34%) than Layer 1 regex-only filtering (69.65%), with Layer 1 alone blocking 112 of 369 injections. [→ Alexandre Cristovão Maiorano 2026](#alexandre-cristovao-maiorano-2026)
`q2 i?` The injection-detection improvement from Layer 1 only to the full multi-layer defense is statistically significant (p < 10^-25) by exact McNemar test. [→ Alexandre Cristovão Maiorano 2026 (2)](#alexandre-cristovao-maiorano-2026-2)

## Evidence

### Alexandre Cristovão Maiorano 2026

Alexandre Cristovão Maiorano. (2026). Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs. https://arxiv.org/abs/2605.06669 [doi:10.48550/arxiv.2605.06669](https://doi.org/10.48550/arxiv.2605.06669)

`q2 · i?` · `causal · r2`

Internal ablation on the same holdout benchmark compares regex-only Layer 1 filtering against the full pipeline. The Layer 1-only configuration blocked "112 of 369 injections", leaving 69.65% bypass versus 46.34% for the multi-layer adapter.

> "Single-Layer Defense (Regex Only): Using Layer 1 in isolation yields 69.65% bypass, with 112 of 369 injections blocked. While better than no defense, a substantial fraction of attacks still succeeds via format bypassing and boundary manipulation."

### Alexandre Cristovão Maiorano 2026 (2)

Alexandre Cristovão Maiorano. (2026). Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs. https://arxiv.org/abs/2605.06669

`q2 · i?` · `design · r2`

Paired significance testing on per-sample paired outcomes between defenses under the holdout protocol. Exact McNemar tests confirm the Layer 1-only to multi-layer improvement is "statistically significant (p <10 −25)"; no effect size is printed.

> "McNemar confirms that the injection-detection improvement from Layer 1 only to the full multi-layer defense is statistically significant (p <10 −25)."

## Discussion


## Related Claims
- [Under defense-in-depth, all 171 multi-layer bypass events are rated severity S0 (no impact) because the tutor system prompt and provider filter absorbed residual leakage](defense-in-depth-critical-bypass-zero.md) — related
- [A four-layer multi-layer defense pipeline achieves 46.34% bypass and 0.00% false positive rate on the holdout benchmark](multi-layer-guardrail-46-bypass-zero-fpr.md) — possibly the same claim (merge candidate)
- [Bypass robustness varies across student personas (32.76% to 52.05%) while FPR stays 0.00% across all personas](persona-stratified-bypass-heterogeneity.md) — related
- [Head-to-head comparison exposes a security-usability-latency tension: NeMo reaches 0% bypass at 16.22% FPR and ~1.5 s latency while Prompt Guard yields 38.48% bypass at 3.60% FPR](nemo-prompt-guard-tradeoff-holdout.md) — related
- [Multilingual gap: the multi-layer defense bypasses 73.5% of PT-BR injection samples versus 25.1% of English samples](ptbr-bypass-gap-lexical-coverage.md) — related
