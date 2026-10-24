---
type: claim
title: LLM grading patterns cluster into six groups aligned with vendor families, with highest correlations within same-vendor model families
description: LLM grading patterns cluster into six groups aligned with vendor families, with highest correlations within same-vendor model families
id: llm-grading-vendor-specific-six-clusters
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: marcin-jukiewicz-2025
    resource: "https://doi.org/10.48550/arxiv.2509.26483"
    title: "Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483 [doi:10.48550/arxiv.2509.26483](https://doi.org/10.48550/arxiv.2509.26483)"
    author: Marcin Jukiewicz
    q: 2
    i: 3
    kind: associational
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

# LLM grading patterns cluster into six groups aligned with vendor families, with highest correlations within same-vendor model families

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Spearman correlations between models' grading patterns range from approximately 0.55 to 0.89, with the highest values within same-vendor families such as the gpt-5 group (ρ≈0.80–0.89) and the Gemini family (ρ≈0.79–0.83). [→ Marcin Jukiewicz 2025](#marcin-jukiewicz-2025)
`q2 i?` K-means and hierarchical clustering identified six well-separated clusters of models with similar scoring styles, including gpt-5, gpt-4, Gemini, DeepSeek, Claude, and an outlier cluster. [→ Marcin Jukiewicz 2025 (2)](#marcin-jukiewicz-2025-2)

## Evidence

### Marcin Jukiewicz 2025

Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483 [doi:10.48550/arxiv.2509.26483](https://doi.org/10.48550/arxiv.2509.26483)

`q2 · i3` · `associational · r2`

Correlation analysis of grading patterns across 18 LLMs on the same 6,081 submissions. The study reports coefficients "ranging from approximately 0.55 to 0.89", with the highest within vendor families (gpt-5 group ρ≈0.80–0.89; Gemini ρ≈0.79–0.83) and lowest for claude-haiku-3.5 and gpt-4.1-nano (0.55–0.68).

> "The Spearman rank correlation analysis (Figure 2) reveals that all models exhibit positive associations in their grading behavior, with coefficients ranging from approximately 0.55 to 0.89."

### Marcin Jukiewicz 2025 (2)

Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483

`q2 · i?` · `associational · r2`

K-means clustering of grade distributions with silhouette scores for k from 2 to 17, plus hierarchical clustering on 1−ρ distance. The "silhouette coefficient... reacheditsmaximumatk= 6", yielding gpt-5, gpt-4, Gemini, DeepSeek, Claude, and outlier clusters consistent across both methods.

> "The silhouette coefficient, measuringcohesionandseparation, reacheditsmaximumatk= 6 (approximately0.5), suggesting a transparent partition of the data into six well-separated groups."

## Discussion


## Related Claims
- [Word count correlates with suggested final grade, with the ordering Gemini Pro > humans > ChatGPT > Gemini among statistically significant correlations (human Spearman's rho = 0.603)](wordcount-grade-correlation-llm-human.md) — related
- [LLM-generated difficulty ratings show only moderate rank alignment with empirical student performance on basic arithmetic items](llm-difficulty-moderate-rank-alignment-arithmetic.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [LLMs differ systematically in grading strictness, forming liberal, restrictive, and balanced grading styles on programming assignments](llms-differ-liberal-restrictive-balanced-grading-styles.md) — related
- [Causal discovery analysis finds four of five LLMs prioritize lexical features in scoring, while DeepSeek R1 uniquely prioritizes syntactic complexity](llm-causal-feature-dependencies-lexical-versus-syntactic.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [gpt-4o graded student submissions most correctly in almost all assignments, but gemini-1.0-pro graded the boolean-algebra assignment most correctly](grader-llm-correctness-comparison-socrates.md) — related
