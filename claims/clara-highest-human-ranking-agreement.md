---
type: claim
title: CLARA achieves the highest agreement with blinded human developmental ranking judgments compared with readability and prompting baselines
description: CLARA achieves the highest agreement with blinded human developmental ranking judgments compared with readability and prompting baselines
id: clara-highest-human-ranking-agreement
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: sijing-yin-2026
    resource: "https://arxiv.org/abs/2610.05783"
    title: "Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu. (2026). CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?. https://arxiv.org/abs/2610.05783"
    author: Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CLARA achieves the highest agreement with blinded human developmental ranking judgments compared with readability and prompting baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On 60 blinded story-pair ranking judgments, CLARA reaches higher agreement with human developmental rankings than FKGL, direct prompting, and rubric-guided prompting. [→ Sijing Yin 2026](#sijing-yin-2026)

## Evidence

### Sijing Yin 2026

Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu. (2026). CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?. https://arxiv.org/abs/2610.05783

`q2 · i?` · `design · r2`

Blinded human developmental ranking validation using 60 story pairs covering adjacent and distant developmental stages, comparing human pairwise rankings against readability metrics, direct prompting, rubric-guided prompting, and CLARA. The article reports "CLARA achieves the high- est agreement with human developmental judg- ments" (0.81 versus 0.58 for FKGL and 0.67 for direct prompting).

> "As shown in Table 8, CLARA achieves the high- est agreement with human developmental judg- ments, suggesting that structured developmental annotation better captures relative developmental complexity than readability-based or direct prompt- ing approaches."

## Discussion


## Related Claims
- [Developmental representations remain relatively stable across translated bilingual narratives](clara-bilingual-translation-consistency.md) — related
- [CLARA annotations align with blinded educator judgments, with 0.81 pairwise agreement and highest-rated educational interpretability](clara-educator-agreement-interpretability.md) — related
- [Structured developmental annotation (CLARA) achieves stronger alignment with developmental references than readability-based and direct prompting baselines](clara-outperforms-readability-and-prompting-baselines.md) — possibly the same claim (merge candidate)
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding](agreement-quality-divergence-human-consensus-bias.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [In disagreement cases, blinded educators more frequently prefer CLARA developmental estimates over publisher recommendations](educators-prefer-clara-over-publisher-labels.md) — related
