---
type: strategy
id: two-pass-llm-validation-grading-workflow
title: Two-pass LLM validation with solution-key comparison and focused manual review of divergent pages
description: "After scripts are scanned, each relevant table is cropped and processed in two parallel LLM requests: one with the correct solution to check whether expected letters appear, and one without the solution to extract ent..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: hartwig-grabowski-2026
    resource: "https://arxiv.org/abs/2606.08855"
    title: "Hartwig Grabowski, Michael Canz. (2026). Hybrid E-Assessment in Higher Education: Semi-Automated Grading of Paper-Based Written Examinations. https://arxiv.org/abs/2606.08855"
    author: Hartwig Grabowski, Michael Canz
---

# Two-pass LLM validation with solution-key comparison and focused manual review of divergent pages

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
After scripts are scanned, each relevant table is cropped and processed in two parallel LLM requests: one with the correct solution to check whether expected letters appear, and one without the solution to extract entered letters independently. "The results of both requests are compared", and agreement triggers automatic mapping to answer options and point values. Pages with ambiguous or divergent recognition are flagged for a final focused examiner pass, and students can be emailed cropped table images to check the recognition result.

## Design Implications

### Context
#### Requirements
- Configuration files mapping pages to table regions and columns to criteria and point values
- Scanned scripts in a combined PDF document
#### Constraints
- The procedure is less economical for small cohorts or rarely repeated examinations

### Target Learners
- higher education students in large examination cohorts

### Target Learning Goals
- valid and fair summative grading of paper-based problem-oriented examinations

## Related Strategies

- [Use LLM-based de-identification as an additional verification layer to catch human redaction mistakes](llm-disagreement-analysis-as-verification-layer.md)
- [Grade long handwritten submissions page by page, asking the AI to identify where the credited evidence appears](page-by-page-evidence-location-ai-grading.md)

## Examples
-

## Key Sources
- Hartwig Grabowski, Michael Canz. (2026). Hybrid E-Assessment in Higher Education: Semi-Automated Grading of Paper-Based Written Examinations. https://arxiv.org/abs/2606.08855
