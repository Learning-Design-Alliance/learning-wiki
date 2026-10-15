---
type: claim
title: "The team's open-track submissions with added features surpassed all other shared task submissions on all three languages, with RMSE near 0.7"
description: "The team's open-track submissions with added features surpassed all other shared task submissions on all three languages, with RMSE near 0.7"
id: open-track-submissions-surpassed-all-others
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: adam-nohejl-2026
    resource: "https://doi.org/10.48550/arxiv.2605.14257"
    title: "Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka. (2026). Sakura at BEA 2026 Shared Task 1: What Makes Vocabulary Difficult? https://arxiv.org/abs/2605.14257 [doi:10.48550/arxiv.2605.14257](https://doi.org/10.48550/arxiv.2605.14257)"
    author: Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# The team's open-track submissions with added features surpassed all other shared task submissions on all three languages, with RMSE near 0.7

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`

## Subclaims
`q2 i?` The open_max and finetuned_llms_plus submissions achieved the best open-track results on Chinese, German, and Spanish, with mean RMSE of 0.699, close to the reported statistical optimum of 0.277. [→ Adam Nohejl 2026](#adam-nohejl-2026)

## Evidence

### Adam Nohejl 2026

Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka. (2026). Sakura at BEA 2026 Shared Task 1: What Makes Vocabulary Difficult? https://arxiv.org/abs/2605.14257 [doi:10.48550/arxiv.2605.14257](https://doi.org/10.48550/arxiv.2605.14257)

`q2 · i?` · `design · r?`

Open-track results (Section 5.1, Table 2) report RMSE by L1 for the submissions: open_max mean 0.699, finetuned_llms_plus mean 0.699, finetuned_llms mean 0.710, against an open-track baseline mean of 1.133. The article notes the RMSE of approximately 0.7 is "relatively close to the statistical optimum of 0.277."

> "The models with added features (open_max and finetuned_llms_plus) surpassed all other submissions in the open track on all three languages."

## Discussion


## Related Claims
- [The explainable feature-based model with LLM-extracted features outperforms the closed-track encoder baseline by a wide margin](explainable-model-outperforms-closed-track-baseline.md) — related
- [Fine-tuning LLMs and MLMs with cross-entropy loss using soft targets outperforms standard discretization and regression-head approaches on vocabulary difficulty prediction](soft-target-finetuning-beats-standard-loss-vocabulary-difficulty.md) — related
