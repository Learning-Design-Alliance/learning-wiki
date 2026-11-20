---
type: strategy
id: llm-feedback-safety-safeguards-strategy
title: Safeguard LLM feedback for students by stripping identity information, limiting interaction rounds, and forcing validated JSON output
description: This strategy packages the safeguards the authors put in place to avoid perpetuating bias when deploying LLM-generated text to students.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: juliette-woodrow-2024
    resource: "https://doi.org/10.1145/3626252.3630773"
    title: "Juliette Woodrow, Ali Malik, and Chris Piech. 2024. AI Teaches the Art of Elegant Coding: Timely, Fair, and Helpful Style Feedback in a Global Course. In Proceedings of the 55th ACM Technical Symposium on Computer Science Education V. 1 (SIGCSE 2024). https://doi.org/10.1145/3626252.3630773"
    author: Juliette Woodrow, Ali Malik, and Chris Piech
---

# Safeguard LLM feedback for students by stripping identity information, limiting interaction rounds, and forcing validated JSON output

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
This strategy packages the safeguards the authors put in place to avoid perpetuating bias when deploying LLM-generated text to students. As they write, "We shared only the text of each student's code, devoid of any information about the student or their course progress." Students were limited to one round of LLM interaction at a time, interacted solely via a comprehensive parsing and validation system, and the LLM was set to deliver responses in JSON form to avoid unsupervised plain text. Safety was evaluated through checks of thousands of responses and sentiment analysis across genders.

## Design Implications

### Context
#### Requirements
- A parsing and validation system through which all student-LLM interactions pass, and JSON-schema-constrained LLM responses.
#### Constraints
- The authors state future research should conduct a more thorough investigation into potential biases of LLM-based tools than this report accomplished.

### Target Learners
- CS1 students in large-scale online courses

### Target Learning Goals
- safe and equitable delivery of automated formative feedback

## Claims

- [The LLM-generated style feedback showed no differential feedback by gender in sentiment analysis and manual checks, and no inappropriate or demographically biased content was found](../claims/llm-style-feedback-no-gender-bias.md) [+W]

## Related Strategies

- [Deploy agentic AI in education with transparency about agentic decisions, human oversight and institutional responsibility](responsible-deployment-transparency-human-oversight-agentic-ai.md)
- [Establish ethical safeguards and debrief participants when piloting LLM tools with learners](ethical-safeguards-debrief-llm-pilots.md)
- [Adopt ethical safeguards and pedagogically grounded frameworks when deploying GenAI assessment tools](ethical-safeguards-pedagogical-frameworks-genai-deployment.md)
- [Address chatbot-induced challenges computationally and pedagogically, including tone safeguards, bias reduction, and user-side prompt engineering](llamalo-challenge-safeguards-strategy.md)
- [Improve LLM feedback quality via JSON-schema prompts with hidden scoring keys and preprocessing code into structured dictionaries](llm-prompt-schema-and-preprocessing-strategy.md)

## Examples
-

## Key Sources
- Juliette Woodrow, Ali Malik, and Chris Piech. 2024. AI Teaches the Art of Elegant Coding: Timely, Fair, and Helpful Style Feedback in a Global Course. In Proceedings of the 55th ACM Technical Symposium on Computer Science Education V. 1 (SIGCSE 2024). https://doi.org/10.1145/3626252.3630773
