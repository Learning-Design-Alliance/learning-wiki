---
type: claim
title: "MathBERT outperforms BASE BERT by about 1.98% to 8.28% on the three tasks, with statistical significance"
description: "MathBERT outperforms BASE BERT by about 1.98% to 8.28% on the three tasks, with statistical significance"
id: mathbert-outperforms-base-bert
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
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

# MathBERT outperforms BASE BERT by about 1.98% to 8.28% on the three tasks, with statistical significance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Both MathBERT versions significantly outperform BASE BERT without further pre-training on all three tasks and metrics. [→ Jia Tracy Shen 2021](#jia-tracy-shen-2021)

## Evidence

### Jia Tracy Shen 2021

Jia Tracy Shen, Michiharu Yamashita, Ethan Prihar, Neil Heffernan, Xintao Wu, Ben Graff, Dongwon Lee. (2021). MathBERT: A Pre-trained Language Model for General NLP Tasks in Mathematics Education. [doi:10.48550/arXiv.2106.07340](https://doi.org/10.48550/arXiv.2106.07340)

`q2 · i?` · `design · r2`

Evaluation section: fine-tuned MathBERT-orig and MathBERT-custom compared to BASE BERT across Tkc, Tag, and Tkt with five random seeds and t-tests; the paper reports improvements of "about 2.14 % to 8.28%" (orig) and "about 1.98% to 8.21%" (custom), all statistically significant.

> "MathBERT-orig outperforms BASE BERT by about 2.14 % to 8.28%, all with statistical significance and MathBERT-custom outperforms it by about 1.98% to 8.21% across metrics and tasks, all with statistical significance."

## Discussion


## Related Claims
- [MathBERT outperforms the best prior methods on three mathematics-education NLP tasks by 1.18% to 22.01% across metrics](mathbert-outperforms-prior-best-methods.md) — related
- [MathBERT+TAPT models outperform MathBERT alone on most metrics, significantly only for knowledge tracing](mathbert-plus-tapt-beats-mathbert.md) — related
