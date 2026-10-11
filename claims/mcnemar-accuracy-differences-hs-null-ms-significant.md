---
type: claim
title: Accuracy differences between the top efficient models were not statistically significant at the high school level but were significant at the middle school level, with Nemotron scoring better
description: Accuracy differences between the top efficient models were not statistically significant at the high school level but were significant at the middle school level, with Nemotron scoring better
id: mcnemar-accuracy-differences-hs-null-ms-significant
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: mixed
sources:
  - id: schroeder-2026
    resource: "https://github.com/InviteInstitute/MS-NGSS-Aligned-Benchmark"
    title: "Schroeder, N. L., Ambarwati, Y. E., Zhang, Y., & Zhai, C. (2026). A Benchmark for LLM's Understanding of Middle School and High School Science. https://github.com/InviteInstitute/MS-NGSS-Aligned-Benchmark"
    author: "Schroeder, N. L., Ambarwati, Y. E., Zhang, Y., & Zhai, C."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Accuracy differences between the top efficient models were not statistically significant at the high school level but were significant at the middle school level, with Nemotron scoring better

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Pairwise McNemar tests with Holm-Bonferroni corrections found no statistically significant accuracy differences between OSS-20b and Nemotron 3 Nano 30b a3 at the high school level, but significant differences at the middle school level favoring Nemotron. [→ Schroeder 2026](#schroeder-2026)

## Evidence

### Schroeder 2026

Schroeder, N. L., Ambarwati, Y. E., Zhang, Y., & Zhai, C. (2026). A Benchmark for LLM's Understanding of Middle School and High School Science. https://github.com/InviteInstitute/MS-NGSS-Aligned-Benchmark

`q2 · i?` · `design · r2`

Statistical comparison (Part II results) of the two efficiency leaders, OSS-20b (94% middle school, 96% high school one-shot) and Nemotron 3 Nano 30b a3 (97% on both). The result holds at high school but not middle school, so the claim is limited accordingly.

> "The differences between the models' accuracy were not statistically significant using pairwise McNemar tests with Holm-Bonferroni corrections at the high school level, but they were at the middle school level, with Nemotron scoring significantly better."

## Discussion


## Related Claims
- [A task-specific prompt with explicit guidance about correct-answer cases significantly outperforms literature-based PedCoT prompting on TM test cases (84% vs 59% accuracy)](task-specific-prompt-beats-pedcot-prompting.md) — related
- [Model size did not correspond to higher scores in secondary science; small open-weight models outperformed significantly larger ones](model-size-did-not-predict-ngss-science-performance.md) — related
- [OSS 120b performed best across both NGSS-aligned secondary science benchmarks, with most tested open-weight models scoring above 90%](oss-120b-best-on-ngss-secondary-science-benchmark.md) — related
