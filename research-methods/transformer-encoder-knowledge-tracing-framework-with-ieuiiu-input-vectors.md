---
type: research-method
id: transformer-encoder-knowledge-tracing-framework-with-ieuiiu-input-vectors
title: Transformer-encoder knowledge tracing framework with IEU/IIU input vectors
description: "A deep knowledge tracing framework for the ASSISTments dataset that predicts students' responses to end-of-unit test problems from action logs of in-unit assignments."
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: lu-2024
    resource: "https://osf.io/mdpzc/"
    title: "Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/"
    author: "Lu, Y., Tong, L., & Cheng, Y"
---

# Transformer-encoder knowledge tracing framework with IEU/IIU input vectors

> **Research Method** · [All research methods](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
A deep knowledge tracing framework for the ASSISTments dataset that predicts students' responses to end-of-unit test problems from action logs of in-unit assignments. It constructs IEU vectors (problem, sequence, student, and class information) as queries and IIU vectors (adding action-type embeddings and action features with positional encoding) as keys and values for a Transformer Encoder. The article states it is "a novel Transformer-based framework for the ASSISTments dataset which integrates several data-preprocessing techniques with a Transformer-based predictive model". Code, saved models, and predictions are released on OSF.

## Accounts
<!-- How each source describes or uses the method -->
- **Transformer-encoder knowledge tracing framework with IEU/IIU input vectors and released code, models, and predictions**: A deep knowledge tracing framework for the ASSISTments dataset that predicts students' responses to end-of-unit test problems from action logs of in-unit assignments. It constructs IEU vectors (problem, sequence, student, and class information) as queries and IIU vectors (adding action-type embeddings and action features with positional encoding) as keys and values for a Transformer Encoder. The article states it is "a novel Transformer-based framework for the ASSISTments dataset which integrates several data-preprocessing techniques with a Transformer-based predictive model". Code, saved models, and predictions are released on OSF. (Lu et al. (2024))

### Claims
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](../claims/model1-outperforms-complex-model2.md) [+M]
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](../claims/ablation-all-features-maximize-auc.md) [+M]
- [Single instances of help-seeking actions (answer requested, explanation requested) carry more predictive information than single correct or open responses (ISA)](../claims/isa-help-seeking-more-informative-than-correct-response.md) [+M]
- [The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an AUC of 78.969% on the private evaluation dataset](../claims/transformer-kt-first-place-edm-cup-2023.md) [+M]
- [NCA scores of IIU input vectors order action types identically to the main-effects ordering (Spearman's ρ = 1)](../claims/nca-scores-align-with-main-effects.md) [+M]
- [In artificial action logs, \"answer requested\" yields the lowest average predicted probability of a correct end-of-unit response, below even \"wrong response\"](../claims/answer-requested-lowest-main-effect.md) [+M]

## Related Research Methods
-

## Key Sources
- Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/

<!-- merged 2026-10-10 from elements/transformer-ieu-iiu-kt-framework ("Transformer-encoder knowledge tracing framework with IEU/IIU input vectors and released code, models, and predictions"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Transformer-encoder knowledge tracing framework with IEU/IIU input vectors and released code, models, and predictions

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
A deep knowledge tracing framework for the ASSISTments dataset that predicts students' responses to end-of-unit test problems from action logs of in-unit assignments. It constructs IEU vectors (problem, sequence, student, and class information) as queries and IIU vectors (adding action-type embeddings and action features with positional encoding) as keys and values for a Transformer Encoder. The article states it is "a novel Transformer-based framework for the ASSISTments dataset which integrates several data-preprocessing techniques with a Transformer-based predictive model". Code, saved models, and predictions are released on OSF.

## Design Implications

### Context
#### Requirements
- Auxiliary information on problems, sequences, students, and classes (e.g., BERT+PCA problem text embeddings, curriculum folder paths, class memberships for SVD embeddings) is available in the training data.
#### Constraints
- The framework is designed for the distinction between in-unit assignments and end-of-unit tests; some dataset items lack features beyond their IDs, introducing missing or incomplete data the model must account for.

### Target Learners
- K-12 mathematics students using the ASSISTments online learning platform

### Target Learning Goals
- Predicting student performance on end-of-unit mathematics test problems from clickstream process data

### Claims
<!- - Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] - ->
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](../claims/model1-outperforms-complex-model2.md) [+M]
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](../claims/ablation-all-features-maximize-auc.md) [+M]
- [Single instances of help-seeking actions (answer requested, explanation requested) carry more predictive information than single correct or open responses (ISA)](../claims/isa-help-seeking-more-informative-than-correct-response.md) [+M]
- [The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an AUC of 78.969% on the private evaluation dataset](../claims/transformer-kt-first-place-edm-cup-2023.md) [+M]
- [NCA scores of IIU input vectors order action types identically to the main-effects ordering (Spearman's ρ = 1)](../claims/nca-scores-align-with-main-effects.md) [+M]
- [In artificial action logs, \"answer requested\" yields the lowest average predicted probability of a correct end-of-unit response, below even \"wrong response\"](../claims/answer-requested-lowest-main-effect.md) [+M]

## Related Elements
- 

## Examples
-

## Key Sources
- Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/
-->
