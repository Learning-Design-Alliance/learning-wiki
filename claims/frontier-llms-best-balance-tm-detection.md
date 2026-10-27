---
type: claim
title: "Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall"
description: "Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall"
id: frontier-llms-best-balance-tm-detection
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: moiz-imran-and-sahan-bulathwela-2026
    resource: "https://doi.org/10.48550/arxiv.2605.23925"
    title: "Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925 [doi:10.48550/arxiv.2605.23925](https://doi.org/10.48550/arxiv.2605.23925)"
    author: Moiz Imran and Sahan Bulathwela
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
  - id: moiz-imran-and-sahan-bulathwela-2026-2
    resource: "https://arxiv.org/abs/2605.23925"
    title: "Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925"
    author: Moiz Imran and Sahan Bulathwela
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Gemini 3 Flash reaches 83.6% TM recall with 94.0% TC recall, significantly better than fine-tuned T5 on TM detection. [→ Moiz Imran and Sahan Bulathwela 2026](#moiz-imran-and-sahan-bulathwela-2026)
`q2 i?` Fine-tuned T5 and BERT achieve under 58% TM recall despite near-perfect separation of correct and incorrect answers (FM recall at or above 98%). [→ Moiz Imran and Sahan Bulathwela 2026 (2)](#moiz-imran-and-sahan-bulathwela-2026-2)

## Evidence

### Moiz Imran and Sahan Bulathwela 2026

Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925 [doi:10.48550/arxiv.2605.23925](https://doi.org/10.48550/arxiv.2605.23925)

`q2 · i?` · `causal · r?`

Model comparison on the 61-case TM test set from the Eedi benchmark. The authors report Gemini 3 Flash "improves TM recall to 83.6% [72.4, 90.8]" with a significant McNemar's test over T5 (p= 0.005).

> "Gemini 3 Flash improves TM recall to 83.6% [72.4, 90.8] while maintaining 94.0% TC recall; the improvement over T5 is significant (McNemar's test,p= 0.005)."

### Moiz Imran and Sahan Bulathwela 2026 (2)

Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925

`q2 · i?` · `design · r?`

Evaluation of fine-tuned T5-small and BERT-base classifiers on the Eedi test data; both models detect few true-misconception cases among correct answers, with TM recall "under 58%".

> "Both achieve under 58% TM recall, showing that optimisation for domi- nant labels leaves rare TM cases under-detected."

## Discussion


## Related Claims
- [On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data](cat-extends-to-prm800k-validation.md) — related
- [Mined misconception labels match personas' assigned misconceptions at F1 ≈ 0.56, a score that does not test whether generated questions elicit the named misconception](collearn-misconception-mining-f1.md) — related
- [At natural TM prevalence (1.6%), even the best model generates roughly 4.3 false alarms per genuine detection, making fully automated stand-alone screening not viable on its own](false-alarms-make-standalone-screening-impractical.md) — related
- Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification — possibly the same claim (merge candidate)
- Standard ML interventions do not improve hidden-misconception detection beyond the fine-tuned classifier baseline — related
- A reasoning-capable open-weight model detects 84% of hidden misconceptions but at realistic prevalence false alarms outnumber genuine detections roughly 8 to 1 — related
- [A task-specific prompt with explicit guidance about correct-answer cases significantly outperforms literature-based PedCoT prompting on TM test cases (84% vs 59% accuracy)](task-specific-prompt-beats-pedcot-prompting.md) — related
- [Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators](prompt-engineering-adaptation-transparency-tradeoff.md) — related
- [Epi2Diff achieves the best performance across all four item-difficulty test sets and all reported metrics, outperforming SLM fine-tuning, LLM prompting, and supervised LLM adaptation baselines](epi2diff-best-across-four-difficulty-benchmarks.md) — related
- [GPT models showed lower accuracy with more rubric-related errors (28% vs. 13% for Gemini 3 Flash) and near parity between false positives and negatives](gpt-models-more-rubric-errors-than-gemini.md) — related
- [LLM-based automated assessment of student code self-explanations outperforms semantic similarity methods on a balanced classification task](llm-assessment-outperforms-semantic-similarity-code-explanations.md) — related
- [Fine-tuning frontier LLMs on authentic tutoring data improves performance on all six conversational and pedagogical benchmarks, moving values toward human-tutor levels](fine-tuning-authentic-data-improves-pedagogical-benchmarks.md) — related
- [LLM feedback agents classify optimal logic proof steps near-ceiling but perform poorly on valid-alternative and incorrect solutions](llm-tutors-near-ceiling-optimal-poor-valid-alternative-incorrect.md) — related
- [The system's error detection recall rate for complex rhythm errors was 91.2% ± 1.8%](rhythm-error-detection-recall-91-2.md) — related
- [LLM feedback agents show model-specific over-rejection of valid-alternative reasoning and over-validation of incorrect solutions](llm-over-rejection-over-validation-patterns.md) — related
- [LLM misconception analysis that ties student errors to instructional content reveals insights not apparent from performance data alone](llm-misconception-analysis-reveals-insights-beyond-performance-data.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [The fine-tuned T5 question-extraction model reached an average training loss of 0.4098, indicating imperfect question extraction](t5-finetuning-average-loss-04098.md) — related
