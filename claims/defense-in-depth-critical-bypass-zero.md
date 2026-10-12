---
type: claim
title: Under defense-in-depth, all 171 multi-layer bypass events are rated severity S0 (no impact) because the tutor system prompt and provider filter absorbed residual leakage
description: Under defense-in-depth, all 171 multi-layer bypass events are rated severity S0 (no impact) because the tutor system prompt and provider filter absorbed residual leakage
id: defense-in-depth-critical-bypass-zero
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: alexandre-cristovão-maiorano-2026
    resource: "https://arxiv.org/abs/2605.06669"
    title: "Alexandre Cristovão Maiorano. (2026). Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs. https://arxiv.org/abs/2605.06669"
    author: Alexandre Cristovão Maiorano
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Under defense-in-depth, all 171 multi-layer bypass events are rated severity S0 (no impact) because the tutor system prompt and provider filter absorbed residual leakage

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Of the 171 inputs escaping the input gate, 71 were provider-filtered and the tutor's pedagogical system prompt refused or redirected all 100 that reached it, so 171/171 bypass events are rated S0 with a critical bypass rate (S2+S3) of 0%. [→ Alexandre Cristovão Maiorano 2026](#alexandre-cristovao-maiorano-2026)

## Evidence

### Alexandre Cristovão Maiorano 2026

Alexandre Cristovão Maiorano. (2026). Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs. https://arxiv.org/abs/2605.06669

`q2 · i?` · `design · r2`

Response-level severity audit of the 171 multi-layer bypass events, run by querying a downstream Azure OpenAI gpt-4.1 tutor and classifying actual response text. The audit found "171/171 (100%) S0"; the result is conditional on the educational system prompt and content-filtered provider being in place.

> "The classifier therefore assigns S0 (no impact) to every bypass event in this evaluation: 171/171 (100%) S0, with 0 events at S1, S2, or S3 and a critical bypass rate (S2+S3) of 0%."

## Discussion


## Related Claims
- [Multi-layer defense significantly reduces bypass relative to regex-only filtering (69.65% to 46.34%), confirmed by exact McNemar test](multi-layer-beats-regex-only-bypass.md) — related
- [A four-layer multi-layer defense pipeline achieves 46.34% bypass and 0.00% false positive rate on the holdout benchmark](multi-layer-guardrail-46-bypass-zero-fpr.md) — related
- [Head-to-head comparison exposes a security-usability-latency tension: NeMo reaches 0% bypass at 16.22% FPR and ~1.5 s latency while Prompt Guard yields 38.48% bypass at 3.60% FPR](nemo-prompt-guard-tradeoff-holdout.md) — related
- [Privacy protection in the framework is partial: three residual leakage channels remain open](partial-privacy-three-residual-leakage-channels.md) — related
