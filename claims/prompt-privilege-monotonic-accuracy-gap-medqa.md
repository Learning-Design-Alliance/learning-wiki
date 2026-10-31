---
type: claim
title: On MedQA, GPT-5.4-mini's accuracy increases monotonically with prompt sophistication across semantically equivalent questions, with generated Low Literacy prompt variants scoring significantly below Prompt Engineer variants
description: On MedQA, GPT-5.4-mini's accuracy increases monotonically with prompt sophistication across semantically equivalent questions, with generated Low Literacy prompt variants scoring significantly below Prompt Engineer variants
id: prompt-privilege-monotonic-accuracy-gap-medqa
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-31
recheck_by: 2029
sources:
  - id: lier-jin-2026
    resource: "https://doi.org/10.48550/arxiv.2608.08942"
    title: "Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942 [doi:10.48550/arxiv.2608.08942](https://doi.org/10.48550/arxiv.2608.08942)"
    author: Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: lier-jin-2026-2
    resource: "https://arxiv.org/abs/2608.08942"
    title: "Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942"
    author: Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: lier-jin-2026-3
    resource: "https://arxiv.org/abs/2608.08942"
    title: "Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942"
    author: Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# On MedQA, GPT-5.4-mini's accuracy increases monotonically with prompt sophistication across semantically equivalent questions, with generated Low Literacy prompt variants scoring significantly below Prompt Engineer variants

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r1` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-31 (automated, 3 of 3 entries) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Design limits** · Lier Jin 2026 (3): the intervention came bundled with another change (read from the study by two models, 2026-10-25)

## Subclaims
`q2 i?` Across semantically equivalent MedQA prompt variants generated to represent user cohorts (not collected from real users) and answered by the same model, GPT-5.4-mini, accuracy exhibits a consistent monotonic trend in which it increases with prompt sophistication. [→ Lier Jin 2026](#lier-jin-2026)
`q2 i?` The Low Literacy cohort achieves the lowest baseline accuracy (82.4%) and the Prompt Engineer cohort the highest (83.4%). [→ Lier Jin 2026 (2)](#lier-jin-2026-2)
`q2 i?` Among all cohort pairs, only the Low Literacy versus Prompt Engineer comparison reaches statistical significance, a 1.0 percentage-point difference with a 95% confidence interval excluding zero. [→ Lier Jin 2026 (3)](#lier-jin-2026-3)

## Evidence

### Lier Jin 2026

Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942 [doi:10.48550/arxiv.2608.08942](https://doi.org/10.48550/arxiv.2608.08942)

`q2 · i?` · `causal · r1`

Baseline benchmark evaluation of GPT-5.4-mini on MedQA prompt variants, measured by classification accuracy under identical inference settings. The article reports that despite identical underlying tasks, the results exhibit a consistent monotonic trend in which accuracy increases with prompt sophistication.

> "Although the absolute performance differences are modest, they exhibit a consistent monotonic trend in which accuracy increases with prompt sophistication."

### Lier Jin 2026 (2)

Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942

`q2 · i?` · `causal · r1`

Same baseline evaluation across the five prompt-style cohorts. The Low Literacy cohort achieves the lowest accuracy (82.4%) while the Prompt Engineer cohort achieves the highest (83.4%), supporting the hypothesis that prompt formulation influences downstream performance when task and intent are unchanged.

> "The Low Literacy cohort achieves the lowest accuracy (82.4%), followed by the Original Question, Everyday User, and Educated User cohorts, while the Prompt Engineer cohort achieves the highest accuracy (83.4%)."

### Lier Jin 2026 (3)

Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942

`q2 · i?` · `causal · r1`

Pairwise accuracy differences with 95% bootstrap confidence intervals in the baseline evaluation. Only the Low Literacy versus Prompt Engineer comparison reaches statistical significance (∆ = 1.0 percentage point, 95% CI[−1.9,−0.1]percentage points); remaining comparisons follow the same trend with intervals overlapping zero.

> "Among all cohort pairs, only the Low Literacy versus Prompt Engineer comparison reaches statistical significance (∆ = 1.0 percentage point, 95% CI[−1.9,−0.1]percentage points)."

## Discussion


## Related Claims
- [After PET normalization, no statistically significant performance differences remain between user cohorts](pet-eliminates-significant-accessibility-disparities.md) — related
- [Applying PET raises accuracy for every user cohort, with the largest gain for the Low Literacy cohort](pet-raises-accuracy-all-cohorts-largest-low-literacy-gain.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — related
- [Certain aspects of AI literacy play a role in higher-quality prompt engineering by non-expert students](ai-literacy-aspects-support-prompt-engineering.md) — a broader claim this one bears on
- [Success rates decrease monotonically from easy to medium to hard difficulty levels across all models](monotonic-difficulty-decline-turtleai.md) — related
- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](prompt-design-affects-mcq-accuracy-asymmetrically.md) — related
- [C3-IoC job role matching accuracy increases monotonically with the number of questionnaire questions answered, reaching about 80% accuracy with four questions and nearly 100% with 24](c3-ioc-matching-accuracy-increases-with-questions.md) — related
- [Increased solution count correlated with decreased LLM accuracy, falling short of statistical significance except at solution count 5](solution-count-decreased-accuracy-not-significant.md) — related
