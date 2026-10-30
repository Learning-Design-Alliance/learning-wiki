---
type: claim
title: "Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones"
description: "Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones"
id: bootstrapping-self-consistency-flags-incorrect-answers
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

# Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Over 50 repetitions per exam at temperature 1.0, GPT-4-0314 was inconsistent on 23 of 124 questions (43% of them incorrect) and GPT-4-0613 on 25 (56% incorrect), while only 4 of the consistent responses of each version were incorrect. [→ Joost C. F. de Winter 2024](#joost-c-f-de-winter-2024)

## Evidence

### Joost C. F. de Winter 2024

Joost C. F. de Winter. (2024). Can ChatGPT Pass High School Exams on English Language Comprehension? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00372-z

`q3 · i?` · `design · r2`

Bootstrapping analysis submitting each exam to GPT-4 50 times (API 'n' parameter set to 50) at temperature 1.0, with answers classified as consistently correct, consistently incorrect, or inconsistent. Among inconsistent responses, "10 or 43% for GPT-4-0314; 14 or 56% for GPT-4-0613" were incorrect.

> "Our analysis showed that out of 124 questions across the three exams combined, GPT-4-0314 displayed inconsistency in 23 cases (19%), while GPT-4-0613 displayed inconsistency in 25 cases (20%)"

## Discussion


## Related Claims
- [GPT-4's March and June 2023 versions showed no notable overall difference on the English exams, but differed on individual questions](gpt4-march-june-versions-comparable-overall.md) — related
- [Self-consistency did not improve GPT-4's answer accuracy on these exams, unlike in chain-of-thought tasks](self-consistency-no-accuracy-gain-reading-exams.md) — related
- [Exam questions that GPT-4 answered inconsistently or incorrectly were harder for human examinees, who scored about 63–68% on them versus about 75% on the rest](gpt4-inconsistent-questions-harder-for-students.md) — related
- [GPT-3.5 passes Dutch VWO English reading comprehension exams with a mean grade of 7.3 with re-prompting, and 6.5 when only its first responses are scored](gpt35-passes-dutch-vwo-english-exams.md) — related
- [GPT-4 significantly outperforms the average Dutch student on VWO English reading comprehension, scoring 8.3 (March) and 8.1 (June) without re-prompting](gpt4-outperforms-average-student-english-exams.md) — related
