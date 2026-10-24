---
type: claim
title: Under the same teacher model, AgenticMath outperforms prior data-generation methods, indicating gains arise from framework design rather than teacher strength
description: Under the same teacher model, AgenticMath outperforms prior data-generation methods, indicating gains arise from framework design rather than teacher strength
id: agenticmath-gains-not-from-stronger-teacher
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: xianyang-liu-2025
    resource: "https://doi.org/10.48550/arxiv.2510.19361"
    title: "Xianyang Liu, Yilin Liu, Shuai Wang, Hao Cheng, Andrew Estornell, Yuzhi Zhao, Jun Shu, Jiaheng Wei. (2025). AgenticMath: Enhancing LLM Reasoning via Agentic-based Math Data Generation. arXiv preprint. https://arxiv.org/abs/2510.19361 [doi:10.48550/arxiv.2510.19361](https://doi.org/10.48550/arxiv.2510.19361)"
    author: Xianyang Liu, Yilin Liu, Shuai Wang, Hao Cheng, Andrew Estornell, Yuzhi Zhao, Jun Shu, Jiaheng Wei
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Under the same teacher model, AgenticMath outperforms prior data-generation methods, indicating gains arise from framework design rather than teacher strength

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In a 10K-sample controlled comparison using the same GPT-4o-mini teacher, AgenticMath achieves the highest average performance (31.6) versus MetaMath (26.9), DARTMath (29.9), and ScaleQuest (26.3). [→ Xianyang Liu 2025](#xianyang-liu-2025)

## Evidence

### Xianyang Liu 2025

Xianyang Liu, Yilin Liu, Shuai Wang, Hao Cheng, Andrew Estornell, Yuzhi Zhao, Jun Shu, Jiaheng Wei. (2025). AgenticMath: Enhancing LLM Reasoning via Agentic-based Math Data Generation. arXiv preprint. https://arxiv.org/abs/2510.19361 [doi:10.48550/arxiv.2510.19361](https://doi.org/10.48550/arxiv.2510.19361)

`q2 · i?` · `design · r2`

Controlled 10K-sample comparison (Table 5) across MetaMath, DARTMath, ScaleQuest, and AgenticMath, all trained under the same SFT configuration on Mistral-7B and using the same teacher model for solution generation; the text reports "AgenticMath achieves the highest av- erage performance among all methods."

> "As shown in Table 5, AgenticMath achieves the highest av- erage performance among all methods. This con- trolled experiment confirms that the observed im- provements do not arise from using a stronger teacher model"

## Discussion


## Related Claims
- [Each AgenticMath component contributes performance gains, with the review-revise loop playing a particularly important role](agenticmath-ablation-all-modules-contribute.md) — related
- [At 30K and 60K data scales, AgenticMath outperforms all compared baselines across four base models on six math benchmarks](agenticmath-sota-at-small-data-scales.md) — related
- [Increasing AgenticMath-generated training data from 7.5K to 22.5K samples yields consistent accuracy gains for Llama3-8B across benchmarks](agenticmath-data-size-positive-correlation-accuracy.md) — related
- [Review-revise iterations improve synthesized problem quality, with gains largely stabilizing by the third iteration](review-revise-iterations-quality-stabilizes.md) — related
