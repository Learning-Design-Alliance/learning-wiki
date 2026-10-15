---
type: claim
title: "The association between RT propensity and learning rate is moderated by prior proficiency: slower propensities predict greater learning efficiency for higher-proficiency students but are weakly negative for lower-proficiency students"
description: "The association between RT propensity and learning rate is moderated by prior proficiency: slower propensities predict greater learning efficiency for higher-proficiency students but are weakly negative for lower-prof..."
id: rt-propensity-proficiency-interaction-learning
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: interaction-1
    title: interaction-1
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: interaction-2
    title: interaction-2
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The association between RT propensity and learning rate is moderated by prior proficiency: slower propensities predict greater learning efficiency for higher-proficiency students but are weakly negative for lower-proficiency students

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 associational `r2` · `q2`

## Subclaims
`q2 i?` There is a significant RT propensity × prior proficiency interaction predicting learning rate (β = 0.11, p = .004), with longer RT propensities associated with steeper opportunity slopes among higher-proficiency students and weakly negative among lower-proficiency students. [→ interaction-1](#interaction-1)
`q2 i?` The interaction remains significant in a sensitivity analysis excluding potentially influential observations (β = 0.147, p = .014). [→ interaction-2](#interaction-2)

## Evidence

### interaction-1

Conrad Borchers, Lijin Zhang, Kexin Yang, Tomohiro Nagashima, and Benjamin W. Domingue. 2026. Understanding Student Effort Using Response-Time Propensities During Problem Solving. Proceedings of the Thirteenth ACM Conference on Learning @ Scale (L@S '26). https://doi.org/10.1145/3774398.3811624

`q2 · i?` · `associational · r2`

Linear regression on student-level parameters from the eight algebra tutoring deployments (794 students), predicting iAFM learning-rate slopes from RT propensity, prior proficiency, and their interaction. The article reports the interaction at "𝛽= 0.11" and interprets slower propensities as constructive processing for higher-proficiency students.

> "Critically, there is a significant RT propensity× prior proficiency interaction (𝛽= 0.11, 95% CI[0.03, 0.18], 𝑝=. 004; Table 4), indicating that the association between RT propensity and learning rate differs by students' baseline proficiency."

### interaction-2

Conrad Borchers, Lijin Zhang, Kexin Yang, Tomohiro Nagashima, and Benjamin W. Domingue. 2026. Understanding Student Effort Using Response-Time Propensities During Problem Solving. Proceedings of the Thirteenth ACM Conference on Learning @ Scale (L@S '26). https://doi.org/10.1145/3774398.3811624

`q2 · i?` · `associational · r2`

Sensitivity analysis re-estimating the interaction model after excluding flagged influential cases (98/787, 12.5%). The interaction "remained significant (𝛽= 0.147, p = .014)", addressing the influence of a small cluster of slow-responding students with low learning rates.

> "We flagged potentially influen-tial observations (Cook's D > 4/N, leverage > 2p/N, or |studentized residual| > 3) and re-estimated the model excluding these cases (98/787, 12.5%). The RT propensity–prior proficiency interaction remained significant (𝛽= 0.147, p = .014)."

## Discussion


## Related Claims
- [Higher prior proficiency is associated with faster step-level response-time propensities](higher-proficiency-faster-step-responses.md) — related
- [RT propensity shows no reliable main effect on learning rate, while prior proficiency is positively associated with learning rate](no-main-effect-rt-propensity-learning-rate.md) — related
- [The RT propensity–learning relationship is strongest early in the class session and attenuates later](rt-learning-relationship-strongest-early-session.md) — related
- [Response-time propensities show moderate to strong within-student stability across practice session slices](rt-propensities-moderate-strong-stability.md) — related
- [Baseline interaction quality moderates component-outcome relations, with strongest relations for teachers with the lowest baseline quality](baseline-quality-moderates-component-relations.md) — related
