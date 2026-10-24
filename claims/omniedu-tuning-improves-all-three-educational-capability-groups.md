---
type: claim
title: Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale
description: Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale
id: omniedu-tuning-improves-all-three-educational-capability-groups
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
sources:
  - id: hao-liang-2026
    resource: "https://doi.org/10.48550/arxiv.2609.23088"
    title: "Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088 [doi:10.48550/arxiv.2609.23088](https://doi.org/10.48550/arxiv.2609.23088)"
    author: Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q2 i?` Across all three curriculum benchmarks, education-oriented tuning consistently improves performance at every model scale (4B, 9B, 27B). [→ Hao Liang 2026](#hao-liang-2026)
`q2 i?` Across all three K-12 problem-solving benchmarks, each tuned model outperforms its corresponding base model on the overall metric. [→ Hao Liang 2026](#hao-liang-2026)
`q2 i?` Across all three tutoring benchmarks, education-oriented tuning improves pedagogical performance at every model scale. [→ Hao Liang 2026](#hao-liang-2026)

## Evidence

### Hao Liang 2026

Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088 [doi:10.48550/arxiv.2609.23088](https://doi.org/10.48550/arxiv.2609.23088)

`q2 · i?` · `design · r2`

Benchmark evaluation of fine-tuned OmniEdu-4B/9B/27B against the models they were tuned from (Qwen3.5-4B-Base, Qwen3.5-9B-Base and Qwen3.8-27B) and open-weight educational and proprietary baselines. The article's overall-findings section states that "education-oriented tuning consistently improves performance at every model scale" across K12-Bench, MathFish, and EDUMATH.

> "Across all three curriculum benchmarks, education-oriented tuning consistently improves performance at every model scale."

## Discussion


## Related Claims
- [OmniEdu-27B achieves the best overall curriculum-grounding performance among evaluated models, raising K12-Bench EM from 52.11% to 63.12%](omniedu-27b-best-curriculum-grounding-k12-bench.md) — a narrower finding that bears on this claim
- [Specializing models for K-12 education does not require a broad loss of general capability, with MMMU-Pro accuracy increasing at all three scales](omniedu-general-capability-retained-after-specialization.md) — a narrower finding that bears on this claim
- [Education-oriented tuning improves authentic K-12 problem solving, with OmniEdu-27B's MDK12-Bench open-question correctness rising from 62.08% to 78.77%](omniedu-k12-problem-solving-gains.md) — a narrower finding that bears on this claim
- [Education-oriented tuning produces the largest gains in scaffolded instruction and use of longitudinal student evidence, with LongTutor Evidence averages rising sharply at all scales](omniedu-largest-gains-scaffolding-longitudinal-evidence.md) — a narrower finding that bears on this claim
- [LoRA adaptation significantly increases closed-book accuracy on the PhysicsMate test set at all three Qwen3 scales](lora-adaptation-raises-bengali-physics-qa-accuracy-all-scales.md) — related
- [Under a matched 2,300-sample SFT budget, K12-Train-Text outperforms eight mainstream instruction-tuning corpora on GaokaoBench and EduEval across two base models](k12-train-text-outperforms-instruction-corpora.md) — related
- [Model family and instruction-tuning approach appear better predictors of tutoring quality than parameter count alone](model-family-beats-parameter-count-for-tutoring-quality.md) — related
- [Model scale does not consistently improve pedagogical safety: within the Qwen2.5 family the 72B model beats the 7B on only 17 of 33 subject-dimension pairs](llm-scale-does-not-predict-tutor-safety.md) — related
- [TACTutor shows no degradation relative to its Qwen backbone on external educational benchmarks, with scores rising on MRBench, TutorBench, LongTutor, and DeepTutor](tactutor-no-degradation-external-benchmarks.md) — related
- [Fine-tuning frontier LLMs on authentic tutoring data improves performance on all six conversational and pedagogical benchmarks, moving values toward human-tutor levels](fine-tuning-authentic-data-improves-pedagogical-benchmarks.md) — related
- [K12-Train-Full achieves the best overall performance on three multimodal educational benchmarks, and textual and visual supervision are complementary](k12-train-full-multimodal-complementarity.md) — related
- [SFT on K12-Train improves out-of-domain subjects (Chinese, Humanities Math), suggesting acquisition of a transferable structurally-grounded answer style](k12-train-cross-subject-transfer.md) — a narrower finding that bears on this claim
- [IKS-Instruct fine-tuning is necessary for IKS pedagogical capability: a compact 7B fine-tune reaches a median judge score of 6.39, within 0.15 of a general-purpose reference, while the base model scores near zero on IKS-specific dimensions](iks-instruct-finetuning-necessary-for-iks-pedagogical-capability.md) — a narrower finding that bears on this claim
- [Task-specific fine-tuning substantially improves open-source LLMs on MedGame Bench and narrows the gap with commercial models](fine-tuning-improves-open-source-llms-medgame-bench.md) — a narrower finding that bears on this claim
- [Current LLMs lack robust curriculum cognition: even the best model reaches only 57.1% exact match on K12-Bench, with prerequisite and neighbor tasks hardest](llms-lack-curriculum-cognition-k12-bench.md) — related
- [DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench](deeptutor-improves-interactive-tutoring-quality-10-76.md) — related
