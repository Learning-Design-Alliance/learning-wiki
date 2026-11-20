---
type: claim
title: Bottom-up models trained on context-free acoustic input do not distinguish phonemes from allophones
description: Bottom-up models trained on context-free acoustic input do not distinguish phonemes from allophones
id: allophony-not-captured-bottom-up
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: frank-lihui-tan-youngah-do-2024
    resource: "https://doi.org/10.48550/arXiv.2407.18501"
    title: "Frank Lihui Tan & Youngah Do. (2024). The formation of perceptual space in early phonetic acquisition: a cross-linguistic modeling approach. Originally published 2023. [doi:10.48550/arXiv.2407.18501](https://doi.org/10.48550/arXiv.2407.18501)"
    author: "Frank Lihui Tan & Youngah Do"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Bottom-up models trained on context-free acoustic input do not distinguish phonemes from allophones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Pairwise ABX error rates among vowel phonemes are not significantly different from pairwise error rates among allophones (p = 0.371), so the model fails to capture allophony. [→ Frank Lihui Tan & Youngah Do 2024](#frank-lihui-tan-youngah-do-2024)

## Evidence

### Frank Lihui Tan & Youngah Do 2024

Frank Lihui Tan & Youngah Do. (2024). The formation of perceptual space in early phonetic acquisition: a cross-linguistic modeling approach. Originally published 2023. [doi:10.48550/arXiv.2407.18501](https://doi.org/10.48550/arXiv.2407.18501)

`q2 · i?` · `design · r2`

ABX comparison of the three Mandarin allophones of /i/ (i, ɹ̩, ɻ̩) against vowel phonemes: phoneme mean 0.15 vs allophone 0.182, p = 0.371. The three allophones were themselves well separated (silhouettes up to 0.45), but the model showed no phoneme/allophone sensitivity.

> "the pairwise error rate among vowel phonemes are not significantly different from the pairwise error rate among allophones ( 𝜇𝑉 =  0.15, 𝜎𝑉 = 0.146; 𝜇𝐴 =  0.182, 𝜎𝐴 =  0.084;  𝑝 =  0.371);"

## Discussion


## Related Claims
- [On the general ABX test over all phone pairs, models discriminate exposed-language phones significantly better than foreign-language phones](general-abx-exposed-better-than-foreign.md) — related
- [Autoencoders trained on context-free acoustic input develop phone clustering well above chance in both native and foreign evaluation conditions](autoencoder-clustering-above-baseline-both-languages.md) — related
- [Unsupervised clustering on realistic speech converges on short context-sensitive acoustic clusters rather than phonemes](clustering-speech-converges-acoustic-clusters-not-phonemes.md) — related
- [On specific minimal phonetic contrasts, models show no significant exposed-vs-foreign difference regardless of the contrast's distribution in the training language](minimal-contrasts-no-native-advantage.md) — related
