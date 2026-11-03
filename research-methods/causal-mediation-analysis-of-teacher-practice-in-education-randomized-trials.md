---
type: research-method
id: causal-mediation-analysis-of-teacher-practice-in-education-randomized-trials
moved_from: [theory/rct-teacher-practice-mediation-model]
title: Causal mediation analysis of teacher practice in education randomized trials
description: "The report defines a mediator as \"an intermediate outcome that is measured after random assignment and that can be affected by the treatment.\" Its Figure 2.1 path model posits that intervention services improve teacher knowledge, which improves teacher practices, which improve student test scores, w"
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: schochet-2009
    resource: "https://www.mathematica.org/publications/do-typical-rcts-of-education-interventions-have-sufficient-statistical-power-for-linking-impacts-on-teacher-practice-and-student-achievement-outcomes"
    title: "Schochet, Peter Z. (2009). Do Typical RCTs of Education Interventions Have Sufficient Statistical Power for Linking Impacts on Teacher Practice and Student Achievement Outcomes? (NCEE 2009-4065). Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. https://www.mathematica.org/publications/do-typical-rcts-of-education-interventions-have-sufficient-statistical-power-for-linking-impacts-on-teacher-practice-and-student-achievement-outcomes"
    author: Schochet, Peter Z
---

# Causal mediation analysis of teacher practice in education randomized trials

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 causal, 1 theoretical), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The report defines a mediator as "an intermediate outcome that is measured after random assignment and that can be affected by the treatment." Its Figure 2.1 path model posits that intervention services improve teacher knowledge, which improves teacher practices, which improve student test scores, with an optional direct path d bypassing the teacher. The empirical focus is path ab (treatment effect on teacher practices) and path c, the "mediator effect" linking teacher practices to achievement. Teacher practice mediators are emphasized because they are expensive to collect and are key intermediate outcomes in the causal chain.

## Accounts
<!-- How each source describes or uses the method -->
- **Conceptual model of teacher practice mediation in education RCTs**: The report defines a mediator as "an intermediate outcome that is measured after random assignment and that can be affected by the treatment." Its Figure 2.1 path model posits that intervention services improve teacher knowledge, which improves teacher practices, which improve student test scores, with an optional direct path d bypassing the teacher. The empirical focus is path ab (treatment effect on teacher practices) and path c, the "mediator effect" linking teacher practices to achievement. Teacher practice mediators are emphasized because they are expensive to collect and are key intermediate outcomes in the causal chain. (Schochet (2009))
- **Base mediation modeling on theory and use sensitivity analysis for omitted variables**: The article argues that omitted variables causing both mediator and outcome bias Paths b and c′ and can mask full mediation, so "statistical modeling should be based on theory and informed by prior research." It frames causal mediation as "a tool for evaluating the extent to which a conceptual model grounded in theory is supported by sample data," and recommends sensitivity analysis to evaluate the potential that a model has omitted variables. Randomization protects Paths a and c from this bias but not b and c′. (Greg Roberts et al. (2018))
- **Mediational analysis framework for unpacking the zero effect of comprehensive teacher induction programs**: The article proposes a mediational framework that treats mentoring content and activities as potential mediators of induction program effects on teaching practices. It uses the ratio-of-mediator-probability weighting (RMPW) method to decompose the total effect into a natural indirect effect channeled through program-induced change in a mediator and a natural direct effect. The RMPW method allows the mentoring effect on the outcome to differ across treatment conditions without assuming a functional form for the outcome model, a strength the authors say is not shared by structural equation modeling. (Hong et al. (2013))

### Claims
- [Mediator-outcome association analyses can identify teacher practice mediators most associated with student learning](../claims/mediator-analyses-identify-key-teacher-practices.md) [+W]
- [The zero effect of CTI programs cannot be attributed to lower participation rates, as treatment teachers participated at an equal or higher rate than control teachers](../claims/cti-zero-effect-not-due-to-low-participation.md) [+M]

## Related Research Methods

- [Mediator–moderator distinction in randomized intervention research](mediatormoderator-distinction-in-randomized-intervention-research.md)

## Key Sources
- Schochet, Peter Z. (2009). Do Typical RCTs of Education Interventions Have Sufficient Statistical Power for Linking Impacts on Teacher Practice and Student Achievement Outcomes? (NCEE 2009-4065). Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. https://www.mathematica.org/publications/do-typical-rcts-of-education-interventions-have-sufficient-statistical-power-for-linking-impacts-on-teacher-practice-and-student-achievement-outcomes
<!-- merged 2026-10-10 from theories/rct-teacher-practice-mediation-model ("Conceptual model of teacher practice mediation in education RCTs"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Greg Roberts, Nancy Scammacca, and Garrett J. Roberts. (2018). Causal Mediation in Educational Intervention Studies. Behavioral Disorders, 43(4), 457–465. https://doi.org/10.1177/0198742917749560
- Hong, Y., & Hong, G. (2013). Making Sense of the “Zero Effect” of Comprehensive Teacher Induction Programs: A Mediational Analysis. SREE Spring 2013 Conference.

# Conceptual model of teacher practice mediation in education RCTs

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The report defines a mediator as "an intermediate outcome that is measured after random assignment and that can be affected by the treatment." Its Figure 2.1 path model posits that intervention services improve teacher knowledge, which improves teacher practices, which improve student test scores, with an optional direct path d bypassing the teacher. The empirical focus is path ab (treatment effect on teacher practices) and path c, the "mediator effect" linking teacher practices to achievement. Teacher practice mediators are emphasized because they are expensive to collect and are key intermediate outcomes in the causal chain.

## Design Implications

### Context
#### Requirements
- Mediator data must be collected for both treatment and control groups after random assignment
- The analysis assumes a single teacher practice mediator at a time, with the teacher knowledge chain subsumed in the practice chain
#### Constraints
- The report does not consider structural equation, path, or latent variable models, so results may not pertain to those approaches
- Mediators measuring the quality or amount of intervention services received are excluded from the empirical analysis

### Target Learners
- elementary school students in low performing schools

### Target Learning Objectives
- student academic achievement as measured by test score gains

### Claims

- [Mediator-outcome association analyses can identify teacher practice mediators most associated with student learning](../claims/mediator-analyses-identify-key-teacher-practices.md) [+W]

## Related Theories

- [Statistical power formulas for linking teacher practice mediators to student outcomes in clustered school-based RCTs](../research-methods/precision-based-sample-size-planning-for-clustered-education-trials.md)

## Examples
-

## Key Sources
- Schochet, Peter Z. (2009). Do Typical RCTs of Education Interventions Have Sufficient Statistical Power for Linking Impacts on Teacher Practice and Student Achievement Outcomes? (NCEE 2009-4065). Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. https://www.mathematica.org/publications/do-typical-rcts-of-education-interventions-have-sufficient-statistical-power-for-linking-impacts-on-teacher-practice-and-student-achievement-outcomes
-->
