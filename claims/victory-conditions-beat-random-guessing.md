---
type: claim
title: Victory conditions compare AI and human prediction quality against each other and against random guessing, requiring both to significantly beat chance
description: Victory conditions compare AI and human prediction quality against each other and against random guessing, requiring both to significantly beat chance
id: victory-conditions-beat-random-guessing
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: shashank-sonkar-2025
    resource: "https://doi.org/10.48550/arXiv.2502.15127"
    title: "Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk. (2025). The Imitation Game for Educational AI. arXiv preprint. [doi:10.48550/arXiv.2502.15127](https://doi.org/10.48550/arXiv.2502.15127)"
    author: Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
---

# Victory conditions compare AI and human prediction quality against each other and against random guessing, requiring both to significantly beat chance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` The formal comparison declares AI win, human win, or draw based on the difference in prediction rates with confidence 1−α, and the comparison is valid only when both AI and human prediction rates exceed the random selection probability of 1/4 by at least δ. [→ Shashank Sonkar 2025](#shashank-sonkar-2025)

## Evidence

### Shashank Sonkar 2025

Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk. (2025). The Imitation Game for Educational AI. arXiv preprint. [doi:10.48550/arXiv.2502.15127](https://doi.org/10.48550/arXiv.2502.15127)

`q1 · i?` · `theoretical · r2`

Analytical framework (Theorem 4 and Definition 3): equivalence requires |pAI − pHuman| ≤ ε, both sources must exceed random guessing, and a Z-diff statistic based on McNemar's test decides AI win, human win, or draw. The article derives required sample sizes n1 and n2 for a chosen margin ε and level α.

> "Critically, this test is only valid when both systems outperform random guessing: min(pAI, pHuman) > pRandom + δ (16) This ensures we're comparing meaningful prediction strategies rather than random noise."

## Discussion


## Related Claims
- [Random forest and support vector machine models also failed to beat chance when predicting laboratory performance, supporting the null result](rf-svm-also-fail-beat-chance-lab-performance.md) — related
- [Graduate graders can distinguish LLM-generated assessment responses from student responses with accuracy better than random guessing, and experience with generative AI improves detection accuracy](graders-detect-llm-responses-neuroscience.md) — related
- [Human markers identified AI versus human authorship only marginally better than random chance](human-judgment-ai-authorship-near-chance.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [Physics instructors and graduate TAs perform better than random guessing at identifying introductory students' most common incorrect FCI answers, but both average only about two-thirds of the maximum possible PCK score](instructors-tas-above-chance-fci-pck.md) — related
