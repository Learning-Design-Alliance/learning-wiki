---
type: claim
title: Among tested LLMs, only BERT beats the baseline; GPT-2, MathBERT and XLM-RoBERTa underperform both baselines
description: Among tested LLMs, only BERT beats the baseline; GPT-2, MathBERT and XLM-RoBERTa underperform both baselines
id: only-bert-beats-error-classification-baseline
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: mcnichols-2023
    resource: "https://doi.org/10.1007/978-3-031-36272-9_30"
    title: "McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. [doi:10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30)"
    author: "McNichols, H., Zhang, M., & Lan, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Among tested LLMs, only BERT beats the baseline; GPT-2, MathBERT and XLM-RoBERTa underperform both baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-2 (71.10), MathBERT (72.66) and XLM-RoBERTa (72.75) score below both GRU+C (75.35) and TE+C (78.71) in mean accuracy. [→ McNichols 2023](#mcnichols-2023)

## Evidence

### McNichols 2023

McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. [doi:10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30)

`q2 · i?` · `design · r2`

In the same five-fold cross-validation comparison (Table 1), GPT-2 scores 71.10 ± 2.58, MathBERT 72.66 ± 2.21 and XLM-RoBERTa 72.75 ± 1.54, below GRU+C (75.35 ± 1.41) and TE+C (78.71 ± 1.74). The authors note "the choice of the LLM architecture and initial weights configuration is crucial".

> "Perhaps surprisingly, other LLMs do not perform as well as either baseline me thod. This observation suggests that the choice of the LLM architecture an d initial weights conﬁguration is crucial for the success of LLMs in classiﬁcation tas ks."

## Discussion


## Related Claims
- [Adding ITS-recorded student action context to the input significantly improves MLM-based error classifiers, though GPT-2 declines slightly](action-context-improves-error-classification.md) — reports the opposite
- [A fine-tuned BERT outperforms the leading tree-embedding baseline (TE+C) on algebra error classification without needing syntax trees](bert-outperforms-tree-embedding-error-classification.md) — related
