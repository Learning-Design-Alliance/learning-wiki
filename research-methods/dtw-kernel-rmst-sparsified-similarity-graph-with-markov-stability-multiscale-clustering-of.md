---
type: research-method
id: dtw-kernel-rmst-sparsified-similarity-graph-with-markov-stability-multiscale-clustering-of
title: DTW-kernel, RMST-sparsified similarity graph with Markov Stability multiscale clustering of learner time-series
description: A three-stage unsupervised framework for analysing online learner temporal behaviour.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-26
---

# DTW-kernel, RMST-sparsified similarity graph with Markov Stability multiscale clustering of learner time-series

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
A three-stage unsupervised framework for analysing online learner temporal behaviour. A dynamic time warping kernel computes pairwise similarity between raw time-series: "Our method uses a dynamic time warping similarity kernel to generate a sparsified similarity graph between learners, to which we apply a multiscale graph partitioning algorithm". RMST sparsification retains strong, globally relevant edges; Markov Stability scans Markov time to find robust partitions at all resolutions without pre-imposing cluster number or type, yielding a quasi-hierarchy from 10 down to 2 clusters that the analyst can choose from.

## Accounts
<!-- How each source describes or uses the method -->
- **DTW-kernel, RMST-sparsified similarity graph with Markov Stability multiscale clustering of learner time-series**: A three-stage unsupervised framework for analysing online learner temporal behaviour. A dynamic time warping kernel computes pairwise similarity between raw time-series: "Our method uses a dynamic time warping similarity kernel to generate a sparsified similarity graph between learners, to which we apply a multiscale graph partitioning algorithm". RMST sparsification retains strong, globally relevant edges; Markov Stability scans Markov time to find robust partitions at all resolutions without pre-imposing cluster number or type, yielding a quasi-hierarchy from 10 down to 2 clusters that the analyst can choose from. (Peach et al. (2019))

### Claims
- [Low-performing learners concentrate in the massed-learning ('Crammers') cluster, with 6 of 7 low performers in that cluster in the main cohort](../claims/low-performers-concentrate-massed-learning-cluster.md) [+M]
- [Unsupervised time-series clustering identifies low performers more accurately than SVM or decision-tree classifiers trained on two temporal statistics](../claims/unsupervised-clustering-beats-feature-classifiers.md) [+M]
- [Bayes factors on Gaussian-process trajectories show each behavioural cluster is statistically distinct from the others](../claims/gpr-bayes-factors-cluster-distinctness.md) [+M]
- [The methodology replicates on a second cohort of 46 learners, with only 1 of 8 low performers in the distributed-learning cluster](../claims/second-cohort-replication-massed-low-performance.md) [+M]
- [On the OULAD page-click dataset, 6 of 7 low performers fall in the massed-learning cluster, whose grade is significantly lower than the distributed cluster (paired t-test at 5%)](../claims/oulad-massed-cluster-low-performers.md) [+M]

## Related Research Methods
-

## Key Sources
- Peach, R. L., Yaliraki, S. N., Lefevre, D. and Barahona, M. (2019). Data-driven unsupervised clustering of online learner behaviour. npj Science of Learning 4:14. https://doi.org/10.1038/s41539-019-0054-0
