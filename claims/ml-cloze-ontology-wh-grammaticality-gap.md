---
type: claim
title: Prior AQG work shows ML yields grammatically correct Cloze questions while ontology approaches struggle with Cloze but produce meaningful Wh-type questions
description: Prior AQG work shows ML yields grammatically correct Cloze questions while ontology approaches struggle with Cloze but produce meaningful Wh-type questions
id: ml-cloze-ontology-wh-grammaticality-gap
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
  - id: praveen-kumar-2024-2
    resource: "https://doi.org/10.1007/s40593-023-00333-6"
    title: "Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K. (2024). A Novel Framework for the Generation of Multiple Choice Question Stems Using Semantic and Machine-Learning Techniques. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00333-6"
    author: "Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Prior AQG work shows ML yields grammatically correct Cloze questions while ontology approaches struggle with Cloze but produce meaningful Wh-type questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Ontology-based approaches fail to generate grammatically correct Cloze questions compared to ML techniques because verbalizing ontology into Cloze questions yields grammatically incorrect questions. [→ Praveen Kumar 2024](#praveen-kumar-2024)
`q2 i?` ML approaches generate reasonably good Cloze questions but fail to generate grammatically correct Wh-type questions compared to the ontology technique. [→ Praveen Kumar 2024 (2)](#praveen-kumar-2024-2)

## Evidence

### Praveen Kumar 2024

Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K. (2024). A Novel Framework for the Generation of Multiple Choice Question Stems Using Semantic and Machine-Learning Techniques. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00333-6

`q2 · i?` · `design · r2`

The article's background synthesis, citing Kurdi et al. (2020) and Faizan & Lohmann (2018), reports that "verbalizing ontology into Cloze questions generates grammatically incorrect questions", motivating the assignment of Cloze generation to ML. This is the review's attribution, not a new experiment.

> "The main reason is that verbalizing ontology into Cloze questions generates grammatically incorrect questions (Faizan & Lohmann, 2018)."

### Praveen Kumar 2024 (2)

Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K. (2024). A Novel Framework for the Generation of Multiple Choice Question Stems Using Semantic and Machine-Learning Techniques. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00333-6

`q2 · i?` · `design · r2`

The article reports, citing the review by Ch and Saha (2018), that "ML generates reasonably good Cloze questions but fails to generate grammatically correct Wh-type questions", which motivates generating Wh-type stems from ontology semantics instead. Second-hand review attribution.

> "ML generates reasonably good Cloze questions but fails to generate grammatically correct Wh-type questions compared to the ontology technique."

## Discussion


## Related Claims
- [Existing AQG approaches concentrate on non-technical domains, and technical-domain Wh-type generation has been limited to Bloom's cognitive Level I](existing-aqg-technical-domain-limited-non-technical.md) — related
- [Expert evaluation found the hybrid system's generated MCQ stems promising in usefulness and grammatical correctness](expert-evaluation-mcq-stems-promising.md) — related
- [EMCQG generated more than 3 million distinct case-based questions for four physician specialities from the EMMeT ontology](emcqg-three-million-questions-four-specialities.md) — related
- [Ontology-based generation produced exam-appropriate case-based MCQs, with 30% of a stratified sample rated appropriate by both expert raters and 50% by at least one](emcqg-expert-rated-exam-appropriate-questions.md) — related
