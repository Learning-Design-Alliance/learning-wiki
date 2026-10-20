---
type: claim
title: In an OLS regression, explicit finish lines in teacher prompts were associated with smaller DOK gaps, while explain-reasoning epistemic framing was associated with larger gaps
description: In an OLS regression, explicit finish lines in teacher prompts were associated with smaller DOK gaps, while explain-reasoning epistemic framing was associated with larger gaps
id: prompt-features-predict-dok-gap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: alex-liu-2026
    resource: "https://doi.org/10.48550/arxiv.2604.16738"
    title: "Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He. (2026). Teacher-Authored Prompts for Configuring StudentAI Dialogue: K12 Classroom Implementation. https://arxiv.org/abs/2604.16738 [doi:10.48550/arxiv.2604.16738](https://doi.org/10.48550/arxiv.2604.16738)"
    author: Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: alex-liu-2026-2
    resource: "https://arxiv.org/abs/2604.16738"
    title: "Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He. (2026). Teacher-Authored Prompts for Configuring StudentAI Dialogue: K12 Classroom Implementation. https://arxiv.org/abs/2604.16738"
    author: Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# In an OLS regression, explicit finish lines in teacher prompts were associated with smaller DOK gaps, while explain-reasoning epistemic framing was associated with larger gaps

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Prompts specifying explicit task endpoints (β=−0.22, p<.001) were associated with smaller DOK gaps. [→ Alex Liu 2026](#alex-liu-2026)
`q2 i?` Prompts requesting students to explain reasoning were associated with larger DOK gaps (β=+0.20, p<.001), which the authors attribute to residual confounding with target ambition. [→ Alex Liu 2026 (2)](#alex-liu-2026-2)

## Evidence

### Alex Liu 2026

Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He. (2026). Teacher-Authored Prompts for Configuring StudentAI Dialogue: K12 Classroom Implementation. https://arxiv.org/abs/2604.16738 [doi:10.48550/arxiv.2604.16738](https://doi.org/10.48550/arxiv.2604.16738)

`q2 · i?` · `associational · r2`

OLS regression of DOK gap on prompt characteristics (N = 1,362, robust SEs clustered by discussion; R² = 0.21). The article reports the finish-line coefficient β=−0.22, p<.001, an unstandardized coefficient with no printed effect size.

> "Prompts specifying explicit task endpoints (β=−0.22,p<.001) were associated with smaller DOK gaps."

### Alex Liu 2026 (2)

Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He. (2026). Teacher-Authored Prompts for Configuring StudentAI Dialogue: K12 Classroom Implementation. https://arxiv.org/abs/2604.16738

`q2 · i?` · `associational · r2`

Same OLS model (Table 5). The article reports the explain-reasoning coefficient β=+0.20, p<.001, and cautions the positive coefficient may reflect residual association after controlling for target DOK rather than a negative effect of epistemic framing.

> "Epistemic framingshowed counterintuitive effects, as prompts requesting students to "explain reasoning" were associated withlargerDOK gaps (β= +0.20,p<.001)."

## Discussion

## Related Claims

- [Instructionally supported (prompted) journal writing outperforms unsupported journal writing on learning outcomes (Hedges's g = 0.78)](prompted-journal-writing-medium-large-effect.md) — the general claim this finding bears on, with the studies behind it
- [A design-enactment gap in cognitive demand: 37.7% of conversations under-reached the teacher-targeted DOK level, and under-targeting increased with target ambition](dok-under-targeting-gap-ai-dialogue.md) — related
- [Teachers authoring student-AI dialogue prompts predominantly write highly specific tasks targeting higher-order thinking (92% at DOK 2–3)](teachers-author-specific-higher-order-ai-prompts.md) — related
- [LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it](llm-upward-cognitive-shift-asymmetry.md) — related
