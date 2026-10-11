---
type: claim
title: Taxonomy-augmented guardrail classifiers reduce educational attack success more than general-purpose jailbreak defenses
description: Taxonomy-augmented guardrail classifiers reduce educational attack success more than general-purpose jailbreak defenses
id: taxonomy-augmented-guardrails-education-specific-risks
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: park-2026
    resource: "https://arxiv.org/abs/2608.02024"
    title: "Park, J., Han, J., Yoo, H., Ahn, S.-Y., Yoon, J., & Oh, A. (2026). EduZone: A Framework for Evaluating LLM Safety for K-12 Students and Teachers. arXiv preprint. https://arxiv.org/abs/2608.02024"
    author: "Park, J., Han, J., Yoo, H., Ahn, S.-Y., Yoon, J., & Oh, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Taxonomy-augmented guardrail classifiers reduce educational attack success more than general-purpose jailbreak defenses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Education-specific defenses outperform general-purpose defenses, with taxonomy-augmented classifiers SG+T (-30.1 pp), GOS+T (-25.6 pp), and LG3+T (-22.2 pp) achieving the largest ASR reductions. [→ Park 2026](#park-2026)

## Evidence

### Park 2026

Park, J., Han, J., Yoo, H., Ahn, S.-Y., Yoon, J., & Oh, A. (2026). EduZone: A Framework for Evaluating LLM Safety for K-12 Students and Teachers. arXiv preprint. https://arxiv.org/abs/2608.02024

`q2 · i?` · `design · r2`

Defense experiment on a stratified 10% sample of 260 educational scenarios balanced across six risk categories, comparing six general defenses against education-specific variants, in which "taxonomy-augmented classi- fiers achieve the largest ASR reductions". SG+T showed the most balanced performance; GOS+T excelled on privacy, misinformation, and academic misconduct.

> "Among them, taxonomy-augmented classi- fiers achieve the largest ASR reductions: SG+T (-30.1 pp), GOS+T (-25.6 pp), and LG3+T (-22.2 pp)."

## Discussion


## Related Claims
- [Current LLMs are more vulnerable to education-specific risks such as academic misconduct and excessive cognitive load than to conventional safety risks in K-12 educational interactions](eduzone-education-specific-risk-vulnerability.md) — related
- [LLM attack success rates increase consistently from single-turn to static multi-turn and dynamic multi-turn interactions in educational settings](asr-increases-dynamic-multi-turn-education.md) — related
- [No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation](no-llm-tutor-reliably-safe-60-percent-harm.md) — related
