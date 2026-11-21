---
type: strategy
id: active-scaffolding-instead-of-llm-complete-solutions
title: Replace complete AI-generated solutions with active-learning scaffolding when students request help during programming practice
description: When a struggling student requests help in an AI-supported programming environment, deliver an active learning activity such as a personalized Parsons puzzle rather than a passive textual answer.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: xinying-hou-2025
    resource: "https://doi.org/10.1145/3641555.3705227"
    title: "Xinying Hou, Zihan Wu, Xu Wang, and Barbara J. Ericson. (2025). Personalized Parsons Puzzles as Scaffolding Enhance Practice Engagement Over Just Showing LLM-Powered Solutions. Proceedings of the 56th ACM Technical Symposium on Computer Science Education V. 2 (SIGCSE TS 2025). https://doi.org/10.1145/3641555.3705227"
    author: Xinying Hou, Zihan Wu, Xu Wang, and Barbara J. Ericson
---

# Replace complete AI-generated solutions with active-learning scaffolding when students request help during programming practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (3 for, 2 mixed) · 2 studies (2 causal), `q2`–`q3` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
When a struggling student requests help in an AI-supported programming environment, deliver an active learning activity such as a personalized Parsons puzzle rather than a passive textual answer. The article reports that "providing students with an active learning activity when requested scaffolding instead of a passive textual answer" led students to engage longer and invest more effort. The authors also plan an optimized support trigger, since help can currently be requested before any code is written.

## Design Implications

### Context
#### Requirements
- An online practice system with a Help button and LLM-generated personalized scaffolding
- Practice problems whose solutions can be decomposed into draggable code blocks
#### Constraints
- Some students perceived the puzzles as too much support and preferred subtle hints; others wanted more guidance on block arrangement

### Target Learners
- novice programmers in introductory courses

### Target Learning Goals
- engaging with and persisting in write-code practice rather than copying AI answers

## Claims

- [Some students given complete LLM-generated solutions copied and submitted answers within minutes without engaging with the practice](../claims/complete-solution-students-copy-submit-quickly.md) [+W]
- [Student perceptions of both puzzle scaffolding and complete solutions were mixed, revealing a trade-off in when to provide what types of support](../claims/mixed-perceptions-support-type-tradeoff.md) [~W]
- [Novice programmers given personalized Parsons puzzle scaffolding on help requests spend significantly longer practicing write-code problems than those given complete LLM-generated solutions](../claims/parsons-scaffolding-longer-practice-time-than-complete-solutions.md) [+W]
- [Students applied more scaffolded practice elements independently on the posttest after using CodeTailor than after receiving an AI-generated solution](../claims/codetailor-higher-scaffolding-apply-rate.md) [+M]
- [Posttest programming scores did not differ significantly between CodeTailor support and receiving an AI-generated solution](../claims/codetailor-posttest-performance-null.md) [~M]

## Related Strategies

- [Design AI tutoring behaviors that withhold solutions, prompt recall, and ask critical questions](withhold-answers-prompt-recall-ask-questions.md)
- [Design AI learning assistants to make the implications of AI use visible rather than restricting assistance](make-ai-use-implications-visible-design-strategy.md)
- [Provide an optional AI-usage prompt template that requests step-by-step method guidance instead of finished code](ai-usage-guidance-prompt-template.md)

## Examples
-

## Key Sources
- Xinying Hou, Zihan Wu, Xu Wang, and Barbara J. Ericson. (2025). Personalized Parsons Puzzles as Scaffolding Enhance Practice Engagement Over Just Showing LLM-Powered Solutions. Proceedings of the 56th ACM Technical Symposium on Computer Science Education V. 2 (SIGCSE TS 2025). https://doi.org/10.1145/3641555.3705227
