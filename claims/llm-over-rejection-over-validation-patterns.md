---
type: claim
title: LLM feedback agents show model-specific over-rejection of valid-alternative reasoning and over-validation of incorrect solutions
description: LLM feedback agents show model-specific over-rejection of valid-alternative reasoning and over-validation of incorrect solutions
id: llm-over-rejection-over-validation-patterns
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: tahreem-yasir-2026
    resource: "https://doi.org/10.48550/arxiv.2605.16207"
    title: "Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207 [doi:10.48550/arxiv.2605.16207](https://doi.org/10.48550/arxiv.2605.16207)"
    author: Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: tahreem-yasir-2026-2
    resource: "https://arxiv.org/abs/2605.16207"
    title: "Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207"
    author: Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM feedback agents show model-specific over-rejection of valid-alternative reasoning and over-validation of incorrect solutions

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r2`, 1 design `r2` · `q2`

## Subclaims
`q2 i?` Gemini and DeepSeek over-validated 69-71% of incorrect solutions while over-rejecting only 13-17% of valid-alternative ones. [→ Tahreem Yasir 2026](#tahreem-yasir-2026)
`q2 i?` LLaMA 3 showed the opposite pattern, over-rejecting 91% of valid-alternative solutions while over-validating only 6%. [→ Tahreem Yasir 2026 (2)](#tahreem-yasir-2026-2)

## Evidence

### Tahreem Yasir 2026

Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207 [doi:10.48550/arxiv.2605.16207](https://doi.org/10.48550/arxiv.2605.16207)

`q2 · i?` · `design · r2`

Conditional error-rate analysis (RQ1, Table 2) of KG-grounded diagnosis across seven models. Gemini and DeepSeek displayed "high over-validation" with low over-rejection; only percentages are printed, no effect size.

> "Gem- ini and DeepSeek showed high over-validation (69-71%) but low over-rejection (13-17%), treat- ing most student solutions as valid-alternative re- gardless of correctness."

### Tahreem Yasir 2026 (2)

Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207

`q2 · i?` · `causal · r2`

Same Table 2 error-rate analysis: LLaMA 3 exhibited the contrasting failure mode of "91% over-rejection but only 6% over-validation". GPT-4.1 and GPT-o3 showed moderate rates of both errors (29-41%); no effect size is printed.

> "LLaMA 3 showed the op- posite pattern: 91% over-rejection but only 6% over-validation, rejecting nearly all non-optimal solutions."

## Discussion


## Related Claims
- [LLM feedback agents classify optimal logic proof steps near-ceiling but perform poorly on valid-alternative and incorrect solutions](llm-tutors-near-ceiling-optimal-poor-valid-alternative-incorrect.md) — a broader claim this one bears on
