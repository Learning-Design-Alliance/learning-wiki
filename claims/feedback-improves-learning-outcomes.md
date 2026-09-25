---
type: claim
title: Feedback improves learning outcomes
id: feedback-improves-learning-outcomes
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
evidence_strength:
sources:
  - id: wisniewski-et-al-2020
    resource: "https://doi.org/10.3389/fpsyg.2019.03087"
    title: "Wisniewski, B., Zierer, K., & Hattie, J. (2020). The power of feedback revisited: A meta-analysis of educational feedback research. *Frontiers in Psychology, 10*, 3087. [doi:10.3389/fpsyg.2019.03087](https://doi.org/10.3389/fpsyg.2019.03087)"
    author: "Wisniewski, B., Zierer, K., & Hattie, J."
    q: 4
    i: 2
    n: "435 studies (k=994 effects, N>61,000)"
  - id: kluger-denisi-1996
    resource: "https://doi.org/10.1037/0033-2909.119.2.254"
    title: "Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin, 119*(2), 254–284. [doi:10.1037/0033-2909.119.2.254](https://doi.org/10.1037/0033-2909.119.2.254)"
    author: "Kluger, A. N., & DeNisi, A."
    q: 4
    i: 2
    n: 607 effect sizes (23,663 observations)
---

# Feedback improves learning outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q4` pre-registered or meta-analytic · `i2` medium

Feedback — information provided to a learner about their performance relative to a goal — is widely treated as one of the most powerful single influences on achievement, but its effects are notoriously heterogeneous: the same intervention can produce large gains, no change, or negative outcomes depending on design and context.

## Subclaims

`q4 i2` On average, feedback improves student learning by a medium amount (d = 0.48 across 435 studies), but the effects vary widely, and the size depends on how much information the feedback carries: reinforcement or punishment d = 0.24, corrective feedback d = 0.46, high-information feedback d = 0.99. [→ Wisniewski et al. 2020](#wisniewski-et-al-2020)

`q4 i2` Feedback interventions improve performance on average (d = .41), but more than a third of them made performance worse, and they work less well the more they turn the learner's attention away from the task and toward the self. [→ Kluger & DeNisi 1996](#kluger-denisi-1996)

## Evidence

### Wisniewski et al. 2020

Wisniewski, B., Zierer, K., & Hattie, J. (2020). The power of feedback revisited: A meta-analysis of educational feedback research. *Frontiers in Psychology, 10*, 3087. [doi:10.3389/fpsyg.2019.03087](https://doi.org/10.3389/fpsyg.2019.03087)

`q4 · random-effects meta-analysis` · `i2 · medium effect, d=0.48` · `n=435 studies (k=994 effects, N>61,000)`

A random-effects meta-analysis of empirical studies of feedback on student learning in education, drawn from the studies behind earlier meta-analyses. The overall effect was medium (d = 0.48), but heterogeneity was large, so the authors argue that feedback should not be treated as a single intervention. The most important moderator was how much information the feedback carried: reinforcement or punishment gave d = 0.24 [0.06–0.43], corrective feedback d = 0.46 [0.39–0.55], and high-information feedback, which adds information about self-regulation, d = 0.99 [0.82–1.15]. Effects were larger on cognitive (d = 0.51) and motor-skill (d = 0.63) outcomes than on motivational ones (d = 0.33).

### Kluger & DeNisi 1996

Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin, 119*(2), 254–284. [doi:10.1037/0033-2909.119.2.254](https://doi.org/10.1037/0033-2909.119.2.254)

`q4 · meta-analysis` · `i2 · medium effect, d=.41` · `n=607 effect sizes (23,663 observations)`

A meta-analysis of feedback interventions on task performance in laboratory and field settings, not only in education. On average, feedback improved performance (d = .41), but more than a third of the interventions reduced performance, and sampling error or whether the feedback was positive or negative did not explain this. The authors' feedback intervention theory, tested with moderator analyses, proposes that feedback becomes less effective as it pulls the learner's attention away from the task and toward the self. This is a strong qualification of the general claim.

## Discussion

**Actionability.** Feedback improves learning when it tells learners something they can act on — what was wrong, why, and what to do next. Feedback that merely evaluates (a grade, a score, "good job") gives the learner no next step. This motivates the design principle of [action-oriented feedback](../strategies/action-oriented-feedback.md), which directs attention to the task and the strategy rather than the person.

**Focus of the feedback.** Feedback directed at the self ("you're so smart") tends to be least useful and can even backfire by diverting attention from the task to the ego; feedback at the task, process, or self-regulation levels is generally more productive. This is a design choice, not a fixed property of the medium.

**Timing and delivery.** Immediate feedback often helps for procedural skills and error prevention, while delayed feedback can support retention and transfer; the optimal interval likely depends on the task and the learner's expertise [~M]. Similarly, feedback that reduces cognitive load for a novice can become redundant for an advanced learner — a moderation pattern consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M].

**Relationship to assessment.** Feedback is the mechanism through which formative assessment exerts its effect: assessment information only improves achievement when it is translated into feedback learners understand and use — see [Assessment for Learning](../principles/assessment-for-learning.md) and [Assessment for learning improves achievement](assessment-for-learning-improves-achievement.md).

**Constraints on effectiveness.** The claim fails under identifiable conditions: evaluative-only feedback with no actionable content [-S]; self-level feedback that redirects attention to the ego [-M]; feedback that overloads working memory for novices or becomes redundant for experts [~M]; and feedback the learner cannot understand or act on because it is not aligned with the task or the learner's current understanding [-S].

**Open questions.** The claim as stated is too broad to be testable as written. Future enrichment should decompose it into subclaims specifying feedback type (verification vs. elaborated), timing, source (teacher, peer, automated), and learner expertise, each with its own evidence base.

## Related Claims

- [Assessment for learning improves achievement](assessment-for-learning-improves-achievement.md) — feedback is the primary mechanism linking formative assessment to achievement gains
- [Adaptive learning improves outcomes](adaptive-learning-improves-outcomes.md) — adaptive systems operationalize feedback by tailoring responses to learner performance
- [Cognitive load reduction improves learning](cognitive-load-reduction-improves-learning.md) — well-designed feedback manages rather than adds to working memory load
- [Cognitive disequilibrium motivates conceptual change](cognitive-disequilibrium-motivates-conceptual-change.md) — feedback that surfaces discrepancies between performance and goals can trigger productive disequilibrium