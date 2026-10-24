---
type: claim
title: "Current LLMs lack robust curriculum cognition: even the best model reaches only 57.1% exact match on K12-Bench, with prerequisite and neighbor tasks hardest"
description: "Current LLMs lack robust curriculum cognition: even the best model reaches only 57.1% exact match on K12-Bench, with prerequisite and neighbor tasks hardest"
id: llms-lack-curriculum-cognition-k12-bench
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Current LLMs lack robust curriculum cognition: even the best model reaches only 57.1% exact match on K12-Bench, with prerequisite and neighbor tasks hardest

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On K12-Bench, the best overall exact match is 57.1% (Gemini-3-Flash) and a strong open-source model (Gemma-4-31B-IT) reaches 46.4%, with Prereq and Neighbor yielding the lowest EM across almost every model. [→ Hao Liang 2026](#hao-liang-2026)

## Evidence

### Hao Liang 2026

Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang. (2026). K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs. arXiv preprint. https://arxiv.org/abs/2605.09635 [doi:10.48550/arxiv.2605.09635](https://doi.org/10.48550/arxiv.2605.09635)

`q2 · i?` · `design · r2`

Zero-shot, answer-only evaluation of five open-source LLMs and five proprietary APIs on K12-Bench, reporting per-task exact match and instance-level macro F1 (Table 3). The article reports "The best overall exact match is only 57.1%" for Gemini-3-Flash and 46.4% for Gemma-4-31B-IT. LLaMA-3-8B-Instruct (EM 7.2%) was essentially indistinguishable from random guessing (EM 6.7%).

> "The best overall exact match is only 57.1% (Gemini-3-Flash); a strong open-source model (Gemma-4-31B-IT) reaches just 46.4%. In more than half the questions, models fail to identify the complete correct answer set."

## Discussion


## Related Claims
- [K12-Train-Full achieves the best overall performance on three multimodal educational benchmarks, and textual and visual supervision are complementary](k12-train-full-multimodal-complementarity.md) — related
- [OmniEdu-27B achieves the best overall curriculum-grounding performance among evaluated models, raising K12-Bench EM from 52.11% to 63.12%](omniedu-27b-best-curriculum-grounding-k12-bench.md) — reports the opposite
- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](omniedu-tuning-improves-all-three-educational-capability-groups.md) — related
