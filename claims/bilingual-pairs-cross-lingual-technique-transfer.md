---
type: claim
title: Bilingual instruction pairs transfer technique knowledge across languages, more strongly to Indo-Aryan (∆TF = +3.2) than Dravidian (∆TF = +1.8) languages
description: Bilingual instruction pairs transfer technique knowledge across languages, more strongly to Indo-Aryan (∆TF = +3.2) than Dravidian (∆TF = +1.8) languages
id: bilingual-pairs-cross-lingual-technique-transfer
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: shwetha-singaravelu-2026
    resource: "https://doi.org/10.48550/arxiv.2607.23322"
    title: "Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani. (2026). IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems. arXiv. https://arxiv.org/abs/2607.23322 [doi:10.48550/arxiv.2607.23322](https://doi.org/10.48550/arxiv.2607.23322)"
    author: Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Bilingual instruction pairs transfer technique knowledge across languages, more strongly to Indo-Aryan (∆TF = +3.2) than Dravidian (∆TF = +1.8) languages

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` Cross-lingual transfer of technique knowledge from bilingual pairs is stronger for procedural techniques and asymmetric across language families. [→ Shwetha Singaravelu 2026](#shwetha-singaravelu-2026)

## Evidence

### Shwetha Singaravelu 2026

Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani. (2026). IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems. arXiv. https://arxiv.org/abs/2607.23322 [doi:10.48550/arxiv.2607.23322](https://doi.org/10.48550/arxiv.2607.23322)

`q2 · i?` · `design · r3`

Per-technique analysis in Section 6.2 of cross-lingual transfer from bilingual pairs, reporting ∆TF of +3.2 for Indo-Aryan targets versus +1.8 for Dravidian targets; the ∆TF values are printed but no standardized effect size is given.

> "transfer from English-Hindi bilingual pairs to other Indo-Aryan languages (Marathi, Bengali) is stronger (∆TF = +3.2) than transfer to Dravidian languages (Tamil, Telugu, ∆TF = +1.8), consistent with the typological distance between these language families"

## Discussion


## Learner Variables
- [Reading and Language](../learner-variables/reading-and-language.md) — moderator: an instructional effect differs with it

## Related Claims
- Process and enact SRL categories transfer slightly better from German to English than English to German — related
- LLM embedding-based SRL classifiers trained on one language reliably classify SRL categories in the other language within the same instructional domain — related
- Cross-language SRL classifier transfer shows about 0.1 AUC degradation relative to within-language performance, except for realizing errors — related
- [Cross-linguistic transfer is skill-specific: phonological awareness and print concepts are more likely to transfer across languages, while vocabulary and comprehension are more language-dependent](cross-linguistic-transfer-skill-specific.md) — a broader claim this one bears on
- [Preserving a bilingual student's heritage language supports rather than hinders English acquisition](heritage-language-preservation-supports-english-acquisition.md) — related
