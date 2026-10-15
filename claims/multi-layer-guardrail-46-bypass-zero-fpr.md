---
type: claim
title: "A four-layer multi-layer defense pipeline achieves 46.34% bypass and 0.00% false positive rate on the holdout benchmark"
description: "A four-layer multi-layer defense pipeline achieves 46.34% bypass and 0.00% false positive rate on the holdout benchmark"
id: multi-layer-guardrail-46-bypass-zero-fpr
status: draft
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
    kind: design
    rigour: 2
---

# A four-layer multi-layer defense pipeline achieves 46.34% bypass and 0.00% false positive rate on the holdout benchmark

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the 480-query holdout benchmark, the multi-layer defense blocked 198 of 369 injection attempts while passing all 111 benign queries, yielding a 46.34% bypass rate and 0.00% false positive rate. [→ Alexandre Cristovão Maiorano 2026](#alexandre-cristovao-maiorano-2026)

## Evidence

### Alexandre Cristovão Maiorano 2026

Alexandre Cristovão Maiorano. (2026). Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs. https://arxiv.org/abs/2605.06669 [doi:10.48550/arxiv.2605.06669](https://doi.org/10.48550/arxiv.2605.06669)

`q2 · i?` · `design · r2`

Offline evaluation on a synthetic 480-query benchmark (369 injection, 111 benign) with a stratified 20% calibration split and an 80% holdout. The primary multi-layer adapter's confusion matrix shows "111/111 benign passed; 198/369 injections blocked", yielding the printed bypass, FPR, and latency figures.

> "Table 2 summarizes per-class outcomes for the primary multi-layer adapter (111/111 benign passed; 198/369 injections blocked). This operating point yields a46.34%bypass rate, a0.00%false positive rate, and an2.50 msaverage latency."

## Discussion


## Related Claims
- [Under defense-in-depth, all 171 multi-layer bypass events are rated severity S0 (no impact) because the tutor system prompt and provider filter absorbed residual leakage](defense-in-depth-critical-bypass-zero.md) — related
- [Multi-layer defense significantly reduces bypass relative to regex-only filtering (69.65% to 46.34%), confirmed by exact McNemar test](multi-layer-beats-regex-only-bypass.md) — possibly the same claim (merge candidate)
- [Bypass robustness varies across student personas (32.76% to 52.05%) while FPR stays 0.00% across all personas](persona-stratified-bypass-heterogeneity.md) — related
- [Head-to-head comparison exposes a security-usability-latency tension: NeMo reaches 0% bypass at 16.22% FPR and ~1.5 s latency while Prompt Guard yields 38.48% bypass at 3.60% FPR](nemo-prompt-guard-tradeoff-holdout.md) — related
- [Multilingual gap: the multi-layer defense bypasses 73.5% of PT-BR injection samples versus 25.1% of English samples](ptbr-bypass-gap-lexical-coverage.md) — related
