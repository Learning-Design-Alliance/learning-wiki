---
type: claim
title: GPT-4 (CoT) prompting achieves the highest recall but the lowest F1 score among GPT baselines because most of its generated questions do not match ground truth
description: GPT-4 (CoT) prompting achieves the highest recall but the lowest F1 score among GPT baselines because most of its generated questions do not match ground truth
id: gpt4-cot-highest-recall-lowest-f1
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: nischal-ashok-kumar-and-andrew-lan-2024
    resource: "https://doi.org/10.48550/arXiv.2403.00199"
    title: "Nischal Ashok Kumar and Andrew Lan. (2024). Improving Socratic Question Generation using Data Augmentation and Preference Optimization. arXiv preprint arXiv:2403.00199. [doi:10.48550/arXiv.2403.00199](https://doi.org/10.48550/arXiv.2403.00199)"
    author: Nischal Ashok Kumar and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 (CoT) prompting achieves the highest recall but the lowest F1 score among GPT baselines because most of its generated questions do not match ground truth

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 (CoT) has the highest recall and the lowest F1 score among the compared methods, due to many generated questions being false positives. [→ Nischal Ashok Kumar and Andrew Lan 2024](#nischal-ashok-kumar-and-andrew-lan-2024)

## Evidence

### Nischal Ashok Kumar and Andrew Lan 2024

Nischal Ashok Kumar and Andrew Lan. (2024). Improving Socratic Question Generation using Data Augmentation and Preference Optimization. arXiv preprint arXiv:2403.00199. [doi:10.48550/arXiv.2403.00199](https://doi.org/10.48550/arXiv.2403.00199)

`q2 · i?` · `design · r2`

Results-section analysis of Table 1, where GPT baseline results are taken from prior work (Al-Hossami et al., 2024). The article reports that "GPT-4 (CoT) has the highest recall" and yet the lowest F1 score, attributing this to many generated questions labeled as false positives, decreasing precision.

> "We observe that GPT-4 (CoT) has the highest recall and yet the low- est F1 score. This observation is because, GPT-4 generates a large number of Socratic questions"

## Discussion


## Related Claims
- [A DPO-optimized Llama 2-7B model gives the best Rouge-L scores among all compared Socratic question generation methods, including GPT-3.5 and GPT-4 prompting baselines](dpo-llama2-best-rouge-l-socratic-question-generation.md) — related
- [Chain-of-thought prompting increases recall at the expense of precision for GPT-4 but lowers GPT-3.5 performance](cot-recall-precision-tradeoff-socratic.md) — possibly the same claim (merge candidate)
- [Automatic text-similarity metrics do not correlate with manual evaluation for Socratic utterance generation](automatic-metrics-uncorrelated-socratic-manual-eval.md) — related
- [GPT-4 context descriptions improve story-matched 3D model generation quality from 3.2 to 4.6 out of 5](gpt4-descriptions-improve-3d-model-context-match.md) — related
