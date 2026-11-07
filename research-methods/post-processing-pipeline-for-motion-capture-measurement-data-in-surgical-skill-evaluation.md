---
type: research-method
id: post-processing-pipeline-for-motion-capture-measurement-data-in-surgical-skill-evaluation
title: Post-processing pipeline for motion-capture measurement data in surgical skill evaluation
description: "A data correction process developed for the measurement data, which \"often include noise and outliers owing to misrecognition by the MoCap system.\" It combines threshold-based outlier removal using a partial measurement success rate over a 600-frame (5 s) moving window, ROI-based removal, and a seco"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-07
---

# Post-processing pipeline for motion-capture measurement data in surgical skill evaluation

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
A data correction process developed for the measurement data, which "often include noise and outliers owing to misrecognition by the MoCap system." It combines threshold-based outlier removal using a partial measurement success rate over a 600-frame (5 s) moving window, ROI-based removal, and a second-order Kalman filter whose estimates flag outliers when the discrepancy exceeds five times the estimated standard deviation, followed by linear and Slerp interpolation and Savitzky–Golay smoothing (window 121, polynomial order 3).

## Accounts
<!-- How each source describes or uses the method -->
- **Post-processing pipeline for outlier removal and smoothing of MoCap measurement data**: A data correction process developed for the measurement data, which "often include noise and outliers owing to misrecognition by the MoCap system." It combines threshold-based outlier removal using a partial measurement success rate over a 600-frame (5 s) moving window, ROI-based removal, and a second-order Kalman filter whose estimates flag outliers when the discrepancy exceeds five times the estimated standard deviation, followed by linear and Slerp interpolation and Savitzky–Golay smoothing (window 121, polynomial order 3). (A surgical instrument motion measurement system for skill evaluation in practical laparosc)

### Claims

## Related Research Methods
-

## Key Sources
- Ebina Koki, Abe Takashige, Yan Lingbo, Hotta Kiyohiko, Shichinohe Toshiaki, Higuchi Madoka, Iwahara Naoya, Hosaka Yukino, Harada Shigeru, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Kurashima Yo, Watanabe Masahiko, Kon Masafumi, Murai Sachiyo, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Senoo Taku, Shinohara Nobuo, Konno Atsushi. (2024). A surgical instrument motion measurement system for skill evaluation in practical laparoscopic surgery training. PLOS ONE. https://doi.org/10.1371/journal.pone.0305693
