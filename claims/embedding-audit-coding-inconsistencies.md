---
type: claim
title: Pairwise semantic distance between embedded responses can audit previously human-coded datasets, flagging near-identical responses that received different codes
description: Pairwise semantic distance between embedded responses can audit previously human-coded datasets, flagging near-identical responses that received different codes
id: embedding-audit-coding-inconsistencies
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: mjaaland-2025
    resource: "https://doi.org/10.3233/faia251443"
    title: "Mjaaland, J. T., Kreutzer, M. F., Tyseng, H., Fussell, R. K., Passante, G., Holmes, N. G., Malthe-Sørenssen, A., & Odden, T. O. B. (2025). A Framework for Deductive Semantic Content Analysis at Scale in Science Education Using Text Embeddings. Data available at Zenodo; code shared via GitHub. [doi:10.3233/faia251443](https://doi.org/10.3233/faia251443)"
    author: "Mjaaland, J. T., Kreutzer, M. F., Tyseng, H., Fussell, R. K., Passante, G., Holmes, N. G., Malthe-Sørenssen, A., & Odden, T. O. B."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Pairwise semantic distance between embedded responses can audit previously human-coded datasets, flagging near-identical responses that received different codes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Flagging response pairs within a cosine distance threshold of 0.15 with different codes revealed 669 inconsistent responses; the coding team resolved 531 by reclassifying 153 responses. [→ Mjaaland 2025](#mjaaland-2025)

## Evidence

### Mjaaland 2025

Mjaaland, J. T., Kreutzer, M. F., Tyseng, H., Fussell, R. K., Passante, G., Holmes, N. G., Malthe-Sørenssen, A., & Odden, T. O. B. (2025). A Framework for Deductive Semantic Content Analysis at Scale in Science Education Using Text Embeddings. Data available at Zenodo; code shared via GitHub. [doi:10.3233/faia251443](https://doi.org/10.3233/faia251443)

`q2 · i?` · `design · r2`

Dataset audit using cosine distance between all pairs of embedded survey responses, flagging pairs within a 0.15 distance threshold that had received different human codes. The article reports "669 responses were nearly identical in content or phrasing to some other response with a different code"; 531 inconsistencies were resolved by reclassifying 153 responses.

> "This revealed that 669 responses were nearly identical in content or phrasing to some other response with a different code."

## Discussion


## Related Claims
- [Personalized responses remain semantically grounded in the shared knowledge base while varying in surface-level expression and structure](semantic-grounding-with-surface-variation.md) — related
- [LLM-based automated assessment of student code self-explanations outperforms semantic similarity methods on a balanced classification task](llm-assessment-outperforms-semantic-similarity-code-explanations.md) — related
- [Only 8.0% of queries reaching a person duplicated existing corpus content, suggesting the knowledge base was already well used](corpus-coverage-8-percent-person-resolved-queries.md) — related
