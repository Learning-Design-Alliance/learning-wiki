---
type: claim
title: Cognitive Load Reduction Improves Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: cognitive-load-reduction-improves-learning
evidence_strength: moderate
sources:
  - id: schroeder-and-cenkci-2018
    resource: "https://doi.org/10.1007/s10648-018-9435-9"
    title: "Schroeder, N. L., & Cenkci, A. T. (2018). Spatial contiguity and spatial split-attention effects in multimedia learning environments: A meta-analysis. *Educational Psychology Review, 30*(3), 679–701. [doi:10.1007/s10648-018-9435-9](https://doi.org/10.1007/s10648-018-9435-9)"
    author: "Schroeder, N. L., & Cenkci, A. T."
    q: 4
    i: 2
    n: 58 comparisons (2,426 participants)
  - id: ginns-2006
    resource: "https://doi.org/10.1016/j.learninstruc.2006.10.001"
    title: "Ginns, P. (2006). Integrating information: A meta-analysis of the spatial contiguity and temporal contiguity effects. *Learning and Instruction, 16*(6), 511–525. [doi:10.1016/j.learninstruc.2006.10.001](https://doi.org/10.1016/j.learninstruc.2006.10.001)"
    author: Ginns, P.
    q: 4
    i: "?"
    n: 50 studies
  - id: schroeder-and-cenkci-2020
    resource: "https://doi.org/10.1037/edu0000372"
    title: "Schroeder, N. L., & Cenkci, A. T. (2020). Do measures of cognitive load explain the spatial split-attention principle in multimedia learning environments? A systematic review. *Journal of Educational Psychology, 112*(2), 254–270. [doi:10.1037/edu0000372](https://doi.org/10.1037/edu0000372)"
    author: "Schroeder, N. L., & Cenkci, A. T."
    q: 3
    i: "?"
    n: 41 comparisons
---

# Cognitive Load Reduction Improves Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 3 studies · `q3`–`q4` · `i2` medium

Reducing extraneous cognitive load — the load imposed by how material is presented rather than its intrinsic difficulty — improves learning outcomes, particularly for novices.

## Subclaims

`q4 i2` Integrating related words and pictures in space, a split-attention (extraneous load) reduction, improves learning across many learner, intervention and context moderators, with a medium overall effect (g = 0.63). [→ Schroeder and Cenkci 2018](#schroeder-and-cenkci-2018)

`q4 i?` Reducing split attention across space or time produces substantial learning gains for novices, especially with complex learning materials; material complexity moderates the benefit. [→ Ginns 2006](#ginns-2006)

`q3 i?` Qualifies the mechanism: measures of cognitive load largely fail to show that integrated designs lower extraneous load, so the learning benefit is not clearly explained by load reduction itself. [→ Schroeder and Cenkci 2020](#schroeder-and-cenkci-2020)

## Evidence

### Schroeder and Cenkci 2018

Schroeder, N. L., & Cenkci, A. T. (2018). Spatial contiguity and spatial split-attention effects in multimedia learning environments: A meta-analysis. *Educational Psychology Review, 30*(3), 679–701. [doi:10.1007/s10648-018-9435-9](https://doi.org/10.1007/s10648-018-9435-9)

`q4 · random-effects meta-analysis` · `i2 · medium effect, g=0.63` · `n=58 comparisons (2,426 participants)`

A random-effects meta-analysis of studies comparing integrated designs (related text and diagrams placed together) with spatially separated designs, which force learners to split their attention. Across 58 independent comparisons with 2,426 participants, integrated designs produced an overall effect of g = 0.63. Moderator analyses found the benefit held across many intervention-related and context-related variables. This is direct support for reducing one well-defined source of extraneous load.

### Ginns 2006

Ginns, P. (2006). Integrating information: A meta-analysis of the spatial contiguity and temporal contiguity effects. *Learning and Instruction, 16*(6), 511–525. [doi:10.1016/j.learninstruc.2006.10.001](https://doi.org/10.1016/j.learninstruc.2006.10.001)

`q4 · meta-analysis` · `i? · no effect size in the abstract read` · `n=50 studies`

A meta-analysis of 50 independent studies on the spatial and temporal contiguity effects, which reduce split attention between related pieces of information that are separated in space or presented at different times. The hypothesised benefits for novices were supported. The complexity of the learning materials moderated the effect: for complex materials in particular, increasing contiguity led to substantial learning gains. Only the abstract was read, and it reports no pooled effect size, so impact is coded `i?`.

### Schroeder and Cenkci 2020

Schroeder, N. L., & Cenkci, A. T. (2020). Do measures of cognitive load explain the spatial split-attention principle in multimedia learning environments? A systematic review. *Journal of Educational Psychology, 112*(2), 254–270. [doi:10.1037/edu0000372](https://doi.org/10.1037/edu0000372)

`q3 · systematic review` · `i? · no effect size reported` · `n=41 comparisons`

A systematic review of 41 comparisons from split-attention studies that also measured cognitive load, testing whether integrated designs work by lowering extraneous load. Measures of cognitive load largely did not support that explanation, and integrated designs did not reliably change any cognitive load measure compared with spatially separated designs. The authors propose that integration may instead help learners allocate germane resources to integrative processing. This leaves the learning benefit standing but qualifies the claim's mechanism, and supports this page's warning that load ratings and learning outcomes can come apart.

## Discussion

This claim is the central practical prediction of [Cognitive Load Theory](../theories/cognitive-load-theory.md): because working memory is severely limited, instructional designs that impose unnecessary processing (split attention, redundant material, irrelevant graphics or narration) leave fewer resources for schema construction, and removing that load should improve learning [~M]. The claim is scoped to *extraneous* load reduction — reducing the inherent complexity of the content itself (intrinsic load) can strip out essential learning challenges rather than support them. Designers should therefore manage intrinsic load (e.g., via [chunking](../principles/chunking.md) or sequencing simple-to-complex) rather than simply minimize it.

Key moderators and boundary conditions:

- **Expertise reversal.** Load-reduction techniques that help novices (e.g., worked examples, integrated sources of information) can become redundant and even harmful for advanced learners, who benefit from practice and problem-solving instead — see the [expertise reversal effect](../theories/expertise-reversal-effect.md) and [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-less-effective-with-expertise.md) [~M] Load-reduction designs should include fading mechanisms that restore challenge as competence grows.
- **Over-fragmentation.** Excessive segmentation or scaffolding can prevent learners from integrating information into coherent schemas; some desirable difficulty supports long-term retention [~W]. Load reduction targets *extraneous* processing, not the effortful *germane* processing that builds schemas — conflating the two produces designs that feel easy but teach little.
- **Motivation interaction.** Reducing load does not guarantee engagement; designs must also [activate](activation-improves-learning.md) learners and sustain effort. An instruction that is low-load but passive may underperform a higher-load design that elicits active processing [~W].
- **Measurement dependence.** Whether a design change genuinely reduces extraneous load is an empirical question; subjective load ratings and performance measures can dissociate, so load-reduction claims should be validated against learning outcomes, not perceived ease alone [~W].

Concrete load-reduction levers documented elsewhere in this wiki include [chunking](../principles/chunking.md), the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md), and the broader [cognitive load reduction / CLT scaffolding approach](../patterns/cognitive-load-reduction-clt-scaffolding-approach.md). The companion claim [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) states the inverse direction of the same mechanism.

**Evidence status.** No primary studies are yet catalogued on this page. The claim currently synthesizes the well-replicated CLT literature at the level of the theory page and its related claims; specific experimental and meta-analytic support still needs to be added to the Evidence section before this claim can be promoted from `review`.

## Related Claims

- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the inverse direction of the same mechanism
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — a primary lever for managing intrinsic load
- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — removing extraneous material improves outcomes
- [Worked examples reduce unnecessary search for novices.](worked-examples-reduce-novice-search.md) — a canonical load-reduction technique
- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-less-effective-with-expertise.md) — key boundary condition on load reduction
- [Clear structure improves learning.](clear-structure-improves-learning.md) — structural signaling is a low-cost extraneous-load reduction
- [Cognitive Load Management](cognitive-load-management.md) — related
- [Split Attention Effect Degrades Learning](split-attention-effect-degrades-learning.md) — possibly the same claim (merge candidate)
- [Redundancy Effect Impairs Learning](redundancy-effect-impairs-learning.md) — related
- [Pure contiguity fails to explain cognitive learning: repeated contiguity between cognitions does not make one evoke the other](contiguity-alone-fails-in-cognitive-learning.md) — related
- [Placing heavier cognitive demands on learners can be counterproductive in mapping tasks](heavy-cognitive-demands-of-mapping-can-be-counterproductive.md) — related
- [Multimedia Principle Improves Learning](multimedia-principle-improves-learning.md) — related
- [Despite ignorance of CLT, surveyed teachers report using some of its principles when designing instructions](teachers-use-clt-principles-despite-ignorance.md) — related