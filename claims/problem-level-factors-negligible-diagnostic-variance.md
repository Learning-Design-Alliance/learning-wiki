---
type: claim
title: Step complexity, distance to conclusion, and inference rule explain negligible diagnostic variance, with complexity predicting misdiagnosis only for optimal steps
description: Step complexity, distance to conclusion, and inference rule explain negligible diagnostic variance, with complexity predicting misdiagnosis only for optimal steps
id: problem-level-factors-negligible-diagnostic-variance
status: review
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
    kind: causal
    rigour: 2
  - id: tahreem-yasir-2026-2
    resource: "https://arxiv.org/abs/2605.16207"
    title: "Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207"
    author: Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: tahreem-yasir-2026-3
    resource: "https://arxiv.org/abs/2605.16207"
    title: "Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207"
    author: Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Step complexity, distance to conclusion, and inference rule explain negligible diagnostic variance, with complexity predicting misdiagnosis only for optimal steps

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Step complexity predicted misdiagnosis only for optimal solutions (misdiagnosed M = 2.46 vs correctly classified M = 1.95, p < .05) and explained negligible variance overall (η² < .01). [→ Tahreem Yasir 2026](#tahreem-yasir-2026)
`q2 i?` Over-rejection was highest at near distances to the conclusion, and distance to conclusion explained negligible variance (η² < .01). [→ Tahreem Yasir 2026 (2)](#tahreem-yasir-2026-2)
`q2 i?` Classification failures concentrated on structurally complex inference rules (MT, CD, DeM). [→ Tahreem Yasir 2026 (3)](#tahreem-yasir-2026-3)

## Evidence

### Tahreem Yasir 2026

Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207 [doi:10.48550/arxiv.2605.16207](https://doi.org/10.48550/arxiv.2605.16207)

`q2 · i?` · `causal · r2`

Complexity analysis (RQ2) pooling feedback agents across models after conditions showed negligible effects. For valid-alternative and incorrect solutions complexity did not predict errors (p > .08); agents rejected simpler valid-alternative solutions (M = 2.97) more often than complex ones (M = 3.62).

> "complexity predicted misdiagnosis only for Optimal solutions: more complex steps were misdiagnosed more often (M= 2.46 ) than correctly classified ones (M= 1.95;p<.05)."

### Tahreem Yasir 2026 (2)

Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207

`q2 · i?` · `causal · r2`

Distance-tier analysis (RQ2) using near (d ≤ 2), mid, and far partitions, reported via Figure 19 and accompanying text. The result is a plotted pattern described in text, supporting model-level rather than position-driven failure.

> "Figure 19 shows that over-rejection is highest at near distances, meaning agents most often penalize valid-alternative reasoning when solutions are closest to the conclusion. Distance to conclusion explained negligible variance (η2 < .01)"

### Tahreem Yasir 2026 (3)

Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207

`q2 · i?` · `design · r2`

Per-inference-rule F1 comparison (RQ2, Figure 20). LLaMA showed minimal gains across most rule types while Gemini and DeepSeek consistently achieved the highest scores; no effect size is printed.

> "Analysis of inference rules and F1 scores (Figure 20) shows that failures con- centrate on structurally complex rules (MT, CD, DeM)."

## Discussion


## Related Claims
- [LLM feedback agents classify optimal logic proof steps near-ceiling but perform poorly on valid-alternative and incorrect solutions](llm-tutors-near-ceiling-optimal-poor-valid-alternative-incorrect.md) — related
- [Model selection, not feedback condition, explains LLM diagnostic accuracy in three-way logic proof classification](model-selection-dominates-feedback-condition-diagnosis.md) — related
