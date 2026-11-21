---
type: research-method
id: cosine-similarity-framework
moved_from: [theory/cosine-similarity-item-test-parameter-framework]
title: Cosine similarity framework
description: The article introduces an angular-statistics framework in which item and test difficulty and discriminating values are obtained from the cosine of the angle between the observed score vector and the maximum possible score vector, involving inner products and vector lengths.
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: chakrabartty-2021
    resource: "https://dx.doi.org/10.52380/ijpes.2021.8.3.190"
    title: "Chakrabartty, S. N. (2021). Assessment of item and test parameters: Cosine similarity approach. International Journal of Psychology and Educational Studies, 8(3), 28-38. https://dx.doi.org/10.52380/ijpes.2021.8.3.190"
    author: Chakrabartty, S. N
---

# Cosine similarity framework

> **Research Method** · [All research methods](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 2 studies (1 causal, 1 theoretical), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The article introduces an angular-statistics framework in which item and test difficulty and discriminating values are obtained from the cosine of the angle between the observed score vector and the maximum possible score vector, involving inner products and vector lengths. It states that "This gives the novel area of angular statistics where Cosθ gives similarity between two vectors of same dimension." The framework uses the entire data, requires no assumption of continuity, linearity or normality, and yields difficulty and discrimination measures bounded between 0 and 1.

## Accounts
<!-- How each source describes or uses the method -->
- **Cosine similarity framework for item and test parameters under classical test theory**: The article introduces an angular-statistics framework in which item and test difficulty and discriminating values are obtained from the cosine of the angle between the observed score vector and the maximum possible score vector, involving inner products and vector lengths. It states that "This gives the novel area of angular statistics where Cosθ gives similarity between two vectors of same dimension." The framework uses the entire data, requires no assumption of continuity, linearity or normality, and yields difficulty and discrimination measures bounded between 0 and 1. (Chakrabartty (2021))
- **Embedding-based alignment-ranking framework for evaluating educational resources against intended learning outcomes**: The framework ranks educational resources by their alignment with intended learning outcomes using text-embedding models. Because identifying teachers' intended learning outcomes was not always feasible, transcripts of accepted resources serve as proxies for outcomes; candidate resources are ranked by "Cosine similaritybetween embedding vectors", with segment-wise embeddings averaged for long transcripts. Ranking quality is scored with a metric "inspired by Kendall's tau", counting correctly resolved accepted-rejected pairs, complemented by Precision@k (k=3, k=5). The framework was applied both to existing YouTube resources and to LLM-generated content, supporting automated, cost-effective alignment verification so teachers can focus on learner needs. (Molavi et al. (2025))

### Claims
- [Test difficulty value defined as ratio of observed to maximum score vector length times cosine of their angle equals test mean divided by number of items](../claims/test-difficulty-value-cosine-definition.md) [+M]
- [Item discriminating value as coefficient of variation decreases monotonically as number of correct answers increases, giving a negative difficulty–discrimination relationship](../claims/item-discrimination-cv-negative-difficulty-relation.md) [+M]
- [Test discriminating value equals the coefficient of variation of test scores (tan∅ = SD/mean)](../claims/test-discriminating-value-cv.md) [~W]
- [The Voyage text-embedding model outperforms other embedding models and the YouTube baseline in ranking educational resources by alignment with intended learning outcomes](../claims/voyage-embedding-best-alignment-ranking-accuracy.md) [+M]
- [Voyage-based alignment ranking reliably matches expert judgments on LLM-generated resources (0.83 average accuracy)](../claims/voyage-validated-expert-generated-resources.md) [+M]
- [Learners studying top-ranked resources performed significantly better than those studying third-ranked resources](../claims/alignment-ranked-resources-predict-learning-performance.md) [+M]

## Related Research Methods
-

## Key Sources
- Chakrabartty, S. N. (2021). Assessment of item and test parameters: Cosine similarity approach. International Journal of Psychology and Educational Studies, 8(3), 28-38. https://dx.doi.org/10.52380/ijpes.2021.8.3.190
<!-- merged 2026-10-10 from theories/cosine-similarity-item-test-parameter-framework ("Cosine similarity framework for item and test parameters under classical test theory"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor. (2025). Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance. https://arxiv.org/abs/2512.13658

# Cosine similarity framework for item and test parameters under classical test theory

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article introduces an angular-statistics framework in which item and test difficulty and discriminating values are obtained from the cosine of the angle between the observed score vector and the maximum possible score vector, involving inner products and vector lengths. It states that "This gives the novel area of angular statistics where Cosθ gives similarity between two vectors of same dimension." The framework uses the entire data, requires no assumption of continuity, linearity or normality, and yields difficulty and discrimination measures bounded between 0 and 1.

## Design Implications

### Context
#### Requirements
- A test of m binary items administered to n respondents with n > m, scored 1 for correct and 0 otherwise
#### Constraints
- The triangle inequality is not satisfied, i.e. CosθXY + CosθYZ ≥ CosθXZ is not always true for X≠Y≠Z
- IRT was not considered primarily for its requirement of large sample size and strict assumptions

### Target Learners
- examinees taking binary-item tests across educational levels

### Target Learning Objectives
- assessment of test and item quality (difficulty, discrimination, reliability)

### Claims
- [Test Difficulty Value Cosine Definition](../claims/test-difficulty-value-cosine-definition.md) [+M]
- [Item Discrimination Cv Negative Difficulty Relation](../claims/item-discrimination-cv-negative-difficulty-relation.md) [+M]

## Related Theories

- [Classical Test Theory (CTT) and its stated limitations](classical-test-theory.md)

## Examples
-

## Key Sources
- Chakrabartty, S. N. (2021). Assessment of item and test parameters: Cosine similarity approach. International Journal of Psychology and Educational Studies, 8(3), 28-38. https://dx.doi.org/10.52380/ijpes.2021.8.3.190
-->
