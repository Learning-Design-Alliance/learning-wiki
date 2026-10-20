---
type: claim
title: "Mastery learning effects are larger with a higher mastery standard, group-based pacing, local tests, and less feedback for the comparison group"
description: "In a multiple regression over 103 studies, larger effects went with group-based rather than self-paced programs, higher unit mastery standards, locally developed rather than standardized criterion tests, and comparison groups that received less quiz feedback; social-science courses showed larger effects than mathematics and natural science."
id: mastery-learning-effects-vary-with-standard-pacing-and-test-type
status: review
generated:
  by: claude/unspecified
  at: 2026-10-13
evidence_strength: moderate
sources:
  - id: kulik-et-al-1990
    resource: "https://doi.org/10.3102/00346543060002265"
    title: "Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of Mastery Learning Programs: A Meta-Analysis. *Review of Educational Research, 60*(2), 265–299. [doi:10.3102/00346543060002265](https://doi.org/10.3102/00346543060002265)"
    author: "Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L."
    q: 4
    i: "?"
    n: 103 studies
    kind: quant-synthesis
    rigour: "?"
---

# Mastery learning effects are larger with a higher mastery standard, group-based pacing, local tests, and less feedback for the comparison group

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r?` · `q4` · n=103 studies

Which features of a mastery learning program, and of the evaluation, go with larger achievement effects.

## Subclaims

`q4 i?` In a multiple regression over 103 studies, larger effects went with group-based rather than self-paced programs, higher unit mastery standards, locally developed rather than standardized criterion tests, and comparison groups that received less quiz feedback; social-science courses showed larger effects than mathematics and natural science. [→ Kulik et al. 1990](#kulik-et-al-1990)

## Evidence

### Kulik et al. 1990

Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of Mastery Learning Programs: A Meta-Analysis. *Review of Educational Research, 60*(2), 265–299. [doi:10.3102/00346543060002265](https://doi.org/10.3102/00346543060002265)

`q4 · meta-analysis (moderator regression over 103 studies)` · `i? · moderator coefficients, no single effect size for the finding` · `n=103 studies` · `quant-synthesis · r?`

The authors regressed study effect sizes on program and design features. Group-based programs produced larger effects than self-paced ones; programs with a high unit mastery standard (the percentage correct required before moving on) beat programs with lower standards; effects measured on locally developed tests were larger than on standardized commercial tests (in four studies with both, standardized effects were near zero, from -0.05 to 0.09, against local effects up to 0.64); and effects were smaller where the comparison group received as much quiz feedback as the mastery group. Group-based social-science courses with a high standard averaged 0.89 SD on local tests and 0.76 on standardized ones.

> "First, group-based programs produced larger effects than did self-paced ones. Second, programs with a high mastery standard were more effective than programs with lower standards. Third, programs whose effects were measured on locally developed tests produced larger effects than did programs whose effects were measured on standardized, commercial tests. Fourth, effects were larger in studies in which control groups received less quiz feedback than did experimental groups."

## Studies bearing on this claim

<!-- synthesis:start -->
*Self-paced or group-paced progression through small units, at what criterion, measured how?* This table gathers the studies behind this claim and the 4 narrower claims that bear on it: **6 distinct studies** (5 quant-synthesis, 1 causal), `q2`–`q4`, 4 of 6 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Kulik et al. 1990](https://doi.org/10.3102/00346543060002265) | q4 · quant-synthesis · r? | i? | this claim; [Self-paced mastery programs (PSI) reduce college course completion, though not by enough t](self-paced-mastery-programs-reduce-college-course-completion.md) (supports) |
| [Hasler et al. 2007](https://doi.org/10.1002/acp.1345) | q3 · causal · r? | i? | [Letting learners pace instruction helped on complex material in one experiment, while lear](learner-paced-beats-system-paced-complex-material.md) (qualifies) |
| [Karich et al. 2014](https://doi.org/10.3102/0034654314526064) | q3 · quant-synthesis · r? | i0 · negligible overall effect, g=0.05 | [Letting learners pace instruction helped on complex material in one experiment, while lear](learner-paced-beats-system-paced-complex-material.md) (qualifies) |
| Guskey 1985 | q2 / q3 · quant-synthesis · r2 | i2; i3 · average effect size .85 | [In one synthesis of group-based mastery learning, five observational studies found more ti](mastery-improves-engagement-attrition.md) (supports) |
| [Ma et al. 2014](https://doi.org/10.1037/a0037123) | q4 · quant-synthesis · r2 | i2 · medium effect, g=0.42 vs teacher-led large-group instruction | [Intelligent tutoring systems improve achievement over non-individualised instruction](adaptive-learning-improves-outcomes.md) (qualifies) |
| [Kulik & Fletcher 2016](https://doi.org/10.3102/0034654315581420) | q4 · quant-synthesis · r? | i2 · medium effect, median 0.66 SD | [Intelligent tutoring systems improve achievement over non-individualised instruction](adaptive-learning-improves-outcomes.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

For design: set a high unit standard and keep the class moving together where possible. For reading the evidence: part of the headline 0.52 SD is the extra quiz feedback mastery students receive, and part is tests written to the course; effects on standardized tests are much smaller.

## Related Claims

- [Mastery Learning Improves Outcomes](mastery-learning-improves-outcomes.md) — the same synthesis, overall effect
- [Group-based mastery learning improves retention of learned material, with an average effect size of .62 across four studies](mastery-improves-retention.md) — related
- [ITS evaluation results depend strongly on test type: effects are large on locally developed tests (ES = 0.73) and small on standardized tests (ES = 0.13)](test-type-moderates-its-effects.md) — related
- [Self-paced mastery programs (PSI) reduce college course completion, though not by enough to explain their examination advantage](self-paced-mastery-programs-reduce-college-course-completion.md) — related
- [Letting learners pace instruction helped on complex material in one experiment, while learner control in general showed almost no effect across 18 studies](learner-paced-beats-system-paced-complex-material.md) — related
