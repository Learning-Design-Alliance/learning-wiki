---
type: claim
title: Interleaving Improves Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: interleaving-improves-learning
evidence_strength: moderate
sources:
  - id: brunmair-richter-2019
    resource: "https://doi.org/10.1037/bul0000209"
    title: "Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin, 145*(11), 1029–1052. [doi:10.1037/bul0000209](https://doi.org/10.1037/bul0000209)"
    author: "Brunmair, M., & Richter, T."
    q: 4
    i: 2
    n: 59 studies (238 effect sizes, 158 samples)
---

# Interleaving Improves Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · `i2` medium · n=59 studies (238 effect sizes, 158 samples)

Mixing different problem types or categories within a study sequence (interleaving) produces better learning and transfer than studying each category in a blocked sequence [+S], largely by forcing learners to discriminate which strategy or concept applies.

## Subclaims

`q4 i2` A multilevel meta-analysis of 59 studies (238 effect sizes) finds a moderate overall benefit of interleaved over blocked inductive-learning presentation (Hedges' g = 0.42), but the effect is strongly moderated by material type — strongest for visual/perceptual category learning (paintings, photographs), smaller for mathematical tasks, and reversed (favoring blocking) for word-based category learning. [→ Brunmair & Richter 2019](#brunmair-richter-2019)

## Evidence

### Brunmair & Richter 2019

Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin, 145*(11), 1029–1052. [doi:10.1037/bul0000209](https://doi.org/10.1037/bul0000209)

`q4 · multilevel meta-analysis` · `i2 · medium effect, Hedges' g=0.42, 95% CI [0.34, 0.50]` · `n=59 studies (238 effect sizes, 158 samples)`

A multilevel meta-analysis of 59 studies comparing interleaved to blocked presentation of category exemplars (paintings, photographs, mathematical procedures, expository texts, words) on a subsequent classification/discrimination test. Interleaving produced a moderate overall benefit (g = 0.42), robust to a sensitivity analysis using only independent effects (g = 0.43). The benefit was not uniform: it was largest for paintings (g = 0.67) and naturalistic photographs (g = 0.35), smaller for mathematical tasks (g = 0.34), nonsignificant for expository texts, and *reversed* for word-based categories (g = −0.39, favoring blocking). A meta-regression found stronger interleaving effects when between-category similarity was higher and within-category similarity was lower — consistent with the attentional-bias/discriminative-contrast account that interleaving works by forcing discrimination between confusable categories.

## Discussion

**Mechanism.** The most widely accepted account is discriminative: blocked practice lets learners apply one strategy repeatedly without identifying the problem type, whereas interleaved practice requires selecting the appropriate strategy for each item [+M]. This selection process is effortful in the moment — interleaved groups typically perform worse during practice — but yields better delayed test performance, a classic desirable-difficulty pattern [+S]. Interleaving also inherently spaces material over time, so its benefits may be partly confounded with [spaced practice](../principles/spaced-practice.md); studies that control for total exposure and spacing still generally find an interleaving advantage, but the two effects are intertwined in most designs [~M].

**Boundary conditions.** The effect is strongest for category learning and problem classification (e.g., mathematics problem types, painting styles, naturalistic categories) where items are highly confusable and discriminating between categories is the core skill [+S]. When categories are easily distinguished, or when the target skill is executing a single procedure fluently rather than choosing among procedures, interleaving offers little advantage and may slow acquisition [~M]. Novices may also be overwhelmed if too many categories are interleaved at once before any category has been minimally learned — an instance of the [expertise reversal effect](../theories/expertise-reversal-effect.md), where a difficulty that helps more experienced learners harms novices [-M].

**Open questions.** How much interleaving is optimal (fully random vs. moderate mixing), how the effect scales with category confusability, and how to overcome learners' preference for blocked practice — learners often judge blocking more effective despite worse outcomes [-W] — remain active research areas. Because interleaving raises in-the-moment processing demands, designers should weigh it against total [cognitive load](../theories/cognitive-load-theory.md) and consider [chunking](../claims/chunking-reduces-working-memory-load.md) and sequencing supports so the added difficulty remains desirable rather than overwhelming.

**Design implication.** A practical sequence is often blocked-then-interleaved: introduce each category in a blocked segment until it is minimally learnable, then mix categories so learners must practice identifying which procedure applies. Expect lower practice scores and higher delayed-test scores than blocked-only designs, and warn learners explicitly that the harder-feeling schedule is the more effective one. Because learners' metacognitive judgments favor blocking [-W], explicit framing of the discriminative-practice rationale is not optional garnish but a condition of persistence with the schedule.

**Relation to example-based instruction.** Interleaving composes naturally with [worked examples](../claims/worked-examples-reduce-novice-search.md): an interleaved sequence can mix example study, faded examples, and problem solving across categories, so learners both discriminate problem types and avoid unguided search during early acquisition [+M]. The same expertise-reversal caution applies to both — see [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md).

## Related Claims

- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — interleaving raises in-the-moment load; chunking and sequencing choices interact
- [Cognitive load reduction improves learning.](cognitive-load-reduction-improves-learning.md) — desirable difficulties like interleaving must be managed against total load
- [Worked examples reduce unnecessary search for novices.](worked-examples-reduce-novice-search.md) — interleaving pairs naturally with example-based sequences across categories
- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md) — same expertise-reversal boundary applies to interleaving schedules
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — supports that fade with expertise may reverse; interleaving benefits likely depend on learner skill level
- [Cognitive load theory](../theories/cognitive-load-theory.md) — the theoretical framework within which interleaving's costs and benefits are usually analyzed