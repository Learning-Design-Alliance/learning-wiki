---
type: claim
title: Automatic text-similarity metrics do not correlate with manual evaluation for Socratic utterance generation
description: Automatic text-similarity metrics do not correlate with manual evaluation for Socratic utterance generation
id: automatic-metrics-uncorrelated-socratic-manual-eval
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

# Automatic text-similarity metrics do not correlate with manual evaluation for Socratic utterance generation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Automatic metrics (BLEU-4, BERT F1, Rouge-L) fail to correlate with manual evaluation in GPT-4's CoT experiment because semantically matching utterances can have no lexical overlap. [→ Erfan Al-Hossami 2024](#erfan-al-hossami-2024)

## Evidence

### Erfan Al-Hossami 2024

Erfan Al-Hossami, Razvan Bunescu, Justin Smith and Ryan Teehan. (2024). Can Language Models Employ the Socratic Method? Experiments with Code Debugging. arXiv. Originally published 2023. [doi:10.1145/3626252.3630799](https://doi.org/10.1145/3626252.3630799)

`q2 · i?` · `design · r2`

Automatic evaluation over the full benchmark using bipartite maximum matching (Edmond's Blossom algorithm) over BLEU-4, BERT F1 (DeBERTa) and Rouge-L similarities. The authors give the example that 'What should your code be doing' semantically matches 'What do you expect your for loop to do?' but scores less than 0.4 on BERT F1.

> "Automatic metri cs do not correlate with manual evaluation in GPT-4’s CoT exper i- ment, likely due to CoT introducing new utterances absent fr om the dataset more often and low lexical and semantic overlap betw een actual and generated utterances."

## Discussion


## Related Claims
- [GPT-4 outperforms GPT-3.5 in generating relevant and diverse Socratic debugging utterances, but remains below human expert levels](gpt4-outperforms-gpt35-socratic-debugging.md) — related
- [Chain-of-thought prompting increases recall at the expense of precision for GPT-4 but lowers GPT-3.5 performance](cot-recall-precision-tradeoff-socratic.md) — related
- [BLEU-4 scored zero on all 179 mathematical-proof responses, which the authors interpret as a property of n-gram metrics rather than system failure](bleu4-zero-mathematical-proofs-metric-limitation.md) — a narrower finding that bears on this claim
- [Human inter-annotator agreement and dataset recall of 75.5 validate the benchmark's coverage of high-quality Socratic utterances](human-ita-dataset-recall-validation.md) — related
- [Cluster membership showed a strong multivariate effect on standard text-similarity metrics (Pillai's trace = 0.85, F(12, 248) = 15.31, p < 0.001)](manova-cluster-effect-text-metrics.md) — related
- [Per-topic performance varied: NP-completeness scored highest ROUGE-1 F1 (0.1285), sorting algorithms highest pedagogical quality (0.8250), and recurrence relations lowest pedagogical quality (0.6629)](algorag-topic-specific-performance-variation.md) — related
- [A DPO-optimized Llama 2-7B model gives the best Rouge-L scores among all compared Socratic question generation methods, including GPT-3.5 and GPT-4 prompting baselines](dpo-llama2-best-rouge-l-socratic-question-generation.md) — related
- [GPT-4 (CoT) prompting achieves the highest recall but the lowest F1 score among GPT baselines because most of its generated questions do not match ground truth](gpt4-cot-highest-recall-lowest-f1.md) — related
