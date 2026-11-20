---
type: claim
title: Unsupervised clustering on realistic speech converges on short context-sensitive acoustic clusters rather than phonemes
description: Unsupervised clustering on realistic speech converges on short context-sensitive acoustic clusters rather than phonemes
id: clustering-speech-converges-acoustic-clusters-not-phonemes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: moderate
newest_evidence: 2018
sources:
  - id: dupoux-2018
    resource: "https://doi.org/10.1016/j.cognition.2017.11.008"
    title: "Dupoux, E. (2018). Cognitive science in the era of artificial intelligence: A roadmap for reverse-engineering the infant language-learner. Cognition, 173, 43-59. https://doi.org/10.1016/j.cognition.2017.11.008"
    author: Dupoux, E.
    q: 2
    i: "?"
    kind: theoretical
    rigour: 2
---

# Unsupervised clustering on realistic speech converges on short context-sensitive acoustic clusters rather than phonemes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A clustering algorithm based on HMMs and Gaussian mixtures run on continuous audio representations does not converge on phonetic segments but on much shorter (30 ms), highly context-sensitive acoustic clusters. [→ Dupoux 2018](#dupoux-2018)

## Evidence

### Dupoux 2018

Dupoux, E. (2018). Cognitive science in the era of artificial intelligence: A roadmap for reverse-engineering the infant language-learner. Cognition, 173, 43-59. https://doi.org/10.1016/j.cognition.2017.11.008

`q2 · i?` · `theoretical · r2`

Numerical result reported by the article from unsupervised clustering run on continuous, large, variable, high-dimensional audio representations, showing the distributional learning hypothesis alone cannot recover phonetic units. No effect size is printed.

> "Varadarajan, Khudanpur, and Dupoux (2008) have shown that a clustering algorithm based on Hidden Markov Models and Gaussian mixtures does not converge on pho- netic segments, but rather, on much shorter (30 ms), highly context-sensitive acoustic clusters"

## Discussion


## Related Claims
- [Off-the-shelf speech models preserve and correct reading errors differently: wav2vec 2.0 preserves errors phonetically, Whisper V2 often corrects them](asr-models-differ-in-preserving-reading-errors.md) — related
- [Word segmentation algorithms that succeed on phoneme transcriptions fail on speech signals](word-segmentation-fails-on-speech-signals.md) — related
- [Unsupervised clustering of individual learning curves identifies seven distinct learner profiles whose proportions shift with target geometry](seven-learner-profiles-soft-dtw-clustering.md) — related
- [Type 2 groups showed a communication–behaviour-synergistic transition, Type 1 a behaviour-oriented, and Type 3 a communication-oriented transition in hidden Markov models](hmm-transitional-regularities-pattern-types.md) — related
- [Bottom-up models trained on context-free acoustic input do not distinguish phonemes from allophones](allophony-not-captured-bottom-up.md) — related
