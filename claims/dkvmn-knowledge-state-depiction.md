---
type: claim
title: "DKVMN can depict a student's changing mastery state of individual concepts over a practice sequence"
description: "DKVMN can depict a student's changing mastery state of individual concepts over a practice sequence"
id: dkvmn-knowledge-state-depiction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
evidence_strength: weak
newest_evidence: 2017
recheck_by: 2020
sources:
  - id: zhang-et-al-2017
    resource: "https://doi.org/10.1145/3038912.3052580"
    title: "Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. WWW 2017, Perth, Australia. https://doi.org/10.1145/3038912.3052580"
    author: Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DKVMN can depict a student's changing mastery state of individual concepts over a practice sequence

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` By reading the value matrix with a one-hot correlation weight, DKVMN outputs a per-concept mastery level; in a worked example, after 50 exercises the student is shown to have mastered the second, third and fourth concepts but not the fifth. [→ Zhang et al. 2017](#zhang-et-al-2017)

## Evidence

### Zhang et al. 2017

Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. WWW 2017, Perth, Australia. https://doi.org/10.1145/3038912.3052580

`q2 · i?` · `design · r2`

Knowledge-state depiction demonstrated on a single student's 50-exercise sequence (Figure 6): concept states rise after correct answers and fall after incorrect ones, e.g. the third concept's state decreases after the fourth exercise is answered incorrectly. This is an illustrative case, not a controlled evaluation.

> "After answering 50 exercises, the student is shown to have mastered the second, third, and fourth concepts but failed to understand the fifth concept"

## Discussion


## Related Claims
- [DKVMN's correlation weights automatically discover underlying concepts of exercises without expert annotation](dkvmn-automatic-concept-discovery.md) — related
- [Posttest predictability of all algorithms varies by skill, with all algorithms struggling on Complete the Sequence and mean-DKVMN best on Decimal Addition](skill-specific-posttest-correlations-vary.md) — related
