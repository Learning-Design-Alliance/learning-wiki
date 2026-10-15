---
type: claim
title: The most common prompt mistakes are omissions of key details, most frequently the specified function return type
description: The most common prompt mistakes are omissions of key details, most frequently the specified function return type
id: omission-key-details-commonest-prompt-mistake
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: victor-alexandru-pădurean-2026
    resource: "https://doi.org/10.1145/3765964.3811639"
    title: "Victor-Alexandru Pădurean, Kaitlin Riegel, Gweneth Barbre, Musa Blake, Paul Denny, Alkis Gotovos, Juho Leinonen, Stephen MacNeil, James Prather, and Adish Singla. (2026). Understanding Student Perceptions, Mistakes, and Debugging Approaches when Solving Natural Language Programming Tasks. Proceedings of the ACM Conference on International Computing Education Research Vol.1 (ICER 2026 Vol. 1). https://doi.org/10.1145/3765964.3811639"
    author: Victor-Alexandru Pădurean, Kaitlin Riegel, Gweneth Barbre, Musa Blake, Paul Denny, Alkis Gotovos, Juho Leinonen, Stephen MacNeil, James Prather, and Adish Singla
    q: 2
    i: "?"
    kind: qualitative
    rigour: "?"
---

# The most common prompt mistakes are omissions of key details, most frequently the specified function return type

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r?` · `q2`

## Subclaims
`q2 i?` In coding of half of all initial incorrect prompts (1,286 prompts), the most frequent mistakes were omissions of key elements such as the specified function return type, specified argument names, and appropriate expected output/return. [→ Victor-Alexandru Pădurean 2026](#victor-alexandru-padurean-2026)

## Evidence

### Victor-Alexandru Pădurean 2026

Victor-Alexandru Pădurean, Kaitlin Riegel, Gweneth Barbre, Musa Blake, Paul Denny, Alkis Gotovos, Juho Leinonen, Stephen MacNeil, James Prather, and Adish Singla. (2026). Understanding Student Perceptions, Mistakes, and Debugging Approaches when Solving Natural Language Programming Tasks. Proceedings of the ACM Conference on International Computing Education Research Vol.1 (ICER 2026 Vol. 1). https://doi.org/10.1145/3765964.3811639

`q2 · i?` · `qualitative · r?`

Coding of 1,286 initial incorrect prompts (half of all incorrect first prompts per problem) for missing elements such as function return type and argument names. The authors interpret omissions as "suggesting both a failure to acknowledge their importance and over-reliance on AI to infer them"; frequencies are printed per problem in Table 3.

> "Common errors were omit- ting aSpecified Function Return TypeorSpecified Argument Namesfrom a prompt across most of the problems. The results sug- gested that omissions often co-occurred."

## Discussion


## Related Claims
- [When prompts failed, students most commonly reported clarifying intent or specifying more detail, and reflecting on the problem depiction, rather than tracing code or examining test cases](clarify-intent-top-refinement-strategy.md) — related
- [Missing prompt-element types significantly co-occur: failure to provide appropriate functionality explanation correlates strongly with missing expected output/return and with extraneous elements](prompt-mistake-co-occurrence-correlations.md) — related
- [Correlations between the number of prompt mistakes and number of messages sent were non-significant or weak, giving little evidence that mistake count influenced prompting effort](mistake-count-message-count-weak-correlation.md) — related
