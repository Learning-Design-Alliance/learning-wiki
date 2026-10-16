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
---

# Cognitive Load Theory

> **Theory** · [All theories](index.md)
> **Evidence** · 35 claims (25 for, 8 mixed, 2 against) · 38 studies (16 causal, 9 quant-synthesis, 6 review, 6 theoretical, 1 design), `q1`–`q4` · 8 of 38 report an effect size · 27 claims rest on one study

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

- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-example-problem-sequences.md) [+S] — example-based sequences reduce load compared to problem-only practice for novices; provides direct experimental evidence for the worked example effect as a CLT application
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
- [Segmenting multimedia instruction into learner-paced segments improves retention and transfer performance with small-to-medium effects](../claims/segmenting-improves-multimedia-learning.md) [+W] — attached 2026-10-13 from Rey et al. (2019), which proposed "Explanatory accounts of the segmenting effect: designer-imposed chunking and structuring, more processing time, and individual pace adaptation".
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
- [Segmenting complex dynamic visualizations into pieces with pauses improves learning outcomes, especially transfer performance, compared with non-segmented presentations](../claims/segmentation-improves-learning-dynamic-visualizations.md) [+W] — attached 2026-10-15 from Spanjers et al. (2010), which proposed "Cognitive load / transience account: segmentation reduces extraneous load from information transience by dividing content into smaller units and providing processing pauses"; tests this page's relationship.
- [Segmentation of dynamic visualizations shows an expertise reversal effect: students with lower prior knowledge benefit, while students with higher prior knowledge learn equally well with or without segmentation](../claims/segmentation-benefits-shrink-with-expertise.md) [+W] — attached 2026-10-15 from Spanjers et al. (2010), which proposed "Cognitive load / transience account: segmentation reduces extraneous load from information transience by dividing content into smaller units and providing processing pauses"; tests this page's relationship.
- [The element interactivity effect relies on changes in element interactivity due to changes in the type of material being learned](../claims/element-interactivity-changes-from-material-type.md) [+W] — attached 2026-10-15 from Chen et al. (2017), which proposed "Unified cognitive load account: the expertise reversal effect as a variant of the element interactivity effect".
- [The expertise reversal effect relies on changes in relative levels of element interactivity due to changes in relative levels of expertise](../claims/expertise-reversal-changes-from-expertise-levels.md) [+W] — attached 2026-10-15 from Chen et al. (2017), which proposed "Unified cognitive load account: the expertise reversal effect as a variant of the element interactivity effect".
- [In its traditional treatment, germane cognitive load is essentially indistinguishable from intrinsic load and may be a redundant concept](../claims/germane-load-indistinguishable-from-intrinsic-load.md) [-W] — attached 2026-10-15 from Kalyuga (2011), which proposed "Redefined germane load as actual working memory resources devoted to dealing with intrinsic rather than extraneous load".
- [Emotions may act as extraneous cognitive load by competing for limited working memory resources with task-irrelevant processing](../claims/emotion-as-extraneous-cognitive-load.md) [+W] — attached 2026-10-15 from Plass et al. (2019), which proposed "Four-perspective taxonomy of emotion–cognitive load relationships understood through an interval view of cognitive load".
- [Emotion may affect intrinsic cognitive load, for example when emotion regulation is part of the learning outcomes](../claims/emotion-as-intrinsic-load-emotion-regulation.md) [+W] — attached 2026-10-15 from Plass et al. (2019), which proposed "Four-perspective taxonomy of emotion–cognitive load relationships understood through an interval view of cognitive load".
- [Reduction of cognitive load can sometimes impair learning rather than enhance it](../claims/load-reduction-can-impair-learning.md) [~W] — attached 2026-10-15 from Schnotz et al. (2007), which proposed "Zone of proximal development perspective on cognitive load theory".
- [Germane cognitive load fully mediates the effect of information-search tool on justification quality (exploratory analysis)](../claims/germane-load-mediates-tool-effect-on-justification-quality.md) [+W] — attached 2026-10-15 from Matthias Stadler et al. (2024), which proposed "Cognitive load–self-regulation tradeoff account of information-search tool effects on learning quality"; tests this page's relationship.

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

## Key Sources
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. [doi:10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)
- Chandler, P., & Sweller, J. (1991). Cognitive load theory and the format of instruction. *Cognition & Instruction, 8*(4), 293-332.
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. G. W. C. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296. [doi:10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Paas, F., Renkl, A., & Sweller, J. (2003). Cognitive load theory and instructional design: Recent developments. *Educational Psychologist, 38*(1), 1–4. [doi:10.1207/S15326985EP3801_1](https://doi.org/10.1207/S15326985EP3801_1)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge. [doi:10.4324/9781315113210](https://doi.org/10.4324/9781315113210)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296. [https://doi.org/10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)

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
