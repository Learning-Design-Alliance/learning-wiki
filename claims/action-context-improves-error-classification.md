---
type: claim
title: Adding ITS-recorded student action context to the input significantly improves MLM-based error classifiers, though GPT-2 declines slightly
description: Adding ITS-recorded student action context to the input significantly improves MLM-based error classifiers, though GPT-2 declines slightly
id: action-context-improves-error-classification
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

# Adding ITS-recorded student action context to the input significantly improves MLM-based error classifiers, though GPT-2 declines slightly

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Including Cognitive Tutor action information improves all MLM models; XLM-RoBERTa improves by 6.5% while GPT-2 shows a small deterioration. [→ McNichols 2023](#mcnichols-2023)

## Evidence

### McNichols 2023

McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. [doi:10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30)

`q2 · i?` · `design · r2`

Experiments on the new 19-label CogTutorBugs labeling (5,339 BUG steps) add Cognitive Tutor-recorded student action information to the LLM input. BERT rises from 82.02 ± 1.09 to 85.90 ± 1.86; the article states action information improves "all MLM models significantly", with XLM-RoBERTa's "largest improvement of 6.5%". No standardized effect size is printed.

> "We observe that introducing action in formation improves the performance of all MLM models signiﬁcantly. XLM-RoBE RTa, in particular, has the largest improvement of 6.5%."

## Discussion


## Related Claims
- [Among tested LLMs, only BERT beats the baseline; GPT-2, MathBERT and XLM-RoBERTa underperform both baselines](only-bert-beats-error-classification-baseline.md) — reports the opposite
- [Adding tutor interface and skill-estimate context to the prompt substantially improves GPT-4's error-diagnosis accuracy](prompt-context-improves-gpt4-error-diagnosis.md) — related
- [Including the textbook source text in the model input improves automated summary scoring accuracy, with Longformer explaining 82% of Content and 70% of Wording score variance versus 67% and 41% for summary-only RoBERTa](longformer-source-text-outperforms-roberta-summary-scoring.md) — a broader claim this one bears on
- [Domain adaptation on PEMDAS data yields no significant change in overall error classification accuracy](domain-adaptation-no-accuracy-change.md) — related
