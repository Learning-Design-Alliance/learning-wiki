---
type: claim
title: "Trained logistic-regression coefficients align with the human coding scheme's inclusion and exclusion criteria"
description: "Trained logistic-regression coefficients align with the human coding scheme's inclusion and exclusion criteria"
id: model-coefficients-align-with-coding-scheme-criteria
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: rebeckah-k-fussell-2024
    resource: "https://doi.org/10.1103/physrevphyseducres.20.010113"
    title: "Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)"
    author: Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: rebeckah-k-fussell-2024-2
    resource: "https://doi.org/10.1103/physrevphyseducres.20.010113"
    title: "Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)"
    author: Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Trained logistic-regression coefficients align with the human coding scheme's inclusion and exclusion criteria

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the CR code, high-coefficient words correspond to the coding scheme's inclusion criteria, and the model's reliance on positive coefficients matches human coders' reliance on inclusion criteria. [→ Rebeckah K. Fussell 2024](#rebeckah-k-fussell-2024)
`q2 i?` For the L code, all exclusion criteria from the human coding scheme are represented by low-coefficient words, matching the scheme's reliance on exclusion criteria. [→ Rebeckah K. Fussell 2024 (2)](#rebeckah-k-fussell-2024-2)

## Evidence

### Rebeckah K. Fussell 2024

Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)

`q2 · i?` · `design · r2`

Qualitative evaluation of the trained CR model's word coefficients (Table I) against the coding scheme. The article notes three of the twelve inclusion criteria are not represented in the high-coefficient list because they are less common in the data.

> "the words with the highest coefficients are all either represented in the inclusion criteria or are close synonyms of words in the inclusion criteria of the human-generated coding scheme"

### Rebeckah K. Fussell 2024 (2)

Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)

`q2 · i?` · `design · r2`

Qualitative evaluation of the trained L model's coefficients (Table II). The article reports the magnitudes of negative coefficient words are much larger than for the CR code, matching the scheme's near-exclusive reliance on exclusion criteria; two vaguely worded criteria are not obviously captured.

> "All exclusion criteria from the human-generated coding scheme are also represented by the words with low coefficients."

## Discussion


## Related Claims
- [A GPT-4-based coding scheme achieved over 90% inter-coder agreement, surpassing results reported for specialised pre-2017 AI (~80%)](gpt4-surpasses-specialised-intelligence-agreement.md) — related
- [Systems Thinking Practices is the hardest CT construct to code reliably for both human raters and the LLM, requiring more explicitly operationalized rubrics](stp-low-reliability-complex-construct.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [GPT-3 classified students' open-ended responses about teaching practices with reliability similar to that of human coders](gpt3-coding-reliability-similar-to-humans.md) — related
- [Inter-rater reliability between human experts and AI coding is very low](low-irr-experts-vs-ai-coding.md) — related
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [Logistic regression over question-specific video segments finds peer attention and valid focus positively predict accuracy while course following negatively predicts it](course-following-negatively-predicts-accuracy.md) — related
