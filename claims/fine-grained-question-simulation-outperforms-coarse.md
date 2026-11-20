---
type: claim
title: Fine-grained per-question simulation of post-test performance outperforms whole-question-set simulation, with pre-test information and engagement improving realism
description: Fine-grained per-question simulation of post-test performance outperforms whole-question-set simulation, with pre-test information and engagement improving realism
id: fine-grained-question-simulation-outperforms-coarse
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: songlin-xu-and-xinyu-zhang-2023
    resource: "https://doi.org/10.48550/arXiv.2310.19206"
    title: "Songlin Xu and Xinyu Zhang. (2023). Leveraging generative artificial intelligence to simulate student learning behavior. [doi:10.48550/arXiv.2310.19206](https://doi.org/10.48550/arXiv.2310.19206)"
    author: Songlin Xu and Xinyu Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: songlin-xu-and-xinyu-zhang-2023-2
    resource: "https://doi.org/10.48550/arXiv.2310.19206"
    title: "Songlin Xu and Xinyu Zhang. (2023). Leveraging generative artificial intelligence to simulate student learning behavior. [doi:10.48550/arXiv.2310.19206](https://doi.org/10.48550/arXiv.2310.19206)"
    author: Songlin Xu and Xinyu Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-grained per-question simulation of post-test performance outperforms whole-question-set simulation, with pre-test information and engagement improving realism

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Treating each post-test question individually (Type 3a to 3c, best r = 0.59) yields more realistic simulation than treating all questions as a whole (Type 1a to 2c, best r = 0.36). [→ Songlin Xu and Xinyu Zhang 2023](#songlin-xu-and-xinyu-zhang-2023)
`q2 i?` Introducing pre-test information significantly improves simulation performance, e.g. from Type 1b (r = −0.15) to Type 1c (r = 0.36). [→ Songlin Xu and Xinyu Zhang 2023 (2)](#songlin-xu-and-xinyu-zhang-2023-2)

## Evidence

### Songlin Xu and Xinyu Zhang 2023

Songlin Xu and Xinyu Zhang. (2023). Leveraging generative artificial intelligence to simulate student learning behavior. [doi:10.48550/arXiv.2310.19206](https://doi.org/10.48550/arXiv.2310.19206)

`q2 · i?` · `design · r2`

Task 2 of the N = 27 experiment simulating post-test scores from demographics, per-slide understanding levels, pre-test scores, and engagement. The authors report per-question simulation "gets more realistic" with best r = 0.59 versus r = 0.36 for whole-set simulation.

> "More importantly, we observe that simulation gets more realistic when we treat each question individually (Type 3a to 3c: best r = 0.59) compared with treating all questions as a whole (Type 1a to 2c: best r = 0.36)."

### Songlin Xu and Xinyu Zhang 2023 (2)

Songlin Xu and Xinyu Zhang. (2023). Leveraging generative artificial intelligence to simulate student learning behavior. [doi:10.48550/arXiv.2310.19206](https://doi.org/10.48550/arXiv.2310.19206)

`q2 · i?` · `design · r2`

Ablation within Task 2 of the N = 27 experiment: the authors report that "introducing pre-test information will significantly improve simulation performance" across configuration pairs, evidenced by a correlation of r = 0.40 between pre-test and post-test performance.

> "introducing pre-test information will significantly improve simulation performance from Type 1b (r = −0.15) to Type 1c (r = 0.36), Type 2b (r = 0.16) to Type 2c (r = 0.36), and Type 3a (r = 0.28) to Type 3b (r = 0.57)."

## Discussion


## Related Claims
- [On the finer-grained per-question label, Process-BERT slightly outperforms CKT with and without response status, with lower AUC than the score label](per-question-label-prediction.md) — related
- [Ablations show score-label prediction depends on the response status pre-training objective when correctness is available, while event type prediction and attention matter most for behavior-only prediction](ablation-response-status-objective-score-label.md) — related
- [A fine-tuned Qwen3.5-9B simulated-respondent model predicts item difficulty with Pearson correlation 0.85, exceeding MathBERT (0.68) and MetaMath (0.75) baselines](llm-simulated-respondents-predict-item-difficulty-above-regression-baselines.md) — related
- [Epi2Diff achieves the best performance across all four item-difficulty test sets and all reported metrics, outperforming SLM fine-tuning, LLM prompting, and supervised LLM adaptation baselines](epi2diff-best-across-four-difficulty-benchmarks.md) — related
