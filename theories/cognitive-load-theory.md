---
type: theory
title: Cognitive Load Theory
description: Cognitive Load Theory (CLT) proposes that learning is constrained by the limited capacity of working memory.
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-08-29
sources:
  - id: sweller-1988
    resource: "https://doi.org/10.1207/s15516709cog1202_4"
    title: "Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285"
    author: Sweller, J
  - id: sweller-1998
    resource: "https://doi.org/10.1023/A:1022193728205"
    title: "Sweller, J., van Merriënboer, J. J. G., & Paas, F. G. W. C. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296"
    author: "Sweller, J., van Merriënboer, J. J. G., & Paas, F. G. W. C"
  - id: paas-2003
    resource: "https://doi.org/10.1207/S15326985EP3801_1"
    title: "Paas, F., Renkl, A., & Sweller, J. (2003). Cognitive load theory and instructional design: Recent developments. *Educational Psychologist, 38*(1), 1–4"
    author: "Paas, F., Renkl, A., & Sweller, J"
  - id: sweller-2019
    resource: "https://doi.org/10.1007/s10648-019-09465-5"
    title: "Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292"
    author: "Sweller, J., van Merriënboer, J. J. G., & Paas, F"
  - id: van-merriënboer-2018
    resource: "https://doi.org/10.4324/9781315113210"
    title: "van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge"
    author: "van Merriënboer, J. J. G., & Kirschner, P. A"
moved_from: [pattern/cognitive-load-theory]
---

# Cognitive Load Theory

> **Theory** · [All theories](index.md)
> **Evidence** · 119 claims (76 for, 33 mixed, 10 against) · 99 studies (42 causal, 23 review, 19 theoretical, 12 quant-synthesis, 2 design, 1 associational), `q1`–`q4` · 21 of 99 report an effect size · 108 claims rest on one study

## Description
Cognitive Load Theory (CLT) proposes that learning is constrained by the limited capacity of working memory. When the total cognitive demand of a learning task exceeds that capacity, learning breaks down — not because the learner lacks ability, but because the instructional design has exhausted the resources available for processing. The theory distinguishes three sources of load and argues that effective instruction reduces unnecessary load to free capacity for the mental work that actually builds schema.

CLT was developed by John Sweller and colleagues in the 1980s–1990s, drawing on George Miller's work on working memory limits and Alan Baddeley's model of working memory components. Its central claim is that instructional design should treat working memory capacity as the binding constraint: the question is not just "what should I teach?" but "how much mental demand does this design impose, and on what?"

## Three Types of Load

**Intrinsic load** is inherent to the material itself — determined by the number of interacting elements the learner must hold in mind simultaneously. High-element-interactivity content (e.g., parsing a sentence, debugging a recursive function) cannot be simplified without distorting it; but it can be sequenced so simpler schemas are built first.

**Extraneous load** is imposed by poor instructional design — split-attention effects, redundant information, unnecessary navigation, irrelevant detail. Extraneous load consumes working memory capacity without contributing to learning. This is the type CLT most directly targets: the primary design goal is to eliminate it.

**Germane load** (in revised CLT) refers to the cognitive effort invested in schema construction and automation — the work that actually produces learning. Earlier formulations treated germane load as a third type to be increased; current CLT treats it as the portion of intrinsic load that is productively engaged, not a separate load type.

## Implications

### Context
- Applies wherever learning requires holding multiple interacting elements in working memory simultaneously — mathematics, programming, language acquisition, clinical reasoning, reading comprehension
- Effect is strongest with novices; as expertise develops, previously separated elements are chunked into single schemas and cease to impose separate load demands (the basis of the [expertise reversal effect](expertise-reversal-effect.md))
- Design choices that reduce extraneous load are never harmful; but scaffolding that reduces intrinsic load too aggressively can prevent the element-interactivity processing needed for schema formation
- Additions intended to make material more *interesting* rather than to reduce load can themselves become an extraneous-load source — see [Seductive details can distract from learning](../claims/seductive-details-effect.md) [-M]

### Target Learners
- Novices with limited prior knowledge in the domain benefit most from CLT-informed design
- Experts may find the same scaffolds redundant or distracting — what reduces load for a novice can introduce it for an expert
- Learners with limited working memory capacity (e.g., younger children, learners under high cognitive stress) are most sensitive to extraneous load
- Especially useful for novices in complex domains.

### Target Learning Objectives
- Procedural skill acquisition: learning to execute multi-step processes
- Conceptual understanding of content with high element interactivity
- Transfer: schema formation is the mechanism by which knowledge transfers to new problems

## Claims

- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-example-problem-sequences.md) [+M] — example-based sequences reduce load compared to problem-only practice for novices; provides direct experimental evidence for the worked example effect as a CLT application
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M] — worked examples reduce unnecessary search load, freeing working memory for schema construction
- [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — expertise reversal: as schemas develop, the same guidance that reduced load for novices begins to impose redundancy load on more experienced learners
- [Redundancy Effect Impairs Learning](../claims/redundancy-principle.md) [+W]
- [Cognitive Load Reduction Improves Learning](../claims/cognitive-load-reduction-improves-learning.md) [+M]
- [Cognitive Load Management](../claims/cognitive-load-management.md) [+M]
- [Split Attention Effect Degrades Learning](../claims/split-attention-effect-degrades-learning.md) [+M]
- [On-screen text that duplicates the narration of a diagram can hurt learning, but spoken–written redundancy is not harmful on average and helps over spoken-only presentation in some conditions](../claims/redundancy-hurts-learning.md) [+M]
- [Segmenting Improves Multimedia Learning](../claims/segmenting-improves-multimedia-learning.md) [+M]
- [Minimal guidance is less effective for novices than explicit instruction](../claims/minimal-guidance-less-effective-for-novices.md) [~M]
- [The authors conclude real-time AI feedback reduces extraneous cognitive load and mitigates fear of failure with expensive laboratory equipment](../claims/ai-feedback-reduces-cognitive-load-and-fear-of-failure.md) [+W] — attached 2026-10-11 from Nuhu et al. (2026), which proposed "Real-time AI feedback as digital scaffolds bridging feedback latency"; tests this page's relationship.
- [ARPG+ shifts cognitive load composition toward productive effort and reduces overload frequency in simulation](../claims/arpg-plus-load-composition-shift-and-overload-reduction.md) [+W] — attached 2026-10-12 from Ye et al. (2026), which proposed "Operationalizing cognitive load theory and ZPD into real-time coaching signals"; tests this page's relationship.
- [Minimally guided instruction is less effective and less efficient than instruction that places a strong emphasis on guidance of the student learning process](../claims/minimally-guided-instruction-less-effective-than-strong-guidance.md) [+W] — attached 2026-10-13 from Kirschner et al. (2006), which proposed "Human cognitive architecture, expert-novice differences, and cognitive load as the explanatory framework for the superiority of guided instruction".
- [The advantage of guidance begins to recede only when learners have sufficiently high prior knowledge to provide internal guidance](../claims/guidance-advantage-recedes-with-high-prior-knowledge.md) [+W] — attached 2026-10-13 from Kirschner et al. (2006), which proposed "Human cognitive architecture, expert-novice differences, and cognitive load as the explanatory framework for the superiority of guided instruction"; tests this page's relationship.
- [Segmentation reduces overall cognitive load during multimedia learning](../claims/segmenting-reduces-cognitive-load.md) [+W] — attached 2026-10-13 from Rey et al. (2019), which proposed "Explanatory accounts of the segmenting effect: designer-imposed chunking and structuring, more processing time, and individual pace adaptation"; tests this page's relationship.
- [Germane cognitive load is reformulated as redistributing working memory resources from extraneous to intrinsic processing rather than adding to total load](../claims/germane-load-redistributive-function-reformulation.md) [~W]
- [Directive feedback is associated with higher cognitive load than Socratic feedback, with no agent-type effects on learning experiences](../claims/directive-feedback-higher-cognitive-load.md) [~W]
- [Modality effect: hearing text alongside visuals improves learning more than reading text alongside visuals](../claims/modality-effect-narration-over-text.md) [+W] — attached 2026-10-13 from Noetel et al. (2022), which proposed "Cognitive Theory of Multimedia Learning: dual-channel, limited-capacity, active processing"; tests this page's relationship.
- [ADA use shows a modest non-significant tendency toward increased intrinsic and extrinsic cognitive load, contrary to prior chatbot research](../claims/ada-cognitive-load-slightly-increased-non-significant.md) [~W]
- [GenAI training leaves total cognitive load comparable while marginally raising intrinsic cognitive load](../claims/genai-training-comparable-load-marginal-intrinsic-increase.md) [~W]
- [Split-attention worked examples lose their advantage over conventional practice, while integrated formats restore it](../claims/split-attention-effect-in-worked-examples.md) [+W] — attached 2026-10-13 from Atkinson et al. (2000), which proposed "A three-factor causal framework organizes the factors that influence learning from worked examples"; tests this page's relationship.
- [Structuring worked examples to emphasize subgoals, via labels or visual segmentation, enhances transfer to novel problems](../claims/subgoal-labels-worked-examples-transfer.md) [+W] — attached 2026-10-13 from Atkinson et al. (2000), which proposed "A three-factor causal framework organizes the factors that influence learning from worked examples".
- [Presentation pacing moderates the modality effect: large under system-paced conditions and not significant under self-paced conditions, where it may disappear or reverse](../claims/modality-effect-moderated-by-pacing.md) [~W] — attached 2026-10-13 from Ginns (2005), which proposed "Cognitive load theory account of the modality effect via dual working-memory channels"; tests this page's relationship.
- [The learning benefit of increasing integration is substantially larger for high element interactivity (complex) materials than for low element interactivity materials](../claims/element-interactivity-moderates-contiguity-effect.md) [+W] — attached 2026-10-13 from Ginns (2006), which proposed "Cognitive Load Theory account of split-attention costs"; tests this page's relationship.
- [Integrating spatially or temporally separated but related elements of instructional information produces a large average learning benefit for novices](../claims/integration-of-related-elements-large-mean-effect.md) [+W] — attached 2026-10-13 from Ginns (2006), which proposed "Cognitive Load Theory account of split-attention costs".
- For novice learners of complex information, the isolated-interacting elements instructional method produces superior learning compared with conventional instruction presenting all interacting information throughout [+W] — attached 2026-10-15 from Pollock (2000), which proposed "The isolated-interacting elements two-phase instructional approach"; tests this page's relationship.
- Experiment 5 showed superior performance for learners who had previously studied isolated elements followed by interacting elements instruction, supporting expertise as the key factor in the technique's benefits [+W] — attached 2026-10-15 from Pollock (2000), which proposed "The isolated-interacting elements two-phase instructional approach"; tests this page's relationship.
- [Segmenting complex dynamic visualizations into pieces with pauses improves learning outcomes, especially transfer performance, at least for novices, compared with non-segmented presentations](../claims/segmentation-improves-learning-dynamic-visualizations.md) [+W] — attached 2026-10-15 from Spanjers et al. (2010), which proposed "Cognitive load / transience account: segmentation reduces extraneous load from information transience by dividing content into smaller units and providing processing pauses"; tests this page's relationship.
- [Segmentation of dynamic visualizations shows an expertise reversal effect: students with lower prior knowledge benefit, while students with higher prior knowledge learn equally well with or without segmentation](../claims/segmentation-benefits-shrink-with-expertise.md) [+W] — attached 2026-10-15 from Spanjers et al. (2010), which proposed "Cognitive load / transience account: segmentation reduces extraneous load from information transience by dividing content into smaller units and providing processing pauses"; tests this page's relationship.
- [The element interactivity effect relies on changes in element interactivity due to changes in the type of material being learned](../claims/element-interactivity-changes-from-material-type.md) [+W] — attached 2026-10-15 from Chen et al. (2017), which proposed "Unified cognitive load account: the expertise reversal effect as a variant of the element interactivity effect".
- [The expertise reversal effect relies on changes in relative levels of element interactivity due to changes in relative levels of expertise](../claims/expertise-reversal-changes-from-expertise-levels.md) [+W] — attached 2026-10-15 from Chen et al. (2017), which proposed "Unified cognitive load account: the expertise reversal effect as a variant of the element interactivity effect".
- [In its traditional treatment, germane cognitive load is essentially indistinguishable from intrinsic load and may be a redundant concept](../claims/germane-load-indistinguishable-from-intrinsic-load.md) [-W] — attached 2026-10-15 from Kalyuga (2011), which proposed "Redefined germane load as actual working memory resources devoted to dealing with intrinsic rather than extraneous load".
- [Emotions may act as extraneous cognitive load by competing for limited working memory resources with task-irrelevant processing](../claims/emotion-as-extraneous-cognitive-load.md) [+W] — attached 2026-10-15 from Plass et al. (2019), which proposed "Four-perspective taxonomy of emotion–cognitive load relationships understood through an interval view of cognitive load".
- [Emotion may affect intrinsic cognitive load, for example when emotion regulation is part of the learning outcomes](../claims/emotion-as-intrinsic-load-emotion-regulation.md) [+W] — attached 2026-10-15 from Plass et al. (2019), which proposed "Four-perspective taxonomy of emotion–cognitive load relationships understood through an interval view of cognitive load".
- [Reduction of cognitive load can sometimes impair learning rather than enhance it](../claims/load-reduction-can-impair-learning.md) [~W] — attached 2026-10-15 from Schnotz et al. (2007), which proposed "Zone of proximal development perspective on cognitive load theory".
- [Germane cognitive load fully mediates the effect of information-search tool on justification quality (exploratory analysis)](../claims/germane-load-mediates-tool-effect-on-justification-quality.md) [+W] — attached 2026-10-15 from Matthias Stadler et al. (2024), which proposed "Cognitive load–self-regulation tradeoff account of information-search tool effects on learning quality"; tests this page's relationship.
- [For circle geometry problems, guidance in the form of subgoals or worked examples increased cognitive load during problem processing (Experiments 1-3)](../claims/guidance-subgoals-worked-examples-increase-cognitive-load-geometry.md) [+W] — attached 2026-10-16 from Ahmad Tarmizi (1991), which proposed "Split-attention cognitive load account of guidance effects"; tests this page's relationship.
- [When guidance was presented in a unitary (integrated) format, worked examples were superior to conventional problems (Experiments 4 and 5)](../claims/unitary-format-worked-examples-superior-conventional-problems.md) [+W] — attached 2026-10-16 from Ahmad Tarmizi (1991), which proposed "Split-attention cognitive load account of guidance effects"; tests this page's relationship.
- [Under many circumstances, studying worked examples produced superior learning compared to active problem solving, as suggested by previous research](../claims/worked-examples-superior-to-problem-solving-many-circumstances.md) [+W] — attached 2026-10-16 from Ahmad Tarmizi (1991), which proposed "Means-ends analysis as a problem-solving strategy that inhibits learning".
- [Studying worked examples is more effective and more efficient than problem solving for novice learners (the worked example effect)](../claims/worked-example-effect-novices-review.md) [+W] — attached 2026-10-16 from Tamara van Gog et al. (2010), which proposed "Cognitive load explanation of why worked examples outperform unsupported problem solving for novices"; tests this page's relationship.
- [Expertise reversal: high-guidance worked examples become ineffective or detrimental once learners have developed cognitive schemata](../claims/expertise-reversal-worked-examples.md) [+W] — attached 2026-10-16 from Tamara van Gog et al. (2010), which proposed "Cognitive load explanation of why worked examples outperform unsupported problem solving for novices"; tests this page's relationship.
- [2D pedagogical agents tended to be more effective than 3D agents (g+ = 0.38 vs. g+ = 0.11), as predicted by the redundancy effect and the coherence principle](../claims/2d-agents-tend-more-effective-than-3d.md) [+W] — attached 2026-10-17 from Castro-Alonso et al. (2021), which proposed "Cognitive load theory (redundancy effect) and cognitive theory of multimedia learning (coherence principle) as the account predicting agent dimensionality effects".
- [Retrieval practice conditions produced significantly higher cognitive load than rereading](../claims/retrieval-practice-increases-cognitive-load.md) [+W] — attached 2026-10-18 from Redifer et al. (2026), which proposed "Cognitive load balance account of the testing effect with advanced materials".
- [In Study 1, a greater seductive detail amount linearly worsened recall performance (b = −0.11, p = .030)](../claims/sd-amount-linear-negative-recall-study1.md) [+W] — attached 2026-10-18 from Lukas Wesenberg et al. (2026), which proposed "Three cognitive-process accounts of the seductive details effect: distraction, disruption, and diversion theory"; tests this page's relationship.
- [Seductive detail amount did not increase extraneous cognitive load in either study](../claims/sd-amount-no-extraneous-load-effect.md) [-W] — attached 2026-10-18 from Lukas Wesenberg et al. (2026), which proposed "Three cognitive-process accounts of the seductive details effect: distraction, disruption, and diversion theory"; tests this page's relationship.
- [Lower-prior-knowledge apprentices experienced higher germane cognitive load when learning with retrospective prompts than with anticipatory prompts](../claims/retrospective-prompts-higher-germane-load-low-prior-knowledge.md) [+W] — attached 2026-10-18 from Meier et al. (2024), which proposed "Cognitive load theory (1998 conception) as the explanatory framework for prompt-direction and expertise effects in example-based learning"; tests this page's relationship.
- [In an immersive VR learning environment, visual-only text yields higher recall than audio-visual text (reverse modality effect)](../claims/vr-reverse-modality-effect-recall.md) [+W] — attached 2026-10-18 from Patrick Albus (2023), which proposed "Boundary-condition account of the reverse modality effect in immersive VR".
- [Visual-only text produces higher germane cognitive load than audio-visual text in VR](../claims/vr-visual-only-higher-germane-load.md) [+W] — attached 2026-10-18 from Patrick Albus (2023), which proposed "Boundary-condition account of the reverse modality effect in immersive VR".
- [A forward linear review strategy predicted lower cognitive load regardless of modality, while scanning and slowing predicted higher cognitive load](../claims/linear-strategy-lower-cognitive-load.md) [+W] — attached 2026-10-18 from Mikko Haavisto (2026), which proposed "The modality effect grounded in cognitive load theory, with hybrid learner control as a dual-advantage design".
- [The claim that high-variability practice imposes germane load rests on post-hoc explanation and does not always replicate](../claims/high-variability-germane-load-post-hoc.md) [-W]
- [Higher germane load and lower extraneous load mediate the effect of instructional guidance on conceptual knowledge](../claims/cognitive-load-mediates-guidance-effect.md) [+W]
- [Reducing extraneous load can also remove affordances for germane processes](../claims/extraneous-load-reduction-may-remove-germane-affordances.md) [~W]
- [Cognitive load showed no significant mediation of the effects of navigation features or self-explanation prompts on video learning outcomes](../claims/cognitive-load-no-mediation-video-learning.md) [-W]
- [The intrinsic–extraneous–germane distinction is conceptually problematic: definitions are tautological and expertise-dependent](../claims/load-type-distinction-conceptually-problematic.md) [-W]
- [Disfluency benefits retention and comprehension only for learners with high working memory capacity](../claims/disfluency-benefits-high-working-memory-only.md) [~W]
- [Current cognitive load measures cannot detect overload because the critical level indicating overload is unknown](../claims/load-measures-cannot-detect-overload.md) [-W]
- [Collaborative learning distributes cognitive load across multiple working memories, aiding learning of high-load tasks](../claims/collaborative-learning-collective-working-memory-advantage.md) [+W]
- [Cognitive load in concurrent storage-processing tasks has a negative linear effect on memory span](../claims/cognitive-load-negative-linear-span-effect.md) [+W]
- [Cognitive Load Theory lacks a motivational focus, which becomes problematic when interpreting interventions that foster effortful learning strategies](../claims/clt-motivation-gap.md) [-W]
- [A dual-channel assumption for emotions is discussed as part of integrating emotion into cognitive load theory](../claims/dual-channel-assumption-emotions-clt.md) [~W]
- [The article analyzes the consequences of explaining the various cognitive load effects in terms of element interactivity](../claims/cognitive-load-effects-reexplained-via-element-interactivity.md) [+W]
- [The definitions of cognitive load used in cognitive load theory are not fully equivalent](../claims/cognitive-load-definitions-not-equivalent.md) [~W]
- [A dual intrinsic/extraneous load framework is sufficient, non-redundant, and makes the boundaries of cognitive load theory transparent](../claims/dual-intrinsic-extraneous-framework-sufficient.md) [~W]
- [Dual-task (secondary-task) measures offer concurrent cognitive load assessment but are rarely used](../claims/dual-task-concurrent-load-measurement.md) [~W]
- [Element interactivity underlies extraneous cognitive load as well as intrinsic cognitive load](../claims/element-interactivity-underlies-extraneous-load.md) [~W]
- [Germane cognitive load was added to the cognitive load framework on theoretical grounds rather than because of empirical results requiring the concept](../claims/germane-load-added-on-theoretical-not-empirical-grounds.md) [~W]
- [Germane cognitive load can be defined in terms of intrinsic cognitive load, associating it with element interactivity](../claims/germane-load-defined-via-intrinsic-load.md) [+W]
- [Learning with erroneous examples often imposed higher cognitive load than correct examples or problem-solving](../claims/errex-higher-cognitive-load.md) [~W]
- [Extraneous cognitive load did not mediate the detrimental effect of seductive details in this online study](../claims/ecl-mediation-not-replicated-online.md) [~W]
- [Both effects are claimed to rely on equivalent changes in element interactivity, with the changes induced by different factors](../claims/equivalent-element-interactivity-changes-both-effects.md) [~W]
- [Self-reported intrinsic and germane cognitive load correlate positively among college students solving algebra problems](../claims/intrinsic-and-germane-cognitive-load-correlate-positively-in-algebra.md) [~W]
- [Working memory load degrades discrimination accuracy and slows responses in youth](../claims/load-degrades-discrimination-and-slows-responses.md) [+W]
- [Learning with multiple representations imposes high demands and often fails to produce expected results because learners do not integrate the representations](../claims/multi-representational-learning-integration-failure.md) [+W]
- [Children too young to use attentional refreshing are limited by retention interval duration, while older children and adults are limited by cognitive load](../claims/refreshing-phase-change-in-childhood.md) [~W]
- [Weeding extraneous information such as music and complex backgrounds improves retention and transfer from video](../claims/weeding-extraneous-content-improves-video-learning.md) [+W]
- [Working memory demand increases with the complexity of arithmetic and math problems, including operand size and number of solution steps](../claims/working-memory-demand-increases-with-math-problem-complexity.md) [+W]
- Correlations of cognitive load types with learning outcomes and prior knowledge support CLT assumptions, and results support the three-factor model [+W] — attached 2026-10-19 from Felix Krieglstein et al. (2022), which proposed "Three-factor model of cognitive load: intrinsic, extraneous, and germane load additively contributing to overall load"; tests this page's relationship.
- [Correlations among cognitive load types partially contradict theory-based assumptions of the additivity hypothesis](../claims/load-type-correlations-partially-contradict-clt.md) [-W] — attached 2026-10-19 from Felix Krieglstein et al. (2022), which proposed "Three-factor model of cognitive load: intrinsic, extraneous, and germane load additively contributing to overall load"; tests this page's relationship.
- [Element interactivity can be estimated by counting interacting elements, illustrated with about 28 elements for solving a/b = c and about 25 for a composite geometry area problem](../claims/counting-interacting-elements-examples.md) [+W]
- [Warning-only LA feedback can increase mental load, whereas pairing warnings with encouragement leads to higher emotional and cognitive engagement](../claims/la-feedback-warnings-encouragement-cognitive-load.md) [+W]
- [Chen et al. (2018): spaced practice superiority was associated with increased availability of working memory resources](../claims/chen-2018-spaced-superiority-associated-with-wm-recovery.md) [+W] — attached 2026-10-21 from Ouhao Chen et al. (2021), which proposed "Spacing effect as a cognitive load effect: working memory resource depletion during learning with recovery during rest-from-deliberate-learning"; tests this page's relationship.
- [Collaborating learners learn more effectively and efficiently than individual learners on cognitively challenging tasks, but group work becomes disadvantageous on cognitively unchallenging tasks](../claims/task-complexity-moderates-group-learning-advantage.md) [~W] — attached 2026-10-21 from Janssen et al. (2010), which proposed "Groups as information processing systems: a cognitive load account of collaborative learning balancing distribution advantage against transaction costs".
- [Element interactivity and expertise reversal effects: cognitive load effects diminish and may reverse as expertise increases because known elements chunk into single elements](../claims/expertise-reversal-effect-element-interactivity.md) [+W] — attached 2026-10-21 from John Sweller (2023), which proposed "Current cognitive load theory: biologically secondary knowledge, limited working memory, vast long-term memory, and element interactivity determining intrinsic and extraneous load"; tests this page's relationship.
- [Redundancy effect: when one source of information is intelligible in isolation, physically integrating it with another source fails to help and eliminating the redundant source facilitates learning](../claims/redundancy-effect-elimination-of-redundant-text.md) [+W] — attached 2026-10-21 from John Sweller (2023), which proposed "Current cognitive load theory: biologically secondary knowledge, limited working memory, vast long-term memory, and element interactivity determining intrinsic and extraneous load"; tests this page's relationship.
- [Transient information effect: lengthy spoken text can reverse the modality effect, while shorter spoken text restores the conventional modality advantage](../claims/transient-information-effect-reverse-modality-length.md) [+W]
- [Biologically primary motor actions such as finger tracing can provide cognitive benefits without causing cognitive load](../claims/primary-motor-actions-benefits-without-load.md) [+W] — attached 2026-10-21 from Alexander Skulmowski (2024), which proposed "Integrated cognitive framework for analyzing activity-based learning: cognitive load theory, biologically primary/secondary knowledge, and layers of action planning".
- [LLM-supported socio-scientific inquiry lowered cognitive load but produced lower-quality reasoning and argumentation than conventional search](../claims/llm-inquiry-lower-load-lower-reasoning.md) [~W]
- [Coherence principle: people learn better when extraneous material is excluded rather than included (d = 0.86 across 19 tests)](../claims/coherence-principle-extraneous-material-effect.md) [+W]
- [CLT can serve as a framework for teaching generalized knowledge and skills, including learning strategies](../claims/clt-framework-generalized-skills.md) [+W]
- [The results suggest a new interpretation of intrinsic and extrinsic load as related to the time needed to process information](../claims/load-interpretation-time-to-process.md) [~W]
- [Cognitive Load Theory has traditionally used slot-based working memory capacity models](../claims/clt-traditionally-used-slot-models.md) [~W]
- [Tracing and pointing lowers extraneous cognitive load under a floor-effect-adjusted test, but not in the unadjusted comparison](../claims/tracing-pointing-lower-extraneous-load-floor-effect.md) [+W] — attached 2026-10-21 from Yining Wang et al. (2025), which proposed "Biologically primary tracing and pointing actions support acquisition of biologically secondary knowledge (cognitive load theory evolutionary account)"; tests this page's relationship.
- [Tracing and pointing does not significantly reduce self-reported intrinsic cognitive load](../claims/tracing-pointing-no-intrinsic-load-reduction.md) [~W] — attached 2026-10-21 from Yining Wang et al. (2025), which proposed "Biologically primary tracing and pointing actions support acquisition of biologically secondary knowledge (cognitive load theory evolutionary account)".
- [Task difficulty shows an inverted U-shaped relation with cognitive strategy use and a positive linear relation with metacognitive strategy use, mediated by cognitive load (Seufert et al., 2024)](../claims/task-difficulty-inverted-u-strategy-use.md) [~W]
- [Animations often do not produce more effective learning than static visualizations, partly because their transience creates high working memory load](../claims/animations-transience-working-memory-load.md) [+W]
- [In the new questionnaire, ICL and ECL correlate positively while both correlate negatively with GCL](../claims/icl-ecl-positive-gcl-negative-correlations.md) [+M] — attached 2026-10-22 from Krieglstein et al. (2023), which proposed "Three types of cognitive load within Cognitive Load Theory: intrinsic, extraneous, and germane".
- [Gesturing while explaining problem solving reduces cognitive load](../claims/gesturing-reduces-cognitive-load.md) [+W]
- [The model's assumed negative correlation between cognitive load and learner resources was not supported; the overall correlation was positive](../claims/load-resources-negative-correlation-not-supported.md) [-W]
- [For metacognitive strategy use, resources competitively mediate the linear effect and cognitive load partially mediates the linear and mediates the quadratic relationship](../claims/mediation-metacognitive-strategies-load-resources.md) [~W]
- [Learning with more than two external representations in STEM has advantageous effects on students' cognitive load and performance compared to learning with two representations.](../claims/more-than-two-representations-benefit-load-and-performance.md) [~W]
- [Embodied action can harm learning when it adds motor demands, redundant cues, or irrelevant activity without improving understanding](../claims/action-hurts-when-adding-motor-demands.md) [+W] — attached 2026-10-22 from Fred Paas et al. (2026), which proposed "Embodied guidance fading: least embodied task-relevant support matched to knowledge and element interactivity, then faded as schemas develop".
- [CSCL environments in which students share external representations share characteristics that induce considerable cognitive load](../claims/cscl-environments-induce-considerable-cognitive-load.md) [+M] — attached 2026-10-22 from Bruggen et al. (2002), which proposed "Cognitive load theory as an analytical framework for CSCL: pinpointing situations of high cognitive load and mismatches between representations and tasks".
- [On the delayed test, a significant three-way interaction showed a worked example effect for high element interactivity material and a generation effect for low element interactivity material for novices](../claims/delayed-test-three-way-interaction-element-interactivity-guidance-expertise.md) [+W] — attached 2026-10-22 from Relations Between the Worked Example et al. (2016), which proposed "Element interactivity as the cognitive load theory measure reconciling the worked example and generation effects"; tests this page's relationship.
- [Expertise produced large main effects on test scores and interacted with element interactivity, with the expertise advantage much larger for high element interactivity material](../claims/expertise-main-effect-and-element-interactivity-interaction.md) [+W] — attached 2026-10-22 from Relations Between the Worked Example et al. (2016), which proposed "Element interactivity as the cognitive load theory measure reconciling the worked example and generation effects"; tests this page's relationship.
- [Mismatch between recording angle and expected angle increases cognitive load both during video observation and during task execution](../claims/expectation-mismatch-increases-cognitive-load.md) [+W] — attached 2026-10-23 from de Jonge et al. (2026), which proposed "Expectation Alignment Hypothesis (EAH)"; tests this page's relationship.
- [Participants informed in advance about a misaligned task angle performed worse and reported higher video cognitive load than those surprised by the misalignment](../claims/informed-misalignment-worse-performance.md) [~W]
- [Intrinsic cognitive load during the scenario negatively predicted problem-solving performance (ANCOVA, p = .01)](../claims/cognitive-load-negatively-predicts-problem-solving.md) [+W]
- [CLT-based instructional design is applied to very high element interactivity material (per Pollock, Chandler, & Sweller)](../claims/clt-design-very-high-element-interactivity.md) [+W]
- [Understanding depends on the degree of interaction among elements of information](../claims/understanding-depends-on-element-interaction.md) [+W] — attached 2026-10-24 from Marcus (1998), which proposed "Element interactivity account of understanding instructions within cognitive load theory"; tests this page's relationship.
- [Incorporating interacting elements into a diagrammatic schema reduces cognitive load and enhances understanding](../claims/diagrammatic-schema-reduces-load-enhances-understanding.md) [+W] — attached 2026-10-24 from Marcus (1998), which proposed "Element interactivity account of understanding instructions within cognitive load theory"; tests this page's relationship.
- [Visual working memory capacity is significantly lower for complex items than for simple items](../claims/wm-capacity-decreases-with-item-complexity.md) [+W]
- [Children's spelling test performance declines as the cognitive load of the assessment method increases, with accuracy greatest in multiple-choice, then cloze dictation, then proofreading](../claims/assessment-method-cognitive-load-performance-decline.md) [+W] — attached 2026-10-26 from Howard et al. (2017), which proposed "Cognitive Load Theory extends from learning and instructional design to the design of educational assessment"; tests this page's relationship.
- [Cognitive load eliminated instruction-induced reversal of specific PIT in prior cited work, suggesting reversal instruction use is resource-dependent](../claims/cognitive-load-eliminates-reversal-pit-cited.md) [+W]
- [In the lab study, adding irrelevant information impaired performance only among low-working-memory participants in the distal condition](../claims/irrelevant-info-impairs-low-kmax-distal.md) [+W]
- [Design guidelines from motivational and complex-skill theories (4C/ID, ARCS, CLT) contradict multimedia learning guidelines (CTML), producing seven specific design dilemmas](../claims/seven-design-dilemmas-multimedia-vs-complex-skill-guidelines.md) [~W]
- [Serial mediation: map-structure salience affects disorientation, which affects extraneous load and learning performance; the chain is only partially confirmed](../claims/salience-disorientation-ecl-serial-mediation.md) [+W] — attached 2026-10-29 from Felix Krieglstein et al. (2022), which proposed "Disorientation as a meaningful supplement to current extraneous cognitive load measurement".
- [A situated embodiment-based flag semaphore strategy improved procedural knowledge and attention with lower extrinsic cognitive load](../claims/situated-embodiment-semaphore-procedural-knowledge.md) [+W]
- [No split-attention difference in comprehension or learning efficiency between text+picture on a mobile device and text on a mobile device plus real objects](../claims/no-split-attention-effect-mobile-text-picture-versus-text-real-objects.md) [~M] — attached 2026-10-29 from Liu et al. (2011), which proposed "Cognitive load theory applied to mobile learning: split-attention and redundancy effects from combining texts, pictures, and real objects"; tests this page's relationship.
- [Redundancy effect on comprehension: TP and TO conditions outperformed the TPO condition in a mobile learning experiment](../claims/redundancy-effect-comprehension-mobile-learning.md) [+M] — attached 2026-10-29 from Liu et al. (2011), which proposed "Cognitive load theory applied to mobile learning: split-attention and redundancy effects from combining texts, pictures, and real objects"; tests this page's relationship.

## The evidence by question

- *Should related text and pictures be integrated rather than separated?* [Cognitive Load Reduction Improves Learning](../claims/cognitive-load-reduction-improves-learning.md) [+S]
- *Do novices learn more from studying worked examples than from solving the same problems unaided?* [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S]
- *For whom: does support that helps novices stop helping as task-specific expertise grows?* [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~S]
- *Does breaking transient material (animation, video, narration) into segments improve learning over a continuous presentation?* [Segmenting Improves Multimedia Learning](../claims/segmenting-improves-multimedia-learning.md) [+M]

## Related Theories

- [Situated Learning](situated-learning.md) — CLT treats working memory as an individual cognitive limit; situated learning argues that cognition is distributed across tools, people, and environment, which can extend effective working memory capacity
- [Self-Regulated Learning](self-regulated-learning.md) — SRL requires learners to monitor and regulate their own processing; CLT explains why novices often cannot self-regulate effectively — metacognitive monitoring itself consumes working memory
- [Dual Coding Theory](dual-coding-theory.md) — Paivio's dual coding theory (separate verbal and visual channels) is a compatible model; multimedia learning theory (Mayer) applies both CLT and dual coding to instructional media design
- [Constructivism](constructivism.md) — tension point: constructivist approaches favor active discovery, which can impose high extraneous load; CLT favors explicit instruction for novices, but converges with constructivism for more expert learners (see expertise reversal)
- [Cognitive Load Theory: working-memory limits, human cognitive architecture, and three load types](clt-three-load-types-framework.md)
- [Skehan's limited attention capacity prediction as an account of task complexity effects on child L2 development](skehan-limited-attention-capacity-child-task-recasts.md)
- [Element interactivity as the CLT criterion of subject complexity](element-interactivity-complexity-criterion-clt.md)
- [Expertise reversal effect applied to multi-principle visual revisions](expertise-reversal-multimedia-revisions.md)

## Examples

**[Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md)** — implements CLT by sequencing the modeling → coaching → fading arc: the modeling phase offloads element-interactivity processing onto the expert's narrated demonstration, reducing load during initial acquisition and fading support as schemas form.

**[Demonstration](../elements/demonstration.md)** — the worked example is CLT's most direct instructional expression; by presenting a fully solved problem, demonstration eliminates the search component of problem solving, which is the primary source of extraneous load for novices.

**[Use Worked Examples](../strategies/worked-examples-first.md)** — concrete application of CLT's worked example effect; the study-then-solve cycle is a direct implementation of the example-problem sequence shown to reduce load and improve transfer.

**[User-Centered Design for Learning](../principles/user-centered-design-for-learning.md)** — applies CLT's extraneous-load concept to interface design: confusing navigation and inconsistent terminology impose extraneous load exactly as an unnecessarily split-attention diagram does.
- [Manage the three load types: reduce extraneous load, optimize intrinsic load, and increase germane load](../principles/cognitive-load-management.md)
- [Select interaction types based on content type rather than random variation to preserve format-meaning coherence](../strategies/content-type-based-interaction-selection.md)
- [Balance cognitive load in digital learning by aligning design-factor costs and benefits with desired learning outcomes via constructive alignment](../strategies/align-cognitive-load-with-learning-outcomes-digital.md)

## Key Sources
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. [doi:10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)
- Chandler, P., & Sweller, J. (1991). Cognitive load theory and the format of instruction. *Cognition & Instruction, 8*(4), 293-332.
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. G. W. C. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296. [doi:10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Paas, F., Renkl, A., & Sweller, J. (2003). Cognitive load theory and instructional design: Recent developments. *Educational Psychologist, 38*(1), 1–4. [doi:10.1207/S15326985EP3801_1](https://doi.org/10.1207/S15326985EP3801_1)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge. [doi:10.4324/9781315113210](https://doi.org/10.4324/9781315113210)

<!-- merged 2026-10-02 from patterns/cognitive-load-theory ("Cognitive Load Theory"), misfiled as a pattern and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Cognitive Load Theory

> **Pattern** · [All patterns](index.md)
> **Evidence** · 7 claims (6 for, 1 mixed) · 11 studies (5 quant-synthesis, 3 review, 2 causal, 1 design), `q2`–`q4` · 3 of 11 report an effect size · 3 claims rest on one study

## Description
Cognitive Load Theory is the short-form canonical target for CLT-informed instructional patterns that reduce extraneous load and calibrate support to expertise.

## Implications

### Context
#### Requirements
- **Attention to working-memory limits**
- **Instructional supports that reduce unnecessary processing**
#### Constraints
- **Novice-oriented supports may hinder experts**
#### Grain Size
- Lesson

### Target Goals
- Improve comprehension and early schema acquisition.

### Target Learners
- Especially useful for novices in complex domains.

### Theory
#### Supporting

- [Cognitive Load Theory](../principles/cognitive-load-theory.md)
- [Redundancy Effect Impairs Learning](../claims/redundancy-principle.md) [+W]
- [Cognitive Load Reduction Improves Learning](../claims/cognitive-load-reduction-improves-learning.md) [+M]
- [Cognitive Load Management](../claims/cognitive-load-management.md) [+M]
- [Split Attention Effect Degrades Learning](../claims/split-attention-effect-degrades-learning.md) [+M]
- [Redundancy Hurts Learning](../claims/redundancy-hurts-learning.md) [+M]
- [Segmenting Improves Multimedia Learning](../claims/segmenting-improves-multimedia-learning.md) [+M]

## Claims
- [Minimal guidance is less effective for novices than explicit instruction](../claims/minimal-guidance-less-effective-for-novices.md) [~M]

## Related Patterns
- [Cognitive Load Reduction (CLT Scaffolding Approach)](../principles/cognitive-load-theory.md)

## Key Sources
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296. [https://doi.org/10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
-->
