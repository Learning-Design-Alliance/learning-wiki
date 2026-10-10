---
type: product
id: kdd-cup-2010-bridge-to-algebra-dataset
title: KDD Cup 2010 Bridge to Algebra dataset
description: A Carnegie Learning–donated dataset distributed through the PSLC DataShop containing large-scale student interaction records from mathematics curriculum practice for educational data-mining and knowledge-tracing research.
product_kind: dataset
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: falakmasir-2015
    resource: "http://pslcdatashop.web.cmu.edu/KDDCup"
    title: "Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup"
    author: "Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K"
---

# KDD Cup 2010 Bridge to Algebra dataset

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
A Carnegie Learning–donated dataset distributed through the PSLC DataShop containing large-scale student interaction records from mathematics curriculum practice for educational data-mining and knowledge-tracing research.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **KDD Cup 2010 Bridge to Algebra dataset and the hmmsclbl fitting tool**: The KDD Cup 2010 Bridge to Algebra dataset, donated by Carnegie Learning and downloadable from the PSLC DataShop, is the validation corpus for Spectral BKT. It "contains about 20 million transactions belonging to over 6 thousand students working on nearly 150 sections of mathematics curriculum practicing around 1650 skills", including curriculum and problem context, cognitive skill labels, timing, first-attempt correctness, and assistance information. The authors describe it as the largest freely available collection of learner data. Models were fit and cross-validated with hmmsclbl, a C/C++ utility available at the standard-bkt GitHub repository. (Falakmasir et al. (2015))

### Claims
- [Spectral BKT achieves higher prediction accuracy than standard BKT on the KDD Cup 2010 Bridge to Algebra data, reaching 92% accuracy](../claims/spectral-bkt-beats-standard-bkt-accuracy-kdd2010.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup

<!-- merged 2026-10-10 from elements/kdd-cup-2010-bridge-to-algebra-dataset ("KDD Cup 2010 Bridge to Algebra dataset and the hmmsclbl fitting tool"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# KDD Cup 2010 Bridge to Algebra dataset and the hmmsclbl fitting tool

> **Element** · [All elements](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
The KDD Cup 2010 Bridge to Algebra dataset, donated by Carnegie Learning and downloadable from the PSLC DataShop, is the validation corpus for Spectral BKT. It "contains about 20 million transactions belonging to over 6 thousand students working on nearly 150 sections of mathematics curriculum practicing around 1650 skills", including curriculum and problem context, cognitive skill labels, timing, first-attempt correctness, and assistance information. The authors describe it as the largest freely available collection of learner data. Models were fit and cross-validated with hmmsclbl, a C/C++ utility available at the standard-bkt GitHub repository.

## Design Implications

### Context
#### Requirements
- Skills are treated as unique within each curriculum section, with null skills treated as a special skill
#### Constraints
- Only the Bridge to Algebra dataset of the two available KDD Cup 2010 datasets was used

### Target Learners
- middle-grade mathematics students using Carnegie Learning's Cognitive Tutor

### Target Learning Goals
- predicting student correctness on math problem steps and modeling skill mastery

### Claims
<!- - Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] - ->
- [Spectral BKT achieves higher prediction accuracy than standard BKT on the KDD Cup 2010 Bridge to Algebra data, reaching 92% accuracy](../claims/spectral-bkt-beats-standard-bkt-accuracy-kdd2010.md) [+M]

## Related Elements

- [Four large-scale real-world sequential knowledge tracing benchmark datasets used to evaluate Adaptive G-UKT](../elements/adaptive-g-ukt-benchmark-datasets.md)
- [PSLC DataShop public repository of online learning data](pslc-datashop.md)

## Examples
-

## Key Sources
- Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup
-->
