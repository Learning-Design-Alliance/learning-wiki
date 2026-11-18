---
type: claim
title: The underlying sentence similarity algorithm achieves Pearson correlations of 0.8753 for word similarity and 0.8794 for sentence similarity against benchmarks
description: The underlying sentence similarity algorithm achieves Pearson correlations of 0.8753 for word similarity and 0.8794 for sentence similarity against benchmarks
id: sentence-similarity-benchmark-correlations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: atish-pawar-and-vijay-mago-2018
    resource: "https://doi.org/10.48550/arXiv.1804.06333"
    title: "Atish Pawar and Vijay Mago. (2018). Similarity between Learning Outcomes from Course Objectives using Semantic Analysis, Bloom's taxonomy and Corpus statistics. [doi:10.48550/arXiv.1804.06333](https://doi.org/10.48550/arXiv.1804.06333)"
    author: Atish Pawar and Vijay Mago
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The underlying sentence similarity algorithm achieves Pearson correlations of 0.8753 for word similarity and 0.8794 for sentence similarity against benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The sentence similarity algorithm used in the methodology correlates with benchmark word-similarity data at Pearson r = 0.8753 and with mean human sentence-similarity judgments at r = 0.8794. [→ Atish Pawar and Vijay Mago 2018](#atish-pawar-and-vijay-mago-2018)

## Evidence

### Atish Pawar and Vijay Mago 2018

Atish Pawar and Vijay Mago. (2018). Similarity between Learning Outcomes from Course Objectives using Semantic Analysis, Bloom's taxonomy and Corpus statistics. [doi:10.48550/arXiv.1804.06333](https://doi.org/10.48550/arXiv.1804.06333)

`q2 · i?` · `design · r2`

Reported in the Discussion section, these are benchmark correlations of the authors' previously established algorithm, not of the full learning-objective methodology. Both "Pearson correlation coeﬃcient" values, 0.8753 and 0.8794, are printed directly.

> "The sentence similarity algorithm used for this methodology achieved good Pearson correlation coeﬃcient of 0.8753 for word similarity concerning the bechmark standard[21] and 0.8794 for sentence similarity with respect to mean human similarity [17]."

## Discussion


## Related Claims
- [The disambiguation-enhanced word similarity algorithm produces better results than the baseline Li et al. algorithm for synonym pairs with similar meaning, and comparable results otherwise](disambiguation-word-similarity-better-for-synonyms.md) — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [Gemini-2.5-Pro can effectively replicate human expert judgments when answering SLM-generated MCQs](gemini-surrogate-judge-replicates-human-answers.md) — related
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
- [Corpus disambiguation can assign inaccurate word senses, which frequency statistics partly mitigate](corpus-disambiguation-inaccuracies.md) — related
- [A small survey of users judged the system's semantic and Bloom similarity results useful for deciding between real learning objectives](lo-similarity-user-survey-usefulness.md) — related
