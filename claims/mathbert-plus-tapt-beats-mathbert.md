---
type: claim
title: MathBERT+TAPT models outperform MathBERT alone on most metrics, significantly only for knowledge tracing
description: MathBERT+TAPT models outperform MathBERT alone on most metrics, significantly only for knowledge tracing
id: mathbert-plus-tapt-beats-mathbert
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: jia-tracy-shen-2021
    resource: "https://doi.org/10.48550/arXiv.2106.07340"
    title: "Jia Tracy Shen, Michiharu Yamashita, Ethan Prihar, Neil Heffernan, Xintao Wu, Ben Graff, Dongwon Lee. (2021). MathBERT: A Pre-trained Language Model for General NLP Tasks in Mathematics Education. [doi:10.48550/arXiv.2106.07340](https://doi.org/10.48550/arXiv.2106.07340)"
    author: Jia Tracy Shen, Michiharu Yamashita, Ethan Prihar, Neil Heffernan, Xintao Wu, Ben Graff, Dongwon Lee
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# MathBERT+TAPT models outperform MathBERT alone on most metrics, significantly only for knowledge tracing

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` MathBERT under-performs MathBERT+TAPT by 0.03% to 1.77% across metrics except KC F1, with significance only on Tkt metrics. [→ Jia Tracy Shen 2021](#jia-tracy-shen-2021)

## Evidence

### Jia Tracy Shen 2021

Jia Tracy Shen, Michiharu Yamashita, Ethan Prihar, Neil Heffernan, Xintao Wu, Ben Graff, Dongwon Lee. (2021). MathBERT: A Pre-trained Language Model for General NLP Tasks in Mathematics Education. [doi:10.48550/arXiv.2106.07340](https://doi.org/10.48550/arXiv.2106.07340)

`q2 · i?` · `design · r2`

Evaluation section comparing MathBERT fine-tuned directly against MathBERT further pre-trained on task data (MathBERT+TAPT); the paper reports under-performance "by 0.03 % to 1.77%" with significance only for knowledge tracing metrics.

> "We see both versions ofMathBERT under-perform the MathBERT+TAPT models by 0.03 % to 1.77% across all the metrics except for F1 score on 𝑇𝑘𝑐 from MathBERT-orig. However, only the metrics for𝑇𝑘𝑡 have obtained significance."

## Discussion


## Related Claims
- [MathBERT outperforms the best prior methods on three mathematics-education NLP tasks by 1.18% to 22.01% across metrics](mathbert-outperforms-prior-best-methods.md) — related
- [MathBERT outperforms BASE BERT by about 1.98% to 8.28% on the three tasks, with statistical significance](mathbert-outperforms-base-bert.md) — related
