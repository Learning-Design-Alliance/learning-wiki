---
type: claim
title: "Worked example type interacted with prior knowledge: Guided examples benefited low prior knowledge students while Buggy examples benefited high prior knowledge students"
description: "Worked example type interacted with prior knowledge: Guided examples benefited low prior knowledge students while Buggy examples benefited high prior knowledge students"
id: ati-buggy-high-guided-low-prior-knowledge
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
    i: 2
    kind: causal
    rigour: 2
  - id: sutapa-dey-tithi-2026-3
    resource: "https://doi.org/10.1145/3772318.3791631"
    title: Sutapa Dey Tithi 2026 (3)
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Worked example type interacted with prior knowledge: Guided examples benefited low prior knowledge students while Buggy examples benefited high prior knowledge students

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q3` · `i1`–`i2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i1` Low prior knowledge students in the Guided group achieved significantly higher posttest rule accuracy than Control (probability-based effect size A = .59). [→ Sutapa Dey Tithi 2026](#sutapa-dey-tithi-2026)
`q3 i2` High prior knowledge students in the Buggy group achieved significantly higher posttest rule accuracy than Control (probability-based effect size A = .62). [→ Sutapa Dey Tithi 2026 (2)](#sutapa-dey-tithi-2026-2)
`q3 i?` Mixed-effects regression confirmed a significant aptitude-treatment interaction for rule accuracy (Buggy high-PK β = 8.94, p = .023). [→ Sutapa Dey Tithi 2026 (3)](#sutapa-dey-tithi-2026-3)

## Evidence

### Sutapa Dey Tithi 2026

Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). [doi:10.1145/3772318.3791631](https://doi.org/10.1145/3772318.3791631)

`q3 · i1` · `causal · r2`

Prior knowledge groups were formed by a median split on pretest score and compared with Bonferroni-corrected Mann-Whitney U tests: "𝐺𝑢𝑖𝑑𝑒𝑑 (mean) = 78.7,𝐶𝑜𝑛𝑡𝑟𝑜𝑙 (mean) = 71.8,𝑝 = 0.013" with printed probability-based effect size A = .59 for low prior knowledge students.

> "the 𝐺𝑢𝑖𝑑𝑒𝑑 group achieved significantly improved rule accuracy for low prior knowledge students at posttest problems (𝐺𝑢𝑖𝑑𝑒𝑑 (mean) = 78.7,𝐶𝑜𝑛𝑡𝑟𝑜𝑙 (mean) = 71.8,𝑝 = 0.013,𝐴=. 59, 95% CI [.52, .65])"

### Sutapa Dey Tithi 2026 (2)

Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). [doi:10.1145/3772318.3791631](https://doi.org/10.1145/3772318.3791631)

`q3 · i2` · `causal · r2`

Same median-split posttest comparison for the Buggy condition: "𝐵𝑢𝑔𝑔𝑦 (mean) = 82.6,𝐶𝑜𝑛𝑡𝑟𝑜𝑙 (mean) = 74.4,𝑝 = 0.0004" with printed probability-based effect size A = .62 for high prior knowledge students.

> "the high prior knowledge students in group𝐵𝑢𝑔𝑔𝑦 achieved significantly higher rule application accuracy than their counterparts in the𝐶𝑜𝑛𝑡𝑟𝑜𝑙 group in the posttest problems (𝐵𝑢𝑔𝑔𝑦 (mean) = 82.6,𝐶𝑜𝑛𝑡𝑟𝑜𝑙 (mean) = 74.4,𝑝 = 0.0004,𝐴=. 62, 95% CI [.55, .68])"

### Sutapa Dey Tithi 2026 (3)

Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). [doi:10.1145/3772318.3791631](https://doi.org/10.1145/3772318.3791631)

`q3 · i?` · `causal · r2`

Mixed-effects regression with Treatment and Prior Knowledge as fixed effects and student ID as random effect confirmed differential effects; "𝛽= 8.94,𝑆𝐸= 3.93,𝑧= 2.3,𝑝=. 023" for Buggy among high prior knowledge students. The β is unstandardized, not an effect size.

> "high prior knowledge students benefited significantly from 𝐵𝑢𝑔𝑔𝑦 examples (𝛽= 8.94,𝑆𝐸= 3.93,𝑧= 2.3,𝑝=. 023) compared to𝐶𝑜𝑛𝑡𝑟𝑜𝑙 (𝑚𝑒𝑎𝑛= 74.4), implying a significant aptitude-treatment interaction"

## Discussion


## Learner Variables
- [Prior Knowledge](../learner-variables/prior-knowledge.md) — moderator: an instructional effect differs with it

## Related Claims
- [Guided examples improved posttest rule application accuracy over Control while Buggy accuracy did not differ significantly after correction](guided-rule-accuracy-gain-buggy-null.md) — related
- [Buggy and Guided interactive worked examples produced significantly higher posttest problem scores than passive worked examples in logic tutoring](buggy-guided-higher-posttest-scores.md) — related
- [DRL scaffolding significantly benefits high prior knowledge students while BKT does not, and condition-by-prior-knowledge interactions are not significant](drl-benefits-high-prior-knowledge-students.md) — related
