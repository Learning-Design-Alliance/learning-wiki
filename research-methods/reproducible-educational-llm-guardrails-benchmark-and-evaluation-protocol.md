---
type: research-method
id: reproducible-educational-llm-guardrails-benchmark-and-evaluation-protocol
title: Reproducible educational LLM guardrails benchmark and evaluation protocol
description: A controlled holdout benchmark of 480 synthetic queries (369 injection, 111 benign) covering six attack families, with stratified bootstrap confidence intervals, paired McNemar tests, and multi-seed sensitivity sweeps, plus unified head-to-head adapter measurements.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Reproducible educational LLM guardrails benchmark and evaluation protocol

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A controlled holdout benchmark of 480 synthetic queries (369 injection, 111 benign) covering six attack families, with stratified bootstrap confidence intervals, paired McNemar tests, and multi-seed sensitivity sweeps, plus unified head-to-head adapter measurements. The article provides "a reproducible controlled protocol (480 queries) with confusion matrix reporting, latency decomposition, statistical uncertainty quantification" and releases a complete reproducibility package (Docker, dataset, scripts) in a public GitHub repository for independent verification.

## Accounts
<!-- How each source describes or uses the method -->
- **Reproducible educational LLM guardrails benchmark and evaluation protocol**: A controlled holdout benchmark of 480 synthetic queries (369 injection, 111 benign) covering six attack families, with stratified bootstrap confidence intervals, paired McNemar tests, and multi-seed sensitivity sweeps, plus unified head-to-head adapter measurements. The article provides "a reproducible controlled protocol (480 queries) with confusion matrix reporting, latency decomposition, statistical uncertainty quantification" and releases a complete reproducibility package (Docker, dataset, scripts) in a public GitHub repository for independent verification. (Alexandre Cristovão Maiorano (2026))

### Claims
- [A four-layer multi-layer defense pipeline achieves 46.34% bypass and 0.00% false positive rate on the holdout benchmark](../claims/multi-layer-guardrail-46-bypass-zero-fpr.md) [+M]
- [Head-to-head comparison exposes a security-usability-latency tension: NeMo reaches 0% bypass at 16.22% FPR and ~1.5 s latency while Prompt Guard yields 38.48% bypass at 3.60% FPR](../claims/nemo-prompt-guard-tradeoff-holdout.md) [+M]

## Related Research Methods
-

## Key Sources
- Alexandre Cristovão Maiorano. (2026). Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs. https://arxiv.org/abs/2605.06669
