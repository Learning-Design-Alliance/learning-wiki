---
type: claim
title: "The rule-based recipe annotation system reaches near-perfect inter-annotator agreement (Cohen's Kappa 0.85) and average accuracy 0.95 in a validation on sampled recipe segments."
description: "The rule-based recipe annotation system reaches near-perfect inter-annotator agreement (Cohen's Kappa 0.85) and average accuracy 0.95 in a validation on sampled recipe segments."
id: relex-annotation-validation-kappa-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: mejia-domenzain-2025
    resource: "https://doi.org/10.1007/s40593-024-00405-1"
    title: "Mejia-Domenzain, P., Frej, J., Neshaei, S. P., Mouchel, L., Nazaretsky, T., Wambsganss, T., Bosselut, A., & Käser, T. (2025). Enhancing Procedural Writing Through Personalized Example Retrieval: A Case Study on Cooking Recipes. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00405-1"
    author: "Mejia-Domenzain, P., Frej, J., Neshaei, S. P., Mouchel, L., Nazaretsky, T., Wambsganss, T., Bosselut, A., & Käser, T."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The rule-based recipe annotation system reaches near-perfect inter-annotator agreement (Cohen's Kappa 0.85) and average accuracy 0.95 in a validation on sampled recipe segments.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Mejia-Domenzain 2025: no comparison group (read from the study by two models, 2026-10-27)

## Subclaims
`q2 i?` Manual validation of the regular-expression annotation rules against human labels yielded Cohen's Kappa of 0.85 and average accuracy of 0.95. [→ Mejia-Domenzain 2025](#mejia-domenzain-2025)

## Evidence

### Mejia-Domenzain 2025

Mejia-Domenzain, P., Frej, J., Neshaei, S. P., Mouchel, L., Nazaretsky, T., Wambsganss, T., Bosselut, A., & Käser, T. (2025). Enhancing Procedural Writing Through Personalized Example Retrieval: A Case Study on Cooking Recipes. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00405-1

`q2 · i?` · `causal · r2`

Evaluation on a random sample of recipe segments: two author-annotators labeled shuffled segments as present/missing per suggestion. The printed result is that "the average accuracy was 0 .95" with near-perfect agreement. No effect size is printed.

> "The Cohen's Kappa score between the annotators was 0.85 (near perfect agreement (Landis & Koch, 1977)) and the average accuracy was 0 .95."

## Discussion


## Related Claims
- [The star-to-sentiment labeling rule agrees with human review-level labels at Cohen's kappa 0.66 with 82% accuracy on 3,000 RateMyProfessor teacher reviews](star-label-rule-kappa-066-82-percent.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — a broader claim this one bears on
- [In classroom video labeling, high raw agreement (often exceeding 90%) co-occurred with low chance-corrected κ due to temporal misalignment](raw-agreement-kappa-paradox-classroom-video.md) — related
- [Three independent expert instructors reached exceptionally high inter-rater reliability when grading 1200 bash exam responses, establishing a reliable human reference standard](expert-triad-high-inter-rater-reliability-bash-grading.md) — related
- [Automatic DAC coding of dialogue acts agrees substantially with manual coding (79.0% agreement, kappa 0.75)](dac-automatic-coding-agrees-with-manual-coding.md) — related
- [Gemini 2.0 Flash validated as a reliable LLM annotator of feedback focus types](gemini-flash-reliable-feedback-focus-annotator.md) — related
- [Machine learning detects five of eight reflective-writing categories with substantial or almost perfect reliability and three with moderate reliability (Cohen's κ .53–.85)](ml-detects-reflection-categories-kappa-053-085.md) — related
- [Kappa agreement with human experts shows a system is neither much worse nor much better than experts, but not that experts are a desirable comparison basis](kappa-expert-agreement-limits.md) — related
- [ML scoring models for scientific argumentation items achieved good to almost perfect agreement with human consensus scores (mean Cohen's kappa = 0.60)](ml-scoring-argumentation-mean-kappa-060.md) — related
