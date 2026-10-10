---
type: claim
title: A deterministic slide-image override converts a 0/9 corpus-grounding failure into 9/10 successful slide matches on the same topic
description: A deterministic slide-image override converts a 0/9 corpus-grounding failure into 9/10 successful slide matches on the same topic
id: slide-image-override-corpus-grounding-recovery
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: md-zabirul-islam-2026
    resource: "https://arxiv.org/abs/2606.20608"
    title: "Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608"
    author: Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A deterministic slide-image override converts a 0/9 corpus-grounding failure into 9/10 successful slide matches on the same topic

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Replacing a prompt-marker strategy with a slide-hints map that mutates layout JSON before the designer's image-generation pass resolved 9 of 10 corpus-eligible slides on the filtered-back-projection topic, versus 0 of 9 for the marker path. [→ Md Zabirul Islam 2026](#md-zabirul-islam-2026)

## Evidence

### Md Zabirul Islam 2026

Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608

`q2 · i?` · `design · r2`

Systems comparison reported in the results section on one topic (filtered back projection): the marker-based path, in which the slide designer silently drops a [CORPUS:·] token, resolved 0 of 9 slides; the deterministic override resolved 9 of 10. No effect size is printed.

> "On the filtered-back-projection topic, that path resolved 0 of 9 corpus-eligible slides. Replacing it with the slide-hints map resolved 9 of 10 slides on the same topic."

## Discussion


## Related Claims
- [The greedy cycle-break algorithm functions as a safety mechanism: none of the five evaluation topics required prerequisite-edge removal](cycle-break-safety-mechanism-concept-graphs.md) — related
- [Domain-matched experts judged 87% of Bespoke-generated lecture videos at or above the rubric midpoint corresponding to a standard MOOC lecture's quality (mean G = 3.42 of 5)](bespoke-87-percent-mooc-comparable-quality.md) — related
- [Reviewer free-text comments identified synthetic voice, slide–narration reveal timing, and slide layout as the main remaining quality issues](bespoke-free-text-voice-reveal-layout-issues.md) — related
- [Automated CTML metrics show significant improvement in temporal contiguity and coherence for CTML-informed videos, while modality, redundancy, and image quality show no significant difference](automated-metrics-temporal-contiguity-coherence.md) — related
