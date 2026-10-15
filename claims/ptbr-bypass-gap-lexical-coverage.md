---
type: claim
title: "Multilingual gap: the multi-layer defense bypasses 73.5% of PT-BR injection samples versus 25.1% of English samples"
description: "Multilingual gap: the multi-layer defense bypasses 73.5% of PT-BR injection samples versus 25.1% of English samples"
id: ptbr-bypass-gap-lexical-coverage
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
    kind: design
    rigour: 2
---

# Multilingual gap: the multi-layer defense bypasses 73.5% of PT-BR injection samples versus 25.1% of English samples

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Portuguese (PT-BR) injection queries bypass the multi-layer defense at 73.5% versus 25.1% for English queries, a 48.3 percentage point gap attributed to Layer 1 pattern coverage gaps. [→ Alexandre Cristovão Maiorano 2026](#alexandre-cristovao-maiorano-2026)

## Evidence

### Alexandre Cristovão Maiorano 2026

Alexandre Cristovão Maiorano. (2026). Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs. https://arxiv.org/abs/2605.06669 [doi:10.48550/arxiv.2605.06669](https://doi.org/10.48550/arxiv.2605.06669)

`q2 · i?` · `design · r2`

Language-stratified analysis of the multi-layer defense on the holdout benchmark (Table 7). Failure-pattern analysis reports "34% of PT-BR injection patterns lack corresponding regex rules in Layer 1", plus accent-character and translation-artifact bypasses.

> "The 48.3 percentage point gap in bypass rate between EN (25.1%) and PT-BR (73.5%) samples indicates that multilingual coverage remains an active challenge."

## Discussion


## Related Claims
- [Head-to-head comparison exposes a security-usability-latency tension: NeMo reaches 0% bypass at 16.22% FPR and ~1.5 s latency while Prompt Guard yields 38.48% bypass at 3.60% FPR](nemo-prompt-guard-tradeoff-holdout.md) — related
- [A four-layer multi-layer defense pipeline achieves 46.34% bypass and 0.00% false positive rate on the holdout benchmark](multi-layer-guardrail-46-bypass-zero-fpr.md) — related
- [Multi-layer defense significantly reduces bypass relative to regex-only filtering (69.65% to 46.34%), confirmed by exact McNemar test](multi-layer-beats-regex-only-bypass.md) — related
- [Bypass robustness varies across student personas (32.76% to 52.05%) while FPR stays 0.00% across all personas](persona-stratified-bypass-heterogeneity.md) — related
