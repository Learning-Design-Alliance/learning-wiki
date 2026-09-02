---
type: element
id: problem-solving-tasks
title: Problem-Solving Tasks
description: Learners complete structured activities that require critical thinking and application.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Problem-Solving Tasks

> **Element** · [All elements](index.md)

## Description
Problem-solving tasks are structured activities in which learners must apply knowledge to reach a goal state that is not directly given — diagnosing a fault, designing a solution, or deciding among alternatives. Unlike routine exercises, they require learners to select and coordinate strategies, making them the primary vehicle for developing analytical reasoning and transferable skill.

## Design Implications

Well-designed problem-solving tasks sit at the right point on the guidance spectrum: enough structure to prevent unproductive search, enough openness to require genuine reasoning [Whole-task practice supports transfer better than part-task drill alone.](../claims/whole-task-performance-improves-transfer.md) [+M]. Tasks should be sequenced from simple to complex with supportive information available on demand, and followed by structured reflection so learners extract generalizable principles from the specific solution they produced.

### Context
#### Requirements
- A problem whose solution is not directly retrievable from instruction — learners must reason, not recall
- Prior instruction or resources sufficient to make the problem solvable ([Activation](activation.md) of relevant prior knowledge before the task)
- Access to feedback: expert solutions, peer comparison, or instructor coaching after attempted solutions
- A debrief or [Self-Explanation](self-explanation.md) prompt that helps learners abstract the underlying principle from their solution path

#### Constraints
- Pure discovery with minimal guidance is less effective than guided problem solving, especially for novices [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [-S] — unguided search overloads working memory and can reinforce errors
- Ill-structured problems without success criteria leave learners unable to evaluate their own solutions; provide rubrics or exemplars
- High-difficulty problems can demotivate learners who lack self-efficacy; scaffold early success before increasing challenge
- Experts gain little from structured problems and may benefit more from open or novel variants [Guidance that helps novices can hinder experts.](../claims/expertise-reversal-effect.md) [~M]

### Target Learners
- Intermediate learners who have foundational knowledge but need practice coordinating it under realistic conditions
- Novices benefit only when tasks are heavily scaffolded or preceded by worked examples [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Students in STEM, business, and applied sciences, where problems mirror professional practice

### Target Learning Goals
- Analytical reasoning: diagnosing, evaluating, and justifying solution strategies
- Application and transfer: using concepts in novel, realistic contexts [Whole-task practice supports transfer better than part-task drill alone.](../claims/whole-task-performance-improves-transfer.md) [+M]
- Metacognitive skill: planning, monitoring, and revising an approach over an extended task

### Affordances
- [Active Learning](../principles/active-learning.md) — problem-solving tasks enact this principle by requiring learners to generate and defend solutions rather than receive them, producing the retrieval and elaboration that passive formats omit
- [Cognitive Load Management](../principles/cognitive-load-management.md) — task sequencing (completion tasks, then near-transfer, then far-transfer) and on-demand hints keep intrinsic load within working-memory limits instead of dumping full complexity on learners at once
- [Collaborative Learning](../principles/collaborative-learning.md) — group problem solving exposes learners to alternative solution paths and distributes the reasoning load, provided roles and accountability are structured
- Situated Learning — embedding problems in authentic professional contexts connects the task to the conditions under which the skill will actually be used

## Related Elements
- [Case-Based Learning](case-based-learning.md) — a problem-solving task anchored in a rich, realistic case narrative
- [Case Studies](case-studies.md) — published cases that supply the problem context and constraints
- [Coaching](coaching.md) — the ongoing feedback mechanism that keeps problem solving productive rather than flailing
- [Collaboration](collaboration.md) — the social structure that turns individual problem solving into comparative reasoning

## Patterns That Use This Element
- Problem-Based Learning — the problem *is* the curriculum; tasks drive all content acquisition
- Goal-Based Scenarios — simulated environments where learners pursue a goal and the system responds to their problem-solving moves
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — the exploration phase, where learners tackle problems with decreasing support

## Examples

**Problem-based medical curricula (e.g., [Maastricht University](https://www.maastrichtuniversity.nl))** — Small groups analyze authentic patient cases, identify learning needs, and return with solutions; the case is the problem-solving task.

**[PhET Interactive Simulations](https://phet.colorado.edu)** — Open-ended physics simulations framed as challenge prompts (e.g., build a circuit that meets constraints), followed by concept-check questions.

**[Harvard Business School case method](https://www.hbs.edu/mba/academic-experience/Pages/the-hbs-case-method.aspx)** — Learners must decide on a course of action in an ambiguous business situation and defend it in class discussion.

**[Code.org CS Discoveries](https://code.org/educate/curriculum/cs-discoveries)** — Structured programming puzzles with progressive difficulty and hint scaffolds, moving from guided to open-ended project tasks.

## Key Sources
- Sweller, J., Kirschner, P. A., & Clark, R. E. (2007). Why minimally guided teaching techniques do not work: A reply to commentaries. *Educational Psychologist, 42*(2), 115–121. [doi:10.1080/00461520701263426](https://doi.org/10.1080/00461520701263426)
- Hmelo-Silver, C. E. (2004). Problem-based learning: What and how do students learn? *Educational Psychology Review, 16*(3), 235–266. [doi:10.1023/B:EDPR.0000034022.16470.f3](https://doi.org/10.1023/B:EDPR.0000034022.16470.f3)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)
- Jonassen, D. H. (2000). Toward a design theory of problem solving. *Educational Technology Research and Development, 48*(4), 63–85. [doi:10.1007/BF02300500](https://doi.org/10.1007/BF02300500)