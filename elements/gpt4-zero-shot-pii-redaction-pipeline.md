---
type: element
id: gpt4-zero-shot-pii-redaction-pipeline
title: GPT-4 zero-shot PII redaction prompt and pipeline for educational forum posts
description: "A de-identification pipeline in which each forum post is sent individually to the OpenAI gpt-4-0613 model via API with a prompt instructing it to \"remov[e] any personally identifiable information (PII)\" including name..."
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

# GPT-4 zero-shot PII redaction prompt and pipeline for educational forum posts

> **Element** · [All elements](index.md)
> **Evidence** · 5 claims (3 for, 2 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
A de-identification pipeline in which each forum post is sent individually to the OpenAI gpt-4-0613 model via API with a prompt instructing it to "remov[e] any personally identifiable information (PII)" including names, company names, places of origin, current living locations, addresses, and social media links, replacing removed PII with '[REDACTED]' while keeping the rest of the text unchanged word for word. The code for the GPT-based de-identification process was released in a GitHub repository for replication.

## Design Implications

### Context
#### Requirements
- API access to GPT-4 with data sent under OpenAI's privacy policy, which retains data for a maximum of 30 days
#### Constraints
- An early prompt draft explicitly instructing GPT not to redact public figures caused lower overall performance for both precision and recall; without instructions to preserve formatting, GPT corrected grammar and changed words

### Target Learners
- Educational data mining and learning analytics researchers de-identifying student text data

### Target Learning Goals
- Automated redaction of PII from student-generated discussion forum posts

## Claims

- [GPT-4 detected 45 PII words that human coders failed to redact across all nine courses](../claims/gpt4-detects-pii-missed-by-human-coders.md) [+W]
- [GPT-4 achieves high recall (average 0.958) but low precision (average 0.526) when de-identifying MOOC forum posts](../claims/gpt4-high-recall-low-precision-pii-redaction.md) [+W]
- [GPT-4 over-redacts famous names, locations, and mythological creatures that are not PII in educational forum discussions](../claims/gpt4-over-redaction-of-non-pii-names-and-locations.md) [~W]
- [Supervised machine learning de-identification still outperforms GPT-4, though GPT-4 exceeds class-list/regular-expression and transformer approaches in recall](../claims/gpt4-redaction-compared-to-prior-methods.md) [+W]
- [GPT-4 de-identification performance varies by course, with lower agreement in courses with longer posts and more qualitative discussion](../claims/gpt4-redaction-performance-varies-by-course-content.md) [~W]

## Related Elements
- 

## Examples

- [Use LLM-based de-identification as an additional verification layer to catch human redaction mistakes](../strategies/llm-disagreement-analysis-as-verification-layer.md)

## Key Sources
- S. Singhal, A. F. Zambrano, M. Pankiewicz, X. Liu, C. Porter, and R. S. Baker. (2024). De-identifying student personally identifying information with gpt-4. Proceedings of the 17th International Conference on Educational Data Mining, pages 559-565, Atlanta, Georgia, USA. https://doi.org/10.5281/zenodo.12729884
