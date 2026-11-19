---
type: claim
title: A fine-tuned BERT outperforms the leading tree-embedding baseline (TE+C) on algebra error classification without needing syntax trees
description: A fine-tuned BERT outperforms the leading tree-embedding baseline (TE+C) on algebra error classification without needing syntax trees
id: bert-outperforms-tree-embedding-error-classification
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

# A fine-tuned BERT outperforms the leading tree-embedding baseline (TE+C) on algebra error classification without needing syntax trees

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` BERT reaches 80.68% mean test classification accuracy versus 78.71% for the TE+C baseline on the 24-label CogTutor BUG subset. [→ McNichols 2023](#mcnichols-2023)

## Evidence

### McNichols 2023

McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. [doi:10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30)

`q2 · i?` · `design · r2`

Five-fold cross-validation on the CogTutor BUG steps (3,318 steps with the 24-label baseline labeling) compares fine-tuned LLMs to baselines by classification accuracy. BERT scores 80.68 ± 1.1 versus TE+C's 78.71 ± 1.74; the article calls this "a slight improvement". No effect size is printed.

> "We observe that BE RT has the best performance across all LLMs and is a slight improvement ov er the lead- ing baseline method (TE+C)."

## Discussion


## Related Claims
- [Training on synthetically generated steps, tree embedding-based methods significantly outperform GRU and CNN encoders when tested on real student data](synthetic-training-tree-embeddings-outperform-real-data.md) — related
- [Tree embedding-based encoding with a classifier performs best at classifying feedback types for incorrect steps, reaching 78.71% accuracy across 24 feedback types](tree-embedding-best-feedback-type-classification.md) — reports the opposite
- [Pre-training on synthetic data before fine-tuning on limited real data improves math operation classification accuracy, with the largest gains when real data is extremely limited](synthetic-pretraining-finetuning-limited-real-data.md) — related
- [Among tested LLMs, only BERT beats the baseline; GPT-2, MathBERT and XLM-RoBERTa underperform both baselines](only-bert-beats-error-classification-baseline.md) — related
