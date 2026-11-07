---
type: claim
title: "In an RCT reviewed here, adding AI-generated feedback to a GenAI virtual patient improved medical students' clinical decision-making relative to simulation alone"
description: "In an RCT reviewed here, adding AI-generated feedback to a GenAI virtual patient improved medical students' clinical decision-making relative to simulation alone"
id: ai-feedback-improves-clinical-decision-making-rct
aliases: [llm-feedback-improves-cdm-history-taking]
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-31
evidence_strength: weak
newest_evidence: 2026
source_checked: 2026-11-07
sources:
  - id: jiang-juming-2026
    resource: "https://doi.org/10.2196/82756"
    title: "Jiang Juming, Ye Megan Zichen, Kwok Tyrone Tai-On, Wong Janet Yuen Ha. (2026). GenAI-Supported Virtual Patients in Health Care Education: Systematic Review. Journal of Medical Internet Research. https://doi.org/10.2196/82756"
    author: Jiang Juming, Ye Megan Zichen, Kwok Tyrone Tai-On, Wong Janet Yuen Ha
    q: 2
    i: "?"
    kind: review
    rigour: 3
  - id: brügge-emilia-2024
    resource: "https://doi.org/10.1186/s12909-024-06399-7"
    title: "Brügge Emilia, Ricchizzi Sarah, Arenbeck Malin, Keller Marius Niklas, Schur Lina, Stummer Walter, Holling Markus, Lu Max Hao, Darici Dogus. (2024). Large language models improve clinical decision making of medical students through patient simulation and structured feedback: a randomized controlled trial. BMC Medical Education. https://doi.org/10.1186/s12909-024-06399-7"
    author: Brügge Emilia, Ricchizzi Sarah, Arenbeck Malin, Keller Marius Niklas, Schur Lina, Stummer Walter, Holling Markus, Lu Max Hao, Darici Dogus
    q: 2
    i: 3
    kind: causal
    rigour: 2
---

# In an RCT reviewed here, adding AI-generated feedback to a GenAI virtual patient improved medical students' clinical decision-making relative to simulation alone

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r2`, 1 review `r3` · `q2` · `i3` large
> **Currency** · newest study 2026 · checked against its sources 2026-11-07 (automated, 2 of 2 entries) · not reviewed by a person

## Subclaims

`q2 i?` The feedback group (AI simulation plus AI feedback) scored significantly higher overall than the conversation-only control group, particularly in creating context and gathering information. [→ Jiang Juming 2026](#jiang-juming-2026)

`q2 i3` After four AI-simulated patient scenarios, medical students who received ChatGPT-generated feedback outperformed the control group on CRI-HTI clinical decision-making scores. [→ Brügge Emilia 2024](#brugge-emilia-2024)

## Evidence

### Jiang Juming 2026

Jiang Juming, Ye Megan Zichen, Kwok Tyrone Tai-On, Wong Janet Yuen Ha. (2026). GenAI-Supported Virtual Patients in Health Care Education: Systematic Review. Journal of Medical Internet Research. https://doi.org/10.2196/82756

`q2 · i?` · `review · r3`

RCT reported in the review's Table 3 (control n=11, feedback n=10, 4 sessions of 6 minutes) comparing AI simulation only with AI simulation plus AI feedback; the review reports the feedback group "scored significantly higher overall". No effect size is printed.

> "By the end, the feedback group scored significantly higher overall, particularly in creating context and gathering information during clinical decision-making."

### Brügge Emilia 2024

Brügge Emilia, Ricchizzi Sarah, Arenbeck Malin, Keller Marius Niklas, Schur Lina, Stummer Walter, Holling Markus, Lu Max Hao, Darici Dogus. (2024). Large language models improve clinical decision making of medical students through patient simulation and structured feedback: a randomized controlled trial. BMC Medical Education. https://doi.org/10.1186/s12909-024-06399-7

`q2 · i3` · `causal · r2`

Double-blind randomized controlled trial in which 21 medical students completed four ChatGPT-simulated history-taking scenarios; the feedback group "outperformed the control group" on the CRI-HTI, F(1,20) = 4.436, p = .049, partial η2 = 0.198.

> "After four scenarios, participants in the feedback group (M = 3.604 ± 0.130; 95% CI: 3.331, 3.878) outperformed the control group (M = 3.017 ± 0.118; 95% CI: 2.770, 3.264), in CDM, F(1,20) = 4.436, p = .049, with a strong effect size, partial η2 = 0.198."

## Discussion



## Learner Variables

- [Problem Solving](../learner-variables/problem-solving.md) — outcome: instruction changes it

## Related Claims

- [Clearest LLM-teaching signals appear in settings with clearly defined tasks, immediate feedback, and repeated practice, such as simulated patients and structured feedback](llm-teaching-benefits-task-defined-feedback-settings.md) — a broader claim this one bears on
- [Multi-agent AI standardized patient training improved final OSCE-aligned examination scores compared with a structured non-LLM control condition](ma-scaffolding-improves-osce-exam-score.md) — related
- [Controlled GenAI virtual-patient and communication studies reported short-term skill gains, but positive findings were not universal](genai-virtual-patient-short-term-gains-mixed.md) — a broader claim this one bears on
- [AI-generated virtual patients in HPE are used mainly for teaching and learning communication skills, diagnostic reasoning and management reasoning, with assessment a minority use case](ai-virtual-patients-hpe-use-case-range.md) — related
- [Adding simulation to online patient-safety training improved nursing students' patient safety competency, but adding classroom teaching to clinical simulation did not further improve teamwork attitudes](blended-simulation-versus-simulation-alone-mixed.md) — related
- [Performance feedback supported skill accuracy and was equally effective when provided by an educator as by automated means in a virtual simulation](feedback-educator-versus-automated-equally-effective.md) — related
- [In an RCT reviewed by this study, an LLM-based digital patient improved ophthalmology medical history-taking skills relative to control](llm-digital-patient-improves-history-taking-rct.md) — related
- [Near-peer feedback improved clinical note scores compared to no feedback in one included study](near-peer-feedback-improves-clinical-note-scores.md) — related
- [Software-based platforms generally improve examination scores, diagnostic accuracy, and decision-making performance](software-platforms-improve-knowledge-and-decision-making.md) — a broader claim this one bears on
- [Immediate feedback combined with reflection improved diagnostic accuracy on training cases versus outpatient clinic attendance or lecture](immediate-feedback-reflection-diagnostic-accuracy-training-cases.md) — related
- [AI-SP training was associated with higher simulated clinical interview scores in information collection, communication, and diagnostic reasoning, but not empathy](ai-sp-interview-performance-empathy-null.md) — related
- [LLM-generated feedback improved the creating context and securing information subdomains of clinical decision making, but not focusing questions](feedback-improves-creating-context-securing-information-not-focusing.md) — related
- [AI-generated feedback following social robotic VP interactions improves medical students' total OSCE performance (Cohen d=0.74)](ai-feedback-sari-improves-total-osce.md) — related
