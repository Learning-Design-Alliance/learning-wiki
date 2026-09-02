---
type: strategy
id: interleaved-practice
title: Interleaved Practice
description: Arranging practice so that different problem types or skills are mixed within a session rather than blocked, forcing learners to discriminate which strategy applies.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Interleaved Practice

> **Strategy** · [All strategies](index.md)

## Description
Interleaved practice mixes different but related problem types, skills, or categories within a single study session (A-B-C-A-B-C) instead of practicing each in a blocked sequence (A-A-A-B-B-B). The key mechanism is discriminative contrast: because learners cannot assume which procedure applies, they must first identify the problem type and select the appropriate strategy before solving. Interleaving is typically combined with [spaced repetition](../elements/practice.md), since interleaved schedules inherently distribute practice over time.

## Design Implications

Interleaving trades short-term performance for long-term retention and transfer: blocked practice feels easier and produces better immediate test scores, but interleaved practice produces superior delayed performance, especially in categorization and mathematics [Interleaved practice improves delayed test performance in mathematics.](../claims/comparing-contrasting-cases-improves-learning.md) [+S]. A meta-analysis across classroom and lab studies found reliable benefits overall, with the largest effects for category induction and mathematics, and smaller or mixed effects for motor skills and foreign-language vocabulary [Brunmair & Richter meta-analysis.](https://doi.org/10.1037/bul0000209) [+S]. Because interleaving makes practice feel harder and slower, learners frequently judge it less effective — a metacognitive illusion that must be addressed explicitly.

### Context
#### Requirements
- A set of problem types or categories that are *confusable* — interleaving works by forcing discrimination between similar-looking items
- Learners who have at least minimal familiarity with each item type; interleaving entirely novel material adds [extraneous load](../theories/cognitive-load-theory.md) without discriminative benefit
- Explicit framing that mixed practice is intentionally harder, to prevent abandonment when performance dips
- Sufficient total practice — interleaving redistributes practice, it does not replace it ([Practice](../elements/practice.md))

#### Constraints
- Blocked practice outperforms interleaving when problem types are highly distinct and never confusable — there is nothing to discriminate [~S]
- For novices at the very start of acquisition, interleaving can overload working memory before any strategy is available to select [~M]; a common design is blocked introduction followed by interleaved consolidation
- Interleaving too many categories at once (more than roughly 3–4 confusable types) dilutes the contrast and can degrade learning [~W]
- Learners' perceived difficulty and preference run opposite to actual effectiveness; unmanaged, this leads to dropout or reversion to blocked study [-M]

#### Implementation Variability
- **Within-session interleaving** (ABCABC) vs. **across-session interleaving** (homework sets that mix the week's topics with prior weeks' topics) — the latter is easier to schedule and adds spacing benefits
- **Incremental interleaving**: start with two categories, add more as discrimination improves
- **Interleaved worked examples**: alternating fully worked examples across categories before independent practice
- **Inductive interleaving**: presenting exemplars from different categories mixed together so learners induce the category boundaries themselves [Kornell & Bjork.](https://doi.org/10.1037/0278-7393.34.5.1093) [+S]

### Target Learners
- Learners past initial acquisition who can execute each procedure but confuse *when* to apply it — the classic profile for interleaving gains [Rohrer et al. classroom study.](https://doi.org/10.1037/xap0000050) [+S]
- Learners prone to overconfidence from blocked practice, who mistake fluent repetition for mastery
- Less suitable for absolute novices on brand-new material, where the [expertise-reversal effect](../theories/expertise-reversal-effect.md) applies [~M]

### Target Learning Goals
- Strategy selection and conditional knowledge: knowing *which* method fits *which* problem
- Categorization and discrimination: learning the boundaries between confusable concepts
- Long-term retention and transfer of procedural skill, rather than immediate performance

### Instructions
1. Identify the confusable problem types or categories in the domain — the pairs learners routinely mix up.
2. Introduce each type with [blocked practice](../elements/practice.md) until learners can execute the procedures, keeping initial sessions low-load.
3. Build interleaved sets that shuffle the types in mixed order, ensuring no type appears in a predictable run; keep the set to 3–4 categories at first.
4. Require learners to name the problem type and select a strategy *before* solving, making the discrimination step explicit.
5. Distribute interleaved sets across sessions so items are revisited after delays, compounding the spacing benefit.
6. Warn learners that mixed practice feels harder and produces more errors, and explain why that difficulty is productive — otherwise they will judge it ineffective and disengage.

## Related Strategies
- Spaced practice — interleaved schedules inherently distribute practice; the two are usually confounded and mutually reinforcing
- Retrieval practice — interleaved sets work best when items are solved from memory rather than by rereading notes
- Comparing contrasting cases — interleaving enacts the same discrimination mechanism at the level of practice scheduling

## Examples
- **Rohrer, Dedrick, and Stershic (2015)** — In real mathematics classrooms, worksheets that interleaved graphing, volume, and slope problems produced dramatically better delayed test scores (about 80% vs. 64%) than blocked worksheets with identical problems.
- **Khan Academy** — Mastery-style exercise sets mix problem types within a skill cluster rather than presenting long runs of one type, and spaced review resurfaces earlier skills mixed with new ones.
- **Art and pathology education** — Studies of painting attribution and histology slide identification interleave exemplars from different artists or disease categories, improving inductive category learning [Kornell & Bjork.](https://doi.org/10.1037/0278-7393.34.5.1093) [+S]

## Key Sources
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)
- Rohrer, D., Dedrick, R. F., & Stershic, S. (2015). Interleaved practice improves mathematics learning. *Journal of Educational Psychology, 107*(3), 900–908. [doi:10.1037/edu0000001](https://doi.org/10.1037/edu0000001)
- Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin, 145*(11), 1029–1052. [doi:10.1037/bul0000209](https://doi.org/10.1037/bul0000209)
- Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the "enemy of induction"? *Psychological Science, 19*(6), 585–592. [doi:10.1111/j.1467-9280.2008.02127.x](https://doi.org/10.1111/j.1467-9280.2008.02127.x)