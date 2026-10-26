---
type: strategy
id: prompt-llm-grading-with-detailed-band-descriptors
title: Engineer LLM grading prompts with detailed, domain-specific evaluation criteria and band descriptors
description: "The study used a three-stage incremental prompt design: Prompt 1 instructed the model to simulate an IELTS examiner with zero-shot reasoning; Prompt 2 added the official grading criteria; Prompt 3 expanded on Prompt 2..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
sources:
  - id: da-wei-zhang-2024
    resource: "https://doi.org/10.1038/s41539-024-00291-1"
    title: "Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia. (2024). Evaluating large language models for criterion-based grading from agreement to consistency. npj Science of Learning 9:79. https://doi.org/10.1038/s41539-024-00291-1"
    author: "Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia"
---

# Engineer LLM grading prompts with detailed, domain-specific evaluation criteria and band descriptors

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (4 for, 1 mixed, 1 against) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The study used a three-stage incremental prompt design: Prompt 1 instructed the model to simulate an IELTS examiner with zero-shot reasoning; Prompt 2 added the official grading criteria; Prompt 3 expanded on Prompt 2 "by incorporating comprehensive band descriptors for each criterion". Prompt 3 was the only condition with significant absolute agreement and achieved the best consistency, showing that embedding detailed criteria in prompts enhances criterion-based feedback quality.

## Design Implications

### Context
#### Requirements
- Access to official, detailed evaluation criteria and band descriptors for the assessment domain
- Re-evaluation loop when outputs do not conform to the scoring guidelines, as the study re-evaluated essays until a compliant score was provided
#### Constraints
- The domain-specific information provided was limited to that available on the IELTS official website, which the authors note might neglect essential knowledge used by IELTS examiners

### Target Learners
- Educators and assessment designers integrating LLMs into grading workflows

### Target Learning Goals
- Accurate criterion-based grading and feedback aligned with established assessment standards

## Claims

- [Prompting ChatGPT 3.5 with detailed IELTS band descriptors achieves moderate interrater agreement and good interrater consistency with official examiner grades](../claims/llm-detailed-criteria-prompt-moderate-agreement-good-consistency.md) [+W]
- [Domain-specific knowledge, rather than model complexity or general abilities, limits the precision of LLM criterion-based grading](../claims/domain-specific-knowledge-limits-llm-grading-precision.md) [+W]
- [More advanced LLMs (ChatGPT 4.0, Claude 3.0 Haiku) did not improve criterion-based grading over ChatGPT 3.5 with the same prompt](../claims/advanced-llms-no-grading-improvement.md) [~W]
- [ChatGPT 3.5 grading with the best prompt was significantly lower than official IELTS examiner grades, indicating systematic bias in absolute grading](../claims/llm-grades-significantly-lower-than-examiners.md) [-W]
- [The best prompt showed excellent test-retest reliability (intrarater consistency ICC = 0.89) when rerun in ChatGPT 3.5](../claims/llm-grading-excellent-intrarater-consistency.md) [+W]
- [A teacher without IELTS-specific training showed poorer grading consistency than the best LLM prompt condition](../claims/teacher-grading-poorer-consistency-than-llm.md) [+W]

## Related Strategies

- [Provide LLM graders with the full human rubric, accepted solutions, and common-mistake penalties in the prompt (rubric-enhanced prompting)](rubric-enhanced-llm-grading-prompt.md)
- [Reserve LLM grading for short, well-structured tasks with explicit rubrics or exemplar answers, newer models, and stable API pipelines](reserve-llm-grading-for-structured-rubric-tasks.md)

## Examples
-

## Key Sources
- Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia. (2024). Evaluating large language models for criterion-based grading from agreement to consistency. npj Science of Learning 9:79. https://doi.org/10.1038/s41539-024-00291-1
