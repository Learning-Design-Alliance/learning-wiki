---
type: claim
title: Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement
description: Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement
id: human-llm-agreement-gap-jaccard
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: liu-2026
    resource: "https://arxiv.org/abs/2607.28890"
    title: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890"
    author: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: liu-2026-2
    resource: "https://arxiv.org/abs/2607.28890"
    title: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890"
    author: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Mean human-LLM Jaccard across five models was 0.30 versus approximately 0.52 for human-human pairs, a gap of roughly 0.22 Jaccard points. [→ Liu 2026](#liu-2026)
`q2 i?` Pairwise agreement among the five LLMs ranged from 0.37 to 0.68, comparable to human-human agreement and notably higher than human-LLM agreement, indicating models share interpretive tendencies that differ from human patterns. [→ Liu 2026 (2)](#liu-2026-2)

## Evidence

### Liu 2026

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i?` · `design · r2`

Agreement analysis of the five focal LLMs and three human coders across 2,210 eligible messages, using Jaccard similarity between code sets. Human-LLM agreement (mean 0.30) sat roughly 0.22 Jaccard points below the human-human baseline of approximately 0.52 on the 284-message overlap set.

> "Mean human-LLM Jaccard across models was 0.30 (range 0.23 to 0.34), with exact match rates of 13.5% to 17.6%. On the overlap set of 284 messages coded by multiple humans, pairwise human-human Jaccard mean approximately 0.52, leaving a gap of roughly 0.22 Jaccard points between human-human and human-LLM agreement."

### Liu 2026 (2)

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i?` · `design · r2`

Same agreement analysis at the model level. LLM-LLM Jaccard ranged from 0.37 to 0.68; all three human coders showed the same relative ordering of model agreement, which the authors read as "a structural difference rather than idiosyncratic coder variation".

> "Pairwise agreement among the five LLMs ranged from 0.37 to 0.68, with Gemini Flash, GPT-5.5, and Claude Opus forming a high-agreement cluster and GPT-4o the most divergent model. LLM-LLM agreement is therefore comparable to human-human agreement and notably higher than human-LLM agreement, indicating that models share interpretive tendencies that differ from human patterns."

## Discussion


## Related Claims
- [Human-LLM agreement is moderated by code properties, multi-model consensus, and model-reported confidence](agreement-moderators-tiers-consensus-confidence.md) — related
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest](llm-within-configuration-reliability-high.md) — related
- [An LLM-based analogy judge validated against expert judgments shows moderate-to-strong agreement and screens most generated analogies as meeting baseline adequacy](anvil-llm-judge-analogy-screening.md) — related
- [CLARA achieves the highest agreement with blinded human developmental ranking judgments compared with readability and prompting baselines](clara-highest-human-ranking-agreement.md) — related
- [The LLM observation function's per-answer mastery evidence correlates with true mastery at r = 0.68 pooled, but only r ≈ 0.15 within the weak tier, making it least reliable for low-ability learners](collearn-observation-function-within-tier-reliability.md) — related
- [Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)](judge-anchoring-raises-human-agreement.md) — related
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — related
- [LLM-judge evaluation of tutoring sycophancy shows systematic self-judge blind spots and missed sycophancy even under judge consensus](llm-judge-reliability-tutoring-sycophancy.md) — related
