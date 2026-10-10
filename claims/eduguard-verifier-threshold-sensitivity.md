---
type: claim
title: The verification threshold trades hallucination reduction against over-refusal, with the default tau of 0.20 providing the best balance
description: The verification threshold trades hallucination reduction against over-refusal, with the default tau of 0.20 providing the best balance
id: eduguard-verifier-threshold-sensitivity
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

# The verification threshold trades hallucination reduction against over-refusal, with the default tau of 0.20 providing the best balance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A strict threshold of 0.10 minimizes hallucination but rejects too many acceptable responses; a relaxed threshold of 0.30 improves coverage but allows more unsupported claims; the default 0.20 provides the best balance. [→ S M Asif Hossain 2026](#s-m-asif-hossain-2026)

## Evidence

### S M Asif Hossain 2026

S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, and Jungpil Shin. (2026). EduGuard: A Safe RAG-Based LLM Tutor for Programming Education. arXiv preprint arXiv:2607.15738. https://arxiv.org/abs/2607.15738

`q2 · i?` · `design · r2`

Verifier threshold sensitivity analysis on BILearn-CS reported in Table 6 across five threshold values. The article states the threshold "controls the trade-off between hallucination reduction and over-refusal"; Table 6 shows hallucination 4.9 with over-refusal 9.7 at tau 0.20.

> "A strict threshold of 0.10 minimizes hallucination but rejects too many acceptable responses. A relaxed threshold of 0.30 improves coverage but allows more unsupported claims. The default 𝜏=0.20 provides the best balance."

## Discussion


## Related Claims
- [On the external CS50-Forum set, EduGuard remains strongest with 86.7% correctness and 6.8% hallucination, though all systems lose grounding](eduguard-cs50-forum-generalization.md) — related
- [Classification threshold trades sensitivity against specificity: 0.30 yields 91.3% sensitivity, 0.60 yields 89.7% specificity](cheating-risk-threshold-sensitivity-tradeoff.md) — related
- [AI hallucination can be turned into a pedagogical resource by making verification and collaborative fact evaluation integral to AI-supported learning](hallucination-as-pedagogical-resource.md) — related
