---
type: claim
title: A ZPD-based curriculum prioritizing challenging yet learnable examples improves fine-tuning convergence and performance, consistent with shared learnability between ICL and fine-tuning
description: A ZPD-based curriculum prioritizing challenging yet learnable examples improves fine-tuning convergence and performance, consistent with shared learnability between ICL and fine-tuning
id: zpd-curriculum-improves-finetuning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: peng-cui-2025
    resource: "https://doi.org/10.18653/v1/2025.findings-naacl.362"
    title: "Peng Cui, Mrinmaya Sachan. (2025). Investigating the Zone of Proximal Development of Language Models for In-Context Learning. arXiv. [doi:10.18653/v1/2025.findings-naacl.362](https://doi.org/10.18653/v1/2025.findings-naacl.362)"
    author: Peng Cui, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# A ZPD-based curriculum prioritizing challenging yet learnable examples improves fine-tuning convergence and performance, consistent with shared learnability between ICL and fine-tuning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Fine-tuning LLaMA-3-8B-Instruct with the ZPD-based curriculum results in faster convergence and improved performance in most cases compared to a random baseline. [→ Peng Cui 2025](#peng-cui-2025)

## Evidence

### Peng Cui 2025

Peng Cui, Mrinmaya Sachan. (2025). Investigating the Zone of Proximal Development of Language Models for In-Context Learning. arXiv. [doi:10.18653/v1/2025.findings-naacl.362](https://doi.org/10.18653/v1/2025.findings-naacl.362)

`q2 · i?` · `causal · r1`

Fine-tuning experiment comparing the ZPD-based curriculum against a random baseline on LLaMA-3-8B-Instruct over 6 epochs on GSM8K and EZStance (Figure 6). The article reports the curriculum "results in faster convergence and improved performance in most cases".

> "As shown in Figure 6, our curriculum results in faster convergence and improved performance in most cases."

## Discussion


## Related Claims
- Early in fine-tuning, strategies exposing difficult examples (D2E, PME, PMD, SMD) show a clear accuracy advantage at the first checkpoint on SST-2 — related
- Selective ICL (SELICL), applying demonstrations only to predicted-ZPD queries, dominates full ICL for 6 of 8 LLaMA models on the accuracy-cost trade-off — related
- [A fine-tuned 8B model outperforms a zero-shot LLaMA-70B baseline on context-dependent components like Evidence and Conclusion, though the 70B excels on self-contained components like Position](fine-tuned-8b-outperforms-70b-on-context-dependent-components.md) — related
- Query difficulty under direct prompting and in-context learnability are not always aligned: positive Pearson correlations on GSM8K but negative correlations on EZStance — related
- [Sequential curriculum fine-tuning yields the strongest overall AES performance, achieving the highest or tied-for-highest F1 on Claim, Evidence, and Conclusion](sequential-curriculum-strongest-aes-performance.md) — related
- [ZPDs of different LLMs differ significantly: Z✗→✓ and Z✗→✗ examples overlap little across models while Z✓ examples are largely shared](zpd-overlap-low-across-models.md) — related
