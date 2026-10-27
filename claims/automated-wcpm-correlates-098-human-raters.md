---
type: claim
title: Fully automated WCPM scores from Whisper V2 transcriptions closely align with expert human raters (correlation 0.98, average difference 4.82 WCPM)
description: Fully automated WCPM scores from Whisper V2 transcriptions closely align with expert human raters (correlation 0.98, average difference 4.82 WCPM)
id: automated-wcpm-correlates-098-human-raters
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
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
  - id: henkel-2025-2
    resource: "https://doi.org/10.1007/s40593-024-00435-9"
    title: "Henkel, O., Horne-Robinson, H., Hills, L., Roberts, B., & McGrane, J. (2025). Supporting Literacy Assessment in West Africa: Using State-of-the-Art Speech Models to Assess Oral Reading Fluency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00435-9"
    author: "Henkel, O., Horne-Robinson, H., Hills, L., Roberts, B., & McGrane, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fully automated WCPM scores from Whisper V2 transcriptions closely align with expert human raters (correlation 0.98, average difference 4.82 WCPM)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On 165 Ghana ORF assessments including noisier recordings and weaker readers, automated WCPM scores correlated 0.98 with expert human scores, with humans slightly stricter (average difference 4.82 WCPM). [→ Henkel 2025](#henkel-2025)
`q2 i?` Per-file human and model error estimates were strongly correlated (correlation coefficient 0.79), indicating broadly similar but not identical transcriptions. [→ Henkel 2025 (2)](#henkel-2025-2)

## Evidence

### Henkel 2025

Henkel, O., Horne-Robinson, H., Hills, L., Roberts, B., & McGrane, J. (2025). Supporting Literacy Assessment in West Africa: Using State-of-the-Art Speech Models to Assess Oral Reading Fluency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00435-9

`q2 · i?` · `design · r2`

Experiment 3 computed WCPM from Whisper V2 transcripts and from expert human transcriptions for 165 ORF assessments (the original 60 plus 95 more, including more background noise and weaker readers). Human raters averaged 91.7 WCPM vs 93.5 automated (Table 6).

> "Further, automated scores and the expert human scores were highly correlated (0.98) high, suggesting that the same students were receiving similar scores relative to one another"

### Henkel 2025 (2)

Henkel, O., Horne-Robinson, H., Hills, L., Roberts, B., & McGrane, J. (2025). Supporting Literacy Assessment in West Africa: Using State-of-the-Art Speech Models to Assess Oral Reading Fluency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00435-9

`q2 · i?` · `design · r2`

Aggregate error-estimate comparison on the same 165 recordings (Table 5): human average WER 0.14 vs model 0.12, average difference per item 0.05, correlation coefficient 0.79.

> "Additionally, the WER results between human and model transcriptions are strongly correlated. We take these results as an indication that Whisper V2 is producing broadly similar but not identical transcriptions"

## Discussion


## Related Claims
- [Off-the-shelf speech models preserve and correct reading errors differently: wav2vec 2.0 preserves errors phonetically, Whisper V2 often corrects them](asr-models-differ-in-preserving-reading-errors.md) — related
- [The automated scoring system's agreement with human raters varied widely by dimension, with information fidelity showing a weak, non-significant correlation](yunyi-human-agreement-varies-by-dimension.md) — related
- [No statistically significant evidence that the model scores Ghanaian students differently by gender or home language relative to human raters](no-significant-asr-bias-gender-home-language.md) — related
