---
type: claim
title: FSM-based evaluation aligns with human judgments of interactivity, functional correctness, and visual quality more strongly than VLM and unit-test baselines on balanced data
description: FSM-based evaluation aligns with human judgments of interactivity, functional correctness, and visual quality more strongly than VLM and unit-test baselines on balanced data
id: fsm-eval-aligns-with-human-interactivity-judgments
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: xiaozao-wang-2026
    resource: "https://arxiv.org/abs/2606.31012"
    title: "Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012"
    author: Xiaozao Wang, Zhewei Wang, Hongyi Wen
    q: 2
    i: 3
    kind: design
    rigour: 2
  - id: xiaozao-wang-2026-2
    resource: "https://arxiv.org/abs/2606.31012"
    title: "Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012"
    author: Xiaozao Wang, Zhewei Wang, Hongyi Wen
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# FSM-based evaluation aligns with human judgments of interactivity, functional correctness, and visual quality more strongly than VLM and unit-test baselines on balanced data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` On the balanced dataset, FSM-based evaluation achieves the highest correlation with human judgment on interactivity (r = 0.728), outperforming VLM-based evaluation and unit testing. [→ Xiaozao Wang 2026](#xiaozao-wang-2026)
`q2 i3` FSM-based evaluation shows strong alignment with human judgments of functional correctness (r = 0.676) and visual quality (r = 0.690), and the highest overall correlation (r = 0.696). [→ Xiaozao Wang 2026 (2)](#xiaozao-wang-2026-2)

## Evidence

### Xiaozao Wang 2026

Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012

`q2 · i3` · `design · r2`

Controlled human evaluation of a randomly sampled subset of 166 explorable explanations rated by two raters each, from the balanced-dataset analysis in Results. FSM-based evaluation reached the highest interactivity correlation, "r= 0.728,p < 0.001", versus VLM at r = 0.530 and unit testing at r = −0.600.

> "Notably, FSM achieves the highest correlation onInteractivity( r= 0.728,p < 0.001), substantially outperforming VLM-based evaluation (r= 0.530 ) and unit testing (r=−0.600 )."

### Xiaozao Wang 2026 (2)

Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012

`q2 · i3` · `design · r2`

Same balanced-dataset human-evaluation analysis in Results, reporting FSM-based correlations with human ratings of "Functional( r= 0.676 )" and visual quality (r = 0.690), with an overall correlation of r = 0.696, the highest among the compared frameworks.

> "FSM also exhibits strong alignment onFunctional( r= 0.676 ) andVisual( r= 0.690 ), resulting in the highest overall correlation (r= 0.696 )."

## Discussion


## Related Claims
- [Unit-test-based evaluation shows consistently negative correlations with human judgment, disproportionately penalizing complex high-quality interactive designs](unit-test-negative-correlation-human-judgment.md) — related
- [Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models](binary-correctness-judgments-near-chance.md) — related
- [FSM-based evaluation discriminates interactive quality across models, with GPT-5 Mini scoring highest and most tiers significantly separated](fsm-eval-discriminates-model-quality.md) — related
