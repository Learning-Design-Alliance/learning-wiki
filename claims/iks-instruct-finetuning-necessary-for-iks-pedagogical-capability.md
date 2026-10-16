---
type: claim
title: "IKS-Instruct fine-tuning is necessary for IKS pedagogical capability: a compact 7B fine-tune reaches a median judge score of 6.39, within 0.15 of a general-purpose reference, while the base model scores near zero on IKS-specific dimensions"
description: "IKS-Instruct fine-tuning is necessary for IKS pedagogical capability: a compact 7B fine-tune reaches a median judge score of 6.39, within 0.15 of a general-purpose reference, while the base model scores near zero on I..."
id: iks-instruct-finetuning-necessary-for-iks-pedagogical-capability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: shwetha-singaravelu-2026
    resource: "https://doi.org/10.48550/arxiv.2607.23322"
    title: "Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani. (2026). IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems. arXiv. https://arxiv.org/abs/2607.23322 [doi:10.48550/arxiv.2607.23322](https://doi.org/10.48550/arxiv.2607.23322)"
    author: Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# IKS-Instruct fine-tuning is necessary for IKS pedagogical capability: a compact 7B fine-tune reaches a median judge score of 6.39, within 0.15 of a general-purpose reference, while the base model scores near zero on IKS-specific dimensions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Under a uniform five-judge external panel, all IKS-Instruct fine-tuned 7B versions score in the 6.1 to 6.4 range, whereas the base model scores near zero on the IKS-specific dimensions. [→ Shwetha Singaravelu 2026](#shwetha-singaravelu-2026)

## Evidence

### Shwetha Singaravelu 2026

Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani. (2026). IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems. arXiv. https://arxiv.org/abs/2607.23322 [doi:10.48550/arxiv.2607.23322](https://doi.org/10.48550/arxiv.2607.23322)

`q2 · i?` · `design · r2`

Model comparison in Section 5.3 using a uniform five-judge external panel over 1,201 stratified items, with the base model evaluated only in an earlier small-scale pilot. The fine-tuned models score "in the 6.1 to 6.4 range" while the base model scores near zero on IKS-specific dimensions; no effect size is printed.

> "all fine-tuned versions score in the 6.1 to 6.4 range under the uniform external panel, whereas the base model (Airavata without IKS fine-tuning), evaluated in an earlier small-scale pilot, scores near zero on the IKS-specific dimensions"

## Discussion


## Related Claims
- Fine-tuning Llama2-7B with parameter-efficient methods yields unsatisfactory results for measuring subject-matter teaching practices, only marginally improving the majority baseline — related
- [Model-level judge quality is non-monotonic in dataset size: the 13,882-pair v1.1 yields the best model (6.39), while both expansion to ~20,000 pairs (6.33) and aggressive curation to 7,130 pairs (6.12) reduce quality](non-monotonic-quality-volume-iks-instruct.md) — related
