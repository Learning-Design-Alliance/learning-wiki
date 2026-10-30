---
type: strategy
id: iterative-validation-loop-gpt-feedback-systems
title: Integrate GPT models into LA-supported feedback systems with an iterative instructor-student validation loop to improve reliability
description: "The article recommends that system developers and LA researchers incorporating LLMs into LA-supported feedback systems \"devise a way to validate and update GPT models regularly to improve the reliability of the genera..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-15
sources:
  - id: dai-2024
    resource: "https://doi.org/10.1016/j.caeai.2024.100299"
    title: "Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen. (2024). Assessing the Proficiency of Large Language Models in Automatic Feedback Generation: An Evaluation Study. Computers and Education: Artificial Intelligence, 7, 100299. Preprint submitted to Elsevier. https://doi.org/10.1016/j.caeai.2024.100299"
    author: Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen
---

# Integrate GPT models into LA-supported feedback systems with an iterative instructor-student validation loop to improve reliability

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends that system developers and LA researchers incorporating LLMs into LA-supported feedback systems "devise a way to validate and update GPT models regularly to improve the reliability of the generated feedback". The proposed mechanism is "creating an iterative feedback loop where instructors and students can provide immediate responses to the feedback given by GPT models regarding its relevance to student assignment, and its reliability as a source of assessment information", enabling immediate refinements and progressive enhancement of the models.

## Design Implications

### Context
#### Requirements
- Instructors and students able to provide immediate responses to GPT-generated feedback on its relevance and reliability
#### Constraints
- The article warns GPT models may generate inaccurate or unreliable feedback that could mislead student learning, so students cannot solely rely on GPT-based tools for feedback

### Target Learners
- higher education students
- instructors of large-enrolment courses

### Target Learning Goals
- reliable assessment feedback on open-ended writing tasks
- student feedback literacy

## Claims

- [GPT models achieved high polarity agreement with instructors only for positive feedback on the Topic aspect, and could not reliably assess the other rubric aspects](../claims/gpt-polarity-agreement-low-except-topic.md) [+W]
- [GPT-4 demonstrated higher reliability of feedback than GPT-3.5, with higher F1 agreement with instructors on most assessment aspects](../claims/gpt4-higher-polarity-reliability-than-gpt35.md) [+W]
- [A human assessor agreed with the majority of GPT-generated feedback comments on assessment aspects that instructors had not commented on](../claims/human-assessor-agrees-with-gpt-feedback-on-uncommented-aspects.md) [+W]

## Related Strategies

- [Center co-design with teachers and students throughout AI tool R&D, using human-in-the-loop workflows as a primary risk mitigation](co-design-human-in-the-loop-ai-edtech-strategy.md)
- [Incorporate an expert human in the loop to support LLM coding of difficult adjacent coding categories](expert-human-in-loop-for-llm-pck-coding.md)
- [Implement AI scoring of OEQs through iterative rubric engineering with humans in the loop checking validity, reliability, reproducibility, and bias](iterative-rubric-engineering-human-in-loop-ai-scoring.md)
- [Integrate co-design and continuous feedback loops into AI evaluation processes](co-design-feedback-loops-ai-evaluation.md)
- [AI system developers should ensure human-centric design, institutional leaders should stay updated on global AI regulations, and LA experts should engage policymakers through dialogue](human-centric-ai-and-policymaker-dialogue-practices.md)
- [Human-in-the-loop instructor control as a design direction for adaptive learning systems](human-in-loop-instructor-realtime-adaptive-control.md)
- [Incorporate pre-delivery LLM-based evaluation approaches into GenAI-powered personalised SRL scaffolding systems to mitigate hallucinations](pre-delivery-llm-evaluation-mitigate-hallucinations.md)

## Examples
-

## Key Sources
- Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen. (2024). Assessing the Proficiency of Large Language Models in Automatic Feedback Generation: An Evaluation Study. Computers and Education: Artificial Intelligence, 7, 100299. Preprint submitted to Elsevier. https://doi.org/10.1016/j.caeai.2024.100299
