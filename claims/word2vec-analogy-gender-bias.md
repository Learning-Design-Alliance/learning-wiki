---
type: claim
title: "Word2Vec analogies reveal societal stereotypes encoded in training data, such as completing 'man : surgeon :: woman : ?' with 'nurse'"
description: "Word2Vec analogies reveal societal stereotypes encoded in training data, such as completing 'man : surgeon :: woman : ?' with 'nurse'"
id: word2vec-analogy-gender-bias
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
    rigour: 2
---

# Word2Vec analogies reveal societal stereotypes encoded in training data, such as completing 'man : surgeon :: woman : ?' with 'nurse'

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Running the analogy 'man : surgeon :: woman : ?' returned 'nurse' (similarity approximately 0.647), revealing societal stereotypes encoded in the training corpus; the article notes such bias extends to larger LLMs like GPT-4. [→ Eugenio Tufino 2025](#eugenio-tufino-2025)

## Evidence

### Eugenio Tufino 2025

Eugenio Tufino. (2025). Exploring Large Language Models (LLMs) through interactive Python activities. [doi:10.1088/1361-6552/adea28](https://doi.org/10.1088/1361-6552/adea28)

`q1 · i?` · `design · r2`

Demonstration in the Word2Vec notebook using the analogy function on the man:surgeon::woman analogy, which returned [('nurse', 0.64670729637146)]. The author reports that "The association of ”woman” with ”nurse” rather than ”surgeon” reveals societal stereotypes encoded in the training corpus" and frames this as an ethics discussion opportunity for educators.

> "The association of ”woman” with ”nurse” rather than ”surgeon” reveals societal stereotypes encoded in the training corpus."

## Discussion


## Related Claims
- [Wikipedia2Vec keyword embeddings yield higher episodic returns than one-hot keyword encodings, but the model appears to overfit each corpus rather than leverage entity relationships](wikipedia2vec-embeddings-beat-onehot-overfit.md) — related
- [Skip-Gram captures semantic relationships better than CBOW for low-frequency words such as 'pulsar'](skipgram-better-low-frequency-words.md) — related
- [Preliminary observation: the inequitable trio had two men and one woman while the equitable trio had two women and one man](gender-ratio-preliminary-lab-equity.md) — related
