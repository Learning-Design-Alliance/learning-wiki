---
type: claim
title: "The framework is robust to 15% ASR transcription noise and retains 99.6% of its ICS under zero-shot cross-domain transfer to EdNet-Math"
description: "The framework is robust to 15% ASR transcription noise and retains 99.6% of its ICS under zero-shot cross-domain transfer to EdNet-Math"
id: framework-robust-asr-noise-cross-domain-transfer
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: li-2025
    resource: "https://doi.org/10.3390/info16100882"
    title: "Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882"
    author: Li, Y.; Yang, H.; Fang, Q.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: li-2025-2
    resource: "https://doi.org/10.3390/info16100882"
    title: "Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882"
    author: Li, Y.; Yang, H.; Fang, Q.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The framework is robust to 15% ASR transcription noise and retains 99.6% of its ICS under zero-shot cross-domain transfer to EdNet-Math

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under 15% injected ASR transcription errors, ICS drops by only 4.1% relative for the proposed model versus drops exceeding 12% for all baselines. [→ Li 2025](#li-2025)
`q2 i?` Without fine-tuning on EdNet-Math, the model retains 99.6% of its TeacherEval-2023 ICS score, outperforming baselines by 6–11% on ICS and ExpScore. [→ Li 2025 (2)](#li-2025-2)

## Evidence

### Li 2025

Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882

`q2 · i?` · `design · r2`

Robustness evaluation (§4.5) under noisy input: 15% ASR transcription errors injected, with the model's ICS degradation described as minimal and visualized in Figure 4, versus baseline drops exceeding 12%.

> "When injecting 15% ASR transcription errors, the Inter-Rater Consistency Score (ICS) drops by only 4.1% relative for our model, compared to drops exceeding 12% for all baselines."

### Li 2025 (2)

Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882

`q2 · i?` · `design · r2`

Cross-dataset transfer test (§4.5, Table 5) with paired t-tests reported significant (p < 0.05) against fine-tuned BERT, Instructor-LM, and GPT-4 zero-shot on ICS and ExpScore.

> "For cross-dataset transfer, we evaluate performance without fine-tuning on EdNet-Math. As shown in Table 5, the model retains 99.6% of its TeacherEval-2023 ICS score, outperforming baselines by 6–11% on both ICS and ExpScore."

## Discussion


## Related Claims
- [Models trained on synthetic classroom incident data transfer zero-shot to real-world footage, with the proposed method best at 63.41% though a synthetic-to-real domain gap remains](zero-shot-synthetic-to-real-classroom-incident-transfer.md) — related
- [A distilled multi-order kinematic model outperforms pose-based baselines on a synthetic classroom incident dataset while using one-tenth as many parameters as PoseC3D](distilled-kinematic-model-outperforms-pose-baselines-synthetic-classroom-incidents.md) — related
- [The proposed framework outperforms fine-tuned BERT, Instructor-LM, GPT-4, and RAPT on TeacherEval-2023 across consistency, credibility, calibration, and fairness metrics](llm-teacher-assessment-outperforms-baselines-teachereval.md) — related
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — related
