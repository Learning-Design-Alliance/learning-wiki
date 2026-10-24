---
type: claim
title: "Head-to-head comparison exposes a security-usability-latency tension: NeMo reaches 0% bypass at 16.22% FPR and ~1.5 s latency while Prompt Guard yields 38.48% bypass at 3.60% FPR"
description: "Head-to-head comparison exposes a security-usability-latency tension: NeMo reaches 0% bypass at 16.22% FPR and ~1.5 s latency while Prompt Guard yields 38.48% bypass at 3.60% FPR"
id: nemo-prompt-guard-tradeoff-holdout
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Head-to-head comparison exposes a security-usability-latency tension: NeMo reaches 0% bypass at 16.22% FPR and ~1.5 s latency while Prompt Guard yields 38.48% bypass at 3.60% FPR

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the identical holdout split, NeMo Guardrails achieves 0% bypass but a 16.22% false positive rate and over 1.4 seconds average latency, while Prompt Guard reduces bypass to 38.48% with a 3.60% FPR. [→ Alexandre Cristovão Maiorano 2026](#alexandre-cristovao-maiorano-2026)

## Evidence

### Alexandre Cristovão Maiorano 2026

Alexandre Cristovão Maiorano. (2026). Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs. https://arxiv.org/abs/2605.06669 [doi:10.48550/arxiv.2605.06669](https://doi.org/10.48550/arxiv.2605.06669)

`q2 · i?` · `design · r2`

Direct head-to-head evaluation of external adapters on the identical 480-query holdout split with unified latency instrumentation. The quote names NeMo's trade-off; Prompt Guard "offers a mid-point, reducing bypass to 38.48% but still suffering a 3.60% FPR." Both were threshold- or rail-configured on a stratified calibration split.

> "NeMo Guardrails achieves a perfect 0% bypass rate, but at the cost of a prohibitive 16.22% false positive rate and extreme latency delays (over 1.4 seconds on average, p95 above 4 seconds)"

## Discussion


## Related Claims
- [Under defense-in-depth, all 171 multi-layer bypass events are rated severity S0 (no impact) because the tutor system prompt and provider filter absorbed residual leakage](defense-in-depth-critical-bypass-zero.md) — related
- [A four-layer multi-layer defense pipeline achieves 46.34% bypass and 0.00% false positive rate on the holdout benchmark](multi-layer-guardrail-46-bypass-zero-fpr.md) — related
- [Bypass robustness varies across student personas (32.76% to 52.05%) while FPR stays 0.00% across all personas](persona-stratified-bypass-heterogeneity.md) — related
- [Multi-layer defense significantly reduces bypass relative to regex-only filtering (69.65% to 46.34%), confirmed by exact McNemar test](multi-layer-beats-regex-only-bypass.md) — related
- [Multilingual gap: the multi-layer defense bypasses 73.5% of PT-BR injection samples versus 25.1% of English samples](ptbr-bypass-gap-lexical-coverage.md) — related
- [Qwen 7B and Mistral Nemo 12B passed the classroom speed gate in round 2 and were retained as candidates pending faculty review](round2-candidates-pass-speed-gate.md) — related
- [Taxonomy-augmented guardrail classifiers reduce educational attack success more than general-purpose jailbreak defenses](taxonomy-augmented-guardrails-education-specific-risks.md) — related
