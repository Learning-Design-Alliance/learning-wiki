---
type: claim
title: LLM marking of code-based scientific plots achieves exceptionally strong rank-order agreement with human markers
description: LLM marking of code-based scientific plots achieves exceptionally strong rank-order agreement with human markers
id: llm-plot-marking-strong-rank-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: will-yeadon-2026
    resource: "https://doi.org/10.48550/arXiv.2603.14732"
    title: "Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)"
    author: Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: will-yeadon-2026-2
    resource: "https://doi.org/10.48550/arXiv.2603.14732"
    title: "Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)"
    author: Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM marking of code-based scientific plots achieves exceptionally strong rank-order agreement with human markers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On 1400 scientific plot elements, rank correlations with human markers are high (Gemini rho = 0.881; Claude rho = 0.909; GPT-5.2 rho = 0.838), several times higher than in essay marking. [→ Will Yeadon 2026](#will-yeadon-2026)
`q2 i?` Gemini's MAE of 4.2 marks out of 70 falls within the human-human inter-rater MAE range of 2.42 to 5.15. [→ Will Yeadon 2026 (2)](#will-yeadon-2026-2)

## Evidence

### Will Yeadon 2026

Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)

`q2 · i?` · `design · r2`

Blind LLM marking of 1400 plot elements from 100 Laboratory Skills and Electronics submissions, each scored 0–5 by three human markers. The article reports "tight alignment with human ranking preferences" across the three image-capable models.

> "Rank correlations indicate tight alignment with human ranking preferences (Gemini:ρ= 0.881, QWK = 0.926; Claude:ρ= 0.909, QWK = 0.802; GPT-5.2:ρ= 0.838, QWK = 0.725)."

### Will Yeadon 2026 (2)

Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)

`q2 · i?` · `design · r2`

Absolute-error analysis of plot marking against three blinded human markers. The article reports "Gemini is the strongest performer (4.2 marks)", within the printed human-human MAE range of 2.42 to 5.15.

> "MAE values differ meaningfully across models: Gemini is the strongest performer (4.2 marks), followed by Claude (6.6) and GPT-5.2 (7.1) (FIG. 12). Human–human inter-rater MAE ranges from 2.42 (markers 1 vs. 3) to 5.15 (markers 2 vs. 3)."

## Discussion


## Related Claims
- [Blind AI essay marking is harsher and more variable than human marking, and adding a marking scheme does not improve rank-order agreement](llm-essay-marking-harsh-low-rank-agreement.md) — related
- [LLM markers show robust rank-order agreement with human markers on blind university exam questions and structured curriculum questions](llm-rank-order-agreement-structured-physics-questions.md) — a broader claim this one bears on
- [LLM-generated scores on multimodal OSPE items correlate strongly with human scores in rank order yet diverge substantially on categorical pass/fail decisions](llm-ospe-rank-agreement-paradox.md) — a broader claim this one bears on
- [A Gemini-based creativity autorater scores real students' complex multimedia creativity tasks on par with human experts (item Kappa 0.66; total-score Pearson r = 0.88)](gemini-autorater-creativity-real-students.md) — related
- [Anchored exemplars shift AI essay means close to the human mean and compress variance below the human standard deviation, but rank-order agreement remains near-zero](anchored-exemplars-fix-distribution-not-ranking.md) — related
