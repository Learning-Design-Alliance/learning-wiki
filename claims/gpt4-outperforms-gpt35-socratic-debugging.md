---
type: claim
title: GPT-4 outperforms GPT-3.5 in generating relevant and diverse Socratic debugging utterances, but remains below human expert levels
description: GPT-4 outperforms GPT-3.5 in generating relevant and diverse Socratic debugging utterances, but remains below human expert levels
id: gpt4-outperforms-gpt35-socratic-debugging
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

# GPT-4 outperforms GPT-3.5 in generating relevant and diverse Socratic debugging utterances, but remains below human expert levels

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Manual evaluation of generated instructor utterances shows GPT-4's superior performance over GPT-3.5 in precision, recall and F1 for Socratic debugging. [→ Erfan Al-Hossami 2024](#erfan-al-hossami-2024)
`q2 i?` GPT-3.5 produces many more poor Socratic questions (93 false positives) than GPT-4 (41 false positives). [→ Erfan Al-Hossami 2024](#erfan-al-hossami-2024)
`q2 i?` Despite outperforming GPT-3.5, GPT-4's precision and recall remain below human expert levels. [→ Erfan Al-Hossami 2024](#erfan-al-hossami-2024)

## Evidence

### Erfan Al-Hossami 2024

Erfan Al-Hossami, Razvan Bunescu, Justin Smith and Ryan Teehan. (2024). Can Language Models Employ the Socratic Method? Experiments with Code Debugging. arXiv. Originally published 2023. [doi:10.1145/3626252.3630799](https://doi.org/10.1145/3626252.3630799)

`q2 · i?` · `design · r2`

Manual evaluation of 149 instructor utterances across 43 turns in 11 benchmark dialogues, judging LM utterances as appropriate Socratic guidance. The authors report "GPT-4’s superior performanc e over GPT-3.5" and note GPT-3.5's poor precision with 93 false positives versus GPT-4's 41.

> "The precision (P), recall (R), and their harmonic m ean (F1) presented in Table 2 highlight GPT-4’s superior performanc e over GPT-3.5 in generating relevant and diverse Socratic uttera nces."

## Discussion


## Related Claims
- [Automatic text-similarity metrics do not correlate with manual evaluation for Socratic utterance generation](automatic-metrics-uncorrelated-socratic-manual-eval.md) — related
- [Chain-of-thought prompting increases recall at the expense of precision for GPT-4 but lowers GPT-3.5 performance](cot-recall-precision-tradeoff-socratic.md) — related
- [Human inter-annotator agreement and dataset recall of 75.5 validate the benchmark's coverage of high-quality Socratic utterances](human-ita-dataset-recall-validation.md) — related
- [LLM ratings of classroom transcripts are more correlated with each other than with expert human ratings, across the same and different tasks](llm-llm-agreement-exceeds-llm-human-classroom-ratings.md) — related
