---
type: strategy
id: future-work-refine-prompts-add-context-improve-label-definitions
title: Future work should refine prompts, add past utterances for context, and use error analysis to improve label definitions
description: "The article recommends three future work strategies: (1) further refine the prompt used for GPT-4 to more effectively represent team communication tasks and clarify properties associated with each label, (2) allow pas..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: spain-2024
    resource: "https://doi.org/10.21203/rs.3.rs-4565500/v1"
    title: "Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J. (2024). Applying Large Language Models to Enhance Dialogue and Communication Analysis for Adaptive Team Training. https://doi.org/10.21203/rs.3.rs-4565500/v1"
    author: "Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J"
---

# Future work should refine prompts, add past utterances for context, and use error analysis to improve label definitions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends three future work strategies: (1) further refine the prompt used for GPT-4 to more effectively represent team communication tasks and clarify properties associated with each label, (2) allow past utterances to provide additional context, enhancing both GPT-4 and T5 model performance in classifying subsequent utterances, and (3) identify characteristics of frequently misclassified utterances based on error analysis results and use these characteristics to improve NLP models by refining label definitions to enhance label distinction and clarity. The article also recommends exploring other LLMs such as Llama 3 and FLAN-T5 and examining other fundamental dialogue analysis tasks such as information flow classification.

## Design Implications

### Context
#### Requirements
- Access to error analysis results identifying frequently misclassified utterances
- Ability to refine label definitions to enhance label distinction and clarity
#### Constraints
- 

### Target Learners
- team members in military squad training exercises

### Target Learning Goals
- team communication analysis
- adaptive team training

## Claims

- [Prompt refinements targeting inter-label confusion yield superior recall rates for challenging dialogue act labels, including Command (F1 raised to 0.75) and Other (GPT-4 recall 0.67 vs. T5 0.54).](../claims/prompt-refinements-improve-recall-challenging-dialogue-acts.md) [+W]
- [Provide-Info, Request-Info, and Other are the dialogue act labels most commonly confused by both GPT-4 and T5 classifiers.](../claims/provide-info-request-info-other-most-confused-labels.md) [+W]

## Related Strategies

- [Use iterative prompt engineering mirroring human coders' labeling processes to refine LLM classification prompts](iterative-prompt-engineering-mirroring-human-coder-refinement.md)

## Examples
-

## Key Sources
- Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J. (2024). Applying Large Language Models to Enhance Dialogue and Communication Analysis for Adaptive Team Training. https://doi.org/10.21203/rs.3.rs-4565500/v1
