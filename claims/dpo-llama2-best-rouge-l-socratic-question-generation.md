---
type: claim
title: A DPO-optimized Llama 2-7B model gives the best Rouge-L scores among all compared Socratic question generation methods, including GPT-3.5 and GPT-4 prompting baselines
description: A DPO-optimized Llama 2-7B model gives the best Rouge-L scores among all compared Socratic question generation methods, including GPT-3.5 and GPT-4 prompting baselines
id: dpo-llama2-best-rouge-l-socratic-question-generation
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

# A DPO-optimized Llama 2-7B model gives the best Rouge-L scores among all compared Socratic question generation methods, including GPT-3.5 and GPT-4 prompting baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Preference-optimized models with DPO give the best Rouge-L precision, recall, and F1 scores of all methods compared on the Socratic code-debugging dataset. [→ Nischal Ashok Kumar and Andrew Lan 2024](#nischal-ashok-kumar-and-andrew-lan-2024)

## Evidence

### Nischal Ashok Kumar and Andrew Lan 2024

Nischal Ashok Kumar and Andrew Lan. (2024). Improving Socratic Question Generation using Data Augmentation and Preference Optimization. arXiv preprint arXiv:2403.00199. [doi:10.48550/arXiv.2403.00199](https://doi.org/10.48550/arXiv.2403.00199)

`q2 · i?` · `design · r2`

Benchmark comparison in the Results section on the Socratic code-debugging dataset of (Al-Hossami et al.), with GPT baseline results taken from prior work. The article reports that "DPO Greedy having the highest precision and DPO Sample-5 having the highest recall and F1 score among all the methods" on Rouge-L.

> "Overall, we see that our preference-optimized models with DPO give the best Rouge-L scores for all precision, recall, and F1 scores with DPO Greedy having the highest precision and DPO Sample-5 having the highest recall and F1 score among all the methods."

## Discussion


## Related Claims
- [DPO consistently outperforms supervised fine-tuning (SFT) for Socratic question generation with Llama 2](dpo-outperforms-sft-socratic-questions.md) — related
- [GPT-4 (CoT) prompting achieves the highest recall but the lowest F1 score among GPT baselines because most of its generated questions do not match ground truth](gpt4-cot-highest-recall-lowest-f1.md) — related
- [Automatic text-similarity metrics do not correlate with manual evaluation for Socratic utterance generation](automatic-metrics-uncorrelated-socratic-manual-eval.md) — related
- [Sampling multiple Socratic questions (Sample-5) yields better performance than greedy decoding](sample-5-beats-greedy-decoding-socratic.md) — related
- [Student performance correlates positively with the teacher's DPO optimization progress and with the share of positive-influence data](teacher-learning-student-performance-correlation.md) — related
- [Generated content averaged BLEU 0.688, cultural relevance 4.4/5 and fluency 4.2/5 across tested African languages, with isiZulu highest and Amharic lowest](multilingual-quality-african-languages.md) — related
