---
type: strategy
id: multi-perspective-surgical-skill-assessment-strategy
title: Combine subjective scores, simulator metrics and EEG-based cognitive-load measures for multi-perspective skill assessment
description: "The article recommends assessing robotic surgical skill with multiple complementary measures rather than one score: GEARS video ratings, objective dVSS simulator scores, NASA TLX workload self-ratings, and EEG power s..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
sources:
  - id: wang-rong-2025
    resource: "https://doi.org/10.1007/s11701-025-02309-1"
    title: "Wang Rong, Zheng Nan, Liang Yujing, Cui Haoxin, Ren Tong, Xing Wenhui, Li Yanghui. (2025). Multi-perspective analysis of daVinci surgical virtual reality training: a prospective randomized controlled study. Journal of Robotic Surgery. https://doi.org/10.1007/s11701-025-02309-1"
    author: Wang Rong, Zheng Nan, Liang Yujing, Cui Haoxin, Ren Tong, Xing Wenhui, Li Yanghui
---

# Combine subjective scores, simulator metrics and EEG-based cognitive-load measures for multi-perspective skill assessment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (7 for) · 2 studies (1 causal, 1 review), `q2`–`q3` · 0 of 2 report an effect size · 7 claims rest on one study

## Description
The article recommends assessing robotic surgical skill with multiple complementary measures rather than one score: GEARS video ratings, objective dVSS simulator scores, NASA TLX workload self-ratings, and EEG power spectral density. It states "more in-depth objective EEG analyses provide mental-level evidence for evaluating the effectiveness of operational training", and that combining the three scores is more reliable than a single score.

## Design Implications

### Context
#### Requirements
- Access to the dVSS simulator scoring system, GEARS-trained raters and operation video recordings
- EEG equipment and analysis toolchains (EEGLAB, MNE) for power spectral density estimation
#### Constraints
- The authors note subjective scores may not fully represent task load or mastery, and the simulator score does not simulate the real surgical environment

### Target Learners
- surgical trainees (residents and fellows) in robotic surgery programs

### Target Learning Goals
- technical skill assessment
- nontechnical skill (cognitive load) assessment in robotic surgery training

## Claims

- [Trainees' performance plateaus by the fifth training attempt on the dVSS simulator](../claims/dvss-learning-curve-plateau-fifth-attempt.md) [+W]
- [VR-training group outperforms controls on dVSS simulator objective scores for most tasks](../claims/dvss-objective-scores-training-group-outperforms.md) [+W]
- [VR-trained group shows higher beta and low-gamma EEG power than controls during simulator tasks](../claims/dvss-vr-training-higher-beta-low-gamma-psd.md) [+W]
- [VR-training group achieves higher GEARS-assessed basic robotic surgical skill than untrained controls (24.91 ± 3.36 vs. 19.68 ± 3.07)](../claims/dvss-vr-training-higher-gears-scores.md) [+W]
- [VR-trained participants perform with lower NASA-TLX workload than controls (40.04 ± 10.55 vs. 48.2 ± 9.88)](../claims/dvss-vr-training-lower-nasa-tlx-workload.md) [+W]
- [Prior surgical experience shows no significant advantage for basic robotic surgical skill acquisition](../claims/surgical-experience-no-gears-advantage.md) [+W]
- [Cognitive and behavioral metrics via EEG and eye-tracking with machine learning predicted surgical training outcomes with 72.5% accuracy](../claims/eeg-eye-metrics-ml-predict-training-outcomes.md) [+W]

## Related Strategies

- [Combine objective metrics with validated subjective tools and audio-visual recording to contextualize interpretation of surgical performance data](combine-objective-metrics-with-subjective-and-av-context.md)
- [Pair convenient platform analytics with transparent, education-specific evaluation criteria rather than trusting either alone](pair-platform-analytics-with-transparent-criteria.md)
- [Use performance thresholds that meaningfully measure surgeon performance alongside standardized terminology when assessing surgical learning curves](meaningful-thresholds-standardized-terminology-learning-curves.md)
- [Use validated EEG and eye-tracking models to provide objective, expert-free performance and learning-rate feedback in surgical residency training](eeg-eye-tracking-objective-ras-training-assessment.md)

## Examples
-

## Key Sources
- Wang Rong, Zheng Nan, Liang Yujing, Cui Haoxin, Ren Tong, Xing Wenhui, Li Yanghui. (2025). Multi-perspective analysis of daVinci surgical virtual reality training: a prospective randomized controlled study. Journal of Robotic Surgery. https://doi.org/10.1007/s11701-025-02309-1
