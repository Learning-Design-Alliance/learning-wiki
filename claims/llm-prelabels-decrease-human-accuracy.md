---
type: claim
title: Providing LLM pre-labels can decrease human annotation accuracy when the model is incorrect, due to automation bias
description: Providing LLM pre-labels can decrease human annotation accuracy when the model is incorrect, due to automation bias
id: llm-prelabels-decrease-human-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: thomas-2026
    resource: "https://doi.org/10.48550/arxiv.2603.29141"
    title: "Thomas, D.R., Borchers, C., Vanacore, K.P., Koedinger, K.R., & Kizilcec, R.F. (2026). Modernizing Ground Truth: Four Shifts Toward Improving Reliability and Validity in AI in Education. https://arxiv.org/abs/2603.29141 [doi:10.48550/arxiv.2603.29141](https://doi.org/10.48550/arxiv.2603.29141)"
    author: "Thomas, D.R., Borchers, C., Vanacore, K.P., Koedinger, K.R., & Kizilcec, R.F."
    q: 1
    i: "?"
    kind: theoretical
    rigour: "?"
---

# Providing LLM pre-labels can decrease human annotation accuracy when the model is incorrect, due to automation bias

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r?` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Demonstrated research shows that providing LLM pre-labels can decrease human accuracy when the model is incorrect, as annotators may uncritically adopt the AI's suggestion. [→ Thomas 2026](#thomas-2026)

## Evidence

### Thomas 2026

Thomas, D.R., Borchers, C., Vanacore, K.P., Koedinger, K.R., & Kizilcec, R.F. (2026). Modernizing Ground Truth: Four Shifts Toward Improving Reliability and Validity in AI in Education. https://arxiv.org/abs/2603.29141 [doi:10.48550/arxiv.2603.29141](https://doi.org/10.48550/arxiv.2603.29141)

`q1 · i?` · `theoretical · r?`

A position paper on reliability and validity in AI in education. It reports, as a finding of prior work, that LLM pre-labels "can actually decrease human accuracy when the model is incorrect" because annotators uncritically adopt the AI's suggestion, and presents no study of its own. The study it cites is Wang, X., Kim, H., Rahman, S., Mitra, K., & Miao, Z. (2024). Human-LLM collaborative annotation through effective verification of LLM labels. *CHI '24*. [doi:10.1145/3613904.3641960](https://doi.org/10.1145/3613904.3641960); its design is not described here and has not been read for this page.

> "[50] demonstrated that providing LLM pre-labels can actually decrease human accuracy when the model is incorrect, as annotators may uncritically adopt the AI's suggestion"

## Discussion


## Related Claims
- [Reviewed literature reports risks of overreliance, AI errors in complex tasks, and students' uncritical acceptance of AI-generated outputs](ai-math-risks-overreliance-errors-uncritical-trust.md) — a broader claim this one bears on
- A pilot human annotation surfaces a framing discrepancy: a NEET aspirant labeled all 10 sampled questions as Recall, including the five the LLM tagged as Elimination/Negation — related
- [Automated AI assessment systems reduce grading time and improve evaluation consistency in nursing education](automated-ai-assessment-reduces-grading-time-bias.md) — related
- [Warning labels alone did not improve performance or reduce reliance on GenAI advice, and students sometimes adopted incorrect AI answers](genai-warning-labels-insufficient-reliance.md) — related
- [Automation bias toward fluent LLM output surrenders learners' epistemic agency](automation-bias-surrenders-epistemic-agency.md) — related
