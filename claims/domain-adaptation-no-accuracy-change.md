---
type: claim
title: Domain adaptation on PEMDAS data yields no significant change in overall error classification accuracy
description: Domain adaptation on PEMDAS data yields no significant change in overall error classification accuracy
id: domain-adaptation-no-accuracy-change
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: mcnichols-2023
    resource: "https://doi.org/10.1007/978-3-031-36272-9_30"
    title: "McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. [doi:10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30)"
    author: "McNichols, H., Zhang, M., & Lan, A."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Domain adaptation on PEMDAS data yields no significant change in overall error classification accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adding 3 or 10 epochs of domain adaptation to BERT does not significantly change overall classification accuracy (82.02 vs 81.10 and 81.00). [→ McNichols 2023](#mcnichols-2023)

## Evidence

### McNichols 2023

McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. [doi:10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30)

`q2 · i?` · `causal · r2`

Domain adaptation (DA) experiments pre-train BERT for 3 or 10 epochs on the PEMDAS subset of the AMPS Mathematica dataset before task fine-tuning. Accuracies are 82.02 ± 1.09 (no DA), 81.10 ± 2.40 (3 epochs) and 81.00 ± 1.72 (10 epochs); the article reports "no significant change in overall accuracy". Equivalence was not formally tested.

> "We observ e no sig- niﬁcant change in overall accuracy with the introduction of either 3 or 10 epochs of DA."

## Discussion


## Related Claims
- [Adding ITS-recorded student action context to the input significantly improves MLM-based error classifiers, though GPT-2 declines slightly](action-context-improves-error-classification.md) — related
- [Explicitly encapsulating linguistic information together with word-level attention improves BloomNet's performance significantly over RoBERTa alone](linguistic-encapsulation-word-attention-improves-classification.md) — related
