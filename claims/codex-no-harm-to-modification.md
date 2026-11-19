---
type: claim
title: Prior AI code generator access does not reduce manual code-modification performance during training
description: Prior AI code generator access does not reduce manual code-modification performance during training
id: codex-no-harm-to-modification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
sources:
  - id: majeed-kazemitabaar-2023
    title: Majeed Kazemitabaar 2023
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Prior AI code generator access does not reduce manual code-modification performance during training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Both groups had similar correctness scores on modifying tasks (Codex M=66.2% vs Baseline M=58.4%, p=.202, d=0.31, not significant). [→ Majeed Kazemitabaar 2023](#majeed-kazemitabaar-2023)

## Evidence

### Majeed Kazemitabaar 2023

Majeed Kazemitabaar, Justin Chow, Carl Ka To Ma, Barbara J. Ericson, David Weintrop, and Tovi Grossman. 2023. Studying the effect of AI Code Generators on Supporting Novice Learners in Introductory Programming. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23). https://doi.org/10.1145/3544548.3580919

`q3 · i?` · `causal · r2`

Training-phase modifying tasks where neither group had AI access. Starter code was the solution to the previous authoring task. "both groups had similar correctness scores on modifying tasks" with no significant difference; equivalence was not tested.

> "both groups had similar correctness scores on modifying tasks (Codex: M=66.2%, SD=25.6%; Baseline: M=58.4%, SD=23.9%; t(67)=1.28, p=.202, d=0.31)"

## Discussion


## Related Claims
- [AI code generator access significantly improves code-authoring correctness, speed, and error rates during training](codex-improves-authoring-performance.md) — related
- [Novices with AI code generator access complete significantly more training tasks than those without](codex-increases-training-completion-rate.md) — related
- [Codex and Baseline groups perform similarly on immediate post-test without AI access](codex-similar-immediate-posttest.md) — related
- [Retention test one week later shows slight Codex-group advantage that does not reach statistical significance](codex-retention-not-significant.md) — related
- [AI code generator access reduces stress and increases eagerness to continue learning programming](codex-reduces-stress-increases-eagerness.md) — related
