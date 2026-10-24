---
type: claim
title: "Harm profiles are subject-dependent: metacognitive harm crosses 90% in all three subjects in multi-turn, peaking at 97.44% for Qwen2.5-32B in Mathematics"
description: "Harm profiles are subject-dependent: metacognitive harm crosses 90% in all three subjects in multi-turn, peaking at 97.44% for Qwen2.5-32B in Mathematics"
id: tutor-harm-subject-dependent-mitigations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: rima-hazra-2026
    resource: "https://doi.org/10.48550/arxiv.2603.17373"
    title: "Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373 [doi:10.48550/arxiv.2603.17373](https://doi.org/10.48550/arxiv.2603.17373)"
    author: Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Harm profiles are subject-dependent: metacognitive harm crosses 90% in all three subjects in multi-turn, peaking at 97.44% for Qwen2.5-32B in Mathematics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Multi-turn metacognitive harm exceeds 90% in all three subjects, peaking at 97.44% for Qwen2.5-32B in Mathematics, indicating mitigations must be discipline-aware. [→ Rima Hazra 2026](#rima-hazra-2026)

## Evidence

### Rima Hazra 2026

Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373 [doi:10.48550/arxiv.2603.17373](https://doi.org/10.48550/arxiv.2603.17373)

`q2 · i?` · `design · r2`

Multi-turn results across mathematics, physics, and chemistry show metacognitive harm above 90% in every subject, "peaking at 97.44% for Qwen2.5-32B in Mathematics". The article concludes mitigation strategies must be discipline-aware; no effect size is printed.

> "Metacognitive harm crosses 90% in all three subjects in multi-turn, peaking at 97.44% for Qwen2.5-32B in Mathematics."

## Discussion


## Learner Variables
- [Metacognition](../learner-variables/metacognition.md) — outcome: instruction changes it

## Related Claims
- [Multi-turn interaction amplifies pedagogical harm: mean harm rises 6-11 percentage points across subjects and pedagogical-relationship harm surges from 17.7% to 77.8%](multi-turn-dialogue-amplifies-tutor-harm.md) — related
- [No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation](no-llm-tutor-reliably-safe-60-percent-harm.md) — related
- [LLM teaching effectiveness varies substantially across subject domains, strongest where knowledge points apply directly and weakest in physics and chemistry](llm-teaching-effectiveness-varies-by-domain.md) — related
- [Informational harm is the sole dimension that decreases in multi-turn interaction, dropping from 60.52% to 11.90%](informational-harm-drops-multi-turn.md) — related
