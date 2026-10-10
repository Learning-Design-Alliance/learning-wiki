---
type: claim
title: A VLM-based screenplay-to-video fidelity proxy shows scene and element structure are usually preserved while action-level fidelity is the primary failure mode
description: A VLM-based screenplay-to-video fidelity proxy shows scene and element structure are usually preserved while action-level fidelity is the primary failure mode
id: anvil-video-fidelity-proxy-action-failure
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: noviello-2026
    resource: "https://arxiv.org/abs/2605.16295"
    title: "Noviello, Y., Birillo, A., Migut, G. (2026). ANVIL: Analogies and Videos for Lecturers. https://arxiv.org/abs/2605.16295"
    author: Noviello, Y., Birillo, A., Migut, G.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A VLM-based screenplay-to-video fidelity proxy shows scene and element structure are usually preserved while action-level fidelity is the primary failure mode

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across n=50 screenplay-animation pairs, 94% of videos met the Scene Fidelity threshold and 88% met Element Fidelity, but only 52% met Action Fidelity, with mean scores of 3.44±0.67, 2.96±0.53, and 2.52±0.58 respectively. [→ Noviello 2026](#noviello-2026)

## Evidence

### Noviello 2026

Noviello, Y., Birillo, A., Migut, G. (2026). ANVIL: Analogies and Videos for Lecturers. https://arxiv.org/abs/2605.16295

`q2 · i?` · `design · r2`

Automated audit in which a VLM (gemini-3.0-pro) reconstructs an observed screenplay from each rendered video and an LLM-based fidelity judge (three gpt-5.2 runs averaged) scores Scene, Element, and Action Fidelity on 4-point scales for n=50 pairs.

> "Most videos met the threshold forScene Fidelity(94%) andElement Fidelity(88%), whereas only52%met the threshold forAction Fidelity under the collapsed two-level label. Mean scores showed the same pattern: scene alignment was high (3.44±0.67) and element alignment was generally strong (2.96±0.53), but action realization was lower (2.52±0.58)"

## Discussion


## Related Claims
- [CS/SE educators rate ANVIL analogies highly and animations as generally faithful, with disagreement concentrated in borderline and visual-clarity judgments](anvil-educator-ratings-analogy-animation-quality.md) — related
- [Educators identify a risk of pedagogical mismatch when generated animations fail to preserve key constraints of the target concept](anvil-pedagogical-mismatch-risk.md) — related
- [Students' primary concerns about AI videos are inaccurate information, reduced interaction with educators, and diminished educational value](student-concerns-ai-videos-quality-interaction-value.md) — related
