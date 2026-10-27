---
type: claim
title: Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.
description: Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.
id: existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial
status: review
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: alexander-scarlatos-2024
    resource: "https://doi.org/10.48550/arxiv.2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490 [doi:10.48550/arxiv.2409.16490](https://doi.org/10.48550/arxiv.2409.16490)"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: alexander-scarlatos-2024-2
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On CoMTA, all existing KT methods almost completely fail, unable to outperform the majority-class baseline (Acc. 57.83±5.08, AUC 50.0±0.00, F1 58.87±29.70). [→ Alexander Scarlatos 2024](#alexander-scarlatos-2024)
`q2 i?` On MathDial, which has 21x more data than CoMTA, existing KT methods perform significantly better, against a majority baseline Acc. of 52.64. [→ Alexander Scarlatos 2024 (2)](#alexander-scarlatos-2024-2)

## Evidence

### Alexander Scarlatos 2024

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490 [doi:10.48550/arxiv.2409.16490](https://doi.org/10.48550/arxiv.2409.16490)

`q2 · i?` · `design · r2`

CoMTA results of the benchmark comparison with 5-fold cross-validation: existing methods "almost completely fail, unable to outperform the simple baseline of predicting the majority class label", which scores Acc. of 57.83±5.08, AUC of 50.0±0.00, and F1 of 58.87±29.70.

> "On CoMTA, we see that all existing KT methods almost completely fail, unable to outperform the simple baseline of predicting the majority class label (which corresponds to an Acc. of 57.83±5.08, AUC of 50.0±0.00, and F1 of 58.87±29.70)."

### Alexander Scarlatos 2024 (2)

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490

`q2 · i?` · `design · r2`

MathDial results of the same comparison: "existing KT methods perform significantly better" with 21x more data; the majority baseline gets an Acc. of 52.64 since class labels are balanced. No effect size is printed.

> "On MathDial, which has 21x more data than CoMTA, we see that existing KT methods perform significantly better (for reference, the majority baseline only gets an Acc. of 52.64 since class labels are balanced)."

## Discussion

## Related Claims

- [The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.](deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) — the general claim this finding bears on, with the studies behind it
- [Llmkt Outperforms Existing Kt Methods On Tutoring Dialogues](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md)
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) — related
- [DKT-Sem, a DKT variant using semantic text embeddings, performs better than existing KT methods on tutoring dialogues, with a smaller margin on the larger MathDial dataset.](dkt-sem-outperforms-existing-kt-methods-most-with-little-training-data.md) — related
- Fine-tuning Llama2-7B with parameter-efficient methods yields unsatisfactory results for measuring subject-matter teaching practices, only marginally improving the majority baseline — related
- [Standardized benchmarks are often too generic to reflect the needs of innovative educational applications](standardized-benchmarks-too-generic-for-education.md) — related
- In system cold-start scenarios, CLST outperformed every baseline KT model across all five datasets, with the largest gains at 8 training students — related
- [A pedagogically informed Tutor Prompt yields higher Success@N and lower Telling@N than MathDial's Base Prompt in simulated tutor-student dialogues](tutor-prompt-outperforms-base-prompt-mathdial.md) — related
- [Longer student histories do not improve LLM knowledge tracing: FKT AUC-ROC stays near 0.5-0.6 whether models see 50 or 400 prior interactions](context-length-no-effect-fkt.md) — related
- [An IRT-based difficulty-aware conversational KT framework improves AUC over the LLMKT baseline on both QATD2k and MathDial](irt-difficulty-aware-kt-beats-llmkt-auc.md) — related
- [Among deep learning KT models, simpler DKT performs comparably to complex architectures under limited dialogue data](dkt-comparable-to-complex-kt-architectures.md) — related
- [Binary classification of students who might need support from keystroke data only slightly exceeds the majority-class baseline (highest AUC 0.57)](keystroke-classification-weak-auc.md) — related
- [On real tutor log data, the models beat mean-time prediction but most of the gain is captured by a simple baseline, and the learning extension slightly overfits](real-data-prediction-baseline-captures-most-gain.md) — related
