---
type: principle
id: cognitive-load-theory
aliases: [lower-extraneous-load-to-increase-germane-effort-in-stem]
title: Cognitive Load Theory
description: "For a task-specific novice on high-element-interactivity material, reducing avoidable processing is expected to improve performance or efficiency, a relationship that weakens or reverses as task-specific expertise grows."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: sweller-1998
    resource: "https://doi.org/10.1023/A:1022193728205"
    title: "Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296"
    author: "Sweller, J., van Merriënboer, J. J. G., & Paas, F"
  - id: gupta-2020
    resource: "https://doi.org/10.20897/ejsteme/9252"
    title: "Gupta, U., & Zheng, R. Z. (2020). Cognitive Load in Solving Mathematics Problems: Validating the Role of Motivation and the Interaction Among Prior Knowledge, Worked Examples, and Task Difficulty. European Journal of STEM Education, 5(1), 05. https://doi.org/10.20897/ejsteme/9252"
    author: "Gupta, U., & Zheng, R. Z"
  - id: sweller-2011
    resource: "https://doi.org/10.1016/B978-0-12-387691-1.00002-8"
    title: "Sweller, J. (2011). Cognitive load theory. *Psychology of Learning and Motivation, 55*, 37-76"
    author: Sweller, J
  - id: van-gog-2011
    resource: "https://doi.org/10.1016/j.cedpsych.2010.10.004"
    title: "van Gog, T., Kester, L., & Paas, F. (2011). Effects of worked examples, example-problem, and problem-example pairs on novices' learning. *Contemporary Educational Psychology, 36*(3), 212-218"
    author: "van Gog, T., Kester, L., & Paas, F"
---

# Cognitive Load Theory

> **Principle** · [All principles](index.md)
> **Evidence** · 37 claims (17 for, 20 mixed) · 42 studies (19 causal, 10 review, 6 quant-synthesis, 6 theoretical, 1 qualitative), `q1`–`q4` · 5 of 42 report an effect size · 27 claims rest on one study

## Conditional relationship

For a learner who is a **novice on the particular task** (not in the wider domain) and who meets material **high in element interactivity** (elements that must be processed together), presentations and sequences that remove avoidable processing (integrated rather than split sources, segmented transient media, isolated interacting elements before the whole, full rather than completion examples) are expected to improve immediate performance, near transfer or instructional efficiency, compared with the unreduced version of the same material. The relationship weakens, disappears or may reverse as the learner's **task-specific** expertise grows, and it is expected to matter little for low-element-interactivity material. Which outcome changes (performance, effort, efficiency) and at what horizon (immediate, delayed) differs between the studies below and must be stated for each design. Working-memory overload and schema construction are the explanatory hypotheses of [Cognitive Load Theory](../theories/cognitive-load-theory.md) and the [expertise reversal effect](../theories/expertise-reversal-effect.md); they are not observations. The [4C/ID pattern](../patterns/4cid-four-component-instructional-design.md) is a reusable whole-task policy that applies this relationship; its response-dependent branches remain proposals.

## Fitting the design to a situation

Ask for three facts when the brief omits them: **how much do these learners already know about this particular task?**, **how many elements must they handle together (simple or complex material)?**, and **how is it presented: text and diagrams, narration, video, and who sets the pace?**

| If the brief says… | Then change… | Basis |
|---|---|---|
| Text and diagrams refer to each other (labelled figures, worked solutions with a diagram) | Place each label or explanation on or next to the part it describes; present narration at the same time as the animation it explains | [Reducing split attention improves learning](../claims/cognitive-load-reduction-improves-learning.md) [+S]; [Integrating text and diagrams beats separating them](../claims/split-attention-effect-degrades-learning.md) [+M] |
| The material is complex, with many interacting elements | Apply the load-reducing design principles first here; their effect was largest for complex material | [Reducing extraneous load improved learning, more for complex material](../claims/cognitive-overload-degrades-learning.md) [+M]; [Integration helps more for high element interactivity](../claims/element-interactivity-moderates-contiguity-effect.md) [+M] |
| The material is simple, or learners control the pace (a website, a document) | Expect a smaller gain from redesign; reported effects were smaller for simple and for learner-paced media | [Design principle effects moderated by pacing and complexity](../claims/design-principle-effects-moderated-by-pacing-and-complexity.md) [~M] |
| Narration plus the same words on screen, alongside pictures or animation | Drop the verbatim on-screen text; with images or animation, adding it gave no benefit | [With images or animation, verbal redundancy does not help](../claims/images-animation-eliminate-redundancy-benefit.md) [~M] |
| Learners are second-language or less fluent readers, and the material is text without pictures | Keep spoken and written text together (narration with captions); the benefit was larger for these readers | [Spoken–written advantages are larger for L2 and nonfluent readers](../claims/reader-fluency-prior-knowledge-moderate-redundancy.md) [+M] |
| The instruction is in a language the learners are still learning | Give explanations in the learners' first language or bilingually where possible | [Foreign-language AI explanations impose a double burden](../claims/double-burden-language-of-ai-instruction.md) [~W] |
| Learners are experienced on this task | Remove explanatory text from diagrams and other guidance that repeats what they know; check with an unsupported task | [Guidance that helps novices can become redundant as expertise grows](../claims/expertise-reversal-effect.md) [~M]; [Split-attention benefit reverses into redundancy for experienced learners](../claims/expertise-reversal-split-attention-redundancy-review.md) [~M] |
| Learners are novices on a multi-step procedure | Open with a full worked example, not a problem: examples only or example–problem pairs, then problems; use full worked examples rather than completion problems at first | [Example-first sequences beat problem-first ones for novices on an immediate test, with lower rated effort](../claims/worked-example-problem-sequences.md) [+M]; [Lower-prior-knowledge learners did better with full than completion examples](../claims/lower-prior-knowledge-learners-score-higher-with-full-than-completion-worked-examples.md) [+M] |
| Support can be adjusted to each learner's last response (one-to-one tutoring, a small group, an adaptive system) | Raise support after a failed step and lower it after a success, instead of fixing one level for everyone; fade full examples as independent success holds | [Contingent support beat fixed or absent support, mostly in one-to-one tutoring](../claims/contingent-scaffolding-improves-learning.md) [+M]; [Worked-example guidance becomes less effective as expertise grows](../claims/worked-examples-less-effective-with-expertise.md) [~M] |
| A complex whole task that novices cannot yet coordinate | Teach the interacting parts separately first, then the whole task | [Isolated parts first helped novices on complex tasks](../claims/part-task-practice-reduces-load-for-novices.md) [+M] |
| Learners have an AI assistant or tutor | Let it remove access barriers (finding, formatting, translating material) but keep the interacting elements the task is meant to teach for the learner to process; check unaided performance | Conceptual arguments only, untested in the wiki: [AI lowers access complexity, not the task's cognitive demand](../claims/ai-raises-problem-complexity-ceiling.md) [~W]; [Outsourcing productive struggle to AI risks cognitive debt](../claims/cognitive-debt-reactive-ai-approaches-insufficient.md) [~W]; [AI as scaffolding that lowers the threshold for understanding](../claims/ai-intelligent-scaffolding-lowers-knowledge-threshold.md) [~W]; [Intrinsic and extraneous load differ by whether interactivity is essential to the task](../claims/intrinsic-extraneous-distinction-essential-vs-instructional.md) [~W] |
| Success will be judged by learners' effort or load ratings | Measure performance and transfer as well; load ratings moved little even where design changes improved learning, and moved without any change in learning in a combinatorics simulation | [Design interventions yield small improvements in load measures](../claims/design-principles-improve-cognitive-load-management.md) [~M]; [Tree diagrams raised rated load](../claims/tree-diagrams-increase-cognitive-load.md) [~M], yet [format made no difference to conceptual or situational knowledge](../claims/no-format-effect-conceptual-situational-knowledge.md) [~M] and [adding equations lowered load without better outcomes](../claims/adding-equations-to-diagrams-reduced-load-not-outcomes.md) [~M] |

## Observation, state and explanation

Record a response **under stated conditions**: the task, its representation, its element interactivity as judged for this learner, the support present (integrated text, segments, examples, hints), time and the response mode. "Overloaded" and "novice" are inferred states, not observations. Accuracy, time, a rated mental effort and confidence are observations; none directly measures working-memory load or a schema, and a low effort rating can also mean disengagement. Expertise is task-specific: a learner fluent on one task class may be a novice on the next, so a rating from an earlier topic does not settle it. Load ratings also travel with motivation: in one algebra study, self-reported extraneous load correlated negatively with germane load (r = −.26) and with expected probability of success (r = −.19), and germane load correlated positively with interest (r = .26), all self-report and correlational ([extraneous load correlates negatively with germane load and expected success](../claims/extraneous-cognitive-load-correlates-negatively-with-germane-load-and-probability-of-success.md) [~M]; [germane load correlates with interest](../claims/germane-cognitive-load-correlates-positively-with-interest.md) [~M]). Read a load rating alongside interest and expected success, not as a pure measure of the material.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Fails a complex task but succeeds on each component in isolation | Interacting elements exceed what the learner can coordinate; a missing integrating relation; a presentation that splits mutually referring sources | Present the same whole task with the sources integrated, then with one interacting element pre-taught; record which change restores performance and every support given. |
| High rated effort and slow progress with full support | Material genuinely high in element interactivity for this learner; redundant support the learner must reconcile with what they already know; unfamiliar representation or language | Offer the same task with the redundant support removed (e.g. diagram without duplicating text) and compare accuracy and effort; probe the representation separately. |
| Learns well from full examples early, then slows or stops improving with them | Rising task-specific expertise making the guidance redundant; fatigue or loss of interest; a plateau on the target relation | Give a completion problem or an unsupported changed problem; if independent success holds, reduce support provisionally. If it fails, the guidance may still be needed. |
| Lower effort with segmented or reduced material but no change in score | Reduced extraneous processing without a learning gain; easier-looking material lowering investment; outcome measure insensitive to the change | Hold the outcome measure fixed and add a delayed or near-transfer probe; report effort and performance separately rather than as one efficiency figure. |

These rows are proposals, untested with learners. The probes can shift confidence among explanations; a single contrast does not identify a cause, and each probe is itself a learning exposure that can change the state.

## Evidence and qualifications

- [Reducing extraneous load in multimedia design improved learning, more for complex material](../claims/cognitive-overload-degrades-learning.md) [+M]: an overview of 29 systematic reviews (1,189 studies, 78,177 participants) reports load-reducing design principles improving learning (g = 0.38), with g = 0.70 for complex, high-element-interactivity materials against g = 0.20 for simple ones. Learner prior knowledge did **not** significantly moderate effects, so it gives weak support to the expertise half of this model. The outcome is pooled learning (general-achievement), horizon not separated; it tests reducing load, not inducing overload. Not settled: the abstract available could not confirm its entries.
- [Integrating mutually referring text and diagrams beats separating them](../claims/split-attention-effect-degrades-learning.md) [+M]: a random-effects meta-analysis of 58 comparisons (n=2426) reports g = 0.63 for spatially integrated over separated presentation, holding broadly across moderators per the abstract. Learners' expertise and the horizon are not reported on the claim page. Not yet checked against its sources; it does not predict a benefit when each source is intelligible alone.
- [Isolating interacting elements first helped novices on complex tasks](../claims/part-task-practice-reduces-load-for-novices.md) [+M]: one experiment reports that, for high-element-interactivity tasks, novices performed better when first given isolated parts before the integrated whole. Sample size, outcome measure and horizon are not reported on the page; not yet checked against its sources.
- [Guidance that helps novices can lose its advantage or reverse for experienced learners](../claims/expertise-reversal-effect.md) [~M]: three experiments with electrical trainees reading circuit diagrams found integrated text best for less experienced trainees and diagram-only best for the most experienced; a narrative review reports the same pattern across five load paradigms. Abstract only, no effect sizes or horizon recorded; not settled against its sources. It does not say at what level of expertise support should change.
- [Segmentation's efficiency advantage disappeared at higher prior knowledge](../claims/segmentation-benefits-shrink-with-expertise.md) [~M]: 75 secondary students, randomized to segmented or continuous animated probability examples. Segmented examples were more efficient (performance relative to mental effort) on near and far transfer at lower prior knowledge; the difference disappeared, not reversed, at higher prior knowledge, and there was no interaction on raw transfer performance. Not yet checked against its sources.
- [Lower-prior-knowledge learners did better with full than completion examples](../claims/lower-prior-knowledge-learners-score-higher-with-full-than-completion-worked-examples.md) [~M]: a factorial experiment with college students on simultaneous equations; lower-prior-knowledge learners scored higher after full-worked examples (t(1,26) = 1.98, p = .05), while higher-prior-knowledge learners' advantage for completion examples was not significant (p = .22) and equivalence was not tested. Judge-checked against the full text; immediate posttest, no effect size printed.
- [Example-first sequences outperformed problem-first ones for novices](../claims/worked-example-problem-sequences.md) [+M]: 96 Dutch secondary novices in circuit troubleshooting, randomized to examples only, example–problem pairs, problem–example pairs or problems only. The two example-first conditions scored higher on an immediate test (partial η² = .23) with lower rated training effort (partial η² = .20); problem–example pairs did not beat problems only, so starting with the example mattered. One study, immediate test only, narrow instruction-aligned items; equivalence between the two example-first conditions was not tested.
- [Contingent scaffolding improved learning more than fixed or absent support](../claims/contingent-scaffolding-improves-learning.md) [+M]: fourth and fifth graders tutored one-to-one on long division (8 per condition) solved more problems at immediate and one-month tests under fully contingent support than under fixed high, moderate or no support; a meta-analysis of dynamic assessment ranks scaffolding above coaching but below explicit strategy training. Most of the evidence is one-to-one tutoring, so it bears on the response-dependent fading in this model, not on whole-class pacing.
- [The expertise reversal is more often partial than full](../claims/expertise-reversal-effect-definition.md) [~M]: Kalyuga and Renkl's introduction to a special issue reports the reversal as replicated across many materials, usually as a partial reversal (a significant interaction, the novice advantage shrinking) rather than a full crossover. With the segmentation result above, it supports expecting support to stop helping before it starts to hurt; it gives no threshold.
- [Worked-example guidance becomes less effective as expertise grows](../claims/worked-examples-less-effective-with-expertise.md) [~M]: two syntheses (Kalyuga et al. 2003; Renkl & Atkinson 2003) argue that full examples should give way to problem solving as competence develops; neither prints an effect size, and the claim's own entries are abstract-level.
- [Chunking reduces working-memory load](../claims/chunking-reduces-working-memory-load.md) [+M]: list-recall experiments show that recoding items into units the learner already knows frees memory for other items held at the same time, and reviews place the limit for novel material near four chunks. No study on that page measures learning or problem solving after material was chunked for learners, so it supports the working-memory premise, not a design effect.

Keep learners, task, comparator, outcome and horizon with each result when transporting it. Efficiency, effort and performance are different outcomes; a non-significant difference is not equivalence; and the pooled values do not forecast an individual learner's response or rank these load-reducing techniques against each other.

## The evidence by question

Each question below links a general claim that gathers the studies behind it into one table, one row per distinct study, with each study's design and effect as recorded and no averaged verdict (`eval/synthesis/cognitive-load.json`, `scripts/synthesize_claim.py`). The count is of distinct studies across the claim and the narrower claims that bear on it.

- Does removing avoidable processing from a presentation improve learning? [Cognitive Overload Degrades Learning](../claims/cognitive-overload-degrades-learning.md) [+S]: 8 distinct studies.
- For which material and pacing does managing load matter most? [Design principle effects are larger in system-paced and in complex media, and learner prior knowledge was not a significant moderator (p = 0.14)](../claims/design-principle-effects-moderated-by-pacing-and-complexity.md) [~M]: 3 distinct studies.
- Should related text and pictures be integrated rather than separated? [Cognitive Load Reduction Improves Learning](../claims/cognitive-load-reduction-improves-learning.md) [~S]: 5 distinct studies.
- Should the same words be given both spoken and written, or other duplicate material be added? [On-screen text that duplicates the narration of a diagram can hurt learning, but spoken–written redundancy is not harmful on average and helps over spoken-only presentation in some conditions](../claims/redundancy-hurts-learning.md) [~S]: 7 distinct studies.
- For whom: does support that helps novices stop helping as task-specific expertise grows? [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~S]: 13 distinct studies.
- Should component knowledge come before the whole task? [Pretraining learners on a system's key parts and terms before the main lesson improved knowledge and real-world transfer in one VR experiment, and is reported second-hand to improve learning in multimedia studies](../claims/pretraining-improves-transfer.md) [~S]: 3 distinct studies.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Re-read 2026-10-19: thirteen of the sixteen claims listed here were moved into the model above (the situation table, the observation section and the evidence list). The three below were read and do not change the model.

- [Students reported similar perceived information quantity across conditions, indicating diverse explanations did not produce perceived information overload](../claims/diverse-explanations-no-perceived-information-overload.md) [~W] — read: one introductory-programming study of LLM explanations; it measures perceived amount of information on a five-point scale, not load or learning, so it does not test this relationship.
- [Two-thirds of students reported limitations of data comics: information overload, limited generalisability, design-dependence, and oversimplification](../claims/data-comics-perceived-limitations-overload-design-dependence.md) [~W] — read: students' open-ended comments (18 of the sample named busy layouts as overloading); a perception consistent with removing clutter, with no comparison of designs or learning outcome.
- [Working memory is limited in capacity and includes partially independent subcomponents for auditory/verbal and visual/2- or 3-dimensional information](../claims/working-memory-partially-independent-modality-subcomponents.md) [+W] — read: the theory's architectural premise as stated by Sweller et al. (1998), with no test; it is part of the explanatory hypothesis named in the conditional relationship, not an observation.

## Objective and learner-valued goal

Ask what the learner wants to accomplish and why, separately from the designer's objective. Agreement, divergence and uncertainty are observations; do not infer motivation from compliance or from a low effort rating. The designer chooses the representative task, the permitted aids, the criterion and the horizon; load reduction is a means to that objective, not the objective.

For example, an apprentice electrician may value reading a real wiring diagram on site without a reference card, while the designer's objective is passing a timed schematic-interpretation test. Integrated labels may raise the test score early yet leave the learner's valued performance (reading an unlabelled diagram) untested. Record both aims, and plan when the integrated support is removed and how unaided reading is checked.

## What would revise this model?

The load-reduction expectation should weaken if comparable novices on high-element-interactivity tasks fail to benefit under defensible comparisons with aligned outcomes, or if benefits appear equally for low-element-interactivity material. The expertise qualification should weaken if, as in the multimedia overview above, prior knowledge repeatedly fails to moderate effects when it is measured. If effort falls without any gain in performance or transfer, the model's claim about learning (as opposed to comfort) is not supported for that design. Do not protect the model by relabelling every failure as "too much load" or "too much expertise" after the fact.

A learning-phase efficiency gain, immediate performance, near transfer, delayed retention and unaided use in the learner's setting are separate claims. The present evidence does not establish a threshold of expertise at which to remove support, a universal ordering of techniques, or that reduced load causes the gains it accompanies.

## Claims

- [How commonly the increased efficiency effect is present in test data is unclear](../claims/increased-efficiency-prevalence-unclear.md) [~W]
- [Avoiding double load on the visual channel improves visual knowledge (channel-overload effect)](../claims/voice-media-outperform-picture-text-overall.md) [+W]
- [Supplementary process estimates linked differentiated support to lower cognitive load for low-proficiency and higher discourse awareness for intermediate learners, but were descriptive only](../claims/descriptive-process-estimates-support-layers.md) [~W]
- [In one middle-school quasi-experiment, adding written text to spoken narration makes no significant difference to achievement with either abstract or concrete animation](../claims/redundancy-effect-not-significant-middle-school.md) [~W]
- [GenAI training leaves total cognitive load comparable while marginally raising intrinsic cognitive load](../claims/genai-training-comparable-load-marginal-intrinsic-increase.md) [~W]
- [Redundant text in the diagram did not affect posttest accuracy or difficulty ratings](../claims/redundant-text-no-effect-posterior-probability-lesson.md) [~W]

## Related Principles
- [Scaffolding](scaffolding.md)
- [Worked Examples](worked-examples.md)
- [Accessible Vocabulary & Syntax](accessible-vocabulary-syntax.md)
- [Cognitive Load Reduction](cognitive-load-management.md)

## Examples

- A novice algebra lesson uses a single integrated visual instead of separate text and diagram panels that learners must constantly coordinate.
- A software onboarding flow replaces open-ended exploration with worked examples and progressively harder tasks until users can perform the workflow independently.
- Example-problem sequences in math or programming.
- Stepwise visual explanations paired with constrained early practice in technical training.
- Instructional materials redesigned to remove split-attention and unnecessary visual clutter.
- [Manage intrinsic load with a part-whole approach, task variability, and self-explanation to raise germane load](../strategies/part-whole-variability-self-explanation-raise-germane-load.md)

## Key Sources
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296. [https://doi.org/10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Gupta, U., & Zheng, R. Z. (2020). Cognitive Load in Solving Mathematics Problems: Validating the Role of Motivation and the Interaction Among Prior Knowledge, Worked Examples, and Task Difficulty. European Journal of STEM Education, 5(1), 05. https://doi.org/10.20897/ejsteme/9252
- Sweller, J., van Merrienboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296. [https://doi.org/10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Sweller, J. (2011). Cognitive load theory. *Psychology of Learning and Motivation, 55*, 37-76. [https://doi.org/10.1016/B978-0-12-387691-1.00002-8](https://doi.org/10.1016/B978-0-12-387691-1.00002-8)
- van Gog, T., Kester, L., & Paas, F. (2011). Effects of worked examples, example-problem, and problem-example pairs on novices' learning. *Contemporary Educational Psychology, 36*(3), 212-218. [https://doi.org/10.1016/j.cedpsych.2010.10.004](https://doi.org/10.1016/j.cedpsych.2010.10.004)

<!-- deprecated 2026-10-01: superseded by the conditional model above; the principle body as it stood before the rewrite, kept verbatim.

## Description
Cognitive Load Theory, as a design principle, emphasizes managing the demands placed on working memory so learners can devote more capacity to schema construction rather than avoidable confusion. In practice this means simplifying presentation, sequencing support, and reducing unnecessary processing costs.
## Implications
Cognitive Load Theory implies that performance problems are often design problems, not just learner problems. When instructional materials split attention, add unnecessary complexity, or demand too much search too early, working memory is consumed by coordination rather than learning. Reducing that avoidable load usually helps novices form schemas faster [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S], but the same supports can become redundant for more advanced learners, so the practical goal is calibrated load, not permanent simplification [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M].

### Context
#### Requirements
- **Instructional choices that reduce extraneous load**
- **Sequencing or support aligned to learner expertise**
- **Attention to how information is presented, not just what is presented**
#### Constraints
- **Over-simplification can underprepare learners for real complexity**
- **Supports that help novices may burden experts**

### Target Learners
- Especially important for novices and for content with high intrinsic complexity.

### Target Learning Objectives
- Improve comprehension and early schema formation by reducing avoidable overload.

### Theory
#### Supporting
- [Cognitive Load Theory](../theories/cognitive-load-theory.md)
#### Contradicting / Qualifying
- Load management should support meaningful learning, not strip away all challenge.

### Claims

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S] — design choices that organize information and reduce unnecessary search help preserve working-memory capacity
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M] — guidance calibrated for novices can lose value or become burdensome as expertise increases
-->

<!-- merged 2026-10-07 from principles/lower-extraneous-load-to-increase-germane-effort-in-stem ("Lower extraneous load in STEM materials to leave room for germane effort"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Lower extraneous load in STEM materials to leave room for germane effort

> **Principle** · [All principles](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
Drawing on the negative extraneous-germane correlation, the authors state that "in order to increase learners’ efforts to learn (germane cognitive load), the educators must improve the design of instructional materials to lower the extraneous cognitive load", for example by removing redundancy or split-attention content. They also suggest interest may be used as a proxy for germane load.

## Design Implications

### Context
#### Requirements
- Identify and remove redundant or split-attention content from instructional materials.
#### Constraints
- The supporting evidence is correlational self-report data; the study did not manipulate extraneous load.

### Target Learners
- Non-science major college students at a Research I university in the western United States

### Target Learning Objectives
- Solving simultaneous equation (systems of equations) algebra problems

### Claims
- [Extraneous Cognitive Load Correlates Negatively With Germane Load And Probability Of Success](../claims/extraneous-cognitive-load-correlates-negatively-with-germane-load-and-probability-of-success.md) [+M]
- [Germane Cognitive Load Correlates Positively With Interest](../claims/germane-cognitive-load-correlates-positively-with-interest.md) [+M]

## Related Principles
- [Cognitive Load Reduction](cognitive-load-management.md)
- [Cognitive Load Management](cognitive-load-management.md)
- [Cognitive Load Theory](cognitive-load-theory.md)

## Examples
-

## Key Sources
- Gupta, U., & Zheng, R. Z. (2020). Cognitive Load in Solving Mathematics Problems: Validating the Role of Motivation and the Interaction Among Prior Knowledge, Worked Examples, and Task Difficulty. European Journal of STEM Education, 5(1), 05. https://doi.org/10.20897/ejsteme/9252
-->

<!-- merged 2026-10-15 from patterns/cognitive-load-reduction-clt-scaffolding-approach ("Cognitive Load Reduction (CLT Scaffolding Approach)"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Cognitive Load Reduction (CLT Scaffolding Approach)

> **Pattern** · [All patterns](index.md)
> **Evidence** · 10 claims (5 for, 5 mixed) · 15 studies (7 causal, 3 theoretical, 2 quant-synthesis, 2 review, 1 qualitative), `q1`–`q4` · 0 of 15 report an effect size · 8 claims rest on one study

## Description
This pattern designs instruction to reduce unnecessary load while preserving the mental work that actually contributes to learning. In practice, it often combines clear sequencing, worked examples, careful multimedia use, segmentation, and guided practice that fades over time. The aim is not to make learning effortless; it is to prevent avoidable overload so learners can focus on understanding and performance.

The pattern is especially useful when material is conceptually dense or when novices face many interacting elements at once. It becomes weaker when used as an excuse for oversimplification or passive spoon-feeding.

## Implications

### Context
#### Requirements
- **High element interactivity or novice difficulty**: Best when learners are likely to overload working memory without support.
- **Careful information design**: Explanations, examples, visuals, and practice need to be sequenced intentionally.
- **Planned fading**: Support should decrease as learner competence grows.
- **Alignment between explanation and practice**: Learners should move from supported examples into increasingly independent performance.
#### Constraints
- **Over-scaffolding risk**: Too much support can suppress active processing or become redundant for more advanced learners.
- **Expertise differences matter**: Supports that help novices can hinder experienced learners.
- **Poor multimedia design can backfire**: More channels do not help if they split attention or add irrelevant detail.
- **Not a complete learning model**: Load reduction needs to be paired with meaningful practice and feedback.
#### Grain Size
- Lesson
- Unit

### Target Goals
- **Initial understanding of complex material**: Helping learners build workable mental models.
- **Efficient novice performance**: Reducing unnecessary search and confusion during early learning.
- **Transition to independence**: Moving from examples and scaffolds toward self-directed problem solving.

### Target Learners
- **Novices in complex domains**: Strong fit when learners lack prior schemas.
- **Learners in technical or concept-heavy instruction**: Useful in STEM, technical training, and structured professional instruction.
- **Learners vulnerable to overload**: Particularly relevant when dense content and weak prior knowledge combine.

### Theory
#### Supporting

- Cognitive load theory — instruction should manage intrinsic load and minimize extraneous load.
- Worked-example traditions — examples can reduce unproductive search for novices.
- Scaffolding and fading perspectives — support should adapt to current competence and then withdraw.
- [Avoiding double load on the visual channel improves visual knowledge (channel-overload effect)](../claims/voice-media-outperform-picture-text-overall.md) [+W]

#### Contradicting / Qualifying
- Load reduction is not the only goal; learners still need productive struggle and meaningful performance.
- Expertise reversal limits the usefulness of novice-oriented supports.

### Claims
#### Supporting
- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-example-problem-sequences.md) [+M]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [+M]
#### Contradicting

- [Worked examples can become redundant or counterproductive for advanced learners.](../claims/worked-examples-less-effective-with-expertise.md) [+M]
- [AI's key contribution in STEM education is intelligent scaffolding that lowers the threshold for understanding knowledge, driving a shift from knowledge transmission to capability development](../claims/ai-intelligent-scaffolding-lowers-knowledge-threshold.md) [~W]
- [Outsourcing productive struggle to AI risks cognitive debt, and reactive compliance-focused approaches are insufficient](../claims/cognitive-debt-reactive-ai-approaches-insufficient.md) [~W]
- [AI raises the ceiling on problem complexity by reducing access complexity rather than cognitive demand](../claims/ai-raises-problem-complexity-ceiling.md) [~W]
- [Students reported similar perceived information quantity across conditions, indicating diverse explanations did not produce perceived information overload](../claims/diverse-explanations-no-perceived-information-overload.md) [~W]
- [Two-thirds of students reported limitations of data comics: information overload, limited generalisability, design-dependence, and oversimplification](../claims/data-comics-perceived-limitations-overload-design-dependence.md) [~W]

## Design

### Sequence
1. Present information in a simplified, well-integrated form.
2. Use worked examples or heavily guided tasks to reduce search demands.
3. Transition into example-problem or guided-practice sequences.
4. Fade supports as learners demonstrate stronger schema formation.
5. Shift toward more independent and variable tasks.

### Elements Used
- [Part-task Practice](../elements/part-task-practice.md)
- [Practice](../elements/practice.md)
- [Problem Presentation](../elements/problem-presentation.md)
- [Assessment](../elements/assessment.md)

### Affordances
- [Worked Examples](../principles/worked-examples.md)
- [Guided Practice](../principles/guided-practice.md)
- [Creating Visual Representations](../principles/dual-coding.md)
- [Multimodal Instruction](../principles/multimodal-instruction.md)

### Personalization
- The amount of guidance can be adjusted by prior knowledge.
- Examples can be faded faster for learners who no longer need them.
- Tasks can be chunked differently depending on where overload is occurring.

## Related Patterns
- [Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md)
- [Problem-Based Learning (PBL)](../patterns/problem-based-learning.md)

## Examples
- Example-problem sequences in math or programming.
- Stepwise visual explanations paired with constrained early practice in technical training.
- Instructional materials redesigned to remove split-attention and unnecessary visual clutter.

## Impact
- Often improves early learning efficiency for novices.
- Requires ongoing adjustment so supports do not remain longer than needed.

## Key Sources
- Sweller, J., van Merrienboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296. [https://doi.org/10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Sweller, J. (2011). Cognitive load theory. *Psychology of Learning and Motivation, 55*, 37-76. [https://doi.org/10.1016/B978-0-12-387691-1.00002-8](https://doi.org/10.1016/B978-0-12-387691-1.00002-8)
- van Gog, T., Kester, L., & Paas, F. (2011). Effects of worked examples, example-problem, and problem-example pairs on novices' learning. *Contemporary Educational Psychology, 36*(3), 212-218. [https://doi.org/10.1016/j.cedpsych.2010.10.004](https://doi.org/10.1016/j.cedpsych.2010.10.004)
-->
