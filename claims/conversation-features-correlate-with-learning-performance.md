---
type: claim
title: "Conversation features correlate with learning performance: words and learning time positively, help and revision requests negatively"
description: "Conversation features correlate with learning performance: words and learning time positively, help and revision requests negatively"
id: conversation-features-correlate-with-learning-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: robin-schmucker-2024
    resource: "https://doi.org/10.1007/978-3-031-64302-6_6"
    title: "Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell. (2024). Ruffle&Riley: Insights from Designing and Evaluating a Large Language Model-Based Conversational Tutoring System. [doi:10.1007/978-3-031-64302-6_6](https://doi.org/10.1007/978-3-031-64302-6_6)"
    author: Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell
    q: 2
    i: 3
    kind: causal
    rigour: 2
  - id: robin-schmucker-2024-2
    resource: "https://doi.org/10.1007/978-3-031-64302-6_6"
    title: "Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell. (2024). Ruffle&Riley: Insights from Designing and Evaluating a Large Language Model-Based Conversational Tutoring System. [doi:10.1007/978-3-031-64302-6_6](https://doi.org/10.1007/978-3-031-64302-6_6)"
    author: Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell
    q: 2
    i: 3
    kind: causal
    rigour: 2
---

# Conversation features correlate with learning performance: words and learning time positively, help and revision requests negatively

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2` · `i3` large
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Robin Schmucker 2024: no comparison group · Robin Schmucker 2024 (2): no comparison group (read from the study by two models, 2026-11-20)

## Subclaims
`q2 i3` Number of words in user explanations correlated positively with post-test (r = 0.38, p = 0.04) and relative gain (r = 0.40, p = 0.02). [→ Robin Schmucker 2024](#robin-schmucker-2024)
`q2 i3` Learning time correlated positively with absolute gain (r = 0.39, p = 0.02), while help requests correlated negatively with post-test (r = -0.35, p = 0.05). [→ Robin Schmucker 2024 (2)](#robin-schmucker-2024-2)

## Evidence

### Robin Schmucker 2024

Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell. (2024). Ruffle&Riley: Insights from Designing and Evaluating a Large Language Model-Based Conversational Tutoring System. [doi:10.1007/978-3-031-64302-6_6](https://doi.org/10.1007/978-3-031-64302-6_6)

`q2 · i3` · `causal · r2`

Pearson correlation analysis of R&R conversation log features against performance measures (Table 6) shows words in user explanations correlated r = 0.38 (p = 0.04) with post-test and r = 0.40 (p = 0.02) with relative gain. The article states "the number ofwords in user explanations both show positive correlations to the performance measures."

> "# Words 0.24 (p = 0.19) 0.38 (p = 0.04) 0.26 (p = 0.17) 0.40 (p = 0.02)"

### Robin Schmucker 2024 (2)

Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell. (2024). Ruffle&Riley: Insights from Designing and Evaluating a Large Language Model-Based Conversational Tutoring System. [doi:10.1007/978-3-031-64302-6_6](https://doi.org/10.1007/978-3-031-64302-6_6)

`q2 · i3` · `causal · r2`

The same Pearson correlation analysis (Table 6) shows learning time correlated r = 0.39 (p = 0.02) with absolute gain, and the article reports that "the number of submittedhelp and receivedrevision requests exhibit negative correlations" with performance; number of user responses showed no significant correlations.

> "Learning Time (min) -0.17 (p = 0.34) 0.16 (p = 0.35) 0.39 (p = 0.02) 0.26 (p = 0.13)"

## Discussion


## Related Claims
- [Conversation-log analysis found the system hosted coherent EMT-based dialogues but was lenient toward partial explanations and sometimes repeated requests](conversation-analysis-coherent-but-lenient.md) — related
- [Students frequently used on-demand help ineffectively, and raw help frequency correlated negatively with learning gains](ineffective-help-seeking-log-data-findings.md) — related
- [Time spent with bottom-out hints correlates positively with learning, consistent with spontaneous self-explanation](bottom-out-hint-time-positive-learning-relation.md) — related
- [Four distinct usage patterns emerged, with conversation-focused users who did not request help showing the highest learning gains](four-usage-patterns-conversation-focused-highest-gains.md) — related
