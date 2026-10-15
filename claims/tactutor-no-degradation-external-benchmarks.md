---
type: claim
title: TACTutor shows no degradation relative to its Qwen backbone on external educational benchmarks, with scores rising on MRBench, TutorBench, LongTutor, and DeepTutor
description: TACTutor shows no degradation relative to its Qwen backbone on external educational benchmarks, with scores rising on MRBench, TutorBench, LongTutor, and DeepTutor
id: tactutor-no-degradation-external-benchmarks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: dongjie-yang-2026
    resource: "https://doi.org/10.48550/arxiv.2608.03952"
    title: "Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen. (2026). TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring. https://arxiv.org/abs/2608.03952 [doi:10.48550/arxiv.2608.03952](https://doi.org/10.48550/arxiv.2608.03952)"
    author: Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# TACTutor shows no degradation relative to its Qwen backbone on external educational benchmarks, with scores rising on MRBench, TutorBench, LongTutor, and DeepTutor

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On external transfer checks, TACTutor shows no degradation relative to the Qwen3.5-4B backbone: MRBench macroDAMR rises from 0.743 to 0.880, TutorBench weighted score from 0.497 to 0.519, LongTutor teaching quality from 3.712 to 3.834, and the DeepTutor smoke score from 3.565 to 3.627. [→ Dongjie Yang 2026](#dongjie-yang-2026)

## Evidence

### Dongjie Yang 2026

Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen. (2026). TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring. https://arxiv.org/abs/2608.03952 [doi:10.48550/arxiv.2608.03952](https://doi.org/10.48550/arxiv.2608.03952)

`q2 · i?` · `design · r2`

Transfer checks on external educational benchmarks covering math tutoring, STEM tutoring, long-history personalization, and interactive tutor simulation (Appendix Table 3). The article reports "no degradation relative to the corresponding Qwen baselines" with the printed score changes; no significance tests are reported.

> "TACTutor shows no degradation relative to the corre-sponding Qwen baselines: MRBench (Maurya et al. 2025) macroDAMRrisesfrom0.743to0.880,TutorBench(Srini-vasa et al. 2025) weighted score from 0.497 to 0.519, Long- Tutor (Li et al. 2026) teaching quality from 3.712 to 3.834, and the DeepTutor (Zhao et al. 2026) smoke score from 3.565 to 3.627."

## Discussion


## Related Claims
- [In a blinded study with 50 learners, TACTutor receives the highest overall mean rating (5.54/7) and is rated above its backbone across all four teaching-behavior dimensions (+0.39 overall)](tactutor-highest-blinded-learner-rating-5-54.md) — related
- [Education-oriented tuning produces the largest gains in scaffolded instruction and use of longitudinal student evidence, with LongTutor Evidence averages rising sharply at all scales](omniedu-largest-gains-scaffolding-longitudinal-evidence.md) — related
- [Taxonomy-guided post-training raises TACTutor's TACT_Overall on TACTBench from 0.629 (backbone) to 0.832, the highest among evaluated models](tactutor-raises-tactbench-overall-0-629-to-0-832.md) — related
- [Post-training improves TACTutor's auxiliary guardrail flags on TACTBench: accept rate rises from 0.603 to 0.872 and leak-or-overhelp falls from 0.346 to 0.026](tactutor-guardrail-flags-improve-accept-leak.md) — related
- [DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench](deeptutor-improves-interactive-tutoring-quality-10-76.md) — related
- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](omniedu-tuning-improves-all-three-educational-capability-groups.md) — related
