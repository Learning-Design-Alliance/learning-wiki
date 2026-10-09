---
type: strategy
id: question-generation
aliases: [question_generation]
title: Question Generation
description: Learners formulate their own questions about material — before, during, or after instruction — to activate prior knowledge, direct attention, and deepen processing.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Question Generation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 unmarked) · 2 studies (2 quant-synthesis), `q3` · 1 of 2 report an effect size

## Description
Question generation asks learners to author questions about the material they are studying rather than only answering questions posed to them. It can occur before instruction (generating curiosity questions), during reading or viewing (self-questioning), or after instruction (comprehension-monitoring and elaborative questions). The strategy works because composing a question forces learners to identify the structure of the content, detect gaps in their understanding, and rephrase ideas in their own terms.

## Design Implications

Generating questions is a form of generative processing: learners must select core ideas and construct relationships among them, which produces better retention and comprehension than re-reading [Self-questioning functions as a form of practice testing, one of the highest-utility learning techniques.](https://doi.org/10.1177/1529100612453266) [+S]. The quality of learner-generated questions is highly trainable — teaching question stems (e.g., "How are X and Y alike?", "What would happen if…?") reliably raises both question quality and learning outcomes [Teaching students how to question and explain improves knowledge construction.](https://doi.org/10.3102/00028312031002338) [+S]. Untrained learners tend to generate shallow, fact-level questions, so scaffolding the *kind* of question matters as much as the act of asking.

### Context
#### Requirements
- Explicit training in question types and stems, especially for novices ([Coaching](../elements/coaching.md) with worked models of good questions)
- A task structure that requires learners to answer their own questions or exchange them with peers — questions asked but never pursued yield little benefit
- Time and norms that make asking questions safe and expected ([Class Discussion](../elements/class-discussion.md) norms, low-stakes framing)
- Source material rich enough to support meaningful questions (a text, case, dataset, or problem)
- Question stems or taxonomies (e.g., Bloom-aligned, "why/how" prompts) when learners are new to the activity

#### Constraints
- Without training, learners generate predominantly literal, text-recall questions that add little beyond re-reading [Intervention studies show gains depend on training in question type, not merely asking.](https://doi.org/10.3102/00346543066002181) [~S]
- Learners with low prior knowledge may lack the schema to ask anything beyond surface questions; front-loading content ([Activation](../elements/activation.md)) is often needed first
- Question generation adds time and working-memory load during reading; for novices handling dense material, it can compete with comprehension itself ([Cognitive Load Management](../principles/cognitive-load-management.md)) [~M]
- Untrained learners default to shallow, literal questions copied from the text surface [-M] — without stems or modeling, generation produces little benefit
- Learners with low prior knowledge generate fewer and weaker questions because they cannot identify what is central [~M]; front-loading content or [Activating Prior Knowledge](../strategies/activating-prior-knowledge.md) helps
- Generation adds working-memory load during reading; for novices with dense material, answering instructor questions first, then generating, works better than generating cold [~M]

#### Implementation Variability
- **Pre-questions**: learners pose questions before a text or lecture, orienting attention toward gaps
- **Self-questioning during reading**: embedded prompts at section boundaries ("What question does this section answer?")
- **Peer questioning**: students exchange questions in pairs or reciprocal-teaching roles; answering a peer's question resembles the [Learning by Teaching](../claims/learning-by-teaching-improves-tutor-learning.md) effect [+M]
- **Question stems and prompts**: sentence frames or a "question ladder" (literal → inferential → elaborative) scaffold quality upward
- **System-prompted questioning**: intelligent tutoring systems such as AutoTutor model deep-reasoning questions and prompt learners to produce them
- **Pre-questions:** learners pose questions before reading to set reading goals and activate schema
- **During-reading self-questioning:** learners pause at intervals to ask and answer their own questions
- **Reciprocal formats:** pairs or small groups exchange and answer each other's questions, adding accountability
- **Question stems:** sentence frames ("What would happen if…?", "How does X relate to Y?") scaffold question quality until learners internalize the forms

### Target Learners
- Elementary through adult learners; effects are documented across age bands but require age-appropriate stem training [Review of 38 intervention studies finds consistent gains when question-asking is explicitly taught.](https://doi.org/10.3102/00346543066002181) [+S]
- Struggling readers and low-achieving students benefit substantially when taught elaborative question stems [Trained questioning and explaining improved comprehension for children across achievement levels.](https://doi.org/10.3102/00028312031002338) [+S]
- Less effective for complete novices in a domain, who cannot yet distinguish central from peripheral content [~M]
- Elementary through adult learners; effects are documented across age bands but require explicit training for all [Rosenshine et al.'s review of question-generation training.](https://doi.org/10.3102/00346543066002181) [+S]
- Struggling readers and novices benefit most when stems and modeling are provided [~M]
- Advanced learners benefit from open-ended generation aimed at identifying gaps and framing inquiry, less from stem-driven formats

### Target Learning Goals
- Reading comprehension and text understanding
- Conceptual integration: "how/why" and comparison questions push beyond recall
- Metacognitive monitoring: question generation doubles as a self-assessment of what one does and does not understand [Self-questioning serves as retrieval practice and monitoring.](https://doi.org/10.1177/1529100612453266) [+S]
- Conceptual understanding through explanation-eliciting questions [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]
- Metacognitive monitoring: noticing what one does not yet understand
- Inquiry skills: learning to formulate researchable or discussable questions

### Instructions
1. Model question generation: read a short passage aloud and think aloud while composing a literal, an inferential, and an elaborative question ([Cognitive Apprenticeship](../elements/cognitive-apprenticeship.md) modeling move).
2. Provide question stems matched to the learning goal (e.g., "What is the difference between…?", "How does X relate to Y?").
3. Have learners generate 2–3 questions individually or in pairs before or during the material.
4. Require learners to answer their own or a partner's questions — closing the loop is what converts asking into learning.
5. Gradually fade the stems as learners internalize the question types ([Fading](../elements/fading.md)).

## Related Strategies

- Reciprocal Teaching — pairs question generation with summarizing, clarifying, and predicting in a role-exchange format
- Self-Explanation — a sibling generative activity; explaining aloud produces similar elaborative processing but does not train the questioning skill itself
- Retrieval Practice — learner-generated questions can serve as self-made retrieval cues for later practice
- [Directly teach students when, why, and how to elaborate on new information](directly-teach-elaborative-processing-strategies.md)
- [Activating Prior Knowledge](../strategies/activating-prior-knowledge.md) — pre-questions serve the same schema-activation function from the learner's side
- [Self-Explanation](../elements/self-explanation.md) — answering one's own generated "why" questions is self-explanation in disguise

## Examples
- **Reciprocal Teaching (Palincsar & Brown)** — small reading groups rotate a "questioner" role; students generate questions about a passage before discussing it, with teacher coaching on question quality.
- **AutoTutor (Graesser et al.)** — an intelligent tutoring system that prompts students to answer deep-reasoning questions and models the questions experts would ask, improving conceptual physics and computer literacy learning.
- **Question Formulation Technique (Right Question Institute)** — a structured protocol in which students produce, refine, and prioritize their own questions about a prompt (https://rightquestion.org).
- **AP/IB exam preparation** — students write practice exam questions for each unit, then exchange and answer them; authoring questions in the exam's format doubles as retrieval practice.
- **Reciprocal Teaching** (Palincsar & Brown, 1984) — small groups take turns generating questions about a passage alongside summarizing, clarifying, and predicting; question generation is one of four trained strategies.
- **Question-Answer Relationships (QAR)** — students learn to classify and generate questions by source (right-there vs. inference), improving both question quality and answering.
- **Case-based courses** — before discussing a case, students submit discussion questions, which the instructor uses to seed [Case-Based Learning](../patterns/case-based-learning.md) sessions.

## Key Sources
- King, A. (1994). Guiding knowledge construction in the classroom: Effects of teaching children how to question and how to explain. *American Educational Research Journal, 31*(2), 338–368. [doi:10.3102/00028312031002338](https://doi.org/10.3102/00028312031002338)
- Rosenshine, B., Meister, C., & Chapman, S. (1996). Teaching students to generate questions: A review of the intervention studies. *Review of Educational Research, 66*(2), 181–221. [doi:10.3102/00346543066002181](https://doi.org/10.3102/00346543066002181)
- Graesser, A. C., & Person, N. K. (1994). Question asking during tutoring. *American Educational Research Journal, 31*(1), 104–137. [doi:10.3102/00028312031001104](https://doi.org/10.3102/00028312031001104)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Palincsar, A. S., & Brown, A. L. (1984). Reciprocal teaching of comprehension-fostering and comprehension-monitoring activities. *Cognition and Instruction, 1*(2), 117–175. [doi:10.1207/s1532690xci0102_1](https://doi.org/10.1207/s1532690xci0102_1)
- Chi, M. T. H., de Leeuw, N., Chiu, M.-H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science, 18*(3), 439–477. [doi:10.1207/s15516709cog1803_3](https://doi.org/10.1207/s15516709cog1803_3)

<!-- merged 2026-10-09 from strategies/question_generation ("Question Generation"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Question Generation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 4 studies (2 quant-synthesis, 1 causal, 1 associational), `q2`–`q4` · 1 of 4 report an effect size

## Description
Question generation asks learners to formulate their own questions about texts, problems, or topics rather than only answering questions posed to them. It can be structured (question stems, prompt cards, assigned roles) or open-ended, and typically precedes or accompanies reading, discussion, or problem solving. The act of composing a question forces learners to identify key concepts, detect gaps in understanding, and rephrase content in their own words.

## Design Implications

Generating questions is a form of generative processing: learners must select main ideas and organize them into a coherent structure before a question can be formed, which produces deeper encoding than answering alone [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]. Training in question generation reliably improves comprehension and question-answering performance, especially when learners are taught specific question types rather than simply told to "ask questions" [Rosenshine et al.'s review of question-generation training.](https://doi.org/10.3102/00346543066002181) [+S]. The quality of learning depends on question depth: "why" and "how" questions elicit explanation-based processing, while "what" and "who" questions elicit retrieval only.

### Context
#### Requirements
- Source material rich enough to support meaningful questions (a text, case, dataset, or problem)
- Question stems or taxonomies (e.g., Bloom-aligned, "why/how" prompts) when learners are new to the activity
- A mechanism for learners to pursue or exchange their questions — peer answering, [Class Discussion](../elements/class-discussion.md), or instructor triage

#### Constraints
- Untrained learners default to shallow, literal questions copied from the text surface [-M] — without stems or modeling, generation produces little benefit
- Learners with low prior knowledge generate fewer and weaker questions because they cannot identify what is central [~M]; front-loading content or [Activating Prior Knowledge](../strategies/activating-prior-knowledge.md) helps
- Generation adds working-memory load during reading; for novices with dense material, answering instructor questions first, then generating, works better than generating cold [~M]

#### Implementation Variability
- **Pre-questions:** learners pose questions before reading to set reading goals and activate schema
- **During-reading self-questioning:** learners pause at intervals to ask and answer their own questions
- **Reciprocal formats:** pairs or small groups exchange and answer each other's questions, adding accountability
- **Question stems:** sentence frames ("What would happen if…?", "How does X relate to Y?") scaffold question quality until learners internalize the forms

### Target Learners
- Elementary through adult learners; effects are documented across age bands but require explicit training for all [Rosenshine et al.'s review of question-generation training.](https://doi.org/10.3102/00346543066002181) [+S]
- Struggling readers and novices benefit most when stems and modeling are provided [~M]
- Advanced learners benefit from open-ended generation aimed at identifying gaps and framing inquiry, less from stem-driven formats

### Target Learning Goals
- Reading comprehension and text understanding
- Conceptual understanding through explanation-eliciting questions [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]
- Metacognitive monitoring: noticing what one does not yet understand
- Inquiry skills: learning to formulate researchable or discussable questions

### Instructions
1. Model question generation on a short sample, thinking aloud about why a question is worth asking ([Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) modeling phase).
2. Provide 3–5 question stems matched to the learning goal (e.g., causal, comparative, application questions).
3. Have learners generate 2–3 questions individually before or during engagement with the material.
4. Pair learners to exchange and answer questions, escalating to whole-group discussion of the strongest questions ([Class Discussion](../elements/class-discussion.md)).
5. Fade the stems over successive sessions as learners internalize question forms.

## Related Strategies
- [Activating Prior Knowledge](../strategies/activating-prior-knowledge.md) — pre-questions serve the same schema-activation function from the learner's side
- [Self-Explanation](../elements/self-explanation.md) — answering one's own generated "why" questions is self-explanation in disguise

## Examples
- **Reciprocal Teaching** (Palincsar & Brown, 1984) — small groups take turns generating questions about a passage alongside summarizing, clarifying, and predicting; question generation is one of four trained strategies.
- **Question-Answer Relationships (QAR)** — students learn to classify and generate questions by source (right-there vs. inference), improving both question quality and answering.
- **Case-based courses** — before discussing a case, students submit discussion questions, which the instructor uses to seed [Case-Based Learning](../patterns/case-based-learning.md) sessions.

## Key Sources
- Palincsar, A. S., & Brown, A. L. (1984). Reciprocal teaching of comprehension-fostering and comprehension-monitoring activities. *Cognition and Instruction, 1*(2), 117–175. [doi:10.1207/s1532690xci0102_1](https://doi.org/10.1207/s1532690xci0102_1)
- Rosenshine, B., Meister, C., & Chapman, S. (1996). Teaching students to generate questions: A review of the intervention studies. *Review of Educational Research, 66*(2), 181–221. [doi:10.3102/00346543066002181](https://doi.org/10.3102/00346543066002181)
- King, A. (1994). Guiding knowledge construction in the classroom: Effects of teaching children how to question and how to explain. *American Educational Research Journal, 31*(2), 338–368. [doi:10.3102/00028312031002338](https://doi.org/10.3102/00028312031002338)
- Chi, M. T. H., de Leeuw, N., Chiu, M.-H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science, 18*(3), 439–477. [doi:10.1207/s15516709cog1803_3](https://doi.org/10.1207/s15516709cog1803_3)
-->
