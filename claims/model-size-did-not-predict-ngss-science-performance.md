---
type: claim
title: Model size did not correspond to higher scores in secondary science; small open-weight models outperformed significantly larger ones
description: Model size did not correspond to higher scores in secondary science; small open-weight models outperformed significantly larger ones
id: model-size-did-not-predict-ngss-science-performance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
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

# Model size did not correspond to higher scores in secondary science; small open-weight models outperformed significantly larger ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across the NGSS secondary science benchmarks, model size did not consistently predict performance; OSS-20b and Nemotron 3 Nano 30b a3 scored well across all metrics, outperforming significantly larger models. [→ Schroeder 2026](#schroeder-2026)

## Evidence

### Schroeder 2026

Schroeder, N. L., Ambarwati, Y. E., Zhang, Y., & Zhai, C. (2026). A Benchmark for LLM's Understanding of Middle School and High School Science. https://github.com/InviteInstitute/MS-NGSS-Aligned-Benchmark

`q2 · i?` · `design · r2`

Discussion of the benchmarking results in Part II: the two small models (20b and 30b parameters) scored well across all metrics while larger models such as Llama 3.3 70b scored lower. The authors conclude "model size did not correspond to higher scores in secondary science and model choice matters."

> "In our results, OSS-20b and Nemotron 3 Nano 30b a3 scored quite well across all metrics, outperforming models significantly larger than themselves."

## Discussion


## Related Claims
- [OSS 120b performed best across both NGSS-aligned secondary science benchmarks, with most tested open-weight models scoring above 90%](oss-120b-best-on-ngss-secondary-science-benchmark.md) — reports the opposite
- [Accuracy differences between the top efficient models were not statistically significant at the high school level but were significant at the middle school level, with Nemotron scoring better](mcnemar-accuracy-differences-hs-null-ms-significant.md) — related
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — reports the opposite
