---
type: strategy
id: deterministic-replicable-text-analysis-methods
title: Use deterministic, fully replicable text-analysis methods with documented search terms when analyzing large text corpora
description: "This strategy replaces nondeterministic LLM-based counting with scripted exact string matching, so that \"Identical inputs produce identical outputs.\" The author used R (v4.4.1) with pdftools and tidyverse to convert p..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: quesen-2026
    resource: "https://eric.ed.gov/?id=ED681368"
    title: "Quesen, S. (2026). What educational research looked like when scores were rising: A comparative analysis of AERA conference programs, 2005–2014 and 2022–2025. WestEd. https://eric.ed.gov/?id=ED681368"
    author: Quesen, S
---

# Use deterministic, fully replicable text-analysis methods with documented search terms when analyzing large text corpora

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
This strategy replaces nondeterministic LLM-based counting with scripted exact string matching, so that "Identical inputs produce identical outputs." The author used R (v4.4.1) with pdftools and tidyverse to convert pdfs to lowercase plain text and search exact term matches, publishing the 13 search terms in three conceptual categories and per-year totals in an appendix so others can audit and reproduce the analysis.

## Design Implications

### Context
#### Requirements
- Document all search terms, conceptual categories, data sources, and software versions; report per-year counts so different sample sizes can be accounted for
#### Constraints
- Term frequency does not capture research quality or practical applicability; composite search terms may capture false positives or miss research using different terminology

### Target Learners
- Education researchers
- Research critics and methodologists

### Target Learning Goals
- Conducting transparent, replicable analyses of educational text corpora

## Related Strategies

- [Match LLM temperature settings to construct characteristics when coding educational dialogue](match-llm-temperature-to-construct-characteristics.md)

## Examples
-

## Key Sources
- Quesen, S. (2026). What educational research looked like when scores were rising: A comparative analysis of AERA conference programs, 2005–2014 and 2022–2025. WestEd. https://eric.ed.gov/?id=ED681368
