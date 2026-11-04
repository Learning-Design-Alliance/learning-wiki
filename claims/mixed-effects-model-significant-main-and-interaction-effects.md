---
type: claim
title: Model choice, prompting configuration, and rubric component all significantly affect LLM-human agreement, with significant interactions
description: Model choice, prompting configuration, and rubric component all significantly affect LLM-human agreement, with significant interactions
id: mixed-effects-model-significant-main-and-interaction-effects
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-03
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: stadler-p-2026
    resource: "https://doi.org/10.2196/94666"
    title: "Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J. (2026). Test-Retest Reliability of Large Language Models and Their Concordance With Human Experts in Rubric-Based Scoring of Clinical Summary Statements: Experimental Comparative Study. JMIR Medical Education. https://doi.org/10.2196/94666"
    author: Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Model choice, prompting configuration, and rubric component all significantly affect LLM-human agreement, with significant interactions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A linear mixed-effects model revealed significant main effects for model, prompting configuration, and rubric component, with all 2-way and 3-way interactions also significant. [→ Stadler P 2026](#stadler-p-2026)

## Evidence

### Stadler P 2026

Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J. (2026). Test-Retest Reliability of Large Language Models and Their Concordance With Human Experts in Rubric-Based Scoring of Clinical Summary Statements: Experimental Comparative Study. JMIR Medical Education. https://doi.org/10.2196/94666

`q2 · i?` · `causal · r2`

A linear mixed-effects model with batch as random intercept followed by Type III ANOVA was conducted on run-level Gwet AC1/AC2 coefficients across all 5 runs per condition. The study reports "significant main effects for model (F3, 64= 2178.01, P<.001)" among others.

> "The analysis revealed significant main effects for model (F3, 64= 2178.01, P<.001), prompting configuration (F3,64=538.21, P<.001), and rubric component (F5,320=714.33, P<.001). Crucially, all 2-way and 3-way interaction effects were also significant (P<.001)."

## Discussion


## Related Claims
- [Concordance between LLM and human ratings is higher for binary rubric components than for ternary components](higher-concordance-binary-than-ternary-components.md) — a narrower finding that bears on this claim
- [Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases](llm-pairwise-agreement-model-type-temperature.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions](variance-decomposition-model-prompt-weak-levers.md) — related
- [A multimodal LLM achieves moderate-to-substantial agreement with human consensus on well-defined CT practices but lower agreement on multi-component constructs like Physics Correctness and Systems Thinking](llm-human-agreement-ct-practices.md) — related
