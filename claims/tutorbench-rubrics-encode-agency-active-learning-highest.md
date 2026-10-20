---
type: claim
title: In the public TutorBench sample, agency-oriented rubric criteria are most concentrated in the active-learning use case (agency-dimension density 0.720, agency-skill density 0.411)
description: In the public TutorBench sample, agency-oriented rubric criteria are most concentrated in the active-learning use case (agency-dimension density 0.720, agency-skill density 0.411)
id: tutorbench-rubrics-encode-agency-active-learning-highest
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: junyi-yao-2026
    resource: "https://doi.org/10.48550/arxiv.2606.16206"
    title: "Junyi Yao, Zihao Zheng, and Baichuan Li. (2026). Beyond Helpfulness: A Teaching-over-Solving Diagnostic for Measuring Educational Impact in LLM Tutors. arXiv preprint. https://arxiv.org/abs/2606.16206 [doi:10.48550/arxiv.2606.16206](https://doi.org/10.48550/arxiv.2606.16206)"
    author: Junyi Yao, Zihao Zheng, and Baichuan Li
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# In the public TutorBench sample, agency-oriented rubric criteria are most concentrated in the active-learning use case (agency-dimension density 0.720, agency-skill density 0.411)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`

## Subclaims
`q2 i?` Across the three use-case families, the active-learning subset has the highest concentration of agency-oriented criteria, with rubric language rewarding guiding questions, hints without full disclosure, and prompting alternative lines of reasoning. [→ Junyi Yao 2026](#junyi-yao-2026)

## Evidence

### Junyi Yao 2026

Junyi Yao, Zihao Zheng, and Baichuan Li. (2026). Beyond Helpfulness: A Teaching-over-Solving Diagnostic for Measuring Educational Impact in LLM Tutors. arXiv preprint. https://arxiv.org/abs/2606.16206 [doi:10.48550/arxiv.2606.16206](https://doi.org/10.48550/arxiv.2606.16206)

`q2 · i?` · `design · r?`

Deterministic rubric-label mapping of the public TutorBench sample (30 scenarios, 324 rubric items across adaptive explanation, assessment/feedback, and active learning). Table 2 reports agency-dimension densities of 0.583, 0.688, and 0.720 and agency-skill densities of 0.139, 0.294, and 0.411 respectively.

> "Even under this stricter item-level counting rule, the active-learning subset has the highest concen- tration of agency-oriented criteria. In qualitative examples, rubric language explicitly rewards ask- ing guiding questions, providing hints without dis- closing the full next step"

## Discussion


## Related Claims
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [TACTutor shows no degradation relative to its Qwen backbone on external educational benchmarks, with scores rising on MRBench, TutorBench, LongTutor, and DeepTutor](tactutor-no-degradation-external-benchmarks.md) — related
