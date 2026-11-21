---
type: claim
title: Automated LLM evaluation of MCQ quality showed only moderate agreement with human evaluation
description: Automated LLM evaluation of MCQ quality showed only moderate agreement with human evaluation
id: moderate-human-ai-evaluation-agreement-mcq
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: krushynska-2026
    resource: "https://doi.org/10.48550/arXiv.2602.08383"
    title: "Krushynska, T., Ursin, J., & Heilala, V. (2026). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. Originally published 2025. [doi:10.48550/arXiv.2602.08383](https://doi.org/10.48550/arXiv.2602.08383)"
    author: "Krushynska, T., Ursin, J., & Heilala, V."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Automated LLM evaluation of MCQ quality showed only moderate agreement with human evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Cohen's kappa was 0.432 for MS Copilot and 0.501 for ChatGPT against human acceptability decisions, conventionally moderate. [→ Krushynska 2026](#krushynska-2026)

## Evidence

### Krushynska 2026

Krushynska, T., Ursin, J., & Heilala, V. (2026). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. Originally published 2025. [doi:10.48550/arXiv.2602.08383](https://doi.org/10.48550/arXiv.2602.08383)

`q2 · i?` · `design · r2`

Evaluation of 18 best and 40 worst MCQs by two AIs against the nine criteria; Table 7 prints κ = 0,432 (MS Copilot) and κ = 0,501 (ChatGPT), both in the 0.41–0.60 moderate band. ChatGPT detected flaws in 35 of 40 worst items, including all 22 Copilot rejected.

> "The calculated values of Cohen’s kappa showed that the evaluation model provides moderate human – AI agreement regarding the acceptability of generated MCQs."

## Discussion


## Related Claims
- [Both LLMs showed high interrater reliability on orthopedic MCQs (ChatGPT κ=0.81; DeepSeek κ=0.78)](llm-interrater-reliability-orthopedic-mcqs-kappa.md) — related
- [Judging learning-objective alignment of generated MCQs is more subjective than answering them, with only moderate human agreement](lo-alignment-judgment-more-subjective-than-answering.md) — related
