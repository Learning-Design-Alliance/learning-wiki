---
type: claim
title: "Human inter-rater agreement on the writing rubric is imperfect: no rubric item reaches full agreement and the most discrepant rater generally falls below 80%"
description: "Human inter-rater agreement on the writing rubric is imperfect: no rubric item reaches full agreement and the most discrepant rater generally falls below 80%"
id: human-inter-rater-agreement-imperfect-upper-bound
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: curi-2026
    resource: "https://doi.org/10.48550/arxiv.2609.05143"
    title: "Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143 [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)"
    author: Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human inter-rater agreement on the writing rubric is imperfect: no rubric item reaches full agreement and the most discrepant rater generally falls below 80%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the 2024 calibration phase with ten expert evaluators scoring 50 texts, no rubric item showed complete agreement with the consensus score, and minimum rater agreement was generally below 80%. [→ Curi 2026](#curi-2026)

## Evidence

### Curi 2026

Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143 [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)

`q2 · i?` · `design · r2`

Inter-rater agreement analysis of the 2024 calibration phase, in which ten evaluators independently scored each of 50 texts (Fig. 2). The article reports no item with full agreement and minimum agreement generally below 80%, establishing an empirical upper bound for AI performance.

> "It can be observed that there is no item for which all evaluators agree on the final assigned score, and that some items show greater discrepancies than others. The results show that the minimum value, that is, the rater exhibiting the greatest discrepancy with the consensus score, generally achieves agreement below 80%."

## Discussion

## Related Claims

- [Raters differed significantly in severity/leniency in the MFRM analysis](raters-differed-severity-mfrm.md) — the general claim this finding bears on, with the studies behind it
- [LLM-based scoring of Spanish argumentative writing achieves 60–80% per-item accuracy, slightly below human inter-rater agreement](llm-scoring-spanish-writing-60-80-accuracy-below-human-agreement.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [Inter-rater agreement among the 20 expert teachers was low, at or below chance across QM criteria](low-inter-rater-agreement-qm-criteria.md) — related
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
- [Automated essay scoring can achieve high agreement with human raters but faces calibration constraints](aes-high-agreement-calibration-constraint.md) — related
- [Three independent expert instructors reached exceptionally high inter-rater reliability when grading 1200 bash exam responses, establishing a reliable human reference standard](expert-triad-high-inter-rater-reliability-bash-grading.md) — reports the opposite
- [AI scoring consistency approaches or exceeds 90% for most rubric items, but spelling is replaced by a deterministic LanguageTool-based approach achieving 68% accuracy with 100% consistency](ai-consistency-high-except-spelling-languagetool-replacement.md) — related
- [Rubrics enhance grading consistency and inter-rater reliability in dental education assessment](rubrics-enhance-grading-consistency-dental-education.md) — reports the opposite
- [Rubric-guided grading pipelines can approach human-level agreement when explicit rubrics, exemplars, and calibration are used](rubric-guided-grading-human-agreement.md) — related
