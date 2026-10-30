---
type: claim
title: A Naïve Bayes classifier distinguishes free-text definitions of curiosity and interest at above-chance accuracy on unseen data
description: A Naïve Bayes classifier distinguishes free-text definitions of curiosity and interest at above-chance accuracy on unseen data
id: naive-bayes-classifies-curiosity-interest-definitions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-22
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: donnellan-2021
    resource: "https://doi.org/10.1007/s10648-021-09622-9"
    title: "Donnellan, E., Aslan, S., Fastrich, G. M., & Murayama, K. (2021). How Are Curiosity and Interest Different? Naïve Bayes Classification of People's Beliefs. Educational Psychology Review. https://doi.org/10.1007/s10648-021-09622-9"
    author: "Donnellan, E., Aslan, S., Fastrich, G. M., & Murayama, K."
    q: 3
    i: "?"
    kind: associational
    rigour: 2
  - id: donnellan-2021-2
    resource: "https://doi.org/10.1007/s10648-021-09622-9"
    title: "Donnellan, E., Aslan, S., Fastrich, G. M., & Murayama, K. (2021). How Are Curiosity and Interest Different? Naïve Bayes Classification of People's Beliefs. Educational Psychology Review. https://doi.org/10.1007/s10648-021-09622-9"
    author: "Donnellan, E., Aslan, S., Fastrich, G. M., & Murayama, K."
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# A Naïve Bayes classifier distinguishes free-text definitions of curiosity and interest at above-chance accuracy on unseen data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Cross-validated classifier accuracy exceeded chance for both the main test data (79.29%) and additional test data (77.06%). [→ Donnellan 2021](#donnellan-2021)
`q3 i?` Feature selection identified 42 word stems that accurately distinguished curiosity and interest definitions in training data (87.13%). [→ Donnellan 2021 (2)](#donnellan-2021-2)

## Evidence

### Donnellan 2021

Donnellan, E., Aslan, S., Fastrich, G. M., & Murayama, K. (2021). How Are Curiosity and Interest Different? Naïve Bayes Classification of People's Beliefs. Educational Psychology Review. https://doi.org/10.1007/s10648-021-09622-9

`q3 · i?` · `associational · r2`

Pre-registered cross-validation study: a Naïve Bayes classifier trained on free-text definitions was tested on unseen main and additional test sets, with binomial tests against 50% chance. The article reports accuracy "significantly above chance" for both test sets; no effect size is printed.

> "Importantly, the classifier was also highly accurate in predicting unseen data (Table 1), accurately predicting the correct definitio n type significantly above chance for both the main test data (79.29%; 95% CI: 72.98 –84.71%, p < .001) and additional test data (77.06%; 95% CI: 70.91 – 82.47%, p < .001)."

### Donnellan 2021 (2)

Donnellan, E., Aslan, S., Fastrich, G. M., & Murayama, K. (2021). How Are Curiosity and Interest Different? Naïve Bayes Classification of People's Beliefs. Educational Psychology Review. https://doi.org/10.1007/s10648-021-09622-9

`q3 · i?` · `associational · r2`

Classifier training on the main dataset (Prolific Academic participants producing two free-text definitions each) identified 42 discriminative word stems, "accurately classifying 87.13% of definitions" in the training data.

> "In training, feature selection identified 42 word stems which accurately distinguished curiosity and interest definitions in the training data (accurately classifying 87.13% of definitions)."

## Discussion


## Related Claims
- [The non-expert-trained classifier also distinguishes expert definitions of curiosity and interest above chance](classifier-generalises-to-expert-definitions.md) — related
- [Frequently used word stems such as \"can\", \"want\", \"thing\" and \"feel\" carry no discriminative value between curiosity and interest definitions](common-word-stems-no-discriminative-value.md) — related
- [Education and age of English acquisition moderated classifier accuracy by definition type in the main test data](demographic-moderators-classifier-accuracy.md) — related
- [The consensus distinction characterises curiosity as active seeking of specific unknown information and interest as pleasurable, in-depth seeking in already-known domains](consensus-distinction-curiosity-active-interest-pleasurable.md) — related
- [Participants' ratings of how similar curiosity and interest are did not predict classifier accuracy](similarity-rating-no-effect-classifier-accuracy.md) — related
