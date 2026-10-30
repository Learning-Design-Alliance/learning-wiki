---
type: claim
title: Human and GPT-2-generated replies differed significantly overall and in informational support, but not in emotional or community support
description: Human and GPT-2-generated replies differed significantly overall and in informational support, but not in emotional or community support
id: human-vs-gpt2-support-types-manova
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: chenglu-li-wanli-xing-2021
    resource: "https://doi.org/10.1007/s40593-020-00235-x"
    title: "Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x"
    author: "Chenglu Li & Wanli Xing"
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: chenglu-li-wanli-xing-2021-2
    resource: "https://doi.org/10.1007/s40593-020-00235-x"
    title: "Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x"
    author: "Chenglu Li & Wanli Xing"
    q: 2
    i: 2
    kind: design
    rigour: 2
---

# Human and GPT-2-generated replies differed significantly overall and in informational support, but not in emotional or community support

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i2` medium
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A MANOVA found a significant multivariate effect between original and generated replies (Λ = 0.95, F(3, 296) = 4.85, p < 0.01), though only 5% of variance was explained. [→ Chenglu Li & Wanli Xing 2021](#chenglu-li-wanli-xing-2021)
`q2 i2` Original replies provided significantly more informational support than generated replies (η² = 0.04, F(1, 298) = 11.725, p < 0.001); emotional and community support showed no significant differences. [→ Chenglu Li & Wanli Xing 2021 (2)](#chenglu-li-wanli-xing-2021-2)

## Evidence

### Chenglu Li & Wanli Xing 2021

Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x

`q2 · i?` · `design · r2`

MANOVA on 150 original and 150 generated replies coded for three support types (sample size set by a G*Power analysis requiring 120 for power 0.95). The article notes "the Wilk 's Λ of 0.95 suggests only 5% of the variance can be explained"; no standardised effect size is printed for the omnibus test.

> "In terms of the MANOVA test, a significant multivariate effect in supporting MOOC learners was found between original replies and generated replies, Λ =0 . 9 5 ,F(3, 296) = 4.85, p < 0.01."

### Chenglu Li & Wanli Xing 2021 (2)

Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x

`q2 · i2` · `design · r2`

Follow-up ANOVA on the same coded replies: 42.85% of original versus 26.43% of generated replies were supportive (moderate or strong) for informational support, with printed effect size η² = 0.04. The article states "The follow-up ANOVA tests do not find any significant differences in emotional and community support".

> "However, there was a significant difference in informational support between original replies and generated replies, η2 = 0.04, F(1, 298) = 11.725, p < 0.001."

## Discussion


## Related Claims
- [The special issue reports that a GPT-2 model could provide supportive and contextual replies to MOOC learners to a similar extent as humans](gpt2-mooc-forum-replies-similar-to-humans.md) — reports the opposite
- [A small validation survey found the trained GPT-2 model generated supportive, contextual replies comparable to humans and generalizable to a new similar MOOC](gpt2-survey-validation-generalizable.md) — related
- [Multivariate analysis confirmed a significant overall group effect, and all outcome variables correlated positively in both groups](ai-ibi-multivariate-group-effect-positive-correlations.md) — a broader claim this one bears on
