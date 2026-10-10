---
type: claim
title: "On the external CS50-Forum set, EduGuard remains strongest with 86.7% correctness and 6.8% hallucination, though all systems lose grounding"
description: "On the external CS50-Forum set, EduGuard remains strongest with 86.7% correctness and 6.8% hallucination, though all systems lose grounding"
id: eduguard-cs50-forum-generalization
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

# On the external CS50-Forum set, EduGuard remains strongest with 86.7% correctness and 6.8% hallucination, though all systems lose grounding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the 150-query public course-forum validation set, EduGuard keeps the top ranking with 86.7% correctness and 6.8% hallucination. [→ S M Asif Hossain 2026](#s-m-asif-hossain-2026)

## Evidence

### S M Asif Hossain 2026

S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, and Jungpil Shin. (2026). EduGuard: A Safe RAG-Based LLM Tutor for Programming Education. arXiv preprint arXiv:2607.15738. https://arxiv.org/abs/2607.15738

`q2 · i?` · `design · r2`

External validation on the 150-query CS50-Forum set (Table 3); the article describes it as "a public course-forum generalization test", with wider confidence intervals because the set is smaller. Leakage for EduGuard was 8.9% in Table 3.

> "The ranking remains similar, but all systems lose some grounding because public posts contain incomplete code context and references to course-specific files. EduGuard remains strongest, with 86.7% correctness and 6.8% hallucination."

## Discussion


## Related Claims
- [The verification threshold trades hallucination reduction against over-refusal, with the default tau of 0.20 providing the best balance](eduguard-verifier-threshold-sensitivity.md) — related
