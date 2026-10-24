---
type: claim
title: "At natural TM prevalence (1.6%), even the best model generates roughly 4.3 false alarms per genuine detection, making fully automated stand-alone screening not viable on its own"
description: "At natural TM prevalence (1.6%), even the best model generates roughly 4.3 false alarms per genuine detection, making fully automated stand-alone screening not viable on its own"
id: false-alarms-make-standalone-screening-impractical
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: moiz-imran-and-sahan-bulathwela-2026
    resource: "https://doi.org/10.48550/arxiv.2605.23925"
    title: "Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925 [doi:10.48550/arxiv.2605.23925](https://doi.org/10.48550/arxiv.2605.23925)"
    author: Moiz Imran and Sahan Bulathwela
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# At natural TM prevalence (1.6%), even the best model generates roughly 4.3 false alarms per genuine detection, making fully automated stand-alone screening not viable on its own

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` At natural TM prevalence of 1.6%, the best-performing model (Gemini 3 Flash) generates roughly 4.3 false alarms per genuine detection, so fully automated screening is not viable on its own. [→ Moiz Imran and Sahan Bulathwela 2026](#moiz-imran-and-sahan-bulathwela-2026)

## Evidence

### Moiz Imran and Sahan Bulathwela 2026

Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925 [doi:10.48550/arxiv.2605.23925](https://doi.org/10.48550/arxiv.2605.23925)

`q2 · i?` · `design · r?`

Deployment-scale analysis of the best model's TM detection at the natural prevalence of TM cases in the Eedi data. The authors state the model "generates roughly 4.3 false alarms per genuine detection".

> "At natural TM prevalence (1.6%), even the best model (Gemini 3 Flash) generates roughly 4.3 false alarms per genuine detection, so fully automated screening is not viable on its own."

## Discussion


## Related Claims
- A reasoning-capable open-weight model detects 84% of hidden misconceptions but at realistic prevalence false alarms outnumber genuine detections roughly 8 to 1 — related
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- Including a mark scheme in the prompt does not change misconception detection but significantly reduces false positives against correct-reasoning students — related
- [Combining the pattern detector with an LLM fallback does not improve joint detection accuracy over the LLM alone](pattern-plus-llm-fallback-no-gain.md) — related
- [Free-tier LLM detection performance varies widely and differs by corpus: gemini-2.0-flash leads on real data while the pattern detector leads on synthetic data for intent detection](llm-detection-variability-across-corpus.md) — related
