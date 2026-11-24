---
type: product
id: parser
title: PARSER
description: "PARSER is Perruchet et al.'s computer model implementing chunking-based word segmentation through a percept-shaper memory store for studying artificial-language learning."
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-24
---

# PARSER

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
PARSER is Perruchet et al.'s computer model implementing chunking-based word segmentation through a percept-shaper memory store for studying artificial-language learning.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **PARSER computer model with its percept shaper memory store**: PARSER is a computer program implementing the chunking account of word segmentation. "PARSER is centered around a single vector, called percept shaper (PS). PS is composed of the internal representations of the displayed material and may be thought of as a memory store or a mental lexicon." Each element carries a familiarity weight; new percepts are created as units, weights are incremented on reuse and decremented by forgetting (0.05) and interference (0.005), and units above a threshold of 1 shape subsequent perception. Key parameters were a starting weight of 1 and an increment of 0.5. (Perruchet et al. (1998))

### Claims
- [A chunking-based computational model extracts the words of an artificial language before exhausting the training material presented to human participants](../claims/parser-extracts-words-before-training-material-exhausted.md) [+M]
- [PARSER matches adult and child incidental-learning segmentation scores while processing only about 3-5% of the training material](../claims/parser-simulates-incidental-learning-with-fragmentary-input.md) [+M]
- [After processing the same 540 syllables as 8-month-old infants, PARSER had extracted a high proportion of the test words and none of the boundary-crossing nonwords](../claims/parser-reproduces-infant-segmentation-540-syllables.md) [+M]
- [PARSER's segmentation performance extends to a language composed of one- to five-syllable words, with no detrimental effect of varied word length](../claims/parser-generalizes-to-varied-word-lengths.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Perruchet, P., & Vinter, A. (1998). PARSER: A Model for Word Segmentation. Journal of Memory and Language, 39, 246-263. https://doi.org/10.1006/jmla.1998.2576
