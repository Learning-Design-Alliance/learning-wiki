---
type: research-method
id: attribute-hierarchy-models-in-cognitive-diagnosis
title: Attribute hierarchy models in cognitive diagnosis
description: Attribute hierarchy models are an approach within cognitively diagnostic modeling in which attributes are treated as interdependent rather than isolated entities.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# Attribute hierarchy models in cognitive diagnosis

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Attribute hierarchy models are an approach within cognitively diagnostic modeling in which attributes are treated as interdependent rather than isolated entities. The article describes the approach of imposing "a hierarchical structure so that mastery of one or more attributes is a prerequisite of mastering one or more other attributes." This organizes the latent attribute space according to prerequisite relations among the skills underlying test performance.

## Accounts
<!-- How each source describes or uses the method -->
- **Attribute hierarchy models in cognitive diagnosis impose prerequisite relations among attributes**: Attribute hierarchy models are an approach within cognitively diagnostic modeling in which attributes are treated as interdependent rather than isolated entities. The article describes the approach of imposing "a hierarchical structure so that mastery of one or more attributes is a prerequisite of mastering one or more other attributes." This organizes the latent attribute space according to prerequisite relations among the skills underlying test performance. (Köhn et al. (2019))
- **Equivalence classes and nonidentifiability of attribute profiles under unrestricted estimation**: The article explains the mechanism behind misclassification when hierarchies exist but estimation is unrestricted. Two different attribute profiles can yield the same ideal response profile, in which case the article states they "cannot be separated, and they are in an equivalence class." Under the DINA model such profiles have exactly the same likelihood; under more general models such as rRUM, ACDM, and GDINA they have very similar likelihoods, so unrestricted MLE can return impermissible profiles. With uniform Bayesian priors, profiles within an equivalence class also have the same or similar posterior probability and cannot be separated. (Tu et al. (2019))
- **Restricted Q-matrix design (QH) for embedding attribute hierarchies in latent class-based CDMs**: The article defines a restricted Q matrix, QH, that guarantees all items reflect a specified attribute hierarchy. It is built from a reachability (R) matrix representing direct and indirect prerequisite relations among attributes. The article states: "QH was defined as a J3K matrix that associates the K attributes to J items and reflects the assumed attribute hierarchy satisfying the following conditions: (a) an R matrix is a submatrix of the QH matrix and (b) all the transposes of the item-attribute Q vectors in it belong to the permissible attribute set." It is used as the cognitive blueprint for item writing before test development, and the article's estimation comparisons all presuppose a Q matrix of this form. (Tu et al. (2019))

### Claims
- [Unrestricted estimation produces impermissible attribute pattern rates around 42.6% to 47.8% in simulation, while restricted estimation produces 0% by construction](../claims/unrestricted-estimation-ipr-simulation.md) [+M]
- [In a real syllogistic reasoning analysis, unrestricted estimation assigns 40.7% to 89.5% of examinees to impermissible attribute profiles depending on the CDM](../claims/real-data-impermissible-rates.md) [+M]
- [In simulations with a restricted Q-matrix design, restricted estimation yields higher pattern-wise classification agreement than unrestricted estimation across four CDMs and four attribute hierarchy structures](../claims/restricted-estimation-higher-par-simulation.md) [+M]

## Related Research Methods
-

## Key Sources
- Köhn, HF., Chiu, CY. (2019). Attribute Hierarchy Models in Cognitive Diagnosis: Identifiability of the Latent Attribute Space and Conditions for Completeness of the Q-Matrix. J Classif. https://doi.org/10.1007/s00357-018-9278-6
- Tu, D., Wang, S., Cai, Y., Douglas, J., & Chang, H.-H. (2019). Cognitive Diagnostic Models With Attribute Hierarchies: Model Estimation With a Restricted Q-Matrix Design. Applied Psychological Measurement, 43(4), 255-271. https://doi.org/10.1177/0146621618765721
