---
type: strategy
id: llm-consistency-caution-clinical-scoring
title: "Caution: LLMs need consistency and accuracy improvements before large-scale adoption for clinical scoring"
description: "The article concludes that although LLMs can automate transcript scoring, \"more work is needed to improve their consistency and accuracy.\" It recommends future studies compare closed-source and open-source LLMs, since..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
sources:
  - id: dhillon-ik-2026
    resource: "https://doi.org/10.2196/83376"
    title: "Dhillon IK, Lee GKY, Hu S. (2026). Evaluating the Pediatric Behavior Guidance of Students Based on Actual Clinical Transcripts Scored by Faculty and Large Language Models: Pilot Comparative Study. JMIR Medical Education. https://doi.org/10.2196/83376"
    author: Dhillon IK, Lee GKY, Hu S
---

# Caution: LLMs need consistency and accuracy improvements before large-scale adoption for clinical scoring

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (1 for, 2 against) · 2 studies (1 associational, 1 theoretical), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The article concludes that although LLMs can automate transcript scoring, "more work is needed to improve their consistency and accuracy." It recommends future studies compare closed-source and open-source LLMs, since open-source models can be fine-tuned for informal clinical language, and cautions that prompt engineering per encounter makes LLMs impractical at scale.

## Design Implications

### Context
#### Requirements
- Good rubric and prompt design
- Further LLM development before large-scale adoption
#### Constraints
- Closed-source LLMs showed low consistency across repeated runs
- Prompt refinement effects are lost when starting a new chat

### Target Learners
- final-year dental students

### Target Learning Goals
- automated scoring of clinical performance

## Claims

- [ChatGPT versions were inconsistent, matching scores in all 3 runs for only 18% and 10% of encounters.](../claims/llm-inconsistent-across-runs.md) [-W]
- [ChatGPT LLM scores showed only moderate agreement with human transcript scores.](../claims/llm-moderate-agreement-human-scores.md) [-W]
- [LLM-as-judge automated evaluation can achieve human-level agreement when carefully validated](../claims/llm-as-judge-human-level-agreement-with-validation.md) [+W]

## Related Strategies

- [Future research directions for reducing the LLM consistency gap on multistep clinical cases](future-research-reduce-consistency-gap.md)
- [Use clinical transcripts as a time-saving route to formative feedback on clinical performance](transcript-based-formative-feedback-strategy.md)

## Examples
-

## Key Sources
- Dhillon IK, Lee GKY, Hu S. (2026). Evaluating the Pediatric Behavior Guidance of Students Based on Actual Clinical Transcripts Scored by Faculty and Large Language Models: Pilot Comparative Study. JMIR Medical Education. https://doi.org/10.2196/83376
