---
type: strategy
id: structured-prompts-clear-construct-definitions-llm-labeling
title: Use structured multi-stage prompts with clearly defined constructs when eliciting LLM topic labels for qualitative coding
description: The article recommends grounding LLM-assisted labeling in structured prompts that define constructs clearly and contextualize them within the research task.
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

# Use structured multi-stage prompts with clearly defined constructs when eliciting LLM topic labels for qualitative coding

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends grounding LLM-assisted labeling in structured prompts that define constructs clearly and contextualize them within the research task. The authors note that "the accuracy of LLM -generated labels improves when constructs are clearly defined and contex- tualized within the prompts." Their own implementation used representative sentences and bestwords from each cluster to construct structured prompts for two GPT-4-based models, with all prompt iterations made by the research team.

## Design Implications

### Context
#### Requirements
- Construct definitions must be clearly stated within prompts
- Prompts should include representative sentences and keywords from each cluster
#### Constraints
- LLM-generated labels remain subject to variability and may reflect anchoring biases or model-specific artifacts

### Target Learners
- educational researchers
- qualitative research teams adopting AI tools

### Target Learning Goals
- accurate and interpretable LLM-assisted topic labeling

### Affordances
- [Human In The Loop Topic Modeling Llm Qualitative Framework](../theories/human-in-the-loop-topic-modeling-llm-qualitative-framework.md)

## Related Strategies

- [Structured prompt framework for LLM-assisted inductive coding (role assignment, format specification, reasoning-based prompting)](structured-prompt-framework-inductive-coding.md)
- [Match LLM temperature settings to construct characteristics when coding educational dialogue](match-llm-temperature-to-construct-characteristics.md)
- [Use LLMs to generate initial course metadata labels, shifting human taggers to a confirmatory role](llm-assisted-course-tagging-confirmatory-role.md)

## Examples
-

## Key Sources
- Teresa M. Ober, Karyssa A. Courey, Michael Flor. (2026). Integrating Topic Modeling and LLM Prompt Engineering into a Human-driven Approach to Analyze Interview Transcripts. Journal of Educational Data Mining, Volume 18, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1008
