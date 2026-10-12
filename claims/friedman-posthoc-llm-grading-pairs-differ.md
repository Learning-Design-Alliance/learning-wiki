---
type: claim
title: Statistical tests show significant grading differences among nearly all pairs of LLMs, with only 7 of 153 pairs statistically indistinguishable
description: Statistical tests show significant grading differences among nearly all pairs of LLMs, with only 7 of 153 pairs statistically indistinguishable
id: friedman-posthoc-llm-grading-pairs-differ
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: marcin-jukiewicz-2025
    resource: "https://arxiv.org/abs/2509.26483"
    title: "Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483"
    author: Marcin Jukiewicz
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: marcin-jukiewicz-2025-2
    resource: "https://arxiv.org/abs/2509.26483"
    title: "Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483"
    author: Marcin Jukiewicz
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Statistical tests show significant grading differences among nearly all pairs of LLMs, with only 7 of 153 pairs statistically indistinguishable

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` The Friedman test revealed significant differences among models' grading scores (χ²(17) = 10630.24, p<0.001). [→ Marcin Jukiewicz 2025](#marcin-jukiewicz-2025)
`q2 i?` Conover post hoc tests with Holm and Holm-Sidak corrections found significant differences for approximately 95% of the 153 model pairs; only 7 pairs showed no significant difference. [→ Marcin Jukiewicz 2025 (2)](#marcin-jukiewicz-2025-2)

## Evidence

### Marcin Jukiewicz 2025

Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483

`q2 · i?` · `design · r2`

Omnibus statistical comparison of grade scores across all 18 models on the same submissions. The article reports the Friedman test "revealed significant differences among the performance scores of the evaluated language models (χ2(17) = 10630.24,p<0.001)".

> "The Friedman test revealed significant differences among the performance scores of the evaluated language models (χ2
(17) = 10630.24,p<0.001)."

### Marcin Jukiewicz 2025 (2)

Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483

`q2 · i?` · `associational · r2`

Post hoc Conover tests with Holm and Holm-Sidak corrections across all pairwise model comparisons. The study reports that "only 7 pairs did not exhibit a statistically significant difference in evaluation scores", with the same pairs non-significant under both corrections (Table 4).

> "out of all pairwise model comparisons (18 models, totaling
153 pairs), only 7 pairs did not exhibit a statistically significant difference in evaluation scores (p≥0.05after correction)."

## Discussion


## Related Claims
- [GenAI models' grades differ significantly across models, with GPTo1 grading more leniently than Llama2, Mistral7B and Cohere](genai-grade-differences-wilcoxon.md) — possibly the same claim (merge candidate)
