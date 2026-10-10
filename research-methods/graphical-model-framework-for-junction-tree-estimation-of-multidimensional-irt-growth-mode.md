---
type: research-method
id: graphical-model-framework-for-junction-tree-estimation-of-multidimensional-irt-growth-mode
title: Graphical model framework for junction-tree estimation of multidimensional IRT growth models
description: The article presents a framework in which a statistical model is represented as a directed acyclic graph, moralized, triangulated, and converted into a junction tree whose cliques define conditionally independent subsets of latent variables.
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: rijmen-2010
    resource: "https://www.ets.org/research/contact.html"
    title: "Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html"
    author: Rijmen, F
---

# Graphical model framework for junction-tree estimation of multidimensional IRT growth models

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article presents a framework in which a statistical model is represented as a directed acyclic graph, moralized, triangulated, and converted into a junction tree whose cliques define conditionally independent subsets of latent variables. The author states that "the computational complexity of a multidimensional model is inversely related to the number of conditional independence relations one is willing to assume." The framework provides algorithms to partition the joint latent space so that brute force integration can be replaced by local computations on cliques, applied to a family of multidimensional IRT growth models.

## Accounts
<!-- How each source describes or uses the method -->
- **Graphical model framework for exploiting conditional independence to make multidimensional IRT estimation tractable**: The article presents a framework in which a statistical model is represented as a directed acyclic graph, moralized, triangulated, and converted into a junction tree whose cliques define conditionally independent subsets of latent variables. The author states that "the computational complexity of a multidimensional model is inversely related to the number of conditional independence relations one is willing to assume." The framework provides algorithms to partition the joint latent space so that brute force integration can be replaced by local computations on cliques, applied to a family of multidimensional IRT growth models. (Rijmen (2010))

### Claims
- [Junction-tree factorization reduces EM algorithm complexity for latent growth IRT models from exponential to linear in the number of measurement occasions](../claims/junction-tree-em-linear-complexity-occasions.md) [+W]

## Related Research Methods
-

## Key Sources
- Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html

<!-- merged 2026-10-10 from theories/graphical-model-framework-multidimensional-irt-complexity ("Graphical model framework for exploiting conditional independence to make multidimensional IRT estimation tractable"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Graphical model framework for exploiting conditional independence to make multidimensional IRT estimation tractable

> **Theory** · [All theories](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article presents a framework in which a statistical model is represented as a directed acyclic graph, moralized, triangulated, and converted into a junction tree whose cliques define conditionally independent subsets of latent variables. The author states that "the computational complexity of a multidimensional model is inversely related to the number of conditional independence relations one is willing to assume." The framework provides algorithms to partition the joint latent space so that brute force integration can be replaced by local computations on cliques, applied to a family of multidimensional IRT growth models.

## Design Implications

### Context
#### Requirements
- The researcher must be willing to incorporate conditional independence assumptions on the latent structure, such as bifactor or higher-order structure within occasions and a first-order Markov assumption across occasions
#### Constraints
- The results require latent variables to be discrete, so continuous latent variables are handled as discrete approximations equivalent to numerical integration over a grid

### Target Learners
- K-12 and other examinees assessed repeatedly over time in longitudinal educational measurement programs

### Target Learning Objectives
- Measurement of growth on multidimensional achievement constructs

### Claims

- [Junction-tree factorization reduces EM algorithm complexity for latent growth IRT models from exponential to linear in the number of measurement occasions](../claims/junction-tree-em-linear-complexity-occasions.md) [+W]

## Related Theories

- [Graphical model framework for deriving efficient MML estimation schemes for multidimensional IRT models](../research-methods/graphical-model-framework-for-mml-estimation-of-multidimensional-irt-models.md)

## Examples
-

## Key Sources
- Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html
-->
