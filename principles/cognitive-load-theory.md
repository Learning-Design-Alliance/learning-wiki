---
type: principle
id: cognitive-load-theory
aliases: [lower-extraneous-load-to-increase-germane-effort-in-stem]
title: Cognitive Load Theory
description: "For a task-specific novice on high-element-interactivity material, reducing avoidable processing is expected to improve performance or efficiency, a relationship that weakens or reverses as task-specific expertise grows."
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
---

# Cognitive Load Theory

> **Principle** · [All principles](index.md)
> **Evidence** · 7 claims (4 for, 3 mixed) · 12 studies (6 causal, 3 review, 2 quant-synthesis, 1 theoretical), `q1`–`q4` · 2 of 12 report an effect size · 4 claims rest on one study

## Conditional relationship

For a learner who is a **novice on the particular task** (not in the wider domain) and who meets material **high in element interactivity** (elements that must be processed together), presentations and sequences that remove avoidable processing (integrated rather than split sources, segmented transient media, isolated interacting elements before the whole, full rather than completion examples) are expected to improve immediate performance, near transfer or instructional efficiency, compared with the unreduced version of the same material. The relationship weakens, disappears or may reverse as the learner's **task-specific** expertise grows, and it is expected to matter little for low-element-interactivity material. Which outcome changes (performance, effort, efficiency) and at what horizon (immediate, delayed) differs between the studies below and must be stated for each design. Working-memory overload and schema construction are the explanatory hypotheses of [Cognitive Load Theory](../theories/cognitive-load-theory.md) and the [expertise reversal effect](../theories/expertise-reversal-effect.md); they are not observations. The [4C/ID pattern](../patterns/4cid-four-component-instructional-design.md) is a reusable whole-task policy that applies this relationship; its response-dependent branches remain proposals.

## Observation, state and explanation

Record a response **under stated conditions**: the task, its representation, its element interactivity as judged for this learner, the support present (integrated text, segments, examples, hints), time and the response mode. "Overloaded" and "novice" are inferred states, not observations. Accuracy, time, a rated mental effort and confidence are observations; none directly measures working-memory load or a schema, and a low effort rating can also mean disengagement. Expertise is task-specific: a learner fluent on one task class may be a novice on the next, so a rating from an earlier topic does not settle it.

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

Keep learners, task, comparator, outcome and horizon with each result when transporting it. Efficiency, effort and performance are different outcomes; a non-significant difference is not equivalence; and the pooled values do not forecast an individual learner's response or rank these load-reducing techniques against each other.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S] — not settled: the text available could not confirm the entries (abstract)
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M] — not settled: the text available could not confirm the entries (abstract)
- [Extraneous Cognitive Load Correlates Negatively With Germane Load And Probability Of Success](../claims/extraneous-cognitive-load-correlates-negatively-with-germane-load-and-probability-of-success.md) [+M]
- [Germane Cognitive Load Correlates Positively With Interest](../claims/germane-cognitive-load-correlates-positively-with-interest.md) [+M]

## Objective and learner-valued goal

Ask what the learner wants to accomplish and why, separately from the designer's objective. Agreement, divergence and uncertainty are observations; do not infer motivation from compliance or from a low effort rating. The designer chooses the representative task, the permitted aids, the criterion and the horizon; load reduction is a means to that objective, not the objective.

For example, an apprentice electrician may value reading a real wiring diagram on site without a reference card, while the designer's objective is passing a timed schematic-interpretation test. Integrated labels may raise the test score early yet leave the learner's valued performance (reading an unlabelled diagram) untested. Record both aims, and plan when the integrated support is removed and how unaided reading is checked.

## What would revise this model?

The load-reduction expectation should weaken if comparable novices on high-element-interactivity tasks fail to benefit under defensible comparisons with aligned outcomes, or if benefits appear equally for low-element-interactivity material. The expertise qualification should weaken if, as in the multimedia overview above, prior knowledge repeatedly fails to moderate effects when it is measured. If effort falls without any gain in performance or transfer, the model's claim about learning (as opposed to comfort) is not supported for that design. Do not protect the model by relabelling every failure as "too much load" or "too much expertise" after the fact.

A learning-phase efficiency gain, immediate performance, near transfer, delayed retention and unaided use in the learner's setting are separate claims. The present evidence does not establish a threshold of expertise at which to remove support, a universal ordering of techniques, or that reduced load causes the gains it accompanies.

## Related Principles
- [Scaffolding](scaffolding.md)
- [Worked Examples](worked-examples.md)
- [Accessible Vocabulary & Syntax](accessible-vocabulary-syntax.md)
- [Cognitive Load Reduction](cognitive-load-reduction.md)
- [Cognitive Load Management](cognitive-load-management.md)

## Examples
- A novice algebra lesson uses a single integrated visual instead of separate text and diagram panels that learners must constantly coordinate.
- A software onboarding flow replaces open-ended exploration with worked examples and progressively harder tasks until users can perform the workflow independently.

## Key Sources
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296. [https://doi.org/10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Gupta, U., & Zheng, R. Z. (2020). Cognitive Load in Solving Mathematics Problems: Validating the Role of Motivation and the Interaction Among Prior Knowledge, Worked Examples, and Task Difficulty. European Journal of STEM Education, 5(1), 05. https://doi.org/10.20897/ejsteme/9252

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
- [Cognitive Load Reduction](cognitive-load-reduction.md)
- [Cognitive Load Management](cognitive-load-management.md)
- [Cognitive Load Theory](cognitive-load-theory.md)

## Examples
-

## Key Sources
- Gupta, U., & Zheng, R. Z. (2020). Cognitive Load in Solving Mathematics Problems: Validating the Role of Motivation and the Interaction Among Prior Knowledge, Worked Examples, and Task Difficulty. European Journal of STEM Education, 5(1), 05. https://doi.org/10.20897/ejsteme/9252
-->
