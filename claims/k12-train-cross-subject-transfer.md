---
type: claim
title: SFT on K12-Train improves out-of-domain subjects (Chinese, Humanities Math), suggesting acquisition of a transferable structurally-grounded answer style
description: SFT on K12-Train improves out-of-domain subjects (Chinese, Humanities Math), suggesting acquisition of a transferable structurally-grounded answer style
id: k12-train-cross-subject-transfer
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: hao-liang-2026
    resource: "https://doi.org/10.48550/arxiv.2605.09635"
    title: "Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang. (2026). K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs. arXiv preprint. https://arxiv.org/abs/2605.09635 [doi:10.48550/arxiv.2605.09635](https://doi.org/10.48550/arxiv.2605.09635)"
    author: Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SFT on K12-Train improves out-of-domain subjects (Chinese, Humanities Math), suggesting acquisition of a transferable structurally-grounded answer style

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Although K12-Train is synthesized only from mathematics, physics, chemistry, and biology subgraphs, SFT on it attains the highest Chinese score (120.18, +3.33 over DataFlow) and the best Humanities Math score (132.00, +4.08 over DataFlow). [→ Hao Liang 2026](#hao-liang-2026)

## Evidence

### Hao Liang 2026

Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang. (2026). K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs. arXiv preprint. https://arxiv.org/abs/2605.09635 [doi:10.48550/arxiv.2605.09635](https://doi.org/10.48550/arxiv.2605.09635)

`q2 · i?` · `design · r2`

Cross-subject analysis of GaokaoBench per-subject scores (Table 4) for models trained on K12-Train-Text. The article argues that since these subjects receive no in-domain supervision, the improvement reflects acquisition of a transferable, structurally-grounded answer style rather than content memorization.

> "SFT on K12-Train also attains the highest Chinese score (120.18,+3.33over the strongest baseline DataFlow) and the best Humanities Math score (132.00,+4 .08over DataFlow)"

## Discussion


## Related Claims
- [Under a matched 2,300-sample SFT budget, K12-Train-Text outperforms eight mainstream instruction-tuning corpora on GaokaoBench and EduEval across two base models](k12-train-text-outperforms-instruction-corpora.md) — related
- [K12-Train-Full achieves the best overall performance on three multimodal educational benchmarks, and textual and visual supervision are complementary](k12-train-full-multimodal-complementarity.md) — related
- [LLM teaching effectiveness varies substantially across subject domains, strongest where knowledge points apply directly and weakest in physics and chemistry](llm-teaching-effectiveness-varies-by-domain.md) — related
- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](omniedu-tuning-improves-all-three-educational-capability-groups.md) — a broader claim this one bears on
