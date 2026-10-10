---
type: claim
title: Ablations show removing the strategy selector substantially increases leakage and replacing the NLI verifier with same-model self-check reduces performance
description: Ablations show removing the strategy selector substantially increases leakage and replacing the NLI verifier with same-model self-check reduces performance
id: eduguard-ablation-component-removal
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: s-m-asif-hossain-2026
    resource: "https://arxiv.org/abs/2607.15738"
    title: "S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, and Jungpil Shin. (2026). EduGuard: A Safe RAG-Based LLM Tutor for Programming Education. arXiv preprint arXiv:2607.15738. https://arxiv.org/abs/2607.15738"
    author: S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, and Jungpil Shin
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Ablations show removing the strategy selector substantially increases leakage and replacing the NLI verifier with same-model self-check reduces performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Removing the strategy selector substantially increases leakage, and replacing the NLI verifier with same-model self-check reduces performance, showing that architectural separation matters. [→ S M Asif Hossain 2026](#s-m-asif-hossain-2026)

## Evidence

### S M Asif Hossain 2026

S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, and Jungpil Shin. (2026). EduGuard: A Safe RAG-Based LLM Tutor for Programming Education. arXiv preprint arXiv:2607.15738. https://arxiv.org/abs/2607.15738

`q2 · i?` · `design · r2`

Ablation study on BILearn-CS reported in Table 5; the article also reports that removing the verifier nearly doubles hallucination and gives the no-strategy-selector variant the highest leakage of the ablations. The same-model verifier variant underperforms the full pipeline.

> "Removing the strategy selector substantially increases leakage. Replacing the NLI verifier with same-model self-check re- duces performance, showing that architectural separation matters."

## Discussion


## Related Claims
- [Ablations show the semi-Markov controller is the primary driver of behavioral fidelity (removal pushes DKL to 6.81) and Strategist/Executor separation is essential for epistemic fidelity and realism](beagle-ablation-semi-markov-and-decoupling.md) — related
