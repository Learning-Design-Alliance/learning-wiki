---
type: claim
title: CDDA achieves stronger pedagogically oriented concept retrieval than open or trainable multimodal baselines on a middle-school physics documentary benchmark
description: CDDA achieves stronger pedagogically oriented concept retrieval than open or trainable multimodal baselines on a middle-school physics documentary benchmark
id: cdda-outperforms-baselines-concept-retrieval
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
    kind: design
    rigour: 2
  - id: haiming-zhao-2026-2
    resource: "https://doi.org/10.48550/arXiv.2610.00973"
    title: "Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li. (2026). Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack. arXiv preprint. [doi:10.48550/arXiv.2610.00973](https://doi.org/10.48550/arXiv.2610.00973)"
    author: Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CDDA achieves stronger pedagogically oriented concept retrieval than open or trainable multimodal baselines on a middle-school physics documentary benchmark

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On top-10 pedagogical hits over five concept queries, CDDA ties Gemini Embedding 2 and outperforms the open or trainable baselines under the same candidate pool. [→ Haiming Zhao 2026](#haiming-zhao-2026)
`q2 i?` Compared with Qwen3-VL-2B, CDDA improves MAP@10 from 0.3723 to 0.3848 and NDCG@5 from 0.4814 to 0.5094. [→ Haiming Zhao 2026 (2)](#haiming-zhao-2026-2)

## Evidence

### Haiming Zhao 2026

Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li. (2026). Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack. arXiv preprint. [doi:10.48550/arXiv.2610.00973](https://doi.org/10.48550/arXiv.2610.00973)

`q2 · i?` · `design · r2`

Evaluation on a curated benchmark of 146 candidate segments from one held-out documentary with five curriculum concept queries and expert-verified relevance labels; CDDA scores 24 pedagogical points, tying Gemini Embedding 2 and beating open baselines.

> "Table 2 shows that CDDA ties Gemini Embedding 2 in pedagogical score and outperforms the open or trainable baselines under the same candidate pool."

### Haiming Zhao 2026 (2)

Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li. (2026). Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack. arXiv preprint. [doi:10.48550/arXiv.2610.00973](https://doi.org/10.48550/arXiv.2610.00973)

`q2 · i?` · `design · r2`

Standard ranking metrics averaged over the five concept queries on the same 146-segment corpus; the article reports these MAP and NDCG improvements as evidence that concept-driven adaptation improves early ranking quality.

> "Compared with Qwen3-VL-2B, CDDA improves MAP@10 from 0.3723 to 0.3848 and NDCG@5 from 0.4814 to 0.5094; compared with ImageBind, it improves MAP@10 by 0.1059 and NDCG@10 by 0.1241."

## Discussion


## Related Claims
- [Visually heterogeneous curriculum concepts benefit most from concept-level alignment: CDDA retrieves 5 of 6 Force segments where multimodal baselines retrieve at most 2](heterogeneous-concepts-benefit-concept-alignment.md) — a narrower finding that bears on this claim
- [Text-only retrieval over subtitles remains weak for concept-to-example retrieval, suggesting subtitles alone miss visually expressed teaching evidence](text-only-subtitle-retrieval-weak.md) — related
- [Stage 1 textual concept structuring is the main source of CDDA's retrieval gains; removing it degrades all reported metrics](stage1-text-structuring-drives-gains.md) — a narrower finding that bears on this claim
- [On a preliminary three-question retrieval sanity check, all seed questions placed their target concept first and within the top three, with mean top-5 recall of 1.00](three-seed-retrieval-sanity-check-perfect.md) — related
- [Concept adaptation preserves concrete image-description matching while improving image-concept decisions](cdda-preserves-concrete-alignment.md) — related
