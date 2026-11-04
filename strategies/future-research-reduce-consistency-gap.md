---
type: strategy
id: future-research-reduce-consistency-gap
title: Future research directions for reducing the LLM consistency gap on multistep clinical cases
description: "The authors outline methodological directions for future work: improving prompting strategies, including explicitly preserving conversation history across questions and evaluating sequential prompting strategies such..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
sources:
  - id: cha-j-2026
    resource: "https://doi.org/10.2196/95342"
    title: "Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342"
    author: Cha J, Zhao Y, Zong H
---

# Future research directions for reducing the LLM consistency gap on multistep clinical cases

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q3` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The authors outline methodological directions for future work: improving prompting strategies, including explicitly preserving conversation history across questions and evaluating sequential prompting strategies such as step-by-step prompts; extending evaluations to medical images and clinical records such as radiology images and narrative medical notes; and training open-source LLMs on well-curated clinical case data with task-specific training focused on clinical workflows to build specialized medical systems that perform more reliably than general-purpose models.

## Design Implications

### Context
#### Requirements
- Future evaluations should include medical images and clinical records to better reflect actual clinical settings
#### Constraints
- The current evaluation was limited to text-based questions and conducted only in Chinese

### Target Learners
- medical AI researchers
- medical education researchers

### Target Learning Goals
- improving LLM reliability on multistep clinical tasks

## Claims

- [The consistency gap increases with case complexity, though the 4-question subgroup contained only 7 cases](../claims/case-complexity-increases-consistency-gap.md) [+W]
- [LLMs with high question-level accuracy on medical licensing exam cases show substantially lower case-level accuracy, with consistency gaps of 10% to 17.9%](../claims/llm-consistency-gap-question-vs-case-level.md) [+W]
- [Scaling Qwen2.5 from 3B to 32B parameters improved both metrics and reduced the consistency gap by approximately 50%](../claims/model-scaling-reduces-consistency-gap.md) [+W]

## Related Strategies

- [Build infrastructure-level mechanisms to monitor, benchmark, and control LLM response behavior across model transitions in conversation-based assessment](infrastructure-mechanisms-for-llm-response-consistency.md)
- [Caution: LLMs need consistency and accuracy improvements before large-scale adoption for clinical scoring](llm-consistency-caution-clinical-scoring.md)

## Examples
-

## Key Sources
- Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342
