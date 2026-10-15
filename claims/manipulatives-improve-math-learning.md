---
type: claim
title: Manipulatives Improve Math Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: manipulatives-improve-math-learning
aliases: [hands-on-learning-improves-achievement]
evidence_strength:
sources:
  - id: carbonneau-et-al-2013
    resource: "https://doi.org/10.1037/a0031084"
    title: "Carbonneau, K. J., Marley, S. C., & Selig, J. P. (2013). A meta-analysis of the efficacy of teaching mathematics with concrete manipulatives. *Journal of Educational Psychology, 105*(2), 380–400. [doi:10.1037/a0031084](https://doi.org/10.1037/a0031084)"
    author: "Carbonneau, K. J., Marley, S. C., & Selig, J. P."
    q: 4
    i: "?"
    n: 7,237 students, k=55 studies
    kind: quant-synthesis
    rigour: 2
---

# Manipulatives Improve Math Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q4` · n=7,237 students, k=55 studies

Physical or visual objects that learners manipulate (counters, base-ten blocks, fraction tiles) can support mathematics learning by making abstract relationships concrete and actionable.

## Subclaims

`q4 i?` A meta-analysis of 55 studies (N=7,237, kindergarten through college) found statistically significant small-to-moderate effects favoring concrete manipulatives over abstract-symbols-only instruction, moderated by instructional and methodological study characteristics. [→ Carbonneau et al. 2013](#carbonneau-et-al-2013)

`q4 i?` A meta-analysis of 55 studies (N=7,237) finds small-to-moderate effects favoring concrete-manipulative (hands-on) mathematics instruction over abstract-symbol-only instruction, strongest for retention. [→ Carbonneau et al. 2013](#carbonneau-et-al-2013)

## Evidence

### Carbonneau et al. 2013

Carbonneau, K. J., Marley, S. C., & Selig, J. P. (2013). A meta-analysis of the efficacy of teaching mathematics with concrete manipulatives. *Journal of Educational Psychology, 105*(2), 380–400. [doi:10.1037/a0031084](https://doi.org/10.1037/a0031084)

`q4 · meta-analysis` · `i? · effect size reported as "small to moderate" but no pooled d value appears in what was read` · `n=7,237 students, k=55 studies` · `quant-synthesis · r2`

Systematic search identified 55 studies comparing mathematics instruction using manipulatives against a control condition using only abstract math symbols, spanning kindergarten to college. Overall results were statistically significant, favoring manipulatives, with small-to-moderate effect sizes (Cohen's d). The manipulatives-learning relationship was moderated by both instructional and methodological characteristics of the studies. Separate analyses by outcome type found moderate-to-large effects on retention (k=53, N=7,140) and small effects on problem solving (k=9, N=477), transfer (k=13, N=3,453), and justification (k=2, N=109), all favoring manipulatives.

<!-- merged 2026-10-14 from hands-on-learning-improves-achievement: that page's entry for this study, which differed from the one above, kept verbatim.
### Carbonneau et al. 2013

Carbonneau, K. J., Marley, S. C., & Selig, J. P. (2013). A meta-analysis of the efficacy of teaching mathematics with concrete manipulatives. *Journal of Educational Psychology, 105*(2), 380–400. [doi:10.1037/a0031084](https://doi.org/10.1037/a0031084)

`q4 · well-powered meta-analysis (55 studies)` · `i? · magnitude described only qualitatively in what was read; no numeric d located` · `n=7,237 (students, kindergarten through college)` · `quant-synthesis · r2`

A systematic search identified 55 studies comparing mathematics instruction using concrete manipulatives against instruction using only abstract math symbols, across students from kindergarten to college level. Statistically significant effects in Cohen's *d* favored manipulatives overall, and separate outcome-specific analyses found moderate-to-large effects on retention (k=53, N=7,140) and small effects on problem solving (k=9, N=477), transfer (k=13, N=3,453), and justification (k=2, N=109). The authors also report that the benefit was moderated by both instructional and methodological characteristics of the studies, so the effect is not uniform across implementations.
-->

## Studies bearing on this claim

<!-- synthesis:start -->
*Does a concrete stage help at all over abstract symbols alone?* This table gathers the studies behind this claim and the 2 narrower claims that bear on it: **4 distinct studies** (3 causal, 1 quant-synthesis), `q2`–`q4`, 0 of 4 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Carbonneau et al. 2013](https://doi.org/10.1037/a0031084) | q4 · quant-synthesis · r2 | i? | this claim |
| [Kontra et al. 2015](https://doi.org/10.1177/0956797615569355) | q3 · causal · r? | i? | [Physical Experience Enhances Science Learning](physical-experience-enhances-science-learning.md) (qualifies) |
| [Zacharia & Olympiou 2011](https://doi.org/10.1016/j.learninstruc.2010.03.001) | q2 · causal · r? | i? | [Physical Experience Enhances Science Learning](physical-experience-enhances-science-learning.md) (qualifies) |
| Kutbay 2020 | q2 · causal · r2 | i? | [Abstract and concrete animation representations do not differ significantly in middle scho](abstract-concrete-representation-no-difference.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

The proposed mechanism is that manipulatives offload and concretize mathematical relationships, reducing demands on working memory in the same general way described in [Cognitive Load Theory](../theories/cognitive-load-theory.md) — but concreteness is a double-edged sword. If the surface features of the object are salient while the target mathematical structure is not, learners may attend to the wrong features, and the manipulation itself can add extraneous load rather than reduce it, consistent with the general finding that [cognitive overload degrades learning](cognitive-overload-degrades-learning.md). Effective use therefore depends on the manipulative being well matched to the concept, on learners being supported to connect the concrete representation to symbolic notation, and on the manipulation being genuinely reasoning-driven rather than procedural.

A key moderator is learner expertise. For novices, a well-designed concrete representation can anchor understanding; for more advanced learners, the same representation may be redundant or even interfere with abstract reasoning, mirroring the [expertise reversal effect](../theories/expertise-reversal-effect.md). Duration and fading also matter: long-term reliance on a specific manipulative without fading toward diagrams and symbols risks learners binding understanding to that object rather than to the underlying mathematics.

Design implications follow directly from these moderators. Manipulatives should be chosen so their perceptual features map transparently onto the target structure (e.g., fraction tiles whose relative sizes encode the part–whole relation), introduced alongside — not after — symbolic notation, and faded deliberately toward drawings and abstract symbols as competence grows. This progression from concrete to pictorial to abstract representation is the design logic of [concrete-representational-abstract sequencing](../strategies/concrete-representational-abstract-cra.md). Teachers should also guard against "hands-on without minds-on": physical activity with an object does not guarantee mathematical reasoning about it, and procedural manipulation can mask conceptual gaps. This connects to the broader principle that [active learning](../principles/active-learning.md) benefits come from cognitive engagement, not physical activity per se.

The one meta-analysis recorded above (Carbonneau et al., 2013) supports a small-to-moderate overall benefit of manipulatives over abstract-symbols-only instruction. The moderators discussed here (learner expertise, fading, connection to symbolic notation) are not quantified by any entry on this page, so they should be read as plausible, mechanism-grounded boundary conditions rather than established ones.

*Merged from “Hands-on learning improves achievement” (hands-on-learning-improves-achievement):* **What the recorded evidence covers.** The one meta-analysis above concerns concrete manipulatives in mathematics, read as an abstract that gives no numeric effect sizes. It does not cover hands-on learning in other subjects.

**Mechanism.** Plausible routes from hands-on activity to achievement include grounding abstract concepts in perceptual-motor experience, generating [cognitive disequilibrium](cognitive-disequilibrium-motivates-conceptual-change.md) that motivates conceptual change, and increasing engagement — see [Active learning improves exam performance](active-learning-improves-exam-performance.md). However, physical activity alone does not guarantee cognitive engagement; the benefit depends on the activity prompting learners to process the target concept, not merely manipulate materials. This is consistent with the broader finding that [active learning improves exam performance](active-learning-improves-exam-performance.md) only when activities require meaningful cognitive processing.

**Moderators and boundary conditions.** Hands-on approaches impose extraneous load when materials, goals, or procedures are poorly scaffolded — see [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) and [Cognitive load management](../principles/cognitive-load-management.md). Guidance matters: minimally guided discovery versions of hands-on learning underperform guided versions for novices, consistent with [Cognitive load theory](../theories/cognitive-load-theory.md). The benefit also plausibly reverses for advanced learners, mirroring the [expertise reversal effect](../theories/expertise-reversal-effect.md). Hands-on formats are also harder to scale and assess than [worked-example](../elements/demonstration.md)-based or [direct instruction](../patterns/direct-instruction.md) formats.

**Enactment vs. sense-making.** A recurring confound in this literature is that "hands-on" conditions typically bundle physical manipulation with prediction, discussion, and reflection. Until studies isolate enactment from guided sense-making, it remains unclear whether the physical component contributes anything beyond the accompanying cognitive activity. Designers should therefore treat the manipulative as a vehicle for structured sense-making rather than as the active ingredient itself.

**Design implications.** Where hands-on formats are used, pair manipulation with prediction prompts, structured discussion, and reflection so that the physical experience is explicitly connected to the target concept. Scaffold procedures and materials to limit extraneous load, and fade that scaffolding as learners gain expertise — the same fading logic applied in [worked example](../elements/demonstration.md) sequences.

**Open questions.** Whether the advantage stems from the physical manipulation itself or from the accompanying discussion, prediction, and reflection remains unresolved. Studies isolating enactment from guided sense-making are needed before the claim can be stated with confidence.

## Related Claims

- [Reviewed studies report experiential learning benefits for engagement, skills, confidence and outcomes in human services education](experiential-learning-engagement-skills-ethical-reasoning.md) — the general claim this finding bears on, with the studies behind it

- [Block play predicts math achievement](block-play-predicts-math-achievement.md) — spatial construction play as a correlate of later mathematics skill, closely tied to the manipulatives rationale.
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — the memory mechanism manipulatives are meant to support by externalizing structure.
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — the boundary condition: poorly designed manipulatives can add rather than remove load.
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — why manipulative benefits should fade as learners advance.
- [Active learning improves exam performance](active-learning-improves-exam-performance.md) — clarifies that engagement must be cognitive, not merely physical, for manipulative use to pay off.
- [A systematic review argues that concrete materials aid mathematics and science learning when they are explicitly and gradually connected to the abstract symbols they represent](manipulatives-require-connection-to-concept.md) — related
- [Spatial Training Improves Math Performance](spatial-training-improves-math-performance.md) — related
- [Using more representations of mathematical ideas is associated with increased student math achievement](more-representations-mathematical-ideas-higher-achievement.md) — related
- [Representation-alignment tension between expert externalization and novice comprehension](representation-alignment-tension-expert-novice.md) — related
- [Concreteness fading enables learners to build a store of memorable images usable when abstract symbols lose meaning](fading-builds-memorable-images.md) — related
- [Conflict-based instruction improves science conceptual learning, though staged contradictions helped only learners who reported being confused, and no study isolates disequilibrium as the mechanism](cognitive-disequilibrium-motivates-conceptual-change.md) — a proposed mechanism linking manipulation to conceptual learning
- [Case-based learning improves exam performance](case-based-learning-improves-exam-performance.md) — an alternative contextualized, activity-based format
- [Physical Experience Enhances Science Learning](physical-experience-enhances-science-learning.md) — related
- [Concreteness fading guides learners to strip away extraneous concrete properties and distill generic, generalizable properties](fading-distills-generalizable-properties.md) — related
