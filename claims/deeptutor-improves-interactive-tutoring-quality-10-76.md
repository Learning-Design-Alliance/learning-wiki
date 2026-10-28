---
type: claim
title: "DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench"
description: "DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench"
id: deeptutor-improves-interactive-tutoring-quality-10-76
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: bingxi-zhao-2026
    resource: "https://doi.org/10.48550/arxiv.2604.26962"
    title: "Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962 [doi:10.48550/arxiv.2604.26962](https://doi.org/10.48550/arxiv.2604.26962)"
    author: Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On TutorBench's first-person interactive evaluation, DeepTutor improves overall quality by 10.76% relative to the Naive Tutor baseline and leads on nearly all of ten metrics. [→ Bingxi Zhao 2026](#bingxi-zhao-2026)

## Evidence

### Bingxi Zhao 2026

Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962 [doi:10.48550/arxiv.2604.26962](https://doi.org/10.48550/arxiv.2604.26962)

`q2 · i?` · `design · r2`

LLM-simulated interactive evaluation of DeepTutor versus four baselines (Naive, CoT, Self-Refine, ReAct) sharing the same backbone and RAG, over the full TutorBench release of 270 tasks. The article reports DeepTutor "improves overall quality by 10.76% and leads on nearly all metrics"; relative gain is not a standardized effect size.

> "The four baselines remain tightly clustered, indicating that adding CoT, self-refinement, or ReAct-style tool use to the same backbone and RAG interface is not sufficient to matchDeepTutor's learner-adaptive behavior.DeepTutor improves overall quality by 10.76% and leads on nearly all metrics."

## Discussion


## Related Claims
- [DeepTutor's interactive tutoring gains are stable across five university-level domains, varying only 0.16 points in overall quality](deeptutor-gains-stable-across-five-domains.md) — related
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — related
- [Tutoring quality belongs to the base model and agent harness together rather than either alone, as adapter rankings reorder across tiers](educlaw-bench-model-harness-interaction.md) — related
- [TACTutor shows no degradation relative to its Qwen backbone on external educational benchmarks, with scores rising on MRBench, TutorBench, LongTutor, and DeepTutor](tactutor-no-degradation-external-benchmarks.md) — related
- [Teacher-agent comparisons show backbone-dependent patterns consistent with ZPD-informed adaptation](teacher-agent-backbone-dependent-zpd-patterns.md) — related
- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](omniedu-tuning-improves-all-three-educational-capability-groups.md) — related
- [Automated metrics and LLM judges can misalign with expert human preferences in non-verifiable educational evaluation](non-verifiability-crisis-llm-judges-misalign.md) — related
- [Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation](skg-dpm-complementary-ablation-deeptutor.md) — related
- [In a blinded study with 50 learners, TACTutor receives the highest overall mean rating (5.54/7) and is rated above its backbone across all four teaching-behavior dimensions (+0.39 overall)](tactutor-highest-blinded-learner-rating-5-54.md) — related
- [DeepTutor's macro-adaptive learning-progressions selection produced 0.79 σ pretest-posttest gains in a small evaluation, versus very little learning without dynamic dialog selection](deeptutor-macro-adaptivity-gains.md) — related
