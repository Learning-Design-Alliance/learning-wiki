---
type: claim
title: A linear mixed-effects model of detection error showed significant paper type, tool, and interaction effects, with underestimation largest for fully AI-generated papers and Pangram consistently producing the smallest errors
description: A linear mixed-effects model of detection error showed significant paper type, tool, and interaction effects, with underestimation largest for fully AI-generated papers and Pangram consistently producing the smallest...
id: mixed-model-detection-error-underestimation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: marijke-van-vlasselaer-2026
    resource: "https://doi.org/10.1007/s40979-026-00226-w"
    title: "Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt. (2026). Who wrote this? Evaluating the reliability of AI detection tools in higher education. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00226-w"
    author: Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt
    q: 2
    i: "?"
    kind: design
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

# A linear mixed-effects model of detection error showed significant paper type, tool, and interaction effects, with underestimation largest for fully AI-generated papers and Pangram consistently producing the smallest errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The overall model and both fixed effects and their interaction were significant (Wald χ²(15) = 7443.65, p<.001; interaction χ²(9) = 1582.33, p < .001). [→ Marijke Van Vlasselaer 2026](#marijke-van-vlasselaer-2026)
`q2 i?` For fully generated papers Turnitin (-99.63) and Copyleaks (-85.97) produced the largest underestimations while Pangram (-14.32) underestimated the least; for hybrid and humanised papers Pangram's average errors (-0.81 and -1.12) were not significantly different from zero. [→ Marijke Van Vlasselaer 2026 (2)](#marijke-van-vlasselaer-2026-2)

## Evidence

### Marijke Van Vlasselaer 2026

Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt. (2026). Who wrote this? Evaluating the reliability of AI detection tools in higher education. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00226-w

`q2 · i?` · `design · r2`

Inferential analysis of prediction error on the 160-paper synthetic dataset: a linear mixed-effects model predicting error scores (ground truth minus tool score) with paper type as a between-subjects and tool as a within-subjects fixed effect. The article reports the printed Wald χ² statistics; no effect size is given.

> "The overall model was significant (Wald χ²(15) = 7443.65, p<.001). Both paper type, χ²(3) = 2392.70, p < .001, and tool, χ²(3) = 2590.66, p < .001, showed significant main effects, as did their interaction, χ²(9) = 1582.33, p < .001."

### Marijke Van Vlasselaer 2026 (2)

Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt. (2026). Who wrote this? Evaluating the reliability of AI detection tools in higher education. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00226-w

`q2 · i?` · `design · r2`

Post hoc estimated marginal means with 95% confidence intervals from the same mixed-effects model. The article reports Pangram was essentially unbiased for hybrid and humanised papers (errors of -0.81 and -1.12, not significantly different from zero) while the other tools showed significant underestimation.

> "Estimated marginal means of the interaction showed that for Fully generated papers, Turnitin (-99.63) and Copyleaks (-85.97) produced the largest underestimations, GPTZero (-85.70) showed a similar underestimation, while Pangram (-14.32) underestimated the least."

## Discussion


## Related Claims
- [On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives](pangram-outperforms-tools-fully-ai-generated-deep-research.md) — related
- [Independent evaluation found commercial AI-text detectors neither sufficiently accurate nor sufficiently reliable for high-stakes use](detectors-insufficient-accuracy-high-stakes.md) — related
- [On hybrid and humanised AI papers, Pangram correctly identified AI content in 37 of 40 cases while GPTZero and Copyleaks performed poorly and Turnitin declined on humanised texts](pangram-robust-hybrid-humanised-texts.md) — related
- [Popular plagiarism detection tools detect plagiarism in AI-assisted essays in less than 15% of cases](plagiarism-detectors-below-15-percent-ai-essays.md) — related
- [No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low](no-threshold-satisfies-all-three-error-rates.md) — related
- [After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero](humanization-drives-detection-below-4-percent.md) — related
- [Applied to 1,163 real master's theses, Pangram flagged 529 (45.5%) as containing AI-generated content, mostly at low-to-moderate levels](pangram-flagged-45-percent-real-theses.md) — related
- [In a single-institution study, the joint system of Turnitin detection plus faculty judgement formally reported only 54.5 per cent of AI-generated submissions](turnitin-joint-system-54-5-percent-reporting.md) — related
