---
type: claim
title: "The two-stage query with SCS elevates grading process up to 40% on the LL dataset and up to 30% at the beginning on the JRL dataset compared to conventional AL"
description: "The two-stage query with SCS elevates grading process up to 40% on the LL dataset and up to 30% at the beginning on the JRL dataset compared to conventional AL"
id: age-elevates-grading-ll-jrl
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: mohammad-iqbal-2024
    resource: "https://doi.org/10.21203/rs.3.rs-5651820/v1"
    title: "Mohammad Iqbal, Tsamara Rana Nugraha and Hsing-Kuo Pao. (2024). Active Grade Estimator on Short Answer Assessment. https://doi.org/10.21203/rs.3.rs-5651820/v1"
    author: Mohammad Iqbal, Tsamara Rana Nugraha and Hsing-Kuo Pao
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The two-stage query with SCS elevates grading process up to 40% on the LL dataset and up to 30% at the beginning on the JRL dataset compared to conventional AL

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the LL dataset, AGE with summarization and VM elevates the grading process up to 40%; on the JRL dataset, it elevates grading up to 30% at the very beginning of iterations. [→ Mohammad Iqbal 2024](#mohammad-iqbal-2024)

## Evidence

### Mohammad Iqbal 2024

Mohammad Iqbal, Tsamara Rana Nugraha and Hsing-Kuo Pao. (2024). Active Grade Estimator on Short Answer Assessment. https://doi.org/10.21203/rs.3.rs-5651820/v1

`q2 · i?` · `design · r2`

Numerical comparison on the UNT dataset answer-key-length scenarios shown in Fig. 4(a). The article reports AGE on the LL dataset performs way better "by elevating the grading pr ocess up to 40%".

> "In general, AGE on the LL dataset continues to perform way bette r with the help of summarization and voting mechanisms by elevating the grading pr ocess up to 40%."

## Discussion


## Related Claims
- [Instead of cutting answers, the proposed model converges faster than conventional AL and elevates grading up to 30% at the very beginning on the JRL dataset](age-converges-faster-jrl-30-percent.md) — possibly the same claim (merge candidate)
- [AGE reduces teacher grading burden by requiring only 1% of student answers in the UNT dataset to be graded](age-grades-only-one-percent-unt.md) — related
- [GPT-4 surpasses other LLMs in the AGE query selection with an accuracy rate 15% better](gpt4-surpasses-other-llms-15-percent.md) — related
- [On the mismatch-grade dataset, all models without the voting mechanism diverge, while AGE with VM estimates student answers increasingly precisely](vm-prevents-divergence-mmg.md) — related
