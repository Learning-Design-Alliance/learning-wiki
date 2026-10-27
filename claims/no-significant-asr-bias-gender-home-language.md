---
type: claim
title: No statistically significant evidence that the model scores Ghanaian students differently by gender or home language relative to human raters
description: No statistically significant evidence that the model scores Ghanaian students differently by gender or home language relative to human raters
id: no-significant-asr-bias-gender-home-language
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: henkel-2025
    resource: "https://doi.org/10.1007/s40593-024-00435-9"
    title: "Henkel, O., Horne-Robinson, H., Hills, L., Roberts, B., & McGrane, J. (2025). Supporting Literacy Assessment in West Africa: Using State-of-the-Art Speech Models to Assess Oral Reading Fluency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00435-9"
    author: "Henkel, O., Horne-Robinson, H., Hills, L., Roberts, B., & McGrane, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# No statistically significant evidence that the model scores Ghanaian students differently by gender or home language relative to human raters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Differences between model and human estimates of WER and WCPM across gender and native-language groups were substantially less than one standard deviation; the null hypothesis of systematic group differences could not be rejected. [→ Henkel 2025](#henkel-2025)

## Evidence

### Henkel 2025

Henkel, O., Horne-Robinson, H., Hills, L., Roberts, B., & McGrane, J. (2025). Supporting Literacy Assessment in West Africa: Using State-of-the-Art Speech Models to Assess Oral Reading Fluency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00435-9

`q2 · i?` · `design · r2`

Bias analysis comparing model vs human score differences by gender (male|female WER difference 0.05|0.03; WCPM 5.9|4.2) and home language (English|other WER 0.05|0.06; WCPM 5.6|4.7), Table 7. Bias was operationalized as a higher model error rate relative to human raters for specific demographic groups.

> "the difference between group averages of model estimates and human estimates is substantially less than one standard deviation. This indicates that we cannot reject the null hypothesis"

## Discussion


## Related Claims
- [Fully automated WCPM scores from Whisper V2 transcriptions closely align with expert human raters (correlation 0.98, average difference 4.82 WCPM)](automated-wcpm-correlates-098-human-raters.md) — related
- [Interaction effects between student background variables (BOOKS, LANG, GENDER) and outcomes were statistically insignificant in both achievement and confidence models](background-interactions-insignificant.md) — related
