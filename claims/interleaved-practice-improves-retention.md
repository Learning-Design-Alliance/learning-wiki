---
type: claim
title: Interleaved Practice Improves Retention
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: interleaved-practice-improves-retention
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

# Interleaved Practice Improves Retention

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · `i2` medium · n=59 studies (238 effect sizes, 158 samples)

Interleaving — mixing different problem types or categories within a practice session rather than blocking them by type — improves long-term retention and discrimination between concepts, even though learners often feel it is less effective during practice.

## Subclaims

`q4 i2` A multilevel meta-analysis of 59 studies (238 effect sizes) finds a moderate overall benefit of interleaved over blocked inductive-learning presentation (Hedges' g = 0.42), but the effect is strongly moderated by material type — strongest for visual/perceptual category learning (paintings, photographs), smaller for mathematical tasks, and reversed (favoring blocking) for word-based category learning. [→ Brunmair & Richter 2019](#brunmair-richter-2019)

## Evidence

### Brunmair & Richter 2019

Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin, 145*(11), 1029–1052. [doi:10.1037/bul0000209](https://doi.org/10.1037/bul0000209)

`q4 · multilevel meta-analysis` · `i2 · medium effect, Hedges' g=0.42, 95% CI [0.34, 0.50]` · `n=59 studies (238 effect sizes, 158 samples)`

A multilevel meta-analysis of 59 studies comparing interleaved to blocked presentation of category exemplars (paintings, photographs, mathematical procedures, expository texts, words) on a subsequent classification/discrimination test. Interleaving produced a moderate overall benefit (g = 0.42), robust to a sensitivity analysis using only independent effects (g = 0.43). The benefit was not uniform: it was largest for paintings (g = 0.67) and naturalistic photographs (g = 0.35), smaller for mathematical tasks (g = 0.34), nonsignificant for expository texts, and *reversed* for word-based categories (g = −0.39, favoring blocking). A meta-regression found stronger interleaving effects when between-category similarity was higher and within-category similarity was lower — consistent with the attentional-bias/discriminative-contrast account that interleaving works by forcing discrimination between confusable categories.

## Discussion

**Desirable difficulties.** Interleaving is a classic "desirable difficulty": it degrades performance during acquisition while improving delayed test performance [+S]. Learners in interleaved conditions typically rate their practice as less effective and prefer blocked practice, so subjective judgments of learning are an unreliable guide here [-M]. Designers should expect and plan for this perception gap rather than letting learner preference drive sequencing decisions.

**Mechanism.** The most supported account is discriminative: interleaved practice forces learners to first identify which strategy or concept applies before executing it, whereas blocked practice lets them repeat one procedure without the selection step [+M]. This makes interleaving especially valuable when categories are confusable — e.g., problem types in mathematics, painting styles in art history, or diagnostic categories in clinical training. The discrimination requirement also connects to [analogical reasoning](../principles/analogical-reasoning.md): comparing across mixed item types supports abstracting the features that distinguish categories.

**Boundary conditions.** Interleaving is most likely to help when (a) the to-be-learned categories are easily confused with one another, (b) each item is still retrievable when revisited (spacing and interleaving interact), and (c) learners have at least minimal exposure to each category before items are mixed. Interleaving items a learner has not yet encoded at all can produce failure rates that swamp any discrimination benefit [-M]. It also trades off with [cognitive load](../theories/cognitive-load-theory.md) concerns for novices — mixed sequences impose more load than blocked ones, and for very low-knowledge learners this can outweigh the discrimination benefit, consistent with expertise-reversal patterns described in [expertise reversal](../theories/expertise-reversal-effect.md) [~M]. Where mixed sequences overload novices, designers can pair interleaving with load-reducing supports such as [worked examples](../elements/demonstration.md) or [chunking](chunking-reduces-working-memory-load.md), since [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) and can erase the interleaving advantage entirely. Managing this load trade-off is a sequencing decision, not an afterthought — see [cognitive load management](../principles/cognitive-load-management.md).

**Practical implications.** Because interleaving feels harder and less productive, designers should (a) sequence blocked introductory exposure before mixed practice, (b) explain to learners why mixed practice feels worse but works better, and (c) assess with delayed, mixed-format tests so practice and assessment align. Spacing mixed practice over days rather than compressing it into one session likely compounds the retention benefit [+W], though the optimal schedule is unresolved.

**Open questions.** Optimal interleaving schedules (how many categories, how many items per category, how much spacing) are not settled, and most published work uses short, well-structured category-learning tasks; generalization to complex, open-ended skill domains is less established [+W].

**Evidence status.** The one meta-analysis recorded above measured inductive category learning, not retention of practised problems, and it found the benefit depends on material: largest for visual categories, smaller for mathematics, and reversed for word-based categories. Studies of interleaved problem practice and delayed retention still need to be recorded here.

## Related Claims

- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — interleaving raises load; chunked, well-structured materials moderate that cost
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — a boundary condition: overloaded novices may benefit less from mixed sequences
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — sequencing benefits shrink or reverse as learner expertise grows
- [Cognitive load theory](../theories/cognitive-load-theory.md) — the theoretical frame for why interleaving is harder during practice but better for retention
- [Cognitive load management](../principles/cognitive-load-management.md) — practical levers for keeping mixed practice within learners' capacity
- [Analogical reasoning improves transfer.](analogical-reasoning-improves-transfer.md) — comparing across mixed items supports the discrimination that interleaving demands