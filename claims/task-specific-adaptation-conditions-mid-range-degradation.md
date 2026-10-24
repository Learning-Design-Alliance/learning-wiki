---
type: claim
title: "Mid-range degradation is conditioned on task-specific adaptation: it is most severe for few-shot LLMs with few examples, decreases with more task-specific data, and is mildest for the fine-tuned encoder"
description: "Mid-range degradation is conditioned on task-specific adaptation: it is most severe for few-shot LLMs with few examples, decreases with more task-specific data, and is mildest for the fine-tuned encoder"
id: task-specific-adaptation-conditions-mid-range-degradation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: abigail-victoria-gurin-schleifer-2026
    resource: "https://doi.org/10.48550/arxiv.2605.07647"
    title: "Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647 [doi:10.48550/arxiv.2605.07647](https://doi.org/10.48550/arxiv.2605.07647)"
    author: Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: abigail-victoria-gurin-schleifer-2026-2
    resource: "https://arxiv.org/abs/2605.07647"
    title: "Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647"
    author: Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: abigail-victoria-gurin-schleifer-2026-3
    resource: "https://arxiv.org/abs/2605.07647"
    title: "Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647"
    author: Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Mid-range degradation is conditioned on task-specific adaptation: it is most severe for few-shot LLMs with few examples, decreases with more task-specific data, and is mildest for the fine-tuned encoder

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r1`–`r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fine-tuned BERT models also degraded in the mid-range but less severely, with maximum average distance of 1.5 categories from the gold scores. [→ Abigail Victoria Gurin Schleifer 2026](#abigail-victoria-gurin-schleifer-2026)
`q2 i?` For GPT-4o, providing only two few-shot examples resulted in substantial mid-range degradation — a difference of 3 categories or more for responses with 4-6 correct categories — on both items. [→ Abigail Victoria Gurin Schleifer 2026 (2)](#abigail-victoria-gurin-schleifer-2026-2)
`q2 i?` In the prompt-number pilot with GPT-4o, 10-shot prompting achieved better overall agreement and mid-range fairness, so the frontier models were run only in the 10-shot version. [→ Abigail Victoria Gurin Schleifer 2026 (3)](#abigail-victoria-gurin-schleifer-2026-3)

## Evidence

### Abigail Victoria Gurin Schleifer 2026

Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647 [doi:10.48550/arxiv.2605.07647](https://doi.org/10.48550/arxiv.2605.07647)

`q2 · i?` · `causal · r2`

Score-level analysis (Results): fine-tuned models degrade mid-range too, but "the maximum average distances from the gold scores is 1.5 categories", milder than the few-shot models' distances.

> "Fine-tuned models also perform worse in this middle range than in the extremes, but the degradation is not as severe – the maximum average distances from the gold scores is 1.5 categories."

### Abigail Victoria Gurin Schleifer 2026 (2)

Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647

`q2 · i?` · `causal · r2`

GPT-4o few-shot dose analysis (Results): "providing only two examples resulted in a substantial degradation in the middle range of the scores" of 3 categories or more for 4-6 correct categories, on both items.

> "providing only two examples resulted in a substantial degradation in the middle range of the scores – difference of 3 categories or more, on average, for scores with 4-6 correct categories out of 10 – for both items."

### Abigail Victoria Gurin Schleifer 2026 (3)

Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647

`q2 · i?` · `causal · r1`

GPT-4o pilot over 2/4/6/8/10-shot prompts (Methodology §3.3.2): "10-shot prompting achieved better results, both in terms of overall (average) agreement and in terms of mid-range fairness"; only 10-shot ran for frontier models.

> "The results showed that 10-shot prompting achieved better results, both in terms of overall (average) agreement and in terms of mid-range fairness, as can be seen in Figure 1."

## Discussion


## Related Claims
- [Ai Mid Range Scoring Degradation U Shape](ai-mid-range-scoring-degradation-u-shape.md)
- The second human expert showed the highest and most stable agreement with the gold-standard rater, with no mid-range degradation across the response quality spectrum — related
- [On fully correct responses, the GPT few-shot models outperformed the fine-tuned models, averaging less than one category distance from the gold score](gpt-outperforms-finetuned-on-fully-correct-responses.md) — related
