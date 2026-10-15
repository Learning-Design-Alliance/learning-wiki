---
type: claim
title: "AI scoring shows a systematic conservative bias, under-grading writing so 15.3% (2024) and 16.5% (2025) of human-passing tests would fail under AI scoring"
description: "AI scoring shows a systematic conservative bias, under-grading writing so 15.3% (2024) and 16.5% (2025) of human-passing tests would fail under AI scoring"
id: ai-scoring-systematic-under-grading-bias-pass-fail
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: curi-2026
    resource: "https://doi.org/10.48550/arxiv.2609.05143"
    title: "Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143 [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)"
    author: Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: curi-2026-2
    resource: "https://doi.org/10.48550/arxiv.2609.05143"
    title: "Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143. [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)"
    author: Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# AI scoring shows a systematic conservative bias, under-grading writing so 15.3% (2024) and 16.5% (2025) of human-passing tests would fail under AI scoring

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` The AI model penalizes responses more strictly than human raters; cases where human raters pass but AI fails are 15.3% in 2024 and 16.5% in 2025, while the reverse direction is rare. [→ Curi 2026](#curi-2026)
`q2 i?` The conservative bias is not uniform: the AI model achieved higher agreement for responses classified as Proficient than for those classified as Insufficient. [→ Curi 2026 (2)](#curi-2026-2)

## Evidence

### Curi 2026

Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143 [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)

`q2 · i?` · `design · r2`

Pass/fail confusion matrices (Fig. 7) combining AI Writing results with human proficiency levels in Reading Comprehension and Problem Solving for the 2024 and 2025 editions. The article reports 15.3% (2024) and 16.5% (2025) of tests passing under human scoring but failing under AI scoring.

> "These cases (15.3% in 2024 and 16.5% in 2025) are of particular interest, as they provide evidence supporting the need for human review of texts for which the AI predicts a failing outcome."

### Curi 2026 (2)

Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143. [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)

`q2 · i?` · `design · r2`

Detailed analysis by proficiency level of the 2024 and 2025 level confusion matrices (Fig. 6), showing the under-grading bias is concentrated in Insufficient-level responses rather than uniform across categories.

> "The AI model achieved higher agreement for responses classified asProficientthan for those classified asInsufficient, a pattern consistent with the confusion matrices presented in Figure 6."

## Discussion


## Related Claims
- [Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding](agreement-quality-divergence-human-consensus-bias.md) — related
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
