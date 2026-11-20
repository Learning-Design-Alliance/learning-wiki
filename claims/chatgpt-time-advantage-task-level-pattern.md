---
type: claim
title: The ChatGPT completion-time advantage is significant on most individual tasks but not on the easiest task or on T7, where generated code needed alignment to the task
description: The ChatGPT completion-time advantage is significant on most individual tasks but not on the easiest task or on T7, where generated code needed alignment to the task
id: chatgpt-time-advantage-task-level-pattern
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: mixed
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: hapnes-toba-2024
    resource: "https://doi.org/10.1007/978-3-031-51979-6_54"
    title: "Hapnes Toba, Oscar Karnalim, Meliana Christianti Johan, Terutoshi Tada, Yenni Merlin Djajalaksana, and Tristan Vivaldy. (2024). Inappropriate Benefits and Identification of ChatGPT Misuse in Programming Tests: A Controlled Experiment. Originally published 2023. [doi:10.1007/978-3-031-51979-6_54](https://doi.org/10.1007/978-3-031-51979-6_54)"
    author: Hapnes Toba, Oscar Karnalim, Meliana Christianti Johan, Terutoshi Tada, Yenni Merlin Djajalaksana, and Tristan Vivaldy
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: hapnes-toba-2024-2
    resource: "https://doi.org/10.1007/978-3-031-51979-6_54"
    title: "Hapnes Toba, Oscar Karnalim, Meliana Christianti Johan, Terutoshi Tada, Yenni Merlin Djajalaksana, and Tristan Vivaldy. (2024). Inappropriate Benefits and Identification of ChatGPT Misuse in Programming Tests: A Controlled Experiment. Originally published 2023. [doi:10.1007/978-3-031-51979-6_54](https://doi.org/10.1007/978-3-031-51979-6_54)"
    author: Hapnes Toba, Oscar Karnalim, Meliana Christianti Johan, Terutoshi Tada, Yenni Merlin Djajalaksana, and Tristan Vivaldy
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The ChatGPT completion-time advantage is significant on most individual tasks but not on the easiest task or on T7, where generated code needed alignment to the task

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Per-task time differences were significant for T2 and T3 in the mid-test and for T5, T6 and T8 in the final test, but not for the easy T1. [→ Hapnes Toba 2024](#hapnes-toba-2024)
`q2 i?` T7 was the only task where ChatGPT users had comparable completion times, reportedly because generated code had a slightly different purpose. [→ Hapnes Toba 2024 (2)](#hapnes-toba-2024-2)

## Evidence

### Hapnes Toba 2024

Hapnes Toba, Oscar Karnalim, Meliana Christianti Johan, Terutoshi Tada, Yenni Merlin Djajalaksana, and Tristan Vivaldy. (2024). Inappropriate Benefits and Identification of ChatGPT Misuse in Programming Tests: A Controlled Experiment. Originally published 2023. [doi:10.1007/978-3-031-51979-6_54](https://doi.org/10.1007/978-3-031-51979-6_54)

`q2 · i?` · `causal · r1`

Mid-test per-task analysis in the controlled experiment: time differences significant on T2 (p<0,01) and T3 (p<0.01); T1 money conversion was "quite easy to solve, the completion time is not significantly affected". Final test showed significance for T5 (p<0.01), T6 (p<0.001), T8 (p<0.01).

> "While observing per task, the difference is only statistically significant on T2 (p<0,01) and T3 (p<0.01). Calculating student GPAs and generating shop invoices are quite common and ChatGPT could help students well."

### Hapnes Toba 2024 (2)

Hapnes Toba, Oscar Karnalim, Meliana Christianti Johan, Terutoshi Tada, Yenni Merlin Djajalaksana, and Tristan Vivaldy. (2024). Inappropriate Benefits and Identification of ChatGPT Misuse in Programming Tests: A Controlled Experiment. Originally published 2023. [doi:10.1007/978-3-031-51979-6_54](https://doi.org/10.1007/978-3-031-51979-6_54)

`q2 · i?` · `causal · r1`

Final-test per-task result: on T7 (closest and farthest 2D coordinates), ChatGPT users averaged 16.33 minutes versus 29.25 but the difference was not significant; an informal post-discussion attributed this to code needing further alignment to the task.

> "T7 is the only task at which students with ChatGPT had comparable completion times with their counterparts. Informal post-discussion with the students notes that for T7, ChatGPT-generated code had a slightly different purpose and needed further alignment to the task."

## Discussion


## Related Claims
- [Students using ChatGPT complete programming tests about two times faster than students without ChatGPT, while their programming performance is comparable](chatgpt-halves-completion-time-comparable-marks.md) — a broader claim this one bears on
