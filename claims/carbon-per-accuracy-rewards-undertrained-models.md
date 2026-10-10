---
type: claim
title: Carbon per Accuracy as a sustainability metric likely rewards under-trained models because accuracy scales non-linearly with compute
description: Carbon per Accuracy as a sustainability metric likely rewards under-trained models because accuracy scales non-linearly with compute
id: carbon-per-accuracy-rewards-undertrained-models
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: eimler-2026
    resource: "https://arxiv.org/abs/2606.11215"
    title: "Eimler, S.C., Erle, L., Flood, D., Haiman, A., Häckert, L., Helgert, A., McGinness, L., Yapici, B. (2026). The Environmental Cost of LLMs in AIED: Reporting and Practices. https://arxiv.org/abs/2606.11215"
    author: Eimler, S.C., Erle, L., Flood, D., Haiman, A., Häckert, L., Helgert, A., McGinness, L., Yapici, B.
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
---

# Carbon per Accuracy as a sustainability metric likely rewards under-trained models because accuracy scales non-linearly with compute

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`

## Subclaims
`q1 i?` The proposed Carbon per Accuracy metric rests on a false assumption of linear accuracy scaling and will likely reward under-trained models rather than strong performance. [→ Eimler 2026](#eimler-2026)

## Evidence

### Eimler 2026

Eimler, S.C., Erle, L., Flood, D., Haiman, A., Häckert, L., Helgert, A., McGinness, L., Yapici, B. (2026). The Environmental Cost of LLMs in AIED: Reporting and Practices. https://arxiv.org/abs/2606.11215

`q1 · i?` · `theoretical · r2`

This is the authors' analytical argument about their own proposed metric, not an empirical test. They note Carbon per Accuracy interprets CO2 required to reach accuracy 1.0 "under the (false) assumption that accuracy scales linearly with computational expense", so it "will likely reward under-trained models".

> "In reality, the performance of ML models plateaus during training, and the relation between accuracy and training compute is highly non-linear. This means that carbon per accuracy will likely reward under-trained models and not reward strong performance."

## Discussion


## Related Claims
- [Few AIED 2025 papers report computational costs or discuss environmental impacts, and reporting is non-standardized](aied-2025-lack-cost-sustainability-reporting.md) — related
- [Training large AI models carries substantial environmental and human labor costs](ai-training-environmental-labor-costs.md) — related
