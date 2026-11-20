---
type: claim
title: Learners guided by a virtual AI teacher acquire the motor skill significantly faster, reaching a competence threshold in fewer sessions than non-guided learners
description: Learners guided by a virtual AI teacher acquire the motor skill significantly faster, reaching a competence threshold in fewer sessions than non-guided learners
id: virtual-teacher-faster-skill-acquisition
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

# Learners guided by a virtual AI teacher acquire the motor skill significantly faster, reaching a competence threshold in fewer sessions than non-guided learners

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Guided learners reached the Frechet-distance threshold in significantly fewer game units than non-guided learners on both the FC task (µ+θ = 4.307 vs µ−θ = 9.692) and the WESL task (µ+θ = 3.3 vs µ−θ = 10.0). [→ Hadar Mulian 2024](#hadar-mulian-2024)

## Evidence

### Hadar Mulian 2024

Hadar Mulian, Segev Shlomov, Lior Limonad, Alessia Noccaro, Silvia Buscaglione. (2024). Mimicking the Maestro: Exploring the Efficacy of a Virtual AI Teacher in Fine Motor Skill Acquisition. [doi:10.1609/aaai.v38i21.30369](https://doi.org/10.1609/aaai.v38i21.30369)

`q1 · i?` · `causal · r1`

H3 test: for each repetition, the first game unit in which the learner exceeded a threshold Frechet distance (θFC = 0.9; θWESL = 0.75) was compared between guided and non-guided synthetic learners. WESL result: t = 15.84, p < 0.5 · 10−10.

> "the result for the FC task showed that the motor skill was acquired significantly faster by the guided learner compared to the number of game units the motor skill was acquired by the non-guided learner ( t = 6 .20,µ+θ = 4 .307,µ−θ = 9.692,p <0.5 · 10−5)."

## Discussion


## Related Claims
- [Learners guided by a virtual AI teacher perform significantly better after each learning session than learners learning independently, on synthetic RL learners](virtual-ai-teacher-session-performance-gain.md) — related
- [Across a series of sessions, virtual-teacher-guided learners achieve significantly higher overall performance (AUC) than non-guided learners on both tasks](virtual-teacher-overall-performance-auc.md) — related
- [Performance variance is lower for virtual-teacher-guided learners and the advantage persists as learning progresses](virtual-teacher-lower-performance-variance.md) — related
- [The virtual teacher's benefit is robust across learner starting conditions, noise levels and session lengths, averaging 25.8% improvement on FC and 15.3% on WESL](virtual-teacher-robustness-across-settings.md) — related
- [Novices using a remote-controlled camera holder reach competency in the peg transfer task significantly faster than novices with a human camera assistant](rch-faster-competency-peg-transfer.md) — related
- [The GAIL-based virtual teacher generalizes from the follow-the-cursor task to handwriting, with connected learners producing letters closely resembling targets](virtual-teacher-generalizes-to-handwriting.md) — related
