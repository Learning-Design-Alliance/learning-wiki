---
type: claim
title: ChatGPT performs poorly on image-based data interpretation across DNA footprinting and BLI questions regardless of image detail
description: ChatGPT performs poorly on image-based data interpretation across DNA footprinting and BLI questions regardless of image detail
id: chatgpt-poor-image-inference-scientific-graphs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: kwong-andrew-c-2026
    resource: "https://doi.org/10.1371/journal.pone.0346127"
    title: "Kwong Andrew C., Magnano Christopher, DeOliveira Cristina, Goglia Christine, Loparo Joseph J., Peters John Jacob. (2026). Designing life science assessments in the era of generative artificial intelligence. PLOS One. https://doi.org/10.1371/journal.pone.0346127"
    author: Kwong Andrew C., Magnano Christopher, DeOliveira Cristina, Goglia Christine, Loparo Joseph J., Peters John Jacob
    q: 3
    i: "?"
    kind: design
    rigour: 2
  - id: kwong-andrew-c-2026-2
    resource: "https://doi.org/10.1371/journal.pone.0346127"
    title: "Kwong Andrew C., Magnano Christopher, DeOliveira Cristina, Goglia Christine, Loparo Joseph J., Peters John Jacob. (2026). Designing life science assessments in the era of generative artificial intelligence. PLOS One. https://doi.org/10.1371/journal.pone.0346127"
    author: Kwong Andrew C., Magnano Christopher, DeOliveira Cristina, Goglia Christine, Loparo Joseph J., Peters John Jacob
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# ChatGPT performs poorly on image-based data interpretation across DNA footprinting and BLI questions regardless of image detail

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` On a DNA footprinting image question, ChatGPT averaged 41% with primary data and 26% with schematized data, correctly identifying the technique in only 45% of cases. [→ Kwong Andrew C. 2026](#kwong-andrew-c-2026)
`q3 i?` On a BLI graph question, ChatGPT averaged 50% regardless of whether axis labels were present, scoring 40% on understand versus 25% on apply-level components. [→ Kwong Andrew C. 2026 (2)](#kwong-andrew-c-2026-2)

## Evidence

### Kwong Andrew C. 2026

Kwong Andrew C., Magnano Christopher, DeOliveira Cristina, Goglia Christine, Loparo Joseph J., Peters John Jacob. (2026). Designing life science assessments in the era of generative artificial intelligence. PLOS One. https://doi.org/10.1371/journal.pone.0346127

`q3 · i?` · `design · r2`

Blind-graded GPT-4o responses (ten per format) to a 4-lane DNA footprinting image question; no significant difference between image formats. DNA footprinting was "only correctly identified in 45% of cases" (Fig 3D).

> "Across ten answers per format, ChatGPT performed poorly, achieving only a 41% average with primary data and a 26% average with schematized data (Fig 3B)."

### Kwong Andrew C. 2026 (2)

Kwong Andrew C., Magnano Christopher, DeOliveira Cristina, Goglia Christine, Loparo Joseph J., Peters John Jacob. (2026). Designing life science assessments in the era of generative artificial intelligence. PLOS One. https://doi.org/10.1371/journal.pone.0346127

`q3 · i?` · `causal · r1`

Blind-graded GPT-4o responses (ten per graph, full versus minimal BLI graph versions) to a biolayer interferometry image question; no difference between detail levels, average 50%. Understand-level (40%) significantly exceeded apply-level (25%) scores.

> "Across ten answers per graph, we saw no difference in ChatGPT's performance achieving an average of 50% (Fig 4B). When we broke the 20 scores down into Bloom's levels, ChatGPT performed significantly better on the “understand” than “apply”-level questions, achieving respective averages of 40% and 25% (Fig 4C)."

## Discussion


## Related Claims
- [Inter-model agreement is moderate, indicating models do not consistently identify the same questions correctly](moderate-inter-model-agreement-endodontic-questions.md) — related
- [ChatGPT's accuracy on image-based MCQs ranged from 13.1% to 100% across studies, and it performed significantly worse on open-ended questions than on MCQs](image-mcq-and-open-ended-question-performance.md) — related
- [ChatGPT-4o's accuracy on U.S. Dental Decks was consistent across question formats (plain-text, case-box, and image-based)](chatgpt-4o-us-question-format-consistency.md) — reports the opposite
- [ChatGPT underperforms doctoral students on long-answer experimental design questions, driven by poor apply-level control answers](chatgpt-underperforms-long-answer-apply-level-controls.md) — related
