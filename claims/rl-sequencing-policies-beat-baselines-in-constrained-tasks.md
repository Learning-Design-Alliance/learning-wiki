---
type: claim
title: Reinforcement-learning sequencing policies beat baseline sequencing in about half of controlled studies, mostly in constrained tasks and against weak baselines
description: A review of 41 controlled studies found reinforcement-learning-induced instructional sequencing policies significantly outperformed all baselines in 21, with success concentrated in paired-associate, concept-learning and activity-type sequencing and none for sequencing interdependent content.
id: rl-sequencing-policies-beat-baselines-in-constrained-tasks
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2019
sources:
  - id: doroudi-2019
    resource: "https://doi.org/10.1007/s40593-019-00187-x"
    title: "Doroudi, S., Aleven, V., & Brunskill, E. (2019). Where's the reward? A review of reinforcement learning for instructional sequencing. International Journal of Artificial Intelligence in Education, 29(4), 568-620"
    author: "Doroudi, S., Aleven, V., & Brunskill, E."
    q: 3
    i: "?"
    n: 41 studies
    kind: review
    rigour: 3
---

# Reinforcement-learning sequencing policies beat baseline sequencing in about half of controlled studies, mostly in constrained tasks and against weak baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r3` · `q3` · n=41 studies (34 papers)
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

An instructional policy induced by reinforcement learning (RL) decides, from a student's past responses and a model fitted to data, which activity to give next. This claim is about how often such policies have beaten other ways of ordering instruction when tested on real students, and in which kinds of sequencing problem.

## Subclaims

`q3 i?` Across 41 controlled studies (34 papers) that compared an RL-induced instructional policy with baseline sequencing on real students, the review classifies 21 as finding an RL-induced policy significantly better than every baseline, 4 as finding an aptitude-treatment interaction favouring lower-performing students, 4 as mixed, 11 as finding no significant difference and 1 as finding the baseline better. [→ Doroudi 2019](#doroudi-2019)

`q3 i?` Success depended on what was sequenced: 11 of 14 paired-associate learning studies and 4 of 7 concept-learning studies found the RL policy better than all baselines, and 4 of 10 activity-type studies did so (4 more found an interaction favouring lower performers), but none of the 8 studies sequencing interdependent content did. [→ Doroudi 2019](#doroudi-2019)

`q3 i?` Many of the positive results came from weak comparisons: 17 of the 24 studies with a significant effect or interaction (71%) compared the RL policy only with random sequencing or with other untested RL policies, against 6 of the studies without a significant effect (35%). [→ Doroudi 2019](#doroudi-2019)

`q3 i?` In classroom settings the record was thinner: of 15 classroom studies, three found an RL-induced policy significantly better than the baselines and four found aptitude-treatment interactions. [→ Doroudi 2019](#doroudi-2019)

## Evidence

### Doroudi 2019

Doroudi, S., Aleven, V., & Brunskill, E. (2019). Where's the reward? A review of reinforcement learning for instructional sequencing. *International Journal of Artificial Intelligence in Education, 29*(4), 568-620. [doi:10.1007/s40593-019-00187-x](https://doi.org/10.1007/s40593-019-00187-x)

`q3 · systematic review (citation-traced search, vote count)` · `i? · no pooled effect size` · `n=41 studies (34 papers)` · `review · r3`

The authors searched by forward and backward citation tracing (Google Scholar, to December 2018) for controlled experiments with real students in which at least one condition's instructional policy was learned from data with some form of optimisation, and compared it with baseline sequencing. They counted outcomes rather than pooling effect sizes, and grouped the studies into five clusters by the kind of instructional action sequenced: paired-associate items such as vocabulary, artificial concept-learning tasks, interdependent content (mostly K-12 mathematics skills), choice of activity type for fixed content (for example [worked example](../elements/worked-examples.md) versus problem solving), and objectives other than learning. Table 2 gives the counts above; the text elsewhere says "Twenty-one of the 36 studies" and "Ten studies found no significant difference", which does not match the table's total of 41, so the subclaims follow the table. The authors note that significant results "often found a Cohen's d effect size of at least 0.8" but report effects per study (Appendix Table 8), not a pooled estimate. The review was prompted by two of the authors' own RL experiments in a fractions tutor, both null, one of which is included.

## Discussion

The authors read the pattern as RL working best where the sequencing problem is constrained (independent items, few actions), where the model of student learning was informed by psychological theory (models of memory and forgetting for paired associates, models of concept learning), where learning-science principles already say order matters (the [spacing effect](spaced-practice-improves-retention.md), the [expertise reversal effect](expertise-reversal-effect.md)), and where students start with little prior knowledge. They also point to the weak baselines: for flashcard-style learning, stronger non-data-driven schedulers such as the Leitner system and SuperMemo exist and were rarely the comparison. For a designer the practical reading is that an RL-sequenced product's claim to beat "random order" is not evidence that it beats an expert-designed or spacing-based sequence, and that for interdependent content no study in the review showed RL sequencing beating reasonable baselines.

The authors recommend constraining RL with theory (for example searching only over policies that fade worked examples into problem solving and deciding when to switch), comparing against state-of-the-art baselines, and testing a policy offline against several plausible student models before running it on students; the robust evaluation matrix, which simulates each candidate policy under several student models fitted to earlier data, is their method for the last. They also note that almost all studies used system control of cognitive outcomes, and suggest shared learner or teacher control and affective or metacognitive targets as untested directions. In the one included study that compared an RL policy with full learner control (Atkinson, 1972), learner control was 53% better than random and the RL policy 108% better than random.

## Related Claims
- [Intelligent tutoring systems improve achievement over non-individualised instruction](adaptive-learning-improves-outcomes.md) — the broader claim about adaptive systems this bears on
- [Spaced practice improves retention](spaced-practice-improves-retention.md) — the principle the review credits for RL's success with paired-associate items
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](expertise-reversal-effect.md) — the principle behind the activity-type cluster
