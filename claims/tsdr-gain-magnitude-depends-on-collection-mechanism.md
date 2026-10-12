---
type: claim
title: "TSDR's AUC gains are largest on open-ended platforms and limited on EdNet, whose mandatory bundle completion policy constrains selection bias"
description: "TSDR's AUC gains are largest on open-ended platforms and limited on EdNet, whose mandatory bundle completion policy constrains selection bias"
id: tsdr-gain-magnitude-depends-on-collection-mechanism
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: peilin-zhan-2026
    resource: "https://arxiv.org/abs/2605.05958"
    title: "Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958"
    author: Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: peilin-zhan-2026-2
    resource: "https://arxiv.org/abs/2605.05958"
    title: "Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958"
    author: Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# TSDR's AUC gains are largest on open-ended platforms and limited on EdNet, whose mandatory bundle completion policy constrains selection bias

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` TSDR improves AKT by 5.06% on the Prob dataset and SparseKT by 4.76% on Assist17 in AUC. [→ Peilin Zhan 2026](#peilin-zhan-2026)
`q2 i?` Improvements on EdNet and Linux are relatively limited, with an AUC gain of approximately 1% on EdNet, attributed to its mandatory bundle completion policy. [→ Peilin Zhan 2026 (2)](#peilin-zhan-2026-2)

## Evidence

### Peilin Zhan 2026

Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958

`q2 · i?` · `design · r2`

Benchmark comparison (RQ1, Table 1) of TSDR-enhanced versus original models. The article reports "TSDR improves AKT by 5.06% on the Prob dataset and SparseKT by 4.76% on Assist17."

> "For instance, TSDR improves AKT by 5.06% on the Prob dataset and SparseKT by 4.76% on Assist17."

### Peilin Zhan 2026 (2)

Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958

`q2 · i?` · `design · r2`

Benchmark comparison (RQ1) on EdNet, whose design "enforces a mandatory 'bundle' completion policy" limiting selection bias, making missingness closer to random. The article reports "an AUC gain of approximately 1% on EdNet."

> "the improvements on EdNet and Linux are relatively limited, as exemplified by an AUC gain of approximately 1% on EdNet"

## Discussion


## Related Claims
- [TSDR is robust to the smoothness coefficient, with a stable sweet spot for lambda in (0.3, 1.0)](tsdr-lambda-sweet-spot-robustness.md) — related
- [Under controlled synthetic MNAR bias, TSDR-equipped models improve across the entire bias spectrum, with the RMSE advantage diminishing beyond gamma > 0.8](tsdr-robust-across-mnar-spectrum.md) — related
