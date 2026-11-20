---
type: claim
title: Learners guided by a virtual AI teacher perform significantly better after each learning session than learners learning independently, on synthetic RL learners
description: Learners guided by a virtual AI teacher perform significantly better after each learning session than learners learning independently, on synthetic RL learners
id: virtual-ai-teacher-session-performance-gain
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

# Learners guided by a virtual AI teacher perform significantly better after each learning session than learners learning independently, on synthetic RL learners

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` After each game unit, guided learners achieved significantly higher Frechet distance than non-guided learners on the FC task (all p-values <0.05), and from the second game unit onwards on the WESL task. [→ Hadar Mulian 2024](#hadar-mulian-2024)

## Evidence

### Hadar Mulian 2024

Hadar Mulian, Segev Shlomov, Lior Limonad, Alessia Noccaro, Silvia Buscaglione. (2024). Mimicking the Maestro: Exploring the Efficacy of a Virtual AI Teacher in Fine Motor Skill Acquisition. [doi:10.1609/aaai.v38i21.30369](https://doi.org/10.1609/aaai.v38i21.30369)

`q1 · i?` · `causal · r1`

Simulation-based evaluation comparing RL-based (A2C) synthetic learners training with versus without an attached virtual teacher on the FC task, evaluated over game units with Frechet distance. Results were "consistent across all game units"; WESL task showed significant differences from the second game unit onwards.

> "Results for the FC task showed that the performance of a learner guided by a virtual teacher was significantly higher than the performance values of the non-guided learner, consistent across all game units (i.e., all p-values <0.05, see Table 2 in appendix)."

## Discussion


## Related Claims
- [Across a series of sessions, virtual-teacher-guided learners achieve significantly higher overall performance (AUC) than non-guided learners on both tasks](virtual-teacher-overall-performance-auc.md) — related
- [Learners guided by a virtual AI teacher acquire the motor skill significantly faster, reaching a competence threshold in fewer sessions than non-guided learners](virtual-teacher-faster-skill-acquisition.md) — related
- [Performance variance is lower for virtual-teacher-guided learners and the advantage persists as learning progresses](virtual-teacher-lower-performance-variance.md) — related
- [The virtual teacher's benefit is robust across learner starting conditions, noise levels and session lengths, averaging 25.8% improvement on FC and 15.3% on WESL](virtual-teacher-robustness-across-settings.md) — related
- [The GAIL-based virtual teacher generalizes from the follow-the-cursor task to handwriting, with connected learners producing letters closely resembling targets](virtual-teacher-generalizes-to-handwriting.md) — related
