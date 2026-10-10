---
type: product
id: psychology-mooc-gt-spring-2013-dataset
title: Psychology MOOC GT - Spring 2013 dataset
description: "A PSLC DataShop dataset containing learner response and skill-tagging data from the Open Learning Initiative's Psychology MOOC GT Spring 2013 course."
product_kind: dataset
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: martori-2015
    resource: "https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    title: "Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    author: "Martori, F., Cuadros, J., & González-Sabaté, L"
---

# Psychology MOOC GT - Spring 2013 dataset

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A PSLC DataShop dataset containing learner response and skill-tagging data from the Open Learning Initiative's Psychology MOOC GT Spring 2013 course.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Psychology MOOC GT Spring 2013 dataset (OLI, via PSLC DataShop)**: A dataset from the 'Psychology MOOC GT - Spring 2013' course, accessed via DataShop (pslcdatashop.org). The course was designed by the Open Learning Initiative (OLI), known for data-driven design, which the authors say ensures skills were properly tagged. It contains data from 5615 students who issued around 2 million first attempt answers, with 226 different skills identified. Skills tagged in fewer than 4 different questions were discarded, leaving 103 skills for training and evaluating the RSS-estimation model. (Martori et al. (2015))

### Claims
- [A linear regression on skill variables (n, dim, pc) predicts the minimum RSS value for BKT-BF training with high predictive ability](../claims/linear-regression-predicts-minimum-rss-bkt-bf.md) [+W]
- [In a preliminary PCA, RMSE is highly correlated with the slip parameter S, while T and G appear orthogonal to RMSE](../claims/pca-rmse-correlates-slip-orthogonal-t-g.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf

<!-- merged 2026-10-10 from elements/psychology-mooc-gt-spring-2013-datashop-dataset ("Psychology MOOC GT Spring 2013 dataset (OLI, via PSLC DataShop)"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Psychology MOOC GT Spring 2013 dataset (OLI, via PSLC DataShop)

> **Element** · [All elements](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A dataset from the 'Psychology MOOC GT - Spring 2013' course, accessed via DataShop (pslcdatashop.org). The course was designed by the Open Learning Initiative (OLI), known for data-driven design, which the authors say ensures skills were properly tagged. It contains data from 5615 students who issued around 2 million first attempt answers, with 226 different skills identified. Skills tagged in fewer than 4 different questions were discarded, leaving 103 skills for training and evaluating the RSS-estimation model.

## Design Implications

### Context
#### Requirements
- Access via DataShop (pslcdatashop.org)
- Skill tagging metadata (skills map)
#### Constraints
- Skills tagged in less than 4 different questions (dim<4) were discarded in this study

### Target Learners
- MOOC students in the OLI psychology course

### Target Learning Goals
- student modeling and knowledge inference research on skill-tagged response data

### Claims
<!- - Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] - ->
- [A linear regression on skill variables (n, dim, pc) predicts the minimum RSS value for BKT-BF training with high predictive ability](../claims/linear-regression-predicts-minimum-rss-bkt-bf.md) [+W]
- [In a preliminary PCA, RMSE is highly correlated with the slip parameter S, while T and G appear orthogonal to RMSE](../claims/pca-rmse-correlates-slip-orthogonal-t-g.md) [+W]

## Related Elements

- [PSLC DataShop public repository of online learning data](../products/pslc-datashop.md)

## Examples
-

## Key Sources
- Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf
-->
