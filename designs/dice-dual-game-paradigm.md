---
type: design
id: dice-dual-game-paradigm
title: Dice Dual zero-sum number-selection game with Pre/During/Post phase structure
description: "Dice Dual is a zero-sum competitive game in which \"both the participant and a computerized opponent select one number of a virtual 6-sided die on each trial\", with even or odd sums determining wins, counterbalanced ac..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-26
sources:
  - id: zhang-2026
    resource: "https://doi.org/10.1038/s41539-026-00414-w"
    title: "Zhang, Y., & Dyson, B. J. (2026). Recover or discover: How outcome feedback shapes response patterns within game spaces. npj Science of Learning. https://doi.org/10.1038/s41539-026-00414-w"
    author: "Zhang, Y., & Dyson, B. J"
---

# Dice Dual zero-sum number-selection game with Pre/During/Post phase structure

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Dice Dual is a zero-sum competitive game in which "both the participant and a computerized opponent select one number of a virtual 6-sided die on each trial", with even or odd sums determining wins, counterbalanced across participants. Each block contains Pre, During, and Post phases: exploitable opponent behaviour types (repetition, alternation) in Pre and Post, and an artificially fixed win rate in During. The authors used it across three experiments to index pattern acquisition, suppression, and reactivation via win rate and optimal behaviour rate (OBR).

## Design Implications

### Context
#### Requirements
- A computerized opponent with exploitable behaviour types (repetition or alternation) in Pre and Post phases
- A fixed win rate programmed in the During phase to simulate punishment or reinforcement
#### Constraints
- Punishment and reinforcement labels are descriptive of outcome valence, not formal operant conditioning or computational reinforcement learning mechanisms
- Phase transitions were covert, with no on-screen cues marking a new phase

### Target Learners
- Adult university students

### Learning Goals
- Strategic adaptation to opponent patterns under outcome feedback
- Balancing reuse of old response patterns with acquisition of new ones

### Claims
- [Relearning Old Beats Learning New Except Severe Punishment](../claims/relearning-old-beats-learning-new-except-severe-punishment.md) [+M]
- [Fixed Win Rate Reduces Obr](../claims/fixed-win-rate-reduces-obr.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zhang, Y., & Dyson, B. J. (2026). Recover or discover: How outcome feedback shapes response patterns within game spaces. npj Science of Learning. https://doi.org/10.1038/s41539-026-00414-w
