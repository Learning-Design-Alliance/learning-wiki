---
type: claim
title: "Comparison models (RoBERTa, SBERT, naïve GPT-4o prompting) failed to reach acceptable agreement on PCK items, with Cohen's κ at or below .55"
description: "Comparison models (RoBERTa, SBERT, naïve GPT-4o prompting) failed to reach acceptable agreement on PCK items, with Cohen's κ at or below .55"
id: baseline-models-unacceptable-pck-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: copur-gencturk-2026
    resource: "https://doi.org/10.1007/s11858-026-01796-2"
    title: "Copur-Gencturk, Y., Moreno, K., Chu, Y., Li, H., & Tang, J. (2026). Automated coding of content and pedagogical content knowledge of mathematics using a multi-agent large language model. ZDM – Mathematics Education. https://doi.org/10.1007/s11858-026-01796-2"
    author: "Copur-Gencturk, Y., Moreno, K., Chu, Y., Li, H., & Tang, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Comparison models (RoBERTa, SBERT, naïve GPT-4o prompting) failed to reach acceptable agreement on PCK items, with Cohen's κ at or below .55

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` RoBERTa and SBERT achieved Cohen's κ between .00 and .39 and .00 and .55 respectively on PCK items, and naïve GPT-4o prompting ranged from .06 to .54. [→ Copur-Gencturk 2026](#copur-gencturk-2026)

## Evidence

### Copur-Gencturk 2026

Copur-Gencturk, Y., Moreno, K., Chu, Y., Li, H., & Tang, J. (2026). Automated coding of content and pedagogical content knowledge of mathematics using a multi-agent large language model. ZDM – Mathematics Education. https://doi.org/10.1007/s11858-026-01796-2

`q2 · i?` · `design · r2`

Results section comparison on the same held-out test set of teachers' PCK responses. The article states RoBERTa and SBERT "did not achieve acceptable levels of performance" and the Naïve Prompt approach "also experienced difficulty coding these responses effectively."

> "The two commonly used pretrained, rule-based methods, RoBERTa and SBERT, did not achieve acceptable levels of performance, particularly in terms of Cohen's κ (.00 to .39 for RoBERTa and .00 to .55 for SBERT). Among the LLM-based methods, the Naïve Prompt approach also experienced difficulty coding these responses effectively (Cohen's κ ranging from .06 to .54)."

## Discussion


## Related Claims
- [The multi-agent LLM GradeOpt achieved substantial agreement with human coders on overall PCK items (κ = .68, QWK = .79) and outperformed RoBERTa, SBERT, and naïve GPT-4o prompting](gradeopt-substantial-agreement-pck-outperforms-baselines.md) — related
- [Prior non-LLM automated coding approaches yielded variable and often lower agreement with human coders on teacher knowledge measures, especially PCK](prior-automated-coding-variable-lower-agreement-pck.md) — related
- [Sentence embedding models reach only moderate agreement and need human supervision for open-ended grading](embedding-models-moderate-agreement-need-supervision.md) — related
