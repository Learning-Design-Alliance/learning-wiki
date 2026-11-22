---
type: claim
title: "Stage 1 textual concept structuring is the main source of CDDA's retrieval gains; removing it degrades all reported metrics"
description: "Stage 1 textual concept structuring is the main source of CDDA's retrieval gains; removing it degrades all reported metrics"
id: stage1-text-structuring-drives-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: haiming-zhao-2026
    resource: "https://doi.org/10.48550/arXiv.2610.00973"
    title: "Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li. (2026). Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack. arXiv preprint. [doi:10.48550/arXiv.2610.00973](https://doi.org/10.48550/arXiv.2610.00973)"
    author: Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: haiming-zhao-2026-2
    resource: "https://doi.org/10.48550/arXiv.2610.00973"
    title: "Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li. (2026). Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack. arXiv preprint. [doi:10.48550/arXiv.2610.00973](https://doi.org/10.48550/arXiv.2610.00973)"
    author: Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Stage 1 textual concept structuring is the main source of CDDA's retrieval gains; removing it degrades all reported metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Removing Stage 1 reduces MAP@10 from 0.3848 to 0.2974, NDCG@10 from 0.5402 to 0.4309, and the pedagogical score from 24 to 20. [→ Haiming Zhao 2026](#haiming-zhao-2026)
`q2 i?` Replacing concept labels with literal descriptions performs worse than concept-level supervision. [→ Haiming Zhao 2026 (2)](#haiming-zhao-2026-2)

## Evidence

### Haiming Zhao 2026

Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li. (2026). Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack. arXiv preprint. [doi:10.48550/arXiv.2610.00973](https://doi.org/10.48550/arXiv.2610.00973)

`q2 · i?` · `causal · r1`

Ablation on the same 146-segment physics retrieval benchmark comparing full CDDA with CDDA(II&III), which removes Stage 1 textual concept structuring and trains only with image-concept pairs.

> "Removing Stage 1 reduces MAP@10 from 0.3848 to 0.2974, NDCG@10 from 0.5402 to 0.4309, and the pedagogical score from 24 to 20."

### Haiming Zhao 2026 (2)

Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li. (2026). Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack. arXiv preprint. [doi:10.48550/arXiv.2610.00973](https://doi.org/10.48550/arXiv.2610.00973)

`q2 · i?` · `causal · r1`

Ablation variants that replace abstract concept labels with literal fact descriptions or description-plus-concept text score 12 and 13 pedagogical points versus 24 for full CDDA, indicating the gain comes from structuring the text space with example-concept supervision.

> "Replacing concept labels with literal descriptions performs worse: CDDA(II&III)d reaches 12 pedagogical points, and appending concept words to descriptions, CDDA(II&III)d+c, reaches only 13."

## Discussion


## Related Claims
- [CDDA achieves stronger pedagogically oriented concept retrieval than open or trainable multimodal baselines on a middle-school physics documentary benchmark](cdda-outperforms-baselines-concept-retrieval.md) — a broader claim this one bears on
- [Visually heterogeneous curriculum concepts benefit most from concept-level alignment: CDDA retrieves 5 of 6 Force segments where multimodal baselines retrieve at most 2](heterogeneous-concepts-benefit-concept-alignment.md) — related
- [Text-only retrieval over subtitles remains weak for concept-to-example retrieval, suggesting subtitles alone miss visually expressed teaching evidence](text-only-subtitle-retrieval-weak.md) — related
