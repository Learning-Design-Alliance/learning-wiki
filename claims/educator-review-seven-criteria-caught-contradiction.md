---
type: claim
title: Educator review of LLM-generated lesson material addressed seven criteria derived from generation records and caught a self-contradictory worked example before delivery
description: Educator review of LLM-generated lesson material addressed seven criteria derived from generation records and caught a self-contradictory worked example before delivery
id: educator-review-seven-criteria-caught-contradiction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: gendo-kumoi-2026
    resource: "https://doi.org/10.48550/arxiv.2607.12235"
    title: "Gendo Kumoi, Fumie Watanabe, Tota Suko, Takashi Ishida, Yuko Kuma, Manabu Kobayashi, and Shigeichi Hirasawa. (2026). A Semi-Automated System for Generating Dialogue-Based TTS Lessons Using Large Language Models: An Exploratory Study of Educational Potential. Preprint, under review at IEEE Access. https://arxiv.org/abs/2607.12235 [doi:10.48550/arxiv.2607.12235](https://doi.org/10.48550/arxiv.2607.12235)"
    author: Gendo Kumoi, Fumie Watanabe, Tota Suko, Takashi Ishida, Yuko Kuma, Manabu Kobayashi, and Shigeichi Hirasawa
    q: 2
    i: "?"
    kind: qualitative
    rigour: 2
  - id: gendo-kumoi-2026-2
    resource: "https://arxiv.org/abs/2607.12235"
    title: "Gendo Kumoi, Fumie Watanabe, Tota Suko, Takashi Ishida, Yuko Kuma, Manabu Kobayashi, and Shigeichi Hirasawa. (2026). A Semi-Automated System for Generating Dialogue-Based TTS Lessons Using Large Language Models: An Exploratory Study of Educational Potential. Preprint, under review at IEEE Access. https://arxiv.org/abs/2607.12235"
    author: Gendo Kumoi, Fumie Watanabe, Tota Suko, Takashi Ishida, Yuko Kuma, Manabu Kobayashi, and Shigeichi Hirasawa
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Educator review of LLM-generated lesson material addressed seven criteria derived from generation records and caught a self-contradictory worked example before delivery

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`

## Subclaims
`q2 i?` Across two lessons the educator issued twelve revision instructions over five rounds, organized into seven criteria including completeness, technical viability, factual accuracy, provenance, fit to delivery mode, fit to the learner, and audio continuity. [→ Gendo Kumoi 2026](#gendo-kumoi-2026)
`q2 i?` Review caught an internal contradiction in a generated worked example, in which a candidate was declared admissible while recorded as violating the admissibility condition, and corrected it before delivery. [→ Gendo Kumoi 2026 (2)](#gendo-kumoi-2026-2)

## Evidence

### Gendo Kumoi 2026

Gendo Kumoi, Fumie Watanabe, Tota Suko, Takashi Ishida, Yuko Kuma, Manabu Kobayashi, and Shigeichi Hirasawa. (2026). A Semi-Automated System for Generating Dialogue-Based TTS Lessons Using Large Language Models: An Exploratory Study of Educational Potential. Preprint, under review at IEEE Access. https://arxiv.org/abs/2607.12235 [doi:10.48550/arxiv.2607.12235](https://doi.org/10.48550/arxiv.2607.12235)

`q2 · i?` · `qualitative · r2`

Document-record analysis of the complete generation logs of the two lessons produced through the workflow, comparing raw LLM output, educator instructions, and the delivered version. The criteria were derived from the record rather than specified in advance.

> "Across the two lessons the educator issued twelve revision instructions over five rounds, and made further changes directly in the files. Table 3 organizes these into seven criteria."

### Gendo Kumoi 2026 (2)

Gendo Kumoi, Fumie Watanabe, Tota Suko, Takashi Ishida, Yuko Kuma, Manabu Kobayashi, and Shigeichi Hirasawa. (2026). A Semi-Automated System for Generating Dialogue-Based TTS Lessons Using Large Language Models: An Exploratory Study of Educational Potential. Preprint, under review at IEEE Access. https://arxiv.org/abs/2607.12235

`q2 · i?` · `causal · r1`

Case analysis of one substantive correction in the generated worked example: the educator corrected the distance in the comparison table and changed the stated ground of exclusion so the exclusion follows from a criterion the candidate genuinely fails.

> "The example thus declared a candidate admissible and simultaneously recorded it as violating the admissibility condition, and the accompanying narration excluded that candidate by appeal to the very condition it had said was met."

## Discussion


## Related Claims
- [Lesson designers identify generic feedback and unclear title-page and instruction sections as key weaknesses of LLM-generated lessons](llm-lesson-weaknesses-generic-feedback-clarity.md) — related
- [LLM-generated lessons produced inauthentic references even when combined with RAG over verified academic papers](rag-does-not-ensure-citation-authenticity.md) — related
