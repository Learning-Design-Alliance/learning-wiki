---
type: product
id: proberai
title: Prober.ai
description: Prober.ai is a research-logging software platform that records consented participant sessions, events, drafts, challenges, unlocks, and reflection-coaching interactions for studying learning behavior.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Prober.ai

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
Prober.ai is a research-logging software platform that records consented participant sessions, events, drafts, challenges, unlocks, and reflection-coaching interactions for studying learning behavior.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Prober.ai research-logging pipeline**: Prober.ai ships with a research-logging pipeline that "captures the full interaction without altering the student experience." An optional Study Setup mode records participant, session, condition, and prompt identifiers with a consent flag, and dedicated endpoints append newline-delimited JSON to six logs (sessions, events, drafts, challenges, unlocks, reflection-coaching). Fine-grained timestamped events let a researcher reconstruct each student's revision trajectory and the {question, defense, score, revision} tuples the reflection gate produces; each model call carries a hashed, privacy-preserving safety_identifier. (Ran Bi et al. (2026))

### Claims

- [Explicit API interception from a pilot cohort of 19 students yielded 1,880 events over about 57 active student-hours](../claims/vismatic-pilot-cohort-1880-events.md) [+W]
- [Macro-level behavioral metrics flagged anomalies consistent with automated workflows and off-platform AI code synthesis](../claims/behavioral-metrics-flag-automated-anomalies.md) [+W]
- [The deterministic reflection gate reliably distinguished low-effort defenses from substantive ones during validation, coaching filler answers rather than unlocking](../claims/reflection-gate-distinguishes-low-effort-defenses.md) [+W]
- [Schema-constrained Structured Outputs eliminated parse failures: every /challenge and /unlock call returned a valid, fully-typed object during development testing](../claims/structured-outputs-eliminate-parse-failure-class.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Ran Bi, Shiyao Wei, Yuanyiyi Zhou. (2026). Prober.ai: Gated Inquiry-Based Feedback via LLM-Constrained Personas for Argumentative Writing Development. https://arxiv.org/abs/2605.05598
