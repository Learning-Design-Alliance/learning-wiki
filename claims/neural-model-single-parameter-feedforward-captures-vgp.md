---
type: claim
title: A single-parameter change in feed-forward connection strength in a neural decision model captures VGP behavior, including faster RTs with stable accuracy
description: A single-parameter change in feed-forward connection strength in a neural decision model captures VGP behavior, including faster RTs with stable accuracy
id: neural-model-single-parameter-feedforward-captures-vgp
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
sources:
  - id: green-2010
    resource: "https://doi.org/10.1016/j.cub.2010.07.040"
    title: "Green, C.S., Pouget, A., & Bavelier, D. (2010). Improved probabilistic inference as a general learning mechanism with action video games. Current Biology. https://doi.org/10.1016/j.cub.2010.07.040"
    author: "Green, C.S., Pouget, A., & Bavelier, D."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A single-parameter change in feed-forward connection strength in a neural decision model captures VGP behavior, including faster RTs with stable accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Increasing feed-forward conductance between sensory and integration layers by 55% (motion) and 51% (auditory) captures VGP performance, raising RT speed while leaving accuracy nearly unchanged. [→ Green 2010](#green-2010)

## Evidence

### Green 2010

Green, C.S., Pouget, A., & Bavelier, D. (2010). Improved probabilistic inference as a general learning mechanism with action video games. Current Biology. https://doi.org/10.1016/j.cub.2010.07.040

`q2 · i?` · `causal · r2`

Numerical model fitting (Figure 2B) of the probabilistic population network of Beck et al. The article explains that increased conductance also induces membrane-potential fluctuations that speed bound-reaching, so the two effects cancel on accuracy. No effect size is printed.

> "The neural model captures the change in performance from NVGP to VGP with a 55% increase in the conductance of the feed-forward connections between the sensory (MT) and the integration (LIP) layers and, in contrast to the DDM, nearly no change in the bound height"

## Discussion


## Related Claims

- [In fixed-duration conditions, accuracy rises faster with presentation duration in VGPs, confirming greater sensory integration and ruling out non-decision-time accounts](fixed-duration-faster-accuracy-rise-vgp.md)
- [According to a probabilistic population neural model, VGPs make better use of the evidence, with log odds 19% higher than NVGPs in the motion task](vgp-better-posterior-log-odds-motion.md)
