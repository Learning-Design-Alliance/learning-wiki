---
type: claim
title: Across a series of sessions, virtual-teacher-guided learners achieve significantly higher overall performance (AUC) than non-guided learners on both tasks
description: Across a series of sessions, virtual-teacher-guided learners achieve significantly higher overall performance (AUC) than non-guided learners on both tasks
id: virtual-teacher-overall-performance-auc
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

# Across a series of sessions, virtual-teacher-guided learners achieve significantly higher overall performance (AUC) than non-guided learners on both tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Guided learners' AUC of Frechet distance across game units was significantly higher than non-guided learners' on both FC and WESL tasks. [→ Hadar Mulian 2024](#hadar-mulian-2024)

## Evidence

### Hadar Mulian 2024

Hadar Mulian, Segev Shlomov, Lior Limonad, Alessia Noccaro, Silvia Buscaglione. (2024). Mimicking the Maestro: Exploring the Efficacy of a Virtual AI Teacher in Fine Motor Skill Acquisition. [doi:10.1609/aaai.v38i21.30369](https://doi.org/10.1609/aaai.v38i21.30369)

`q1 · i?` · `causal · r1`

H2 test: per repetition, AUC of Frechet distances across game units was computed for guided versus non-guided synthetic learners. FC: t = 6.58, p < 0.5 · 10−5; WESL was "also consistent for the WESL task" (t = 7.31, µ+AUC = 3.550, µ−AUC = 2.544, p < 0.5 · 10−5).

> "The result for the FC task showed that the overall performance of the guided learner as reflected by the corresponding AUC value was significantly higher than the performance of the non-guided learner ( t = 6 .58,µ+AU C= 4.971,µ−AU C= 2.975,p <0.5 · 10−5)."

## Discussion


## Related Claims
- [Learners guided by a virtual AI teacher perform significantly better after each learning session than learners learning independently, on synthetic RL learners](virtual-ai-teacher-session-performance-gain.md) — related
- [Learners guided by a virtual AI teacher acquire the motor skill significantly faster, reaching a competence threshold in fewer sessions than non-guided learners](virtual-teacher-faster-skill-acquisition.md) — related
- [The GAIL-based virtual teacher generalizes from the follow-the-cursor task to handwriting, with connected learners producing letters closely resembling targets](virtual-teacher-generalizes-to-handwriting.md) — related
- [Performance variance is lower for virtual-teacher-guided learners and the advantage persists as learning progresses](virtual-teacher-lower-performance-variance.md) — related
- [The virtual teacher's benefit is robust across learner starting conditions, noise levels and session lengths, averaging 25.8% improvement on FC and 15.3% on WESL](virtual-teacher-robustness-across-settings.md) — a broader claim this one bears on
