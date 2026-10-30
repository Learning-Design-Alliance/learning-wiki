---
type: claim
title: On the mismatch-grade dataset, all models without the voting mechanism diverge, while AGE with VM estimates student answers increasingly precisely
description: On the mismatch-grade dataset, all models without the voting mechanism diverge, while AGE with VM estimates student answers increasingly precisely
id: vm-prevents-divergence-mmg
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

# On the mismatch-grade dataset, all models without the voting mechanism diverge, while AGE with VM estimates student answers increasingly precisely

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the MMG dataset, all models without VM went divergent, and the proposed model with VM estimates student answers more and more precisely. [→ Mohammad Iqbal 2024](#mohammad-iqbal-2024)

## Evidence

### Mohammad Iqbal 2024

Mohammad Iqbal, Tsamara Rana Nugraha and Hsing-Kuo Pao. (2024). Active Grade Estimator on Short Answer Assessment. https://doi.org/10.21203/rs.3.rs-5651820/v1

`q2 · i?` · `design · r2`

Numerical comparison on the mismatch-grade (MMG) subset of the UNT dataset shown in Fig. 6(b). Models without the voting mechanism diverge; the article reports the proposed model "estimates the student answers more and more precisely".

> "As expected, all models w.o. VM went too badly as they were divergent. Even for SS, SC, and SCS prompts, none of them can reduce their errors. With no doubt, the proposed model estimates the student answers more and more precisely; in this case , diﬀerent grading viewpoints from the multiple teachers."

## Discussion


## Related Claims

- [The two-stage query with SCS elevates grading process up to 40% on the LL dataset and up to 30% at the beginning on the JRL dataset compared to conventional AL](age-elevates-grading-ll-jrl.md) — related
- [Instead of cutting answers, the proposed model converges faster than conventional AL and elevates grading up to 30% at the very beginning on the JRL dataset](age-converges-faster-jrl-30-percent.md) — related
- [GPT-4 surpasses other LLMs in the AGE query selection with an accuracy rate 15% better](gpt4-surpasses-other-llms-15-percent.md)
