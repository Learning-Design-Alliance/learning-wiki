---
type: claim
title: Under a matched 2,300-sample SFT budget, K12-Train-Text outperforms eight mainstream instruction-tuning corpora on GaokaoBench and EduEval across two base models
description: Under a matched 2,300-sample SFT budget, K12-Train-Text outperforms eight mainstream instruction-tuning corpora on GaokaoBench and EduEval across two base models
id: k12-train-text-outperforms-instruction-corpora
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: hao-liang-2026
    resource: "https://arxiv.org/abs/2605.09635"
    title: "Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang. (2026). K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs. arXiv preprint. https://arxiv.org/abs/2605.09635"
    author: Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: hao-liang-2026-2
    resource: "https://arxiv.org/abs/2605.09635"
    title: "Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang. (2026). K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs. arXiv preprint. https://arxiv.org/abs/2605.09635"
    author: Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Under a matched 2,300-sample SFT budget, K12-Train-Text outperforms eight mainstream instruction-tuning corpora on GaokaoBench and EduEval across two base models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` On Qwen3-4B-Base, K12-Train-Text achieves the highest GaokaoBench total (1009.96), improving over the strongest baseline DataFlow (985.91) by +24.1; on Llama3.1-8B-Base it again obtains the highest total (625.49), outperforming WizardLM (593.08) by +32.4. [→ Hao Liang 2026](#hao-liang-2026)
`q2 i?` On EduEval, K12-Train-Text achieves the best average score on both backbones (66.76 on Qwen3-4B-Base; 40.90 on Llama3.1-8B-Base) under the same 2,300-sample budget. [→ Hao Liang 2026 (2)](#hao-liang-2026-2)

## Evidence

### Hao Liang 2026

Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang. (2026). K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs. arXiv preprint. https://arxiv.org/abs/2605.09635

`q2 · i?` · `causal · r2`

Full-parameter SFT of Qwen3-4B-Base and Llama3.1-8B-Base on K12-Train-Text and eight general instruction-tuning datasets, all matched to approximately 2,300 samples with identical hyperparameters, evaluated on GaokaoBench (Table 4). The article reports the highest totals for K12-Train-Text on both backbones.

> "On Qwen3-4B-Base, K12-Train-Text achieves the highest overall total (1009.96), improving over the strongest baseline DataFlow (985.91) by +24.1, while also reaching the best objective score rate (81.8%) and subjective score rate (89.5%)."

### Hao Liang 2026 (2)

Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang. (2026). K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs. arXiv preprint. https://arxiv.org/abs/2605.09635

`q2 · i?` · `causal · r2`

Evaluation of the same SFT models on 18 EduEval sub-tasks across five capability dimensions (Table 5). The article reports K12-Train-Text reaching the best average on both backbones, though "the overall gains are smaller than on GaokaoBench, they remain consistent across both base models."

> "On Qwen3-4B-Base, K12-Train-Text achieves the best average score (66.76) among all 2,300-sample SFT configurations, surpassing the strongest baseline WizardLM (66.70) while delivering the strongest Ethics results overall."

## Discussion


## Related Claims
- [SFT on K12-Train improves out-of-domain subjects (Chinese, Humanities Math), suggesting acquisition of a transferable structurally-grounded answer style](k12-train-cross-subject-transfer.md) — related
- [K12-Train-Full achieves the best overall performance on three multimodal educational benchmarks, and textual and visual supervision are complementary](k12-train-full-multimodal-complementarity.md) — related
