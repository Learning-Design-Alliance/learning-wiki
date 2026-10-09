---
type: principle
id: cognitive-load-management
aliases: [design-principles-depend-on-prior-knowledge, determine-element-interactivity-before-designing-instruction, low-task-complexity-child-learners-recasts, measured-pace-one-concept-at-a-time-older-learners, reduce-extraneous-optimize-intrinsic-increase-germane]
title: Cognitive Load Management
description: "Across a sequence, matching how presentation, task order and support distribute processing demand to a learner's current task-specific capacity is expected to improve learning, while keeping effortful processing that the intended outcome and horizon need."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-02
sources:
  - id: sweller-1998
    resource: "https://doi.org/10.1023/A:1022193728205"
    title: "Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296"
    author: "Sweller, J., van Merriënboer, J. J. G., & Paas, F"
  - id: clinton-2017
    resource: "https://eric.ed.gov/?id=ED574984"
    title: "Clinton, V., Cooper, J.L., Michaelis, J., Alibali, M.W., & Nathan, M.J. (2017). How Revisions to Mathematical Visuals Affect Cognition: Evidence from Eye Tracking. In Eye-tracking technology applications in educational research (pp. 195-218). IGI Global. https://eric.ed.gov/?id=ED574984"
    author: "Clinton, V., Cooper, J.L., Michaelis, J., Alibali, M.W., & Nathan, M.J"
  - id: kala-2023
    resource: "https://doi.org/10.36681/tused.2023.027"
    title: "Kala, N., & Ayas, A. (2023). Effect of instructional design based on cognitive load theory on students' performances and the indicators of element interactivity. Journal of Turkish Science Education, 20(3), 468-489. https://doi.org/10.36681/tused.2023.027"
    author: "Kala, N., & Ayas, A"
  - id: lihui-lv-chunyan-liu-2022
    resource: "https://doi.org/10.5539/elt.v15n9p95"
    title: "Lihui Lv & Chunyan Liu. (2022). Recast, Task Complexity and Child Learners' L2 Development. English Language Teaching, 15(9). https://doi.org/10.5539/elt.v15n9p95"
    author: "Lihui Lv & Chunyan Liu"
  - id: weintraub-2025
    resource: "http://doi.org/10.35847/LWeintraub.7.1.37"
    title: "Weintraub, L. (2025). Grandma Needs English, Too. Adult Literacy Education. http://doi.org/10.35847/LWeintraub.7.1.37"
    author: Weintraub, L
  - id: houichi-2020
    resource: "https://dx.doi.org/10.24093/awej/vol11no4.8"
    title: "Houichi, A., & Sarnou, D. (2020). Cognitive Load Theory and its Relation to Instructional Design: Perspectives of Some Algerian University Teachers of English. Arab World English Journal. https://dx.doi.org/10.24093/awej/vol11no4.8"
    author: "Houichi, A., & Sarnou, D"
---

# Cognitive Load Management

> **Principle** · [All principles](index.md)
> **Evidence** · 24 claims (16 for, 8 mixed) · 24 studies (8 quant-synthesis, 7 causal, 7 review, 1 design, 1 theoretical), `q1`–`q4` · 8 of 24 report an effect size · 17 claims rest on one study

## Conditional relationship

For a learner whose current capacity on **the particular task** is limited (a `novice` on that task, whatever their standing in the wider domain), material whose interacting elements must be processed together (`complex-skill`, `principle` or multi-step `procedure` goals) is expected to be learned better when the design distributes processing demand over the sequence instead of presenting it all at once: avoidable processing removed from the presentation, component knowledge introduced before the whole (pretraining, segmenting, isolated parts first), and support withdrawn or effort reintroduced as the learner's task-specific capacity grows. Compared with an unmanaged version of the same material, this is expected to change performance, transfer or efficiency; which of them changes, and whether the change holds at a delayed horizon, differs between the claims below and must be stated for each design.

The relationship has two edges. Too much simultaneous demand for this learner is expected to impede learning; but **less effort is not the objective**. Conditions that slow performance during learning (retrieval, spacing, interleaving, problem-solving before instruction) can improve `delayed-retention`, `conceptual-understanding` or transfer, and support that helps at the start can become redundant later. Managing load therefore means deciding, for a stated outcome and horizon, which demand to remove, which to defer and which to keep.

[Cognitive Load Theory](cognitive-load-theory.md), the converted sibling principle, holds the narrower model that sits inside this one: for task-specific novices on high-element-interactivity material, removing avoidable processing (integrated sources, segmented transient media, isolated elements, full examples) improves immediate performance or efficiency, a relationship that weakens with expertise. This page adds the sequence-level decisions around that lever: when to defer intrinsic demand, when to restore effortful processing, and how to tell which a response calls for. Working-memory limits and schema construction are the explanatory hypotheses of the [theory](../theories/cognitive-load-theory.md) and of the [expertise reversal effect](../theories/expertise-reversal-effect.md); they are not observations. The [4C/ID pattern](../patterns/4cid-four-component-instructional-design.md) is a reusable whole-task policy that applies both; its response-dependent branches remain proposals.

## Observation, state and explanation

Record a response **under stated conditions**: the task and its representation, how many elements must be handled together as judged for this learner, the supports present (integrated labels, segments, a primer, worked steps, hints, aids), the pacing, the time taken and the response mode. "Overloaded", "under-challenged" and "novice" are inferred states. Accuracy, time, a rated mental effort, errors and confidence are observations; none measures working-memory load or a schema directly. A synthesis below found that integrated designs improved learning without reliably changing load ratings, so a rating and a learning outcome can move apart, and a low rating can also mean disengagement or an easy-looking task.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Stalls at the start of a new topic, misusing its terms and asking what parts are called | Component vocabulary missing, so names and relations are being learned at once; a representation the learner cannot read; a language barrier unrelated to the topic | Give a short primer naming the parts, then the same task; separately present the representation with a familiar example. Record which change restores progress and every support given. |
| Fluent, error-free practice with heavy support, then poor on a delayed or changed task | Support removed the processing the outcome needed; performance during learning mistaken for learning; forgetting over the delay | Compare an immediate and a delayed probe on the same items, and a changed item; then give a retrieval or problem-first episode with feedback and see whether the delayed result changes. |
| Rates effort high and progresses slowly, yet improves across sessions | Genuinely high intrinsic demand for this learner, which is not by itself a problem; extraneous demand from the presentation; unfamiliar language | Remove one avoidable demand (split sources, redundant text) while holding the task constant; if effort falls and progress rises, the demand was avoidable. If not, keep the task and sequence it. |
| Skips segments, examples or explanations and does as well without them | Rising task-specific expertise making the support redundant; impatience with a correct need for it; the outcome measure too easy to show the difference | Give an unsupported changed problem; if independent success holds, withdraw support provisionally and re-check later. If it fails, the support may still be needed in a shorter form. |
| Struggles on a problem attempted before instruction, then learns well from the instruction | Productive generation preparing the instruction; learning from the instruction alone; exposure from the attempt as a pretest | Compare conceptual and procedural items separately and note the learner's age and the skill's generality; record the attempts the learner produced. |

These rows are proposals, untested with learners. A probe can shift confidence among explanations; a single contrast does not identify a cause, and each probe is itself a learning exposure that changes the state.

## Evidence and qualifications

- [Managing load through segmenting and worked examples improved learning, with qualifications](../claims/cognitive-load-management.md) [+M]: two meta-analyses. Segmented multimedia (56 investigations, 88 comparisons) had small to medium effects on retention and transfer against continuous presentation, lowered overall rated load and lengthened learning time; learners with high prior knowledge gained **more** on retention than those with little, against what the expertise reversal effect predicts. Worked examples in mathematics (55 studies, elementary to postsecondary) gave g = 0.48, and adding self-explanation prompts produced a negative effect against examples without them, so an added effort-inducing activity did not help there. Horizons are not separated on the claim page. Not yet checked against its sources.
- [Reducing split attention improves learning, though load measures do not show why](../claims/cognitive-load-reduction-improves-learning.md) [+M]: integrated rather than separated text and diagrams, g = 0.63 over 58 comparisons (2,426 participants), holding across many moderators; a second meta-analysis of 50 studies reports the benefit for novices largest with complex materials. A systematic review of 41 comparisons found integrated designs did not reliably change any cognitive-load measure, so the benefit stands while its explanation by reduced load is not established. Not settled: the abstracts available could not confirm the entries.
- [A pretraining primer before a complex lesson improved transfer](../claims/pretraining-improves-transfer.md) [+M]: one randomized experiment, n=93; a video naming a micropipette's parts before an immersive VR procedure lesson, against the same lesson with no primer. The primed group scored higher on a knowledge test, made fewer errors on a real-life transfer task and reported lower load; errors inside VR did not differ. No standardized effect size, delayed horizon or prior-knowledge moderation is reported. It supports deferring component knowledge out of a complex task, not a primer for learners who already know the parts. Not yet checked against its sources.
- [Guidance that helps novices can become redundant or counterproductive as expertise grows](../claims/expertise-reversal-effect.md) [~M]: a synthesis of cognitive load studies, read from its abstract, reporting that integrated explanations, worked examples and step-by-step guidance help novices and can depress performance relative to leaner conditions as prior knowledge increases. No effect sizes, threshold or horizon are recorded. It argues for changing support over time; it does not say when, and the segmenting result above runs the other way on retention. Not settled against its sources.
- [Effortful conditions can slow learning-phase performance while improving delayed retention](../claims/desirable-difficulties-enhance-learning.md) [~M]: three meta-analyses of classroom quizzing (222 studies, g = 0.499 against restudy and other strategies), spaced against massed retrieval (29 studies, g = 0.74) and interleaving for category learning (59 studies, g = 0.42, but blocking beat interleaving for words, g = -0.39). It limits this principle: minimizing effort is not the goal when the outcome is delayed retention. The claim page itself says the difficulty must be surmountable, and none of these studies manipulated presentation load, so it does not say how the two interact. Partly checked: 1 of 2 entries pass, the rest could not be confirmed.
- [Problem-solving before instruction improved conceptual learning and transfer, not procedure](../claims/productive-failure-improves-conceptual-learning.md) [~M]: a meta-analysis of 53 studies (166 comparisons), problem-solving first against the same instruction first: g = 0.36 on conceptual knowledge and transfer, g = −0.03 on procedural knowledge; the advantage **reversed** for second to fifth graders and for domain-general skills. One more randomized study pair in mathematics. It limits the load-reduction default for conceptual goals in older learners; it does not license unguided problem-solving for novices, since instruction follows in every comparison. Partly checked: 1 of 2 entries pass.

Keep learners, task, comparator, outcome and horizon with each result when transporting it. Effort ratings, efficiency, immediate performance, delayed retention and transfer are different outcomes; a non-significant difference is not equivalence; pooled effects do not forecast one learner's response, and these unlike comparisons are not ranked here. **No claim in the wiki tests the general relationship as stated**, a sequence-level policy of removing, deferring and restoring demand against a fixed design; the claims test one lever each.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02 (maintainer's decision): claims this page cited before the 2026-10-02 rewrite which the rewrite did not use as core evidence. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S] — not settled: the text available could not confirm the entries (abstract)
- [Revised Visuals No Learning Effect](../claims/revised-visuals-no-learning-effect.md) [~M]
- [Revised Visuals Processing Text Prior Knowledge Interaction](../claims/revised-visuals-processing-text-prior-knowledge-interaction.md) [+M]
- [Revisions to math-relevant visuals affect cognitive load differently by prior knowledge group, including reduced load for high prior knowledge students](../claims/revised-visuals-cognitive-load-math-visuals-interaction.md) [+W]
- [Revised visuals reduce cognitive load while reading lesson text for low prior knowledge students but increase it for middle prior knowledge students](../claims/revised-visuals-cognitive-load-text-prior-knowledge-interaction.md) [+W]
- [Revised visuals reduce cognitive processing of math-relevant visuals for low prior knowledge students but increase it for middle prior knowledge students](../claims/revised-visuals-processing-math-visuals-interaction.md) [+W]
- [Revisions made no reliable difference to total time spent with the lesson](../claims/revisions-no-effect-time-with-lesson.md) [+W]
- [Mental Effort Study Time Indicate Element Interactivity](../claims/mental-effort-study-time-indicate-element-interactivity.md) [+M]
- [Clt Design Effective Learning Retention Transfer](../claims/clt-design-effective-learning-retention-transfer.md) [+M]
- [As the element interactivity level of thermodynamics topics increases, learning becomes more difficult and retention and transfer scores decrease](../claims/retention-transfer-scores-decrease-with-element-interactivity.md) [+W]
- [A CLT-based instructional design yields significantly higher retention and transfer scores than lecturer-designed instruction in thermodynamics, controlling for prior knowledge and memory span](../claims/clt-instructional-design-raises-retention-transfer-thermodynamics.md) [+W]
- [No significant difference between groups on the thermodynamics achievement post-test or cognitive load scale after CLT-based versus lecturer-designed instruction](../claims/no-group-difference-tat-posttest-cls.md) [~W]
- [Task Complexity Negatively Related Child Written Production](../claims/task-complexity-negatively-related-child-written-production.md) [+M]
- [Task Complexity No Effect Child Oral Production](../claims/task-complexity-no-effect-child-oral-production.md) [~M]
- [Older Beginner Esl Outcome Gains](../claims/older-beginner-esl-outcome-gains.md) [+M]
- [Common language teaching methods such as oral drills, memorization, and fast-paced competitive activities disadvantage older learners](../claims/rote-drills-disadvantage-older-learners.md) [+W]
- [Learning ability does not decline with age in healthy older adults](../claims/learning-ability-does-not-decline-with-age.md) [~W]
- [No research evidence suggests older adults cannot succeed in learning another language, though adults need more deliberate learning effort than children](../claims/no-evidence-older-adults-cannot-learn-language.md) [~W]

## Objective and learner-valued goal

Ask what the learner wants to accomplish and why, separately from the designer's objective. Agreement, divergence and uncertainty are observations; do not infer motivation from compliance or from a low effort rating. The designer chooses the representative task, the permitted aids, the criterion and the horizon. Load management is a means to that objective, and the objective decides which effort is avoidable: an aid that removes effort is a support if the objective allows it and an obstacle to the target if it does not.

For example, a laboratory trainee may value getting through a pipetting session without the embarrassment of handling equipment they cannot name, while the designer's objective is accurate unaided pipetting a week later. A primer and step-by-step guidance can serve the first and raise in-session accuracy, yet the delayed, unaided performance remains untested until it is probed. Record both aims, say when the guidance is withdrawn, and check the delayed task.

## What would revise this model?

The model should weaken if comparable learners on comparable material learn as well from the unmanaged design under defensible comparisons with aligned outcomes, or if deferring component knowledge (primers, segments, parts first) repeatedly fails to help on tasks with many interacting elements. The expertise qualification should weaken if, as in the segmenting synthesis, higher prior knowledge keeps predicting larger rather than smaller benefits. The "keep productive effort" edge should weaken if effortful conditions fail to improve delayed outcomes for the learners and materials in question, as interleaving did for word lists and problem-first designs did for younger children. If rated effort falls without any gain in performance, transfer or retention, the design reduced discomfort, not demand on learning. Do not protect the model by relabelling every failure after the fact as "too much load" or "too little challenge".

A learning-phase efficiency gain, immediate performance, near transfer, delayed retention and unaided use in the learner's setting are separate claims. The present evidence does not establish a threshold of expertise at which to remove support, an optimal amount of difficulty, an ordering of load-management techniques, or that changes in load cause the gains they accompany.

## Related Principles
- [Cognitive Load Theory](cognitive-load-theory.md)
- [Use the age-friendly ESL classroom as a remedy for social isolation by building a supportive community of learners with confidence-building and peer mentoring](expanding-social-networks.md)
- [Contextualize abstract content in familiar, personal topics and teach new vocabulary primarily through visuals and body language](contextualize-abstract-content-older-learners.md)

## Examples
- A math lesson introduces multi-step equation solving in short worked chunks, with each step visually separated and narrated before learners attempt a full problem.
- A science simulation hides advanced controls for novices, then gradually reveals more variables once learners can explain the core system.
- [Consider a focused more is more approach combining minimized extraneous processing with prompts for generative processing](../strategies/focused-more-is-more-generative-processing.md)
- [Step One: a free age-friendly pre-beginning ESL and citizenship curriculum for older immigrants](../elements/step-one-age-friendly-esl-curriculum.md)
- [Accommodating Processing Speed Challenges](../strategies/accommodating_processing_speed_challenges.md)
- [Allow Think-Time and Re-reading (Processing Speed)](../strategies/allow-think-time-and-re-reading-processing-speed.md)
- [Wait Time](../strategies/wait-time.md)
- [Allowing Think-Time and Re-Reading](../strategies/allowing_think-time_and_re-reading.md)
- [Think-Time and Re-Reading](../strategies/think-time_and_re-reading.md)
- [Jointly varying intrinsic and extraneous load in a Reversi game to isolate germane load effects](../designs/reversi-training-conditions-varying-intrinsic-and-extraneous-load.md)

## Key Sources
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296. [https://doi.org/10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Clinton, V., Cooper, J.L., Michaelis, J., Alibali, M.W., & Nathan, M.J. (2017). How Revisions to Mathematical Visuals Affect Cognition: Evidence from Eye Tracking. In Eye-tracking technology applications in educational research (pp. 195-218). IGI Global. https://eric.ed.gov/?id=ED574984
- Kala, N., & Ayas, A. (2023). Effect of instructional design based on cognitive load theory on students' performances and the indicators of element interactivity. Journal of Turkish Science Education, 20(3), 468-489. https://doi.org/10.36681/tused.2023.027
- Lihui Lv & Chunyan Liu. (2022). Recast, Task Complexity and Child Learners' L2 Development. English Language Teaching, 15(9). https://doi.org/10.5539/elt.v15n9p95
- Weintraub, L. (2025). Grandma Needs English, Too. Adult Literacy Education. http://doi.org/10.35847/LWeintraub.7.1.37
- Houichi, A., & Sarnou, D. (2020). Cognitive Load Theory and its Relation to Instructional Design: Perspectives of Some Algerian University Teachers of English. Arab World English Journal. https://dx.doi.org/10.24093/awej/vol11no4.8

<!-- deprecated 2026-10-02: superseded by the conditional model above; the principle body as it stood before the rewrite, kept verbatim.

## Description
Cognitive load management is the short-form canonical target for instructional choices that reduce extraneous processing, sequence support, and calibrate task demands to learner expertise.

## Implications
Cognitive load management matters when instruction risks overwhelming working memory before learners have formed stable schemas. In practice, this means chunking information and removing unnecessary complexity so learners can devote more attention to the underlying idea or procedure [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S]. These moves usually make early learning more manageable, but the same supports can become inefficient once learners are more knowledgeable, so guidance should fade or simplify as expertise grows [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M].

### Context
#### Requirements
- **Attention to what consumes working memory**
- **Support matched to task complexity and learner expertise**
#### Constraints
- **Over-management can remove productive challenge**

### Target Learning Objectives
- Preserve capacity for understanding and schema construction.

### Theory
#### Supporting
- [Cognitive Load Theory](cognitive-load-theory.md)

### Claims
- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S] — reducing unnecessary processing and organizing material into coherent units preserves capacity for schema formation
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M] — supports that help novices can become inefficient or redundant as learner expertise increases
-->

<!-- merged 2026-10-07 from principles/design-principles-depend-on-prior-knowledge ("Apply instructional design principles with attention to learners' prior knowledge, since effects on cognition depend on proficiency level"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Apply instructional design principles with attention to learners' prior knowledge, since effects on cognition depend on proficiency level

> **Principle** · [All principles](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The article concludes that although many instructional design principles are framed as "one size fits all," their effects on student cognition may depend on students' level of prior knowledge. Revisions based on signaling, contiguity, and coherence principles reduced cognitive load and processing for low prior knowledge students but increased them for middle prior knowledge students. Curriculum developers should therefore consider prior knowledge when applying such principles, and the authors caution it "may be premature to apply these principles to curriculum development on a large scale."

## Design Implications

### Context
#### Requirements
- Assessment of learners' prior knowledge before applying design revisions
#### Constraints
- The findings do not support the effectiveness of the "less is more" approach in improving student learning; combining principles makes it uncertain how each principle individually related to the findings

### Target Learners
- middle-school mathematics students

### Target Learning Objectives
- learning from lessons with text and visual representations

### Claims

- [Revised Visuals No Learning Effect](../claims/revised-visuals-no-learning-effect.md) [~M]
- [Revised Visuals Processing Text Prior Knowledge Interaction](../claims/revised-visuals-processing-text-prior-knowledge-interaction.md) [+M]
- [Revisions to math-relevant visuals affect cognitive load differently by prior knowledge group, including reduced load for high prior knowledge students](../claims/revised-visuals-cognitive-load-math-visuals-interaction.md) [+W]
- [Revised visuals reduce cognitive load while reading lesson text for low prior knowledge students but increase it for middle prior knowledge students](../claims/revised-visuals-cognitive-load-text-prior-knowledge-interaction.md) [+W]
- [Revised visuals reduce cognitive processing of math-relevant visuals for low prior knowledge students but increase it for middle prior knowledge students](../claims/revised-visuals-processing-math-visuals-interaction.md) [+W]
- [Revisions made no reliable difference to total time spent with the lesson](../claims/revisions-no-effect-time-with-lesson.md) [+W]

## Related Principles
- 

## Examples

- [Consider a focused more is more approach combining minimized extraneous processing with prompts for generative processing](../strategies/focused-more-is-more-generative-processing.md)

## Key Sources
- Clinton, V., Cooper, J.L., Michaelis, J., Alibali, M.W., & Nathan, M.J. (2017). How Revisions to Mathematical Visuals Affect Cognition: Evidence from Eye Tracking. In Eye-tracking technology applications in educational research (pp. 195-218). IGI Global. https://eric.ed.gov/?id=ED574984
-->

<!-- merged 2026-10-07 from principles/determine-element-interactivity-before-designing-instruction ("Teachers should determine a topic's element interactivity level and develop an instructional design appropriate to it"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Teachers should determine a topic's element interactivity level and develop an instructional design appropriate to it

> **Principle** · [All principles](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 5 claims rest on one study

## Description
The article concludes that "Teachers are responsible for determining a topic's level of element interactivity and developing an appropriate instructional design." Because complexity within CLT arises from element interactivity, teachers should first classify the topics they teach (e.g. with expert judgement into low, high, very high) and then design instruction — such as CLT-based materials — that manages working memory load accordingly. The study's evidence that scores, mental effort and study time track interactivity level grounds this recommendation.

## Design Implications

### Context
#### Requirements
- Determination of students' prior knowledge before classifying topics, since interactivity level depends on the learner's existing schemata.
#### Constraints
- The study's classification was made relative to topics within one unit, judged by two expert lecturers with over ten years' experience each.

### Target Learners
- first-year university chemistry students
- high school chemistry students

### Target Learning Objectives
- effective learning of high element interactivity science topics at retention and transfer levels

### Claims

- [Mental Effort Study Time Indicate Element Interactivity](../claims/mental-effort-study-time-indicate-element-interactivity.md) [+M]
- [Clt Design Effective Learning Retention Transfer](../claims/clt-design-effective-learning-retention-transfer.md) [+M]
- [As the element interactivity level of thermodynamics topics increases, learning becomes more difficult and retention and transfer scores decrease](../claims/retention-transfer-scores-decrease-with-element-interactivity.md) [+W]
- [A CLT-based instructional design yields significantly higher retention and transfer scores than lecturer-designed instruction in thermodynamics, controlling for prior knowledge and memory span](../claims/clt-instructional-design-raises-retention-transfer-thermodynamics.md) [+W]
- [No significant difference between groups on the thermodynamics achievement post-test or cognitive load scale after CLT-based versus lecturer-designed instruction](../claims/no-group-difference-tat-posttest-cls.md) [~W]

## Related Principles
- 

## Examples
-

## Key Sources
- Kala, N., & Ayas, A. (2023). Effect of instructional design based on cognitive load theory on students' performances and the indicators of element interactivity. Journal of Turkish Science Education, 20(3), 468-489. https://doi.org/10.36681/tused.2023.027
-->

<!-- merged 2026-10-07 from principles/low-task-complexity-child-learners-recasts ("For child beginner language learners, keep task complexity low or moderate so attention remains available for noticing recasts"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# For child beginner language learners, keep task complexity low or moderate so attention remains available for noticing recasts

> **Principle** · [All principles](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends that when designing tasks for young foreign language beginners, cognitive demands should match learners' cognitive development level: "it is better to set a moderate or low task complexity level to allow the learners to have more attention available for the development of the target-like language." Otherwise learners become cognitively overloaded and have little attention left to notice recasts and process the target language.

## Design Implications

### Context
#### Requirements
- Tasks must still elicit production of the target form so that recasts can be supplied in response to errors
#### Constraints
- Grounded in child learners aged 11-12 learning English in China; the authors state task complexity should not exceed child learners' cognitive load

### Target Learners
- child beginner EFL learners in primary school

### Target Learning Objectives
- grammar acquisition through corrective feedback during task-based interaction

### Claims
- [Task Complexity Negatively Related Child Written Production](../claims/task-complexity-negatively-related-child-written-production.md) [+M]
- [Task Complexity No Effect Child Oral Production](../claims/task-complexity-no-effect-child-oral-production.md) [~M]

## Related Principles
- 

## Examples
-

## Key Sources
- Lihui Lv & Chunyan Liu. (2022). Recast, Task Complexity and Child Learners' L2 Development. English Language Teaching, 15(9). https://doi.org/10.5539/elt.v15n9p95
-->

<!-- merged 2026-10-07 from principles/measured-pace-one-concept-at-a-time-older-learners ("Teach older language learners at a measured pace, one new skill or concept at a time, with extra review and wait time"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Teach older language learners at a measured pace, one new skill or concept at a time, with extra review and wait time

> **Principle** · [All principles](index.md)
> **Evidence** · 4 claims (2 for, 2 mixed) · 3 studies (2 review, 1 design), `q1`–`q2` · 0 of 3 report an effect size · 4 claims rest on one study

## Description
Because older adults tend to process information more slowly and may have declining working memory, the author delivers instruction in careful stages, provides more repetition and review than a typical ESL class, and lets students demonstrate comprehension (yes/no, "or", and "show me" tasks) before producing new language from memory. She reports that "A few extra seconds of "wait time" can make a big difference in students' willingness to take risks, their ability to produce responses, and to develop confidence in speaking English." She also found combining several new concepts in one activity caused lessons to fail to connect.

## Design Implications

### Context
#### Requirements
- Instructors must plan staged presentation of new information and resist combining multiple new concepts in a single activity
#### Constraints
- The author notes not every older student exhibits the same characteristics, but the older the student, the more likely modifications are needed

### Target Learners
- older adult beginning-level English learners

### Target Learning Objectives
- oral English comprehension and production
- retention of new vocabulary and concepts

### Claims

- [Older Beginner Esl Outcome Gains](../claims/older-beginner-esl-outcome-gains.md) [+M]
- [Common language teaching methods such as oral drills, memorization, and fast-paced competitive activities disadvantage older learners](../claims/rote-drills-disadvantage-older-learners.md) [+W]
- [Learning ability does not decline with age in healthy older adults](../claims/learning-ability-does-not-decline-with-age.md) [~W]
- [No research evidence suggests older adults cannot succeed in learning another language, though adults need more deliberate learning effort than children](../claims/no-evidence-older-adults-cannot-learn-language.md) [~W]

## Related Principles

- [Use the age-friendly ESL classroom as a remedy for social isolation by building a supportive community of learners with confidence-building and peer mentoring](expanding-social-networks.md)
- [Contextualize abstract content in familiar, personal topics and teach new vocabulary primarily through visuals and body language](contextualize-abstract-content-older-learners.md)

## Examples

- [Step One: a free age-friendly pre-beginning ESL and citizenship curriculum for older immigrants](../elements/step-one-age-friendly-esl-curriculum.md)
- [Accommodating Processing Speed Challenges](../strategies/accommodating_processing_speed_challenges.md)
- [Allow Think-Time and Re-reading (Processing Speed)](../strategies/allow-think-time-and-re-reading-processing-speed.md)
- [Wait Time](../strategies/wait-time.md)
- [Allowing Think-Time and Re-Reading](../strategies/allowing_think-time_and_re-reading.md)
- [Think-Time and Re-Reading](../strategies/think-time_and_re-reading.md)

## Key Sources
- Weintraub, L. (2025). Grandma Needs English, Too. Adult Literacy Education. http://doi.org/10.35847/LWeintraub.7.1.37
-->

<!-- merged 2026-10-07 from principles/reduce-extraneous-optimize-intrinsic-increase-germane ("Manage the three load types: reduce extraneous load, optimize intrinsic load, and increase germane load"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Manage the three load types: reduce extraneous load, optimize intrinsic load, and increase germane load

> **Principle** · [All principles](index.md)
> **Evidence** · 1 claim (1 for) · 2 studies (2 quant-synthesis), `q4` · 1 of 2 report an effect size

## Description
The article states that instructional material is most effective when no load type overburdens working memory capacity, and that educators must manage the three loads differentially. It attributes to Van Merrienboer and Sweller the directive that "Educators must seek to reduce extraneous load, optimize intrinsic load, and increase germane load". Reducing extraneous load frees working-memory capacity that can then be allocated to germane processing, supporting schema construction in long-term memory.

## Design Implications

### Context
#### Requirements
- Teachers must understand human cognitive architecture and the three load types to apply the principle
#### Constraints
- The extent to which instructional features contribute to extraneous or germane load may depend on the learner and their experienced intrinsic load

### Target Learners
- university EFL students

### Target Learning Objectives
- effective instructional design that avoids working memory overload

### Claims

- [Clt Three Load Types Framework](../theories/clt-three-load-types-framework.md) [+M]
- [Cognitive Load Management](../claims/cognitive-load-management.md) [+M]

## Related Principles
- 

## Examples

- [Jointly varying intrinsic and extraneous load in a Reversi game to isolate germane load effects](../designs/reversi-training-conditions-varying-intrinsic-and-extraneous-load.md)

## Key Sources
- Houichi, A., & Sarnou, D. (2020). Cognitive Load Theory and its Relation to Instructional Design: Perspectives of Some Algerian University Teachers of English. Arab World English Journal. https://dx.doi.org/10.24093/awej/vol11no4.8
-->
