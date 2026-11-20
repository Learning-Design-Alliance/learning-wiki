---
type: claim
title: "The virtual teacher's benefit is robust across learner starting conditions, noise levels and session lengths, averaging 25.8% improvement on FC and 15.3% on WESL"
description: "The virtual teacher's benefit is robust across learner starting conditions, noise levels and session lengths, averaging 25.8% improvement on FC and 15.3% on WESL"
id: virtual-teacher-robustness-across-settings
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

# The virtual teacher's benefit is robust across learner starting conditions, noise levels and session lengths, averaging 25.8% improvement on FC and 15.3% on WESL

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Across 64 settings, connected learners outperformed non-connected learners in every comparison, with average Frechet-distance improvements of 25.8% (FC) and 15.3% (WESL) and minimal improvements of 17% and 11%. [→ Hadar Mulian 2024](#hadar-mulian-2024)

## Evidence

### Hadar Mulian 2024

Hadar Mulian, Segev Shlomov, Lior Limonad, Alessia Noccaro, Silvia Buscaglione. (2024). Mimicking the Maestro: Exploring the Efficacy of a Virtual AI Teacher in Fine Motor Skill Acquisition. [doi:10.1609/aaai.v38i21.30369](https://doi.org/10.1609/aaai.v38i21.30369)

`q1 · i?` · `causal · r1`

Robustness tests varied learners' initial skills, learning rates, attention (noise) levels, noise type (Gaussian/uniform), and session lengths across 64 settings and 32 comparisons of 10 learners each. The maximal difference between comparisons was 39% (FC) and 20.1% (WESL).

> "The average improvement (i.e., the difference between the Frechet distance) between connected and not-connected learners across all settings are 25.8% and 15.3% for the FC task and the WESL task respectively, where the standard deviations are 0.05 and 0.025."

## Discussion


## Related Claims
- [Learners guided by a virtual AI teacher perform significantly better after each learning session than learners learning independently, on synthetic RL learners](virtual-ai-teacher-session-performance-gain.md) — related
- [Learners guided by a virtual AI teacher acquire the motor skill significantly faster, reaching a competence threshold in fewer sessions than non-guided learners](virtual-teacher-faster-skill-acquisition.md) — related
- [The GAIL-based virtual teacher generalizes from the follow-the-cursor task to handwriting, with connected learners producing letters closely resembling targets](virtual-teacher-generalizes-to-handwriting.md) — a narrower finding that bears on this claim
- [Performance variance is lower for virtual-teacher-guided learners and the advantage persists as learning progresses](virtual-teacher-lower-performance-variance.md) — related
- [Across a series of sessions, virtual-teacher-guided learners achieve significantly higher overall performance (AUC) than non-guided learners on both tasks](virtual-teacher-overall-performance-auc.md) — a narrower finding that bears on this claim
