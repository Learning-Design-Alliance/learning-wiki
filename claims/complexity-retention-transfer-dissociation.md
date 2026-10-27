---
type: claim
title: "Rail complexity affects retention and transfer in opposite directions: retention gains increase with complexity while transfer gains decrease, with no inverted-U"
description: "Rail complexity affects retention and transfer in opposite directions: retention gains increase with complexity while transfer gains decrease, with no inverted-U"
id: complexity-retention-transfer-dissociation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: mixed
newest_evidence: 2026
sources:
  - id: yinqi-huang-2026
    resource: "https://doi.org/10.1038/s41539-026-00442-6"
    title: "Yinqi Huang, Yilin Cai, Mengyao Li, Yue Chen & Robert C. Wilson. (2026). Human learning dynamics during teleoperation of surgical robots. npj Science of Learning. https://doi.org/10.1038/s41539-026-00442-6"
    author: "Yinqi Huang, Yilin Cai, Mengyao Li, Yue Chen & Robert C. Wilson"
    q: 2
    i: 3
    kind: causal
    rigour: 1
  - id: yinqi-huang-2026-2
    resource: "https://doi.org/10.1038/s41539-026-00442-6"
    title: "Yinqi Huang, Yilin Cai, Mengyao Li, Yue Chen & Robert C. Wilson. (2026). Human learning dynamics during teleoperation of surgical robots. npj Science of Learning. https://doi.org/10.1038/s41539-026-00442-6"
    author: "Yinqi Huang, Yilin Cai, Mengyao Li, Yue Chen & Robert C. Wilson"
    q: 2
    i: 3
    kind: causal
    rigour: 1
  - id: yinqi-huang-2026-3
    resource: "https://doi.org/10.1038/s41539-026-00442-6"
    title: "Yinqi Huang, Yilin Cai, Mengyao Li, Yue Chen & Robert C. Wilson. (2026). Human learning dynamics during teleoperation of surgical robots. npj Science of Learning. https://doi.org/10.1038/s41539-026-00442-6"
    author: "Yinqi Huang, Yilin Cai, Mengyao Li, Yue Chen & Robert C. Wilson"
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Rail complexity affects retention and transfer in opposite directions: retention gains increase with complexity while transfer gains decrease, with no inverted-U

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r1` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i3` Transfer performance showed a significant main effect of complexity level (η²partial = 0.300), strongest at the lowest complexity. [→ Yinqi Huang 2026](#yinqi-huang-2026)
`q2 i3` Retention improvement showed a significant main effect of complexity level (η²partial = 0.372), largest at the highest complexity. [→ Yinqi Huang 2026 (2)](#yinqi-huang-2026-2)
`q2 i?` The hypothesized inverted U-shaped complexity-learning relationship was not observed. [→ Yinqi Huang 2026 (3)](#yinqi-huang-2026-3)

## Evidence

### Yinqi Huang 2026

Yinqi Huang, Yilin Cai, Mengyao Li, Yue Chen & Robert C. Wilson. (2026). Human learning dynamics during teleoperation of surgical robots. npj Science of Learning. https://doi.org/10.1038/s41539-026-00442-6

`q2 · i3` · `causal · r1`

LME on absolute transfer PCA scores across three complexity levels with modest per-condition samples (n = 4 per condition as printed); the printed effect size was η²partial = 0.300 (f = 0.655), which the article calls "a large effect sizedespite the modest sample size".

> "The LME revealed a signiﬁcant main effect of complexity level, Fð2; 18Þ¼ 3:858; p ¼ 0:040; η2 partial ¼ 0:300; f ¼ 0:655;"

### Yinqi Huang 2026 (2)

Yinqi Huang, Yilin Cai, Mengyao Li, Yue Chen & Robert C. Wilson. (2026). Human learning dynamics during teleoperation of surgical robots. npj Science of Learning. https://doi.org/10.1038/s41539-026-00442-6

`q2 · i3` · `causal · r1`

LME on retention PCA improvements across complexity levels; the printed effect size was η²partial = 0.372 (f = 0.770), described as "a large effect size". Retention improvement increased with complexity (Level 3 M = 11.74 vs Level 1 M = 3.32).

> "Similarly for retention, we also observed a signi ﬁcant main effect of Complexity Level, Fð2; 18Þ¼ 5:331; p ¼ 0:015; η2 partial ¼ 0:372; f ¼ 0:770:"

### Yinqi Huang 2026 (3)

Yinqi Huang, Yilin Cai, Mengyao Li, Yue Chen & Robert C. Wilson. (2026). Human learning dynamics during teleoperation of surgical robots. npj Science of Learning. https://doi.org/10.1038/s41539-026-00442-6

`q2 · i?` · `causal · r1`

Authors' statement of the retained-versus-transferred dissociation: transfer decreased with complexity while retention increased, contradicting the Challenge Point-based inverted-U hypothesis.

> "Together, these results do not support Hypothesis 1 as originally stated. Speciﬁcally, we did not observe an inverted U relationship between task complexity and post-training performance."

## Discussion


## Learner Variables
- [Long-Term Memory](../learner-variables/long-term-memory.md) — outcome: instruction changes it

## Related Claims
- [In one thermodynamics study, retention and transfer scores tended to be lower on topics of higher element interactivity, a descriptive pattern with several sessions that did not fit it](retention-transfer-scores-decrease-with-element-interactivity.md) — related
- [Delayed post-learning assessments of ICL, ECL, and GCL do not differ between increasing and decreasing complexity sequences](delayed-assessments-invariant-to-sequence.md) — related
- [Human trainees show no clear asymmetric transfer of motion scaling ratio, and scaling ratio effects are small relative to complexity effects](no-asymmetric-scaling-transfer-in-humans.md) — related
- [In LQG transfer simulations, complexity affects all metrics while scaling-ratio effects appear only in efficiency metrics, with a rotational-path-length Complexity × Ratio interaction](lqg-transfer-complexity-dominates-ratio-efficiency-only.md) — related
