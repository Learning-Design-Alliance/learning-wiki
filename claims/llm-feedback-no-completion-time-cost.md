---
type: claim
title: Receiving LLM feedback did not significantly increase lesson completion time
description: Receiving LLM feedback did not significantly increase lesson completion time
id: llm-feedback-no-completion-time-cost
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: thomas-2025
    resource: "https://doi.org/10.1007/978-3-032-03870-8_33"
    title: "Thomas, D. R., Borchers, C., Bhushan, S., Gatz, E., Gupta, S., & Koedinger, K. R. (2025). LLM-Generated Feedback Supports Learning If Learners Choose to Use It. arXiv. [doi:10.1007/978-3-032-03870-8_33](https://doi.org/10.1007/978-3-032-03870-8_33)"
    author: "Thomas, D. R., Borchers, C., Bhushan, S., Gatz, E., Gupta, S., & Koedinger, K. R."
    q: 3
    i: 0
    kind: causal
    rigour: 2
---

# Receiving LLM feedback did not significantly increase lesson completion time

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3` · `i0` negligible
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i0` A linear mixed model on log-transformed completion time found no statistically significant effect of receiving LLM feedback (Estimate = 0.00, p = .999), with conditions differing by an average of 9 seconds. [→ Thomas 2025](#thomas-2025)

## Evidence

### Thomas 2025

Thomas, D. R., Borchers, C., Bhushan, S., Gatz, E., Gupta, S., & Koedinger, K. R. (2025). LLM-Generated Feedback Supports Learning If Learners Choose to Use It. arXiv. [doi:10.1007/978-3-032-03870-8_33](https://doi.org/10.1007/978-3-032-03870-8_33)

`q3 · i0` · `causal · r2`

Efficiency analysis (RQ2) comparing TOT learners against Control and ITT non-users using log-transformed completion time in a linear mixed model with random intercepts. The quote prints "Estimate = 0.00, 95% CI [-0.08, 0.08], p = .999"; learners receiving feedback averaged 5.75 minutes versus 5.59 minutes. Equivalence was not tested.

> "Results indicate no statistically significant effect of receiving LLM feedback on the time taken to complete lessons (Estimate = 0.00, 95% CI [-0.08, 0.08], p = .999)."

## Discussion


## Related Claims
- [Mere assignment of LLM feedback availability (ITT) did not significantly improve posttest performance](itt-availability-no-significant-effect.md) — related
- [All three LLM-generated feedback types are associated with faster time to solution than a compiler-errors-only baseline, with Single-Issue Feedback showing the largest reduction](llm-feedback-faster-time-to-solution.md) — reports the opposite
- [Error rates per completed problem-solving step did not significantly differ between conditions](no-difference-error-rate-log.md) — related
- [Feedback effects on time to solution did not differ significantly between novice and advanced students, though predicted trends suggest feedback was more beneficial for advanced students](no-significant-feedback-expertise-interaction.md) — related
