---
type: claim
title: Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability
description: Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability
id: llm-grading-moderate-human-agreement-icc
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: marcin-jukiewicz-2025
    resource: "https://doi.org/10.48550/arxiv.2509.26483"
    title: "Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483 [doi:10.48550/arxiv.2509.26483](https://doi.org/10.48550/arxiv.2509.26483)"
    author: Marcin Jukiewicz
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The highest human-model agreement was claude-haiku-3.5 at ICC(2,1) = 0.470 (moderate); the lowest was gpt-4.1-nano at 0.204 (slight); all values below 0.5 formally indicate poor reliability. [→ Marcin Jukiewicz 2025](#marcin-jukiewicz-2025)

## Evidence

### Marcin Jukiewicz 2025

Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483 [doi:10.48550/arxiv.2509.26483](https://doi.org/10.48550/arxiv.2509.26483)

`q2 · i?` · `design · r2`

Comparison of each model's grades with human teachers' grades using ICC(2,1) over the 6,081 submissions (Table 5). The study reports claude-haiku-3.5 achieved "an ICC value of 0.470, corresponding to a moderate level of agreement", and that all values below 0.5 formally indicate poor reliability, below the ICC≥0.75 'good' threshold.

> "The highest level of agreement was obtained by claude-haiku-3.5, with an ICC value of 0.470, corresponding to a moderate level of agreement. This is the highest score among the compared models."

## Discussion

## Related Claims

- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — the general claim this finding bears on, with the studies behind it
- [Sentence embedding models reach only moderate agreement and need human supervision for open-ended grading](embedding-models-moderate-agreement-need-supervision.md) — related
- [Full-scale LLM versions consistently achieve higher agreement with human grades than their mini and nano counterparts](full-scale-llms-outperform-mini-nano-grading.md) — related
- [LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades](llm-high-consensus-agreement-circularity-risk.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [LLMs differ systematically in grading strictness, forming liberal, restrictive, and balanced grading styles on programming assignments](llms-differ-liberal-restrictive-balanced-grading-styles.md) — related
- [Teachers systematically assign higher grades than all evaluated LLM grading models](teachers-grade-higher-than-all-llm-models.md) — related
- [Llama 4 Maverick shows the strongest human-LLM alignment, while Claude Sonnet 4 performs weakest with poor calibration](llama-strongest-human-llm-alignment-claude-weakest.md) — related
- [Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades](claude3-palm2-substantial-agreement-failing-grades.md) — reports the opposite
