---
type: claim
title: Feedback Improves Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: feedback-improves-learning
aliases: [feedback-improves-learning-outcomes]
evidence_strength: moderate
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

# Feedback Improves Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q4` pre-registered or meta-analytic · `i2` medium

Information provided to learners about their performance or understanding can improve subsequent learning, relative to practice without such information. This page covers the general claim; its strength depends heavily on the form, timing, and content of the feedback and on the learner's stage of expertise.

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

**Feedback is not uniformly beneficial.** The broad claim hides substantial failure modes. Feedback that merely reports right or wrong without explaining why [~M], feedback delivered at a moment when the learner can no longer act on it [-M], and feedback that redirects attention to the self rather than the task [-M] have all been associated with null or negative effects in the wider literature. The claim should therefore be read as conditional: feedback improves learning when it gives the learner usable information they did not already have [+S]. Where feedback functions only as praise or reward, its effects are better explained by [behaviorism](../theories/behaviorism.md) than by information processing — and such effects rarely transfer to learning outcomes [-M].

**What the feedback is about matters.** Feedback specifying what was wrong and how to improve tends to support learning more than feedback that only evaluates [+M]. Feedback directed at the self ("good job") is generally the least productive focus [-M], and feedback on self-regulation — prompting learners to monitor and adjust their own [strategies](../theories/self-regulated-learning.md) — may have the most durable effects [+W], though it is also the hardest to deliver well. This aligns with the broader pattern in which [active learning improves exam performance](active-learning-improves-exam-performance.md): feedback that prompts the learner to do cognitive work outperforms feedback that does the work for them.

**Timing is a moderator, not a simple rule.** Immediate feedback helps when the content is not yet retrievable or when errors would otherwise be rehearsed and consolidated [+M]. Delayed feedback can help when it gives learners a chance to attempt retrieval first, or when the intervening activity would otherwise be abandoned [~M]. The question for designers is not "immediate or delayed?" but "will the learner still be able to act on this, and will acting on it involve productive effort?"

**Working memory and actionability constrain feedback uptake.** Feedback that arrives when working memory is already saturated [-M], or that arrives in a volume the learner cannot act on [-M], is effectively lost. Keeping feedback specific, task-focused, and within what the learner can process in the moment — consistent with [cognitive load reduction improves learning](cognitive-load-reduction-improves-learning.md) — is a precondition for any benefit.

**Expertise changes what feedback is for.** Novices benefit most from feedback on procedures and concepts [+M]; more advanced learners may find the same feedback redundant or even irritating [-M], an instance of the [expertise reversal effect](../theories/expertise-reversal-effect.md). Feedback design should fade in specificity and shift toward self-evaluation as competence grows.

**Relationship to formative assessment.** Feedback is the primary mechanism through which formative assessment influences achievement [+S], but the two claims are distinct: [assessment for learning improves achievement](assessment-for-learning-improves-achievement.md) covers the full cycle of eliciting evidence, interpreting it, and adapting instruction. This page should focus on the feedback episode itself, not the whole cycle.

**Design implications.** Feedback is most likely to improve learning when it is specific and task-focused [+M], delivered close enough to practice that the learner can still revise [+M], kept within working-memory limits, and paired with an opportunity to act on it — for example through [action-oriented feedback](../strategies/action-oriented-feedback.md) that names the next concrete step [+W]. Rubrics and exemplars can make feedback criteria visible in advance, so the feedback episode confirms rather than introduces expectations [+W].

**Open questions.** The relative contributions of task-level, process-level, and self-regulation feedback across domains remain unsettled, as do the boundary conditions for immediate versus delayed delivery. How automated feedback systems should adapt timing and specificity to learner expertise at scale is an active design problem.

*Merged from “Feedback improves learning outcomes” (feedback-improves-learning-outcomes):* **Actionability.** Feedback improves learning when it tells learners something they can act on — what was wrong, why, and what to do next. Feedback that merely evaluates (a grade, a score, "good job") gives the learner no next step. This motivates the design principle of [action-oriented feedback](../strategies/action-oriented-feedback.md), which directs attention to the task and the strategy rather than the person.

**Focus of the feedback.** Feedback directed at the self ("you're so smart") tends to be least useful and can even backfire by diverting attention from the task to the ego; feedback at the task, process, or self-regulation levels is generally more productive. This is a design choice, not a fixed property of the medium.

**Timing and delivery.** Immediate feedback often helps for procedural skills and error prevention, while delayed feedback can support retention and transfer; the optimal interval likely depends on the task and the learner's expertise [~M]. Similarly, feedback that reduces cognitive load for a novice can become redundant for an advanced learner — a moderation pattern consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M].

**Relationship to assessment.** Feedback is the mechanism through which formative assessment exerts its effect: assessment information only improves achievement when it is translated into feedback learners understand and use — see [Assessment for Learning](../principles/assessment-for-learning.md) and [Assessment for learning improves achievement](assessment-for-learning-improves-achievement.md).

**Constraints on effectiveness.** The claim fails under identifiable conditions: evaluative-only feedback with no actionable content [-S]; self-level feedback that redirects attention to the ego [-M]; feedback that overloads working memory for novices or becomes redundant for experts [~M]; and feedback the learner cannot understand or act on because it is not aligned with the task or the learner's current understanding [-S].

**Open questions.** The claim as stated is too broad to be testable as written. Future enrichment should decompose it into subclaims specifying feedback type (verification vs. elaborated), timing, source (teacher, peer, automated), and learner expertise, each with its own evidence base.

## Related Claims

- [Assessment for learning improves achievement](assessment-for-learning-improves-achievement.md) — feedback is the central mechanism of formative assessment; the two claims should not double-count the same evidence
- [Cognitive load reduction improves learning](cognitive-load-reduction-improves-learning.md) — feedback that exceeds working-memory capacity cannot be used, however accurate it is
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — structuring feedback into digestible units keeps it actionable
- [Clear structure improves learning](clear-structure-improves-learning.md) — well-structured feedback is easier to locate, interpret, and act on
- [Self-regulated learning](../theories/self-regulated-learning.md) — self-regulation-level feedback aims to make learners their own feedback providers
- [Adaptive learning improves outcomes](adaptive-learning-improves-outcomes.md) — adaptive systems operationalize feedback by tailoring responses to learner performance
- [Cognitive disequilibrium motivates conceptual change](cognitive-disequilibrium-motivates-conceptual-change.md) — feedback that surfaces discrepancies between performance and goals can trigger productive disequilibrium
- [Feedback Addressing Task Improves Learning](feedback-addressing-task-improves-learning.md) — a narrower finding that bears on this claim
- [Feedback Most Effective At Task And Process Levels](feedback-most-effective-at-task-and-process-levels.md) — related
- [Feedback Improves Learning When It Addresses Task Goals](feedback-improves-learning-when-it-addresses-task-goals.md) — related
- [Feedback Use Improves Learning](feedback-use-improves-learning.md) — related
