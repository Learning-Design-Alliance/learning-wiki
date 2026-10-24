---
type: claim
title: "Prompt-based scoring prompts developed on one year's test generalize to the next year's edition with only minor adjustments"
description: "Prompt-based scoring prompts developed on one year's test generalize to the next year's edition with only minor adjustments"
id: prompt-scoring-generalizes-across-test-editions
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

# Prompt-based scoring prompts developed on one year's test generalize to the next year's edition with only minor adjustments

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Applying 2024-derived prompts to a 1,000-text sample of the 2025 test produced accuracy very similar to 2024, with only minor adjustments to items referencing the yearly writing topic. [→ Curi 2026](#curi-2026)

## Evidence

### Curi 2026

Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143 [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)

`q2 · i?` · `design · r2`

Cross-year validation on a random sample of 1,000 texts from the 2025 test, scored with prompts derived from 2024 data without retraining (Fig. 5). The article reports "the observed performance variations with respect to 2024 were very small."

> "Figure 5 presents the results, showing that the observed performance variations with respect to 2024 were very small. This is a relevant finding, as it indicates that prompts developed for one year's assessment can generalize to another year's test without major effort"

## Discussion


## Related Claims
- Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign — related
- [AI scoring consistency approaches or exceeds 90% for most rubric items, but spelling is replaced by a deterministic LanguageTool-based approach achieving 68% accuracy with 100% consistency](ai-consistency-high-except-spelling-languagetool-replacement.md) — related
