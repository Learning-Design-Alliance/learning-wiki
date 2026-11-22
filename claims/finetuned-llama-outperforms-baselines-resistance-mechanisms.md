---
type: claim
title: Fine-tuned Llama-3.1-8B model outperforms GPT-4o and Claude-3.5-Sonnet at rating the four resistance-response mechanisms
description: Fine-tuned Llama-3.1-8B model outperforms GPT-4o and Claude-3.5-Sonnet at rating the four resistance-response mechanisms
id: finetuned-llama-outperforms-baselines-resistance-mechanisms
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: anqi-li-2026
    resource: "https://doi.org/10.48550/arXiv.2602.21638"
    title: "Anqi Li, Ruihan Wang, Zhaoming Chen, Yuqian Chen, Yu Lu, Yi Zhu, Yuan Xie, Zhenzhong Lan. (2026). Multi-dimensional Assessment and Explainable Feedback for Counselor Responses to Client Resistance in Text-based Counseling with LLMs. [doi:10.48550/arXiv.2602.21638](https://doi.org/10.48550/arXiv.2602.21638)"
    author: Anqi Li, Ruihan Wang, Zhaoming Chen, Yuqian Chen, Yu Lu, Yi Zhu, Yuan Xie, Zhenzhong Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned Llama-3.1-8B model outperforms GPT-4o and Claude-3.5-Sonnet at rating the four resistance-response mechanisms

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The fine-tuned model achieves macro-F1 scores of 77-81% across the four communication mechanisms, more than 20 F1 points above the best zero-shot baselines. [→ Anqi Li 2026](#anqi-li-2026)

## Evidence

### Anqi Li 2026

Anqi Li, Ruihan Wang, Zhaoming Chen, Yuqian Chen, Yu Lu, Yi Zhu, Yuan Xie, Zhenzhong Lan. (2026). Multi-dimensional Assessment and Explainable Feedback for Counselor Responses to Client Resistance in Text-based Counseling with LLMs. [doi:10.48550/arXiv.2602.21638](https://doi.org/10.48550/arXiv.2602.21638)

`q2 · i?` · `design · r2`

Five-fold cross-validated evaluation of the full-parameter fine-tuned Llama-3.1-8B-Instruct model against zero-shot baselines on the 3,836-sample dataset. The article reports macro-F1 "scores ranging from 77% to 81%" and gains of more than 20 F1 points, with up to 35.5 F1 points in Respect for Autonomy.

> "In contrast, our approach achieves substantial improvements across all four communication dimensions, with macro-F1 scores ranging from 77% to 81%. Relative to the best-performing general-purpose LLMs, our model yields gains of more than 20 F1 points overall"

## Discussion


## Related Claims
- [AI-generated feedback significantly improves counselors' responses to client resistance in a controlled experiment](ai-feedback-improves-counselor-responses-experiment.md) — related
- [In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task](sft-less-effective-than-prompting-for-feedback-generation.md) — related
- [Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B](finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics.md) — related
- [Fine-tuned model generates explanations that nearly double baseline BLEU-1 and receive near-ceiling expert ratings](finetuned-model-explanations-outperform-baselines.md) — related
- [A fine-tuned GPT-4o model outperforms GPTZero at detecting LLM-generated short answers in an online lesson, achieving 80% accuracy versus GPTZero's 70%](fine-tuned-gpt4o-outperforms-gptzero-short-answers.md) — related
- [The best fine-tuned open-source model outperforms GPT-5-mini prompting by 2.1% macro F1 and trails GPT-5 by 1.9% macro F1 on unseen rubrics](fine-tuned-open-source-competitive-with-proprietary-llms.md) — related
- [Fine-tuning substantially outperforms zero-shot prompting of the same open-source model for cross-rubric scoring, improving macro F1 from 0.222 to 0.353](fine-tuning-beats-zero-shot-prompting-same-model.md) — related
