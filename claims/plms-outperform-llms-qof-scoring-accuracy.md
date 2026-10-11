---
type: claim
title: Fine-tuned PLMs outperform prompted LLMs in rubric-based teaching quality scoring accuracy, while LLMs better preserve score variability
description: Fine-tuned PLMs outperform prompted LLMs in rubric-based teaching quality scoring accuracy, while LLMs better preserve score variability
id: plms-outperform-llms-qof-scoring-accuracy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: ivo-bueno-2026
    resource: "https://arxiv.org/abs/2606.05180"
    title: "Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci. (2026). From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment. arXiv. https://arxiv.org/abs/2606.05180"
    author: Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned PLMs outperform prompted LLMs in rubric-based teaching quality scoring accuracy, while LLMs better preserve score variability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the NCTE Quality of Feedback scoring task, fine-tuned PLMs achieve lower error than prompted LLMs, but LLM predictions span the full 1–7 range while PLMs compress toward mid-scale scores. [→ Ivo Bueno 2026](#ivo-bueno-2026)

## Evidence

### Ivo Bueno 2026

Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci. (2026). From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment. arXiv. https://arxiv.org/abs/2606.05180

`q2 · i?` · `design · r2`

Computational evaluation on 6,005 NCTE transcript segments (4,775 train / 1,230 test) scoring the CLASS Quality of Feedback dimension. Fine-tuned PLMs reached MAE 0.96–1.00; the best LLM, Mistral Small Instruct, achieved an MAE of 1.02, higher than the constant baseline. The article reports "fine-tuned PLMs outperform prompted LLMs in accuracy".

> "In response to RQ1, fine-tuned PLMs outperform prompted LLMs in accuracy, while LLMs better preserve score variability."

## Discussion


## Related Claims
- [Fine-tuned PLMs exhibit label compression toward mid-scale QoF scores, never predicting extreme labels 1 and 7](plm-label-compression-qof-extremes.md) — related
