---
type: claim
title: "Manually verified numerical accuracy of generated visuals is lowest under pre-generation control (12.2%), intermediate under mid-generation control (59.83%), and highest under post-generation control (97.85%)"
description: "Manually verified numerical accuracy of generated visuals is lowest under pre-generation control (12.2%), intermediate under mid-generation control (59.83%), and highest under post-generation control (97.85%)"
id: manual-verification-accuracy-by-control-timing
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: zhengxu-li-2026
    resource: "https://doi.org/10.48550/arxiv.2605.10672"
    title: "Zhengxu Li, Junling Wang, and April Yi Wang. (2026). When Should Teachers Control AI Generation for Mathematics Visuals? arXiv preprint. https://arxiv.org/abs/2605.10672 [doi:10.48550/arxiv.2605.10672](https://doi.org/10.48550/arxiv.2605.10672)"
    author: Zhengxu Li, Junling Wang, and April Yi Wang
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: zhengxu-li-2026-2
    resource: "https://arxiv.org/abs/2605.10672"
    title: "Zhengxu Li, Junling Wang, and April Yi Wang. (2026). When Should Teachers Control AI Generation for Mathematics Visuals? arXiv preprint. https://arxiv.org/abs/2605.10672"
    author: Zhengxu Li, Junling Wang, and April Yi Wang
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: zhengxu-li-2026-3
    resource: "https://arxiv.org/abs/2605.10672"
    title: "Zhengxu Li, Junling Wang, and April Yi Wang. (2026). When Should Teachers Control AI Generation for Mathematics Visuals? arXiv preprint. https://arxiv.org/abs/2605.10672"
    author: Zhengxu Li, Junling Wang, and April Yi Wang
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Manually verified numerical accuracy of generated visuals is lowest under pre-generation control (12.2%), intermediate under mid-generation control (59.83%), and highest under post-generation control (97.85%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q3`

## Subclaims
`q3 i?` Manual verification of generated images found only 11 of 90 pre-gen images contained the correct number of objects (accuracy 12.2%). [→ Zhengxu Li 2026](#zhengxu-li-2026)
`q3 i?` Manual verification found 70 of 117 mid-gen images contained the correct number of objects (accuracy 59.83%). [→ Zhengxu Li 2026 (2)](#zhengxu-li-2026-2)
`q3 i?` Manual verification found only 2 of 93 post-gen images were numerically incorrect (accuracy 97.85%). [→ Zhengxu Li 2026 (3)](#zhengxu-li-2026-3)

## Evidence

### Zhengxu Li 2026

Zhengxu Li, Junling Wang, and April Yi Wang. (2026). When Should Teachers Control AI Generation for Mathematics Visuals? arXiv preprint. https://arxiv.org/abs/2605.10672 [doi:10.48550/arxiv.2605.10672](https://doi.org/10.48550/arxiv.2605.10672)

`q3 · i?` · `causal · r2`

Manual verification of images generated in the 24-teacher within-subject study. The authors report that only 11 of 90 pre-gen images "contained the correct number of objects specified in the prompt (accuracy: 12.2%)". No effect size printed.

> "Based on manual verification of the 90 images generated using pre-gen control across all participants, only 11 images contained the correct number of objects specified in the prompt (accuracy: 12.2%)."

### Zhengxu Li 2026 (2)

Zhengxu Li, Junling Wang, and April Yi Wang. (2026). When Should Teachers Control AI Generation for Mathematics Visuals? arXiv preprint. https://arxiv.org/abs/2605.10672

`q3 · i?` · `causal · r2`

Manual verification of mid-gen images in the same study: 70 of 117 images "contained the correct number of objects (accuracy: 59.83%)". Fifteen participants appreciated that layouts helped encode structure but still verified final images. No effect size printed.

> "Based on manual verification, 70 out of the 117 images generated using mid-gen control contained the correct number of objects (accuracy: 59.83%)."

### Zhengxu Li 2026 (3)

Zhengxu Li, Junling Wang, and April Yi Wang. (2026). When Should Teachers Control AI Generation for Mathematics Visuals? arXiv preprint. https://arxiv.org/abs/2605.10672

`q3 · i?` · `causal · r2`

Manual verification of post-gen images in the same study: of 93 images, "only 2 were numerically incorrect (accuracy: 97.85%)". Post-gen visuals are deterministic SVG objects edited directly, so no further synthesis occurs. No effect size printed.

> "In contrast, post-gen control exhibited substantially higher numerical accuracy: of the 93 images generated using post-gen control, only 2 were numerically incorrect (accuracy: 97.85%)."

## Discussion


## Related Claims
- [Primary mathematics teachers rate post-generation control significantly higher than pre- and mid-generation control on perceived numerical correctness of generated visuals](post-generation-control-higher-perceived-numerical-correctness.md) — related
