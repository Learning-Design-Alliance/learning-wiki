---
type: claim
title: The GAIL-based virtual teacher generalizes from the follow-the-cursor task to handwriting, with connected learners producing letters closely resembling targets
description: The GAIL-based virtual teacher generalizes from the follow-the-cursor task to handwriting, with connected learners producing letters closely resembling targets
id: virtual-teacher-generalizes-to-handwriting
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: hadar-mulian-2024
    resource: "https://doi.org/10.1609/aaai.v38i21.30369"
    title: "Hadar Mulian, Segev Shlomov, Lior Limonad, Alessia Noccaro, Silvia Buscaglione. (2024). Mimicking the Maestro: Exploring the Efficacy of a Virtual AI Teacher in Fine Motor Skill Acquisition. [doi:10.1609/aaai.v38i21.30369](https://doi.org/10.1609/aaai.v38i21.30369)"
    author: Hadar Mulian, Segev Shlomov, Lior Limonad, Alessia Noccaro, Silvia Buscaglione
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The GAIL-based virtual teacher generalizes from the follow-the-cursor task to handwriting, with connected learners producing letters closely resembling targets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` On the WESL handwriting task, learners trained with the virtual teacher showed higher similarity and smaller variance than self-trained learners, whose letters lacked range and precision. [→ Hadar Mulian 2024](#hadar-mulian-2024)

## Evidence

### Hadar Mulian 2024

Hadar Mulian, Segev Shlomov, Lior Limonad, Alessia Noccaro, Silvia Buscaglione. (2024). Mimicking the Maestro: Exploring the Efficacy of a Virtual AI Teacher in Fine Motor Skill Acquisition. [doi:10.1609/aaai.v38i21.30369](https://doi.org/10.1609/aaai.v38i21.30369)

`q1 · i?` · `design · r2`

Numerical evaluation of learner performance on the WESL handwriting task (26 letter episodes) with low-high connectivity, shown in Figure 3. Contour plots showed connected learners' "silhouettes closely resembling the target letters" while the unconnected learner's curves "lacked both range and precision".

> "Results from the evaluation with the WESL task, with low-high modality, demonstrate a difference in similarity in favor of the connected settings, and overall a smaller variance in performance across all game units"

## Discussion


## Learner Variables
- [Writing Skills](../learner-variables/writing-skills.md) — outcome: measured as an outcome of the instruction studied

## Related Claims
- [The virtual teacher's benefit is robust across learner starting conditions, noise levels and session lengths, averaging 25.8% improvement on FC and 15.3% on WESL](virtual-teacher-robustness-across-settings.md) — a broader claim this one bears on
- [Performance variance is lower for virtual-teacher-guided learners and the advantage persists as learning progresses](virtual-teacher-lower-performance-variance.md) — related
- [Across a series of sessions, virtual-teacher-guided learners achieve significantly higher overall performance (AUC) than non-guided learners on both tasks](virtual-teacher-overall-performance-auc.md) — related
- [Learners guided by a virtual AI teacher perform significantly better after each learning session than learners learning independently, on synthetic RL learners](virtual-ai-teacher-session-performance-gain.md) — related
- [Learners guided by a virtual AI teacher acquire the motor skill significantly faster, reaching a competence threshold in fewer sessions than non-guided learners](virtual-teacher-faster-skill-acquisition.md) — related
