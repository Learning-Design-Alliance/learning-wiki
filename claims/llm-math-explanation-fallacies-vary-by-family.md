---
type: claim
title: Dominant logical fallacies in LLM mathematical explanations shift from family to family and across prompting modes
description: Dominant logical fallacies in LLM mathematical explanations shift from family to family and across prompting modes
id: llm-math-explanation-fallacies-vary-by-family
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: esposito-2026
    resource: "https://doi.org/10.48550/arxiv.2604.27618"
    title: "Esposito, N., Tricarico, A., Porzio, L., Aghazadeh Ardebili, A., & Stella, M. (2026). Math Education Digital Shadows for Investigating Learning with GenAI: Mathematics Performance, Anxiety, and Confidence in LLMs. arXiv preprint. https://arxiv.org/abs/2604.27618 [doi:10.48550/arxiv.2604.27618](https://doi.org/10.48550/arxiv.2604.27618)"
    author: "Esposito, N., Tricarico, A., Porzio, L., Aghazadeh Ardebili, A., & Stella, M."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Dominant logical fallacies in LLM mathematical explanations shift from family to family and across prompting modes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fallacy detection rates in LLM mathematical explanations vary by model family and prompting mode, with circular reasoning, fallacy of logic, and fallacy of relevance dominating in different models. [→ Esposito 2026](#esposito-2026)

## Evidence

### Esposito 2026

Esposito, N., Tricarico, A., Porzio, L., Aghazadeh Ardebili, A., & Stella, M. (2026). Math Education Digital Shadows for Investigating Learning with GenAI: Mathematics Performance, Anxiety, and Confidence in LLMs. arXiv preprint. https://arxiv.org/abs/2604.27618 [doi:10.48550/arxiv.2604.27618](https://doi.org/10.48550/arxiv.2604.27618)

`q2 · i?` · `design · r2`

Fallacy classification of Task 1 explanations (Q4–Q6) using a DistilBERT fallacy classifier thresholded at the 85th percentile per category. The article reports that "Granite 4 Tiny, Ministral 14B, and Anita 24B show a marked reliance on circular reasoning in AI-assistant mode," while DeepSeek Chat shows appeal to emotion as dominant in both conditions.

> "Looking instead at the actual detection rates shown in Fig. 2a, the dominant fallacy shifts from family to family. Granite 4 Tiny, Ministral 14B, and Anita 24B show a marked reliance on circular reasoning in AI-assistant mode."

## Discussion


## Related Claims
- Family-level permutation tests do not detect reliable reasoning-versus-non-reasoning differences in accuracy, refusal, or consistency — related
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
- [Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive](llm-logical-inconsistency-scoring-feedback.md) — related
