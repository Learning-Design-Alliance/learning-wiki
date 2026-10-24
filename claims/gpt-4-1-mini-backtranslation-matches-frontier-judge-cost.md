---
type: claim
title: GPT-4.1-Mini with back-translation matches the best LLM-judge (GPT-5) at 10.3x lower evaluation cost
description: GPT-4.1-Mini with back-translation matches the best LLM-judge (GPT-5) at 10.3x lower evaluation cost
id: gpt-4-1-mini-backtranslation-matches-frontier-judge-cost
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: vishal-kumar-2025
    resource: "https://doi.org/10.48550/arxiv.2511.08283"
    title: "Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky. (2025). DiagramIR: An Automatic Pipeline for Educational Math Diagram Evaluation. NeurIPS 2025 Workshop: MATH-AI. https://arxiv.org/abs/2511.08283 [doi:10.48550/arxiv.2511.08283](https://doi.org/10.48550/arxiv.2511.08283)"
    author: Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# GPT-4.1-Mini with back-translation matches the best LLM-judge (GPT-5) at 10.3x lower evaluation cost

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Because back-translation decouples parsing TikZ from verifying correctness, the weakest model (GPT-4.1-Mini) performs similarly with back-translation to the best LLM-judge (GPT-5) at 10.3x lower cost. [→ Vishal Kumar 2025](#vishal-kumar-2025)

## Evidence

### Vishal Kumar 2025

Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky. (2025). DiagramIR: An Automatic Pipeline for Educational Math Diagram Evaluation. NeurIPS 2025 Workshop: MATH-AI. https://arxiv.org/abs/2511.08283 [doi:10.48550/arxiv.2511.08283](https://doi.org/10.48550/arxiv.2511.08283)

`q2 · i?` · `design · r3`

Numerical comparison in the Results section (Table 2) of total dataset API cost: GPT-4.1-Mini back-translation cost $0.47 versus $4.83 for GPT-5 judging, described as "similar performance" with "the best LLM-judge (GPT-5)".

> "even the weakest model, GPT-4.1- Mini, demonstrates similar performance with back-translation as compared to the best LLM-judge (GPT-5) at 10.3x lower the cost ($0.47 vs. $4.83)"

## Discussion


## Related Claims
- [Back-translation evaluation outperforms LLM-as-a-Judge (code+image) in agreement with human raters across four models](backtranslation-outperforms-llm-judge-diagram-agreement.md) — a broader claim this one bears on
- [Back-translation yields higher human agreement on spatial checks, while LLM-as-a-Judge considerably outperforms it on the angle-label check](checkwise-backtranslation-spatial-strong-angle-weak.md) — related
- [LLM-judge evaluation of tutoring sycophancy shows systematic self-judge blind spots and missed sycophancy even under judge consensus](llm-judge-reliability-tutoring-sycophancy.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
