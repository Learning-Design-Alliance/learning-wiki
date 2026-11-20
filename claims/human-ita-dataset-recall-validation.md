---
type: claim
title: "Human inter-annotator agreement and dataset recall of 75.5 validate the benchmark's coverage of high-quality Socratic utterances"
description: "Human inter-annotator agreement and dataset recall of 75.5 validate the benchmark's coverage of high-quality Socratic utterances"
id: human-ita-dataset-recall-validation
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

# Human inter-annotator agreement and dataset recall of 75.5 validate the benchmark's coverage of high-quality Socratic utterances

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Inter-annotator agreement reaches P = 77.4, R = 46.1, F1 = 57.8, substantially higher than the best-performing system, especially in precision. [→ Erfan Al-Hossami 2024](#erfan-al-hossami-2024)
`q2 i?` Benchmark dataset recall during human evaluation is 75.5, suggesting most high-quality LM-generated Socratic utterances are captured in the dataset. [→ Erfan Al-Hossami 2024](#erfan-al-hossami-2024)

## Evidence

### Erfan Al-Hossami 2024

Erfan Al-Hossami, Razvan Bunescu, Justin Smith and Ryan Teehan. (2024). Can Language Models Employ the Socratic Method? Experiments with Code Debugging. arXiv. Originally published 2023. [doi:10.1145/3626252.3630799](https://doi.org/10.1145/3626252.3630799)

`q2 · i?` · `design · r2`

Inter-annotator agreement computed on 5 dialogues (24 turns, over 73 instructor utterances) by having one contributor write utterances against ground truth from others. Additionally, 82.1% of correct utterances were semantically equivalent to one contributed by another contributor, and dataset recall was 75.5.

> "The ITA evaluation results in 𝑃 = 77.4, 𝑅 = 46.1, and 𝐹1 = 57.8. This is substantially higher than the best-performing system shown in Table 2, especially in terms of pr eci- sion, demonstrating that a human data contributor can reliably write high-quality Socratic utterances."

## Discussion


## Related Claims
- [Automatic text-similarity metrics do not correlate with manual evaluation for Socratic utterance generation](automatic-metrics-uncorrelated-socratic-manual-eval.md) — related
- [GPT-4 outperforms GPT-3.5 in generating relevant and diverse Socratic debugging utterances, but remains below human expert levels](gpt4-outperforms-gpt35-socratic-debugging.md) — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — related
- [Inter-annotator agreement was moderate (combined mean Fleiss's κ of 0.62 across 23 groups), yet most students reported having reached consensus](moderate-kappa-versus-perceived-consensus-gap.md) — related
- [Human inter-rater agreement for FRISCO essay scoring was reliable, with mean kappa 0.78–0.84 and percentage of agreement above 75% in all six dimensions](frisco-rater-agreement-reliable.md) — related
