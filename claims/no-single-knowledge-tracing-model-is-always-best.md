---
type: claim
title: The survey reports, citing Pavlik et al., that no single knowledge tracing model was always the best, and that a better model must consider multiple student features and the learning context.
description: The survey reports, citing Pavlik et al., that no single knowledge tracing model was always the best, and that a better model must consider multiple student features and the learning context.
id: no-single-knowledge-tracing-model-is-always-best
status: review
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: weak
sources:
  - id: shuanghong-shen-2021
    resource: "https://doi.org/10.48550/arxiv.2105.15106"
    title: "Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106 [doi:10.48550/arxiv.2105.15106](https://doi.org/10.48550/arxiv.2105.15106)"
    author: Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen
    q: 2
    i: "?"
    kind: review
    rigour: "?"
---

# The survey reports, citing Pavlik et al., that no single knowledge tracing model was always the best, and that a better model must consider multiple student features and the learning context.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r?` · `q2`

## Subclaims
`q2 i?` The review attributes to Pavlik et al. an empirical verification that no single KT model was always best. [→ Shuanghong Shen 2021](#shuanghong-shen-2021)

## Evidence

### Shuanghong Shen 2021

Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106 [doi:10.48550/arxiv.2105.15106](https://doi.org/10.48550/arxiv.2105.15106)

`q2 · i?` · `review · r?`

Narrative review citing Pavlik et al.; the survey reports they "empirically verified that no single KT model was always the best". The survey uses this to justify not comparing model performance across datasets collected with various settings, subjects, learning stages and scales.

> "Pavlik et al. [34] have also empirically verified that no single KT model was always the best, a specific better model must consider multiple student features and the learning context."

## Studies bearing on this claim

<!-- synthesis:start -->
*Does extending a knowledge-tracing model with individual parameters, engagement signals, forgetting or other side information improve how well it predicts learners' answers?* This table gathers the studies behind this claim and the 11 narrower claims that bear on it: **5 distinct studies** (3 design, 1 review, 1 associational), `q1`–`q3`, 0 of 5 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Shuanghong Shen 2021](https://doi.org/10.48550/arxiv.2105.15106) | q2 · review · r? | i? | this claim; [The survey reports, citing Lee and Brunskill, that individualized BKT in an intelligent tu](individualized-bkt-reduces-questions-needed-for-mastery.md) (supports); [The survey reports, citing Mongkhonvanit et al., that DKT achieved better performance when](engagement-covariates-improve-deep-knowledge-tracing.md) (supports); [The survey reports, citing Qiu et al., that BKT consistently overestimates the accuracy of](bkt-overestimates-accuracy-after-a-day-elapses.md) (supports); [The survey reports, citing Jung et al., that students' language proficiency as side inform](language-proficiency-side-information-improves-kt-models.md) (supports) |
| [Pardos 2010](https://doi.org/10.1007/978-3-642-13470-8_24) | q1 / q2 · design · r2 | i? | [Individualizing the initial knowledge parameter reliably improves prediction of real-world](individualizing-initial-knowledge-improves-prediction.md) (supports); [Corbett and Anderson's original individualization attempts produced mixed results](corbett-anderson-individualization-mixed-results.md) (qualifies) |
| [Reddy 2016](https://doi.org/10.1145/2939672.2939850) | q2 · associational · r2 | i? | [In Mnemosyne flashcard log data, adding a delay term improves the recall-prediction perfor](delay-term-improves-exponential-forgetting-curve-recall-prediction.md) (supports); [In Mnemosyne log data, exponential forgetting curve models that include a delay term perfo](exponential-forgetting-models-with-delay-perform-comparably-to-1pl-irt.md) (qualifies) |
| [Yuhao Jia 2026](https://doi.org/10.48550/arxiv.2605.08697) | q2 · design · r2 | i? | [Injecting MBP-KT's global collaborative information consistently improves KT models across](mbp-kt-consistently-improves-kt-backbones.md) (supports); [MBP-KT yields significantly greater improvements for learners with fewer interaction recor](mbp-kt-greater-gains-sparse-learners.md) (qualifies) |
| [Haotian Zhang 2026](https://doi.org/10.48550/arxiv.2608.24005) | q3 · design · r2 | i? | [Modeling knowledge transfer within and across domains alleviates the cold-start problem on](knowledge-transfer-alleviates-cold-start-kt.md) (supports) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [Deep Learning Knowledge Tracing Outperforms But Lacks Interpretability](deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md)
- [No single learner model was best across the six datasets, justifying a broad multi-model approach](no-single-learner-model-best-across-datasets.md) — possibly the same claim (merge candidate)
- [Memory-decay-based models fit fact-learning datasets better than models insensitive to memory decay](memory-features-improve-fit-for-fact-learning-datasets.md) — related
- [For Chinese tone learning, simpler models insensitive to memory decay fit as well as or better than memory-feature models](simpler-models-sufficient-for-tone-learning.md) — related
- [The PPE memory model was the best-fitting model for the Andes physics dataset, with the recency feature also beneficial](ppe-best-fitting-andes-physics.md) — related
- [Models able to weight performance by recency fit better on the Assistments and KDD datasets, without explicit memory-decay terms being necessary](recency-weighting-models-better-assistments-kdd.md) — related
- [Four methods of identifying individual change each duplicated group-based effect sizes, with the reliable change index and growth curve approaches showing stronger consistency and predictive power (Frijters et al.)](four-change-metrics-reliable-change-and-growth-curve-stronger.md) — related
- [A multi-skill prior strategy yielded lower prediction error in 33 of 42 problem sets](multi-skill-prior-strategy-best-prediction-error.md) — related
- [The survey reports, citing Lee and Brunskill, that individualized BKT in an intelligent tutoring system reduced by about half the questions required for 20% of students to achieve mastery.](individualized-bkt-reduces-questions-needed-for-mastery.md) — related
- [The survey reports, citing Qiu et al., that BKT consistently overestimates the accuracy of students' answers when a day or more has elapsed since their previous responses.](bkt-overestimates-accuracy-after-a-day-elapses.md) — related
- [Corbett and Anderson's original individualization attempts produced mixed results](corbett-anderson-individualization-mixed-results.md) — related
