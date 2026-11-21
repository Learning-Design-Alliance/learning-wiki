---
type: claim
title: A two-pass extraction-then-filtering architecture eliminated bimodal output in LLM question identification over lecture transcripts
description: A two-pass extraction-then-filtering architecture eliminated bimodal output in LLM question identification over lecture transcripts
id: two-pass-architecture-bimodal-question-extraction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: eric-m-furst-and-vasudevan-venkateshwaran-2026
    resource: "https://doi.org/10.48550/arXiv.2603.04657"
    title: "Eric M. Furst and Vasudevan Venkateshwaran. (2026). Stan: An LLM-based thermodynamics course assistant. [doi:10.48550/arXiv.2603.04657](https://doi.org/10.48550/arXiv.2603.04657)"
    author: Eric M. Furst and Vasudevan Venkateshwaran
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: eric-m-furst-and-vasudevan-venkateshwaran-2026-2
    resource: "https://doi.org/10.48550/arXiv.2603.04657"
    title: "Eric M. Furst and Vasudevan Venkateshwaran. (2026). Stan: An LLM-based thermodynamics course assistant. [doi:10.48550/arXiv.2603.04657](https://doi.org/10.48550/arXiv.2603.04657)"
    author: Eric M. Furst and Vasudevan Venkateshwaran
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A two-pass extraction-then-filtering architecture eliminated bimodal output in LLM question identification over lecture transcripts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` With a one-shot prompt, question extraction output was sharply bimodal: 26 of 35 lectures produced exactly 8 questions each while 5 lectures produced 64–108 questions. [→ Eric M. Furst and Vasudevan Venkateshwaran 2026](#eric-m-furst-and-vasudevan-venkateshwaran-2026)
`q2 i?` Decomposing into an extraction pass and a filtering pass made the output distribution smooth (range 2–15, mean 8.8) and eliminated the bimodal failure entirely. [→ Eric M. Furst and Vasudevan Venkateshwaran 2026 (2)](#eric-m-furst-and-vasudevan-venkateshwaran-2026-2)

## Evidence

### Eric M. Furst and Vasudevan Venkateshwaran 2026

Eric M. Furst and Vasudevan Venkateshwaran. (2026). Stan: An LLM-based thermodynamics course assistant. [doi:10.48550/arXiv.2603.04657](https://doi.org/10.48550/arXiv.2603.04657)

`q2 · i?` · `design · r2`

Structured-extraction deployment analysis using Llama 3.1 8B over 35 lecture transcripts: the one-shot composite task produced a bimodal distribution, with "26 of 35 lectures produced exactly 8 questions each" in a formulaic mode and 5 lectures exhaustively extracting every exchange. No effect size is printed.

> "the output distribution was sharply bimodal: 26 of 35 lectures produced exactly 8 questions each (with fabricated timestamps, uniform classification, and evenly spaced entries), while 5 lectures produced 64–108 questions"

### Eric M. Furst and Vasudevan Venkateshwaran 2026 (2)

Eric M. Furst and Vasudevan Venkateshwaran. (2026). Stan: An LLM-based thermodynamics course assistant. [doi:10.48550/arXiv.2603.04657](https://doi.org/10.48550/arXiv.2603.04657)

`q2 · i?` · `design · r2`

The two-pass architecture (Pass 1 high-recall extraction with verbatim quotes; Pass 2 classification and filtering on a much shorter candidate list) resolved the failure; the article notes it doubled per-lecture processing time but eliminated the bimodal failure entirely.

> "With this decomposition, the output distribution became smooth (range 2–15, mean 8.8, no clustering), candidate counts varied naturally across lectures (2–46), and the filter pass demonstrably reduced over-extracted lectures"

## Discussion


## Related Claims
- [All four evaluated LLMs produce strongly bimodal item-level score distributions on bash exams, and rubric-enhanced prompts amplify the near-perfect-score peak](llm-bash-score-distributions-bimodal-v2-amplifies.md) — related
