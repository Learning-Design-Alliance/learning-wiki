---
type: claim
title: Sequentially fine-tuned models dramatically outperform independently fine-tuned models on scoring conclusions, implying conclusions require contextual representations from other essay parts
description: Sequentially fine-tuned models dramatically outperform independently fine-tuned models on scoring conclusions, implying conclusions require contextual representations from other essay parts
id: sequential-beats-independent-on-conclusion
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ali-keramati-and-mark-warschauer-2026
    resource: "https://doi.org/10.48550/arXiv.2606.10327"
    title: "Ali Keramati and Mark Warschauer. (2026). The Order Matters: Sequential Fine-Tuning of LLaMA for Coherent Automated Essay Scoring. Published as a conference paper at ICLR 2026. [doi:10.48550/arXiv.2606.10327](https://doi.org/10.48550/arXiv.2606.10327)"
    author: Ali Keramati and Mark Warschauer
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Sequentially fine-tuned models dramatically outperform independently fine-tuned models on scoring conclusions, implying conclusions require contextual representations from other essay parts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the Conclusion component, the Sequential model reaches 87% F1 while the Independent model fails at 12% F1, suggesting conclusion evaluation depends on representations informed by other essay parts. [→ Ali Keramati and Mark Warschauer 2026](#ali-keramati-and-mark-warschauer-2026)

## Evidence

### Ali Keramati and Mark Warschauer 2026

Ali Keramati and Mark Warschauer. (2026). The Order Matters: Sequential Fine-Tuning of LLaMA for Coherent Automated Essay Scoring. Published as a conference paper at ICLR 2026. [doi:10.48550/arXiv.2606.10327](https://doi.org/10.48550/arXiv.2606.10327)

`q2 · i?` · `causal · r1`

Comparison of the Sequential and Independent fine-tuning conditions on the Conclusion task in the PERSUADE 2.0 experiments (Section 5.2, finding 3). The Sequential model reached 87% F1 while the Independent model "catastrophically fails (12% F1)".

> "While theSequentialmodel excels (87% F1), theIndependentmodel catastrophically fails (12% F1). This divergence strongly implies that evaluating a conclusion effectively requires contex- tual representations informed by other parts of the essay."

## Discussion


## Related Claims
- [Sequential curriculum fine-tuning yields the strongest overall AES performance, achieving the highest or tied-for-highest F1 on Claim, Evidence, and Conclusion](sequential-curriculum-strongest-aes-performance.md) — possibly the same claim (merge candidate)
- [A fine-tuned 8B model outperforms a zero-shot LLaMA-70B baseline on context-dependent components like Evidence and Conclusion, though the 70B excels on self-contained components like Position](fine-tuned-8b-outperforms-70b-on-context-dependent-components.md) — related
