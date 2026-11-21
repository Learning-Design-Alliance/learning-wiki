---
type: claim
title: Guided examples improved posttest rule application accuracy over Control while Buggy accuracy did not differ significantly after correction
description: Guided examples improved posttest rule application accuracy over Control while Buggy accuracy did not differ significantly after correction
id: guided-rule-accuracy-gain-buggy-null
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

# Guided examples improved posttest rule application accuracy over Control while Buggy accuracy did not differ significantly after correction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i1` small
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i1` Guided students achieved significantly higher posttest rule application accuracy than Control students (probability-based effect size A = .58). [→ Sutapa Dey Tithi 2026](#sutapa-dey-tithi-2026)
`q3 i?` Rule application accuracy was not significantly different between Buggy and Control at the corrected threshold. [→ Sutapa Dey Tithi 2026 (2)](#sutapa-dey-tithi-2026-2)

## Evidence

### Sutapa Dey Tithi 2026

Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). [doi:10.1145/3772318.3791631](https://doi.org/10.1145/3772318.3791631)

`q3 · i1` · `causal · r2`

Mann-Whitney U tests on the rule application accuracy metric (correct rule applications divided by total attempts) in the 155-student between-subjects experiment: "𝐺𝑢𝑖𝑑𝑒𝑑 (mean) = 79.3,𝐶𝑜𝑛𝑡𝑟𝑜𝑙 (mean) = 73.2,𝑝 = 0.001" with printed probability-based effect size A = .58.

> "𝐺𝑢𝑖𝑑𝑒𝑑 students achieved significantly higher rule application accuracy than𝐶𝑜𝑛𝑡𝑟𝑜𝑙 in posttest problems (𝐺𝑢𝑖𝑑𝑒𝑑 (mean) = 79.3,𝐶𝑜𝑛𝑡𝑟𝑜𝑙 (mean) = 73.2,𝑝 = 0.001,𝐴=. 58, 95% CI [.53, .62])"

### Sutapa Dey Tithi 2026 (2)

Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). [doi:10.1145/3772318.3791631](https://doi.org/10.1145/3772318.3791631)

`q3 · i?` · `causal · r?`

Same posttest accuracy analysis: the Buggy-Control contrast ("𝐵𝑢𝑔𝑔𝑦(mean) = 76.8,𝐶𝑜𝑛𝑡𝑟𝑜𝑙(mean) = 73.2,𝑝= 0.04") did not pass the Bonferroni-corrected threshold; equivalence was not tested.

> "The rule application accuracy was not significantly different between𝐵𝑢𝑔𝑔𝑦 and𝐶𝑜𝑛𝑡𝑟𝑜𝑙in posttest problems (𝐵𝑢𝑔𝑔𝑦(mean) = 76.8,𝐶𝑜𝑛𝑡𝑟𝑜𝑙(mean) = 73.2,𝑝= 0.04,𝐴=.55, 95% CI [.50, .60])"

## Discussion


## Related Claims
- [Worked example type interacted with prior knowledge: Guided examples benefited low prior knowledge students while Buggy examples benefited high prior knowledge students](ati-buggy-high-guided-low-prior-knowledge.md) — related
- [Buggy and Guided interactive worked examples produced significantly higher posttest problem scores than passive worked examples in logic tutoring](buggy-guided-higher-posttest-scores.md) — related
- [Markov transition analysis of tutor logs showed Buggy examples produced error-loop struggle patterns while Guided examples redirected errors toward hint-seeking](markov-behavior-patterns-logic-tutor.md) — related
- [Both Buggy and Guided training reduced posttest problem completion time relative to Control in the logic tutor](interactive-we-reduced-posttest-time.md) — related
- [Training with Buggy or Guided examples did not significantly change posttest solution length](no-solution-length-difference-logic-tutor.md) — related
