---
type: claim
title: LFA identifies over-taught and under-taught skills, and split skills can hide under-practiced subskills such as CMsegment
description: LFA identifies over-taught and under-taught skills, and split skills can hide under-practiced subskills such as CMsegment
id: lfa-identifies-overtaught-undertught-skills
status: review
generated:
  by: claude/unspecified
  at: 2026-11-27
evidence_strength: moderate
newest_evidence: 2006
recheck_by: 2009
sources:
  - id: cen-et-al-2006
    resource: "https://doi.org/10.1007/11774303_17"
    title: "Hao Cen, Kenneth Koedinger, Brian Junker. (2006). Learning Factors Analysis – A General Method for Cognitive Model Evaluation and Improvement. https://doi.org/10.1007/11774303_17"
    author: Hao Cen, Kenneth Koedinger, Brian Junker
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: cen-et-al-2006-2
    resource: "https://doi.org/10.1007/11774303_17"
    title: "Hao Cen, Kenneth Koedinger, Brian Junker. (2006). Learning Factors Analysis – A General Method for Cognitive Model Evaluation and Improvement. https://doi.org/10.1007/11774303_17"
    author: Hao Cen, Kenneth Koedinger, Brian Junker
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LFA identifies over-taught and under-taught skills, and split skills can hide under-practiced subskills such as CMsegment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2006 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2009**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Parallelogram-side is over-practiced (initial success probability .94, about 14.9 practices per student) so practice can be reduced, while Trapezoid-height (initial probability .29, final .69) needs more practice to reach mastery. [→ Cen et al. 2006](#cen-et-al-2006)
`q2 i?` After splitting Compose-by-multiplication, CMsegment has final probability only .60 with less than 2 average practices, so knowledge tracing on the original unsplit rule may release students before they master CMsegment. [→ Cen et al. 2006 (2)](#cen-et-al-2006-2)

## Evidence

### Cen et al. 2006

Hao Cen, Kenneth Koedinger, Brian Junker. (2006). Learning Factors Analysis – A General Method for Cognitive Model Evaluation and Improvement. https://doi.org/10.1007/11774303_17

`q2 · i?` · `associational · r2`

Combining Experiments 1–3, the article examines per-skill practice statistics: Parallelogram-side has intercept 2.06, slope -.01, initial probability .94 and 14.9 average practices; Trapezoid-height has intercept -1.55, slope .27, initial probability .29, final probability .69 and 4.2 average practices.

> "Much practice spent on an easy skill is not a good use of student time. Reducing the amount of practice for this skill should save student time without compromising their performance."

### Cen et al. 2006 (2)

Hao Cen, Kenneth Koedinger, Brian Junker. (2006). Learning Factors Analysis – A General Method for Cognitive Model Evaluation and Improvement. https://doi.org/10.1007/11774303_17

`q2 · i?` · `design · r2`

Analysis of Table 9 statistics for Compose-by-multiplication before and after split: CM has final probability .92, CMarea .96, but CMsegment .60 with 1.9 average practice opportunities. With the LFA model, the article argues knowledge tracing could catch weakness in acquiring CMsegment.

> "But CMsegment has final probability only .60 and an average amount of practice less than 2. The knowledge-tracing algorithm in the tutor may let the student go after he reaches the mastery on Compose-by-addition in the original model."

## Discussion


## Related Claims
- [LFA detects hidden knowledge components as learning-curve blips without visual inspection, as in the Compose-by-multiplication split](lfa-detects-hidden-blip-cm-split.md) — related
- [Fitting the extended power-law logistic model yields per-skill initial difficulty and learning rates, with Pentagon-area hardest and Parallelogram-area easiest](lfa-skill-difficulty-learning-rates.md) — related
