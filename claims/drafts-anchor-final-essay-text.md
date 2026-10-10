---
type: claim
title: In this experiment, drafts—human-written or AI-generated—anchored the final essay, with AI-generated drafts revised somewhat more but underlying phrases largely retained across conditions.
description: In this experiment, drafts—human-written or AI-generated—anchored the final essay, with AI-generated drafts revised somewhat more but underlying phrases largely retained across conditions.
id: drafts-anchor-final-essay-text
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: ngram-retention
    title: ngram-retention
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# In this experiment, drafts—human-written or AI-generated—anchored the final essay, with AI-generated drafts revised somewhat more but underlying phrases largely retained across conditions.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` Draft-to-final 3-gram retention was ≥93% in every condition and 5-gram retention dipped to ~88% only in ai draft, indicating AI support shifted how verbatim carryover was rather than whether content flowed through. [→ ngram-retention](#ngram-retention)

## Evidence

### ngram-retention

Katy Ilonka Gero, Tao Long, Carly Schnitzler, and Paramveer S. Dhillon. 2026. From Planning to Revision: How AI Writing Support at Different Stages Alters Ownership. In Designing Interactive Systems Conference (DIS '26), June 13–17, 2026, Singapore, Singapore. ACM, New York, NY, USA. https://doi.org/10.1145/3800645.3813003

`q3 · i?` · `causal · r2`

N-gram retention analysis (Table 2) across the n=253 experiment's four conditions: "people did not revise too much in any condition; when AI provides the draft, people do revise a bit more (lower 5-gram), but the underlying phrases remain largely intact (still high 3-gram)." Reported as descriptive telemetry, not model covariates.

> "In other words, people did not revise too much in any condition; when AI provides the draft, people do revise a bit more (lower 5-gram), but the underlying phrases remain largely intact (still high 3-gram)."

## Discussion


## Related Claims
- [Essay quality was highest for AI-generated drafts and lowest with no AI, negatively correlated with ownership, suggesting an ownership-quality tradeoff.](ai-draft-quality-ownership-tradeoff.md) — related
- [AI support shifts perceived attribution of ideas and text toward the AI, most strongly for AI-generated drafts, and an AI draft based on the writer's own outline contributed more ideas than expected (27%).](ai-stage-shifts-idea-text-attribution.md) — related
- [AI support during drafting lowers ownership substantially more than support during planning or revision, and planning support preserves more ownership than revision support.](drafting-support-largest-ownership-decrease.md) — related
