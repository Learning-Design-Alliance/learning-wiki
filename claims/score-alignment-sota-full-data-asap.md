---
type: claim
title: Score Alignment applied to DualBERT outperforms previous SOTA AES models (ArTS+RMTS and SaMRL) in the full-data setting on ASAP++
description: Score Alignment applied to DualBERT outperforms previous SOTA AES models (ArTS+RMTS and SaMRL) in the full-data setting on ASAP++
id: score-alignment-sota-full-data-asap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: hongseok-choi-2026
    resource: "https://doi.org/10.1109/ACCESS.2026.3718177"
    title: "Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177"
    author: Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang
    q: 3
    i: "?"
    kind: design
    rigour: 2
  - id: hongseok-choi-2026-2
    resource: "https://doi.org/10.1109/ACCESS.2026.3718177"
    title: "Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177"
    author: Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Score Alignment applied to DualBERT outperforms previous SOTA AES models (ArTS+RMTS and SaMRL) in the full-data setting on ASAP++

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` In the full-data setting on ASAP++, Score Alignment applied to DualBERT outperformed previous SOTA models ArTS+RMTS and SaMRL while showing lower standard deviation. [→ Hongseok Choi 2026](#hongseok-choi-2026)
`q3 i?` Integrating LoRA and Score Alignment yielded QWK scores of 0.714 (per-trait) and 0.732 (per-prompt), with statistically significant gains over DualBERT. [→ Hongseok Choi 2026 (2)](#hongseok-choi-2026-2)

## Evidence

### Hongseok Choi 2026

Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177

`q3 · i?` · `design · r2`

Full-data experiment on ASAP++ (five random seeds, 3:1:1 splits) comparing DualBERT+Score Alignment against existing AES methods in Tables 3 and 4; the article reports it "outperformed previous SOTA models" with lower SD.

> "Score Align- ment, when applied to DualBERT, outperformed previous SOTA models—ArTS+RMTS and SaMRL—while demon- strating better performance stability (i.e., lower SD)."

### Hongseok Choi 2026 (2)

Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177

`q3 · i?` · `causal · r2`

Full-data ASAP++ experiment; the paired t-test section reports Score Alignment improves AVG QWK by 0.011 (per-trait; 95% CI [0.003, 0.019]) and LoRA+SA by 0.013, with p < 0.01 for LoRA+SA.

> "the integration of LoRA and Score Alignment yielded additional performance gains, with QWK scores of 0.714 and 0.732 for per-trait and per-prompt performance, respectively."

## Discussion


## Related Claims
- [PsyScore-AES achieves a state-of-the-art average QWK of 0.747 on ASAP++, surpassing the strongest baseline SaMRL-large (0.722) and ranking first on 6 of 8 prompts](psyscore-aes-sota-qwk-0-747-asap.md) — related
- [In the 32-data setting on ASAP++, the integrated LoRA+SA+UST method reaches 91.2% of full-data performance, with statistically significant gains over DualBERT](integrated-method-32-data-asap.md) — related
- [Score Alignment and UST generalize to TOEFL11 and ELLIPSE, but LoRA slightly degrades performance on those datasets](technique-generalizability-toefl11-ellipse.md) — related
