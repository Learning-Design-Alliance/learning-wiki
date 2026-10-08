---
type: theory
title: Hybrid human-in-the-loop framework integrating topic modeling, LLM prompting, and human coding
description: The article introduces a multi-stage methodological framework for qualitative analysis at scale.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: teresa-m-ober-2026
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1008"
    title: "Teresa M. Ober, Karyssa A. Courey, Michael Flor. (2026). Integrating Topic Modeling and LLM Prompt Engineering into a Human-driven Approach to Analyze Interview Transcripts. Journal of Educational Data Mining, Volume 18, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1008"
    author: Teresa M. Ober, Karyssa A. Courey, Michael Flor
---

# Hybrid human-in-the-loop framework integrating topic modeling, LLM prompting, and human coding

> **Theory** · [All theories](index.md)
> **Evidence** · 4 claims (1 for, 2 mixed, 1 against) · 3 studies (2 design, 1 causal), `q1`–`q2` · 0 of 3 report an effect size · 4 claims rest on one study

## Description
The article introduces a multi-stage methodological framework for qualitative analysis at scale. It combines grounded human coding, semantic clustering via SentenceBERT embeddings and Affinity Propagation, LLM-assisted topic labeling with two GPT-4-based models, and iterative codebook refinement. As the abstract states, "This study presents a hybrid, human -in-the-loop methodological framework  that integrates topic modeling, LLM prompting, and human-derived codes to support rigorous qualitative analysis." Human decision-making is positioned as the theoretical anchor, with topic modeling providing stable, mathematically grounded theme identification and LLMs supporting labeling and refinement.

## Design Implications

### Context
#### Requirements
- Human expertise must review and refine LLM-generated labels and map human-derived themes onto data-derived clusters
- Prompts must include clear construct definitions and contextual framing
#### Constraints
- Topic modeling outputs are sensitive to parameter tuning and may struggle with short or ambiguous text segments
- The study did not include comparative conditions to empirically evaluate whether the hybrid approach outperforms alternatives

### Target Learners
- educational researchers analyzing qualitative interview data

### Target Learning Objectives
- scalable and interpretable thematic analysis of open-ended qualitative data

### Claims

- [A hybrid human-AI workflow using GPT-4o with retrieval-augmented generation supported efficient inductive thematic analysis while preserving researcher judgment](../claims/hybrid-gpt4o-human-inductive-thematic-analysis-workflow.md) [+W]
- [LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers](../claims/llm-inductive-coding-risks-require-human-oversight.md) [~W]
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](../claims/llm-competency-error-patterns-four-types.md) [~W]
- [The study lacked comparative conditions, so hybrid-approach improvement claims remain conceptual rather than empirically validated](../claims/no-comparative-conditions-hybrid-improvement-unvalidated.md) [-W]

## Related Theories
- 

## Examples

- [Use structured multi-stage prompts with clearly defined constructs when eliciting LLM topic labels for qualitative coding](../strategies/structured-prompts-clear-construct-definitions-llm-labeling.md)
- [Structured prompt framework for LLM-assisted inductive coding (role assignment, format specification, reasoning-based prompting)](../strategies/structured-prompt-framework-inductive-coding.md)

## Key Sources
- Teresa M. Ober, Karyssa A. Courey, Michael Flor. (2026). Integrating Topic Modeling and LLM Prompt Engineering into a Human-driven Approach to Analyze Interview Transcripts. Journal of Educational Data Mining, Volume 18, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1008
