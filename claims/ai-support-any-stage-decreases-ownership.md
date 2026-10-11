---
type: claim
title: Any AI writing support decreases feelings of ownership compared to no AI support, with ownership following a gradient by stage (highest with no AI, then planning, revision, and AI-generated draft lowest).
description: Any AI writing support decreases feelings of ownership compared to no AI support, with ownership following a gradient by stage (highest with no AI, then planning, revision, and AI-generated draft lowest).
id: ai-support-any-stage-decreases-ownership
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: c1-contrast
    title: c1-contrast
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: ownership-means
    title: ownership-means
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Any AI writing support decreases feelings of ownership compared to no AI support, with ownership following a gradient by stage (highest with no AI, then planning, revision, and AI-generated draft lowest).

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q3`

## Subclaims
`q3 i?` Introducing any AI support significantly lowered ownership relative to no AI support (+1.36 Likert points, p<.001). [→ c1-contrast](#c1-contrast)
`q3 i?` Ownership followed a stage gradient: no ai highest (6.74), ai plan 6.30, ai revision 5.57, ai draft lowest (4.29). [→ ownership-means](#ownership-means)

## Evidence

### c1-contrast

Katy Ilonka Gero, Tao Long, Carly Schnitzler, and Paramveer S. Dhillon. 2026. From Planning to Revision: How AI Writing Support at Different Stages Alters Ownership. In Designing Interactive Systems Conference (DIS '26), June 13–17, 2026, Singapore, Singapore. ACM, New York, NY, USA. https://doi.org/10.1145/3800645.3813003

`q3 · i?` · `causal · r2`

Pre-planned contrast C1 from a between-subjects experiment (n=253, four conditions) on the 7-point ownership item own_primary, using prompt-adjusted means and robust standard errors. The contrast showed "no AI support had significantly higher ownership than when any AI assistance is introduced." No standardized effect size was printed.

> "The contrastC1(no-aivs. the average of all AI stages) was +1.36Lik-ert points (𝑝<. 001), indicating no AI support had significantly higher ownership than when any AI assistance is introduced."

### ownership-means

Katy Ilonka Gero, Tao Long, Carly Schnitzler, and Paramveer S. Dhillon. 2026. From Planning to Revision: How AI Writing Support at Different Stages Alters Ownership. In Designing Interactive Systems Conference (DIS '26), June 13–17, 2026, Singapore, Singapore. ACM, New York, NY, USA. https://doi.org/10.1145/3800645.3813003

`q3 · i?` · `causal · r2`

Prompt-adjusted condition means on the 1–7 ownership scale from the same experiment: "ai plan remained relatively high (6.30), ai revision was lower (5.57), and ai draft was lowest (4.29)"; no ai was highest at 6.74. Means are descriptive; only the contrast tests were inferential.

> "Ownership decreased with AI assistance and followed a clear gradient by stage: ai plan remained relatively high (6.30), ai revision was lower (5.57), and ai draft was lowest (4.29)."

## Discussion


## Related Claims
- [Essay quality was highest for AI-generated drafts and lowest with no AI, negatively correlated with ownership, suggesting an ownership-quality tradeoff.](ai-draft-quality-ownership-tradeoff.md) — related
- [AI support during drafting lowers ownership substantially more than support during planning or revision, and planning support preserves more ownership than revision support.](drafting-support-largest-ownership-decrease.md) — possibly the same claim (merge candidate)
- [AI support shifts perceived attribution of ideas and text toward the AI, most strongly for AI-generated drafts, and an AI draft based on the writer's own outline contributed more ideas than expected (27%).](ai-stage-shifts-idea-text-attribution.md) — related
- [Planning-stage AI ideas were often redundant with or rejected in favor of writers' own ideas: idea attribution was 17.8% among users versus 2.9% among non-users, but ownership did not differ between users and non-users within ai plan.](planning-ai-ideas-redundant-unused.md) — related
- [Prototype generation is the only GenAI activity significantly associated with perceived loss of creativity or ownership](prototype-generation-linked-ownership-loss.md) — reports the opposite
