---
type: claim
title: The simulated learner tracks a real-student KT model with calibration error 0.049, and the helpfulness rubric transfers to real classroom transcripts
description: The simulated learner tracks a real-student KT model with calibration error 0.049, and the helpfulness rubric transfers to real classroom transcripts
id: educlaw-bench-simulator-calibration
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: lee-2026
    resource: "https://arxiv.org/abs/2608.03206"
    title: "Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206"
    author: Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: lee-2026-2
    resource: "https://arxiv.org/abs/2608.03206"
    title: "Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206"
    author: Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The simulated learner tracks a real-student KT model with calibration error 0.049, and the helpfulness rubric transfers to real classroom transcripts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Binning all 176,187 (run, day) pairs by predicted mastery against observed accuracy gives an Expected Calibration Error of 0.049 and Brier score of 0.033 over 1.19M item attempts. [→ Lee 2026](#lee-2026)
`q2 i?` Scoring 150 real K-12 tutoring sessions with the same rubric gives a field Helpfulness of 6.02 (sd 1.21), inside the simulator's range (6.19, sd 0.45) with no distinguishable difference (Mann-Whitney p = 0.68). [→ Lee 2026 (2)](#lee-2026-2)

## Evidence

### Lee 2026

Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206

`q2 · i?` · `design · r2`

AKT-predicted KC mastery plotted against observed probe accuracy, with points hugging the diagonal, so its knowledge state tracks the real-student KT model rather than drifting.

> "binning all176,187(run, day) pairs by predicted mastery against observed accuracy gives an Expected Calibration Error of 0.049and a Brier score of0.033over1.19M item attempts"

### Lee 2026 (2)

Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206

`q2 · i?` · `design · r2`

Field test with about 500 K-12 students across several partner classrooms using a live tutor on solar-mini. The rubric therefore transfers to real transcripts; Cohen's d = 0.18 for the difference.

> "Scoring 150 of these sessions with the same rubric gives a field Helpfulness of6.02(sd1.21), inside the simulator’s range for that axis (6.19, sd0.45) with no distinguishable differ- ence (Mann-Whitneyp= 0.68)"

## Discussion


## Related Claims
- [Almost no model-and-harness combination sustains tutoring over the full 30-day horizon, as learning plateaus within 5–10 days](educlaw-bench-plateau-within-days.md) — related
- [CogEvolution performs comparably to the KT-based PEERS model on mastery prediction (AUC 0.80 vs 0.82) while achieving higher mistake precision (76.8%) on CogMath-948](cogevolution-mistake-precision-beats-kt-baseline.md) — related
- [Fine-tuning on KTLP data improved CLST output calibration, moving predictions closer to the ideal diagonal](fine-tuning-improves-clst-calibration.md) — related
- [Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses](bkt-mastery-floor-above-learn-rate.md) — related
- [LLM-based transcript classifications agreed highly with human judgment for explicit questions (κ = .778) and math talk (κ = .722), but only moderately for need for help (κ = .562) and confusion (κ = .531)](llm-classification-agreement-varies-by-construct.md) — related
- [In system cold-start scenarios, CLST outperformed every baseline KT model across all five datasets, with the largest gains at 8 training students](clst-outperforms-baselines-cold-start.md) — related
- [MS-BKT mastery estimates fluctuate less than classic BKT and avoid over-high estimates after long incorrect runs, in fictitious-student comparisons](ms-bkt-estimates-fluctuate-less-than-bkt.md) — related
