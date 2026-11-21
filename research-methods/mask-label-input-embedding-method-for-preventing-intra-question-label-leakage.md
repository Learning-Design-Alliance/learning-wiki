---
type: research-method
id: mask-label-input-embedding-method-for-preventing-intra-question-label-leakage
title: MASK label input-embedding method for preventing intra-question label leakage
description: The MASK label method adds a special mask label alongside binary response labels in the expanded KC interaction sequence.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# MASK label input-embedding method for preventing intra-question label leakage

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The MASK label method adds a special mask label alongside binary response labels in the expanded KC interaction sequence. The article states: "Any ground- truth response preceding another KC within the same question is replaced withMASK", so only the final KC of a question retains its ground-truth label. The MASK token is applied exclusively to input embeddings while output predictions remain constrained to labels 0 and 1, and it is applied during both training and inference, requiring no special-case handling. Labels are assigned once during sequence construction. Variants include DKT-ML, DKT-ML+, AKT-ML and SAKT-ML, with separate or combined KC-response embedding implementations.

## Accounts
<!-- How each source describes or uses the method -->
- **MASK label input-embedding method for preventing intra-question label leakage**: The MASK label method adds a special mask label alongside binary response labels in the expanded KC interaction sequence. The article states: "Any ground- truth response preceding another KC within the same question is replaced withMASK", so only the final KC of a question retains its ground-truth label. The MASK token is applied exclusively to input embeddings while output predictions remain constrained to labels 0 and 1, and it is applied during both training and inference, requiring no special-case handling. Labels are assigned once during sequence construction. Variants include DKT-ML, DKT-ML+, AKT-ML and SAKT-ML, with separate or combined KC-response embedding implementations. (Yahya Badran et al. (2025))

### Claims
- [The MASK label method outperforms alternative leakage-mitigation strategies across most KT benchmark datasets](../claims/mask-label-outperforms-mitigation-alternatives.md) [+M]

## Related Research Methods
-

## Key Sources
- Yahya Badran and Christine Preisach. (2025). Enhancing Knowledge Tracing through Leakage-Free and Recency-Aware Embeddings. https://arxiv.org/abs/2508.17092
