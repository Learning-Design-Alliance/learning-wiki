---
type: strategy
id: include-supplemental-context-in-scoring-inputs
title: Include supplemental response context in model inputs when human raters used it during scoring
description: When human raters score a target response with access to supplemental items (multiple choice, drag-and-drop, or text), the scoring model input should be modified to include that context.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: morris-2025
    resource: "https://doi.org/10.1007/s40593-024-00418-w"
    title: "Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w"
    author: "Morris, W., Holmes, L., Choi, J. S., & Crossley, S"
---

# Include supplemental response context in model inputs when human raters used it during scoring

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
When human raters score a target response with access to supplemental items (multiple choice, drag-and-drop, or text), the scoring model input should be modified to include that context. The article constructs modified inputs by prepending labeled supplemental content, using a Likert-style textual representation of scoring confidence for ambiguous responses.

## Design Implications

### Context
#### Requirements
- Documentation of which supplemental response types influenced human scoring for each item
#### Constraints
- Human scoring of supplemental responses may itself be inconsistent, as with ITEM 4 where the response "1:2" was equally likely to be scored correct or incorrect

### Target Learners
- K-12 students taking standardized math assessments

### Target Learning Goals
- Accurate automated scoring of multi-step constructed response math items

## Claims

- [Including supplemental response context in modified inputs was necessary because human raters scored target responses with access to those responses](../claims/supplemental-response-context-modified-inputs.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w
