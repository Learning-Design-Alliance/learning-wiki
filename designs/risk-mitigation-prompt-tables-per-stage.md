---
type: design
id: risk-mitigation-prompt-tables-per-stage
title: "Risk-and-mitigation task tables: each LLM-supported task pairs a baseline prompt with task-specific risks and mitigation strategies"
description: The taxonomy is instantiated as four tables (Tables 2-5), one per workflow stage, where each task row gives a definition, a model-agnostic baseline prompt, and a risk-and-mitigation column.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: laurence-dierickx-2026
    resource: "https://doi.org/10.1007/s42438-026-00690-0"
    title: "Laurence Dierickx, Fredrik Bjerknes, Andreas L. Opdahl, Carl-Gustav Lindén. (2026). A Taxonomy of LLM-Supported Tasks for Critical AI Literacy in Journalism. Postdigital Science and Education. https://doi.org/10.1007/s42438-026-00690-0"
    author: Laurence Dierickx, Fredrik Bjerknes, Andreas L. Opdahl, Carl-Gustav Lindén
---

# Risk-and-mitigation task tables: each LLM-supported task pairs a baseline prompt with task-specific risks and mitigation strategies

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 theoretical), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The taxonomy is instantiated as four tables (Tables 2-5), one per workflow stage, where each task row gives a definition, a model-agnostic baseline prompt, and a risk-and-mitigation column. The paper says the prompts and risk categories are designed to be transferable across tools and versions, and that "each task in the taxonomy is situated within a risk-based ethical framework and articulated through a baseline prompt." For example, summarisation carries the risk of missing key elements or introducing inaccuracies, mitigated by human reading of the document and cross-checking consistency using multiple models.

## Design Implications

### Context
#### Requirements
- Prompts are intentionally simple and model-agnostic so students can translate journalistic intentions into explicit instructions; recurring tasks such as generation recur across stages but with different risks per editorial object
#### Constraints
- The paper notes risks do not disappear but manifest differently depending on how a task is defined

### Target Learners
- journalism students

### Learning Goals
- structured prompting practice
- ethical risk identification and mitigation
- human oversight of AI-assisted workflows

### Claims
- [Four Stage News Workflow Organisation](../claims/four-stage-news-workflow-organisation.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Laurence Dierickx, Fredrik Bjerknes, Andreas L. Opdahl, Carl-Gustav Lindén. (2026). A Taxonomy of LLM-Supported Tasks for Critical AI Literacy in Journalism. Postdigital Science and Education. https://doi.org/10.1007/s42438-026-00690-0
