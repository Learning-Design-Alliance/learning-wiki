---
type: claim
title: Montessori-Instruct outperforms all baselines on out-of-domain tasks, with maximum MT-Bench improvements of 0.673 and 0.372
description: Montessori-Instruct outperforms all baselines on out-of-domain tasks, with maximum MT-Bench improvements of 0.673 and 0.372
id: montessori-instruct-out-of-domain-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: xiaochuan-li-2024
    resource: "https://doi.org/10.48550/arXiv.2410.14208"
    title: "Xiaochuan Li, Zichun Yu, Chenyan Xiong. (2024). MONTESSORI-INSTRUCT: GENERATE INFLUENTIAL TRAINING DATA TAILORED FOR STUDENT LEARNING. Preprint. [doi:10.48550/arXiv.2410.14208](https://doi.org/10.48550/arXiv.2410.14208)"
    author: Xiaochuan Li, Zichun Yu, Chenyan Xiong
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Montessori-Instruct outperforms all baselines on out-of-domain tasks, with maximum MT-Bench improvements of 0.673 and 0.372

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On out-of-domain tasks, Montessori-Instruct outperforms all baselines, achieving maximum improvements of 0.673 and 0.372 on MT-Bench in the 8B and 1.1B settings respectively, indicating the optimized teacher does not overfit the reference tasks. [→ Xiaochuan Li 2024](#xiaochuan-li-2024)

## Evidence

### Xiaochuan Li 2024

Xiaochuan Li, Zichun Yu, Chenyan Xiong. (2024). MONTESSORI-INSTRUCT: GENERATE INFLUENTIAL TRAINING DATA TAILORED FOR STUDENT LEARNING. Preprint. [doi:10.48550/arXiv.2410.14208](https://doi.org/10.48550/arXiv.2410.14208)

`q2 · i?` · `causal · r2`

Out-of-domain evaluation in §5.1 (Table 1) across MT-Bench, ARC-Challenge, GSM8K, HellaSwag, GPQA and MMLU for both the 8B and 1.1B students. The article reports the method "outperforms all the baselines on out-of-domain tasks" with the printed MT-Bench maxima.

> "Montessori-Instruct also outperforms all the baselines on out-of-domain tasks, achieving maximum improvements of 0.673 and 0.372 on the MT-Bench in the 8B and 1.1B settings, respectively."

## Discussion


## Related Claims
- [Montessori-Instruct significantly outperforms Self-Instruct on in-domain Alpaca Eval in the 8B setting](montessori-instruct-outperforms-self-instruct-alpaca-eval.md) — related
- [Data from a teacher optimized for a 1.1B student's preferences yields consistent gains across four different student models](montessori-data-generalizes-across-students.md) — related
