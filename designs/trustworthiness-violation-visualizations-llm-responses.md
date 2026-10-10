---
type: design
id: trustworthiness-violation-visualizations-llm-responses
title: Six visualizations for tracing and comparing trustworthiness metric violations across LLM responses
description: The article co-designed six visualizations that help learning engineers trace where each trustworthiness metric was violated in an LLM response and compare relative performance across multiple responses.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: adam-coscia-2026
    resource: "https://arxiv.org/abs/2608.04006"
    title: "Adam Coscia, Sujata Duwal, Langdon Holmes, Scott Crossley, and Alex Endert. (2026). Calibrating Trustworthiness: Co-Designing Metrics and Visualizations for Evaluating LLMs in Education. https://arxiv.org/abs/2608.04006"
    author: Adam Coscia, Sujata Duwal, Langdon Holmes, Scott Crossley, and Alex Endert
---

# Six visualizations for tracing and comparing trustworthiness metric violations across LLM responses

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article co-designed six visualizations that help learning engineers trace where each trustworthiness metric was violated in an LLM response and compare relative performance across multiple responses. Key design features include "Highlighting violations in LLM response" and "Explanations for metric violations." Visualizations map each violation onto the span of the response, the learner's message, or the passage responsible, enabling raters to verify flags against the source text before acting on them.

## Design Implications

### Context
#### Requirements
- Visualizations should show which metrics each response violates and where two responses differ before a rater reads either one closely
- Each violation must be traceable to the specific text span responsible
#### Constraints
- Visualization literacy of collaborators was a design consideration, requiring simpler views that avoid complex analytical thought

### Target Learners
- learning engineers evaluating LLM responses

### Learning Goals
- calibrating expert judgment of LLM trustworthiness
- supporting A/B comparison of LLM responses

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Adam Coscia, Sujata Duwal, Langdon Holmes, Scott Crossley, and Alex Endert. (2026). Calibrating Trustworthiness: Co-Designing Metrics and Visualizations for Evaluating LLMs in Education. https://arxiv.org/abs/2608.04006
