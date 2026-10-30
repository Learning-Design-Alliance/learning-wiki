---
type: claim
title: "GPT-4's March and June 2023 versions showed no notable overall difference on the English exams, but differed on individual questions"
description: "GPT-4's March and June 2023 versions showed no notable overall difference on the English exams, but differed on individual questions"
id: gpt4-march-june-versions-comparable-overall
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: joost-c-f-de-winter-2024
    resource: "https://doi.org/10.1007/s40593-023-00372-z"
    title: "Joost C. F. de Winter. (2024). Can ChatGPT Pass High School Exams on English Language Comprehension? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00372-z"
    author: Joost C. F. de Winter
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4's March and June 2023 versions showed no notable overall difference on the English exams, but differed on individual questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` With temperature 0, mean exam grades were 8.3 (March) and 8.1 (June), and bootstrapped grades 8.11 vs 8.21, yet the versions answered different individual questions incorrectly (14 vs 18 incorrect, only 9 overlapping). [→ Joost C. F. de Winter 2024](#joost-c-f-de-winter-2024)

## Evidence

### Joost C. F. de Winter 2024

Joost C. F. de Winter. (2024). Can ChatGPT Pass High School Exams on English Language Comprehension? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00372-z

`q3 · i?` · `design · r2`

Version comparison from the Discussion's re-analysis of Table 1 and Table 2 data. Overall averages were comparable between GPT-4-0314 and GPT-4-0613, but "only 9 of these questions were answered incorrectly by both models", indicating per-question shifts despite stable totals.

> "With a temperature setting of 0, GPT-4-0314 answered a total of 14 questions incorrectly (worth 16 points), while GPT-4-0613 incorrectly answered 18 questions (worth 19 points). However, only 9 of these questions were answered incorrectly by both models"

## Discussion


## Related Claims
- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](bootstrapping-self-consistency-flags-incorrect-answers.md) — related
- [GPT-3.5 passes Dutch VWO English reading comprehension exams with a mean grade of 7.3 with re-prompting, and 6.5 when only its first responses are scored](gpt35-passes-dutch-vwo-english-exams.md) — related
- [GPT-4 significantly outperforms the average Dutch student on VWO English reading comprehension, scoring 8.3 (March) and 8.1 (June) without re-prompting](gpt4-outperforms-average-student-english-exams.md) — related
- [Self-consistency did not improve GPT-4's answer accuracy on these exams, unlike in chain-of-thought tasks](self-consistency-no-accuracy-gain-reading-exams.md) — related
