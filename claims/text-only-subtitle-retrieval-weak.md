---
type: claim
title: Text-only retrieval over subtitles remains weak for concept-to-example retrieval, suggesting subtitles alone miss visually expressed teaching evidence
description: Text-only retrieval over subtitles remains weak for concept-to-example retrieval, suggesting subtitles alone miss visually expressed teaching evidence
id: text-only-subtitle-retrieval-weak
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: haiming-zhao-2026
    resource: "https://doi.org/10.48550/arXiv.2610.00973"
    title: "Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li. (2026). Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack. arXiv preprint. [doi:10.48550/arXiv.2610.00973](https://doi.org/10.48550/arXiv.2610.00973)"
    author: Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Text-only retrieval over subtitles remains weak for concept-to-example retrieval, suggesting subtitles alone miss visually expressed teaching evidence

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Text-only baselines (BM25, CN-CLIP_text, KBERT) score lowest on pedagogical hits, indicating subtitles alone miss visually expressed teaching evidence. [→ Haiming Zhao 2026](#haiming-zhao-2026)

## Evidence

### Haiming Zhao 2026

Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li. (2026). Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack. arXiv preprint. [doi:10.48550/arXiv.2610.00973](https://doi.org/10.48550/arXiv.2610.00973)

`q2 · i?` · `design · r2`

Comparison in Table 2 where text-only baselines over subtitles (BM25 with 10, KBERT with 9 pedagogical points) trail all multimodal methods on the same 146-segment candidate pool with five concept queries.

> "Text-only baselines remain weak, suggesting that subtitles alone miss visually expressed teaching evidence."

## Discussion


## Related Claims
- [CDDA achieves stronger pedagogically oriented concept retrieval than open or trainable multimodal baselines on a middle-school physics documentary benchmark](cdda-outperforms-baselines-concept-retrieval.md) — related
- [Visually heterogeneous curriculum concepts benefit most from concept-level alignment: CDDA retrieves 5 of 6 Force segments where multimodal baselines retrieve at most 2](heterogeneous-concepts-benefit-concept-alignment.md) — related
- [Standard semantic retrieval alone does not reliably recover the pedagogically required chunk types, with comparison chunks retrieved worst (14.3% on the real corpus)](semantic-retrieval-insufficient-pedagogical-content.md) — a broader claim this one bears on
- [Reviewer free-text comments identified synthetic voice, slide–narration reveal timing, and slide layout as the main remaining quality issues](bespoke-free-text-voice-reveal-layout-issues.md) — related
- [Stage 1 textual concept structuring is the main source of CDDA's retrieval gains; removing it degrades all reported metrics](stage1-text-structuring-drives-gains.md) — related
