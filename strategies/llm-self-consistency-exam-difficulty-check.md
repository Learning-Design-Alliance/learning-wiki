---
type: strategy
id: llm-self-consistency-exam-difficulty-check
title: Use bootstrapped self-consistency of LLM answers as an initial measure of exam item difficulty
description: The article proposes that organizations designing exams have ChatGPT repeatedly attempt newly developed exams and assess mean consistency across items as an initial difficulty check.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: joost-c-f-de-winter-2024
    resource: "https://doi.org/10.1007/s40593-023-00372-z"
    title: "Joost C. F. de Winter. (2024). Can ChatGPT Pass High School Exams on English Language Comprehension? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00372-z"
    author: Joost C. F. de Winter
---

# Use bootstrapped self-consistency of LLM answers as an initial measure of exam item difficulty

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article proposes that organizations designing exams have ChatGPT repeatedly attempt newly developed exams and assess mean consistency across items as an initial difficulty check. As the authors state, "by having ChatGPT repeatedly attempt newly developed exams (with a temperature setting of 1) and assessing the mean consistency level across all items, one could obtain an initial measure of exam difficulty". This builds on their finding that GPT-4's inconsistent or incorrect questions were also harder for human examinees.

## Design Implications

### Context
#### Requirements
- Access to an LLM API with an adjustable temperature parameter set to 1.0
- Newly developed exam items suitable for unambiguous scoring
#### Constraints
- The feasibility and efficacy of this approach would require further validation through additional research
- The self-consistency method did not improve answer accuracy in this study, so it serves difficulty estimation, not answering

### Target Learners
- Exam and assessment organizations
- Secondary education (VWO) assessment designers

### Target Learning Goals
- Maintaining consistent exam difficulty year on year
- Flagging items that are difficult for examinees

## Claims

- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](../claims/bootstrapping-self-consistency-flags-incorrect-answers.md) [+W]
- [Exam questions that GPT-4 answered inconsistently or incorrectly were harder for human examinees, who scored about 63–68% on them versus about 75% on the rest](../claims/gpt4-inconsistent-questions-harder-for-students.md) [+W]
- [Self-consistency did not improve GPT-4's answer accuracy on these exams, unlike in chain-of-thought tasks](../claims/self-consistency-no-accuracy-gain-reading-exams.md) [~W]

## Related Strategies

- [Reevaluate online assessment security and assessment formats in light of LLM performance on comprehension exams](reevaluate-assessment-chatgpt-integrity.md)

## Examples
-

## Key Sources
- Joost C. F. de Winter. (2024). Can ChatGPT Pass High School Exams on English Language Comprehension? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00372-z
