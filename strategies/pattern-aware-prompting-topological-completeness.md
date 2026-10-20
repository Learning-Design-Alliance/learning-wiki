---
type: strategy
id: pattern-aware-prompting-topological-completeness
title: Ground LLM prompts in retrieved structural patterns rather than node labels or keyword matching
description: Pattern-aware prompt construction is a prompting strategy in which the LLM receives the partially recognized input graph together with the retrieved structural template, so reasoning focuses on abstract topology rathe...
status: review
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
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

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

## Claims

- [StructRAG achieves 89.3% question-level accuracy and 93.0% edge-level F1 on 1,650 STEM diagram questions, outperforming OCR+CV, GPT-4 graph-only, direct-image GPT-4o, and ablated variants](../claims/structrag-outperforms-baselines-stem-diagrams.md) [+M] (the full system, with pattern-aware prompting, against ablations)
- [Current AI tutoring systems misinterpret complex STEM engineering diagrams, omitting edges, misclassifying component connections, and flattening hierarchical topologies](../claims/ai-systems-misinterpret-stem-diagrams.md) [~W] (the failure it addresses)

## Related Strategies
- 

## Examples

- [StructRAG](../products/structrag.md): the diagram-reasoning system that uses this prompting

## Key Sources
- Sun Y., Liao Y. & Ma X. (2026). Advancing diagram-based reasoning in AI tutoring systems: a structural approach for STEM education. Smart Learning Environments. https://doi.org/10.1186/s40561-026-00459-9
