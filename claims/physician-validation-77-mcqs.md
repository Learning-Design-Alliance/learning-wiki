---
type: claim
title: Expert physician review excluded 23 of 100 LLM-generated MCQs, yielding a validated set of 77 questions
description: Expert physician review excluded 23 of 100 LLM-generated MCQs, yielding a validated set of 77 questions
id: physician-validation-77-mcqs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: vinson-2026
    resource: "https://doi.org/10.1038/s41598-026-48326-4"
    title: "Vinson, J., Caronia, C., & Savargaonkar, R. (2026). Input structure–driven instability and convergence in large language model clinical reasoning: a formative study using pediatric residency–level MCQs. Scientific Reports. https://doi.org/10.1038/s41598-026-48326-4"
    author: "Vinson, J., Caronia, C., & Savargaonkar, R."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Expert physician review excluded 23 of 100 LLM-generated MCQs, yielding a validated set of 77 questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Vinson 2026: no comparison group (read from the study by two models, 2026-11-04)

## Subclaims
`q2 i?` Three pediatric physicians independently reviewed 100 randomly selected LLM-generated MCQs and unanimously excluded 23, leaving 77 validated questions. [→ Vinson 2026](#vinson-2026)

## Evidence

### Vinson 2026

Vinson, J., Caronia, C., & Savargaonkar, R. (2026). Input structure–driven instability and convergence in large language model clinical reasoning: a formative study using pediatric residency–level MCQs. Scientific Reports. https://doi.org/10.1038/s41598-026-48326-4

`q2 · i?` · `causal · r1`

Question-validation phase of the cross-sectional study: two U.S. board-certified pediatricians and one pediatric resident independently assessed 100 randomly selected ChatGPT-generated items for medical accuracy, clinical realism, subspecialty relevance, and USMLE formatting. The article reports "a final validated set of 77 MCQs."

> "Through unanimous consensus, 23 questions were excluded due to ambiguity, formatting issues, or flawed medical logic, resulting in a final validated set of 77 MCQs."

## Discussion


## Related Claims
- [Blind expert assessment of GPT-4-generated MCQs found the majority valid as exam questions, with problematic-question rates varying by field](gpt4-blind-assessment-majority-valid.md) — a broader claim this one bears on
- [Ontology-based generation produced exam-appropriate case-based MCQs, with 30% of a stratified sample rated appropriate by both expert raters and 50% by at least one](emcqg-expert-rated-exam-appropriate-questions.md) — related
- [LLM accuracy on pediatric residency-level MCQs varies widely (38%–90%) across models when all questions are delivered simultaneously](all-at-once-llm-accuracy-38-90.md) — related
- [Batch delivery of ten questions converges LLM accuracy to 83%–88% with no statistically significant inter-model differences](batch-delivery-convergence-83-88.md) — related
