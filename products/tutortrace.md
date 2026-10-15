---
type: product
id: tutortrace
title: TutorTrace
description: "TutorTrace is a dataset and taxonomy developed by its authors that uses IDE telemetry to classify introductory Python learners' behavioral states around AI help-seeking and support tutor interventions."
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# TutorTrace

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
TutorTrace is a dataset and taxonomy developed by its authors that uses IDE telemetry to classify introductory Python learners' behavioral states around AI help-seeking and support tutor interventions.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **TutorTrace three-window behavioral taxonomy of ten learner profiles around AI help-seeking**: The taxonomy organizes learner activity surrounding AI help-seeking into three temporal windows: before the first AI query (Cold Start, Oriented, Struggling), between consecutive queries (Passive, Iterating, Debugging, Spinning), and session-wide re-querying patterns (Passive Re-querying, Active Testing, Untested Editing) — ten profiles in total. Profiles were derived via outcome-guided K-means clustering over window-specific metric pools, with rule-defined profiles for zero-effort observations. Each profile carries an expert-informed intervention strategy supplied to the AI tutor's prompt, e.g. Cold Start: "Scaffold task entry. Offer pseudocode with blanks." (TutorTrace: A Dataset and Taxonomy for Classifying Learner Behavioral States during AI-Ass)
- **TutorTrace automated behavioral classifier transforming raw IDE telemetry into labeled behavioral sequences in real time**: The TutorTrace classifier is an automated pipeline that transforms raw IDE telemetry into labeled behavioral sequences in real time. Its rules are grounded in the judgment of four domain-expert annotators who coded session replays with a codebook of behaviors such as Implementing, Debugging, Thinking, and Seeking Help, refined over 10 pilot sessions. Validation triangulated learner self-reports, expert annotations, and the automated classifier: "overall Cohen's𝜅 ranged from 0.73 to 0.83, and overall raw agreement ranged from 78% to 87%" (Table 4). (TutorTrace: A Dataset and Taxonomy for Classifying Learner Behavioral States during AI-Ass)

### Claims
- [First queries from Cold Start learners were overwhelmingly dependent (96.7%), contrasting with mostly guided first queries from Oriented (69.1%) and Struggling (71.4%) learners](../claims/cold-start-first-queries-dependent-help-seeking.md) [+M]
- [Window 1 profiles complicate the assumption that greater pre-query effort signals better progress: Cold Start learners completed at 97% while Struggling learners completed at 67%](../claims/pre-query-effort-completion-descriptive-profiles.md) [+M]

## Related Products and Programmes

- [BILearn-CS](bilearn-cs.md)

## Key Sources
- David Barron, Xiaohang Tang, Rezky Dwisantika, Minsun Kim, David H. Smith IV, Jiaming Cui, and Yan Chen. 2026. TutorTrace: A Dataset and Taxonomy for Classifying Learner Behavioral States during AI-Assisted Programming Education. https://arxiv.org/abs/2608.26184
