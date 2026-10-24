---
type: claim
title: In simulation, an adaptive prompt router outperforms two static prompt baselines on pedagogical score across 390 scenarios
description: In simulation, an adaptive prompt router outperforms two static prompt baselines on pedagogical score across 390 scenarios
id: prompt-router-beats-static-baselines-simulation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: po-chin-chang-2026
    resource: "https://doi.org/10.48550/arxiv.2606.20138"
    title: "Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138 [doi:10.48550/arxiv.2606.20138](https://doi.org/10.48550/arxiv.2606.20138)"
    author: Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In simulation, an adaptive prompt router outperforms two static prompt baselines on pedagogical score across 390 scenarios

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The dynamic routing model achieves a higher mean pedagogical score (0.694) than the production baseline (0.64) and the literature baseline (0.647) in simulation, p<0.001. [→ Po-Chin Chang 2026](#po-chin-chang-2026)

## Evidence

### Po-Chin Chang 2026

Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138 [doi:10.48550/arxiv.2606.20138](https://doi.org/10.48550/arxiv.2606.20138)

`q2 · i?` · `causal · r2`

Simulation benchmark over 390 simulated scenarios comparing the frozen routing model against the Futurewhiz production prompt and the static Dinucu_Prompt. The router "achieves the highest mean score (0.694)" and eliminates the tail of severe pedagogical failures (scores<0.4).

> "Figure 10 shows that the router achieves the highest mean score (0.694), but both the commercial production baseline and the literature promptDinucu_Prompthave lower mean score (0.64 with production baseline, 0.647 with literature prompt,p<0.001 )."

## Discussion


## Related Claims
- [In simulation the router matches the empirically optimal subject strategy in 8 of 13 subjects, but retreats to a safe strategy where gains are marginal](router-subject-strategy-alignment-simulation.md) — related
- [A stochastic (exploration) router yields a higher exercise conversion rate than the static baseline, while the greedy router is comparable](stochastic-router-higher-conversion-rate.md) — related
- [The adaptive router reduces turns in long conversations (turns≥5) but not across the unfiltered dataset](router-reduces-turns-long-conversations.md) — related
- [Live feedback shifts the router's strategy from the Feynman prompt favored in simulation to the scaffolding Coach prompt, with superior live performance](sim-to-real-strategy-shift-feynman-to-coach.md) — related
- [A pedagogically informed Tutor Prompt yields higher Success@N and lower Telling@N than MathDial's Base Prompt in simulated tutor-student dialogues](tutor-prompt-outperforms-base-prompt-mathdial.md) — related
- [Higher AI pedagogical scores are associated with exercise conversion in real student sessions](pedagogical-score-predicts-exercise-conversion.md) — related
