---
type: claim
title: "MAMCR fails to replicate for large FCI samples: Infomap with LANS sparsification consistently identified only one large community of incorrect answers"
description: "MAMCR fails to replicate for large FCI samples: Infomap with LANS sparsification consistently identified only one large community of incorrect answers"
id: mamcr-fails-large-fci-samples
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: james-wells-2019
    resource: "https://doi.org/10.1103/physrevphyseducres.15.020122"
    title: "James Wells, Rachel Henderson, John Stewart, Gay Stewart, Jie Yang, and Adrienne Traxler. (2019). Exploring the Structure of Misconceptions in the Force Concept Inventory with Modified Module Analysis. [doi:10.1103/physrevphyseducres.15.020122](https://doi.org/10.1103/physrevphyseducres.15.020122)"
    author: James Wells, Rachel Henderson, John Stewart, Gay Stewart, Jie Yang, and Adrienne Traxler
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: james-wells-2019-2
    resource: "https://doi.org/10.1103/physrevphyseducres.15.020122"
    title: "James Wells, Rachel Henderson, John Stewart, Gay Stewart, Jie Yang, and Adrienne Traxler. (2019). Exploring the Structure of Misconceptions in the Force Concept Inventory with Modified Module Analysis. [doi:10.1103/physrevphyseducres.15.020122](https://doi.org/10.1103/physrevphyseducres.15.020122)"
    author: James Wells, Rachel Henderson, John Stewart, Gay Stewart, Jie Yang, and Adrienne Traxler
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# MAMCR fails to replicate for large FCI samples: Infomap with LANS sparsification consistently identified only one large community of incorrect answers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Applying Infomap with LANS sparsification to the large sample's incorrect-response networks failed to identify meaningful community structure, consistently identifying only one large community. [→ James Wells 2019](#james-wells-2019)
`q2 i?` Subsampling to 143 students to match Study 1 did not restore the original structure: Infomap identified one community in 100% of runs without sparsification and 92% of runs with an N/10 edge-weight threshold. [→ James Wells 2019 (2)](#james-wells-2019-2)

## Evidence

### James Wells 2019

James Wells, Rachel Henderson, John Stewart, Gay Stewart, Jie Yang, and Adrienne Traxler. (2019). Exploring the Structure of Misconceptions in the Force Concept Inventory with Modified Module Analysis. [doi:10.1103/physrevphyseducres.15.020122](https://doi.org/10.1103/physrevphyseducres.15.020122)

`q2 · i?` · `associational · r2`

Replication attempt applying the original MAMCR pipeline (LANS sparsification followed by Infomap community detection) to the large sample's incorrect-response networks; the article reports the attempt "failed to identify meaningful community structure", with Infomap finding only one community.

> "Applying Infomap with LANS sparsiﬁcation failed to identify meaningful community structure for the large data set in the current study; Infomap consistently identiﬁed only one large community."

### James Wells 2019 (2)

James Wells, Rachel Henderson, John Stewart, Gay Stewart, Jie Yang, and Adrienne Traxler. (2019). Exploring the Structure of Misconceptions in the Force Concept Inventory with Modified Module Analysis. [doi:10.1103/physrevphyseducres.15.020122](https://doi.org/10.1103/physrevphyseducres.15.020122)

`q2 · i?` · `associational · r2`

Sample-size probe drawing 100 subsamples of 143 students to match Study 1's sample size; Infomap identified one community "100% of the time with no sparsiﬁcation" and 92% of the time with an N/10 edge-weight threshold.

> "Applying Infomap using "R" identiﬁed only one community 100% of the time with no sparsiﬁcation and one community 92% of the time with the requirement the edge weight be at least N/10 where N is the number of students."

## Discussion


## Related Claims
- [FCI incorrect-answer communities divide into two classes: those from consistently applied incorrect reasoning (misconceptions) and those from the blocked structure of items sharing a common stem](fci-incorrect-communities-blocking-versus-misconceptions.md) — related
- [Relaxing sparsification thresholds did not merge FCI misconceptions into a coherent non-Newtonian framework; they appear to exist relatively independently as small groups of consistent answers](fci-misconceptions-independent-small-groups.md) — related
- [Modified Module Analysis identified 9 groups of incorrect FCI answers on the pretest and 11 on the post-test, in most cases mappable to common misconceptions](mma-identifies-incorrect-answer-groups.md) — reports the opposite
- [Module analysis (MAMCR) of correct PIQL responses identifies modules that differ across course stages and mix all three PQL constructs](mamcr-modules-differ-across-course-stages.md) — related
- [Infomap community structure matches the curriculum's block organization exactly for Mathematics and partially for Physics and the integrated network](infomap-communities-match-curriculum-blocks.md) — related
