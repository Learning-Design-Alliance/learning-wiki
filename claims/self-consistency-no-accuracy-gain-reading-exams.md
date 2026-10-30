---
type: claim
title: "Self-consistency did not improve GPT-4's answer accuracy on these exams, unlike in chain-of-thought tasks"
description: "Self-consistency did not improve GPT-4's answer accuracy on these exams, unlike in chain-of-thought tasks"
id: self-consistency-no-accuracy-gain-reading-exams
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: joost-c-f-de-winter-2024
    resource: "https://doi.org/10.1007/s40593-023-00372-z"
    title: "Joost C. F. de Winter. (2024). Can ChatGPT Pass High School Exams on English Language Comprehension? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00372-z"
    author: Joost C. F. de Winter
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Self-consistency did not improve GPT-4's answer accuracy on these exams, unlike in chain-of-thought tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The self-consistency method did not yield more accurate answers because the exam questions required directly converging on an answer rather than chain-of-thought reasoning. [→ Joost C. F. de Winter 2024](#joost-c-f-de-winter-2024)

## Evidence

### Joost C. F. de Winter 2024

Joost C. F. de Winter. (2024). Can ChatGPT Pass High School Exams on English Language Comprehension? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00372-z

`q2 · i?` · `design · r2`

Authors' interpretation in the Discussion of why bootstrapping flagged uncertainty without improving accuracy: ChatGPT had to directly converge on an answer such as a multiple-choice letter, so adding variation at higher temperature provided no accuracy benefit. This is an author interpretation, not a tested manipulation.

> "this method did not prove to be useful for arriving at a more accurate answer, contrary to findings by Wang et al. ( 2023). A possible explanation is that the English exam questions did not involve chain-of-thought reasoning as in Wang et al. ( 2023)"

## Discussion


## Related Claims
- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](bootstrapping-self-consistency-flags-incorrect-answers.md) — related
- [GPT-4's March and June 2023 versions showed no notable overall difference on the English exams, but differed on individual questions](gpt4-march-june-versions-comparable-overall.md) — related
