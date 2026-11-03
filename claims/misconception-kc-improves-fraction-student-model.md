---
type: claim
title: Adding a whole-number-strategy misconception to a fraction tutor's student model improved its fit to the data and gave per-student misconception estimates that tracked pre-test errors
description: In logged data from 40 students using a fraction arithmetic tutor, a knowledge component coded +1 where the independent whole-number strategy gives the right answer and -1 where it gives a wrong one improved the Additive Factors Model's fit, and each student's estimated misconception strength correlated with the share of their pre-test errors that followed that strategy (Spearman R = 0.46).
id: misconception-kc-improves-fraction-student-model
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-02
evidence_strength: weak
newest_evidence: 2016
recheck_by: 2019
sources:
  - id: liu-patel-koedinger-2016
    resource: "https://doi.org/10.1145/2883851.2883967"
    title: "Liu, R., Patel, R., & Koedinger, K. R. (2016). Modeling common misconceptions in learning process data. In *Proceedings of the Sixth International Conference on Learning Analytics & Knowledge (LAK '16)* (pp. 369–377). ACM. [doi:10.1145/2883851.2883967](https://doi.org/10.1145/2883851.2883967)"
    author: "Liu, R., Patel, R., & Koedinger, K. R."
    q: 2
    i: "?"
    n: 40 students
    kind: associational
    rigour: 1
---

# Adding a whole-number-strategy misconception to a fraction tutor's student model improved its fit to the data and gave per-student misconception estimates that tracked pre-test errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2` · n=40 students
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

The student models that choose the next problem in an intelligent tutor usually track only skills that help a learner succeed. This claim is about whether a model can also track a misconception: a strategy that gives correct answers on some problems and wrong answers on others. In the independent whole-number strategy, a learner applies the operation to the two numerators and the two denominators separately (1/2 + 2/3 gives 3/5). This gives correct answers to fraction multiplication problems and wrong ones to most addition problems.

## Subclaims

`q2 i?` Adding a misconception knowledge component for the independent whole-number strategy to an Additive Factors Model of 40 students' fraction-tutor data lowered AIC from 4238 to 4119 and BIC from 4328 to 4216, a significantly better fit (p < 0.0001); separate terms for chances to strengthen and to weaken the misconception improved it further (AIC 4093, BIC 4203). [→ Liu, Patel & Koedinger 2016](#liu-patel-koedinger-2016)

`q2 i?` In that model, each problem step where the strategy happened to give a correct answer increased the misconception's estimated weight (0.038 per opportunity), and each step where it gave a wrong answer and drew negative feedback decreased it (−0.052 per opportunity). [→ Liu, Patel & Koedinger 2016](#liu-patel-koedinger-2016)

`q2 i?` Each student's model-estimated misconception strength correlated with the proportion of that student's pre-test errors that followed the strategy (Spearman R = 0.46, p = 0.002), which the authors read as evidence that the estimates are externally valid. [→ Liu, Patel & Koedinger 2016](#liu-patel-koedinger-2016)

## Evidence

### Liu, Patel & Koedinger 2016

Liu, R., Patel, R., & Koedinger, K. R. (2016). Modeling common misconceptions in learning process data. In *Proceedings of the Sixth International Conference on Learning Analytics & Knowledge (LAK '16)* (pp. 369–377). ACM. [doi:10.1145/2883851.2883967](https://doi.org/10.1145/2883851.2883967)

`q2 · secondary analysis of tutor log data, model comparison` · `i? · fit statistics and a correlation, no treatment effect` · `n=40 students` · `associational · r1`

A modelling study on a public dataset of 40 students who used a fraction arithmetic tutor and met the problem types in a mixed (interleaved) order. Each student did 24 multiplication problems, 10 additions with the same denominators and 14 with different denominators. The authors compared three logistic Additive Factors Models fitted with lme4: the original expert-built model with six skills; that model plus an intercept for a misconception knowledge component, coded +1 on steps where the independent whole-number strategy yields the right answer, −1 where it yields a wrong one and 0 where it does not apply; and a version that also gave the misconception separate learning slopes for opportunities to strengthen and to weaken it. Both additions improved fit (chi-square tests, p < 0.0001). The misconception model predicted poor performance on one step that the original model treated as equivalent to another, which shifts the instructional implication from more practice on equivalent fractions to addressing the misconception. Per-student misconception intercepts, fitted as random effects, correlated with each student's proportion of strategy-consistent errors at pre-test (Spearman R = 0.46). The authors note that the strategy accounted for about 25% of non-hint errors in the data, and they found no other misconception accounting for a large share. They list these limits: one misconception modelled in one dataset; a misconception component must predict a pattern no combination of the regular skills can, which needs a fine-grained tutor interface; and the logistic model credits a correct multiplication step to both the multiplication skill and the misconception, which is probably wrong. The learners' ages and setting are not given in the article.

## Discussion

This is evidence about a component an adaptive tutor could rely on, a student-model term for a misconception, not a test of teaching. The strengthen and weaken slopes are what the model estimates from the order in which students happened to meet problems, not the result of an experiment that varied that order. The authors' suggested uses, such as giving a student with a high estimated misconception weight more problems where the strategy fails, or showing erroneous examples, are proposals that the article does not test.

## Related Claims

- [Equal accuracy on fraction comparison items can mask fundamentally different misconceptions](fraction-accuracy-masks-distinct-misconceptions.md) — related
