---
type: research-method
id: totcompute-mechanism-for-automatic-computation-of-task-dependent-timeontask-engagement-thr
title: ToTCompute mechanism for automatic computation of task-dependent TimeOnTask engagement thresholds
description: ToTCompute is a mechanism that automatically computes TimeOnTask threshold values for various game tasks using game-playing logs and EEG engagement data collected during an initial testing session.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# ToTCompute mechanism for automatic computation of task-dependent TimeOnTask engagement thresholds

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
ToTCompute is a mechanism that automatically computes TimeOnTask threshold values for various game tasks using game-playing logs and EEG engagement data collected during an initial testing session. It computes "the relative engagement changes for all participants every second (i.e., every TimeOnTask iteration)" and applies a time series linear model with an autocorrelation test, returning NA when data is random or the trend is not negative. Thresholds represent upper limits above which engagement decreases by a predefined relative change (e.g., 5, 10, 15%).

## Accounts
<!-- How each source describes or uses the method -->
- **ToTCompute mechanism for automatic computation of task-dependent TimeOnTask engagement thresholds**: ToTCompute is a mechanism that automatically computes TimeOnTask threshold values for various game tasks using game-playing logs and EEG engagement data collected during an initial testing session. It computes "the relative engagement changes for all participants every second (i.e., every TimeOnTask iteration)" and applies a time series linear model with an autocorrelation test, returning NA when data is random or the trend is not negative. Thresholds represent upper limits above which engagement decreases by a predefined relative change (e.g., 5, 10, 15%). (Ghergulescu et al. (2016))

### Claims

- [TimeOnTask threshold values computed by ToTCompute explain up to 76.2% of the variance in engagement change](../claims/totcompute-threshold-explains-engagement-change-variance.md) [+W]
- [TimeOnTask threshold values are highly task-dependent, making manual setting laborious](../claims/timeontask-thresholds-task-dependent.md) [+W]

## Related Research Methods

- [Non-disturbing engagement monitoring via game-play interaction logging and physiological sensing](non-disturbing-engagement-monitoring-via-game-play-interaction-logging-and-physiological-s.md)

## Key Sources
- Ghergulescu, I. & Muntean, C. H. (2016). ToTCompute: A Novel EEG-Based TimeOnTask Threshold Computation Mechanism for Engagement Modelling and Monitoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0111-2
