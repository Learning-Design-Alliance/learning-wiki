---
type: claim
title: "Behavior-aware AI-tutor prompting was associated with a decrease in Passive inter-query windows from 50.0% to 20.7% in a nonrandomized between-deployment comparison"
description: "Behavior-aware AI-tutor prompting was associated with a decrease in Passive inter-query windows from 50.0% to 20.7% in a nonrandomized between-deployment comparison"
id: behavior-aware-prompting-reduces-passive-inter-query-windows
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: mixed
sources:
  - id: eval-1
    title: eval-1
    q: 2
    i: "?"
  - id: eval-2
    title: eval-2
    q: 2
    i: "?"
---

# Behavior-aware AI-tutor prompting was associated with a decrease in Passive inter-query windows from 50.0% to 20.7% in a nonrandomized between-deployment comparison

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment

## Subclaims
`q2 i?` In a preliminary comparison of two course deployments, behavior-aware prompting was associated with Passive inter-query windows falling from 50.0% to 20.7%, with a significant overall profile-distribution difference. [→ eval-1](#eval-1)
`q2 i?` Task completion among eligible AI users did not differ significantly between baseline (33.3%) and intervention (43.5%) deployments. [→ eval-2](#eval-2)

## Evidence

### eval-1

David Barron, Xiaohang Tang, Rezky Dwisantika, Minsun Kim, David H. Smith IV, Jiaming Cui, and Yan Chen. 2026. TutorTrace: A Dataset and Taxonomy for Classifying Learner Behavioral States during AI-Assisted Programming Education. https://arxiv.org/abs/2608.26184

`q2 · i?`

Preliminary classroom comparison of Deployment 3 (baseline, n=48 eligible AI users) versus Deployment 4 (intervention, n=85) of the same course and task. The article reports the profile-distribution difference as "𝜒 2(3)=27.55, 𝑝<. 0001" and a learner-level comparison (U=1533, p<.0001), plus more edits (23.7 vs 11.7), runs (2.1 vs 1.0), and activity time (74.9 s vs 47.0 s).

> "Passive inter-query windows accounted for 50.0% of valid win- dows in the baseline deployment and 20.7% in the intervention deployment (−29.3 pp)."

### eval-2

David Barron, Xiaohang Tang, Rezky Dwisantika, Minsun Kim, David H. Smith IV, Jiaming Cui, and Yan Chen. 2026. TutorTrace: A Dataset and Taxonomy for Classifying Learner Behavioral States during AI-Assisted Programming Education. https://arxiv.org/abs/2608.26184

`q2 · i?`

Null secondary outcome in the same between-deployment comparison: task completion among eligible AI users was 33.3% versus 43.5%, "not statistically significant (𝑝=.273)", and the design is confounded. Equivalence was not tested.

> "Completion among eligible AI users was 33.3% in the baseline deployment and 43.5% in the intervention deployment. This difference was not statistically significant (𝑝=.273) and remains confounded by the between-session design."

## Discussion


## Related Claims
- [Sustained deployment surfaced four behavioral archetypes — self-directed, tutor-reliant, late engager, and passive consumer — including patterns invisible to the reactive teaching system](itas-behavioral-archetypes.md) — related
- [Window 1 profiles complicate the assumption that greater pre-query effort signals better progress: Cold Start learners completed at 97% while Struggling learners completed at 67%](pre-query-effort-completion-descriptive-profiles.md) — related
