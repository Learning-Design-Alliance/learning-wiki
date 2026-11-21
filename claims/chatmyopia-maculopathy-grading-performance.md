---
type: claim
title: The ChatMyopia image classification tool graded myopic maculopathy with high test-set performance (overall AUROC 0.967, accuracy 0.934)
description: The ChatMyopia image classification tool graded myopic maculopathy with high test-set performance (overall AUROC 0.967, accuracy 0.934)
id: chatmyopia-maculopathy-grading-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: wu-y-2025
    resource: "https://doi.org/10.1016/j.isci.2025.113768"
    title: "Wu Y, Chen X, Zhang W, Liu S, Sum WMR, Wu X, Shang X, Kee C, He M, Shi D. (2025). ChatMyopia: An AI Agent for Pre-consultation Education in Primary Eye Care Settings. [doi:10.1016/j.isci.2025.113768](https://doi.org/10.1016/j.isci.2025.113768)"
    author: Wu Y, Chen X, Zhang W, Liu S, Sum WMR, Wu X, Shang X, Kee C, He M, Shi D.
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# The ChatMyopia image classification tool graded myopic maculopathy with high test-set performance (overall AUROC 0.967, accuracy 0.934)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` On the held-out test set, the myopic maculopathy grading model achieved overall AUROC 0.967, accuracy 0.934, sensitivity 0.830, and specificity 0.958. [→ Wu Y 2025](#wu-y-2025)

## Evidence

### Wu Y 2025

Wu Y, Chen X, Zhang W, Liu S, Sum WMR, Wu X, Shang X, Kee C, He M, Shi D. (2025). ChatMyopia: An AI Agent for Pre-consultation Education in Primary Eye Care Settings. [doi:10.1016/j.isci.2025.113768](https://doi.org/10.1016/j.isci.2025.113768)

`q3 · i?` · `causal · r2`

Evaluation of a ViT-large model fine-tuned on 2,769 fundus images (MMAC, HPMI, and a private dataset, split 8:1:1) on the test set, reported in Table 1. The quote prints the overall metrics; per-condition metrics appear in Table 1.

> "The overall AUROC was 0.967, with an accuracy of 0.934 , sensitivity of 0.830, and specificity of 0.958 ."

## Discussion


## Related Claims
- [An LLM-based question-specificity classifier reached .830 knowledge and .829 scaffold accuracy without fine-tuning](question-specificity-classifier-accuracy.md) — related
