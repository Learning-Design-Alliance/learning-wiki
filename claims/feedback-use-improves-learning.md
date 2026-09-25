---
type: claim
title: Feedback Use Improves Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: feedback-use-improves-learning
evidence_strength:
sources:
  - id: wisniewski-zierer-hattie-2020
    resource: "https://doi.org/10.3389/fpsyg.2019.03087"
    title: "Wisniewski, B., Zierer, K., & Hattie, J. (2020). The Power of Feedback Revisited: A Meta-Analysis of Educational Feedback Research. *Frontiers in Psychology, 10*, 3087. [doi:10.3389/fpsyg.2019.03087](https://doi.org/10.3389/fpsyg.2019.03087)"
    author: "Wisniewski, B., Zierer, K., & Hattie, J."
    q: 4
    i: 2
    n: "994 effect sizes, N>61,000"
---

# Feedback Use Improves Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · `i2` medium · n=994 effect sizes, N>61,000

Learners benefit when they receive feedback on their performance and actively use it to revise their understanding or work. The claim centers on feedback **use** — revision, re-attempt, strategy adjustment — not merely feedback delivery.

## Subclaims

`q4 i2` A meta-analysis of 435 studies (k=994 effect sizes, N>61,000) finds a medium overall effect of feedback on student learning (d=0.48), but the pooled effect masks large heterogeneity by feedback type and outcome domain — feedback is not a single consistent treatment. [→ Wisniewski Zierer Hattie 2020](#wisniewski-zierer-hattie-2020)

## Evidence

### Wisniewski Zierer Hattie 2020

Wisniewski, B., Zierer, K., & Hattie, J. (2020). The Power of Feedback Revisited: A Meta-Analysis of Educational Feedback Research. *Frontiers in Psychology, 10*, 3087. [doi:10.3389/fpsyg.2019.03087](https://doi.org/10.3389/fpsyg.2019.03087)

`q4 · meta-analysis (random-effects model, 435 primary studies)` · `i2 · medium effect, d=0.48` · `n=994 effect sizes, N>61,000`

A random-effects meta-analysis synthesizing 435 studies and 994 effect sizes (over 61,000 participants) on feedback and student learning, conducted to replicate and expand Hattie's Visible Learning synthesis. The pooled effect was medium (d=0.48), but heterogeneity was significant, meaning feedback cannot be treated as one uniform intervention. Moderator analysis found the type and information content of the feedback drove the effect: praise, punishment, and reward carried low or low-to-medium effects, while corrective feedback aimed at new-skill acquisition was highly effective, and feedback had a larger impact on cognitive/motor outcomes than on motivational/behavioral ones. Video/audio and computer-assisted feedback channels showed medium-high to high effects, and specific written comments outperformed generic ones. Note: this study's unit of analysis is feedback *delivered*, not verified feedback *use* (revision/re-attempt) — the sharper claim this page centers on; a second candidate source for that distinction, Kluger & DeNisi (1996, doi:10.1037/0033-2909.119.2.254), could not be read (APA PsycNET paywalled it and no open-access copy was found), so it is not cited here.

## Discussion

Feedback is one of the most consistently reported influences on achievement in the learning sciences, but its effects are famously variable: the same feedback can help, do nothing, or harm depending on its content, timing, and how the learner responds. A useful distinction separates feedback **about the task** (what was wrong and how to improve), **about the process** (strategies to try), **about self-regulation** (how to monitor and adjust one's own work), and **about the self** (praise or criticism of the person). Task- and process-level feedback are the forms most plausibly tied to improved performance; personal praise carries little instructional information and can even undermine engagement when it frames ability as fixed.

The claim as stated centers on feedback **use**, not merely feedback delivery. Feedback only improves learning when the learner does something with it — revising a solution, re-attempting a task, or adjusting a strategy. This links the claim to [self-regulated learning](../theories/self-regulated-learning.md): learners must notice the gap between current and target performance and act to close it. Designers should therefore build in time and structure for feedback uptake (revision cycles, re-submission, immediate re-practice) rather than treating feedback as a terminal event — see [Action-oriented feedback](../strategies/action-oriented-feedback.md) for design patterns that specify what the learner should do next.

Key moderators and boundary conditions to document when evidence is added:

- **Timing.** Immediate feedback often helps for procedural skills; delayed feedback can aid retention and transfer by spacing re-engagement. The optimal interval likely depends on task type.
- **Goal orientation.** Feedback is more effective when learners hold mastery goals than when they hold performance goals, where critical feedback can be experienced as a threat.
- **Cognitive load.** Feedback on complex tasks must be timed and sized so that reading it does not itself overload working memory — see [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) and [cognitive load theory](../theories/cognitive-load-theory.md). Chunked, prioritized feedback is easier to absorb and act on than exhaustive error lists — see [Chunking reduces working memory load](chunking-reduces-working-memory-load.md).
- **Expertise.** Novices generally need more directive, task-level feedback; advanced learners may benefit more from prompts to self-evaluate, consistent with the expertise-reversal pattern described in [expertise reversal effect](../theories/expertise-reversal-effect.md).

Open questions: how durable feedback effects are over time, how feedback interacts with grading, and which digital feedback formats best support uptake at scale.

## Related Claims

- [Assessment for learning improves achievement](assessment-for-learning-improves-achievement.md) — formative assessment is the practice context in which feedback is generated and used.
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — overloaded learners cannot process or act on feedback.
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — chunked feedback is easier to absorb and act on.
- [Self-regulated learning](../theories/self-regulated-learning.md) — feedback uptake depends on learners monitoring gaps and adjusting their own strategies.
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — the optimal feedback type shifts from directive to self-evaluative prompts as expertise grows.