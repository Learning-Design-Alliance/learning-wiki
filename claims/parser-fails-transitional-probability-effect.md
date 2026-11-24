---
type: claim
title: PARSER failed to reproduce the human advantage for higher-transitional-probability words, revealing an inability to abstract statistical regularities
description: PARSER failed to reproduce the human advantage for higher-transitional-probability words, revealing an inability to abstract statistical regularities
id: parser-fails-transitional-probability-effect
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-24
evidence_strength: mixed
newest_evidence: 1998
recheck_by: 2001
sources:
  - id: perruchet-1998
    resource: "https://doi.org/10.1006/jmla.1998.2576"
    title: "Perruchet, P., & Vinter, A. (1998). PARSER: A Model for Word Segmentation. Journal of Memory and Language, 39, 246-263. https://doi.org/10.1006/jmla.1998.2576"
    author: "Perruchet, P., & Vinter, A."
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# PARSER failed to reproduce the human advantage for higher-transitional-probability words, revealing an inability to abstract statistical regularities

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 1998 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2001**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Only the single word with the highest transitional probability (dutaba) was learned significantly better (F(1,99) = 22.45, p < .0001); the two-set contrast computed by Saffran et al. was not significant in the model (F < 1). [→ Perruchet 1998](#perruchet-1998)

## Evidence

### Perruchet 1998

Perruchet, P., & Vinter, A. (1998). PARSER: A Model for Word Segmentation. Journal of Memory and Language, 39, 246-263. https://doi.org/10.1006/jmla.1998.2576

`q2 · i?` · `theoretical · r3`

Simulation analysis in Study 1 using word weights after 9000 syllables as the learning index. Saffran et al. had found 79% vs 72% correct for high versus low transitional-probability words; PARSER reproduced only the dutaba advantage, with "not significant (F , 1)" for the set contrast.

> "However, the scores for the other words were unrelated to their mean transitional probabilities, and the contrast between the two sets of three words as computed by Saffran et al. was not significant (F , 1)."

## Discussion


## Related Claims
- [A chunking-based computational model extracts the words of an artificial language before exhausting the training material presented to human participants](parser-extracts-words-before-training-material-exhausted.md) — related
- [After processing the same 540 syllables as 8-month-old infants, PARSER had extracted a high proportion of the test words and none of the boundary-crossing nonwords](parser-reproduces-infant-segmentation-540-syllables.md) — related
- [PARSER's segmentation performance extends to a language composed of one- to five-syllable words, with no detrimental effect of varied word length](parser-generalizes-to-varied-word-lengths.md) — related
- [PARSER matches adult and child incidental-learning segmentation scores while processing only about 3-5% of the training material](parser-simulates-incidental-learning-with-fragmentary-input.md) — related
