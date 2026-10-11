---
type: claim
title: An LLM-based analogy judge validated against expert judgments shows moderate-to-strong agreement and screens most generated analogies as meeting baseline adequacy
description: An LLM-based analogy judge validated against expert judgments shows moderate-to-strong agreement and screens most generated analogies as meeting baseline adequacy
id: anvil-llm-judge-analogy-screening
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: noviello-2026
    resource: "https://arxiv.org/abs/2605.16295"
    title: "Noviello, Y., Birillo, A., Migut, G. (2026). ANVIL: Analogies and Videos for Lecturers. https://arxiv.org/abs/2605.16295"
    author: Noviello, Y., Birillo, A., Migut, G.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: noviello-2026-2
    resource: "https://arxiv.org/abs/2605.16295"
    title: "Noviello, Y., Birillo, A., Migut, G. (2026). ANVIL: Analogies and Videos for Lecturers. https://arxiv.org/abs/2605.16295"
    author: Noviello, Y., Birillo, A., Migut, G.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# An LLM-based analogy judge validated against expert judgments shows moderate-to-strong agreement and screens most generated analogies as meeting baseline adequacy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Against expert judgments with controlled negative examples, the gpt-5.2-based judge reached alpha = 0.66 for TCC and 0.67 for MS on the 4-point scale, and perfect agreement for TCC (alpha = 1.00) and strong for MS (alpha = 0.81) on collapsed labels. [→ Noviello 2026](#noviello-2026)
`q2 i?` Applied to n=50 concept-analogy pairs, 88% of analogies met the TCC threshold and 92% met the MS threshold, with mean scores of 3.52±0.50 (TCC) and 3.55±0.47 (MS). [→ Noviello 2026 (2)](#noviello-2026-2)

## Evidence

### Noviello 2026

Noviello, Y., Birillo, A., Migut, G. (2026). ANVIL: Analogies and Videos for Lecturers. https://arxiv.org/abs/2605.16295

`q2 · i?` · `design · r2`

Validation of an LLM-based judge (three independent gpt-5.2 runs averaged) against expert medians on the expert-rated dataset plus three controlled negative examples constructed following prior work on plausible but incorrect analogies.

> "On the 4-point ordinal scale,agreementbetween the LLM-based evaluator and experts was moderate (α= 0.66for TCC,α= 0.67for MS). On the collapsed labels (1–2 vs. 3–4), agreement was perfect for TCC (α= 1.00) and strong for MS (α= 0.81)."

### Noviello 2026 (2)

Noviello, Y., Birillo, A., Migut, G. (2026). ANVIL: Analogies and Videos for Lecturers. https://arxiv.org/abs/2605.16295

`q2 · i?` · `design · r2`

Scale application of the judge to the n=50 concept-analogy pairs generated for the robustness analysis, estimating how many system outputs would meet a baseline standard for educator use.

> "The results show that the majority of analogies met the threshold under the collapsed two-level label (TCC:88%, MS:92%). Mean scores were concentrated toward the upper end of the scale, with TCC at3.52±0.50and MS at3.55±0.47."

## Discussion


## Related Claims
- [CS/SE educators rate ANVIL analogies highly and animations as generally faithful, with disagreement concentrated in borderline and visual-clarity judgments](anvil-educator-ratings-analogy-animation-quality.md) — related
- [LLM-as-judge automated evaluation can achieve human-level agreement when carefully validated](llm-as-judge-human-level-agreement-with-validation.md) — a broader claim this one bears on
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)](judge-anchoring-raises-human-agreement.md) — related
- [A Gemini-based creativity autorater scores real students' complex multimedia creativity tasks on par with human experts (item Kappa 0.66; total-score Pearson r = 0.88)](gemini-autorater-creativity-real-students.md) — related
- [Gemini-2.5-Pro can effectively replicate human expert judgments when answering SLM-generated MCQs](gemini-surrogate-judge-replicates-human-answers.md) — related
