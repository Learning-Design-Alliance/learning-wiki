---
type: claim
title: Chain-of-thought prompting increases recall at the expense of precision for GPT-4 but lowers GPT-3.5 performance
description: Chain-of-thought prompting increases recall at the expense of precision for GPT-4 but lowers GPT-3.5 performance
id: cot-recall-precision-tradeoff-socratic
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: erfan-al-hossami-2024
    resource: "https://doi.org/10.1145/3626252.3630799"
    title: "Erfan Al-Hossami, Razvan Bunescu, Justin Smith and Ryan Teehan. (2024). Can Language Models Employ the Socratic Method? Experiments with Code Debugging. arXiv. Originally published 2023. [doi:10.1145/3626252.3630799](https://doi.org/10.1145/3626252.3630799)"
    author: Erfan Al-Hossami, Razvan Bunescu, Justin Smith and Ryan Teehan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Chain-of-thought prompting increases recall at the expense of precision for GPT-4 but lowers GPT-3.5 performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using CoT with GPT-4 yields an increase in recall at the expense of precision. [→ Erfan Al-Hossami 2024](#erfan-al-hossami-2024)
`q2 i?` GPT-3.5 performs worse with CoT due to its poor ability to list possible reasons and misconceptions. [→ Erfan Al-Hossami 2024](#erfan-al-hossami-2024)

## Evidence

### Erfan Al-Hossami 2024

Erfan Al-Hossami, Razvan Bunescu, Justin Smith and Ryan Teehan. (2024). Can Language Models Employ the Socratic Method? Experiments with Code Debugging. arXiv. Originally published 2023. [doi:10.1145/3626252.3630799](https://doi.org/10.1145/3626252.3630799)

`q2 · i?` · `design · r2`

Manual evaluation on the benchmark shows GPT-4 with CoT generates more utterances addressing possible reasons or misconceptions, but also more duplicates, already-asked questions, and premature utterances. The authors also report lower GPT-3.5 performance with CoT due to its poor ability in listing possible reasons and misconceptions.

> "On the other hand, we obse rve an increase in recall at the expense of precision when using C oT when using GPT-4."

## Discussion


## Related Claims
- [Automatic text-similarity metrics do not correlate with manual evaluation for Socratic utterance generation](automatic-metrics-uncorrelated-socratic-manual-eval.md) — related
- [In detecting teacher questions with zero-shot GPT-3.5-turbo, chain-of-thought prompting had slightly higher F1 and precision than Self-Ask but slightly lower recall and balanced accuracy](cot-outperforms-self-ask-zero-shot.md) — related
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](few-shot-cot-outperforms-zero-shot-question-detection.md) — related
- [GPT-4 outperforms GPT-3.5-turbo in a single-lesson question-detection test](gpt4-outperforms-gpt35-single-lesson.md) — related
- [GPT-4 outperforms GPT-3.5 in generating relevant and diverse Socratic debugging utterances, but remains below human expert levels](gpt4-outperforms-gpt35-socratic-debugging.md) — related
- [Chain-of-thought prompting yields higher-quality GenAI feedback on argumentative essays than Zero-shot prompting and teacher feedback](cot-prompting-higher-feedback-quality-than-zero-shot-and-teacher.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — a broader claim this one bears on
- [GPT-4 (CoT) prompting achieves the highest recall but the lowest F1 score among GPT baselines because most of its generated questions do not match ground truth](gpt4-cot-highest-recall-lowest-f1.md) — possibly the same claim (merge candidate)
