---
type: claim
title: "Existing AQG approaches concentrate on non-technical domains, and technical-domain Wh-type generation has been limited to Bloom's cognitive Level I"
description: "Existing AQG approaches concentrate on non-technical domains, and technical-domain Wh-type generation has been limited to Bloom's cognitive Level I"
id: existing-aqg-technical-domain-limited-non-technical
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: praveen-kumar-2024
    resource: "https://doi.org/10.1007/s40593-023-00333-6"
    title: "Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K. (2024). A Novel Framework for the Generation of Multiple Choice Question Stems Using Semantic and Machine-Learning Techniques. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00333-6"
    author: "Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Existing AQG approaches concentrate on non-technical domains, and technical-domain Wh-type generation has been limited to Bloom's cognitive Level I

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The majority of existing ontology- and ML-based AQG approaches concentrate on non-technical domains and therefore have no relevance to Bloom's-Taxonomy-based question evaluation. [→ Praveen Kumar 2024](#praveen-kumar-2024)

## Evidence

### Praveen Kumar 2024

Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K. (2024). A Novel Framework for the Generation of Multiple Choice Question Stems Using Semantic and Machine-Learning Techniques. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00333-6

`q2 · i?` · `design · r2`

In the Summary of Related Work, the article derives from its Tables 3 and 4 that "Majority of the approaches have concentrated only on non-technical domains", positioning this research's technical-domain, Bloom-aligned focus as a gap-filling contribution. Narrative-review-level inference.

> "Majority of the approaches have concentrated only on non-technical domains and therefore have no relevance in evaluating questions based on Bloom's Taxonomy"

## Discussion


## Related Claims
- [Prior AQG work shows ML yields grammatically correct Cloze questions while ontology approaches struggle with Cloze but produce meaningful Wh-type questions](ml-cloze-ontology-wh-grammaticality-gap.md) — related
- [Prior automatic MCQ generation approaches produce structurally simple questions (at most two stem entities) testing mainly recall](prior-aqg-simple-recall-questions.md) — related
- [EMCQG generated more than 3 million distinct case-based questions for four physician specialities from the EMMeT ontology](emcqg-three-million-questions-four-specialities.md) — reports the opposite
- [The Bloom-driven framework generalizes to social-science questions, with automated rubrics agreeing strongly with experts on usability but only modestly on Bloom level](social-science-generalization-human-agreement.md) — related
- [LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retrieval practice (ρ=0.06), as do co-generated Bloom levels (ρ=0.02)](llm-difficulty-labels-fail-to-predict-empirical-item-difficulty.md) — related
- [Assessment remains the dominant purpose of educational AQG, mirroring pre-2014 findings](aqg-assessment-dominant-purpose.md) — related
- AQG evaluation suffers from insufficient and heterogeneous experimental reporting and metrics — related
- [Text remains the most popular AQG input, while Semantic Web sources are used mainly for domain-unspecific questions](aqg-text-most-popular-input.md) — related
