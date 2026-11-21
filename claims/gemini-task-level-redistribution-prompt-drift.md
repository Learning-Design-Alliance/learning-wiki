---
type: claim
title: Gemini showed task-level redistribution of correct classifications despite unchanged overall accuracy, a pattern the authors call consistent with prompt drift
description: Gemini showed task-level redistribution of correct classifications despite unchanged overall accuracy, a pattern the authors call consistent with prompt drift
id: gemini-task-level-redistribution-prompt-drift
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: fox-2026
    resource: "https://doi.org/10.48550/arXiv.2605.30151"
    title: "Fox, D. S., Robles, B. L., DiPietro Brovey, E., & Schunn, C. D. (2026). Temporal Stability and Few-Shot Prompting in Math Task Assessment. [doi:10.48550/arXiv.2605.30151](https://doi.org/10.48550/arXiv.2605.30151)"
    author: "Fox, D. S., Robles, B. L., DiPietro Brovey, E., & Schunn, C. D."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Gemini showed task-level redistribution of correct classifications despite unchanged overall accuracy, a pattern the authors call consistent with prompt drift

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Three tasks Gemini had correctly classified at Time 1 were misclassified at Time 2a, while three previously misclassified tasks became correct, keeping overall accuracy at 58%. [→ Fox 2026](#fox-2026)

## Evidence

### Fox 2026

Fox, D. S., Robles, B. L., DiPietro Brovey, E., & Schunn, C. D. (2026). Temporal Stability and Few-Shot Prompting in Math Task Assessment. [doi:10.48550/arXiv.2605.30151](https://doi.org/10.48550/arXiv.2605.30151)

`q2 · i?` · `causal · r1`

Task-by-task comparison across the seven-week interval for Gemini from Table 1 and Section 2.4.2. The article reports "Three tasks that Gemini had correctly classified at Time 1 were misclassified at Time 2a" and interprets this redistribution as consistent with prompt drift, undetectable by benchmark reports.

> "Three tasks that Gemini had correctly classified at Time 1 were misclassified at Time 2a, while three previously misclassified tasks became correct."

## Discussion


## Related Claims
- [AI classification accuracy on math cognitive-demand tasks is temporally unstable over a seven-week interval, with Gemini stable at 58% and Coteach declining from 75% to 50%](ai-task-classification-temporal-instability-seven-weeks.md) — related
