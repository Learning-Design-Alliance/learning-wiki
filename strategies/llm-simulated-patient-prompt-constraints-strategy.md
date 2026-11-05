---
type: strategy
id: llm-simulated-patient-prompt-constraints-strategy
title: Configure the LLM simulated patient with behavioral constraints and standardized scripts to ensure consistency
description: "The article specifies implementable controls: temperature set at 0.7 and top-p fixed at 0.9, the model not fine-tuned, and system-prompt rules that the model was \"restricted from providing medical advice or deviating..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
sources:
  - id: gao-lingling-2026
    resource: "https://doi.org/10.1186/s12909-026-09219-2"
    title: "Gao Lingling, Zhang Li, Zhang Yanxin, Wu Min, Xu Jianbo, Lu Dan. (2026). Utilizing generative artificial intelligence to create simulated patient for history taking in gynecology. BMC Medical Education. https://doi.org/10.1186/s12909-026-09219-2"
    author: Gao Lingling, Zhang Li, Zhang Yanxin, Wu Min, Xu Jianbo, Lu Dan
---

# Configure the LLM simulated patient with behavioral constraints and standardized scripts to ensure consistency

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article specifies implementable controls: temperature set at 0.7 and top-p fixed at 0.9, the model not fine-tuned, and system-prompt rules that the model was "restricted from providing medical advice or deviating from its assigned patient role", instructed to use lay language, and withheld diagnostic clues unless elicited through appropriate student questioning. Case scripts were preloaded before each session to standardize the educational challenge.

## Design Implications

### Context
#### Requirements
- Predefined technical parameters and structured prompt controls
- Case scripts calibrated identically to any human standardized-patient comparison condition
#### Constraints
- Text interface lacks non-verbal clinical cues

### Target Learners
- fourth-year medical students

### Target Learning Goals
- gynecological history taking

### Affordances
- [Llm Simulated Patient History Taking Model](../designs/llm-simulated-patient-history-taking-model.md)

## Claims

- [Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits](../claims/prompting-limited-uneven-proficiency-control-writing-simulation.md) [+W]

## Related Strategies

- [Development strategies targeting AI virtual patient limitations: expert-reviewed content, iterative prompt engineering, behavioral rules, few-shot prompting, and conversational memory](ai-virtual-patient-mitigation-strategies.md)
- [Gate sensitive simulated-patient content behind an accumulated-skill threshold with constraint-first prompting](avp-content-gating-strategy.md)
- [Match LLM temperature settings to construct characteristics when coding educational dialogue](match-llm-temperature-to-construct-characteristics.md)
- [Use expert-reviewed, prompt-standardized LLM-generated scenarios as supplementary materials in simulation-based learning](llm-scenarios-supplementary-materials-strategy.md)

## Examples
-

## Key Sources
- Gao Lingling, Zhang Li, Zhang Yanxin, Wu Min, Xu Jianbo, Lu Dan. (2026). Utilizing generative artificial intelligence to create simulated patient for history taking in gynecology. BMC Medical Education. https://doi.org/10.1186/s12909-026-09219-2
