---
type: claim
title: "Gaps between Cohen's κ and QWK indicate GradeOpt often assigned codes adjacent to human codes rather than entirely discrepant ones"
description: "Gaps between Cohen's κ and QWK indicate GradeOpt often assigned codes adjacent to human codes rather than entirely discrepant ones"
id: kappa-qwk-gaps-adjacent-codes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: copur-gencturk-2026
    resource: "https://doi.org/10.1007/s11858-026-01796-2"
    title: "Copur-Gencturk, Y., Moreno, K., Chu, Y., Li, H., & Tang, J. (2026). Automated coding of content and pedagogical content knowledge of mathematics using a multi-agent large language model. ZDM – Mathematics Education. https://doi.org/10.1007/s11858-026-01796-2"
    author: "Copur-Gencturk, Y., Moreno, K., Chu, Y., Li, H., & Tang, J."
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Gaps between Cohen's κ and QWK indicate GradeOpt often assigned codes adjacent to human codes rather than entirely discrepant ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Notable κ–QWK differences (e.g., Δ = .18 for knowledge of mathematical tasks Item 1; Δ = .13 to .19 for knowledge of teaching mathematics items) indicate partial agreement through adjacent-category coding. [→ Copur-Gencturk 2026](#copur-gencturk-2026)

## Evidence

### Copur-Gencturk 2026

Copur-Gencturk, Y., Moreno, K., Chu, Y., Li, H., & Tang, J. (2026). Automated coding of content and pedagogical content knowledge of mathematics using a multi-agent large language model. ZDM – Mathematics Education. https://doi.org/10.1007/s11858-026-01796-2

`q2 · i?` · `design · r3`

Results-section interpretation of QWK versus κ discrepancies on 3-point rubric items, where QWK penalizes larger score discrepancies. The article reports specific gaps including knowledge of mathematical tasks, Item 1 (Δ = .18) and all knowledge of teaching mathematics items (Δ = .13 to .19).

> "These differences suggest that although the exact category agreement was sometimes lower, GradeOpt often generated codes adjacent to those assigned by human coders rather than entirely discrepant codes, indicating partial agreement."

## Discussion


## Related Claims
- [On CK items, GradeOpt showed near-perfect alignment with human codes (κ = .88 and .85; QWK = .89 and .94), comparable to human–human agreement](gradeopt-near-perfect-ck-agreement.md) — related
- [The multi-agent LLM GradeOpt achieved substantial agreement with human coders on overall PCK items (κ = .68, QWK = .79) and outperformed RoBERTa, SBERT, and naïve GPT-4o prompting](gradeopt-substantial-agreement-pck-outperforms-baselines.md) — related
- [All automated models, including GradeOpt, were most challenged by knowledge of teaching mathematics items (GradeOpt κ = .59) and least challenged by knowledge of students' mathematical thinking (κ = .79)](pck-subdomain-variation-ktm-hardest.md) — related
- [Most faculty–GPT-4 scoring discrepancies were only one-point differences, shrinking across iterations](oeq-scoring-discrepancies-mostly-one-point.md) — related
