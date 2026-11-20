---
type: claim
title: NLP topic modeling (BERTopic) cross-validates human coding of syllabi but misses rare topics, creating an equity-relevant bias
description: NLP topic modeling (BERTopic) cross-validates human coding of syllabi but misses rare topics, creating an equity-relevant bias
id: bertopic-cross-validation-human-coding-syllabi-bias-rare-topics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: buzzell-2025
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010139"
    title: "Buzzell, A., Barthelemy, R., & Atherton, T. (2025). Modern physics courses: Understanding the content taught in the U.S. arXiv. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010139](https://doi.org/10.1103/physrevphyseducres.21.010139)"
    author: "Buzzell, A., Barthelemy, R., & Atherton, T."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: buzzell-2025-2
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010139"
    title: "Buzzell, A., Barthelemy, R., & Atherton, T. (2025). Modern physics courses: Understanding the content taught in the U.S. arXiv. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010139](https://doi.org/10.1103/physrevphyseducres.21.010139)"
    author: "Buzzell, A., Barthelemy, R., & Atherton, T."
    q: 2
    i: "?"
    kind: qualitative
    rigour: 2
---

# NLP topic modeling (BERTopic) cross-validates human coding of syllabi but misses rare topics, creating an equity-relevant bias

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` BERTopic-generated topic frequencies matched human-coded results closely, with the exam topic occurring in 91/169 documents, matching the human-coded exam figure almost exactly. [→ Buzzell 2025](#buzzell-2025)
`q2 i?` The NLP analysis failed to capture rare features including pregnancy/childbirth (2%), AI/ChatGPT (1%), and Lagrangian/Hamiltonian mechanics (3%), which has important implications for equity. [→ Buzzell 2025 (2)](#buzzell-2025-2)

## Evidence

### Buzzell 2025

Buzzell, A., Barthelemy, R., & Atherton, T. (2025). Modern physics courses: Understanding the content taught in the U.S. arXiv. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010139](https://doi.org/10.1103/physrevphyseducres.21.010139)

`q2 · i?` · `associational · r2`

BERTopic was run 20 times on a corpus of 169 syllabus documents, producing between 97 and 105 topics per run. Human-coded policy topics were compared to the largest closely related NLP topic frequency distributions, and the authors report the relative frequencies are strikingly similar for many topics.

> "The sixth topic in table I, for example, concerns exams, and occurs in 91/169 documents, a number that matches almost exactly with the human-coded results in Figure 10."

### Buzzell 2025 (2)

Buzzell, A., Barthelemy, R., & Atherton, T. (2025). Modern physics courses: Understanding the content taught in the U.S. arXiv. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010139](https://doi.org/10.1103/physrevphyseducres.21.010139)

`q2 · i?` · `qualitative · r2`

Topics too infrequent to survive HDBSCAN clustering were missed by BERTopic. Some of these, such as pregnancy/childbirth, are closely related to issues of equity, representing a possible source of bias if NLP analysis were relied on exclusively.

> "the NLP analysis was not able to capture the fact that 2% of the syllabi referred to pregnancy, 1% referred to AI/ChatGPT, and 3% referred to Lagrangian/Hamiltonian mechanics; neglecting the uncommon has important implications for equity."

## Discussion


## Related Claims
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — a broader claim this one bears on
- [Students' variation in concern across ethical issues corresponds with topic coverage on typical CS ethics syllabi, which rarely address military applications](syllabus-coverage-matches-concern-variation.md) — related
- [Twitter users' concerns about ChatGPT in education converge on five frequently discussed categories: academic integrity, impact on learning outcomes and skill development, limitation of capabilities, policy and social concerns, and workforce challenges](chatgpt-education-five-concern-categories.md) — related
- [90% of modern physics syllabi explicitly state exams are used, and 78% do not state whether grades will be curved](modern-physics-assessment-exams-grading-curve-unstated.md) — related
