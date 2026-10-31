---
type: claim
title: The selected-questions-verbs prompting strategy yields the strongest LLM Bloom classification, reaching weighted F1 up to 0.84
description: The selected-questions-verbs prompting strategy yields the strongest LLM Bloom classification, reaching weighted F1 up to 0.84
id: selected-questions-verbs-best-prompt
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: abdolali-faraji-2026
    resource: "https://doi.org/10.48550/arxiv.2606.13684"
    title: "Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684 [doi:10.48550/arxiv.2606.13684](https://doi.org/10.48550/arxiv.2606.13684)"
    author: Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The selected-questions-verbs prompting strategy yields the strongest LLM Bloom classification, reaching weighted F1 up to 0.84

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Combining manually selected in-context examples with expert-curated level-specific action verbs achieved the highest weighted F1 scores across datasets. [→ Abdolali Faraji 2026](#abdolali-faraji-2026)

## Evidence

### Abdolali Faraji 2026

Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684 [doi:10.48550/arxiv.2606.13684](https://doi.org/10.48550/arxiv.2606.13684)

`q2 · i?` · `causal · r1`

LLM evaluation (RQ2, Table 3): GPT-5 and GPT-5-mini classified all questions in five datasets under five prompting strategies; the "selected-questions-verbs" prompt reached weighted F1 up to 0.84 on the Yahya dataset.

> "Specifically, theselected-questions-verbsprompt achieves the strongest performance, reaching weighted F1-scores of up to 0.84 on the Yahya dataset."

## Discussion


## Related Claims
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](in-context-examples-improve-bloom-classification.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Dual-Lens attention aligns with expert pedagogical focus, allocating most weight to Bloom's taxonomy verbs and problem-solving steps](dual-lens-attention-aligns-expert-pedagogical-focus.md) — related
- [A meta-analysis of literature and policy sources yields climate resilience education ideas groupable into content, methods, goals and actions aligned with learning objectives](meta-analysis-groups-climate-resilience-education-into-content-methods-goals-actions.md) — related
