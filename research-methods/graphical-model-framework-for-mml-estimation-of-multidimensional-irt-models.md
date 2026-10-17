---
type: research-method
id: graphical-model-framework-for-mml-estimation-of-multidimensional-irt-models
aliases: [graphical-model-framework-for-junction-tree-estimation-of-multidimensional-irt-growth-mode]
title: Graphical model framework for MML estimation of multidimensional IRT models
description: The article presents a framework in which a multidimensional IRT model is represented as a directed acyclic graph whose nodes are random variables and whose edges encode conditional (in)dependence relations.
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: rijmen-2009
    resource: "http://www.ets.org/research/contact.html"
    title: "Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html"
    author: Rijmen, F
  - id: rijmen-2010
    resource: "https://www.ets.org/research/contact.html"
    title: "Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html"
    author: Rijmen, F
---

# Graphical model framework for MML estimation of multidimensional IRT models

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article presents a framework in which a multidimensional IRT model is represented as a directed acyclic graph whose nodes are random variables and whose edges encode conditional (in)dependence relations. The DAG is moralized, triangulated, and transformed into a junction tree, and the E-step of the EM algorithm is carried out via local computations on the tree. A stated advantage is that "these subsets of variables can be derived in a fully automatic way by applying algorithms to the graphical representation of the model", making the approach generally applicable and rendering hand derivations obsolete.

## Accounts
<!-- How each source describes or uses the method -->
- **Graphical model framework for deriving efficient MML estimation schemes for multidimensional IRT models**: The article presents a framework in which a multidimensional IRT model is represented as a directed acyclic graph whose nodes are random variables and whose edges encode conditional (in)dependence relations. The DAG is moralized, triangulated, and transformed into a junction tree, and the E-step of the EM algorithm is carried out via local computations on the tree. A stated advantage is that "these subsets of variables can be derived in a fully automatic way by applying algorithms to the graphical representation of the model", making the approach generally applicable and rendering hand derivations obsolete. (Rijmen (2009))
- **Graphical model framework for exploiting conditional independence to make multidimensional IRT estimation tractable**: The article presents a framework in which a statistical model is represented as a directed acyclic graph, moralized, triangulated, and converted into a junction tree whose cliques define conditionally independent subsets of latent variables. The author states that "the computational complexity of a multidimensional model is inversely related to the number of conditional independence relations one is willing to assume." The framework provides algorithms to partition the joint latent space so that brute force integration can be replaced by local computations on cliques, applied to a family of multidimensional IRT growth models. (Rijmen (2010))

### Claims
- [Full information MML estimation of the bi-factor model requires only two-dimensional integrations under more general conditions than the probit-link, multivariate-normal derivation of Gibbons and Hedeker](../claims/mml-bifactor-two-dimensional-integrals-general-conditions.md) [+M]
- [Computational complexity of the graph-based MML procedure scales with the number of latent variables within a conditionally independent subset, and brute-force integration scales exponentially with dimensionality](../claims/mml-complexity-scales-with-clique-state-spaces.md) [+M]
- [Full information MML estimation of a multidimensional IRT model with a second-order dimension also requires only two-dimensional integrals](../claims/mml-second-order-dimension-two-dimensional-integrals.md) [+W]

## Related Research Methods
-

## Key Sources
- Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html. [doi:10.1002/j.2333-8504.2009.tb02160.x](https://doi.org/10.1002/j.2333-8504.2009.tb02160.x)
- Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html

<!-- merged 2026-10-10 from theories/graphical-model-framework-mml-irt-estimation ("Graphical model framework for deriving efficient MML estimation schemes for multidimensional IRT models"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Graphical model framework for deriving efficient MML estimation schemes for multidimensional IRT models

> **Theory** · [All theories](index.md)
> **Evidence** · 6 claims (5 for, 1 against) · 2 studies (2 theoretical), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The article presents a framework in which a multidimensional IRT model is represented as a directed acyclic graph whose nodes are random variables and whose edges encode conditional (in)dependence relations. The DAG is moralized, triangulated, and transformed into a junction tree, and the E-step of the EM algorithm is carried out via local computations on the tree. A stated advantage is that "these subsets of variables can be derived in a fully automatic way by applying algorithms to the graphical representation of the model", making the approach generally applicable and rendering hand derivations obsolete.

## Design Implications

### Context
#### Requirements
- The statistical model must be representable as a directed acyclic graph, with latent variables approximated by discrete latent variables when continuous parents would have discrete children
- Conditional independence relations must be imposed by the model structure for the efficiency gains to materialize
#### Constraints
- A thorough account of the graph theory behind the general procedure is stated to be outside the scope of the paper, with main results given without proof
- Finding an optimal triangulation is NP-hard, though well performing heuristic algorithms are available

### Target Learners
- Educational measurement researchers and psychometricians estimating multidimensional IRT models

### Target Learning Objectives
- Efficient, feasible estimation of parameters of structured multidimensional item response theory models

### Claims

- [Mml Bifactor Two Dimensional Integrals General Conditions](../claims/mml-bifactor-two-dimensional-integrals-general-conditions.md) [+M]
- [Mml Complexity Scales With Clique State Spaces](../claims/mml-complexity-scales-with-clique-state-spaces.md) [+M]
- [Full information MML estimation of a multidimensional IRT model with a second-order dimension also requires only two-dimensional integrals](../claims/mml-second-order-dimension-two-dimensional-integrals.md) [+W]

## Related Theories

- [Graphical model framework for exploiting conditional independence to make multidimensional IRT estimation tractable](graphical-model-framework-for-mml-estimation-of-multidimensional-irt-models.md)
- [Item Response Theory as a framework for scale development](../theories/irt-framework-scale-development.md)
- [Graphical modeling as learning the conditional dependence structure of multivariate relations](../theories/graphical-modeling-conditional-dependence-framework.md)

## Examples

- [Bayes Net Toolbox for Matlab used to carry out graph transformations algorithmically](../products/bayes-net-toolbox-for-matlab.md)
- [BNL (Bayesian networks with logistic regression nodes)](../products/bnl-bayesian-networks-with-logistic-regression-nodes.md)
- [Explore candidate models with limited-information estimation first, then estimate the structured model with the efficient EM algorithm](../strategies/limited-information-then-efficient-em-sequential-procedure.md)

## Key Sources
- Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html. [doi:10.1002/j.2333-8504.2009.tb02160.x](https://doi.org/10.1002/j.2333-8504.2009.tb02160.x)
-->

<!-- merged 2026-10-17 from research-methods/graphical-model-framework-for-junction-tree-estimation-of-multidimensional-irt-growth-mode ("Graphical model framework for junction-tree estimation of multidimensional IRT growth models"), thin research-method page folded into the method it is a variant of (maintainer, 2026-10-17): its body as it stood. Its bullets this page lacked were added above.

# Graphical model framework for junction-tree estimation of multidimensional IRT growth models

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
The article presents a framework in which a statistical model is represented as a directed acyclic graph, moralized, triangulated, and converted into a junction tree whose cliques define conditionally independent subsets of latent variables. The author states that "the computational complexity of a multidimensional model is inversely related to the number of conditional independence relations one is willing to assume." The framework provides algorithms to partition the joint latent space so that brute force integration can be replaced by local computations on cliques, applied to a family of multidimensional IRT growth models.

## Accounts
<!- - How each source describes or uses the method - ->
- **Graphical model framework for exploiting conditional independence to make multidimensional IRT estimation tractable**: The article presents a framework in which a statistical model is represented as a directed acyclic graph, moralized, triangulated, and converted into a junction tree whose cliques define conditionally independent subsets of latent variables. The author states that "the computational complexity of a multidimensional model is inversely related to the number of conditional independence relations one is willing to assume." The framework provides algorithms to partition the joint latent space so that brute force integration can be replaced by local computations on cliques, applied to a family of multidimensional IRT growth models. (Rijmen (2010))

### Claims

## Related Research Methods
-

## Key Sources
- Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html

<!- - merged 2026-10-10 from theories/graphical-model-framework-multidimensional-irt-complexity ("Graphical model framework for exploiting conditional independence to make multidimensional IRT estimation tractable"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

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


## Related Theories

- [Graphical model framework for deriving efficient MML estimation schemes for multidimensional IRT models](../research-methods/graphical-model-framework-for-mml-estimation-of-multidimensional-irt-models.md)

## Examples
-

## Key Sources
- Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html
- ->
-->
