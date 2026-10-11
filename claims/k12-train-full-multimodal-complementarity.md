---
type: claim
title: K12-Train-Full achieves the best overall performance on three multimodal educational benchmarks, and textual and visual supervision are complementary
description: K12-Train-Full achieves the best overall performance on three multimodal educational benchmarks, and textual and visual supervision are complementary
id: k12-train-full-multimodal-complementarity
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
    kind: design
    rigour: 2
  - id: hao-liang-2026-2
    resource: "https://arxiv.org/abs/2605.09635"
    title: "Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang. (2026). K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs. arXiv preprint. https://arxiv.org/abs/2605.09635"
    author: Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# K12-Train-Full achieves the best overall performance on three multimodal educational benchmarks, and textual and visual supervision are complementary

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` K12-Train-Full achieves the best overall result on Gaokao-MM, MDK12-Bench, and K12Vista, consistently outperforming both Text-Only and MM-Only configurations, indicating the two supervision sources are complementary. [→ Hao Liang 2026](#hao-liang-2026)
`q2 i?` On K12Vista, K12-Train-Full is the only fine-tuned configuration that improves upon the untuned base model (79.95 vs. 79.72). [→ Hao Liang 2026 (2)](#hao-liang-2026-2)

## Evidence

### Hao Liang 2026

Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang. (2026). K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs. arXiv preprint. https://arxiv.org/abs/2605.09635

`q2 · i?` · `design · r2`

LoRA SFT of Qwen3.5-2B-Base on K12-Train-Full, K12-Train-Text, K12-Train-MM, and full DataFlow and WizardLM datasets, evaluated on Gaokao-MM, MDK12-Bench, and K12Vista (Tables 6-8). The article reports K12-Train-Full surpassing the full DataFlow and WizardLM baselines with a smaller sample size (7,335 vs. 10,000/142,759).

> "K12-Train-Full achieves the best overall result on all three multimodal benchmarks and consistently outperforms both Text Only and MM Only, indicating that the two supervision sources are complementary."

### Hao Liang 2026 (2)

Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang. (2026). K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs. arXiv preprint. https://arxiv.org/abs/2605.09635

`q2 · i?` · `design · r2`

K12Vista evaluation across five subjects and three question formats (Table 8), described as a rigorous test of capability retention since the untuned base model already scores 79.72. K12-Train-Full achieved the best results across multiple-choice, fill-in-the-blank, and open-ended QA formats.

> "K12-Train-Full is the only fine-tuned configuration that improves upon the base model, reaching the best average score of79.95."

## Discussion


## Related Claims
- [Epi2Diff achieves the best performance across all four item-difficulty test sets and all reported metrics, outperforming SLM fine-tuning, LLM prompting, and supervised LLM adaptation baselines](epi2diff-best-across-four-difficulty-benchmarks.md) — related
- [SFT on K12-Train improves out-of-domain subjects (Chinese, Humanities Math), suggesting acquisition of a transferable structurally-grounded answer style](k12-train-cross-subject-transfer.md) — related
- [Under a matched 2,300-sample SFT budget, K12-Train-Text outperforms eight mainstream instruction-tuning corpora on GaokaoBench and EduEval across two base models](k12-train-text-outperforms-instruction-corpora.md) — related
- [Current LLMs lack robust curriculum cognition: even the best model reaches only 57.1% exact match on K12-Bench, with prerequisite and neighbor tasks hardest](llms-lack-curriculum-cognition-k12-bench.md) — related
