---
type: research-method
id: strategy-based-temporal-analytics-framework-for-stealth-assessment-using-lstm-evidence-mod
title: Strategy-based temporal analytics framework for stealth assessment using LSTM evidence models
description: "A stealth assessment framework that derives temporal evidence from students' dynamic in-game strategy use rather than only from ECD evidence modeling."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-16
---

# Strategy-based temporal analytics framework for stealth assessment using LSTM evidence models

> **Research Method** · [All research methods](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
A stealth assessment framework that derives temporal evidence from students' dynamic in-game strategy use rather than only from ECD evidence modeling. Student flip sequences are encoded as n-grams, clustered per task with EM clustering to yield strategy labels, and sequences of strategy cluster memberships across consecutive tasks are fed to an LSTM evidence model that predicts post-test performance. The article states the approach "does not require a labor -intensive process of labeling data" because strategies are discovered unsupervised from log data.

## Accounts
<!-- How each source describes or uses the method -->
- **Strategy-based temporal analytics framework for stealth assessment using LSTM evidence models**: A stealth assessment framework that derives temporal evidence from students' dynamic in-game strategy use rather than only from ECD evidence modeling. Student flip sequences are encoded as n-grams, clustered per task with EM clustering to yield strategy labels, and sequences of strategy cluster memberships across consecutive tasks are fed to an LSTM evidence model that predicts post-test performance. The article states the approach "does not require a labor -intensive process of labeling data" because strategies are discovered unsupervised from log data. (Akram et al. (2017))

### Claims

- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](../claims/lstm-strategy-temporal-analytics-outperforms-baselines.md) [+M]
- [Adding in-game strategy features to pre-test features substantially improves LSTM-based stealth assessment accuracy](../claims/in-game-strategy-features-improve-prediction-over-pretest-only.md) [+M]
- [Clustering n-gram flip sequences per task yields three distinct problem-solving strategy groups across the binary challenges](../claims/three-strategy-clusters-from-ngram-flip-sequences.md) [+M]
- [GRU is the lowest-performing model across both single-task and multi-task competency modeling, likely due to its two gating units versus LSTMs' three](../claims/gru-lowest-performing-competency-model.md) [+W]

## Related Research Methods

- [Retrospective emulation of evidence-centered design features for learning analytics](retrospective-emulation-of-evidence-centered-design-features-for-learning-analytics.md)
- [Evidence-Centered Design](evidence-centered-design.md)

## Key Sources
- Akram, B., Mott, B., Min, W., Boyer, K. E., Wiebe, E., & Lester, J. (2017). Improving Stealth Assessment in Game-based Learning with LSTM-based Analytics. https://scholar.google.com/scholar?q=Improving+Stealth+Assessment+in+Game-based+Learning+with+LSTM-based+Analytics
