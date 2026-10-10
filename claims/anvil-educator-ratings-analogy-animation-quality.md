---
type: claim
title: CS/SE educators rate ANVIL analogies highly and animations as generally faithful, with disagreement concentrated in borderline and visual-clarity judgments
description: CS/SE educators rate ANVIL analogies highly and animations as generally faithful, with disagreement concentrated in borderline and visual-clarity judgments
id: anvil-educator-ratings-analogy-animation-quality
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
    q: 3
    i: "?"
    kind: design
    rigour: 2
  - id: noviello-2026-2
    resource: "https://arxiv.org/abs/2605.16295"
    title: "Noviello, Y., Birillo, A., Migut, G. (2026). ANVIL: Analogies and Videos for Lecturers. https://arxiv.org/abs/2605.16295"
    author: Noviello, Y., Birillo, A., Migut, G.
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# CS/SE educators rate ANVIL analogies highly and animations as generally faithful, with disagreement concentrated in borderline and visual-clarity judgments

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`

## Subclaims
`q3 i?` In a rubric-based evaluation with 11 CS/SE educators across nine CS topics, analogy criteria TCC and MS had medians of 3-4 for most topics (BST lower), animations showed high ATA medians, and VC medians were generally 3 with lower clarity for Stack. [→ Noviello 2026](#noviello-2026)
`q3 i?` Inter-rater agreement on 4-point ordinal ratings was low (Krippendorff's alpha at or below 0.15), but Gwet's AC1 on collapsed binary labels indicated substantial agreement for TCC (0.77), ATA (0.75), and MS (0.71), and moderate agreement for VC (0.45). [→ Noviello 2026 (2)](#noviello-2026-2)

## Evidence

### Noviello 2026

Noviello, Y., Birillo, A., Migut, G. (2026). ANVIL: Analogies and Videos for Lecturers. https://arxiv.org/abs/2605.16295

`q3 · i?` · `design · r2`

Rubric-based human evaluation in which 11 CS/SE educators (8 university professors, 3 PhD candidates) rated nine topics' analogies and animations on 4-point Likert scales; the authors report medians and IQRs per artifact, noting "Low IQRs (usually≤1) indicate moderate consensus on fundamental correctness."

> "Analogies were generally rated highly: TCC and MS medians were 3–4 ("Strong" or "Very Strong") for most topics, withBSTas a lower-scoring case. Animations were typically faithful to the text (high ATA medians), whileVC medians were generally 3 ("Good") with lower clarity forStack."

### Noviello 2026 (2)

Noviello, Y., Birillo, A., Migut, G. (2026). ANVIL: Analogies and Videos for Lecturers. https://arxiv.org/abs/2605.16295

`q3 · i?` · `design · r2`

Agreement analysis of the same 11-educator evaluation using Krippendorff's alpha on ordinal ratings and Gwet's AC1 on collapsed binary labels (1-2 vs 3-4); collapsed exact agreement rose to 66.9-81.0% while alpha remained low due to label prevalence.

> "Inter-rater agreementwas low on the 4-point ordinal ratings (α≤0.15), with exact agreement between 36.8% and 45.7%, where most disagreements occurred between adjacent high scores (i.e., 3 vs. 4)."

## Discussion


## Related Claims
- [An LLM-based analogy judge validated against expert judgments shows moderate-to-strong agreement and screens most generated analogies as meeting baseline adequacy](anvil-llm-judge-analogy-screening.md) — related
- [Educators identify a risk of pedagogical mismatch when generated animations fail to preserve key constraints of the target concept](anvil-pedagogical-mismatch-risk.md) — related
- [Educators view ANVIL as a creative collaborator requiring instructor control and editability, not an autonomous content creator](anvil-educators-instructor-control-editability.md) — related
- [A VLM-based screenplay-to-video fidelity proxy shows scene and element structure are usually preserved while action-level fidelity is the primary failure mode](anvil-video-fidelity-proxy-action-failure.md) — related
