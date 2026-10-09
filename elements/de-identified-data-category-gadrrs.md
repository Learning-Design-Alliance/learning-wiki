---
type: element
id: de-identified-data-category-gadrrs
title: De-identified data category exempt from agreement restrictions with a re-identification ban
description: The agreement defines De-identified Data as data where any and all Personally Identifiable Information has been removed, such that no one knows who the students are when analyzing the data.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: lastinger-center-for-learning-2024
    resource: "https://creativecommons.org/licenses/by-nd/4.0/"
    title: "Lastinger Center for Learning, University of Florida. (2024). Guidance and Agreement for Data harmony, Responsibility, Retention, and Sharing (GADRRS). https://creativecommons.org/licenses/by-nd/4.0/"
    author: Lastinger Center for Learning, University of Florida
---

# De-identified data category exempt from agreement restrictions with a re-identification ban

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 2 studies (1 review, 1 design), `q1`–`q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The agreement defines De-identified Data as data where any and all Personally Identifiable Information has been removed, such that no one knows who the students are when analyzing the data. It states that de-identified data is not considered student data and is not subject to the agreement's terms, and cites the U.S. Department of Education that such data may be shared without FERPA consent with any party for any purpose. The receiving party may use it after termination to assist research or develop its educational sites, services, or applications, but under no circumstances shall it attempt re-identification.

## Design Implications

### Context
#### Requirements
- All PII, including student names, ID numbers, and dates of birth, must be removed before data counts as de-identified.
#### Constraints
- Re-identification attempts are prohibited under all circumstances; the exemption applies only to data from which all PII has been removed.

### Target Learners
- K-12 students whose data are de-identified for analysis

### Target Learning Goals
- Enabling secondary analysis and educational tool development without exposing student identities

## Claims

- [GPT-4 de-identification performance varies by course, with lower agreement in courses with longer posts and more qualitative discussion](../claims/gpt4-redaction-performance-varies-by-course-content.md) [~W]
- [GPT-4 detected 45 PII words that human coders failed to redact across all nine courses](../claims/gpt4-detects-pii-missed-by-human-coders.md) [+W]
- [Maintaining NHSR status requires no researcher access to identifiable records, no added procedures, and no non-standard prompts](../claims/nhsr-maintenance-three-conditions.md) [+W]

## Related Elements

- [GADRRS: an openly licensed data sharing agreement template for educational data exchanges](gadrrs-data-sharing-agreement-template.md)

## Examples

- [Use an operationally separate honest broker to perform linkage and de-identification](../strategies/honest-broker-role-separation-workflow.md)

## Key Sources
- Lastinger Center for Learning, University of Florida. (2024). Guidance and Agreement for Data harmony, Responsibility, Retention, and Sharing (GADRRS). https://creativecommons.org/licenses/by-nd/4.0/
