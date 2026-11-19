---
type: claim
title: "About 30% of ChatGPT-generated hints failed manual quality checks, all due to incorrect answers or solution steps"
description: "About 30% of ChatGPT-generated hints failed manual quality checks, all due to incorrect answers or solution steps"
id: chatgpt-hint-30-percent-rejection-rate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: zachary-a-pardos-2023
    resource: "https://doi.org/10.48550/arXiv.2302.06871"
    title: "Zachary A. Pardos, Shreya Bhandari. (2023). Learning gain differences between ChatGPT and human tutor generated algebra hints. arXiv. [doi:10.48550/arXiv.2302.06871](https://doi.org/10.48550/arXiv.2302.06871)"
    author: Zachary A. Pardos, Shreya Bhandari
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# About 30% of ChatGPT-generated hints failed manual quality checks, all due to incorrect answers or solution steps

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly
> **Design limits** · Zachary A. Pardos 2023: no comparison group (read from the study by two models, 2026-11-19)

## Subclaims
`q2 i?` A three-point quality check (correct answer, correct work shown, no inappropriate language) rejected 30% of ChatGPT hints; all rejections were for wrong answers or wrong solution steps, and none contained inappropriate language. [→ Zachary A. Pardos 2023](#zachary-a-pardos-2023)

## Evidence

### Zachary A. Pardos 2023

Zachary A. Pardos, Shreya Bhandari. (2023). Learning gain differences between ChatGPT and human tutor generated algebra hints. arXiv. [doi:10.48550/arXiv.2302.06871](https://doi.org/10.48550/arXiv.2302.06871)

`q2 · i?` · `causal · r2`

Quality-check audit of all ChatGPT hints generated for the two lessons (24 Elementary and 16 Intermediate problems per Table 1), checking answer correctness, work correctness, and appropriateness. The article reports a "30% rejection rate" and that rejections suggest "human supervision in its current form".

> "Results of our study producing algebra hints using ChatGPT showed a 30% rejection rate of produced hints based on quality (RQ1), suggesting that the technology still requires human supervision in its current form."

## Discussion


## Related Claims
- [ChatGPT 3.5 produced low-quality hints for 32% of problems, reducible to near 0% for algebra and 13% for statistics via the self-consistency technique](chatgpt-hint-error-rate-self-consistency.md) — related
- [GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer](gpt4-feedback-66-percent-targeted-35-percent-flawed.md) — related
