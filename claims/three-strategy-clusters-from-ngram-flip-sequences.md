---
type: claim
title: Clustering n-gram flip sequences per task yields three distinct problem-solving strategy groups across the binary challenges
description: Clustering n-gram flip sequences per task yields three distinct problem-solving strategy groups across the binary challenges
id: three-strategy-clusters-from-ngram-flip-sequences
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
newest_evidence: 2017
sources:
  - id: akram-2017
    resource: "https://scholar.google.com/scholar?q=Improving+Stealth+Assessment+in+Game-based+Learning+with+LSTM-based+Analytics"
    title: "Akram, B., Mott, B., Min, W., Boyer, K. E., Wiebe, E., & Lester, J. (2017). Improving Stealth Assessment in Game-based Learning with LSTM-based Analytics. https://scholar.google.com/scholar?q=Improving+Stealth+Assessment+in+Game-based+Learning+with+LSTM-based+Analytics"
    author: "Akram, B., Mott, B., Min, W., Boyer, K. E., Wiebe, E., & Lester, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Clustering n-gram flip sequences per task yields three distinct problem-solving strategy groups across the binary challenges

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` EM clustering of n-gram features of tile-flip sequences produced three coherent strategy clusters: quick solvers with few trial-and-error attempts, moderate solvers with thoughtful trial-and-error, and slow solvers with many flips and seemingly random trial-and-error. [→ Akram 2017](#akram-2017)

## Evidence

### Akram 2017

Akram, B., Mott, B., Min, W., Boyer, K. E., Wiebe, E., & Lester, J. (2017). Improving Stealth Assessment in Game-based Learning with LSTM-based Analytics. https://scholar.google.com/scholar?q=Improving+Stealth+Assessment+in+Game-based+Learning+with+LSTM-based+Analytics

`q2 · i?` · `design · r2`

Unsupervised EM clustering (MClust in R) of n-gram features from flip sequences, performed separately for each of the 11 tasks on the training set. Decimal and binary error-decay plots (Figures 3 and 4) showed distinct decay patterns per cluster; three clusters were chosen for all tasks.

> "The clustering grouped students into those who solved the problem in a few flips and a few attempts, those who solved the problem with a moderate number of flips and with thoughtful trial-and-error, and those who solved the problem with a long sequence of flips and with seemingly random trial-and-error."

## Discussion


## Related Claims

- [Adding in-game strategy features to pre-test features substantially improves LSTM-based stealth assessment accuracy](in-game-strategy-features-improve-prediction-over-pretest-only.md)
- [AI-supported argumentative writing yields three distinct uptake clusters (text reproducers, text integrators, text reconstructors) based on recurring n-gram overlap](three-uptake-clusters-human-ai-cowriting.md)
- [Cluster analysis of student-AI dialogue identifies three distinct collaboration profiles: Delegated Reasoning, Concerted Interpretation, and Delegated Elaboration](three-human-ai-cps-profiles-dr-ci-de.md)
- [Optimal clustering of five-channel CPS sequences detected three types of collaborative patterns among graduate student groups](three-collaborative-pattern-types-cps.md)
- [Clustering yields a small number of behaviorally distinct team clusters that instructors can use for cluster-differentiated feedback](clustering-cluster-differentiated-feedback-ttx.md)
