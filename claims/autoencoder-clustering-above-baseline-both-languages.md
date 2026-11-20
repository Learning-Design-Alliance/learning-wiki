---
type: claim
title: Autoencoders trained on context-free acoustic input develop phone clustering well above chance in both native and foreign evaluation conditions
description: Autoencoders trained on context-free acoustic input develop phone clustering well above chance in both native and foreign evaluation conditions
id: autoencoder-clustering-above-baseline-both-languages
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

# Autoencoders trained on context-free acoustic input develop phone clustering well above chance in both native and foreign evaluation conditions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` HCV clustering scores for all four train/evaluate conditions (EE, EM, MM, ME) far exceed a random-assignment baseline, indicating phonetic category centers emerge from context-free acoustic input. [→ Frank Lihui Tan & Youngah Do 2024](#frank-lihui-tan-youngah-do-2024)

## Evidence

### Frank Lihui Tan & Youngah Do 2024

Frank Lihui Tan & Youngah Do. (2024). The formation of perceptual space in early phonetic acquisition: a cross-linguistic modeling approach. Originally published 2023. [doi:10.48550/arXiv.2407.18501](https://doi.org/10.48550/arXiv.2407.18501)

`q2 · i?` · `design · r2`

Unsupervised clustering evaluation (Kmeans, 256 clusters) of hidden representations against ground-truth phonetic labels, scored with homogeneity, completeness, and V-measure. The authors report all four conditions were "much higher than the baseline model" (e.g., exposed English V = 0.271 vs baseline 0.007).

> "As shown in Table 2, the HCV scores of all four conditions, i.e., EE, EM, MM, and ME, were much higher than the baseline model."

## Discussion


## Related Claims
- [Bottom-up models trained on context-free acoustic input do not distinguish phonemes from allophones](allophony-not-captured-bottom-up.md) — related
- [On the general ABX test over all phone pairs, models discriminate exposed-language phones significantly better than foreign-language phones](general-abx-exposed-better-than-foreign.md) — related
- [On specific minimal phonetic contrasts, models show no significant exposed-vs-foreign difference regardless of the contrast's distribution in the training language](minimal-contrasts-no-native-advantage.md) — related
