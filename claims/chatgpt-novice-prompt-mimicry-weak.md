---
type: claim
title: "ChatGPT mimics novice student answers poorly: ChatGPT3.5 barely beats random and ChatGPT4 underperforms random guessing"
description: "ChatGPT mimics novice student answers poorly: ChatGPT3.5 barely beats random and ChatGPT4 underperforms random guessing"
id: chatgpt-novice-prompt-mimicry-weak
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: mixed
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: colin-g-west-2023
    resource: "https://doi.org/10.48550/arXiv.2303.01067"
    title: "Colin G. West. (2023). AI and the FCI: Can ChatGPT project an understanding of introductory physics?. [doi:10.48550/arXiv.2303.01067](https://doi.org/10.48550/arXiv.2303.01067)"
    author: Colin G. West
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: colin-g-west-2023-2
    resource: "https://doi.org/10.48550/arXiv.2303.01067"
    title: "Colin G. West. (2023). AI and the FCI: Can ChatGPT project an understanding of introductory physics?. [doi:10.48550/arXiv.2303.01067](https://doi.org/10.48550/arXiv.2303.01067)"
    author: Colin G. West
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: colin-g-west-2023-3
    resource: "https://doi.org/10.48550/arXiv.2303.01067"
    title: "Colin G. West. (2023). AI and the FCI: Can ChatGPT project an understanding of introductory physics?. [doi:10.48550/arXiv.2303.01067](https://doi.org/10.48550/arXiv.2303.01067)"
    author: Colin G. West
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ChatGPT mimics novice student answers poorly: ChatGPT3.5 barely beats random and ChatGPT4 underperforms random guessing

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ChatGPT3.5's NOVICE-prompt answers matched the most common student pretest answers on 11 of 23 questions. [→ Colin G. West 2023](#colin-g-west-2023)
`q2 i?` On the weighted novice-mimicry metric ChatGPT3.5 scored 63 against a random-guessing minimum of 58. [→ Colin G. West 2023 (2)](#colin-g-west-2023-2)
`q2 i?` ChatGPT4 scored 36, low enough that random guessing about novice choices would outperform it. [→ Colin G. West 2023 (3)](#colin-g-west-2023-3)

## Evidence

### Colin G. West 2023

Colin G. West. (2023). AI and the FCI: Can ChatGPT project an understanding of introductory physics?. [doi:10.48550/arXiv.2303.01067](https://doi.org/10.48550/arXiv.2303.01067)

`q2 · i?` · `design · r2`

Scoring ChatGPT3.5's NOVICE-prompt answers against a key of the most common Fall 2018 pretest student answers: ChatGPT "matched these most-common student answers on 11 occasions out of 23."

> "ChatGPT’s answers to questions with the “NOVICE” prompt matched these most-common student answers on 11 occasions out of 23."

### Colin G. West 2023 (2)

Colin G. West. (2023). AI and the FCI: Can ChatGPT project an understanding of introductory physics?. [doi:10.48550/arXiv.2303.01067](https://doi.org/10.48550/arXiv.2303.01067)

`q2 · i?` · `design · r2`

On a weighted metric crediting each answer by the fraction of pretest students choosing it, excluding plurality-correct items, ChatGPT3.5 scored 63 while "the minimum score would be 58" for random guessing under this response distribution.

> "gives ChatGPT3.5 a score of 63. Note that if we run this cal- culation for the average performance of someone guessing randomly, for this particular distribution of student re- sponses, the minimum score would be 58."

### Colin G. West 2023 (3)

Colin G. West. (2023). AI and the FCI: Can ChatGPT project an understanding of introductory physics?. [doi:10.48550/arXiv.2303.01067](https://doi.org/10.48550/arXiv.2303.01067)

`q2 · i?` · `design · r2`

The identical novice-mimicry metric applied to ChatGPT4: "Its score using the same metric above was a 36," so low that a person randomly guessing novice choices would outperform it, because the model insisted on correct answers.

> "Its score using the same metric above was a 36– i.e., a person randomly trying to guess what a novice would choose would outperform it, because the model insisted on choosing correct answers"

## Discussion


## Related Claims
- [ChatGPT3.5's FCI answers are unstable only where its reasoning is confused, while ChatGPT4 is insensitive to perturbations](chatgpt-response-stability-perturbations.md) — related
- [ChatGPT3.5 answers 15 of 23 modified FCI questions correctly, scoring near or above the median end-of-semester student](chatgpt35-fci-15-of-23-near-median-student.md) — related
- [ChatGPT4 answers 22 of 23 modified FCI questions correctly, performing in the uppermost decile of physics students](chatgpt4-fci-22-of-23-uppermost-decile.md) — related
- [ChatGPT3.5's FCI free responses split between expert-level accuracy and complete incoherence](chatgpt35-fci-free-response-expert-test.md) — related
- [Relative to end-of-semester students in a Fall '18 introductory course, GPT-3.5 would fall at the 39th percentile and GPT-4 above the 96th percentile on the FCI](gpt4-fci-above-96th-percentile-students.md) — related
