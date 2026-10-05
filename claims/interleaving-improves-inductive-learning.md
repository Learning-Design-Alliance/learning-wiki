---
type: claim
title: "Interleaving category examples improves inductive category learning for visual and mathematical materials, but not for expository texts or word categories"
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: interleaving-improves-inductive-learning
aliases: [interleaved-practice-improves-retention, interleaving-improves-learning, interleaving-improves-transfer]
evidence_strength:
sources:
  - id: brunmair-richter-2019
    resource: "https://doi.org/10.1037/bul0000209"
    title: "Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin, 145*(11), 1029–1052. [doi:10.1037/bul0000209](https://doi.org/10.1037/bul0000209)"
    author: "Brunmair, M., & Richter, T."
    q: 4
    i: 2
    n: 59 studies (238 effect sizes, 158 samples)
    kind: quant-synthesis
    rigour: "?"
---

# Interleaving category examples improves inductive category learning for visual and mathematical materials, but not for expository texts or word categories

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r?` · `q4` · `i2` medium · n=59 studies (238 effect sizes, 158 samples)
<!-- deprecated title (2026-10-05, overstated its evidence; the precise title came from interleaved-practice-improves-retention, folded in): Interleaving Improves Inductive Learning -->

Interleaving — mixing different problem or category types within a practice sequence rather than blocking them by type — improves learners' ability to induce the distinguishing features of concepts and select appropriate strategies.

## Subclaims

`q4 i2` A multilevel meta-analysis of 59 studies (238 effect sizes) finds a moderate overall benefit of interleaved over blocked inductive-learning presentation (Hedges' g = 0.42), but the effect is strongly moderated by material type — strongest for visual/perceptual category learning (paintings, photographs), smaller for mathematical tasks, and reversed (favoring blocking) for word-based category learning. [→ Brunmair & Richter 2019](#brunmair-richter-2019)

## Evidence

### Brunmair & Richter 2019

Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin, 145*(11), 1029–1052. [doi:10.1037/bul0000209](https://doi.org/10.1037/bul0000209)

`q4 · multilevel meta-analysis` · `i2 · medium effect, Hedges' g=0.42, 95% CI [0.34, 0.50]` · `n=59 studies (238 effect sizes, 158 samples)` · `quant-synthesis · r?`

A multilevel meta-analysis of 59 studies comparing interleaved to blocked presentation of category exemplars (paintings, photographs, mathematical procedures, expository texts, words) on a subsequent classification/discrimination test. Interleaving produced a moderate overall benefit (g = 0.42), robust to a sensitivity analysis using only independent effects (g = 0.43). The benefit was not uniform: it was largest for paintings (g = 0.67) and naturalistic photographs (g = 0.35), smaller for mathematical tasks (g = 0.34), nonsignificant for expository texts, and *reversed* for word-based categories (g = −0.39, favoring blocking). A meta-regression found stronger interleaving effects when between-category similarity was higher and within-category similarity was lower — consistent with the attentional-bias/discriminative-contrast account that interleaving works by forcing discrimination between confusable categories.

## Discussion

**Mechanism.** Interleaving is thought to work through two complementary routes. First, when different problem types are juxtaposed, learners must discriminate between them and identify which strategy each requires — a discriminative-contrast process that supports inductive learning of category boundaries. Second, interleaving inherently spaces repeated exposure to each problem type, so part of the benefit may be attributable to [spacing](../principles/spaced-learning.md) rather than mixing per se; studies that control for spacing typically find interleaving still adds a discriminative advantage, though the two are difficult to fully disentangle.

**Perceived difficulty.** A recurring boundary condition is that interleaved practice feels harder and produces worse practice-session performance than blocked practice, even though it yields better delayed test performance. Learners and instructors therefore often judge interleaving to be less effective — a metacognitive illusion that can lead to it being abandoned prematurely. Designers should expect lower in-practice accuracy and communicate the delayed benefit explicitly.

**Boundary conditions.** The benefit is strongest when the to-be-learned categories or problem types are highly confusable, so that side-by-side comparison exposes their distinguishing features. When categories are easily discriminated, or when the material is at the very start of skill acquisition, blocked practice may be preferable — consistent with the general pattern in [cognitive load theory](../theories/cognitive-load-theory.md) that high-guidance, high-variability formats suit learners with some prior knowledge better than complete novices (see the [expertise reversal effect](../theories/expertise-reversal-effect.md)). Interleaving also presupposes that each item is learnable on first exposure; if items are too difficult, mixing them can overload working memory rather than support contrastive comparison — see [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md)

**Open questions.** The relative contributions of discrimination and spacing, the optimal interleaving ratio (how many items per type within a sequence), and how interleaving interacts with feedback timing remain active research questions. The meta-analysis recorded above finds a moderate benefit for interleaved over blocked presentation in inductive learning (g = 0.42), strongest for visual categories and reversed for word-based categories, so the claim holds for perceptual material and not for all category learning.

*Merged from “Interleaving category examples improves inductive category learning for visual and mathematical materials, but not for expository texts or word categories” (interleaved-practice-improves-retention):* **Desirable difficulties.** Interleaving is a classic "desirable difficulty": it degrades performance during acquisition while improving delayed test performance [+S]. Learners in interleaved conditions typically rate their practice as less effective and prefer blocked practice, so subjective judgments of learning are an unreliable guide here [-M]. Designers should expect and plan for this perception gap rather than letting learner preference drive sequencing decisions.

**Mechanism.** The most supported account is discriminative: interleaved practice forces learners to first identify which strategy or concept applies before executing it, whereas blocked practice lets them repeat one procedure without the selection step [+M]. This makes interleaving especially valuable when categories are confusable — e.g., problem types in mathematics, painting styles in art history, or diagnostic categories in clinical training. The discrimination requirement also connects to [analogical reasoning](../principles/analogical-reasoning.md): comparing across mixed item types supports abstracting the features that distinguish categories.

**Boundary conditions.** Interleaving is most likely to help when (a) the to-be-learned categories are easily confused with one another, (b) each item is still retrievable when revisited (spacing and interleaving interact), and (c) learners have at least minimal exposure to each category before items are mixed. Interleaving items a learner has not yet encoded at all can produce failure rates that swamp any discrimination benefit [-M]. It also trades off with [cognitive load](../theories/cognitive-load-theory.md) concerns for novices — mixed sequences impose more load than blocked ones, and for very low-knowledge learners this can outweigh the discrimination benefit, consistent with expertise-reversal patterns described in [expertise reversal](../theories/expertise-reversal-effect.md) [~M]. Where mixed sequences overload novices, designers can pair interleaving with load-reducing supports such as [worked examples](../elements/demonstration.md) or [chunking](chunking-reduces-working-memory-load.md), since [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) and can erase the interleaving advantage entirely. Managing this load trade-off is a sequencing decision, not an afterthought — see [cognitive load management](../principles/cognitive-load-management.md).

**Practical implications.** Because interleaving feels harder and less productive, designers should (a) sequence blocked introductory exposure before mixed practice, (b) explain to learners why mixed practice feels worse but works better, and (c) assess with delayed, mixed-format tests so practice and assessment align. Spacing mixed practice over days rather than compressing it into one session likely compounds the retention benefit [+W], though the optimal schedule is unresolved.

**Open questions.** Optimal interleaving schedules (how many categories, how many items per category, how much spacing) are not settled, and most published work uses short, well-structured category-learning tasks; generalization to complex, open-ended skill domains is less established [+W].

**Evidence status.** The one meta-analysis recorded above measured inductive category learning, not retention of practised problems, and it found the benefit depends on material: largest for visual categories, smaller for mathematics, and reversed for word-based categories. Studies of interleaved problem practice and delayed retention still need to be recorded here.

*Merged from “Interleaving Improves Learning” (interleaving-improves-learning):* **Mechanism.** The most widely accepted account is discriminative: blocked practice lets learners apply one strategy repeatedly without identifying the problem type, whereas interleaved practice requires selecting the appropriate strategy for each item [+M]. This selection process is effortful in the moment — interleaved groups typically perform worse during practice — but yields better delayed test performance, a classic desirable-difficulty pattern [+S]. Interleaving also inherently spaces material over time, so its benefits may be partly confounded with [spaced practice](../principles/spaced-learning.md); studies that control for total exposure and spacing still generally find an interleaving advantage, but the two effects are intertwined in most designs [~M].

**Boundary conditions.** The effect is strongest for category learning and problem classification (e.g., mathematics problem types, painting styles, naturalistic categories) where items are highly confusable and discriminating between categories is the core skill [+S]. When categories are easily distinguished, or when the target skill is executing a single procedure fluently rather than choosing among procedures, interleaving offers little advantage and may slow acquisition [~M]. Novices may also be overwhelmed if too many categories are interleaved at once before any category has been minimally learned — an instance of the [expertise reversal effect](../theories/expertise-reversal-effect.md), where a difficulty that helps more experienced learners harms novices [-M].

**Open questions.** How much interleaving is optimal (fully random vs. moderate mixing), how the effect scales with category confusability, and how to overcome learners' preference for blocked practice — learners often judge blocking more effective despite worse outcomes [-W] — remain active research areas. Because interleaving raises in-the-moment processing demands, designers should weigh it against total [cognitive load](../theories/cognitive-load-theory.md) and consider [chunking](../claims/chunking-reduces-working-memory-load.md) and sequencing supports so the added difficulty remains desirable rather than overwhelming.

**Design implication.** A practical sequence is often blocked-then-interleaved: introduce each category in a blocked segment until it is minimally learnable, then mix categories so learners must practice identifying which procedure applies. Expect lower practice scores and higher delayed-test scores than blocked-only designs, and warn learners explicitly that the harder-feeling schedule is the more effective one. Because learners' metacognitive judgments favor blocking [-W], explicit framing of the discriminative-practice rationale is not optional garnish but a condition of persistence with the schedule.

**Relation to example-based instruction.** Interleaving composes naturally with [worked examples](../claims/worked-examples-reduce-novice-search.md): an interleaved sequence can mix example study, faded examples, and problem solving across categories, so learners both discriminate problem types and avoid unguided search during early acquisition [+M]. The same expertise-reversal caution applies to both — see [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-less-effective-with-expertise.md).

*Merged from “Interleaving Improves Transfer” (interleaving-improves-transfer):* **Mechanism.** The most widely accepted account is discriminative contrast: when problem types are interleaved, learners must first identify *which* strategy applies before executing it, forcing them to notice the deep features that distinguish categories [~M]. Blocked practice allows learners to repeat a single strategy without this identification step, which can produce strong blocked performance that collapses on mixed or transfer tests. This identification-before-execution step is what distinguishes interleaving from mere varied practice, and it connects interleaving to the broader family of comparison-based interventions — see [Analogical reasoning improves transfer.](analogical-reasoning-improves-transfer.md)

**Performance during practice vs. learning.** A recurring pattern in the interleaving literature is that interleaved practice feels harder and produces slower, more error-prone practice performance, yet yields better delayed test performance — a desirable difficulty [~M]. Designers and learners should not read poor practice-session performance as evidence that interleaving is failing. This dissociation between momentary performance and durable learning mirrors findings for other desirable difficulties, and it means formative checks built on blocked practice can be misleading — see [Assessment for learning improves achievement.](assessment-for-learning-improves-achievement.md)

**Boundary conditions.** Benefits are strongest when the interleaved categories are highly confusable (e.g., volume of a wedge vs. a cone; painting styles of similar artists) and when each category has already received some initial exposure — interleaving entirely novel material can overload novices and reverse the benefit [~M]. Interleaving is also domain-sensitive: it applies naturally to categorization and strategy-selection tasks, but is less obviously applicable to skills with a single procedure [~W]. The added difficulty also interacts with working-memory demands — see [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) and [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md). A practical implication is a *fading* schedule: begin with blocked introduction of each category, then transition to mixed practice once minimal familiarity is established, analogous to fading in example-based instruction — see [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-less-effective-with-expertise.md) for the parallel expertise-reversal logic.

**Open questions.** Optimal interleaving schedules (fixed rotation vs. random mixing), the ideal ratio of interleaved to blocked practice for novices, and durability of benefits over long retention intervals remain active research areas. Most published studies use short laboratory or classroom interventions with immediate or short-delay tests; evidence for very long-term retention is thinner. Until controlled studies are added to the Evidence section, this claim should be treated as directionally plausible but not yet quantitatively established.

## Related Claims

- [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) — interleaving only helps when mixed items remain within working memory capacity
- [Analogical reasoning improves transfer.](../claims/analogical-reasoning-improves-transfer.md) — interleaving supports the same contrastive comparison process across examples
- [Cognitive flexibility theory: multiple cases.](../theories/cognitive-flexibility-theory.md) — varied, interleaved cases build flexible, transferable knowledge
- [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) — the productive difficulty of interleaving can drive reevaluation of strategies
- [Cognitive load reduction improves learning.](../claims/cognitive-load-reduction-improves-learning.md) — interleaving imposes load that must be managed for the discriminative benefit to emerge
- [Interleaving Improves Discrimination](interleaving-improves-discrimination.md) — a narrower finding that bears on this claim
- [The usefulness of induction and errorful learning varies with the type of terminal task being taught](task-type-moderates-induction-error-usefulness.md) — related
- [Learning varied tasks of the same type enables transfer to unencountered tasks of that type](task-variety-enables-transfer-same-task-type.md) — related
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — interleaving raises load; chunked, well-structured materials moderate that cost
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — a boundary condition: overloaded novices may benefit less from mixed sequences
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — sequencing benefits shrink or reverse as learner expertise grows
- [Cognitive load theory](../theories/cognitive-load-theory.md) — the theoretical frame for why interleaving is harder during practice but better for retention
- [Cognitive load management](../principles/cognitive-load-management.md) — practical levers for keeping mixed practice within learners' capacity
- [Analogical reasoning improves transfer.](analogical-reasoning-improves-transfer.md) — comparing across mixed items supports the discrimination that interleaving demands
- [Desirable Difficulties Enhance Learning](desirable-difficulties-enhance-learning.md) — related
- [Spaced Repetition Improves Retention](spaced-repetition-improves-retention.md) — related
- [Spaced Practice Improves Retention](spaced-practice-improves-retention.md) — related
- [Faster rate of learning may be negatively related to long-term retention (efficiency-effectiveness trade-off)](learning-rate-retention-tradeoff.md) — related
- [Sequencing worked examples with practice problems improves learning for novices](worked-example-problem-sequences.md) — related
- [Task rehearsal improves fluency and complexity on the repeated task but does not transfer to a new task of the same type](task-repetition-fluency-complexity-same-task-only.md) — related
- [Cognitive load reduction improves learning.](cognitive-load-reduction-improves-learning.md) — desirable difficulties like interleaving must be managed against total load
- [Worked examples reduce unnecessary search for novices.](worked-examples-reduce-novice-search.md) — interleaving pairs naturally with example-based sequences across categories
- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-less-effective-with-expertise.md) — same expertise-reversal boundary applies to interleaving schedules
- [Assessment for learning improves achievement.](assessment-for-learning-improves-achievement.md) — interleaved practice's poor visible performance means assessment must probe discrimination, not just execution
- [Cognitive load management](cognitive-load-management.md) — interleaving is a load-management decision: it trades reduced load during acquisition for greater load during practice
- [Comparing Contrasting Cases Improves Learning](comparing-contrasting-cases-improves-learning.md) — related
