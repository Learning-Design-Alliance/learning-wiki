---
type: claim
title: Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS
description: Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS
id: adaptive-icap-scaffolding-improves-posttest-logic-tutor
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: tithi-2026
    resource: "https://doi.org/10.48550/arxiv.2602.07308"
    title: "Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308 [doi:10.48550/arxiv.2602.07308](https://doi.org/10.48550/arxiv.2602.07308)"
    author: Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T.
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` Both adaptive conditions (BKT and DRL) significantly outperformed the Control condition on posttest score, with comparable effect sizes. [→ Tithi 2026](#tithi-2026)

## Evidence

### Tithi 2026

Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308 [doi:10.48550/arxiv.2602.07308](https://doi.org/10.48550/arxiv.2602.07308)

`q3 · i?` · `causal · r2`

Controlled between-subjects classroom study (N=113 undergraduates in a discrete math course) comparing Control, BKT, and DRL scaffolding conditions with stratified random assignment after pretest. A mixed-effect regression with problem ID as random intercept found a significant condition-posttest association (p <0.001); "both adaptive conditions significantly outperformed theControl" with A=.58 for BKT and A=.58 (p=.002) for DRL.

> "As shown in Table 2, both adaptive conditions significantly outperformed theControl(mean = 65.7) on posttest score. TheBKTgroup (mean= 72.3) showed significant improvement overControl(A=.58, 95% CI [.52, .63],p=.005)"

## Studies bearing on this claim

<!-- synthesis:start -->
*Does choosing practice or scaffolding by BKT's mastery estimate improve learning or reduce the practice needed, compared with fixed or random sequencing, and for whom?* This table gathers the studies behind this claim and the 8 narrower claims that bear on it: **3 distinct studies** (2 causal, 1 review), `q2`–`q3`, 0 of 3 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Tithi 2026](https://doi.org/10.48550/arxiv.2602.07308) | q3 · causal · r2 | i? | this claim; [BKT scaffolding significantly benefits low prior knowledge students, who outperformed low ](bkt-benefits-low-prior-knowledge-students.md) (supports); [All training policies narrowed the prior-knowledge achievement gap from pretest to posttes](bkt-largest-achievement-gap-reduction.md) (supports); [BKT students completed posttest problems significantly faster than Control students, with ](bkt-faster-posttest-completion.md) (supports); [DRL scaffolding significantly benefits high prior knowledge students while BKT does not, a](drl-benefits-high-prior-knowledge-students.md) (qualifies) |
| [Shuanghong Shen 2021](https://doi.org/10.48550/arxiv.2105.15106) | q2 · review · r2 | i? | [The survey reports, citing Lee and Brunskill, that individualized BKT in an intelligent tu](individualized-bkt-reduces-questions-needed-for-mastery.md) (supports); [The survey reports, citing Desmarais and Baker, that students using the BKT-sequence recom](bkt-sequence-recommendation-students-solved-harder-exercises.md) (supports) |
| eff-1 | q2 · causal · r1 | i? | [BKT is the most efficient knowledge tracing approach overall in simulated online mastery l](bkt-most-efficient-online-mastery-learning.md) (supports); [In simulated online mastery learning, BKT gave the fewest problems, Streak the second fewe](problem-counts-by-knowledge-tracing-condition.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [DRL scaffolding significantly benefits high prior knowledge students while BKT does not, and condition-by-prior-knowledge interactions are not significant](drl-benefits-high-prior-knowledge-students.md) — a narrower finding that bears on this claim
- [BKT scaffolding significantly benefits low prior knowledge students, who outperformed low prior knowledge controls](bkt-benefits-low-prior-knowledge-students.md) — a narrower finding that bears on this claim
- [No significant differences in posttest rule accuracy across scaffolding conditions](no-rule-accuracy-difference-across-conditions.md) — related
- [BKT students completed posttest problems significantly faster than Control students, with DRL showing marginal advantages in time and solution optimality](bkt-faster-posttest-completion.md) — related
- [The DRL policy produced a significantly different scaffolding distribution than Control and BKT, favoring Guided examples (60%) and avoiding Buggy examples (4%)](drl-policy-favors-guided-examples-distribution.md) — related
- [All training policies narrowed the prior-knowledge achievement gap from pretest to posttest, with BKT achieving the largest reduction (77.1%)](bkt-largest-achievement-gap-reduction.md) — related
- [Intelligent tutoring systems improve achievement over non-individualised instruction](adaptive-learning-improves-outcomes.md) — a broader claim this one bears on
- Students receiving Adaptive proactive hints based on HelpNeed predictions achieve significantly higher posttest optimality than Control students — related
- [Structured GenAI scaffolding training raises sophomore STEM students' posttest CSEM electromagnetism scores over problem-solving training (d = 0.81)](genai-scaffolding-training-improves-revision-performance.md) — related
- [Adaptive task difficulty in an ITS did not improve second-graders' mathematics posttest performance compared with an identical non-adaptive ITS](task-difficulty-adaptation-no-learning-benefit-second-grade.md) — reports the opposite
- [Teacher-judged logical reasoning combined with prior knowledge to predict learning only under the control condition; scaffolding almost fully diminished the disadvantage of lower logical reasoning](scaffolds-diminish-logical-reasoning-disadvantage.md) — related
