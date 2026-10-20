---
type: claim
title: Cognitive Overload Degrades Learning
status: review
generated:
  by: claude/unspecified
  at: 2026-09-25
id: cognitive-overload-degrades-learning
evidence_strength:
sources:
  - id: noetel-et-al-2022
    resource: "https://doi.org/10.3102/00346543211052329"
    title: "Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., Parker, P., del Pozo Cruz, B., & Lonsdale, C. (2022). Multimedia design for learning: An overview of reviews with meta-meta-analysis. *Review of Educational Research, 92*(3), 413–454. [doi:10.3102/00346543211052329](https://doi.org/10.3102/00346543211052329)"
    author: "Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., Parker, P., del Pozo Cruz, B., & Lonsdale, C."
    q: 4
    i: 1
    n: 29 reviews (1,189 studies; 78,177 participants in the abstract, 79,415 in the Results)
    kind: quant-synthesis
    rigour: 2
  - id: sweller-1988
    resource: "https://doi.org/10.1207/s15516709cog1202_4"
    title: "Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. [doi:10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)"
    author: Sweller, J.
    q: 3
    i: "?"
    n: unreported (abstract only)
    kind: causal
    rigour: "?"
---

# Cognitive Overload Degrades Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r?`, 1 quant-synthesis `r2` · `q3`–`q4` · `i1` small

When the demands of a learning task exceed the capacity of working memory, learning suffers. This claim covers the general mechanism; specific load-reduction techniques are treated in their own pages.

## Subclaims

`q4 i1` Across 29 systematic reviews (1,189 studies, 78,177 participants per the abstract), multimedia design principles, many of them load-reducing, improved learning on average (g = 0.38, pooled across all principles in the 11 largest reviews), and the benefit was far larger for complex, high-element-interactivity materials (g = 0.70) than simple ones (g = 0.20), consistent with overload hurting learning mainly when total demand is high. [→ Noetel et al. 2022](#noetel-et-al-2022)

`q3 i?` Conventional means–ends problem solving uses so much processing capacity that little is left for schema acquisition, which the author supports with a computational model and experimental evidence; the abstract reports no effect size. [→ Sweller 1988](#sweller-1988)

## Evidence

### Noetel et al. 2022

Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., Parker, P., del Pozo Cruz, B., & Lonsdale, C. (2022). Multimedia design for learning: An overview of reviews with meta-meta-analysis. *Review of Educational Research, 92*(3), 413–454. [doi:10.3102/00346543211052329](https://doi.org/10.3102/00346543211052329)

`q4 · overview of systematic reviews with meta-meta-analysis` · `i1 · small-to-moderate average effect, g=0.38 (g=0.70 for complex materials)` · `n=29 reviews (1,189 studies; 78,177 participants in the abstract, 79,415 in the Results)` · `quant-synthesis · r2`

An overview of 29 systematic reviews testing how multimedia design affects learning or cognitive load. Pooling the 11 largest reviews (808 effect sizes), multimedia design principles as a whole improved learning (g = 0.38, 95% CI [0.27, 0.49]); the pool includes load-reducing principles such as contiguity, signaling, segmenting and removing seductive details, and others such as animation, anthropomorphics and pedagogical agents. The complexity of the material (element interactivity) moderated these effects: design mattered much more for complex media (g = 0.70) than for simple media (g = 0.20), which the authors read as support for the idea that complex materials are the ones likely to cause cognitive overload without good design. Learner prior knowledge did not significantly moderate effects, and the authors conclude that the expertise-reversal hypothesis was not supported by their analyses. This is indirect evidence: it tests *reducing* load, not inducing overload.

### Sweller 1988

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. [doi:10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)

`q3 · peer-reviewed experiments with a computational model` · `i? · no effect size in the abstract` · `n=unreported (abstract only)` · `causal · r?`

The founding cognitive load paper. It argues that conventional problem solving by means–ends analysis takes up a relatively large amount of cognitive processing capacity, leaving that capacity unavailable for schema acquisition, and so it is an ineffective way to learn. A computational model and experimental evidence are offered in support. Only the abstract was read here, so the experiments' samples and effect sizes are not recorded.

## Studies bearing on this claim

<!-- synthesis:start -->
*Does removing avoidable processing from a presentation improve learning?* This table gathers the studies behind this claim and the 10 narrower claims that bear on it: **10 distinct studies** (6 causal, 3 quant-synthesis, 1 associational), `q2`–`q4`, 4 of 10 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Noetel et al. 2022](https://doi.org/10.3102/00346543211052329) | q2 / q3 / q4 · quant-synthesis · r2 | i1 · small-to-moderate average effect, g=0.38 (g=0.70 for complex materials); i1; i2 | this claim; [Multimedia design interventions yield small average improvements in cognitive load managem](design-principles-improve-cognitive-load-management.md) (qualifies) |
| [Sweller 1988](https://doi.org/10.1207/s15516709cog1202_4) | q3 · causal · r? | i? | this claim |
| [Pollock et al. 2002](<https://doi.org/10.1016/s0959-4752(01)00016-0>) | q3 · causal · r? | i? | [Part-task practice reduces cognitive load for absolute novices during initial skill acquis](part-task-practice-reduces-load-for-novices.md) (supports) |
| [Rey et al. 2019](https://doi.org/10.1007/s10648-018-9456-4) | q4 · quant-synthesis · r? | i? | [Cognitive Load Management](cognitive-load-management.md) (supports) |
| [Barbieri et al. 2023](https://doi.org/10.1007/s10648-023-09745-1) | q4 · quant-synthesis · r? | i2 · medium effect, g=0.48 | [Cognitive Load Management](cognitive-load-management.md) (supports) |
| [Kala 2023](https://doi.org/10.36681/tused.2023.027) | q3 · causal · r1 | i?; i2 | [In one study of 37 thermodynamics freshmen, a CLT-based instructional design yields higher](clt-instructional-design-raises-retention-transfer-thermodynamics.md) (supports); [The CLT-based design produced higher effective learning scores at retention and transfer, ](clt-design-effective-learning-retention-transfer.md) (supports); [No significant difference between groups on the thermodynamics achievement post-test or co](no-group-difference-tat-posttest-cls.md) (qualifies) |
| [Rania Abdelghani 2026](https://doi.org/10.48550/arxiv.2606.08568) | q2 · associational · r2 | i? | [Higher extraneous cognitive load predicted lower post-test scores after controlling for pr](extraneous-load-predicts-lower-post-test.md) (supports) |
| Miwa et al. 2017 | q2 · causal · r1 | i0 | [Under high extraneous load (hint presentation and L and rL condition), no test-score incre](extraneous-load-eliminates-germane-load-learning-gains.md) (supports) |
| [Guttormsen Schär 2007](https://doi.org/10.1080/15391523.2007.10782497) | q2 · causal · r2 | i? | [Voice-based multimedia settings (animation+voice and picture+voice) produce better learnin](voice-media-outperform-picture-text-overall.md) (supports) |
| [Sweller & Cooper 1985](https://doi.org/10.1207/s1532690xci0201_3) | q3 · causal · r? | i? | [Worked examples reduce unnecessary search for novices.](worked-examples-reduce-novice-search.md) (supports) |
<!-- synthesis:end -->

## Discussion

**Mechanism.** Working memory can hold and process only a small number of elements at once. When intrinsic element interactivity (complexity of the material), extraneous load (poor presentation, irrelevant material), or both push total demand past that capacity, learners cannot construct or automate schemas, and performance degrades. This is the central prediction of [Cognitive Load Theory](../theories/cognitive-load-theory.md) and the theoretical basis for the related principle that [reducing cognitive load improves learning](cognitive-load-reduction-improves-learning.md).

**Sources of load.** Overload can arise from the material itself (high element interactivity for novices), from instructional design choices — e.g., split attention between diagram and text, redundant on-screen narration, irrelevant graphics — or from learner-generated inefficiencies such as means–ends search during unguided problem-solving. Designers control the second and third sources; see [Cognitive Load Reduction](../principles/cognitive-load-management.md) and [Chunking](../principles/chunking.md).

**Moderators.** The point at which load becomes "overload" depends on learner expertise (the [expertise reversal effect](../theories/expertise-reversal-effect.md)): scaffolds that reduce load for novices can add redundant load for experts. It also depends on prior knowledge activation, element interactivity of the domain, and whether load measurement distinguishes productive from unproductive effort. Note that some desirable difficulties — e.g., [generative](active-learning-improves-exam-performance.md) or effortful retrieval — impose load that *supports* learning; the claim applies to load that exceeds capacity, not to effort per se.

**Boundary conditions.** The claim is directional but conditional: it predicts degradation only when total demand genuinely exceeds capacity. Moderate challenge within capacity can be productive — see [Conflict-based instruction improves science conceptual learning, though staged contradictions helped only learners who reported being confused, and no study isolates disequilibrium as the mechanism](cognitive-disequilibrium-motivates-conceptual-change.md). Designers should therefore treat load reduction as a means of freeing capacity for [generative processing](cognitive-load-management.md), not as an end in itself; stripping all effort from a task risks disengagement.

**Design implications.** Practical countermeasures follow directly from the mechanism: [chunking](chunking-reduces-working-memory-load.md) complex material into integrated units, removing extraneous elements (coherence), integrating text and diagrams to avoid split attention, and sequencing instruction so that element interactivity rises as schemas are automated. Load reduction is most valuable for novices facing high-element-interactivity material; for advanced learners the same supports can backfire.

**Open questions.** Two studies are recorded: an overview of 29 systematic reviews in which load-reducing multimedia designs helped most for complex materials (g = 0.70 against 0.20 for simple ones), and Sweller's (1988) founding paper, read as an abstract only. Neither tests load-measurement validity, and no entry here measures overload directly rather than inferring it from design manipulations. <!-- deprecated 2026-10-05 (stale; two entries exist): Evidence for this page still needs to be added — including the foundational experimental and meta-analytic work on load effects and load-measurement validity. Until then, treat the claim as well-established theoretically but under-sourced here. -->

## Learner Variables
- [Working Memory](../learner-variables/working-memory.md) — predictor: learners who differ on it differ in outcomes

## Related Claims

- [Design principle effects are larger in system-paced and in complex media, and learner prior knowledge was not a significant moderator (p = 0.14)](design-principle-effects-moderated-by-pacing-and-complexity.md) — the general claim this finding bears on, with the studies behind it

- [Coherence principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) — extraneous material is a direct source of overload
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — a primary design countermeasure
- [Worked examples can become redundant or counterproductive for advanced learners](worked-examples-less-effective-with-expertise.md) — expertise moderates when load-reducing scaffolds help
- [Automatic word recognition frees resources for comprehension](automatic-word-recognition-frees-resources-for-comprehension.md) — automaticity lowers load in literacy tasks
- [Conflict-based instruction improves science conceptual learning, though staged contradictions helped only learners who reported being confused, and no study isolates disequilibrium as the mechanism](cognitive-disequilibrium-motivates-conceptual-change.md) — moderate challenge can be productive; overload is the failure point beyond it
- [Clear Structure Improves Learning](clear-structure-improves-learning.md) — related
- [Cognitive Load Reduction Improves Learning](cognitive-load-reduction-improves-learning.md) — a narrower finding that bears on this claim
- [Cognitive Load Management](cognitive-load-management.md) — related
- [Multimedia Principles Benefit Novices](expertise-reversal-effect.md) — related
- [Signaling Improves Learning](signaling-improves-learning.md) — related
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](part-task-practice-reduces-load-for-novices.md) — a narrower finding that bears on this claim
- [Individual user goals, such as avoiding cognitive load, can contradict the objectives of the educational community](user-goals-contradict-educational-objectives.md) — related
- [Reported limitations of AR enhanced analytics include cognitive overload from immersive environments, technological constraints, usability challenges, and inconsistent measurement approaches](ar-analytics-limitations-cognitive-overload-inconsistency.md) — related
- [ARPG+ shifts cognitive load composition toward productive effort and reduces overload frequency in simulation](arpg-plus-load-composition-shift-and-overload-reduction.md) — a narrower finding that bears on this claim
- [Multimedia design principles improve learning by g = 0.38 on average across the 11 largest reviews, an effect the authors call moderate, with large differences between principles](multimedia-design-principles-improve-learning-overall.md) — related
- [The learning benefit of increasing integration is substantially larger for high element interactivity (complex) materials than for low element interactivity materials](element-interactivity-moderates-contiguity-effect.md) — related
- [Weeding extraneous information such as music and complex backgrounds improves retention and transfer from video](weeding-extraneous-content-improves-video-learning.md) — a narrower finding that bears on this claim
- [Real-life complex tasks carry high intrinsic cognitive load, requiring new load-management methods](real-life-tasks-high-intrinsic-load-need-management.md) — related
- [Studying worked examples is more effective and more efficient than problem solving for novice learners (the worked example effect)](worked-example-effect-novices-review.md) — a narrower finding that bears on this claim
- [Material difficulty is not determined solely by element number and interactivity](difficulty-beyond-element-interactivity.md) — related
- [Extraneous cognitive load arising from limited scope and high distance in the rule-based game pushed the facilitator toward first- and second-order interventions instead of the third-order interventions the learning goal required](extraneous-load-shifts-facilitator-to-fol-interventions.md) — a narrower finding that bears on this claim
- [Multimedia learning principles are not clearly attributable to the multicomponent model or to applied multimedia theories](multimedia-principles-not-attributable-to-multicomponent-model.md) — related
- [Struggling participants in the rule-based game initiated emergent facilitation — self-organized peer facilitation — which was fuelled by cognitive load, scope disturbances and high distance and supported first- and second-order learning](emergent-facilitation-by-participants-in-rule-based-sg.md) — related
- [Variations in material design are reflected in the extraneous cognitive load scale: worked examples and integrated formats lower ECL](design-variations-reflected-in-ecl-scale.md) — a narrower finding that bears on this claim
- [The worked example effect holds for the schema-acquisition goal, but other instructional goals may be better served by other means](worked-example-effect-goal-dependent.md) — related
- [No significant difference between groups on the thermodynamics achievement post-test or cognitive load scale after CLT-based versus lecturer-designed instruction](no-group-difference-tat-posttest-cls.md) — a narrower finding that bears on this claim
- [Segmenting Improves Multimedia Learning](segmenting-improves-multimedia-learning.md) — related
- [In one study of 37 thermodynamics freshmen, a CLT-based instructional design yields higher retention and transfer scores than lecturer-designed instruction, controlling for prior knowledge and memory span](clt-instructional-design-raises-retention-transfer-thermodynamics.md) — a narrower finding that bears on this claim
- [The worked example effect is explained by reduced element interactivity relative to problem solving, and reverses with expertise](worked-example-effect-element-interactivity-explanation.md) — a narrower finding that bears on this claim
- [Under high extraneous load (hint presentation and L and rL condition), no test-score increases were observed on identical or near-transfer problems](extraneous-load-eliminates-germane-load-learning-gains.md) — a narrower finding that bears on this claim