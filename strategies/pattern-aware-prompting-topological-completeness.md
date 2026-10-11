---
type: strategy
id: pattern-aware-prompting-topological-completeness
title: Ground LLM prompts in retrieved structural patterns rather than node labels or keyword matching
description: Pattern-aware prompt construction is a prompting strategy in which the LLM receives the partially recognized input graph together with the retrieved structural template, so reasoning focuses on abstract topology rathe...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: sun-y-2026
    resource: "https://doi.org/10.1186/s40561-026-00459-9"
    title: "Sun Y., Liao Y. & Ma X. (2026). Advancing diagram-based reasoning in AI tutoring systems: a structural approach for STEM education. Smart Learning Environments. https://doi.org/10.1186/s40561-026-00459-9"
    author: "Sun Y., Liao Y. & Ma X"
---

# Ground LLM prompts in retrieved structural patterns rather than node labels or keyword matching

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Pattern-aware prompt construction is a prompting strategy in which the LLM receives the partially recognized input graph together with the retrieved structural template, so reasoning focuses on abstract topology rather than specific symbolic entities. Unlike typical OCR+QA prompts such as asking what a node connects to without context, the article states that "our prompts are grounded in veriﬁed patterns, shifting the reasoning focus from superﬁcial label accuracy to topological completeness." This lets the model infer, for example, that a central hub should have three connections even when a node label is misread. The article reports this approach enhances robustness to OCR errors and reduces hallucinations.

## Design Implications

### Context
#### Requirements
- Requires a retrieved structural template matched to the input graph before prompt construction
- Requires the LLM to receive the input graph, uncertain-edge set, and candidate edge differences in a structured JSON format
#### Constraints
- The article reports the approach in the context of engineering diagrams abstracted to small graphs; large-scale real-time deployment would require additional engineering optimizations

### Target Learners
- Students submitting diagram-based questions in STEM tutoring systems

### Target Learning Goals
- Producing structure-aware feedback and corrections for student-uploaded engineering diagrams

## Related Strategies
- 

## Examples
-

## Key Sources
- Sun Y., Liao Y. & Ma X. (2026). Advancing diagram-based reasoning in AI tutoring systems: a structural approach for STEM education. Smart Learning Environments. https://doi.org/10.1186/s40561-026-00459-9
