---
type: claim
title: Sampling multiple Socratic questions (Sample-5) yields better performance than greedy decoding
description: Sampling multiple Socratic questions (Sample-5) yields better performance than greedy decoding
id: sample-5-beats-greedy-decoding-socratic
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

# Sampling multiple Socratic questions (Sample-5) yields better performance than greedy decoding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Among decoding variants for the trained models, nucleus-sampling five sequences outperforms greedy decoding. [→ Nischal Ashok Kumar and Andrew Lan 2024](#nischal-ashok-kumar-and-andrew-lan-2024)

## Evidence

### Nischal Ashok Kumar and Andrew Lan 2024

Nischal Ashok Kumar and Andrew Lan. (2024). Improving Socratic Question Generation using Data Augmentation and Preference Optimization. arXiv preprint arXiv:2403.00199. [doi:10.48550/arXiv.2403.00199](https://doi.org/10.48550/arXiv.2403.00199)

`q2 · i?` · `design · r2`

Results-section comparison of decoding techniques for the SFT and DPO models, using nucleus sampling with a p value of 0.9 and five return sequences versus greedy decoding. The article states "the Sample-5 method is better than the Greedy method".

> "Among decoding variants, we see that the Sample-5 method is better than the Greedy method highlighting the importance of sampling multiple possible Socratic questions instead of just one."

## Discussion


## Related Claims
- [A DPO-optimized Llama 2-7B model gives the best Rouge-L scores among all compared Socratic question generation methods, including GPT-3.5 and GPT-4 prompting baselines](dpo-llama2-best-rouge-l-socratic-question-generation.md) — related
