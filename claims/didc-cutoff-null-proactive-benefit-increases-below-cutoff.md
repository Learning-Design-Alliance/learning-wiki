---
type: claim
title: At the median cutoff, proactive and reactive tutoring show no significant difference in MAP growth, with proactive benefits increasing for students farther below the cutoff
description: At the median cutoff, proactive and reactive tutoring show no significant difference in MAP growth, with proactive benefits increasing for students farther below the cutoff
id: didc-cutoff-null-proactive-benefit-increases-below-cutoff
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: ashish-gurung-2026
    resource: "https://arxiv.org/abs/2605.11155"
    title: "Ashish Gurung, Ge Gao, Jordan Gutterman, Danielle R. Thomas, Shivang Gupta, Lee Branstetter, Emma Brunskill, Vincent Aleven, Kenneth R. Koedinger. (2026). Improving Hybrid Human-AI Tutoring by Differentiating Human Tutor Roles Based on Student Needs. arXiv preprint. https://arxiv.org/abs/2605.11155"
    author: Ashish Gurung, Ge Gao, Jordan Gutterman, Danielle R. Thomas, Shivang Gupta, Lee Branstetter, Emma Brunskill, Vincent Aleven, Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: ashish-gurung-2026-2
    resource: "https://arxiv.org/abs/2605.11155"
    title: "Ashish Gurung, Ge Gao, Jordan Gutterman, Danielle R. Thomas, Shivang Gupta, Lee Branstetter, Emma Brunskill, Vincent Aleven, Kenneth R. Koedinger. (2026). Improving Hybrid Human-AI Tutoring by Differentiating Human Tutor Roles Based on Student Needs. arXiv preprint. https://arxiv.org/abs/2605.11155"
    author: Ashish Gurung, Ge Gao, Jordan Gutterman, Danielle R. Thomas, Shivang Gupta, Lee Branstetter, Emma Brunskill, Vincent Aleven, Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# At the median cutoff, proactive and reactive tutoring show no significant difference in MAP growth, with proactive benefits increasing for students farther below the cutoff

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` At the cutoff, the difference between proactive and reactive tutoring on relative MAP growth was not statistically significant (-0.33, p = .579), while reactive students at the cutoff achieved 1.74x expected growth. [→ Ashish Gurung 2026](#ashish-gurung-2026)
`q2 i?` The proactive-by-prior-performance interaction was not statistically significant (-1.61, p = .247), but its magnitude suggests the proactive benefit increased by approximately 1.6x per SD below the cutoff. [→ Ashish Gurung 2026 (2)](#ashish-gurung-2026-2)

## Evidence

### Ashish Gurung 2026

Ashish Gurung, Ge Gao, Jordan Gutterman, Danielle R. Thomas, Shivang Gupta, Lee Branstetter, Emma Brunskill, Vincent Aleven, Kenneth R. Koedinger. (2026). Improving Hybrid Human-AI Tutoring by Differentiating Human Tutor Roles Based on Student Needs. arXiv preprint. https://arxiv.org/abs/2605.11155

`q2 · i?` · `causal · r2`

DiDC analysis (Equation 4) on the IK-bandwidth subsample estimating the treatment effect at the median cutoff, with prior performance standardized within grades. The proactive-reactive difference at the cutoff was "not statistically significant (-0.33, p = .579)"; equivalence was not tested.

> "At the cutoff, students in the reactive group achieved 1.74×expected MAP growth (+74%, p = .007). Although proactive students at the cutoff showed numerically lower growth, this difference was not statistically significant (-0.33, p = .579)."

### Ashish Gurung 2026 (2)

Ashish Gurung, Ge Gao, Jordan Gutterman, Danielle R. Thomas, Shivang Gupta, Lee Branstetter, Emma Brunskill, Vincent Aleven, Kenneth R. Koedinger. (2026). Improving Hybrid Human-AI Tutoring by Differentiating Human Tutor Roles Based on Student Needs. arXiv preprint. https://arxiv.org/abs/2605.11155

`q2 · i?` · `causal · r2`

DiDC heterogeneity estimate (Equation 4) on the IK-bandwidth subsample. The interaction was "not statistically significant (-1.61, p = .247)"; the authors interpret the point estimate as indicating the proactive benefit increased by approximately 1.6x per SD below the cutoff.

> "The in- teraction between proactive tutoring and prior performance was also not statistically significant (-1.61, p = .247); how- ever, the magnitude of this estimate suggests a meaningful pattern."

## Discussion


## Related Claims
- [Proactive tutoring produced larger relative MAP growth than reactive tutoring on average (75% marginally significant in the IK bandwidth)](proactive-tutoring-larger-relative-map-growth.md) — related
- [Introducing human-AI tutoring improves relative MAP academic growth by 61% over an AI-only baseline within the IK bandwidth](human-ai-tutoring-improves-map-growth-over-ai-only.md) — related
- [Human-AI tutoring increases IXL time on task by 25% with no significant difference between proactive and reactive groups](human-ai-tutoring-increases-time-on-task.md) — related
- [Human-AI tutoring is associated with a 36% rise in IXL skill proficiency, but the gap widened in favor of reactively tutored students (difference-in-differences preprint)](human-ai-tutoring-skill-proficiency-gap-widens.md) — reports the opposite
