---
type: strategy
id: question-based_elearning_design
title: Question-based eLearning Design
description: An instructional approach that replaces expository presentation with questions learners must answer, driving active information-seeking and knowledge construction.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Question-based eLearning Design

> **Strategy** · [All strategies](index.md)

## Description
Question-based eLearning design replaces the traditional expository method with an inquiry-oriented one. Instead of presenting information as statements, the course poses questions — through realistic scenarios, concept-identification examples, or complex problems — and learners gather information to answer them. The question, not the content dump, becomes the organizing unit of the learning experience, promoting active exploration and critical thinking.

## Design Implications

Questions function as prequestions and retrieval prompts that direct attention and induce processing that passive reading does not [Active learning improves exam performance over lecture alone.](../claims/active-learning-improves-exam-performance.md) [+S]. However, the benefit depends on scaffolding: unguided question-posing shades into pure discovery, which consistently underperforms guided instruction for novices [Pure discovery learning is less effective than guided instruction for novices.](../claims/expertise-reversal-effect.md) [~S]. Effective designs pair questions with feedback on answers, since unanswered or uncorrected questions leave errors intact [Feedback is most effective at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].

### Context
#### Requirements
- Well-designed questions that are answerable from the available content and matched to learner prior knowledge
- Guidance structures — hints, resource links, worked partial answers — so learners can close the gap without floundering
- Feedback or self-check opportunities so learners can verify their answers ([Assess Performance](../elements/assess-performance.md))
- Careful analysis of the audience's abilities and knowledge before setting question difficulty

#### Constraints
- Unguided inquiry questions impose heavy extraneous load on novices, who lack schemas to structure the search [Pure discovery learning is less effective than guided instruction for novices.](../claims/expertise-reversal-effect.md) [-S]
- Questions that are rhetorical or answerable without processing ("click-to-continue" questions) add interaction without learning benefit
- Requires more development time and resources than expository design; poorly targeted questions disengage rather than intrigue
- Less suitable for foundational factual fluency, where direct exposition plus retrieval practice is more efficient

#### Implementation Variability
- **Scenario-driven:** a realistic situation opens with a problem question; content is revealed as learners seek answers
- **Concept identification:** learners classify examples and non-examples by answering "which of these is…?" questions
- **Guided problem-solving:** a complex problem is decomposed into a question sequence that walks learners through a solution path
- **Reflective wrap-up:** expository content is followed by questions that force application and self-explanation

### Target Learners
- Adult learners and professionals in self-paced or collaborative settings, who have enough prior knowledge and self-regulation to sustain inquiry
- Learners with moderate prior knowledge benefit most; complete novices need substantially more question scaffolding [Pure discovery learning is less effective than guided instruction for novices.](../claims/expertise-reversal-effect.md) [~M]
- For experts, heavy question scaffolding becomes redundant and can depress performance [Guidance that helps novices can hinder more knowledgeable learners.](../claims/expertise-reversal-effect.md) [-M]

### Target Learning Goals
- Problem-solving and application objectives, where learners must locate and integrate information
- Conceptual understanding through self-explanation prompted by "why" and "how" questions [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]
- Curiosity activation and engagement, particularly for experienced learners who resist expository formats
- Less efficient for rote retention of arbitrary facts, where spaced retrieval of presented content works better

### Instructions
1. Open with a scenario or problem that poses a meaningful question and activates relevant prior knowledge ([Activation](../elements/activation.md))
2. Provide resources, hints, or partial models so learners can pursue the answer without unguided search ([Coaching](../elements/coaching.md))
3. Require learners to apply the answer — classify a case, make a decision, solve a variant ([Application](../elements/application.md))
4. Give feedback on answers, explaining why alternatives are wrong ([Assess Performance](../elements/assess-performance.md))
5. Close with a reflective question that prompts learners to articulate what they learned ([Individual Reflection](../elements/individual-reflection.md))

## Related Strategies
- [Activating Prior Knowledge](../strategies/activating-prior-knowledge.md) — prequestions serve this function by surfacing what learners already know before new content
- [Case-based Learning](../patterns/case-based-learning.md) — a pattern-level instantiation where cases carry the questions

## Related Elements
- [Activation](../elements/activation.md) — opening questions work by connecting to existing knowledge
- [Coaching](../elements/coaching.md) — the guidance layer that keeps question-driven search productive
- [Application](../elements/application.md) — questions only produce learning when answers must be used
- [Assess Performance](../elements/assess-performance.md) — feedback on answers corrects errors before they consolidate
- [Individual Reflection](../elements/individual-reflection.md) — closing questions consolidate learning through self-explanation

## Patterns That Use This Strategy
- [Case-Based Learning](../patterns/case-based-learning.md) — cases pose the driving questions
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — questioning is a core coaching method
- [Gagné's 9 Events](../patterns/gagnes-9-events-of-instruction.md) — "gain attention" and "elicit performance" events

## Tools
- Scenario and branching tools (e.g., [Twine](https://twinery.org), [Articulate Storyline](https://www.articulate.com)) for question-driven scenarios
- [H5P](https://h5p.org) question sets and interactive video with embedded questions
- [Khan Academy](https://www.khanacademy.org) — video content punctuated by questions with hints and feedback

## Examples
- **Scenario-based compliance training** (e.g., [Vyond](https://www.vyond.com)-built branching scenarios): learners answer "what would you do?" questions and see consequences unfold, rather than reading policy statements
- **Concept identification in medical eLearning:** learners view imaging cases and answer "is this presentation X or Y?" before receiving expert explanation
- **Interactive case studies in business courses:** a decision point poses a question, learners commit, then compare their reasoning against expert analysis
- **Reflective question wrap-ups** (Connie Malamed, [The eLearning Coach](https://www.theelearningcoach.com)): each module ends with questions requiring application of the content just presented

## Key Sources
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Mayer, R. E. (2004). Should there be a three-strikes rule against pure discovery learning? *American Psychologist, 59*(1), 14–19. [doi:10.1037/0003-066X.59.1.14](https://doi.org/10.1037/0003-066X.59.1.14)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Hmelo-Silver, C. E. (2004). Problem-based learning: What and how do students learn? *Educational Psychology Review, 16*(3), 235–266. [doi:10.1023/B:EDPR.0000034022.16470.f3](https://doi.org/10.1023/B:EDPR.0000034022.16470.f3)
- Chi, M. T. H., de Leeuw, N., Chiu, M.-H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science, 18*(3), 439–477. [doi:10.1207/s15516709cog1803_3](https://doi.org/10.1207/s15516709cog1803_3)
