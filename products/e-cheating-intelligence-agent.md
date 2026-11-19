---
type: product
id: e-cheating-intelligence-agent
title: E-cheating intelligence agent
description: A software system developed by Leslie Ching Ow Tiong et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# E-cheating intelligence agent

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
A software system developed by Leslie Ching Ow Tiong et al. that combines IP-address monitoring with deep-learning analysis of online-examination behaviour to flag suspected cheating and issue warnings or alter question delivery.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **E-cheating intelligence agent combining an IP detection agent and a deep-learning behaviour detection agent**: The e-cheating intelligence agent is a monitoring system for online examinations composed of two modules. As the article states, "The e-cheating intelligence agent consists of two main agents: the network IP detection agent (described in Section III-A) and the behaviour detection agent (described in Section III-B)." The rule-based IP agent monitors candidates' IP addresses and alerts the system if a student changes device or location, while the deep-learning behaviour agent monitors answering behaviour and can trigger question reassignment and warning messages when abnormal behaviour is detected. (Leslie Ching Ow Tiong et al. (2021))
- **E-cheating intelligent agent framework combining an IP detector and a deep-learning behavioural monitor**: The article proposes an e-cheating intelligent agent with two components: a rule-based network IP detector that monitors IP addresses and reassigns randomised question sets when a suspicious address is detected, and a deep-learning behavioural monitor that scans assessment responses for irregularities and, when triggered, alerts invigilators and reassigns remaining questions. The authors state this combination of techniques "has never been attempted in literature to the best of our knowledge". The framework is applied to remote online assessments lacking conventional invigilation. (Leslie Ching Ow Tiong et al. (2022))

### Claims
- [DenseLSTM achieves the highest overall accuracy of 95.32% for detecting abnormal student behaviour at online examinations, outperforming LSTM, RNN and DNN benchmarks](../claims/denselstm-highest-overall-accuracy-95-32.md) [+M]
- [DenseLSTM achieves the highest classification accuracy of the tested networks, 90.72% overall, outperforming LSTM, RNN and DNN benchmarks on the PT Behavioural Database](../claims/denselstm-highest-accuracy-90-72-overall.md) [+M]
- [Suspected IP addresses in the test sets originate from geographically similar locations, and fewer than 10 cases were flagged per test set](../claims/suspected-ips-geographically-similar-locations.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Leslie Ching Ow Tiong and HeeJeong Jasmine Lee. (2021). E-cheating Prevention Measures: Detection of Cheating at Online Examinations Using Deep Learning Approach - A Case Study. https://arxiv.org/abs/2101.09841
- Leslie Ching Ow Tiong, HeeJeong Jasmine Lee, Kai Li Lim. (2022). Online Assessment Misconduct Detection using Internet Protocol and Behavioural Classification. arXiv preprint. https://arxiv.org/abs/2201.13226
