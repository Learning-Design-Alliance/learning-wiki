---
type: design
id: trinocular-mocap-instrument-motion-system
title: Trinocular MoCap-based surgical instrument motion measurement system
description: "A motion-capture measurement system for skill evaluation during practical laparoscopic surgery training, built around a trinocular camera unit (OptiTrack V120: Trio) installed on top of the laparoscopic monitor."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-07
sources:
  - id: ebina-koki-2024
    resource: "https://doi.org/10.1371/journal.pone.0305693"
    title: "Ebina Koki, Abe Takashige, Yan Lingbo, Hotta Kiyohiko, Shichinohe Toshiaki, Higuchi Madoka, Iwahara Naoya, Hosaka Yukino, Harada Shigeru, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Kurashima Yo, Watanabe Masahiko, Kon Masafumi, Murai Sachiyo, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Senoo Taku, Shinohara Nobuo, Konno Atsushi. (2024). A surgical instrument motion measurement system for skill evaluation in practical laparoscopic surgery training. PLOS ONE. https://doi.org/10.1371/journal.pone.0305693"
    author: Ebina Koki, Abe Takashige, Yan Lingbo, Hotta Kiyohiko, Shichinohe Toshiaki, Higuchi Madoka, Iwahara Naoya, Hosaka Yukino, Harada Shigeru, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Kurashima Yo, Watanabe Masahiko, Kon Masafumi, Murai Sachiyo, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Senoo Taku, Shinohara Nobuo, Konno Atsushi
---

# Trinocular MoCap-based surgical instrument motion measurement system

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
A motion-capture measurement system for skill evaluation during practical laparoscopic surgery training, built around a trinocular camera unit (OptiTrack V120: Trio) installed on top of the laparoscopic monitor. Because "each surgical instrument has a different marker pattern, the proposed system can recognize and track multiple surgical instruments and support intraoperative exchange." Tip position and orientation are calculated from markers attached to the instrument root via a registration process using Rodrigues' rotation formula, and orientation is output as quaternions.

## Design Implications

### Context
#### Requirements
- Requires the line of sight from the surgeon to the laparoscopic monitor to guarantee stable measurement, with the camera unit mounted above the monitor
- Requires marker sets attached with dedicated 3D-printed ABS-like resin jigs and registration of each instrument as a rigid body in MoCap software
#### Constraints
- Measures instrument motion from only one direction, so data include noise and outliers from obstacles and misrecognition
- Measurement accuracy is slightly inferior to the authors' previous six-camera system due to the simplified configuration

### Target Learners
- surgeons in laparoscopic surgery training
- urology residents and junior surgeons

### Learning Goals
- objective evaluation of surgical skill
- improving skill transfer efficiency in laparoscopic surgery training

### Claims
- [Trio Success Rate Lower Than Six Camera Wetlab](../claims/trio-success-rate-lower-than-six-camera-wetlab.md) [+M]
- [Kinematic Indices High Spearman Correlation](../claims/kinematic-indices-high-spearman-correlation.md) [+M]
- [Cadaver Training Measurement Success Rates](../claims/cadaver-training-measurement-success-rates.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Ebina Koki, Abe Takashige, Yan Lingbo, Hotta Kiyohiko, Shichinohe Toshiaki, Higuchi Madoka, Iwahara Naoya, Hosaka Yukino, Harada Shigeru, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Kurashima Yo, Watanabe Masahiko, Kon Masafumi, Murai Sachiyo, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Senoo Taku, Shinohara Nobuo, Konno Atsushi. (2024). A surgical instrument motion measurement system for skill evaluation in practical laparoscopic surgery training. PLOS ONE. https://doi.org/10.1371/journal.pone.0305693
