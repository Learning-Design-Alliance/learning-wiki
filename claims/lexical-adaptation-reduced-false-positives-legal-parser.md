---
type: claim
title: Lexical adaptation of the general rhetorical parser reduced false positives in legal essay analysis without introducing parse errors
description: Lexical adaptation of the general rhetorical parser reduced false positives in legal essay analysis without introducing parse errors
id: lexical-adaptation-reduced-false-positives-legal-parser
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2016
recheck_by: 2019
sources:
  - id: knight-2016
    resource: "https://doi.org/10.1007/s40593-016-0121-0"
    title: "Knight, S., Buckingham Shum, S., Ryan, P., Sándor, Á., & Wang, X. (2016). Designing Academic Writing Analytics for Civil Law Student Self-Assessment. *International Journal of Artificial Intelligence in Education, 28*(1), 1–28. [doi:10.1007/s40593-016-0121-0](https://doi.org/10.1007/s40593-016-0121-0)"
    author: "Knight, S., Buckingham Shum, S., Ryan, P., Sándor, Á., & Wang, X."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Lexical adaptation of the general rhetorical parser reduced false positives in legal essay analysis without introducing parse errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Deleting legal 'terms of art' from the general analytical lexicon decreased False Positives from 13 to 5 with a commensurate increase in True Negatives from 52 to 60, while True Positives (19) and False Negatives (7) were unchanged. [→ Knight 2016](#knight-2016)

## Evidence

### Knight 2016

Knight, S., Buckingham Shum, S., Ryan, P., Sándor, Á., & Wang, X. (2016). Designing Academic Writing Analytics for Civil Law Student Self-Assessment. *International Journal of Artificial Intelligence in Education, 28*(1), 1–28. [doi:10.1007/s40593-016-0121-0](https://doi.org/10.1007/s40593-016-0121-0)

`q2 · i?` · `design · r2`

Annotation exercise by the civil law academic on a sample of essays with known grades, comparing confusion matrices before (TP: 19, FP: 13, FN: 7, TN: 52) and after lexical adaptation (TP: 19, FP: 5, FN: 7, TN: 60). The article reports "a decrease in the number of False Positives" following deletion of legal terms. No formal evaluation beyond this comparison was performed.

> "These changes resulted in a decrease in the number of False Positives with a commensurate increase in the number of True Negatives. This was due to the deletion of the legal terms from the general analytical lexicon."

## Discussion


## Related Claims
- [Expert-judged sentence selection by a tuned rhetorical parser succeeded, but student reactions to key-sentence highlighting were mixed](awa-sentence-highlighting-mixed-student-response.md) — related
- [GPT models showed lower accuracy with more rubric-related errors (28% vs. 13% for Gemini 3 Flash) and near parity between false positives and negatives](gpt-models-more-rubric-errors-than-gemini.md) — related
