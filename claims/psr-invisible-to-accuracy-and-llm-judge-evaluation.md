---
type: claim
title: Structural knowledge deficits in LLMs remain invisible to accuracy-based and LLM-as-judge reasoning evaluations
description: Structural knowledge deficits in LLMs remain invisible to accuracy-based and LLM-as-judge reasoning evaluations
id: psr-invisible-to-accuracy-and-llm-judge-evaluation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: peng-cui-2026
    resource: "https://doi.org/10.18653/2026.findings-emnlp.494"
    title: "Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. [doi:10.18653/2026.findings-emnlp.494](https://doi.org/10.18653/2026.findings-emnlp.494)"
    author: Peng Cui, Heejin Do, and Mrinmaya Sachan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Structural knowledge deficits in LLMs remain invisible to accuracy-based and LLM-as-judge reasoning evaluations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Among the strongest open-source models, LLM-as-judge reasoning scores differ only modestly while PSR = 1.0 rates vary non-monotonically, so models that appear similarly strong under reasoning evaluation differ in prerequisite satisfaction. [→ Peng Cui 2026](#peng-cui-2026)

## Evidence

### Peng Cui 2026

Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. [doi:10.18653/2026.findings-emnlp.494](https://doi.org/10.18653/2026.findings-emnlp.494)

`q2 · i?` · `design · r2`

Appendix C comparison scoring reasoning traces of five open-source models with GPT-4.1-MINI as LLM-as-judge on Relevance, Coherence, and Accuracy dimensions (per Do et al., 2025), plotted against PSR metrics in Figure 6. Reasoning scores and PSR "exhibit different patterns in the high-performance regime", with PSR remaining "more variable and non-monotonic".

> "Specifically, Relevance increases from 4.76 for LLAMA-3.1-70B-INSTRUCT to 4.86 for QWEN2.5-7B-INSTRUCTand 4.93 for QWEN2.5-32B-INSTRUCT, while the corresponding PSR = 1.0 rates are 20.81%, 27.32%, and 25.44%, respectively."

## Discussion


## Related Claims
- [LLMs satisfy mathematical prerequisite dependencies far less often than human learners despite matching or exceeding human accuracy](llms-violate-prerequisite-dependencies-despite-high-accuracy.md) — a narrower finding that bears on this claim
- [The LLM-judge separates weak submissions but its ranking of the strongest systems has almost no agreement with crowd ranking (Spearman ρ = −0.17)](llm-judge-ranks-strongest-systems-poorly.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
