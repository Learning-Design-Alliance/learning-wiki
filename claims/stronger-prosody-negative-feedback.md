---
type: claim
title: Teachers express prosody more strongly (higher energy and loudness) during negative feedback than positive feedback
description: Teachers express prosody more strongly (higher energy and loudness) during negative feedback than positive feedback
id: stronger-prosody-negative-feedback
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: matilda-knierim-2024
    resource: "https://doi.org/10.1145/3678957.3685735"
    title: "Matilda Knierim, Sahil Jain, Murat Han Aydoğan, Kenneth Mitra, Kush Desai, Akanksha Saran, and Kim Baraka. (2024). Prosody as a Teaching Signal for Agent Learning: Exploratory Studies and Algorithmic Implications. INTERNATIONAL CONFERENCE ON MULTIMODAL INTERACTION (ICMI '24). https://doi.org/10.1145/3678957.3685735"
    author: Matilda Knierim, Sahil Jain, Murat Han Aydoğan, Kenneth Mitra, Kush Desai, Akanksha Saran, and Kim Baraka
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: matilda-knierim-2024-2
    resource: "https://doi.org/10.1145/3678957.3685735"
    title: "Matilda Knierim, Sahil Jain, Murat Han Aydoğan, Kenneth Mitra, Kush Desai, Akanksha Saran, and Kim Baraka. (2024). Prosody as a Teaching Signal for Agent Learning: Exploratory Studies and Algorithmic Implications. INTERNATIONAL CONFERENCE ON MULTIMODAL INTERACTION (ICMI '24). https://doi.org/10.1145/3678957.3685735"
    author: Matilda Knierim, Sahil Jain, Murat Han Aydoğan, Kenneth Mitra, Kush Desai, Akanksha Saran, and Kim Baraka
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Teachers express prosody more strongly (higher energy and loudness) during negative feedback than positive feedback

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the interactive RL study, energy and loudness differed significantly between "yes" and "no" utterances for 13 of 14 trainers, with louder, higher-energy negative feedback. [→ Matilda Knierim 2024](#matilda-knierim-2024)
`q2 i?` In the Atari demonstration study, energy and loudness measures were significantly higher for "no" than "yes" utterances across the games. [→ Matilda Knierim 2024 (2)](#matilda-knierim-2024-2)

## Evidence

### Matilda Knierim 2024

Matilda Knierim, Sahil Jain, Murat Han Aydoğan, Kenneth Mitra, Kush Desai, Akanksha Saran, and Kim Baraka. (2024). Prosody as a Teaching Signal for Agent Learning: Exploratory Studies and Algorithmic Implications. INTERNATIONAL CONFERENCE ON MULTIMODAL INTERACTION (ICMI '24). https://doi.org/10.1145/3678957.3685735

`q2 · i?` · `associational · r1`

T-test analyses per prosodic feature and participant in the Wizard-of-Oz interactive RL study (14 sessions). "Participants spoke louder and with higher energy when they gave negative feedback"; pitch showed a less clear distinction (7 of 14 trainers significant).

> "energy and loudness have 13 out of 14 significant differences between the prosodic features of the feedback word "yes" and "no". This highlights that participants spoke louder and with higher energy when they gave negative feedback to the agent."

### Matilda Knierim 2024 (2)

Matilda Knierim, Sahil Jain, Murat Han Aydoğan, Kenneth Mitra, Kush Desai, Akanksha Saran, and Kim Baraka. (2024). Prosody as a Teaching Signal for Agent Learning: Exploratory Studies and Algorithmic Implications. INTERNATIONAL CONFERENCE ON MULTIMODAL INTERACTION (ICMI '24). https://doi.org/10.1145/3678957.3685735

`q2 · i?` · `associational · r1`

Prosodic feature analysis of a single demonstrator's utterances in three Atari games, with a 0.5-second buffer around each utterance. Energy and loudness measures were significantly higher for "no" utterances (p < 0.05), except maximum loudness during Space Invaders.

> "We find that mean energy, maximum energy, total energy, mean loudness, and maximum loudness are significantly higher (𝑝 < 0.05) for negative feedback ("no") compared to positive feedback ("yes") for all the games (except maximum loudness during Space Invaders)."

## Discussion


## Related Claims
- [In speech-augmented demonstrations, mean pitch correlates with reward magnitude: higher-pitch \"yes\" utterances accompany higher returns and higher-pitch \"no\" utterances lower returns](pitch-correlates-reward-magnitude-demonstrations.md) — related
- [Human teachers give significantly more positive than negative feedback when teaching agents in both interactive RL and demonstration settings](positive-feedback-bias-teaching-agents.md) — related
- [Prosodic features of teacher feedback correlate with the advantage function at the individual level but not at the population level](prosody-advantage-correlation-individual-level.md) — related
- [Prosody-augmented TAMER statistically significantly outperformed speech-content-only TAMER for three of four participants in offline evaluation](prosody-augmented-tamer-outperforms-baseline.md) — related
