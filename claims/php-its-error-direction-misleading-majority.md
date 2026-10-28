---
type: claim
title: "81.54% of incorrectly analysed programs were incorrect programs analysed as correct"
description: "81.54% of incorrectly analysed programs were incorrect programs analysed as correct"
id: php-its-error-direction-misleading-majority
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2014
sources:
  - id: weragama-2014
    resource: "https://doi.org/10.1007/s40593-014-0014-z"
    title: "Weragama, D. & Reye, J. (2014). Analysing Student Programs in the PHP Intelligent Tutoring System. Int J Artif Intell Educ 24:162–188. https://doi.org/10.1007/s40593-014-0014-z"
    author: "Weragama, D. & Reye, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# 81.54% of incorrectly analysed programs were incorrect programs analysed as correct

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Most incorrect analyses involved false positives (incorrect programs judged correct) rather than false negatives. [→ Weragama 2014](#weragama-2014)

## Evidence

### Weragama 2014

Weragama, D. & Reye, J. (2014). Analysing Student Programs in the PHP Intelligent Tutoring System. Int J Artif Intell Educ 24:162–188. https://doi.org/10.1007/s40593-014-0014-z

`q2 · i?` · `design · r2`

Further investigation of the nature of incorrect analyses in the evaluation data. "81.54 % of the incorrectly analysed programs were incorrect programs being analysed as correct."

> "The results showed that 81.54 % of the incorrectly analysed programs were incorrect programs being analysed as correct."

## Discussion


## Related Claims
- [The final PHP ITS version correctly analysed 96.31% of student solutions to programming exercises](php-its-96-percent-analysis-accuracy.md) — related
- [LLM-based scoring produced fewer false negatives than Deep Tutor on a balanced test set, which the authors expect would spare students the frustration of correct explanations judged incorrect](llm-scoring-fewer-false-negatives-than-deep-tutor.md) — related
- [Validator false-negative cases reveal structural reasoning weaknesses, including answer-schema misinterpretation and internal inconsistency](code-gen-validator-fn-reasoning-weaknesses.md) — related
- [No consistent relationship was observed between false-positive and false-negative rates and either the question or the LLM model](no-consistent-fp-fn-pattern.md) — related
