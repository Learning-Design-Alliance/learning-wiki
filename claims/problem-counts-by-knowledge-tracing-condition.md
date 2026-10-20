---
type: claim
title: In simulated online mastery learning, BKT gave the fewest problems, Streak the second fewest, Random the most, and DKT gave almost as many as Random in one problem type and the least in the other two
description: In simulated online mastery learning, BKT gave the fewest problems, Streak the second fewest, Random the most, and DKT gave almost as many as Random in one problem type and the least in the other two
id: problem-counts-by-knowledge-tracing-condition
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
sources:
  - id: counts-1
    title: counts-1
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# In simulated online mastery learning, BKT gave the fewest problems, Streak the second fewest, Random the most, and DKT gave almost as many as Random in one problem type and the least in the other two

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Evidence quality** · No study behind this claim is a peer-reviewed article with a DOI: it rests on a source with no registered publication record (a web page, book or unpublished report). It is kept because 2 design pages cite it; treat it as a lead to check, not an established finding.

## Subclaims
`q2 i?` Problem counts differed sharply by condition: Streak gave around 17 AD, 10 AS and 9 M problems; BKT default around 11 AD and 6 AS and M; DKT random gave around 78 AD problems but fewer than 3 in AS and M. [→ counts-1](#counts-1)

## Evidence

### counts-1

Qiao Zhang and Christopher MacLellan “Going Online: A simulated student approach for evaluating knowledge tracing in the context of mastery learning”. 2021. In: Proceedings of The 14th International Conference on Educational Data Mining (EDM21). International Educational Data Mining Society, 331-337. https://educationaldatamining.org/edm2021/

`q2 · i? · the article prints no effect size for this finding` · `causal · r1`

Simulation results shown in Figure 1 report problems administered per condition and problem type across 30 simulated students per condition. The authors hypothesize BKT human gives slightly more problems than BKT random because BKT random parameters were fit to the simulated students.

> "DKT random gives around 78 AD problems, almost as many as Random; however, it gives less than 3 problems in AS and M."

## Discussion

## Related Claims

- [Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS](adaptive-icap-scaffolding-improves-posttest-logic-tutor.md) — the general claim this finding bears on, with the studies behind it
- [BKT is the most efficient knowledge tracing approach overall in simulated online mastery learning, though DKT is more efficient for AS and M problems](bkt-most-efficient-online-mastery-learning.md) — related
- Deep Knowledge Tracing has a fundamental limitation that prevents it from supporting mastery learning on multi-step problems — related
- Simulated students (Apprentice agents) can successfully evaluate online knowledge tracing models, exposing errors before costly classroom testing — a broader claim this one bears on
- [KT4EQG remains competitive when evaluated with alternative knowledge tracers (BKT and DKT), though its advantage varies across modules](kt4eqg-competitive-under-alternative-tracers.md) — related
- [The DRL policy produced a significantly different scaffolding distribution than Control and BKT, favoring Guided examples (60%) and avoiding Buggy examples (4%)](drl-policy-favors-guided-examples-distribution.md) — related
