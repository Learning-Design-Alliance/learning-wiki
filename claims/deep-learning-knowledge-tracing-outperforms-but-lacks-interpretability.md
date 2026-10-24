---
type: claim
title: The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.
description: The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.
id: deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability
status: review
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: mixed
newest_evidence: 2021
source_checked: 2026-10-20
recheck_by: 2024
sources:
  - id: shuanghong-shen-2021
    resource: "https://doi.org/10.48550/arxiv.2105.15106"
    title: "Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106 [doi:10.48550/arxiv.2105.15106](https://doi.org/10.48550/arxiv.2105.15106)"
    author: Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2021 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The review asserts deep learning KT models exhibit superior performance compared to Bayesian and logistic models while leaving significant room for improvement in interpretability and explainability. [→ Shuanghong Shen 2021](#shuanghong-shen-2021)

## Evidence

### Shuanghong Shen 2021

Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106 [doi:10.48550/arxiv.2105.15106](https://doi.org/10.48550/arxiv.2105.15106)

`q2 · i?` · `review · r2`

Narrative review summary of the fundamental models section, with no pooled comparison by the authors: deep learning models are described as "exhibiting superior performance compared to Bayesian mod- els and logistic models" but lacking interpretability, which the survey says has limited their further applicability.

> "It is crucial to emphasize that, despite deep learning models exhibiting superior performance compared to Bayesian mod- els and logistic models, there remains significant room for improvement in their interpretability and explainability."

## Studies bearing on this claim

<!-- synthesis:start -->
*How accurately does BKT predict a learner's next answers, compared with other knowledge-tracing models, and do its assumptions and fitted parameters hold up?* This table gathers the studies behind this claim and the 18 narrower claims that bear on it: **11 distinct studies** (7 design, 1 review, 1 causal, 1 associational, 1 theoretical), `q1`–`q3`, 1 of 11 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Shuanghong Shen 2021](https://doi.org/10.48550/arxiv.2105.15106) | q2 · review · r2 | i? | this claim; [The survey reports, citing Pavlik et al., that no single knowledge tracing model was alway](no-single-knowledge-tracing-model-is-always-best.md) (qualifies); [The survey reports, citing Pu and Becker, that removing students' repeated interactions on](attentive-knowledge-tracing-benefits-from-repeated-interactions.md) (qualifies); [The survey reports, citing Lu et al., that xAI-based interpretations of deep knowledge tra](xai-interpretation-of-dkt-enhances-trust.md) (qualifies); [The survey reports, citing Qiu et al., that BKT consistently overestimates the accuracy of](bkt-overestimates-accuracy-after-a-day-elapses.md) (supports) |
| [Jaewook Kim 2026](https://doi.org/10.48550/arxiv.2605.04727) | q2 · causal · r2 | i? | [Task-specific hyperparameter optimization substantially raises baseline DKT performance, i](task-specific-hyperparameter-tuning-raises-dkt-baseline.md) (qualifies) |
| [Shuyan Huang 2026](https://doi.org/10.48550/arxiv.2605.01097) | q2 · design · r2 | i? | [Among deep learning KT models, simpler DKT performs comparably to complex architectures un](dkt-comparable-to-complex-kt-architectures.md) (qualifies) |
| [Hooshyar 2026](https://doi.org/10.48550/arxiv.2604.08263) | q2 · design · r2 | i? | [Responsible-DKT outperforms a neural-symbolic baseline without knowledge injection and a f](responsible-dkt-outperforms-baselines-predictive-accuracy.md) (supports); [Symbolic knowledge injection improves temporal reliability of predictions, yielding lower ](responsible-dkt-temporal-reliability.md) (qualifies) |
| [Lu 2024](https://doi.org/10.31219/osf.io/3k7z2) | q3 · design · r2 | i2 | [The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an ](transformer-kt-first-place-edm-cup-2023.md) (supports) |
| [Haotian Zhang 2026](https://doi.org/10.48550/arxiv.2608.24005) | q3 · design · r2 | i? | [LT-MKT achieves the best performance across all four datasets and all three evaluation met](lt-mkt-outperforms-kt-baselines-four-datasets.md) (supports) |
| [Alexander Scarlatos 2024](https://doi.org/10.48550/arxiv.2409.16490) | q2 · design · r2 | i? | [DKT-Sem, a DKT variant using semantic text embeddings, performs better than existing KT me](dkt-sem-outperforms-existing-kt-methods-most-with-little-training-data.md) (supports); [Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dat](existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial.md) (qualifies) |
| [Pardos 2010](https://doi.org/10.1007/978-3-642-13470-8_24) | q2 · design · r2 | i? | [Individualizing the initial knowledge parameter reliably improves prediction of real-world](individualizing-initial-knowledge-improves-prediction.md) (qualifies) |
| [Wei 2026](https://doi.org/10.3389/fpsyg.2026.1905847) | q2 · associational · r2 | i? | [Per-pitch BKT attains the highest accuracy, lowest BCE and lowest Brier score of the four ](bkt-highest-accuracy-lower-auc-than-irt.md) (qualifies) |
| [Siddhartha Pradhan 2026](https://doi.org/10.48550/arxiv.2605.23048) | q2 · design · r2 | i? | [On the ASSISTments 2020 dataset, StanBKT inference methods achieve nearly identical predic](stanbkt-methods-comparable-predictive-performance-assistments-2020.md) (qualifies) |
| [Brett Van de Sande 2013](https://doi.org/10.5281/zenodo.3554629) | q1 / q2 · theoretical · r3 | i? | [The exponential functional form of the BKT Markov chain calls into question the popular pr](bkt-hmm-exponential-form-questions-fitting-practice.md) (qualifies); [The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) w](bkt-identifiability-explained-by-parameter-a.md) (qualifies); [The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity ](bkt-hmm-form-is-three-parameter-exponential.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [No Single Knowledge Tracing Model Is Always Best](no-single-knowledge-tracing-model-is-always-best.md)
- [The survey reports, citing Lu et al., that xAI-based interpretations of deep knowledge tracing were demonstrated to aid in enhancing the trust of students and teachers.](xai-interpretation-of-dkt-enhances-trust.md) — related
- [BKT is the most efficient knowledge tracing approach overall in simulated online mastery learning, though DKT is more efficient for AS and M problems](bkt-most-efficient-online-mastery-learning.md) — related
- [Among deep learning KT models, simpler DKT performs comparably to complex architectures under limited dialogue data](dkt-comparable-to-complex-kt-architectures.md) — related
- [LT-MKT achieves the best performance across all four datasets and all three evaluation metrics against eleven KT baselines](lt-mkt-outperforms-kt-baselines-four-datasets.md) — related
- [DKT-Sem, a DKT variant using semantic text embeddings, performs better than existing KT methods on tutoring dialogues, with a smaller margin on the larger MathDial dataset.](dkt-sem-outperforms-existing-kt-methods-most-with-little-training-data.md) — related
- [The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an AUC of 78.969% on the private evaluation dataset](transformer-kt-first-place-edm-cup-2023.md) — related
- [Symbolic knowledge injection improves temporal reliability of predictions, yielding lower early- and mid-sequence errors and the lowest prediction inconsistency rates across sequence lengths](responsible-dkt-temporal-reliability.md) — related
- [Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.](existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial.md) — related
- [On the ASSISTments 2020 dataset, StanBKT inference methods achieve nearly identical predictive performance while differing mainly in fit time](stanbkt-methods-comparable-predictive-performance-assistments-2020.md) — related
- [Responsible-DKT outperforms a neural-symbolic baseline without knowledge injection and a fully data-driven PyTorch DKT in predictive accuracy across training ratios and sequence lengths](responsible-dkt-outperforms-baselines-predictive-accuracy.md) — a narrower finding that bears on this claim
- [The survey reports, citing Qiu et al., that BKT consistently overestimates the accuracy of students' answers when a day or more has elapsed since their previous responses.](bkt-overestimates-accuracy-after-a-day-elapses.md) — related
