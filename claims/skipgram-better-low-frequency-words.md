---
type: claim
title: "Skip-Gram captures semantic relationships better than CBOW for low-frequency words such as 'pulsar'"
description: "Skip-Gram captures semantic relationships better than CBOW for low-frequency words such as 'pulsar'"
id: skipgram-better-low-frequency-words
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: eugenio-tufino-2025
    resource: "https://doi.org/10.1088/1361-6552/adea28"
    title: "Eugenio Tufino. (2025). Exploring Large Language Models (LLMs) through interactive Python activities. [doi:10.1088/1361-6552/adea28](https://doi.org/10.1088/1361-6552/adea28)"
    author: Eugenio Tufino
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# Skip-Gram captures semantic relationships better than CBOW for low-frequency words such as 'pulsar'

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` On the text8 corpus, Skip-Gram provided more domain-specific neighbours than CBOW for the rare word 'pulsar', demonstrating its effectiveness for low-frequency words. [→ Eugenio Tufino 2025](#eugenio-tufino-2025)

## Evidence

### Eugenio Tufino 2025

Eugenio Tufino. (2025). Exploring Large Language Models (LLMs) through interactive Python activities. [doi:10.1088/1361-6552/adea28](https://doi.org/10.1088/1361-6552/adea28)

`q1 · i?` · `design · r1`

Comparison of CBOW and Skip-Gram embeddings trained on the text8 corpus in the Word2Vec notebook. Listing 2 shows CBOW's top neighbours for 'pulsar' are unrelated terms while Skip-Gram returns terms such as 'pulsars', 'extrasolar' and 'ephemeris'; the article states "Skip-Gram provides more domain-specific neighbors for the relatively rare termpulsar".

> "As shown in Listing 2, Skip-Gram provides more domain-specific neighbors for the relatively rare termpulsar, demonstrating its effectiveness for low-frequency words."

## Discussion


## Related Claims
- [Corpus disambiguation can assign inaccurate word senses, which frequency statistics partly mitigate](corpus-disambiguation-inaccuracies.md) — related
- [Word2Vec analogies reveal societal stereotypes encoded in training data, such as completing 'man : surgeon :: woman : ?' with 'nurse'](word2vec-analogy-gender-bias.md) — related
