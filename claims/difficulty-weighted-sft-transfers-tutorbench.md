---
type: claim
title: "A single difficulty-weighted SFT run on a vision-language base model reaches 61.64% overall accuracy on TutorBench, surpassing Gemini-3 Pro (58.52%)"
description: "A single difficulty-weighted SFT run on a vision-language base model reaches 61.64% overall accuracy on TutorBench, surpassing Gemini-3 Pro (58.52%)"
id: difficulty-weighted-sft-transfers-tutorbench
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: singh-2026
    resource: "https://doi.org/10.48550/arxiv.2604.06385"
    title: "Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R. (2026). Application-Driven Pedagogical Knowledge Optimization of Open-Source LLMs via Reinforcement Learning and Supervised Fine-Tuning. Preprint. https://arxiv.org/abs/2604.06385 [doi:10.48550/arxiv.2604.06385](https://doi.org/10.48550/arxiv.2604.06385)"
    author: "Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A single difficulty-weighted SFT run on a vision-language base model reaches 61.64% overall accuracy on TutorBench, surpassing Gemini-3 Pro (58.52%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` EduQwen 30B-VL-SFT, produced by one SFT run from the Qwen3-30B-VL baseline (55.39%), achieves 61.64% overall accuracy on TutorBench, above Gemini-3 Pro's 58.52%. [→ Singh 2026](#singh-2026)

## Evidence

### Singh 2026

Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R. (2026). Application-Driven Pedagogical Knowledge Optimization of Open-Source LLMs via Reinforcement Learning and Supervised Fine-Tuning. Preprint. https://arxiv.org/abs/2604.06385 [doi:10.48550/arxiv.2604.06385](https://doi.org/10.48550/arxiv.2604.06385)

`q2 · i?` · `design · r2`

Preliminary transfer experiment on TutorBench, a multimodal tutoring benchmark, using a single SFT run with 596 high-quality synthetic responses filtered from model outputs, judged by Claude-4.5-Sonnet. The model achieved "61.64% overall accuracy".

> "our SFT-optimized model (EduQwen 30B-VL-SFT) achieves 61.64% overall accuracy, surpass- ing Gemini-3 Pro (58.52%), a top-performing model on the TutorBench leaderboard (Rank no. 3) (scale.com, 2025), despite starting from a weaker baseline (55.39%)."

## Discussion


## Related Claims
- [The EduQwen 32B models achieve up to 96.52% accuracy on the CDPK Benchmark, surpassing the previous leaderboard leader Gemini-3 Pro at 90.55%](eduqwen-32b-sota-cdpk-benchmark.md) — related
- [Specializing models for K-12 education does not require a broad loss of general capability, with MMMU-Pro accuracy increasing at all three scales](omniedu-general-capability-retained-after-specialization.md) — related
- [Frontier-model choice affects LecturaAgents performance, with Gemini 3 Pro ranking first at 80.4% AAR](lecturaagents-frontier-model-evaluation-aar.md) — related
