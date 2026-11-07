---
type: claim
title: "About 10% of data are missing in the cadaver system, a major challenge for applications beyond skill evaluation; IMU sensor fusion is proposed"
description: "About 10% of data are missing in the cadaver system, a major challenge for applications beyond skill evaluation; IMU sensor fusion is proposed"
id: ten-percent-missing-data-imu-sensor-fusion
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: ebina-koki-2024
    resource: "https://doi.org/10.1371/journal.pone.0305693"
    title: "Ebina Koki, Abe Takashige, Yan Lingbo, Hotta Kiyohiko, Shichinohe Toshiaki, Higuchi Madoka, Iwahara Naoya, Hosaka Yukino, Harada Shigeru, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Kurashima Yo, Watanabe Masahiko, Kon Masafumi, Murai Sachiyo, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Senoo Taku, Shinohara Nobuo, Konno Atsushi. (2024). A surgical instrument motion measurement system for skill evaluation in practical laparoscopic surgery training. PLOS ONE. https://doi.org/10.1371/journal.pone.0305693"
    author: Ebina Koki, Abe Takashige, Yan Lingbo, Hotta Kiyohiko, Shichinohe Toshiaki, Higuchi Madoka, Iwahara Naoya, Hosaka Yukino, Harada Shigeru, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Kurashima Yo, Watanabe Masahiko, Kon Masafumi, Murai Sachiyo, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Senoo Taku, Shinohara Nobuo, Konno Atsushi
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ebina-koki-2024-2
    resource: "https://doi.org/10.1371/journal.pone.0305693"
    title: "Ebina Koki, Abe Takashige, Yan Lingbo, Hotta Kiyohiko, Shichinohe Toshiaki, Higuchi Madoka, Iwahara Naoya, Hosaka Yukino, Harada Shigeru, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Kurashima Yo, Watanabe Masahiko, Kon Masafumi, Murai Sachiyo, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Senoo Taku, Shinohara Nobuo, Konno Atsushi. (2024). A surgical instrument motion measurement system for skill evaluation in practical laparoscopic surgery training. PLOS ONE. https://doi.org/10.1371/journal.pone.0305693"
    author: Ebina Koki, Abe Takashige, Yan Lingbo, Hotta Kiyohiko, Shichinohe Toshiaki, Higuchi Madoka, Iwahara Naoya, Hosaka Yukino, Harada Shigeru, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Kurashima Yo, Watanabe Masahiko, Kon Masafumi, Murai Sachiyo, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Senoo Taku, Shinohara Nobuo, Konno Atsushi
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# About 10% of data are missing in the cadaver system, a major challenge for applications beyond skill evaluation; IMU sensor fusion is proposed

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`–`q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Approximately 10% of the data were missing in the cadaver system, which the authors call a major challenge for other applications such as a surgical assistant system. [→ Ebina Koki 2024](#ebina-koki-2024)
`q1 i?` The authors propose installing an inertial measurement unit on the instrument and interpolating missing data via sensor fusion, a system currently under development. [→ Ebina Koki 2024 (2)](#ebina-koki-2024-2)

## Evidence

### Ebina Koki 2024

Ebina Koki, Abe Takashige, Yan Lingbo, Hotta Kiyohiko, Shichinohe Toshiaki, Higuchi Madoka, Iwahara Naoya, Hosaka Yukino, Harada Shigeru, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Kurashima Yo, Watanabe Masahiko, Kon Masafumi, Murai Sachiyo, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Senoo Taku, Shinohara Nobuo, Konno Atsushi. (2024). A surgical instrument motion measurement system for skill evaluation in practical laparoscopic surgery training. PLOS ONE. https://doi.org/10.1371/journal.pone.0305693

`q2 · i?` · `design · r2`

Authors' discussion of the cadaver training results: the effect of the low measurement success rate on skill evaluation was judged acceptable based on the wet-lab accuracy verification, but the missing data limit other applications.

> "However, as presented in Table 4, approximately 10% of the data were missing in this system. This is a major challenge in using this system for other applications such as the surgical assistant system."

### Ebina Koki 2024 (2)

Ebina Koki, Abe Takashige, Yan Lingbo, Hotta Kiyohiko, Shichinohe Toshiaki, Higuchi Madoka, Iwahara Naoya, Hosaka Yukino, Harada Shigeru, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Kurashima Yo, Watanabe Masahiko, Kon Masafumi, Murai Sachiyo, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Senoo Taku, Shinohara Nobuo, Konno Atsushi. (2024). A surgical instrument motion measurement system for skill evaluation in practical laparoscopic surgery training. PLOS ONE. https://doi.org/10.1371/journal.pone.0305693

`q1 · i?` · `design · r2`

Authors' forward-looking proposal in the discussion: an IMU alone produces considerable yaw angle drift errors, but combined with the MoCap system their mutual limitations can be offset; such a system is under development by the research group.

> "A possible solution to this challenge is to install an inertial measurement unit (IMU) on the surgical instrument and interpolate the missing data using sensor fusion."

## Discussion


## Related Claims
- [During cadaver surgical training the system recorded six instruments with success rates of approximately 90% across 25 analyzable cases](cadaver-training-measurement-success-rates.md) — related
- [Questionnaire surveys found the attached markers only slightly affected instrument operation in both wet-lab and cadaver training](markers-minimal-interference-questionnaires.md) — related
- [Multimodal sensor fusion outperforms single sensors for detecting learner states, yet few studies integrate continuous biometric monitoring with elementary learning outcomes](multimodal-fusion-outperforms-single-sensors-lab-classroom-gap.md) — related
- [The developed system measures instrument tip position with median errors of about 2–4 mm and attitude angles of about 0.8–1.4°, supporting practical skill evaluation](trio-practical-accuracy-mm-errors.md) — related
