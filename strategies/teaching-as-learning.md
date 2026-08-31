---
type: strategy
title: Teaching as Learning
description: Learners study material in order to teach it to someone else, then actually teach it — the preparation and the explaining are the learning activity, not a service to the audience.
status: review
generated:
  by: claude/unspecified
  at: 2026-08-30
sources:
  - id: fiorella-mayer-2013
    resource: "https://doi.org/10.1016/j.cedpsych.2013.06.001"
    title: "Fiorella, L., & Mayer, R. E. (2013). The relative benefits of learning by teaching and teaching expectancy. *Contemporary Educational Psychology, 38*(4), 281–288"
    author: "Fiorella, L., & Mayer, R. E"
  - id: nestojko-2014
    resource: "https://doi.org/10.3758/s13421-014-0416-z"
    title: "Nestojko, J. F., Bui, D. C., Kornell, N., & Bjork, E. L. (2014). Expecting to teach enhances learning and organization of knowledge in free recall of text passages. *Memory & Cognition, 42*(7), 1038–1048"
    author: "Nestojko, J. F., Bui, D. C., Kornell, N., & Bjork, E. L"
  - id: roscoe-chi-2007
    resource: "https://doi.org/10.3102/0034654307309920"
    title: "Roscoe, R. D., & Chi, M. T. H. (2007). Understanding tutor learning: Knowledge-building and knowledge-telling in peer tutors' explanations and questions. *Review of Educational Research, 77*(4), 534–574"
    author: "Roscoe, R. D., & Chi, M. T. H"
  - id: topping-1998
    resource: "https://doi.org/10.3102/00346543068003249"
    title: "Topping, K. J. (1998). Peer assessment between students in colleges and universities. *Review of Educational Research, 68*(3), 249–276"
    author: "Topping, K. J"
---

# Teaching as Learning

> **Strategy** · [All strategies](index.md)

## Description
Teaching as learning assigns a learner responsibility for explaining material to someone else, and treats that responsibility as the instructional intervention. The learner studies with the knowledge that they will have to present, then delivers the explanation to a peer, a younger student, a camera, or a software agent. The gain accrues to the *teacher*, not the audience: preparing to explain forces the learner to organize the material into something transmissible, and delivering the explanation exposes every place where the organization was incomplete.

## Design Implications

The effect has two separable parts, and the design question is whether you need both. Merely *expecting* to teach changes how learners study — they organize more, recall more, and structure knowledge better than learners studying for a test on the same material [Learning By Teaching Improves Learning](../claims/learning-by-teaching-improves-learning.md) [+M]. Actually *delivering* the explanation adds further gain on top of the expectancy [Learning By Teaching Improves Mastery](../claims/learning-by-teaching-improves-mastery.md) [+M], because generating an explanation aloud without notes is both a retrieval event and a self-monitoring one [Retrieval Practice Improves Transfer](../claims/retrieval-practice-improves-transfer.md) [+S].

What determines size of benefit is what the tutor actually does while teaching. Roscoe and Chi's distinction is the operative one: tutors who engage in *knowledge-building* — reasoning aloud, integrating, repairing their own gaps — learn substantially; tutors who engage in *knowledge-telling* — summarizing and restating what they read — learn little [Learning By Teaching Improves Tutor Learning](../claims/learning-by-teaching-improves-tutor-learning.md) [+M]. Unstructured "go teach your partner" defaults to knowledge-telling, which is why structure matters more here than in most peer arrangements [Structured Peer Tutoring Outperforms Unstructured](../claims/structured-peer-tutoring-outperforms-unstructured.md) [+M].

### Context
#### Requirements
- A genuine expectation of teaching, established before study begins — announcing it afterwards recovers none of the study-phase benefit
- Delivery without notes or slides to read from, so the explanation must be generated rather than transmitted ([Articulation](../elements/articulation.md))
- Questions from the audience, or a prompt structure that forces reasoning rather than restatement ([Eliciting Student Thinking](../elements/eliciting-student-thinking.md))
- A correctness check after teaching, since a confident wrong explanation is otherwise reinforced ([Feedback](../elements/feedback.md))
- Material the learner can plausibly master to the point of explaining — the strategy needs a floor of prior knowledge [Activation Improves Learning](../claims/activation-improves-learning.md) [+M]

#### Constraints
- Without prompts that require reasoning, tutors default to summarizing, and summarizing produces little learning for the tutor [-M]
- Learners with weak grasp of the material can consolidate and then propagate misconceptions; peer explanation is least accurate exactly where it is most needed [Peer feedback accuracy depends on expertise.](../claims/peer-feedback-accuracy-depends-on-expertise.md) [-M]
- The time cost is high relative to studying, and for pure factual retention plain [retrieval practice](../claims/retrieval-practice-improves-transfer.md) achieves comparable gains far more cheaply [~M]
- Public explanation carries social risk; anxious learners may spend their preparation managing exposure rather than organizing content [-W]
- The arrangement raises an equity problem when the same learners are always cast as tutors: the tutoring role carries the learning benefit, so distributing it unevenly distributes the benefit unevenly [-M]

#### Implementation Variability
- **Teaching expectancy only** — learners study "to teach" but are then tested instead; captures the study-phase benefit at near-zero cost
- **Teach to camera** — learners record an explanation with no live audience, which removes scheduling and social cost while keeping generation
- **Peer tutoring, same age** — reciprocal pairs alternate roles so both learners get the tutor benefit ([Peer Tutoring](peer-tutoring.md))
- **Cross-age tutoring** — an older learner teaches a younger one, which raises accountability and lowers the tutor's fear of exposure ([Cross-Age Tutoring](cross-age-tutoring.md))
- **Jigsaw** — each learner masters one segment and teaches it to the group, making the teaching structurally necessary rather than exhortative ([Jigsaw](jigsaw.md))
- **Teachable agents** — learners teach a software agent that then answers questions, so errors surface as the agent's visible failures rather than the learner's

### Target Learners
- Learners with enough prior knowledge to organize the material, not merely to recite it
- Secondary and post-secondary learners in conceptually dense subjects where organization is the bottleneck
- Learners who over-rate their own understanding from re-reading; the demand to explain reliably exposes the gap
- Weaker fit for genuine novices, who lack the schema to build an explanation and fall back on paraphrase
- Weaker fit where accuracy is safety-critical and no expert check is available

### Target Learning Goals
- Conceptual understanding and knowledge organization rather than recall of isolated facts
- Ability to explain: articulating causal structure in one's own words
- Metacognitive calibration — discovering the boundary of one's own understanding [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]
- Retention and transfer, via the retrieval demand built into explaining without notes

### Instructions
1. **Announce the teaching before study starts.** Name the audience and the format. This is the step that changes how learners read, and it is free.
2. **Assign non-overlapping content.** Give each learner material the audience does not already hold, so the explanation is genuinely necessary ([Jigsaw](jigsaw.md)).
3. **Require a preparation artifact.** A one-page explanation plan, a worked example to walk through, or three questions they expect to be asked — this forces organizing rather than re-reading.
4. **Have them teach without reading aloud.** Notes may be consulted, not recited; the explanation must be generated in the moment ([Articulation](../elements/articulation.md)).
5. **Require the audience to interrogate.** Give listeners two obligatory questions — one asking why, one asking about a case not covered — so the tutor must reason past their script ([Eliciting Student Thinking](../elements/eliciting-student-thinking.md)).
6. **Check accuracy afterwards.** Review the explanations against a canonical account, publicly correcting shared errors ([Feedback](../elements/feedback.md)).
7. **Rotate the role.** Over a unit, ensure every learner teaches, since the benefit belongs to whoever is doing the explaining.

## Related Strategies
- [Peer Tutoring](peer-tutoring.md) — the institutional form of this strategy, with the tutor as the intended beneficiary [Peer Tutoring Improves Achievement](../claims/peer-tutoring-improves-achievement.md) [+S]
- [Cross-Age Tutoring](cross-age-tutoring.md) — an older learner teaches a younger one, raising accountability without raising peer exposure
- [Jigsaw](jigsaw.md) — makes teaching structurally necessary by distributing content across group members
- [Peer Instruction](peer-instruction.md) — the same explain-to-a-peer mechanism compressed into a lecture, around a concept question [Peer Discussion Improves Conceptual Understanding](../claims/peer-discussion-improves-conceptual-understanding.md) [+S]
- [Peer Feedback](peer_feedback.md) — a related arrangement where the assessor gains from evaluating, as the tutor gains from explaining [Peer Assessment Benefits Assessor](../claims/peer-assessment-benefits-assessor.md) [+M]

## Examples

**Fiorella and Mayer's teaching-expectancy experiments:** Undergraduates who studied a lesson expecting to teach it outperformed those studying for a test, and those who went on to actually deliver a videotaped explanation gained more still — separating the expectancy effect from the delivery effect.

**Nestojko et al.'s free-recall study:** Participants told they would teach a text passage recalled more of it, and recalled it in better-organized form, than participants told they would be tested — with no difference in study time.

**Jigsaw in secondary science:** Each group member becomes the expert on one mechanism, meets other experts on the same mechanism to rehearse, then returns to teach their home group — the teaching is unavoidable because nobody else has the content.

**Teachable agents (Betty's Brain):** Students teach a software agent by building a concept map; the agent then answers quiz questions using only what it was taught, so gaps in the student's model surface as the agent's public failures rather than as the student's.

## Key Sources
- Fiorella, L., & Mayer, R. E. (2013). The relative benefits of learning by teaching and teaching expectancy. *Contemporary Educational Psychology, 38*(4), 281–288. [doi:10.1016/j.cedpsych.2013.06.001](https://doi.org/10.1016/j.cedpsych.2013.06.001)
- Nestojko, J. F., Bui, D. C., Kornell, N., & Bjork, E. L. (2014). Expecting to teach enhances learning and organization of knowledge in free recall of text passages. *Memory & Cognition, 42*(7), 1038–1048. [doi:10.3758/s13421-014-0416-z](https://doi.org/10.3758/s13421-014-0416-z)
- Roscoe, R. D., & Chi, M. T. H. (2007). Understanding tutor learning: Knowledge-building and knowledge-telling in peer tutors' explanations and questions. *Review of Educational Research, 77*(4), 534–574. [doi:10.3102/0034654307309920](https://doi.org/10.3102/0034654307309920)
- Topping, K. J. (1998). Peer assessment between students in colleges and universities. *Review of Educational Research, 68*(3), 249–276. [doi:10.3102/00346543068003249](https://doi.org/10.3102/00346543068003249)
