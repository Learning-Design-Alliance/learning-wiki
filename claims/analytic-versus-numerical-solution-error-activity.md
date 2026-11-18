---
type: claim
title: Comparing analytic with Euler and Euler-Cromer numerical solutions led students to quantify iteration error, which affected position but not velocity
description: Comparing analytic with Euler and Euler-Cromer numerical solutions led students to quantify iteration error, which affected position but not velocity
id: analytic-versus-numerical-solution-error-activity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-16
evidence_strength: weak
newest_evidence: 2010
sources:
  - id: rui-gomes-neves-2010
    resource: "https://doi.org/10.48550/arXiv.1006.4662"
    title: "Rui Gomes Neves, Jorge Carvalho Silva & Vítor Duarte Teodoro. (2010). Computational Modelling with Modellus: An Enhancement Vector for the General University Physics Course. [doi:10.48550/arXiv.1006.4662](https://doi.org/10.48550/arXiv.1006.4662)"
    author: "Rui Gomes Neves, Jorge Carvalho Silva & Vítor Duarte Teodoro"
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: rui-gomes-neves-2010-2
    resource: "https://doi.org/10.48550/arXiv.1006.4662"
    title: "Rui Gomes Neves, Jorge Carvalho Silva & Vítor Duarte Teodoro. (2010). Computational Modelling with Modellus: An Enhancement Vector for the General University Physics Course. [doi:10.48550/arXiv.1006.4662](https://doi.org/10.48550/arXiv.1006.4662)"
    author: "Rui Gomes Neves, Jorge Carvalho Silva & Vítor Duarte Teodoro"
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Comparing analytic with Euler and Euler-Cromer numerical solutions led students to quantify iteration error, which affected position but not velocity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`
> **Currency** · newest study 2010 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` For the same applied forces and initial conditions, students found the analytic solution differed from the numerical solutions obtained with the Euler and Euler-Cromer methods, learned there is always an error from the iterative approximations, and quantified it for both methods. [→ Rui Gomes Neves 2010](#rui-gomes-neves-2010)
`q1 i?` The activity showed students that the error is present only for the position and not for the velocity, since velocity changes linearly with time. [→ Rui Gomes Neves 2010 (2)](#rui-gomes-neves-2010-2)

## Evidence

### Rui Gomes Neves 2010

Rui Gomes Neves, Jorge Carvalho Silva & Vítor Duarte Teodoro. (2010). Computational Modelling with Modellus: An Enhancement Vector for the General University Physics Course. [doi:10.48550/arXiv.1006.4662](https://doi.org/10.48550/arXiv.1006.4662)

`q1 · i?` · `design · r2`

Classroom activity in §3.4 comparing analytic and numerical solutions of projectile motion (Fig. 7). Students learned that "there is always an error associated with the iterative approximations used" and how to quantify it for both methods; no quantitative error values are printed.

> "For the same sum of applied forces and the same initial conditions students were lead to ﬁnd that the analytic solution is diﬀerent from the numerical solutions."

### Rui Gomes Neves 2010 (2)

Rui Gomes Neves, Jorge Carvalho Silva & Vítor Duarte Teodoro. (2010). Computational Modelling with Modellus: An Enhancement Vector for the General University Physics Course. [doi:10.48550/arXiv.1006.4662](https://doi.org/10.48550/arXiv.1006.4662)

`q1 · i?` · `design · r2`

Continuation of the same analytic-versus-numerical comparison activity in §3.4, reported as a finding of the activity about which quantities carry the iteration error.

> "The activity showed students that the error is only present for the position and not for the velocity, since this quantity changes linearly with time."

## Discussion


## Related Claims
- [Only the well-specified text-only prompt produced a correct quantitative result from o4-mini, while underspecified prompts led to numerical errors and misleading final results](prompt-specificity-shapes-lrm-physics-solution-correctness.md) — related
- [Multimodal prompts caused o4-mini to skip numerical integration and produce only qualitative final responses despite recovering much of the analytical structure](multimodal-prompts-cause-skipped-numerical-integration.md) — related
- [MAPS-guided critique preparation led students to identify more expert-aligned weaknesses in an AI solution than independent problem-solving preparation](maps-guided-critique-supports-expert-aligned-evaluation-of-ai-solutions.md) — related
- [The spring exercise lets students demonstrate interactively that the half-cycle time of harmonic motion does not depend on amplitude, even under Euler-Cromer integration](spring-exercise-period-amplitude-independence.md) — related
