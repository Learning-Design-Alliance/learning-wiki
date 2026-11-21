---
type: claim
title: Fine-tuned model generates explanations that nearly double baseline BLEU-1 and receive near-ceiling expert ratings
description: Fine-tuned model generates explanations that nearly double baseline BLEU-1 and receive near-ceiling expert ratings
id: finetuned-model-explanations-outperform-baselines
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
  - id: anqi-li-2026-2
    resource: "https://doi.org/10.48550/arXiv.2602.21638"
    title: "Anqi Li, Ruihan Wang, Zhaoming Chen, Yuqian Chen, Yu Lu, Yi Zhu, Yuan Xie, Zhenzhong Lan. (2026). Multi-dimensional Assessment and Explainable Feedback for Counselor Responses to Client Resistance in Text-based Counseling with LLMs. [doi:10.48550/arXiv.2602.21638](https://doi.org/10.48550/arXiv.2602.21638)"
    author: Anqi Li, Ruihan Wang, Zhaoming Chen, Yuqian Chen, Yu Lu, Yi Zhu, Yuan Xie, Zhenzhong Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned model generates explanations that nearly double baseline BLEU-1 and receive near-ceiling expert ratings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The model's explanations reach BLEU-1 of 0.60 versus 0.32 for the strongest baseline Claude-3.5-Sonnet. [→ Anqi Li 2026](#anqi-li-2026)
`q2 i?` Human experts rate the model's explanations 2.8-2.9 out of 3.0 on framework consistency, evidence anchoring, and clarity and specificity. [→ Anqi Li 2026 (2)](#anqi-li-2026-2)

## Evidence

### Anqi Li 2026

Anqi Li, Ruihan Wang, Zhaoming Chen, Yuqian Chen, Yu Lu, Yi Zhu, Yuan Xie, Zhenzhong Lan. (2026). Multi-dimensional Assessment and Explainable Feedback for Counselor Responses to Client Resistance in Text-based Counseling with LLMs. [doi:10.48550/arXiv.2602.21638](https://doi.org/10.48550/arXiv.2602.21638)

`q2 · i?` · `design · r2`

Automatic evaluation of generated explanations on the held-out folds using BLEU and ROUGE metrics. The article reports the model "achieves a BLEU-1 score of 0.60" against 0.32 for Claude-3.5-Sonnet.

> "In terms of automatic lexical overlap, our model achieves a BLEU-1 score of 0.60, nearly doubling the performance of the strongest baseline, Claude-3.5-Sonnet (0.32)."

### Anqi Li 2026 (2)

Anqi Li, Ruihan Wang, Zhaoming Chen, Yuqian Chen, Yu Lu, Yi Zhu, Yuan Xie, Zhenzhong Lan. (2026). Multi-dimensional Assessment and Explainable Feedback for Counselor Responses to Client Resistance in Text-based Counseling with LLMs. [doi:10.48550/arXiv.2602.21638](https://doi.org/10.48550/arXiv.2602.21638)

`q2 · i?` · `design · r2`

Human expert evaluation of generated explanations along three dimensions on a 3-point scale. The article reports ratings "ranging from 2.8 to 2.9", above GPT-4o and Claude-3.5-Sonnet.

> "Our model consistently receives near-perfect ratings, ranging from 2.8 to 2.9, which markedly outperforms the scores of GPT-4o and Claude-3.5-Sonnet."

## Discussion


## Related Claims
- [AI-generated feedback significantly improves counselors' responses to client resistance in a controlled experiment](ai-feedback-improves-counselor-responses-experiment.md) — related
- [Fine-tuned Llama-3.1-8B model outperforms GPT-4o and Claude-3.5-Sonnet at rating the four resistance-response mechanisms](finetuned-llama-outperforms-baselines-resistance-mechanisms.md) — related
- [Task-specific fine-tuning substantially improves open-source LLMs on MedGame Bench and narrows the gap with commercial models](fine-tuning-improves-open-source-llms-medgame-bench.md) — a broader claim this one bears on
- [DeepSeek-MoE (Ours) achieves the strongest overall balance of accuracy among tested configurations, reaching 78.6% overall and 81.2% multi-hop reasoning accuracy on a 300-query OER evaluation set](deepseek-moe-ours-strongest-accuracy-balance.md) — a broader claim this one bears on
- [INSIDE fine-tuning achieves the highest alignment between generated internal dialogue and ground-truth student code edits, up to 57.9%](inside-highest-reasoning-alignment-57-9.md) — related
