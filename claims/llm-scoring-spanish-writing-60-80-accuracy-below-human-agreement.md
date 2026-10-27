---
type: claim
title: "LLM-based scoring of Spanish argumentative writing achieves 60–80% per-item accuracy, slightly below human inter-rater agreement"
description: "LLM-based scoring of Spanish argumentative writing achieves 60–80% per-item accuracy, slightly below human inter-rater agreement"
id: llm-scoring-spanish-writing-60-80-accuracy-below-human-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
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

# LLM-based scoring of Spanish argumentative writing achieves 60–80% per-item accuracy, slightly below human inter-rater agreement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a large-scale national exam, AI model accuracy per rubric item ranges between 60% and 80%, falling slightly below average human inter-rater agreement (gap ~5% for most items, never exceeding 15%). [→ Curi 2026](#curi-2026)

## Evidence

### Curi 2026

Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143 [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)

`q2 · i?` · `design · r2`

Analysis of the 2024 calibration phase (50 texts, each scored 10 times by the AI model) comparing mean AI accuracy to average human inter-rater agreement per rubric item (Fig. 3). The article reports "AI model accuracy ranges between 60% and 80%" with gaps of about 5% for most items.

> "As expected, the model's results fall slightly below the agreement observed between human raters. However, for more than half of the rubric items, this difference is approximately 5%, and for the remaining items, it never exceeds 15%. In absolute terms, AI model accuracy ranges between 60% and 80%."

## Discussion


## Related Claims
- [AI scoring consistency approaches or exceeds 90% for most rubric items, but spelling is replaced by a deterministic LanguageTool-based approach achieving 68% accuracy with 100% consistency](ai-consistency-high-except-spelling-languagetool-replacement.md) — related
- [Human inter-rater agreement on the writing rubric is imperfect: no rubric item reaches full agreement and the most discrepant rater generally falls below 80%](human-inter-rater-agreement-imperfect-upper-bound.md) — related
- [Automated essay scoring can achieve high agreement with human raters but faces calibration constraints](aes-high-agreement-calibration-constraint.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
- [Spellcheck and autocorrect are not foolproof: efficacy is bounded near 80% and the most common student writing error is now correctly spelled but inappropriate words](spellcheck-not-foolproof-wrong-word-errors.md) — related
- [ASR-based item-level accuracy scores show moderate agreement with human raters in a Dutch word decoding and passage reading task](asr-accuracy-moderate-agreement-human-raters.md) — related
