---
type: claim
title: Distillation increases misclassification of ambiguous To Some Extent tutor responses as Yes
description: Distillation increases misclassification of ambiguous To Some Extent tutor responses as Yes
id: distillation-increases-ambiguous-yes-bias
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: tahmid-al-hannan-2026
    resource: "https://doi.org/10.48550/arxiv.2607.10647"
    title: "Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini. (2026). Knowledge Distillation for Automated AI Tutor Evaluation. https://arxiv.org/abs/2607.10647 [doi:10.48550/arxiv.2607.10647](https://doi.org/10.48550/arxiv.2607.10647)"
    author: Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Distillation increases misclassification of ambiguous To Some Extent tutor responses as Yes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In the baseline model 50.0% of To Some Extent examples were predicted as Yes; after distillation this rose to 65.1%, even as accuracy on clear positive (97.7%) and negative (94.5%) examples improved. [→ Tahmid Al Hannan 2026](#tahmid-al-hannan-2026)

## Evidence

### Tahmid Al Hannan 2026

Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini. (2026). Knowledge Distillation for Automated AI Tutor Evaluation. https://arxiv.org/abs/2607.10647 [doi:10.48550/arxiv.2607.10647](https://doi.org/10.48550/arxiv.2607.10647)

`q2 · i?` · `design · r2`

Confusion-matrix analysis of the Mistake Identification task before (Figure 2) and after (Figure 3) knowledge distillation. The article reports that distillation "also increased this bias, with 65.1% of ambiguous examples classified asYes" while improving clear-case accuracy.

> "In the baseline model, 50.0% ofTo Some Extentexamples were predicted asYes. Although knowledge distillation further improved accuracy on clear positive (97.7%) and negative (94.5%) examples, it also increased this bias, with 65.1% of ambiguous examples classified asYes."

## Discussion


## Related Claims
- [Verification bottleneck: as reliance on AI increases, accuracy in detecting AI errors decreases while confidence does not](verification-bottleneck-confidence-dissociation.md) — related
- [Accuracy-cost value frontier: at $0.10 per million tokens, CDPK performance rose from 50% (April 2024) to 82% (June 2025)](cdpk-value-frontier-rapid-cost-performance-improvement.md) — related
- [Limited output accuracy and over-reliance are the most pressing challenges Chinese HSS students report in GenAI use, alongside strong ethical concern](genai-accuracy-overreliance-challenges-hss.md) — related
- [Knowledge distillation from a frontier LLM substantially improves lightweight AI-tutor evaluation across all four pedagogical dimensions](distillation-improves-ai-tutor-evaluation.md) — reports the opposite
