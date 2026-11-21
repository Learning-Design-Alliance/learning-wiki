---
type: claim
title: Domain-prompted Whisper and institutional Kaltura transcripts were similar in aggregate word counts but differed in contextual fidelity
description: Domain-prompted Whisper and institutional Kaltura transcripts were similar in aggregate word counts but differed in contextual fidelity
id: kaltura-whisper-transcript-comparison-contextual-fidelity
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

# Domain-prompted Whisper and institutional Kaltura transcripts were similar in aggregate word counts but differed in contextual fidelity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across six matched lectures, word counts were within 1% between Kaltura and domain-prompted Whisper transcripts, and high-frequency domain terms appeared at nearly identical rates. [→ Eric M. Furst and Vasudevan Venkateshwaran 2026](#eric-m-furst-and-vasudevan-venkateshwaran-2026)
`q2 i?` The real difference lies in contextual fidelity: Kaltura produced phonetically plausible but semantically nonsensical substitutions while the domain-prompted Whisper transcript preserved intended meaning. [→ Eric M. Furst and Vasudevan Venkateshwaran 2026 (2)](#eric-m-furst-and-vasudevan-venkateshwaran-2026-2)

## Evidence

### Eric M. Furst and Vasudevan Venkateshwaran 2026

Eric M. Furst and Vasudevan Venkateshwaran. (2026). Stan: An LLM-based thermodynamics course assistant. [doi:10.48550/arXiv.2603.04657](https://doi.org/10.48550/arXiv.2603.04657)

`q2 · i?` · `design · r2`

Comparison of institutional Kaltura ASR transcripts against domain-prompted Whisper transcripts for six matched lecture pairs (lectures 26–31), matched by a shared recording identifier. The article reports word counts "within 1% for all six lectures"; no effect size is printed.

> "At the aggregate level, the two systems are remarkably similar. Table III summarizes the comparison. Word counts are within 1% for all six lectures."

### Eric M. Furst and Vasudevan Venkateshwaran 2026 (2)

Eric M. Furst and Vasudevan Venkateshwaran. (2026). Stan: An LLM-based thermodynamics course assistant. [doi:10.48550/arXiv.2603.04657](https://doi.org/10.48550/arXiv.2603.04657)

`q2 · i?` · `design · r2`

Passage-level comparison from lecture 9 (Table IV): Kaltura produced semantically nonsensical substitutions (e.g. "liquid versus gaffy") while Whisper preserved intended meaning. The article also notes Whisper's sentence-level segmentation with timestamps enables downstream analyses that unsegmented Kaltura text cannot support.

> "The real difference lies incontextual fidelity—the accuracy of words surrounding the domain terms and the recognition of less common scientific vocabulary."

## Discussion


## Related Claims
- [Domain vocabulary prompting substantially improved recognition of specialized thermodynamics terms in lecture transcription](domain-vocabulary-prompting-whisper-technical-terms.md) — related
- [A three-layer mitigation strategy reduced Whisper hallucination loops from 6.4% of segments to 0.02% across a lecture corpus](whisper-hallucination-loop-mitigation-transcripts.md) — related
