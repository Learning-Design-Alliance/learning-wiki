---
type: claim
title: Multilingual mBERT embeddings uniformly outperform monolingual ELECTRA embeddings when parsing Old English with Modern English-trained models
description: Multilingual mBERT embeddings uniformly outperform monolingual ELECTRA embeddings when parsing Old English with Modern English-trained models
id: mbert-beats-electra-on-oe-parsing
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: lauren-levine-2025
    resource: "https://doi.org/10.48550/arXiv.2504.18718"
    title: "Lauren Levine, Junghyun Min, and Amir Zeldes. (2025). Building UD Cairo for Old English in the Classroom. [doi:10.48550/arXiv.2504.18718](https://doi.org/10.48550/arXiv.2504.18718)"
    author: Lauren Levine, Junghyun Min, and Amir Zeldes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Multilingual mBERT embeddings uniformly outperform monolingual ELECTRA embeddings when parsing Old English with Modern English-trained models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Although ELECTRA performs higher on the Modern English GUM 11 dev data, mBERT performs better on the Old English data for all annotation categories, demonstrating the advantage of multilingual pretrained embeddings on a different language than training. [→ Lauren Levine 2025](#lauren-levine-2025)

## Evidence

### Lauren Levine 2025

Lauren Levine, Junghyun Min, and Amir Zeldes. (2025). Building UD Cairo for Old English in the Classroom. [doi:10.48550/arXiv.2504.18718](https://doi.org/10.48550/arXiv.2504.18718)

`q2 · i?` · `design · r2`

Comparison in the parsing experiments section (Table 2): DiaParser with English ELECTRA vs multilingual mBERT embeddings, trained on GUM 11 and evaluated on the OE Cairo sentences across Form, Lemma, Hyperlemma, and Gloss input categories.

> "although the ELECTRA model has higher performance on the Modern English GUM 11 dev data, mBERT uniformly performs better on the Old English data for all annotation categories"

## Discussion


## Related Claims
- Parsing Old English with Modern English-trained parsers improves when annotated features (hyperlemma, gloss) replace raw forms as input — related
- Current LLM outputs in Old English do not reflect authentic syntax but can be mitigated by post-editing — related
- [Multilingual student models perform better for low-resource languages while monolingual models suit high-resource languages](multilingual-student-models-lrl-monolingual-hrl.md) — related
- [Novice student annotators with minimal UD instruction achieve attachment scores comparable to experienced annotators on an Old English treebanking assignment](novice-annotators-comparable-ud-accuracy.md) — related
