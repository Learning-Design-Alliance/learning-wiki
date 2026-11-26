---
type: claim
title: On simulated conjunctive data, CFM-PMLE was as good as or better than AFM-PMLE in mean cross-validation error, with the largest gap when all skill probabilities were high (.9, .9, .9)
description: On simulated conjunctive data, CFM-PMLE was as good as or better than AFM-PMLE in mean cross-validation error, with the largest gap when all skill probabilities were high (.9, .9, .9)
id: cfm-beats-afm-simulated-conjunctive-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
evidence_strength: moderate
newest_evidence: 2008
recheck_by: 2011
sources:
  - id: cen-et-al-2008
    resource: "https://doi.org/10.1007/978-3-540-69132-7_111"
    title: "Hao Cen, Kenneth Koedinger, and Brian Junker. (2008). Comparing Two IRT Models for Conjunctive Skills. ITS 2008, LNCS 5091, pp. 796–798. https://doi.org/10.1007/978-3-540-69132-7_111"
    author: Hao Cen, Kenneth Koedinger, and Brian Junker
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# On simulated conjunctive data, CFM-PMLE was as good as or better than AFM-PMLE in mean cross-validation error, with the largest gap when all skill probabilities were high (.9, .9, .9)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2008 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2011**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In nearly all simulated conjunctive conditions, CFM-PMLE achieved equal or lower mean cross-validation error than AFM-PMLE. [→ Cen et al. 2008](#cen-et-al-2008)
`q2 i?` The biggest difference favored CFM for the skill set (.9, .9, .9), where AFM-P cannot behave in a conjunctive form. [→ Cen et al. 2008](#cen-et-al-2008)

## Evidence

### Cen et al. 2008

Hao Cen, Kenneth Koedinger, and Brian Junker. (2008). Comparing Two IRT Models for Conjunctive Skills. ITS 2008, LNCS 5091, pp. 796–798. https://doi.org/10.1007/978-3-540-69132-7_111

`q2 · i?` · `associational · r2`

Simulation study drawing data from a CFM model with 100 student parameters, 3 skill parameters, and 7 items, across four skill probability sets. The authors report that "In nearly all cases, CFM-PMLE was as good as or better than AFM-PMLE in cross validation"; Table 1 shows CVMean 0.111 for CFM-P versus 0.120 for AFM-P in one condition.

> "In nearly all cases, CFM-PMLE was as good as or better than AFM-PMLE in cross validation. The biggest difference was from the skill set (.9, .9, .9) because the skill parameter values are so high that AFM-P cannot behave in a conjunctive form"

## Discussion


## Related Claims
- [On the real EAPS algebra dataset, CFM-P was not clearly better than AFM-P, and AFM-P essentially performed as a conjunctive model through negative skill estimates](afm-acts-conjunctive-eaps-real-data.md) — related
- [No single learner model was best across the six datasets, justifying a broad multi-model approach](no-single-learner-model-best-across-datasets.md) — a broader claim this one bears on
