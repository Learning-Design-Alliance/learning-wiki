---
type: claim
title: "ChatGPT3.5's FCI answers are unstable only where its reasoning is confused, while ChatGPT4 is insensitive to perturbations"
description: "ChatGPT3.5's FCI answers are unstable only where its reasoning is confused, while ChatGPT4 is insensitive to perturbations"
id: chatgpt-response-stability-perturbations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: colin-g-west-2023
    resource: "https://doi.org/10.48550/arXiv.2303.01067"
    title: "Colin G. West. (2023). AI and the FCI: Can ChatGPT project an understanding of introductory physics?. [doi:10.48550/arXiv.2303.01067](https://doi.org/10.48550/arXiv.2303.01067)"
    author: Colin G. West
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: colin-g-west-2023-2
    resource: "https://doi.org/10.48550/arXiv.2303.01067"
    title: "Colin G. West. (2023). AI and the FCI: Can ChatGPT project an understanding of introductory physics?. [doi:10.48550/arXiv.2303.01067](https://doi.org/10.48550/arXiv.2303.01067)"
    author: Colin G. West
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# ChatGPT3.5's FCI answers are unstable only where its reasoning is confused, while ChatGPT4 is insensitive to perturbations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q1 i?` ChatGPT3.5 consistently changed answers between regenerations only on a subset of the eight questions whose written responses were completely confused. [→ Colin G. West 2023](#colin-g-west-2023)
`q1 i?` ChatGPT4's responses were completely insensitive to both perturbation types. [→ Colin G. West 2023 (2)](#colin-g-west-2023-2)

## Evidence

### Colin G. West 2023

Colin G. West. (2023). AI and the FCI: Can ChatGPT project an understanding of introductory physics?. [doi:10.48550/arXiv.2303.01067](https://doi.org/10.48550/arXiv.2303.01067)

`q1 · i?` · `design · r2`

A preliminary stability probe regenerating each ChatGPT3.5 response three times with the regenerate-response feature: consistent answer changes occurred only on "a subset of the eight questions for which we judged that its written responses were completely confused."

> "The only cases where ChatGPT3.5 consistently changed its answers between regenerations were a subset of the eight questions for which we judged that its written responses were completely confused."

### Colin G. West 2023 (2)

Colin G. West. (2023). AI and the FCI: Can ChatGPT project an understanding of introductory physics?. [doi:10.48550/arXiv.2303.01067](https://doi.org/10.48550/arXiv.2303.01067)

`q1 · i?` · `design · r2`

The same stability probing, including reworded input variants, applied to ChatGPT4: its responses were "completely insensitive to either of the perturbation types described above."

> "Our discussion here has focused on ChatGPT3.5 be- cause we found that ChatGPT4’s responses were com- pletely insensitive to either of the perturbation types described above."

## Discussion


## Related Claims
- [ChatGPT mimics novice student answers poorly: ChatGPT3.5 barely beats random and ChatGPT4 underperforms random guessing](chatgpt-novice-prompt-mimicry-weak.md) — related
- [ChatGPT4 gives no completely confused FCI free responses, with 20 of 23 assessed exactly correct](chatgpt4-fci-free-responses-exactly-correct.md) — related
- [ChatGPT3.5's FCI free responses split between expert-level accuracy and complete incoherence](chatgpt35-fci-free-response-expert-test.md) — related
- [ChatGPT3.5 answers 15 of 23 modified FCI questions correctly, scoring near or above the median end-of-semester student](chatgpt35-fci-15-of-23-near-median-student.md) — related
- [ChatGPT4 answers 22 of 23 modified FCI questions correctly, performing in the uppermost decile of physics students](chatgpt4-fci-22-of-23-uppermost-decile.md) — related
