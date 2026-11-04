---
type: claim
title: "Scaling Qwen2.5 from 3B to 32B parameters improved both metrics and reduced the consistency gap by approximately 50%"
description: "Scaling Qwen2.5 from 3B to 32B parameters improved both metrics and reduced the consistency gap by approximately 50%"
id: model-scaling-reduces-consistency-gap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: cha-j-2026
    resource: "https://doi.org/10.2196/95342"
    title: "Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342"
    author: Cha J, Zhao Y, Zong H.
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# Scaling Qwen2.5 from 3B to 32B parameters improved both metrics and reduced the consistency gap by approximately 50%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Increasing Qwen2.5 size from 3B to 32B raised QPR from 74.4% to 89.6% and CPR from 48.1% to 76.2%, with all comparisons between the 3B model and larger models significant (all P<.001). [→ Cha J 2026](#cha-j-2026)
`q3 i?` The consistency gap declined from 26.3% in the 3B model to 13.5% in the 32B model, a reduction of approximately 50%. [→ Cha J 2026](#cha-j-2026)

## Evidence

### Cha J 2026

Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342

`q3 · i?` · `associational · r2`

Scaling analysis of the Qwen2.5 family (3B, 7B, 14B, 32B deployed locally via Ollama) on the same 473 questions and 189 cases. Both metrics improved with size; the 32B model significantly outperformed the 7B model in QPR (P=.02), but 7B vs 14B and 14B vs 32B CPR differences were not significant.

> "The gap reduced by approximately 50%, from 26.3% in the 3B model to 13.5% in the 32B model. This pattern suggests that while smaller models may correctly answer individual questions, larger models are more likely to achieve success on complete patient cases."

## Discussion


## Related Claims
- [LLMs with high question-level accuracy on medical licensing exam cases show substantially lower case-level accuracy, with consistency gaps of 10% to 17.9%](llm-consistency-gap-question-vs-case-level.md) — related
- [In the fine-tuning experiments, increasing base model size up to 32B parameters improved performance, and larger LLMs consistently outperformed smaller MLMs](model-size-and-llm-vs-mlm-performance-vocabulary-difficulty.md) — related
- [Observed case pass rates closely align with expected case pass rates computed under question independence](observed-cpr-matches-expected-independence-benchmark.md) — related
