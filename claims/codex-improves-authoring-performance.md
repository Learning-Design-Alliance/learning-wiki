---
type: claim
title: AI code generator access significantly improves code-authoring correctness, speed, and error rates during training
description: AI code generator access significantly improves code-authoring correctness, speed, and error rates during training
id: codex-improves-authoring-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: strong
sources:
  - id: majeed-kazemitabaar-2023
    title: Majeed Kazemitabaar 2023
    q: 3
    i: 3
    kind: causal
    rigour: 2
  - id: majeed-kazemitabaar-2023-2
    title: Majeed Kazemitabaar 2023 (2)
    q: 3
    i: 3
    kind: causal
    rigour: 2
  - id: majeed-kazemitabaar-2023-3
    title: Majeed Kazemitabaar 2023 (3)
    q: 3
    i: 2
    kind: causal
    rigour: 2
---

# AI code generator access significantly improves code-authoring correctness, speed, and error rates during training

> **Claim** · [All claims](index.md)
> **Evidence** · 3 studies · 3 causal `r2` · `q3` · `i2`–`i3`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i3` Codex group scored significantly higher on authoring task correctness (M=80.1% vs M=44.4%, d=1.67). [→ Majeed Kazemitabaar 2023](#majeed-kazemitabaar-2023)
`q3 i3` Codex group completed authoring tasks significantly faster (M=210s vs M=361s, d=1.56). [→ Majeed Kazemitabaar 2023 (2)](#majeed-kazemitabaar-2023-2)
`q3 i2` Codex group encountered significantly fewer errors per task (M=1.28 vs M=2.17, d=0.74). [→ Majeed Kazemitabaar 2023 (3)](#majeed-kazemitabaar-2023-3)

## Evidence

### Majeed Kazemitabaar 2023

Majeed Kazemitabaar, Justin Chow, Carl Ka To Ma, Barbara J. Ericson, David Weintrop, and Tovi Grossman. 2023. Studying the effect of AI Code Generators on Supporting Novice Learners in Introductory Programming. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23). https://doi.org/10.1145/3544548.3580919

`q3 · i3` · `causal · r2`

Training-phase authoring tasks, the only phase where Codex group had AI access. Independent t-test showed "correctness score was significantly higher for the Codex group" with a large effect size d=1.67.

> "correctness score was significantly higher for the Codex group (Codex: M=80.1%, SD=14.5%; Baseline: M=44.4%, SD=26.5%; t(67)=6.92, p<.001; d=1.67)"

### Majeed Kazemitabaar 2023 (2)

Majeed Kazemitabaar, Justin Chow, Carl Ka To Ma, Barbara J. Ericson, David Weintrop, and Tovi Grossman. 2023. Studying the effect of AI Code Generators on Supporting Novice Learners in Introductory Programming. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23). https://doi.org/10.1145/3544548.3580919

`q3 · i3` · `causal · r2`

Active completion time on training authoring tasks, measured by removing inactivity gaps over one minute. "task completion time was significantly less in the Codex group" with d=1.56.

> "task completion time was significantly less in the Codex group (Codex: M=210s, SD=99s; Baseline: M=361s, SD=95s; t(67)=6.40, p<.001, d=1.56)"

### Majeed Kazemitabaar 2023 (3)

Majeed Kazemitabaar, Justin Chow, Carl Ka To Ma, Barbara J. Ericson, David Weintrop, and Tovi Grossman. 2023. Studying the effect of AI Code Generators on Supporting Novice Learners in Introductory Programming. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23). https://doi.org/10.1145/3544548.3580919

`q3 · i2` · `causal · r2`

Error counts from console logs categorized into syntax, data-type, and semantic errors. "Learners in the Codex group also encountered significantly fewer errors per task" with d=0.74.

> "Learners in the Codex group also encountered significantly fewer errors per task (Codex: M=1.28, SD=1.1; Baseline: M=2.17, SD=1.31; t(67)=3.03, p=.004, d=0.74)"

## Discussion


## Related Claims
- [Prior AI code generator access does not reduce manual code-modification performance during training](codex-no-harm-to-modification.md) — related
- [Novices with AI code generator access complete significantly more training tasks than those without](codex-increases-training-completion-rate.md) — related
- [Codex and Baseline groups perform similarly on immediate post-test without AI access](codex-similar-immediate-posttest.md) — related
- [Learners with higher prior programming competency benefit more from AI code generators on retention](prior-competency-moderates-codex-benefit.md) — related
- [Retention test one week later shows slight Codex-group advantage that does not reach statistical significance](codex-retention-not-significant.md) — related
- [AI code generator access reduces stress and increases eagerness to continue learning programming](codex-reduces-stress-increases-eagerness.md) — related
- [Novices use AI code generators in varied patterns including copying task descriptions and submitting generated code unmodified](codex-usage-patterns-novices.md) — related
- [At publication, a frontier coding model could produce solutions to six of the ten research-shaped assignments but struggled with four, which the authors treat as non-durable design experience](kt1-model-resistance-six-of-ten-assignments.md) — related
