---
type: research-method
id: fake-learner-detection-algorithms-for-cuma-and-unauthorized-collaboration-in-moocs
title: Fake-learner detection algorithms for CUMA and unauthorized collaboration in MOOCs
description: "The article uses dedicated algorithms to identify two types of fake learners: \"Copying Using Multiple Accounts (CUMA)\", where a master account receives credit while harvesting accounts collect correct answers, and unauthorized \"Collaborators\" who submit assignments together, detected using dissimila"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# Fake-learner detection algorithms for CUMA and unauthorized collaboration in MOOCs

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 associational), `q2`–`q3` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The article uses dedicated algorithms to identify two types of fake learners: "Copying Using Multiple Accounts (CUMA)", where a master account receives credit while harvesting accounts collect correct answers, and unauthorized "Collaborators" who submit assignments together, detected using dissimilarity metrics on submission timing. In the 8.MReVx course, the CUMA algorithm detects 65 master accounts out of 478 certificate earners (a lower bound), and the collaborator algorithm identifies 20 (~4%) of certificate earners.

## Accounts
<!-- How each source describes or uses the method -->
- **Fake-learner detection algorithms for CUMA and unauthorized collaboration in MOOCs.**: The article uses dedicated algorithms to identify two types of fake learners: "Copying Using Multiple Accounts (CUMA)", where a master account receives credit while harvesting accounts collect correct answers, and unauthorized "Collaborators" who submit assignments together, detected using dissimilarity metrics on submission timing. In the 8.MReVx course, the CUMA algorithm detects 65 master accounts out of 478 certificate earners (a lower bound), and the collaborator algorithm identifies 20 (~4%) of certificate earners. (Alexandron et al. (2019))
- **Five-filter CAMEO detection algorithm using clickstream timestamp distributions**: A detection algorithm that considers all ordered pairs of accounts as candidate harvester–master pairs and applies five conjunctive filters: a Bayesian criterion requiring 90% confidence that the proportion of positive Δt values exceeds 0.9; a 90th-percentile Δt cutoff of 5 minutes; certified master with uncertified harvester; shared IP address via transitive closure of modal IPs and usernames; and exclusion of groups with 10 or more accounts sharing a modal IP. The algorithm "is comprised of five filters with highly conservative cutoffs intended to reduce false positives." (Northcutt et al. (2015))
- **CAMEO detection algorithm: IP-group linkage plus multi-filter time-series analysis of clickstream logs**: The article operationalizes CAMEO as a temporal pattern detectable in edX clickstream logs. The cornerstone is that accounts operated by the same person share an IP address: "Our algorithm searches for CAMEO only between user accounts that share the same IP address at some point during the course." Within IP groups, the two-step algorithm collects master:harvester event pairs (harvester obtained or viewed the answer within 24 hours before the master's correct submission), then applies six filters (harvester earns no certificate, at least 10 questions, more than 5% of master's correct submissions harvested, inhumanly fast submissions, harvester works for the master, no mutual master/harvester behavior) to remove false positives. (Alexandron et al. (2017))

### Claims
- [Fake learners spent significantly less time on each type of instructional resource than true learners in the MITx 8.MReVx MOOC.](../claims/fake-learners-less-time-on-instructional-resources.md) [+M]
- [About 12.9% of certificate earners in an introductory physics MOOC used CAMEO to obtain more than 1% of their correct answers, and 3.7% obtained the majority](../claims/cameo-prevalence-certificate-earners.md) [+M]

## Related Research Methods
-

## Key Sources
- Alexandron, G., Yoo, L. Y., Ruipérez-Valiente, J. A., Lee, S., & Pritchard, D. E. (2019). Are MOOC Learning Analytics Results Trustworthy? With Fake Learners, They Might Not Be! International Journal of Artificial Intelligence in Education, 29, 484–506. https://doi.org/10.1007/s40593-019-00183-1
- Northcutt, C. G., Ho, A. D., & Chuang, I. L. (2015). Detecting and Preventing “Multiple-Account” Cheating in Massive Open Online Courses. *arXiv preprint* arXiv:1508.05699. https://doi.org/10.48550/arxiv.1508.05699
- Alexandron, G., Ruipérez-Valiente, J. A., Chen, Z., Muñoz-Merino, P. J., Pritchard, D. E. (2017). Copying@Scale: Using Harvesting Accounts for Collecting Correct Answers in a MOOC. Computers & Education, 108, 96-114. https://doi.org/10.1016/j.compedu.2017.01.015
