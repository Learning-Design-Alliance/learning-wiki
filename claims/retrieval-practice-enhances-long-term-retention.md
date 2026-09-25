---
type: claim
title: Retrieval Practice Enhances Long Term Retention
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: retrieval-practice-enhances-long-term-retention
evidence_strength: strong
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

# Retrieval Practice Enhances Long Term Retention

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4` · `i2`–`i3`

Attempting to retrieve information from memory strengthens that memory more than restudying the same material, producing durable gains in long-term retention. The claim concerns the *relative* benefit of retrieval over restudy at a delay; it does not claim retrieval practice is always preferable during initial learning, when material is not yet retrievable.

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

The proposed mechanism is that retrieval is itself a learning event: successfully reconstructing information from memory modifies the memory trace and makes future retrieval more likely, whereas restudying only re-exposes learners to material without requiring reconstruction. This distinguishes retrieval practice from mere re-exposure and places it within [cognitive load theory](../theories/cognitive-load-theory.md) and broader accounts of how [chunking reduces working memory load](../claims/chunking-reduces-working-memory-load.md) during encoding and consolidation.

Several boundary conditions are worth noting. Retrieval practice is effortful, and learners often misjudge its value because successful retrieval feels harder and less productive than rereading — a fluency illusion that can lead learners to prefer less effective strategies [-M]. Retrieval attempts that fail entirely, without feedback or subsequent successful retrieval, may contribute little; the benefit is generally tied to successful (or eventually successful) retrieval [~M]. The effect also depends on the material being retrievable and on learners having sufficient prior knowledge to attempt retrieval meaningfully — for very novice learners, unsupported retrieval attempts can impose extraneous load and contribute to conditions where [cognitive overload degrades learning](../claims/cognitive-overload-degrades-learning.md) [~M].

Design implications follow directly. Low-stakes quizzing, closed-book recall prompts, and [assessment for learning](../claims/assessment-for-learning-improves-achievement.md) designs all operationalize retrieval practice; the key is that learners must generate answers from memory rather than recognize or reread them. Because retrieval is demanding, it should be introduced with feedback and adequate scaffolding, consistent with [cognitive load reduction](../claims/cognitive-load-reduction-improves-learning.md) principles, and paired with [activation](../claims/activation-improves-learning.md) of relevant prior knowledge so that retrieval attempts are meaningful rather than guesswork.

Open questions that evidence entries should address include: how retrieval practice compares with restudying across retention intervals (the effect is expected to grow as the retention interval lengthens), how feedback moderates the effect, whether benefits transfer beyond memorization to inference and application, and how effect sizes vary across domains, learner ages, and formats (free recall, cued recall, multiple choice).

## Related Claims

- [Active learning improves exam performance](active-learning-improves-exam-performance.md) — retrieval-based activities are a core component of active learning designs.
- [Assessment for learning improves achievement](assessment-for-learning-improves-achievement.md) — low-stakes formative quizzing embeds retrieval practice into instruction.
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — organized, chunked material is easier to retrieve successfully, moderating retrieval benefits.
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — overly demanding retrieval attempts can backfire for novices.
- [Cognitive load reduction improves learning](cognitive-load-reduction-improves-learning.md) — scaffolding retrieval attempts keeps them productive rather than overwhelming.
- [Activation improves learning](activation-improves-learning.md) — activated prior knowledge makes retrieval attempts meaningful and successful.