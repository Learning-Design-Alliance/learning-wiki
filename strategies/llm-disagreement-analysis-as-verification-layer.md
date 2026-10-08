---
type: strategy
id: llm-disagreement-analysis-as-verification-layer
title: Use LLM-based de-identification as an additional verification layer to catch human redaction mistakes
description: The article recommends running an LLM redaction pass alongside human de-identification and analyzing the disagreements between the two, so that human omissions can be caught and corrected.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: s-singhal-2024
    resource: "https://doi.org/10.5281/zenodo.12729884"
    title: "S. Singhal, A. F. Zambrano, M. Pankiewicz, X. Liu, C. Porter, and R. S. Baker. (2024). De-identifying student personally identifying information with gpt-4. Proceedings of the 17th International Conference on Educational Data Mining, pages 559-565, Atlanta, Georgia, USA. https://doi.org/10.5281/zenodo.12729884"
    author: S. Singhal, A. F. Zambrano, M. Pankiewicz, X. Liu, C. Porter, and R. S. Baker
---

# Use LLM-based de-identification as an additional verification layer to catch human redaction mistakes

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends running an LLM redaction pass alongside human de-identification and analyzing the disagreements between the two, so that human omissions can be caught and corrected. As the authors put it, "the analysis of their disagreements with human redactions can help us identify our own mistakes in the process." In this study, manually checking each human-GPT discrepancy surfaced 45 PII words the human coders had overlooked, improving the ground truth itself.

## Design Implications

### Context
#### Requirements
- A human de-identification pass whose disagreements with the LLM output can be manually reviewed and adjudicated
#### Constraints
- GPT redactions are not perfect, so the LLM pass supplements rather than replaces human review

### Target Learners
- Researchers working with student-generated discussion forum and chat data

### Target Learning Goals
- Protecting student privacy when sharing or analyzing educational datasets

## Related Strategies
- 

## Examples
-

## Key Sources
- S. Singhal, A. F. Zambrano, M. Pankiewicz, X. Liu, C. Porter, and R. S. Baker. (2024). De-identifying student personally identifying information with gpt-4. Proceedings of the 17th International Conference on Educational Data Mining, pages 559-565, Atlanta, Georgia, USA. https://doi.org/10.5281/zenodo.12729884
