---
type: claim
title: Both LLMs correlate only weakly with human ground-truth scores overall, with agreement strongest for Programming and near-zero for Mathematics
description: Both LLMs correlate only weakly with human ground-truth scores overall, with agreement strongest for Programming and near-zero for Mathematics
id: weak-human-llm-grading-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: rudra-jadhav-2026
    resource: "https://doi.org/10.48550/arXiv.2603.18765"
    title: "Rudra Jadhav, Janhavi Danve, and Sonalika Shaw. (2026). Implicit Grading Bias in Large Language Models: How Writing Style Affects Automated Assessment Across Math, Programming, and Essay Tasks. Preprint. [doi:10.48550/arXiv.2603.18765](https://doi.org/10.48550/arXiv.2603.18765)"
    author: Rudra Jadhav, Janhavi Danve, and Sonalika Shaw
    q: 2
    i: 2
    kind: causal
    rigour: 1
---

# Both LLMs correlate only weakly with human ground-truth scores overall, with agreement strongest for Programming and near-zero for Mathematics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2` · `i2` medium
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i2` Overall human-LLM correlations were weak (LLaMA r = 0.315; Qwen r = 0.339), strongest for Programming (r approximately 0.48) and weakest for Mathematics (r = 0.00 and r = -0.04). [→ Rudra Jadhav 2026](#rudra-jadhav-2026)

## Evidence

### Rudra Jadhav 2026

Rudra Jadhav, Janhavi Danve, and Sonalika Shaw. (2026). Implicit Grading Bias in Large Language Models: How Writing Style Affects Automated Assessment Across Math, Programming, and Essay Tasks. Preprint. [doi:10.48550/arXiv.2603.18765](https://doi.org/10.48550/arXiv.2603.18765)

`q2 · i2` · `causal · r1`

Pearson correlations and MAE were computed against human ground-truth scores (range 7-10) across the 180-response dataset. The article reports "weak overall correlation with human ground-truth scores" and attributes the near-zero Math correlation to ceiling effects producing minimal score variance.

> "Both models showed weak overall correlation with human ground-truth scores (LLaMA: r= 0.315 , MAE = 0.922; Qwen: r= 0.339 , MAE = 0.856 )."

## Discussion


## Related Claims
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
- [LLM marking agrees with human markers on only about half of graded Physics answers, and assigns higher, less variable normalized scores than humans](llm-marking-concordance-with-humans-about-half.md) — related
- [LLM grading bias follows a subjectivity gradient: near-zero bias for Programming and Math, severe bias for Essay/Writing, consistent across both models](llm-grading-subjectivity-gradient.md) — related
- [AAG system scores align closely with human TA scores on open-ended statistics questions, with Pearson correlations of 0.75 and 0.82](aag-ta-score-correlation-open-ended.md) — related
