---
type: claim
title: "Applied to 1,163 real master's theses, Pangram flagged 529 (45.5%) as containing AI-generated content, mostly at low-to-moderate levels"
description: "Applied to 1,163 real master's theses, Pangram flagged 529 (45.5%) as containing AI-generated content, mostly at low-to-moderate levels"
id: pangram-flagged-45-percent-real-theses
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: marijke-van-vlasselaer-2026
    resource: "https://doi.org/10.1007/s40979-026-00226-w"
    title: "Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt. (2026). Who wrote this? Evaluating the reliability of AI detection tools in higher education. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00226-w"
    author: Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: marijke-van-vlasselaer-2026-2
    resource: "https://doi.org/10.1007/s40979-026-00226-w"
    title: "Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt. (2026). Who wrote this? Evaluating the reliability of AI detection tools in higher education. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00226-w"
    author: Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Applied to 1,163 real master's theses, Pangram flagged 529 (45.5%) as containing AI-generated content, mostly at low-to-moderate levels

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Design limits** · Marijke Van Vlasselaer 2026: no comparison group (read from the study by two models, 2026-10-25)

## Subclaims
`q2 i?` Pangram flagged 529 of 1,163 theses (45.5%) as containing AI-generated content. [→ Marijke Van Vlasselaer 2026](#marijke-van-vlasselaer-2026)
`q2 i?` Among flagged theses, mean estimated AI usage was 34.0% (median 30.0%, SD 19.9%), with very high AI usage (>80%) rare. [→ Marijke Van Vlasselaer 2026 (2)](#marijke-van-vlasselaer-2026-2)

## Evidence

### Marijke Van Vlasselaer 2026

Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt. (2026). Who wrote this? Evaluating the reliability of AI detection tools in higher education. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00226-w

`q2 · i?` · `causal · r2`

Real-world exploratory application of Pangram to 1,163 master's theses submitted in academic year 2024–2025, with no ground truth available. The article reports "Pangram flagged 529 theses (45.5%)"; accuracy cannot be determined in this context.

> "In total, we analysed 1,163 master’s theses submitted across the educational programs in the faculty of Social Sciences and Economics (Table 6). Pangram flagged 529 theses (45.5%) that contained AI-generated content."

### Marijke Van Vlasselaer 2026 (2)

Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt. (2026). Who wrote this? Evaluating the reliability of AI detection tools in higher education. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00226-w

`q2 · i?` · `design · r2`

Descriptive statistics for the 529 flagged theses. The article reports an interquartile range of 32.0% (Q1 17.0%, Q3 49.0%) and that very high AI usage (>80%) was rare at 1.9%; these are descriptive values, not tested effects.

> "For these flagged theses, the mean estimated AI usage was 34.0% (median = 30.0%, SD = 19.9%), ranging from 7% to 100%."

## Discussion


## Related Claims
- [Inter-detector agreement between Pangram and GPTZero collapses after humanization, so a single vendor flag is not a reliable consensus signal](detector-agreement-collapses-after-humanization.md) — related
- [Light AI-assisted edits to human-written abstracts are flagged by commercial detectors at 64–80% (Pangram) and 38–49% (GPTZero) rates](light-ai-edits-flagged-at-high-rates.md) — related
- [No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low](no-threshold-satisfies-all-three-error-rates.md) — related
- [After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero](humanization-drives-detection-below-4-percent.md) — related
- [Detector flag rates on 2023–2025 original abstracts vary sharply by domain, with non-STEM rates far above STEM](non-stem-abstracts-flagged-more-than-stem.md) — related
- [On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives](pangram-outperforms-tools-fully-ai-generated-deep-research.md) — related
- [On hybrid and humanised AI papers, Pangram correctly identified AI content in 37 of 40 cases while GPTZero and Copyleaks performed poorly and Turnitin declined on humanised texts](pangram-robust-hybrid-humanised-texts.md) — related
- [In a single-institution study, the joint system of Turnitin detection plus faculty judgement formally reported only 54.5 per cent of AI-generated submissions](turnitin-joint-system-54-5-percent-reporting.md) — related
- [A linear mixed-effects model of detection error showed significant paper type, tool, and interaction effects, with underestimation largest for fully AI-generated papers and Pangram consistently producing the smallest errors](mixed-model-detection-error-underestimation.md) — related
- [Both detectors achieved substantially lower accuracy on scientific writing than on humanities texts](detectors-lower-accuracy-scientific-writing.md) — related
