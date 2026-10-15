---
type: claim
title: LLMs show a systematic optimism bias in knowledge tracing, predicting far more accurately for students who answer correctly than for those who answer incorrectly
description: LLMs show a systematic optimism bias in knowledge tracing, predicting far more accurately for students who answer correctly than for those who answer incorrectly
id: llm-optimism-bias-knowledge-tracing
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: eamon-worden-2026
    resource: "https://doi.org/10.48550/arxiv.2602.00070"
    title: "Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)"
    author: Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLMs show a systematic optimism bias in knowledge tracing, predicting far more accurately for students who answer correctly than for those who answer incorrectly

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` All models perform far better when students actually answer correctly than when they answer incorrectly; Llama-3.3-70B achieves 85.4% accuracy when ground truth is correct but only 12.6% when incorrect. [→ Eamon Worden 2026](#eamon-worden-2026)

## Evidence

### Eamon Worden 2026

Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)

`q2 · i?` · `design · r2`

Breakdown of knowledge tracing accuracy by actual correctness (Table 7), reported in Section 6.1.4. The authors attribute the bias to LLMs' pretraining on correct reasoning patterns, quoting that it "achieves 85.4% accuracy when the ground truth is correct but only 12.6% when incorrect".

> "The most extreme case is Llama-3.3-70B: it achieves 85.4% accuracy when the ground truth is correct but only 12.6% when incorrect."

## Discussion


## Related Claims
- CLST's predicted mastery levels track response correctness and move similarly for related knowledge components — related
- DKT's input/output representation significantly affects performance, with KC inputs and item outputs working best on most datasets — related
- [Stealth assessment in AI-GBL achieves accurate prediction of learner states, with bias auditing demonstrated without accuracy loss](stealth-assessment-accuracy-and-bias-audits.md) — related
- ConcepTests with roughly 35% to 70% of students answering correctly before discussion appear to produce the highest engagement and most effective discussions — related
