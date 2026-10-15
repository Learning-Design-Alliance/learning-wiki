---
type: claim
title: "Bypass robustness varies across student personas (32.76% to 52.05%) while FPR stays 0.00% across all personas"
description: "Bypass robustness varies across student personas (32.76% to 52.05%) while FPR stays 0.00% across all personas"
id: persona-stratified-bypass-heterogeneity
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

# Bypass robustness varies across student personas (32.76% to 52.05%) while FPR stays 0.00% across all personas

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Under the multi-layer configuration, bypass ranges from 32.76% (career switcher) to 52.05% (teaching assistant), a 19.29 percentage-point spread, while FPR remains 0.00% across all personas. [→ Alexandre Cristovão Maiorano 2026](#alexandre-cristovao-maiorano-2026)

## Evidence

### Alexandre Cristovão Maiorano 2026

Alexandre Cristovão Maiorano. (2026). Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs. https://arxiv.org/abs/2605.06669 [doi:10.48550/arxiv.2605.06669](https://doi.org/10.48550/arxiv.2605.06669)

`q2 · i?` · `design · r2`

Persona-stratified holdout stress testing across five personas (deadline student, red team tester, teaching assistant, curious beginner, career switcher). The text states benign-access protection is stable across archetypes but adversarial robustness varies with persona/scenario mix.

> "In the multi-layer configuration, bypass ranges from 32.76% (career switcher) to 52.05% (teaching assistant), a 19.29 percentage-point spread, while FPR remains 0.00% across all personas in this benchmark."

## Discussion


## Related Claims
- [Multi-layer defense significantly reduces bypass relative to regex-only filtering (69.65% to 46.34%), confirmed by exact McNemar test](multi-layer-beats-regex-only-bypass.md) — related
- [A four-layer multi-layer defense pipeline achieves 46.34% bypass and 0.00% false positive rate on the holdout benchmark](multi-layer-guardrail-46-bypass-zero-fpr.md) — related
- [Head-to-head comparison exposes a security-usability-latency tension: NeMo reaches 0% bypass at 16.22% FPR and ~1.5 s latency while Prompt Guard yields 38.48% bypass at 3.60% FPR](nemo-prompt-guard-tradeoff-holdout.md) — related
- [Multilingual gap: the multi-layer defense bypasses 73.5% of PT-BR injection samples versus 25.1% of English samples](ptbr-bypass-gap-lexical-coverage.md) — related
