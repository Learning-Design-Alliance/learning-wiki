---
type: claim
title: Dialogue-based RL training on mathematics tutoring dialogues generalizes to unseen educational benchmarks while largely preserving factual knowledge
description: Dialogue-based RL training on mathematics tutoring dialogues generalizes to unseen educational benchmarks while largely preserving factual knowledge
id: dialogue-rl-out-of-distribution-generalization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: unggi-lee-2026
    resource: "https://doi.org/10.48550/arXiv.2601.14560"
    title: "Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee. (2026). Rewarding How Models Think Pedagogically: Integrating Pedagogical Reasoning and Thinking Rewards for LLMs in Education. arXiv. [doi:10.48550/arXiv.2601.14560](https://doi.org/10.48550/arXiv.2601.14560)"
    author: Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: unggi-lee-2026-2
    resource: "https://doi.org/10.48550/arXiv.2601.14560"
    title: "Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee. (2026). Rewarding How Models Think Pedagogically: Integrating Pedagogical Reasoning and Thinking Rewards for LLMs in Education. arXiv. [doi:10.48550/arXiv.2601.14560](https://doi.org/10.48550/arXiv.2601.14560)"
    author: Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Dialogue-based RL training on mathematics tutoring dialogues generalizes to unseen educational benchmarks while largely preserving factual knowledge

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` RL-trained models improved on WBEB pedagogical knowledge (+4.9 to +8.4%p), essay scoring (+12.9 to +14.8%p), and decision making (+37.3 to +38.6%p) despite training only on math tutoring dialogues. [→ Unggi Lee 2026](#unggi-lee-2026)
`q2 i?` Subject knowledge degradation stayed within 1.5 percentage points across conditions, indicating the base model's factual knowledge was largely preserved. [→ Unggi Lee 2026 (2)](#unggi-lee-2026-2)

## Evidence

### Unggi Lee 2026

Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee. (2026). Rewarding How Models Think Pedagogically: Integrating Pedagogical Reasoning and Thinking Rewards for LLMs in Education. arXiv. [doi:10.48550/arXiv.2601.14560](https://doi.org/10.48550/arXiv.2601.14560)

`q2 · i?` · `causal · r2`

Evaluation on the Well-balanced Educational Benchmark (WBEB), which was not included in training data; the article reports accuracy gains in percentage points across the RL-trained conditions. No standardized effect size is printed.

> "all RL-trained models show substantial improvements in pedagogical knowledge (+4.9 to +8.4%p), essay scoring (+12.9 to +14.8%p), and decision making (+37.3 to +38.6%p)."

### Unggi Lee 2026 (2)

Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee. (2026). Rewarding How Models Think Pedagogically: Integrating Pedagogical Reasoning and Thinking Rewards for LLMs in Education. arXiv. [doi:10.48550/arXiv.2601.14560](https://doi.org/10.48550/arXiv.2601.14560)

`q2 · i?` · `causal · r1`

WBEB subject-knowledge accuracy comparison between the original Qwen3-8B and the RL-trained models; the article reports degradation "within 1.5 percentage points". Knowledge tracing was excluded because all models achieved AUC near 0.5.

> "Although subject knowledge slightly decreases across all conditions, the degradation remains within 1.5 percentage points, indicating that the base model's factual knowledge is largely preserved during dialogue-based RL training."

## Discussion


## Related Claims
- [Disability-aware training does not degrade out-of-domain educational knowledge on OpenLearnLM](sped-training-no-ood-knowledge-cost.md) — related
- [Fine-tuning frontier LLMs on authentic tutoring data improves performance on all six conversational and pedagogical benchmarks, moving values toward human-tutor levels](fine-tuning-authentic-data-improves-pedagogical-benchmarks.md) — related
