---
type: strategy
id: honest-broker-role-separation-workflow
title: Use an operationally separate honest broker to perform linkage and de-identification
description: The guide recommends assigning data linkage and de-identification to a person or service that stays outside the research team, so researchers analyze only de-identified datasets.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: younger-j-2026-september-navigating
    resource: "https://doi.org/10.51388/20.500.12265/318"
    title: "Younger, J. (2026, September). Navigating research approvals for edtech research and evaluation: A practical guide. Digital Promise. https://doi.org/10.51388/20.500.12265/318"
---

# Use an operationally separate honest broker to perform linkage and de-identification

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The guide recommends assigning data linkage and de-identification to a person or service that stays outside the research team, so researchers analyze only de-identified datasets. An internal employee such as a data engineer can serve, "provided they remain operationally separate from the research team." The broker maintains linkage keys and enforces suppression thresholds such as redacting demographic fields when subgroup counts fall below a safe threshold.

## Design Implications

### Context
#### Requirements
- Plan the honest broker workflow before research begins and document each person's responsibilities
- Researchers must never possess crosswalk keys, raw logs, or contextual data needed to relink records
#### Constraints
- Small companies where engineers wear multiple hats may need another person to perform the broker role

### Target Learners
- K-12 students in districts sharing records for edtech research

### Target Learning Goals
- Enabling external evidence generation while protecting student privacy

## Related Strategies

- [Use LLM-based de-identification as an additional verification layer to catch human redaction mistakes](llm-disagreement-analysis-as-verification-layer.md)
- [Integrate PETs at every stage of the research lifecycle](integrate-pets-across-research-lifecycle.md)

## Examples
-

## Key Sources
- Younger, J. (2026, September). Navigating research approvals for edtech research and evaluation: A practical guide. Digital Promise. https://doi.org/10.51388/20.500.12265/318
