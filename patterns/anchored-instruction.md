---
type: pattern
id: anchored-instruction
aliases: [storyline-science-curriculum-design]
title: Anchored Instruction
description: "A reusable policy for building a lesson or unit around a shared narrative or media scenario: check that solving the anchor's problem requires the target concept, guide novices through it rather than leave them to search, connect the anchor explicitly to the concept, and judge the unit on individual use of the concept in a new situation."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-02
sources:
  - id: cognition-and-technology-group-at-vanderbilt-1992
    resource: "https://doi.org/10.1007/BF02296729"
    title: "Cognition and Technology Group at Vanderbilt. (1992). The Jasper experiment: An exploration of issues in learning and instructional design. *Educational Technology Research and Development, 40*(1), 65-80"
    author: Cognition and Technology Group at Vanderbilt
  - id: penuel-et-al-2022
    resource: "https://doi.org/10.1080/07370008.2021.2010207"
    title: "Penuel, W. R., Allen, A.-R., Henson, K., Campanella, M., Patton, R., Rademaker, K., Reed, W., Watkins, D., Wingert, K., Reiser, B., & Zivic, A. (2022). Learning Practical Design Knowledge through Co-Designing Storyline Science Curriculum Units. Cognition and Instruction, 40(1), 148-170."
    author: "Penuel, W. R., Allen, A.-R., Henson, K., Campanella, M., Patton, R., Rademaker, K., Reed, W., Watkins, D., Wingert, K., Reiser, B., & Zivic, A."
author: John Bransford and the Cognition and Technology Group at Vanderbilt
grain_size: lesson
---

# Anchored Instruction

> **Pattern** · [All patterns](index.md)
> **Evidence** · 14 claims (4 for, 9 mixed, 1 against) · 30 studies (12 causal, 8 quant-synthesis, 4 review, 3 qualitative, 1 associational, 1 design, 1 theoretical), `q1`–`q4` · 5 of 30 report an effect size · 9 claims rest on one study

## Description and scope

A reusable policy for organizing a lesson or unit around one rich, shared scenario (a story, video or multimedia situation, the "anchor") that contains the information, constraints and question learners must work with, and for deciding how the anchor is built, how much guidance learners get while they work in it, and how the anchor is connected back to the target concept. It draws on the [problem-based learning principle](../principles/problem-based-learning.md) and on [inquiry-based learning](../principles/inquiry-based-learning.md). The study configurations below are evidence about neighbouring relationships; the response-dependent policy is an **untested design proposal**. Use it to gather better evidence about a learner group, not to certify that a learner "can apply the concept in context".

**What the evidence does and does not test.** No claim recorded in this wiki tests anchored instruction itself: neither an anchored unit against another format, nor an anchor against the same problem posed without one. The claims below test neighbouring relationships (how much guidance novices need, contingent support, irrelevant but interesting detail, the link between a concrete representation and the concept, part-task practice for complex wholes). This page therefore treats the anchor as a delivery vehicle whose value is unestablished, and treats guidance, an explicit connection to the concept and an individual transfer probe as the parts of the configuration the evidence bears on. "Use a compelling scenario" on its own is an unsupported promise.

**How the converted siblings sit beside it.** [Problem-based learning](problem-based-learning.md) is the more general pattern for problem-centred units: it owns the decisions about guidance level for novices, whether a problem-first phase precedes instruction, and consolidation. This page applies those decisions and adds only what is specific to an anchor: building a shared scenario whose embedded information makes the target concept necessary, keeping the scenario's detail from displacing the concept, and returning to the same anchor as understanding develops. [Case-based learning](case-based-learning.md) works at lesson grain with several cases analysed and compared; where a designer uses more than one anchor, or wants learners to abstract a principle across anchors, its comparison guidance applies rather than this page's.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Age band (`child`, `adolescent`, `adult`) and task-specific starting knowledge (`novice`, `intermediate`, `advanced`, or `?`); each learner's brief independent first response to the anchor: what they think the question is, which information they think matters, and what they would do first. Preserve unknowns. |
| Context and activities | Setting (`classroom`, `online-instructor-led`, `workplace-clinical`, ...), duration (`single-session`, `days-weeks`), group size, who facilitates, the anchor's format and length, and exactly which prompts, resources, explanations and feedback are planned and when. |
| Learner-valued goal | Ask what the learner wants from working on a situation like this one and why (to solve problems they meet outside class, to pass an assessment, to understand the subject). Record disagreement with the designer objective; negotiate rather than assume agreement. |
| Designer objective | The concept, principle or complex skill (`concept`, `principle`, `complex-skill`) the anchor is meant to carry, its element interactivity (`low`, `high`, `?`), and whether a correct resolution of the anchor's problem actually requires it. |
| Outcome | Separate instruments for use of the concept in a new situation (`near-transfer`, `far-transfer`), `conceptual-understanding`, and recall of the anchor's own details; individual as well as group measures; immediate and delayed horizons. |

A request for "engaging, real-world learning" does not specify these inputs. Ask for them before building an anchor, choosing a guidance level or predicting a gain. Check first that the anchor's embedded information is correct, that the problem cannot be resolved by common sense or by reading the story alone, and which details in it are deliberately irrelevant (distractors that are part of the task) and which are only decorative.

## Sequence and conditional policy

Each step carries its evidence status. The steps are the earlier page's sequence, kept as a default design and now labelled; none has been tested as an anchored sequence.

1. **Present the anchor, then elicit individually.** Show the scenario and ask each learner (not only the group) what the question is, what they notice and what they need to know. Keep this short and record it as a learning exposure. *Untested; from the earlier page.*
2. **Choose the guidance level provisionally.** For task-specific novices on the target concept, make the concept available explicitly (a short explanation, a modelled step, resources that carry it) before or alongside the work in the anchor, rather than leaving it to be found. A problem-first phase is a narrower candidate, for learners who can generate partial solutions, and must be followed by instruction (see the [problem-based learning pattern](problem-based-learning.md)). *Bears on: [unassisted discovery underperforms explicit instruction for novices, while enhanced discovery outperforms other instruction](../claims/minimal-guidance-less-effective-for-novices.md) [~S]; not tested in anchored units.* Where the anchor's whole problem is too complex for the learner's current knowledge, consider isolating a component first. *Bears on: [part-task practice for novices](../claims/part-task-practice-reduces-load-for-novices.md) [~M]; one experiment, unchecked.*
3. **Guide the inquiry contingently.** Learners work through the anchor's data and constraints, collaboratively where planned. Raise support when a learner or group is stuck, lower it when they progress, and record each intervention. *Bears on: [contingent scaffolding](../claims/contingent-scaffolding-improves-learning.md) [+M], from one-to-one tutoring; not tested in anchored groups.*
4. **Have learners propose, justify and refine; revisit the anchor.** Ask learners to state which information from the anchor their solution uses and why, and to return to the anchor to check it. *Untested; from the earlier page.*
5. **Connect the anchor explicitly to the concept.** Debrief the reasoning, name the concept, and show how it maps onto the anchor's specifics; correct a mapping learners have built wrongly. *Bears on: [concrete materials help only when explicitly connected to the concept](../claims/manipulatives-require-connection-to-concept.md) [~M], a review about manipulatives in mathematics and science, carried here by analogy only.*
6. **Reobserve individually in a new situation.** Use a problem with different surface details that requires the same concept, scored separately for use of the concept and for recall of the anchor, at the agreed horizon. If the response disagrees with the expectation, revise the interpretation or the configuration. *Untested; added in this rewrite.*

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Learners retell the story but cannot say what the question is | Ask for a first decision only, or show a model of a finished answer to a different anchor; re-present the key information in a simpler form. | If a simpler presentation releases a start, the barrier may be access to the anchor (length, language, media): adjust the anchor. If not, supply the target concept explicitly before continuing. Neither branch is a validated diagnosis. |
| Discussion centres on vivid story details that do not bear on the problem | Ask which pieces of information the answer depends on; check whether those details were intended as distractors or are only decorative. | If decorative, trim or de-emphasize them. If they are intended distractors, prompt for relevance judgements explicitly. The seductive-details evidence concerns decorative additions to text and shows small, learner-dependent effects, so this is a precaution, not a predicted loss. |
| Group reaches an answer, but individuals cannot explain which concept it uses | Individual explanation, or a changed condition inside the same anchor, matched in demand. | Move the explicit connection (step 5) earlier, or add an individual justification prompt; record who contributed what. Activity and a group answer do not show that each member learned the concept. |
| Concept used inside the anchor, but not on a new problem | A problem with new surface details and the same concept. | Make the mapping from anchor to concept explicit and give a second situation; consider [comparing two anchors or cases](case-based-learning.md). Knowledge tied to one concrete representation may not travel; the claim recording this is an argument, not a test. |
| Learners stall for a long time and attempts do not converge | Ask what they already know that applies; check whether the anchor's problem needs several new ideas at once. | Give targeted support or a worked step now; if many new elements interact, isolate one component first and return to the whole anchor. The supporting experiment is single and unchecked. |

## Choosing configurations from evidence

- **Whether to expect anything from the anchor itself.** No claim recorded here compares anchored instruction with another format, or an anchored problem with the same problem posed plainly. Plan and evaluate a specific configuration; do not promise a gain from the label or from the scenario's realism.
- **Amount of guidance.** [Minimal guidance is less effective for novices than explicit instruction](../claims/minimal-guidance-less-effective-for-novices.md) [~S]: a meta-analysis pooled 580 comparisons in which explicit instruction outperformed unassisted discovery (d = 0.38 in favour of explicit instruction) and 360 in which discovery enhanced with feedback, worked examples, scaffolding or elicited explanations outperformed other instruction (d = 0.30); with 112 third- and fourth-graders learning to design unconfounded experiments, many more mastered the procedure by direct instruction than by discovery, and those taught directly did as well on a later transfer task. This rules out an anchor in which novices must find the essential concept unsupported; it does not rule out guided work inside an anchor. The meta-analysis is not broken down by prior knowledge on the claim page, and no study it reports used an anchor.
- **Facilitation.** [Contingent scaffolding improves learning more than fixed or absent support](../claims/contingent-scaffolding-improves-learning.md) [+M]: in one-to-one tutoring of fourth and fifth graders on long division (8 per condition), fully contingent support beat fixed, moderate and no support at immediate and one-month tests; in a second small study a contingent, questioning style gave similar immediate learning and better transfer. A dynamic-assessment meta-analysis found explicit strategy training more effective than scaffolding. The evidence comes from one-to-one tutoring; whether a teacher can be contingent with groups working in an anchor is not recorded.
- **Rich detail.** [Interesting but irrelevant details can impair comprehension and transfer, with effects that vary with the material and the learner](../claims/seductive-details-effect.md) [~M]: a meta-analysis found that seductive additions can hinder learning, with the effect depending on format and design features; decorative pictures neither helped nor harmed 7th and 8th graders overall but weakened the benefit of instructional pictures, most for learners with lower prior knowledge; in undergraduates a small harm (η² = .04) appeared, and in a harder follow-up only for students with low attentional inhibition. These are decorative additions to texts and e-learning, not narrative anchors whose details carry the problem's data, so they argue for checking each detail's purpose, not for stripping the anchor.
- **Connecting the anchor to the concept.** [Manipulatives require connection to concept](../claims/manipulatives-require-connection-to-concept.md) [~M]: a systematic review of concreteness fading in mathematics and science argues that concrete materials aid learning only when explicitly and gradually connected to the abstract representation, not left unconnected. It concerns manipulatives and concrete-to-symbolic sequences; applying it to a narrative anchor is an analogy that no recorded study tests. A single designers' reflection, with no learner data, found that the context of a real-life mathematics task [dropped out once the mathematical relationships were recognized](../claims/contextualized-real-life-task-reverted-to-pure-mathematics-and-felt-too-school.md) [~W]: a reason to decide in advance whether the anchor is meant to stay in play or to be left behind.
- **When the whole problem is too complex.** [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition](../claims/part-task-practice-reduces-load-for-novices.md) [~M]: in one experiment, novices on tasks with high element interactivity did better when first given isolated parts before the integrated whole. The page records no sample size and no effect size, and its source has not been checked. It qualifies an anchor that presents one large integrated problem to novices; it does not say the anchor should be abandoned.

Do not rank these results against one another: their comparators (unassisted discovery, fixed support, materials without decoration, unconnected concrete materials, whole-task presentation) and outcomes differ, and none was measured in an anchored unit. A precise abstention names the missing comparison, outcome or observation and the next way to resolve it.

## Fitting the design to a situation

No claim in the wiki tests an anchored unit against another format, so these rows adjust the parts the evidence bears on. Ask for four facts when the brief omits them: **what do learners already know of the target concept?**, **which details in the anchor are needed for the problem and which are decoration?**, **is transfer to a new situation the goal?**, and **how many sessions are there?**

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are novices on the concept the anchor is meant to carry | Make the concept available explicitly (a short explanation or modelled step) before or alongside the work in the anchor | [Minimal guidance is less effective for novices](../claims/minimal-guidance-less-effective-for-novices.md) [-M] |
| The anchor is a vivid story or video with much interesting but irrelevant detail, and learners have low prior knowledge | Trim or play down decorative details; keep only distractors that are part of the task, and prompt for relevance judgements on those | [Seductive details can impair comprehension and transfer](../claims/seductive-details-effect.md) [-M] |
| The goal is use of the concept in new situations | Give a second anchor or case with different surface details and the same concept, and have learners compare the two | [Comparing cases side by side improves learning and transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M] |
| The debrief is planned as a retelling of the story | Make step 5 an explicit mapping: name the concept and show which parts of the anchor correspond to it | [Concrete materials help only when connected to the concept](../claims/manipulatives-require-connection-to-concept.md) [~W] (manipulatives; carried to anchors by analogy) |
| The anchor's problem needs several new interacting ideas at once and learners are complete beginners | Isolate one component first, then return to the whole anchor | [Part-task practice reduces load for absolute novices](../claims/part-task-practice-reduces-load-for-novices.md) [~W] |
| Small groups work in the anchor with a facilitator | Raise support when a group is stuck and lower it when it progresses, recording each intervention | [Contingent scaffolding improves learning](../claims/contingent-scaffolding-improves-learning.md) [+M] (one-to-one tutoring) |
| The anchor is a simulation or video that learners work through alone (`online-self-paced`) | Build prompts and feedback into the environment instead of leaving the anchor open | [Guidance added to simulation inquiry modestly improves outcomes](../claims/simulation-guidance-moderate-effect-dangelo.md) [+W] |
| Learners are in the early primary years and the plan has them attempt the anchor's problem before any teaching | Teach the concept first and use the anchor as application | [PS-I effects are negative for 2nd–5th graders](../claims/psi-effect-increases-with-grade-level.md) [-M] |
| Only one session is available | Use one short anchor, connect it explicitly to the concept within the session, and end with one individual item on a new situation | untested proposal |
| The assessment asks about the anchor's own story | Score recall of the anchor separately from use of the concept on a new problem; only the second shows the concept travelled | untested proposal |

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02 (maintainer's decision): claims this page cited before the 2026-10-02 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [~M] — checked by the judge: all 1 entries pass (abstract)
- [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [~S] — not settled: the text available could not confirm the entries (abstract)
- [Co-design tools for standards analysis, student-interest data, and launch rehearsal support balancing standards alignment with student interests](../claims/co-design-tools-support-balancing-standards-and-student-interests.md) [+M]
- [OpenSciEd enactment faces key challenges: project fatigue, unit length and pacing, pseudoagency, and gaps in student sensemaking practices](../claims/openscied-enactment-challenges-fatigue-pacing-pseudoagency.md) [~W]

## Illustrative design instance and observation record

*Illustration only, invented, not a tested lesson.* A lower-secondary mathematics class (`adolescent`, `classroom`, `days-weeks`) watches a ten-minute video in which a family plans a day trip: the video embeds a map with distances, a fuel gauge, the car's consumption, opening times and a budget, and ends by asking whether they can reach the lake and be home by dark. The designer's objective is that learners can use rates (distance, time, consumption) to test a plan; one learner says he wants to be able to plan his own cycling trips. Agree that both using rates on a new plan and a checked trip plan of his own matter. Ask each learner for a first framing; most guess from the story and none computes a time. Give a short explicit explanation of rate with one worked step, let pairs work through the anchor's data with contingent prompts, revisit the video to check assumptions, then debrief by naming the rate relationships and mapping each to the video. Assess individually two weeks later with a different journey, scored separately for use of rates and for recall of the video's details.

Record: **anchor and its embedded data → each learner's first framing → explanations, prompts and support actually given, with timing → solutions proposed and the anchor information each used → candidate interpretations and confidence basis → distinguishing probe → explicit connection delivered → individual response to a new situation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record but must not fabricate missing inputs or assign numerical state probabilities without a calibrated model.

## Elements and limits

[Anchored instruction](../elements/anchored-instruction.md), [problem scenario](../elements/problem-scenario.md), [problem presentation](../elements/problem-presentation.md), [peer interaction](../elements/peer-interaction.md), [scaffolding](../elements/scaffolding.md), [explicit teaching](../elements/explicit-teaching.md), [self-explanation](../elements/self-explanation.md), [comparing cases](../elements/comparing-cases.md) and [debrief](../elements/debrief.md).

This pattern is scoped to lessons and units built around one shared scenario, with guidance and an explicit connection to the target concept planned. Fully self-directed inquiry in an anchor, multi-anchor curricula, and anchors judged only on engagement need distinct configurations and evidence. The wiki records no comparison of anchored instruction with another approach, and the diagnostic branches above remain to be tested with actual learners.

## Claims

- [In the Reading in Four Voices task, students connected story values to a distance–time graph by engaging in both literacy and oracy](../claims/reading-four-voices-connects-story-and-graph.md) [~W]

## Related Patterns

- [Problem-Based Learning (PBL)](problem-based-learning.md)
- [Goal-Based Scenarios (GBS)](goal-based-scenarios.md)
- [Learning by Producing (multimedia production as learning)](learning-by-producing-pattern.md)
- (none yet linked)

## Examples
- Jasper-style video math problems that embed quantitative reasoning in a narrative.
- Case launches in science or civics where learners work from a shared media scenario.
- Professional training modules built around a realistic event or dilemma.
- A high school unit anchored in space exploration (selected over a student-interest-matched air-pollution phenomenon because air pollution content matched middle-school, not high-school, standards).

## Key Sources
- Bransford, J. D., Sherwood, R. D., Hasselbring, T. S., Kinzer, C. K., & Williams, S. M. (1990). Anchored instruction: Why we need it and how technology can help. In D. Nix & R. Spiro (Eds.), *Cognition, education, and multimedia* (pp. 115-141). Erlbaum.
- Cognition and Technology Group at Vanderbilt. (1992). The Jasper experiment: An exploration of issues in learning and instructional design. *Educational Technology Research and Development, 40*(1), 65-80. [https://doi.org/10.1007/BF02296729](https://doi.org/10.1007/BF02296729)
- Penuel, W. R., Allen, A.-R., Henson, K., Campanella, M., Patton, R., Rademaker, K., Reed, W., Watkins, D., Wingert, K., Reiser, B., & Zivic, A. (2022). Learning Practical Design Knowledge through Co-Designing Storyline Science Curriculum Units. *Cognition and Instruction, 40*(1), 148-170. [https://doi.org/10.1080/07370008.2021.2010207](https://doi.org/10.1080/07370008.2021.2010207)

<!-- deprecated 2026-10-02: superseded by the conditional model above. Old body kept verbatim.

## Description
Anchored instruction organizes learning around a rich, shared scenario that acts as the "anchor" for inquiry, discussion, and problem solving. Instead of teaching ideas first and application later, the pattern begins with a narrative or multimedia situation containing the information, constraints, and questions learners will need to investigate. The anchor creates a common reference point that learners can revisit as they gather evidence and develop solutions.

The pattern is useful when learners need to reason through messy situations rather than complete routine exercises. It gives instructors a way to situate abstract ideas inside a concrete case while still guiding analysis and collaborative interpretation.

## Implications

### Context
#### Requirements
- **A strong anchor**: The opening scenario needs enough richness, realism, and information to support sustained inquiry.
- **Facilitated problem solving**: Learners need questions, discussion, and scaffolds that help them interpret the anchor productively.
- **A meaningful problem or decision**: The scenario should require reasoning, not only recall.
- **Opportunities to revisit evidence**: Learners should return to the anchor as they refine understanding.
#### Constraints
- **Scenario quality is decisive**: Weak or artificial anchors undermine the whole pattern.
- **Novice overload risk**: Without guidance, learners may focus on story details rather than relevant structure.
- **Preparation burden**: Good anchored instruction often depends on well-built media and facilitation materials.
- **Weak fit for narrowly procedural outcomes**: It is better for inquiry and application than for isolated routine drills.
#### Grain Size
- Lesson
- Unit

### Target Goals
- **Applied problem solving**: Using knowledge inside a meaningful situation.
- **Transfer and interpretation**: Seeing how concepts matter in context.
- **Collaborative reasoning**: Building understanding through shared analysis of the anchor.

### Target Learners
- **Learners needing context for abstraction**: Useful when abstract ideas become clearer through a concrete scenario.
- **Learners engaged in inquiry-heavy tasks**: Good fit for math, science, humanities, and professional contexts.
- **Groups working through shared evidence**: The anchor gives everyone a common object for analysis.

### Theory
#### Supporting
- Situated learning perspectives — knowledge is easier to use when learned in meaningful contexts.
- Constructivist perspectives — learners build understanding by investigating and interpreting rich situations.
- Cognitive apprenticeship perspectives — guided participation helps learners notice what matters in a complex scenario.
#### Contradicting / Qualifying
- Anchors support inquiry, but they do not remove the need for explicit clarification of key concepts.
- A compelling story is not enough if the underlying task structure is weak.

### Claims
#### Supporting
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [~S]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [~S]
#### Contradicting
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [~M]

## Design

### Sequence
1. Present a shared narrative, video, or multimedia scenario that contains a complex problem.
2. Ask learners to identify what they notice, what they need to know, and what the key questions are.
3. Guide collaborative inquiry into the scenario's data, constraints, and implications.
4. Have learners propose, justify, and refine responses.
5. Debrief the reasoning and connect it back to the target concepts.

### Elements Used
- [Anchored Instruction](../elements/anchored-instruction.md)
- [Problem Scenario](../elements/problem-scenario.md)
- [Problem Presentation](../elements/problem-presentation.md)
- [Peer Interaction](../elements/peer-interaction.md)

### Affordances
- [Problem-based Learning](../principles/problem-based-learning.md)
- [Inquiry-based Learning](../principles/inquiry-based-learning.md)
- [Authentic Audiences & Purposes](../principles/authentic-audiences-purposes.md)
- [Creating Visual Representations](../principles/dual-coding.md)

### Personalization
- Anchors can be chosen or adapted to different learner interests and backgrounds.
- Scaffolds can range from heavily guided questioning to more open inquiry.
- Teams can take different roles or analyze different facets of the same anchor.

## Impact
- Useful for increasing engagement and helping learners connect ideas to realistic contexts.
- Especially strong when the debrief makes underlying concepts explicit after inquiry.
-->

<!-- merged 2026-10-15 from patterns/storyline-science-curriculum-design ("Storyline Science Curriculum Design"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Storyline Science Curriculum Design

> **Pattern** · [All patterns](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 2 studies (1 review, 1 qualitative), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
Rather than sequencing a science unit around disciplinary topics, a storyline unit is organized around a coherent sequence of questions that students themselves raise in response to an anchoring phenomenon — the curriculum materials are written from the student's own perspective (using "we" pronouns: "we figure out," "we wonder about"), and each lesson's activities exist to answer a question the class has already asked, not to introduce content the curriculum has pre-decided is next. Standards coverage is achieved by backward design: only phenomena that require the target disciplinary ideas to explain are selected as anchors in the first place.

## Implications

### Context
#### Requirements
- An anchoring phenomenon selected specifically because explaining it requires the standards-targeted ideas (verified via a "gateway check": co-designers write the target explanation first, then discard phenomena that don't require it)
- A Driving Question Board or equivalent structure to capture and track the actual questions students raise, so the lesson sequence can be built to answer them
- Materials drafted in first-person plural ("we") from the student perspective, with explicit "punchlines" naming what students figure out and what question comes next
#### Constraints
- Building a genuine storyline (not just adding phenomenon framing to an existing topic sequence) requires substantial front-loaded design work — unpacking standards, surveying student interest, rehearsing the anchoring-phenomenon launch — that is not a lightweight addition to conventional curriculum writing
#### Grain Size
Unit (a several-week instructional unit; the source co-design process itself spanned roughly 2 years of pre-work and workshop time)

### Target Goals
- Aligning standards coverage with genuine student-generated inquiry, rather than sequencing content by disciplinary logic alone
- [Co-design tools for standards analysis, student-interest data, and launch rehearsal support balancing standards alignment with student interests](../claims/co-design-tools-support-balancing-standards-and-student-interests.md) [+M]

### Target Learners
- K-12 science students in NGSS-aligned (or similarly phenomenon-based) instructional contexts

### Theory
#### Supporting
- Phenomenon-based science education (Next Generation Science Standards) — anchoring instruction in an observable event students investigate using science and engineering practices
- Backward design — writing the target student explanation before selecting the phenomenon, to guarantee standards alignment

### Claims
#### Supporting
#### Contradicting

- (none yet linked)
- [OpenSciEd enactment faces key challenges: project fatigue, unit length and pacing, pseudoagency, and gaps in student sensemaking practices](../claims/openscied-enactment-challenges-fatigue-pacing-pseudoagency.md) [~W]

## Design

### Sequence
1. Select an anchoring phenomenon via backward design: write the target disciplinary explanation first, and discard any candidate phenomenon that doesn't require it.
2. Launch the unit with the phenomenon and capture the questions students themselves raise (e.g., via a Driving Question Board).
3. Sequence subsequent lessons to answer the class's own questions in order, rather than following a pre-set topic sequence, looping back to standards coverage as needed.
4. Draft each lesson's materials in first-person plural ("we figure out...", "we wonder about...") from the student perspective, naming an explicit "punchline" (what was figured out) and the transition to the next question.
5. Culminate the unit once the sequence of student-raised questions has been answered and the target disciplinary explanation has been collectively constructed.

### Affordances
- (none yet linked)

### Personalization
- The specific anchoring phenomenon and disciplinary content are interchangeable; what matters structurally is that lesson sequencing follows genuine student questions rather than a pre-set topic order, and that materials are written from the student's own perspective.

## Related Patterns
- (none yet linked)

## Examples
- A high school unit anchored in space exploration (selected over a student-interest-matched air-pollution phenomenon because air pollution content matched middle-school, not high-school, standards).

## Key Sources
- Penuel, W. R., Allen, A.-R., Henson, K., Campanella, M., Patton, R., Rademaker, K., Reed, W., Watkins, D., Wingert, K., Reiser, B., & Zivic, A. (2022). Learning Practical Design Knowledge through Co-Designing Storyline Science Curriculum Units. *Cognition and Instruction, 40*(1), 148-170. [https://doi.org/10.1080/07370008.2021.2010207](https://doi.org/10.1080/07370008.2021.2010207)
-->
