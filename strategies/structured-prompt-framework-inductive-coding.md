---
type: strategy
id: structured-prompt-framework-inductive-coding
title: Structured prompt framework for LLM-assisted inductive coding (role assignment, format specification, reasoning-based prompting)
description: "The article's prompt engineering strategy specifies that prompts should meet \"three core criteria: (1) clearly specifying the model's role, (2) defining input and output formats, and (3) incorporating reasoning -based..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: potter-2026
    resource: "https://osf.io/8j9y6/?view_only=3a21ed900475418a8c258ea595cbe53b"
    title: "Potter, A.; Serhan, Z.; Patne, N. A.; Öncel, P.; Ahmed, I.; Arner, T.; Islam, R.; Roscoe, R. D.; Allen, L. A.; Crossley, S. A.; McNamara, D. S. (2026). Human-AI Collaboration for Qualitative Analysis in Participatory Design: Refining the Writing Analytics Tool. Journal of Educational Data Mining, Volume 18, No 1. https://osf.io/8j9y6/?view_only=3a21ed900475418a8c258ea595cbe53b"
    author: Potter, A.; Serhan, Z.; Patne, N. A.; Öncel, P.; Ahmed, I.; Arner, T.; Islam, R.; Roscoe, R. D.; Allen, L. A.; Crossley, S. A.; McNamara, D. S
---

# Structured prompt framework for LLM-assisted inductive coding (role assignment, format specification, reasoning-based prompting)

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article's prompt engineering strategy specifies that prompts should meet "three core criteria: (1) clearly specifying the model's role, (2) defining input and output formats, and (3) incorporating reasoning -based strategies". Prompts distinguished open, axial, and selective coding phases, used role-based framing (instructing the model to act as a qualitative researcher), and chain-of-thought prompting to elicit rationales for each coding decision. Follow-up prompts requested clearer code definitions, additional examples, and attribution of quotes to participants, supporting auditability and researcher control over analytic content.

## Design Implications

### Context
#### Requirements
- Iterative prompt development by multiple researchers aligned to the study's research questions, and a platform permitting multi-turn prompting
#### Constraints
- Because CreateAI Chat did not support persistent system-level prompts, all role instructions had to be delivered through the initial user prompt of each session

### Target Learners
- Qualitative researchers and educational technology design teams

### Target Learning Goals
- Rigorous, transparent inductive thematic analysis of user feedback data

## Related Strategies

- [Curricular chain-of-thought prompting: extract key pedagogical elements before competency inference](curricular-chain-of-thought-prompting.md)
- [Use structured multi-stage prompts with clearly defined constructs when eliciting LLM topic labels for qualitative coding](structured-prompts-clear-construct-definitions-llm-labeling.md)

## Examples
-

## Key Sources
- Potter, A.; Serhan, Z.; Patne, N. A.; Öncel, P.; Ahmed, I.; Arner, T.; Islam, R.; Roscoe, R. D.; Allen, L. A.; Crossley, S. A.; McNamara, D. S. (2026). Human-AI Collaboration for Qualitative Analysis in Participatory Design: Refining the Writing Analytics Tool. Journal of Educational Data Mining, Volume 18, No 1. https://osf.io/8j9y6/?view_only=3a21ed900475418a8c258ea595cbe53b
