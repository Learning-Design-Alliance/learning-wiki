---
type: research-method
id: tutoring-effectiveness-index-tei
title: Tutoring Effectiveness Index (TEI)
description: "TEI is a fixed-weight linear index over four signals computed without any external model at selection time: \"a Schoenfeld-Verify keyword ratio, a math-step density, an ends-question rate, and a deep-reasoning gate from the Deep-Thinking Ratio (DTR) probe\"."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# Tutoring Effectiveness Index (TEI)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 causal), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
TEI is a fixed-weight linear index over four signals computed without any external model at selection time: "a Schoenfeld-Verify keyword ratio, a math-step density, an ends-question rate, and a deep-reasoning gate from the Deep-Thinking Ratio (DTR) probe". Verification and explicit math content are rewarded, ending tutor turns with questions is penalised, and the DTR gate adds a small bonus. Weights (α, β, γ, δ) = (1.0, 0.75, 1.0, 0.5) are fixed a priori from theory to preserve the training-free, judge-free property.

## Accounts
<!-- How each source describes or uses the method -->
- **Tutoring Effectiveness Index (TEI): a training-free, judge-free four-signal index for scoring candidate tutor responses**: TEI is a fixed-weight linear index over four signals computed without any external model at selection time: "a Schoenfeld-Verify keyword ratio, a math-step density, an ends-question rate, and a deep-reasoning gate from the Deep-Thinking Ratio (DTR) probe". Verification and explicit math content are rewarded, ending tutor turns with questions is penalised, and the DTR gate adds a small bonus. Weights (α, β, γ, δ) = (1.0, 0.75, 1.0, 0.5) are fixed a priori from theory to preserve the training-free, judge-free property. (The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation)

### Claims
- [TEI@N inference-time selection raises the improvement rate on pre-incorrect math scenarios from 59.0% to 81.9% at N=8 over Greedy on a frozen DeepSeek-R1-8B base](../claims/tei-selection-raises-improvement-rate-pre-incorrect.md) [+M]
- [On the same frozen base, TEI@4 beats both DTR@4 and Greedy on Δ Solve Rate, leak rate, and composite R_total at no training cost](../claims/tei4-beats-dtr4-and-greedy-same-base.md) [+M]

## Related Research Methods
-

## Key Sources
- Shim Jaechang and Unggi Lee. 2026. The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals. In Proceedings of The 35th ACM International Conference on Information and Knowledge Management (CIKM '26). https://arxiv.org/abs/2605.30666
