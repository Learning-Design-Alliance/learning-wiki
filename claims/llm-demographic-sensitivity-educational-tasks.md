---
type: claim
title: "LLMs exhibit demographic sensitivity: systematic output differences attributable solely to demographic context when task inputs are held constant"
description: "LLMs exhibit demographic sensitivity: systematic output differences attributable solely to demographic context when task inputs are held constant"
id: llm-demographic-sensitivity-educational-tasks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: donya-rooein-2026
    resource: "https://doi.org/10.48550/arxiv.2609.16993"
    title: "Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993 [doi:10.48550/arxiv.2609.16993](https://doi.org/10.48550/arxiv.2609.16993)"
    author: Donya Rooein, Luca Benedetto, Dirk Hovy
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLMs exhibit demographic sensitivity: systematic output differences attributable solely to demographic context when task inputs are held constant

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across six LLMs and three educational tasks, models pick up on both explicit and implicit demographic cues and change scoring, feedback, and answers accordingly. [→ Donya Rooein 2026](#donya-rooein-2026)

## Evidence

### Donya Rooein 2026

Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993 [doi:10.48550/arxiv.2609.16993](https://doi.org/10.48550/arxiv.2609.16993)

`q2 · i?` · `causal · r2`

Controlled counterfactual sensitivity-testing experiment in which six LLMs performed AES, formative feedback, and QA under model default, explicit-persona, and implicit-history conditions. In both explicit and implicit cases, the article reports that "the models pick up on demographic cues and can change their scoring, feedback, and answers accordingly". The design comprised 192,480 LLM inference calls.

> "We set up controlled prompts to test 1) explicit demographic effects, where we mention demographic details directly, and 2) implicit effects, where we use conversation his- tory as a demographic signal."

## Discussion


## Related Claims
- [Implicit demographic cues produce larger and less predictable effects in open-ended tasks, including longer responses for laptop users and education-related length effects](implicit-cues-unpredictable-effects-open-ended-tasks.md) — a narrower finding that bears on this claim
- [Explicitly prompting a student attribute produces large, systematic increases in the concentration of stereotype-aligned marked words in LLM-generated writing feedback](prompted-attributes-increase-marked-pedagogy-concentration.md) — a narrower finding that bears on this claim
- [Names alone elicit weaker, less consistent identity-marked feedback language than explicit attribute prompts](names-alone-elicit-weaker-marked-language.md) — a narrower finding that bears on this claim
- [In one reviewed study, GPT-4 automated essay scoring showed score inflation, with AI–human rating discrepancies exceeding 1.5 standard deviations in 38% of graduate-level bibliographies](gpt4-essay-score-inflation.md) — related
