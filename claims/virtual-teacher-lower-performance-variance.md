---
type: claim
title: Performance variance is lower for virtual-teacher-guided learners and the advantage persists as learning progresses
description: Performance variance is lower for virtual-teacher-guided learners and the advantage persists as learning progresses
id: virtual-teacher-lower-performance-variance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: hadar-mulian-2024
    resource: "https://doi.org/10.1609/aaai.v38i21.30369"
    title: "Hadar Mulian, Segev Shlomov, Lior Limonad, Alessia Noccaro, Silvia Buscaglione. (2024). Mimicking the Maestro: Exploring the Efficacy of a Virtual AI Teacher in Fine Motor Skill Acquisition. [doi:10.1609/aaai.v38i21.30369](https://doi.org/10.1609/aaai.v38i21.30369)"
    author: Hadar Mulian, Segev Shlomov, Lior Limonad, Alessia Noccaro, Silvia Buscaglione
    q: 1
    i: "?"
    kind: causal
    rigour: 1
---

# Performance variance is lower for virtual-teacher-guided learners and the advantage persists as learning progresses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` After learning convergence, the average standard deviation of Frechet distance was lower for guided than non-guided learners on both tasks. [→ Hadar Mulian 2024](#hadar-mulian-2024)

## Evidence

### Hadar Mulian 2024

Hadar Mulian, Segev Shlomov, Lior Limonad, Alessia Noccaro, Silvia Buscaglione. (2024). Mimicking the Maestro: Exploring the Efficacy of a Virtual AI Teacher in Fine Motor Skill Acquisition. [doi:10.1609/aaai.v38i21.30369](https://doi.org/10.1609/aaai.v38i21.30369)

`q1 · i?` · `causal · r1`

H4 test: learning convergence was marked at game unit 4 (FC) and game unit 3 (WESL); standard deviation was computed for remaining game units. WESL result: t = 3.35, µ+SD = 0.036, µ−SD = 0.086, p < 0.05.

> "the result for the FC task showed a lower average in the standard deviation for the guided learner compared to the non-guided learner ( t = 7 .38,µ+SD = 0 .07,µ−SD = 0 .27,p < 0.001)."

## Discussion


## Related Claims
- [Learners guided by a virtual AI teacher perform significantly better after each learning session than learners learning independently, on synthetic RL learners](virtual-ai-teacher-session-performance-gain.md) — related
- [Learners guided by a virtual AI teacher acquire the motor skill significantly faster, reaching a competence threshold in fewer sessions than non-guided learners](virtual-teacher-faster-skill-acquisition.md) — related
- [The GAIL-based virtual teacher generalizes from the follow-the-cursor task to handwriting, with connected learners producing letters closely resembling targets](virtual-teacher-generalizes-to-handwriting.md) — related
- [Across a series of sessions, virtual-teacher-guided learners achieve significantly higher overall performance (AUC) than non-guided learners on both tasks](virtual-teacher-overall-performance-auc.md) — related
- [The virtual teacher's benefit is robust across learner starting conditions, noise levels and session lengths, averaging 25.8% improvement on FC and 15.3% on WESL](virtual-teacher-robustness-across-settings.md) — related
