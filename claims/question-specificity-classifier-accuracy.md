---
type: claim
title: An LLM-based question-specificity classifier reached .830 knowledge and .829 scaffold accuracy without fine-tuning
description: An LLM-based question-specificity classifier reached .830 knowledge and .829 scaffold accuracy without fine-tuning
id: question-specificity-classifier-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: hyoungwook-jin-2026
    resource: "https://doi.org/10.48550/arxiv.2609.28918"
    title: "Hyoungwook Jin, Weirui Peng, Jieun Han, Q. Vera Liao, and Xu Wang. (2026). HelpCoach: Scaffolding Targeted AI Help-Seeking During Problem-Solving. arXiv. https://arxiv.org/abs/2609.28918 [doi:10.48550/arxiv.2609.28918](https://doi.org/10.48550/arxiv.2609.28918)"
    author: Hyoungwook Jin, Weirui Peng, Jieun Han, Q. Vera Liao, and Xu Wang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# An LLM-based question-specificity classifier reached .830 knowledge and .829 scaffold accuracy without fine-tuning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Among three tested models, Gemini-3.5-Flash performed best consistently across the three programming tasks for both knowledge specificity (.830) and scaffold specificity (.829) against human-annotated data. [→ Hyoungwook Jin 2026](#hyoungwook-jin-2026)

## Evidence

### Hyoungwook Jin 2026

Hyoungwook Jin, Weirui Peng, Jieun Han, Q. Vera Liao, and Xu Wang. (2026). HelpCoach: Scaffolding Targeted AI Help-Seeking During Problem-Solving. arXiv. https://arxiv.org/abs/2609.28918 [doi:10.48550/arxiv.2609.28918](https://doi.org/10.48550/arxiv.2609.28918)

`q2 · i?` · `causal · r2`

Technical evaluation comparing three LLM classifiers against human-annotated data from Study 1 (739 questions) on binary knowledge- and scaffold-specificity classification. Gemini-3.5-Flash achieved the highest accuracy; the article notes it achieved reasonable accuracy without fine-tuning on a large dataset.

> "Among the three models, Gemini-3.5-Flash performed the best consistently across the three programming tasks for both knowledge specificity (.830) and scaffold specificity (.829)."

## Discussion


## Related Claims
- [FATE benchmarks rank Gemini 2.5 Flash highest among commercial AI tutors, with actionability weakest for all models](fate-benchmark-commercial-ai-tutors.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Gemini-3-flash achieved the highest rubric-item accuracy, ranging from 89% on Course 2 to over 99% on Course 1](gemini-3-flash-highest-rubric-item-accuracy.md) — related
- [Gemini 2.0 Flash validated as a reliable LLM annotator of feedback focus types](gemini-flash-reliable-feedback-focus-annotator.md) — related
- [One student group compared outputs across three LLMs and judged Gemini more accurate overall, though it still failed fine-grained distinctions](multi-llm-comparison-gemini-more-accurate.md) — related
