---
type: claim
title: Among 828 manually coded matched references, the most common issue was ACM metadata mismatch (229 cases), followed by author-field errors (225 cases)
description: Among 828 manually coded matched references, the most common issue was ACM metadata mismatch (229 cases), followed by author-field errors (225 cases)
id: acm-metadata-mismatch-most-common-error
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: paul-denny-2027
    resource: "https://arxiv.org/abs/2609.16574"
    title: "Paul Denny, Gweneth Barbre, Musa Blake, Yan Cathy Hua, Juho Leinonen, Andrew Luxton-Reilly, James Prather, and Brent N. Reeves. (2027). Testing Our Foundations: Citation Trends, Errors, and Emerging Hallucinations in the Computing Education Literature. SIGCSE-TS 2027. https://arxiv.org/abs/2609.16574"
    author: Paul Denny, Gweneth Barbre, Musa Blake, Yan Cathy Hua, Juho Leinonen, Andrew Luxton-Reilly, James Prather, and Brent N. Reeves
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Among 828 manually coded matched references, the most common issue was ACM metadata mismatch (229 cases), followed by author-field errors (225 cases)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Manual coding of 828 records from SET A found 229 cases of ACM metadata mismatch where the PDF showed correct information, and 225 author-field errors classified as potential hallucination in the Li et al. taxonomy. [→ Paul Denny 2027](#paul-denny-2027)

## Evidence

### Paul Denny 2027

Paul Denny, Gweneth Barbre, Musa Blake, Yan Cathy Hua, Juho Leinonen, Andrew Luxton-Reilly, James Prather, and Brent N. Reeves. (2027). Testing Our Foundations: Citation Trends, Errors, and Emerging Hallucinations in the Computing Education Literature. SIGCSE-TS 2027. https://arxiv.org/abs/2609.16574

`q2 · i?` · `associational · r2`

Two coders divided 828 SET A records within each year, classifying them with an adapted Li et al. taxonomy; codes included S (229), H (225), R (188), W (150), M (22), and A (14). The most common issue was a mismatch between ACM DL XML data and the camera-ready PDF.

> "Surprisingly, the most common issue was an apparent mismatch between the ACM DL XML reference data and the plain-text reference as printed in the camera-ready PDF (codeS, 229 cases)."

## Discussion


## Related Claims
- [Conservative manual verification identified 30 hallucinated references across 14 papers in 2025 and 2026 computing education venues](30-hallucinated-references-14-papers-csed.md) — related
- [Of 30 verified hallucinated references, 13 appeared entirely fabricated and 17 were hybrid references combining a real title with fabricated authorship or metadata](hybrid-hallucinated-references-real-title-fake-authors.md) — related
