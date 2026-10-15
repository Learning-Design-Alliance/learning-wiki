---
type: claim
title: "Taxonomy-guided post-training raises TACTutor's TACT_Overall on TACTBench from 0.629 (backbone) to 0.832, the highest among evaluated models"
description: "Taxonomy-guided post-training raises TACTutor's TACT_Overall on TACTBench from 0.629 (backbone) to 0.832, the highest among evaluated models"
id: tactutor-raises-tactbench-overall-0-629-to-0-832
status: draft
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
  - id: dongjie-yang-2026-2
    resource: "https://arxiv.org/abs/2608.03952"
    title: "Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen. (2026). TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring. https://arxiv.org/abs/2608.03952"
    author: Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Taxonomy-guided post-training raises TACTutor's TACT_Overall on TACTBench from 0.629 (backbone) to 0.832, the highest among evaluated models

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` Post-training with SFT and taxonomy-grounded GRPO raises TACT_Overall from 0.629 for the Qwen3.5-4B backbone to 0.832 on the 78-context TACTBench diagnostic. [→ Dongjie Yang 2026](#dongjie-yang-2026)
`q2 i?` TACTutor achieves the highest Overall score among evaluated proprietary baselines despite using an open 4B backbone, with qwen3.7-max closest at 0.829. [→ Dongjie Yang 2026 (2)](#dongjie-yang-2026-2)

## Evidence

### Dongjie Yang 2026

Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen. (2026). TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring. https://arxiv.org/abs/2608.03952 [doi:10.48550/arxiv.2608.03952](https://doi.org/10.48550/arxiv.2608.03952)

`q2 · i?` · `design · r2`

Diagnostic evaluation on TACTBench under deployment-like inputs, judged with hidden references and rubric. The article reports that post-training "raisesTACT_Overallfrom0.629forthebackboneto0.832", with no effect size or significance test printed.

> "This post-training raisesTACT_Overallfrom0.629forthebackboneto0.832;the auxiliary flags also improve, with accept rate increasing from 0.603 to 0.872 and leak-or-overhelp falling from 0.346 to0.026."

### Dongjie Yang 2026 (2)

Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen. (2026). TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring. https://arxiv.org/abs/2608.03952

`q2 · i?` · `design · r2`

Comparison of judged TACTBench Overall scores across evaluated models. The article notes qwen3.7-max is "closest in Overall score (0.829)" while "TACTutor achieves the highest Overall score"; per-dimension leads by other models are reported descriptively.

> "Amongstrongleaderboardbaselines,qwen3.7-max is closest in Overall score (0.829), GLM-5.2 leads on Move and Tone, and GPT-5.5 leads on ESL; nevertheless, TACTutor achieves the highest Overall score despite using an open 4B backbone."

## Discussion


## Related Claims
- [Post-training improves TACTutor's auxiliary guardrail flags on TACTBench: accept rate rises from 0.603 to 0.872 and leak-or-overhelp falls from 0.346 to 0.026](tactutor-guardrail-flags-improve-accept-leak.md) — related
- [In a blinded study with 50 learners, TACTutor receives the highest overall mean rating (5.54/7) and is rated above its backbone across all four teaching-behavior dimensions (+0.39 overall)](tactutor-highest-blinded-learner-rating-5-54.md) — related
- [TACTutor shows no degradation relative to its Qwen backbone on external educational benchmarks, with scores rising on MRBench, TutorBench, LongTutor, and DeepTutor](tactutor-no-degradation-external-benchmarks.md) — related
- [GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall](grpo-sfs-reward-beats-dpo.md) — a broader claim this one bears on
- [Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)](sft-improves-selective-update-behavior.md) — a broader claim this one bears on
- [SFS-aligned post-training generalizes out-of-domain: models trained on one dataset retain substantial SFS gains on the other](sfs-post-training-cross-domain-generalization.md) — a broader claim this one bears on
