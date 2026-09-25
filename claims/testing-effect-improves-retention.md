---
type: claim
title: Testing Effect Improves Retention
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: testing-effect-improves-retention
evidence_strength:
sources:
  - id: rowland-2014
    resource: "https://doi.org/10.1037/a0037559"
    title: "Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. [doi:10.1037/a0037559](https://doi.org/10.1037/a0037559)"
    author: Rowland, C. A.
    q: 4
    i: 2
    n: 159 effect sizes from 61 studies
  - id: roediger-and-karpicke-2006
    resource: "https://doi.org/10.1111/j.1467-9280.2006.01693.x"
    title: "Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)"
    author: "Roediger, H. L., & Karpicke, J. D."
    q: 3
    i: 3
    n: 300 undergraduates (120 + 180)
---

# Testing Effect Improves Retention

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4` · `i2`–`i3`

Retrieving information from memory (being tested) strengthens long-term retention of that information more than restudying the same material for an equivalent amount of time.

## Subclaims

`q4 i2` Across 159 effect sizes from 61 studies, taking a practice test produced better retention than restudying the same material. The benefit was larger after delays of one day or more, and when the initial test used recall or gave feedback. With no feedback and initial test performance of 50% or below, the benefit was about zero. [→ Rowland 2014](#rowland-2014)

`q3 i3` With prose passages, students who recalled the material outperformed students who restudied it on tests two days and one week later. On a test five minutes later, restudying was ahead. [→ Roediger and Karpicke 2006](#roediger-and-karpicke-2006)

## Evidence

### Rowland 2014

Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. [doi:10.1037/a0037559](https://doi.org/10.1037/a0037559)

`q4 · meta-analysis` · `i2 · medium effect, g=0.50` · `n=159 effect sizes from 61 studies`

This random-effects meta-analysis covers 159 effect sizes from 61 studies reported between 1975 and 2013. Each effect compares information that learners were tested on with information they restudied. The mean weighted effect was g = 0.50 (95% CI 0.42 to 0.58), and heterogeneity was high. The effect was larger at retention intervals of at least one day (g = 0.69) than below one day (g = 0.41). It was also larger when the initial test gave [feedback](../elements/feedback.md) (g = 0.73 against 0.39 without) and when the initial test was cued recall rather than recognition (0.61 against 0.29). With no feedback and initial test performance of 50% or below, the effect was about zero (g = 0.03, CI −0.21 to 0.27). Published studies showed larger effects than unpublished ones (0.58 against 0.25), so the author advises caution about publication bias.

### Roediger and Karpicke 2006

Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)

`q3 · peer-reviewed experiment (two experiments)` · `i3 · large effect, d=0.83 at 1 week (Exp. 1)` · `n=300 undergraduates (120 + 180)`

Undergraduates at Washington University read short science passages. In Experiment 1 (120 students), they either restudied a passage or took a free-recall test on it, without feedback. At five minutes, restudying did better (81% against 75% recalled). At two days, testing did better (68% against 54%, d = 0.95), and at one week also (56% against 42%, d = 0.83). In Experiment 2 (180 students), one study period followed by three recall tests beat four study periods on the one-week test (61% against 40%, d = 1.26). Repeated study scored best at five minutes and made students more confident they would remember, but it did worst at one week.

## Discussion

**Mechanism.** The testing effect (also called retrieval practice) is generally explained by the idea that the act of successful retrieval itself modifies the underlying memory trace, making it more accessible later — a "desirable difficulty" in Bjork's sense. Restudying, by contrast, can create fluency illusions: material feels familiar, but that familiarity does not predict durable retention. This connects to broader claims that [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) when effort is misallocated, and that effortful processing — like [chunking](chunking-reduces-working-memory-load.md) — shapes what survives in [information processing](../theories/information-processing-theory.md).

**Boundary conditions to watch for.** The benefit depends on successful retrieval: if learners fail the test and receive no feedback, the effect shrinks or reverses [-M]. It is strongest when retrieval is effortful but successful (e.g., after a short delay rather than immediately), when feedback follows errors, and when tests are low-stakes so the effect is not confounded with test anxiety [~M]. Repeated spaced retrieval outperforms a single retrieval [+M]. These moderators should be confirmed against specific studies once Evidence entries are added.

**Design implications.** Because the effect requires retrieval to be effortful but successful, designers should schedule low-stakes quizzes after a short delay rather than immediately after study, provide corrective feedback, and space repeated retrieval opportunities across sessions. In classroom settings, frequent low-stakes quizzing (rather than a few high-stakes exams) captures the retention benefit while avoiding anxiety confounds. Retrieval practice also pairs naturally with [active learning](active-learning-improves-exam-performance.md) formats such as clicker questions and free recall, and functions as a form of [assessment for learning](assessment-for-learning-improves-achievement.md) when quiz results feed back into instruction.

**Open questions.** How the effect scales from lab materials (word lists, prose passages) to complex classroom content, and how it interacts with [active learning](active-learning-improves-exam-performance.md) formats, remain active areas of replication and meta-analysis.

## Related Claims

- [Active learning improves exam performance.](active-learning-improves-exam-performance.md) — testing is a core active-learning format; both predict better exam outcomes
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — retrieval must be effortful but not overwhelming to produce the benefit
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — organizing material before retrieval supports successful recall
- [Assessment for learning improves achievement.](assessment-for-learning-improves-achievement.md) — low-stakes retrieval practice doubles as formative assessment
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — frames when retrieval demands help versus hinder learning
- [Information Processing Theory](../theories/information-processing-theory.md) — explains how retrieval strengthens memory traces over time