---
type: claim
title: The explainable feature-based model with LLM-extracted features outperforms the closed-track encoder baseline by a wide margin
description: The explainable feature-based model with LLM-extracted features outperforms the closed-track encoder baseline by a wide margin
id: explainable-model-outperforms-closed-track-baseline
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: adam-nohejl-2026
    resource: "https://arxiv.org/abs/2605.14257"
    title: "Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka. (2026). Sakura at BEA 2026 Shared Task 1: What Makes Vocabulary Difficult? https://arxiv.org/abs/2605.14257"
    author: Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka
    q: 2
    i: "?"
---

# The explainable feature-based model with LLM-extracted features outperforms the closed-track encoder baseline by a wide margin

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` The explainable model achieved mean RMSE of 1.067 versus the closed-track baseline's 1.218, and the traditional-features-only variant performed on par with the baseline. [→ Adam Nohejl 2026](#adam-nohejl-2026)

## Evidence

### Adam Nohejl 2026

Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka. (2026). Sakura at BEA 2026 Shared Task 1: What Makes Vocabulary Difficult? https://arxiv.org/abs/2605.14257

`q2 · i?`

Closed-track results (Section 5.2, Table 3) comparing submissions to the fine-tuned XLM-RoBERTa baseline: explainable mean RMSE 1.067, traditional 1.193, closed_max 0.921, baseline 1.218. The explainable model "outperforms the baseline by a relatively wide margin."

> "Interestingly, our model with only traditional features performs on par with the encoder-based baseline, and ourexplainable model with extra LLM-based features outperforms the baseline by a relatively wide margin (mean RMSEof1.218vs.1.067)."

## Discussion


## Related Claims
- [The team's open-track submissions with added features surpassed all other shared task submissions on all three languages, with RMSE near 0.7](open-track-submissions-surpassed-all-others.md) — related
