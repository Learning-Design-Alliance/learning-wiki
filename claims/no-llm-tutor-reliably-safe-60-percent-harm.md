---
type: claim
title: "No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation"
description: "No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation"
id: no-llm-tutor-reliably-safe-60-percent-harm
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: rima-hazra-2026
    resource: "https://arxiv.org/abs/2603.17373"
    title: "Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373"
    author: Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Every evaluated model exceeds a 60% harm rate on at least five risk categories in single-turn and six in multi-turn settings. [→ Rima Hazra 2026](#rima-hazra-2026)

## Evidence

### Rima Hazra 2026

Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373

`q2 · i?` · `design · r2`

Benchmark evaluation of ten open-weight LLMs (3.8B-72B) and one closed-weight model on SAFETUTORS across three STEM subjects and eleven harm dimensions, with harm rates reported in Tables 1 and 2. The article reports that "Every evaluated model exceeds 60% harm rate" on at least five single-turn and six multi-turn categories; no effect size is printed.

> "No model is universally safe:Every evaluated model exceeds 60% harm rate on at least five cat- egories in single-turn and six in multi-turn."

## Discussion


## Related Claims
- [Informational harm is the sole dimension that decreases in multi-turn interaction, dropping from 60.52% to 11.90%](informational-harm-drops-multi-turn.md) — related
- [Adaptive multi-turn interactions substantially amplify LLM vulnerabilities to conventional safety risks in educational contexts](dynamic-multi-turn-amplifies-conventional-risks.md) — related
- [LLM attack success rates increase consistently from single-turn to static multi-turn and dynamic multi-turn interactions in educational settings](asr-increases-dynamic-multi-turn-education.md) — related
- [Multi-turn interaction amplifies pedagogical harm: mean harm rises 6-11 percentage points across subjects and pedagogical-relationship harm surges from 17.7% to 77.8%](multi-turn-dialogue-amplifies-tutor-harm.md) — related
- [Current LLMs are more vulnerable to education-specific risks such as academic misconduct and excessive cognitive load than to conventional safety risks in K-12 educational interactions](eduzone-education-specific-risk-vulnerability.md) — related
- [Risk category explains the largest share of variation in educational attack success, far more than LLM usage context or curriculum topic](risk-category-dominates-educational-safety-variance.md) — related
- [Taxonomy-augmented guardrail classifiers reduce educational attack success more than general-purpose jailbreak defenses](taxonomy-augmented-guardrails-education-specific-risks.md) — related
- [Single-turn tutors disclose answers pervasively while challenge scores are near zero across every model and subject](single-turn-answer-disclosure-challenge-near-zero.md) — related
- [Harm profiles are subject-dependent: metacognitive harm crosses 90% in all three subjects in multi-turn, peaking at 97.44% for Qwen2.5-32B in Mathematics](tutor-harm-subject-dependent-mitigations.md) — related
