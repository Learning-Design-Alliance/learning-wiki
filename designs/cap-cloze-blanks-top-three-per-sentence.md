---
type: design
id: cap-cloze-blanks-top-three-per-sentence
title: Cap Cloze questions per key sentence at the three highest-probability candidate words to reduce manual evaluation burden
description: "The article limits blank selection to the top-ranked words from the Naive Bayes probability list, because generating every candidate would make human evaluation prohibitive: \"the number of Cloze questions generated fr..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
sources:
  - id: praveen-kumar-2024
    resource: "https://doi.org/10.1007/s40593-023-00333-6"
    title: "Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K. (2024). A Novel Framework for the Generation of Multiple Choice Question Stems Using Semantic and Machine-Learning Techniques. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00333-6"
    author: "Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K"
---

# Cap Cloze questions per key sentence at the three highest-probability candidate words to reduce manual evaluation burden

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article limits blank selection to the top-ranked words from the Naive Bayes probability list, because generating every candidate would make human evaluation prohibitive: "the number of Cloze questions generated from each key sentence is limited by choosing only the first three words from the Word_prd list." This keeps expert evaluation of usefulness tractable while retaining the highest-probability blanks.

## Design Implications

### Context
#### Requirements
- A sorted Word_prd list of words with computed blank-substitution probabilities
#### Constraints
- The article presents this cap as an evaluation-burden trade-off; it does not report testing whether three blanks per sentence is optimal

### Target Learners
- students taking MCQ assessments in technical courses

### Learning Goals
- practical scale-up of automatically generated Cloze items for drills and practice

### Claims
- Mbt Three Stage Cloze Pipeline [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K. (2024). A Novel Framework for the Generation of Multiple Choice Question Stems Using Semantic and Machine-Learning Techniques. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00333-6
