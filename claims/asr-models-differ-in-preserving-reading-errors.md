---
type: claim
title: "Off-the-shelf speech models preserve and correct reading errors differently: wav2vec 2.0 preserves errors phonetically, Whisper V2 often corrects them"
description: "Off-the-shelf speech models preserve and correct reading errors differently: wav2vec 2.0 preserves errors phonetically, Whisper V2 often corrects them"
id: asr-models-differ-in-preserving-reading-errors
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
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Off-the-shelf speech models preserve and correct reading errors differently: wav2vec 2.0 preserves errors phonetically, Whisper V2 often corrects them

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Qualitative transcript comparison found wav2vec 2.0 preserves reading errors more faithfully and transcribes some words phonetically, whereas Whisper V2 more often corrects repetitions and reading errors. [→ Henkel 2025](#henkel-2025)

## Evidence

### Henkel 2025

Henkel, O., Horne-Robinson, H., Hills, L., Roberts, B., & McGrane, J. (2025). Supporting Literacy Assessment in West Africa: Using State-of-the-Art Speech Models to Assess Oral Reading Fluency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00435-9

`q1 · i?` · `design · r2`

Manual inspection of model transcripts of the same audio clips in Experiment 1 (Fig. 2). The authors attribute the difference to training approaches: wav2vec 2.0's unsupervised training is more sensitive to acoustics, while Whisper V2's lightly supervised transcript-audio pairs often omit repeated words and verbal stumbles.

> "Qualitatively, wav2vec 2.0 appears to preserve reading errors more faithfully (e.g., "he locked, he looked", "had head headed"), whereas Whisper V2 more often corrects repetitions and reading errors."

## Discussion


## Related Claims
- [Fully automated WCPM scores from Whisper V2 transcriptions closely align with expert human raters (correlation 0.98, average difference 4.82 WCPM)](automated-wcpm-correlates-098-human-raters.md) — related
