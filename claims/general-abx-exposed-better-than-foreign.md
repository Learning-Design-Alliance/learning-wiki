---
type: claim
title: On the general ABX test over all phone pairs, models discriminate exposed-language phones significantly better than foreign-language phones
description: On the general ABX test over all phone pairs, models discriminate exposed-language phones significantly better than foreign-language phones
id: general-abx-exposed-better-than-foreign
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: frank-lihui-tan-youngah-do-2024
    resource: "https://doi.org/10.48550/arXiv.2407.18501"
    title: "Frank Lihui Tan & Youngah Do. (2024). The formation of perceptual space in early phonetic acquisition: a cross-linguistic modeling approach. Originally published 2023. [doi:10.48550/arXiv.2407.18501](https://doi.org/10.48550/arXiv.2407.18501)"
    author: "Frank Lihui Tan & Youngah Do"
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: frank-lihui-tan-youngah-do-2024-2
    resource: "https://doi.org/10.48550/arXiv.2407.18501"
    title: "Frank Lihui Tan & Youngah Do. (2024). The formation of perceptual space in early phonetic acquisition: a cross-linguistic modeling approach. Originally published 2023. [doi:10.48550/arXiv.2407.18501](https://doi.org/10.48550/arXiv.2407.18501)"
    author: "Frank Lihui Tan & Youngah Do"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On the general ABX test over all phone pairs, models discriminate exposed-language phones significantly better than foreign-language phones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across all vowel and consonant pairs, exposed conditions (EE, MM) achieved significantly lower ABX error rates than foreign conditions (EM, ME), with p < 0.001 for both EE vs ME and MM vs EM. [→ Frank Lihui Tan & Youngah Do 2024](#frank-lihui-tan-youngah-do-2024)
`q2 i?` The two exposed conditions did not differ from each other (EE vs MM, p = 0.851). [→ Frank Lihui Tan & Youngah Do 2024 (2)](#frank-lihui-tan-youngah-do-2024-2)

## Evidence

### Frank Lihui Tan & Youngah Do 2024

Frank Lihui Tan & Youngah Do. (2024). The formation of perceptual space in early phonetic acquisition: a cross-linguistic modeling approach. Originally published 2023. [doi:10.48550/arXiv.2407.18501](https://doi.org/10.48550/arXiv.2407.18501)

`q2 · i?` · `design · r2`

ABX discrimination test over all logically possible vowel and consonant pairs (885 English pairs, 714 Mandarin pairs) using Euclidean distance on z-scored hidden representations. Exposed means: EE 0.3, MM 0.301; foreign: ME 0.321, EM 0.327; both comparisons p < 0.001.

> "Overall, the models tested on exposed languages (EE and MM) achieved significantly lower error rate than models tested on untrained , foreign languages (EM and ME) ( 𝜇𝐸𝐸 =  0.3, 𝜎𝐸𝐸 = 0.12; 𝜇𝑀𝑀 =  0.301, 𝜎𝑀𝑀 =  0.132; 𝜇𝑀𝐸 =  0.321, 𝜎𝑀𝐸 =  0.119; 𝜇𝐸𝑀 =  0.327, 𝜎𝐸𝑀 = 0.126;  𝐸𝐸 𝑣𝑠 𝑀𝐸, 𝑝 <  0.001;  𝑀𝑀 𝑣𝑠 𝐸𝑀, 𝑝 <  0.001;"

### Frank Lihui Tan & Youngah Do 2024 (2)

Frank Lihui Tan & Youngah Do. (2024). The formation of perceptual space in early phonetic acquisition: a cross-linguistic modeling approach. Originally published 2023. [doi:10.48550/arXiv.2407.18501](https://doi.org/10.48550/arXiv.2407.18501)

`q2 · i?` · `design · r2`

Same general ABX test: the two exposed-language conditions did not differ significantly from each other (p = 0.851), reported alongside the exposed-vs-foreign comparisons in the same analysis.

> "𝐸𝐸 𝑣𝑠 𝑀𝑀, 𝑝 =  0.851). See Figure 2."

## Discussion


## Related Claims
- [Bottom-up models trained on context-free acoustic input do not distinguish phonemes from allophones](allophony-not-captured-bottom-up.md) — related
- [Autoencoders trained on context-free acoustic input develop phone clustering well above chance in both native and foreign evaluation conditions](autoencoder-clustering-above-baseline-both-languages.md) — related
- [On specific minimal phonetic contrasts, models show no significant exposed-vs-foreign difference regardless of the contrast's distribution in the training language](minimal-contrasts-no-native-advantage.md) — related
