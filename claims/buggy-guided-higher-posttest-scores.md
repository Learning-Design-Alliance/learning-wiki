---
type: claim
title: Buggy and Guided interactive worked examples produced significantly higher posttest problem scores than passive worked examples in logic tutoring
description: Buggy and Guided interactive worked examples produced significantly higher posttest problem scores than passive worked examples in logic tutoring
id: buggy-guided-higher-posttest-scores
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: sutapa-dey-tithi-2026
    resource: "https://doi.org/10.1145/3772318.3791631"
    title: Sutapa Dey Tithi 2026
    q: 3
    i: 1
    kind: causal
    rigour: 2
  - id: sutapa-dey-tithi-2026-2
    resource: "https://doi.org/10.1145/3772318.3791631"
    title: Sutapa Dey Tithi 2026 (2)
    q: 3
    i: "?"
    kind: causal
    rigour: "?"
---

# Buggy and Guided interactive worked examples produced significantly higher posttest problem scores than passive worked examples in logic tutoring

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i1` small
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i1` Both the Buggy and Guided groups scored significantly higher on posttest problems than the Control group (probability-based effect size A = 0.56 and A = 0.57). [→ Sutapa Dey Tithi 2026](#sutapa-dey-tithi-2026)
`q3 i?` Mixed-effects regression confirmed higher posttest scores for Buggy (β = 4.44) and Guided (β = 4.56) relative to Control. [→ Sutapa Dey Tithi 2026 (2)](#sutapa-dey-tithi-2026-2)

## Evidence

### Sutapa Dey Tithi 2026

Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). [doi:10.1145/3772318.3791631](https://doi.org/10.1145/3772318.3791631)

`q3 · i1` · `causal · r2`

Post hoc Mann-Whitney U tests with Bonferroni correction compared posttest problem scores across the three training conditions of the controlled between-subjects study (155 undergraduates). Buggy (mean 72.3) and Guided (mean 72.4) beat Control (mean 67.8), with printed probability-based effect size A = 0.56 (p = .009) and A = 0.57 (p = .004).

> "The𝐵𝑢𝑔𝑔𝑦 group showed a significant improvement (𝑚𝑒𝑎𝑛= 72.3,𝐴= 0.56, 95% CI [.52, .61],𝑝=. 009). Similarly, the 𝐺𝑢𝑖𝑑𝑒𝑑 group also demonstrated a significant improvement (𝑚𝑒𝑎𝑛= 72.4,𝐴= 0.57, 95% CI [.52, .61],𝑝=. 004)"

### Sutapa Dey Tithi 2026 (2)

Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). [doi:10.1145/3772318.3791631](https://doi.org/10.1145/3772318.3791631)

`q3 · i?` · `causal · r?`

Mixed-effects regression on all posttest problems, with problem ID as random effect and treatment as fixed effect, confirmed the score advantage: "𝛽= 4.44,𝑆𝐸= 1.71,𝑧= 2.60,𝑝=. 009" for Buggy and β = 4.56 (p = .007) for Guided versus Control. These are unstandardized coefficients, not effect sizes.

> "Compared to the 𝐶𝑜𝑛𝑡𝑟𝑜𝑙 condition (𝑚𝑒𝑎𝑛= 67.82,𝑆𝐸= 3.32), participants in the 𝐵𝑢𝑔𝑔𝑦 condition scored significantly higher (𝛽= 4.44,𝑆𝐸= 1.71,𝑧= 2.60,𝑝=. 009), as did participants in the 𝐺𝑢𝑖𝑑𝑒𝑑 condition (𝛽= 4.56,𝑆𝐸= 1.70,𝑧= 2.68,𝑝=. 007)"

## Discussion


## Related Claims
- [Worked example type interacted with prior knowledge: Guided examples benefited low prior knowledge students while Buggy examples benefited high prior knowledge students](ati-buggy-high-guided-low-prior-knowledge.md) — related
- [Both Buggy and Guided training reduced posttest problem completion time relative to Control in the logic tutor](interactive-we-reduced-posttest-time.md) — related
- [Markov transition analysis of tutor logs showed Buggy examples produced error-loop struggle patterns while Guided examples redirected errors toward hint-seeking](markov-behavior-patterns-logic-tutor.md) — related
- [The DRL policy produced a significantly different scaffolding distribution than Control and BKT, favoring Guided examples (60%) and avoiding Buggy examples (4%)](drl-policy-favors-guided-examples-distribution.md) — related
- [Guided examples improved posttest rule application accuracy over Control while Buggy accuracy did not differ significantly after correction](guided-rule-accuracy-gain-buggy-null.md) — related
- [Training with Buggy or Guided examples did not significantly change posttest solution length](no-solution-length-difference-logic-tutor.md) — related
