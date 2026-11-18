---
type: research-method
id: curricular-analytics-graph-based-measures-of-degree-program-complexity-blocking-delay-cent
title: "Curricular analytics: graph-based measures of degree-program complexity (blocking, delay, centrality, structural complexity)"
description: Curricular analytics is the study of academic program design and layout, in which a degree plan is translated into a directed acyclic graph of courses and prerequisites.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-16
---

# Curricular analytics: graph-based measures of degree-program complexity (blocking, delay, centrality, structural complexity)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
Curricular analytics is the study of academic program design and layout, in which a degree plan is translated into a directed acyclic graph of courses and prerequisites. From the graph, four measures are computed: blocking factor (the number of courses reachable from a course node), delay factor (the maximum number of courses that must be completed in sequential order), centrality (the sum of the delay of all paths containing that course), and structural complexity (an unweighted linear combination of delay and blocking, with overall program complexity the sum of individual course complexities). The article uses these measures to compare 60 CS degrees against representation of women graduates.

## Accounts
<!-- How each source describes or uses the method -->
- **Curricular analytics: graph-based measures of degree-program complexity (blocking, delay, centrality, structural complexity)**: Curricular analytics is the study of academic program design and layout, in which a degree plan is translated into a directed acyclic graph of courses and prerequisites. From the graph, four measures are computed: blocking factor (the number of courses reachable from a course node), delay factor (the maximum number of courses that must be completed in sequential order), centrality (the sum of the delay of all paths containing that course), and structural complexity (an unweighted linear combination of delay and blocking, with overall program complexity the sum of individual course complexities). The article uses these measures to compare 60 CS degrees against representation of women graduates. (Does Curricular Complexity in Computer Science Influence the Representation of Women CS Gr)
- **Combined data-mining framework for uncovering key courses in an academic curriculum**: The article proposes a framework combining three methods applied to a students-by-courses grade matrix: (a) observing course positions in the maximal spanning tree of the correlation network, (b) computing course mean scores and variances, and (c) computing courses' contributions to the first principal component. When outcomes from these methods agree, the framework identifies central and differentiating courses. The authors suggest it "can be used at Universities and at other schools as as an additional tool to optimize teaching strategies since it does not need a priori knowledge of assumed curriculum aims." (L. Gajewski et al. (2016))

### Claims
- [CS programs with higher structural curricular complexity have lower representation of women graduates (ANOVA across three representation groups)](../claims/cs-curricular-complexity-inversely-related-women-representation.md) [+M]
- [Blocking factors of CS 1 and CS 2 differ significantly across women-representation groups, with lower-blocking programs having higher representation of women](../claims/cs1-cs2-blocking-factor-differs-by-women-representation.md) [+M]
- [The authors' data supports that Calculus 1 need not be a prerequisite for lower-level CS courses](../claims/calculus1-need-not-prerequisite-lower-level-cs.md) [+W]
- [A triple of first- and second-semester courses (FP1, FP2, AG) forms the central hub of the course-correlation network](../claims/central-courses-fp1-fp2-ag-mst-hubs.md) [+M]
- [A differentiating group of courses (QP, MA2, MA3, PL) contributes significantly to score variance and separates students](../claims/differentiating-courses-qp-ma2-ma3-pl.md) [+M]

## Related Research Methods

- [Diffusion-based centrality framework for measuring uptake in CSCL discourse](diffusion-based-centrality-framework-for-measuring-uptake-in-cscl-discourse.md)
- [Principal-component course-significance analysis for empirical credit allocation](principal-component-course-significance-analysis-for-empirical-credit-allocation.md)

## Key Sources
- Albert Lionelle, McKenna Quam, Carla Brodley, and Catherine Gill. 2024. Does Curricular Complexity in Computer Science Influence the Representation of Women CS Graduates?. In Proceedings of the 55th ACM Technical Symposium on Computer Science Education V. 1 (SIGCSE 2024). https://doi.org/10.1145/3626252.3630835
- L. Gajewski, J. Chołoniewski, J. A. Hołyst. (2016). Key courses of academic curriculum uncovered by data mining of students' grades. arXiv preprint. https://arxiv.org/abs/1604.07074
