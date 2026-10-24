---
type: claim
title: The multi-agent LLM GradeOpt achieved substantial agreement with human coders on overall PCK items (κ = .68, QWK = .79) and outperformed RoBERTa, SBERT, and naïve GPT-4o prompting
description: The multi-agent LLM GradeOpt achieved substantial agreement with human coders on overall PCK items (κ = .68, QWK = .79) and outperformed RoBERTa, SBERT, and naïve GPT-4o prompting
id: gradeopt-substantial-agreement-pck-outperforms-baselines
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

# The multi-agent LLM GradeOpt achieved substantial agreement with human coders on overall PCK items (κ = .68, QWK = .79) and outperformed RoBERTa, SBERT, and naïve GPT-4o prompting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On overall PCK coding of teachers' open-ended responses, GradeOpt achieved Cohen's κ = .68 and QWK = .79, higher than all comparison models on every indicator except one item. [→ Copur-Gencturk 2026](#copur-gencturk-2026)

## Evidence

### Copur-Gencturk 2026

Copur-Gencturk, Y., Moreno, K., Chu, Y., Li, H., & Tang, J. (2026). Automated coding of content and pedagogical content knowledge of mathematics using a multi-agent large language model. ZDM – Mathematics Education. https://doi.org/10.1007/s11858-026-01796-2

`q2 · i?` · `design · r3`

Secondary analysis of agreed-on human codes from 268 U.S. middle school mathematics teachers' responses to nine open-ended PCK items, evaluated on a held-out 20% test set. The article reports "Cohen's κ = .68" overall and QWK = .79 for GradeOpt, with exact agreement ranging from 73% to 89%.

> "Across the automated coding models, GradeOpt demonstrated higher performance on each indicator of success, exact agreement, Cohen's κ, and QWK, at the overall PCK level, across subdomains, and for all items except one, knowledge of mathematical tasks, Item 2."

## Discussion


## Related Claims
- [Comparison models (RoBERTa, SBERT, naïve GPT-4o prompting) failed to reach acceptable agreement on PCK items, with Cohen's κ at or below .55](baseline-models-unacceptable-pck-agreement.md) — related
- [On CK items, GradeOpt showed near-perfect alignment with human codes (κ = .88 and .85; QWK = .89 and .94), comparable to human–human agreement](gradeopt-near-perfect-ck-agreement.md) — related
- [All automated models, including GradeOpt, were most challenged by knowledge of teaching mathematics items (GradeOpt κ = .59) and least challenged by knowledge of students' mathematical thinking (κ = .79)](pck-subdomain-variation-ktm-hardest.md) — related
- [Gaps between Cohen's κ and QWK indicate GradeOpt often assigned codes adjacent to human codes rather than entirely discrepant ones](kappa-qwk-gaps-adjacent-codes.md) — related
- [Prior non-LLM automated coding approaches yielded variable and often lower agreement with human coders on teacher knowledge measures, especially PCK](prior-automated-coding-variable-lower-agreement-pck.md) — related
- [In an AI-guided PD program, rural teachers engaged with mathematical creativity, content knowledge, and PCK as interconnected forms of reasoning rather than isolated domains](ai-guided-pd-integrated-mc-ck-pck-engagement.md) — related
