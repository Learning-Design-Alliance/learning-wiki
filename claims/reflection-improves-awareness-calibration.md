---
type: claim
title: Reflection improves correspondence between perceived and behavioral reliance on ChatGPT
description: Reflection improves correspondence between perceived and behavioral reliance on ChatGPT
id: reflection-improves-awareness-calibration
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-16
sources:
  - id: ren-s-2026
    title: Ren S 2026
    q: 3
    i: 3
    kind: causal
    rigour: 2
  - id: ren-s-2026-2
    title: Ren S 2026 (2)
    q: 3
    i: 1
    kind: causal
    rigour: 2
---

# Reflection improves correspondence between perceived and behavioral reliance on ChatGPT

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q3` · `i1`–`i3`
> **Currency** · newest study 2026 · checked against its sources 2026-10-16 (automated, 2 of 2 entries) · not reviewed by a person
> **Design limits** · Ren S 2026: the intervention came bundled with another change (The reflection prompt was accompanied by increased engagement time on AI-assisted trials) (read from the study by two models, 2026-10-25)

## Subclaims
`q3 i3` The reflection condition showed higher awareness calibration than the open ChatGPT condition (0.59 vs. 0.41, d = 1.12). [→ Ren S 2026](#ren-s-2026)
`q3 i1` The open ChatGPT condition showed underestimation of behavioral reliance (negative signed discrepancy), while the reflection condition was near zero (d = 0.29). [→ Ren S 2026 (2)](#ren-s-2026-2)

## Evidence

### Ren S 2026

Ren S (2026) College students’ metacognitive awareness of generative-AI reliance: an experimental study of decision confidence and attribution bias. Front. Psychol. 17:1926110. https://doi.org/10.3389/fpsyg.2026.1926110

`q3 · i3` · `causal · r2`

Participant-level comparison of the awareness-calibration score (reverse-coded absolute discrepancy between standardized perceived and behavioral reliance) in the two AI-assisted conditions; "d = 1.12". Trial-level perceived–behavioral correlations were r = 0.51 (reflection) vs. r = 0.24 (open).

> "The reﬂection condition showed higher absolute calibration than the open ChatGPT condition (M = 0.59,SD = 0.15 vs. M = 0.41,SD = 0.17), t(226) = 8.48,p < 0.001,d = 1.12, 95% CI for the mean diﬀerence [0.14, 0.22]."

### Ren S 2026 (2)

Ren S (2026) College students’ metacognitive awareness of generative-AI reliance: an experimental study of decision confidence and attribution bias. Front. Psychol. 17:1926110. https://doi.org/10.3389/fpsyg.2026.1926110

`q3 · i1` · `causal · r2`

Directional signed-discrepancy analysis in the two AI-assisted conditions: "behavioral reliance tended to exceed perceived reliance" under open ChatGPT support, with the reflection condition near zero; "d = 0.29".

> "The open ChatGPT condition had a negative mean signed discrepancy ( M = −0.22,SD = 0.71), indicating that behavioral reliance tended to exceed perceived reliance, whereas the reﬂection condition was close to zero (M =− 0.02,SD = 0.66); the between-conditiondiﬀerencewasstatisticallysigniﬁcant, t(224.8) = 2.20,p = 0.029,d = 0.29."

## Studies bearing on this claim

<!-- synthesis:start -->
*When learners work with generative AI, does adding a reflection step improve their judgement of the AI and what they learn, compared with using its output directly?* This table gathers the studies behind this claim and the 7 narrower claims that bear on it: **2 distinct studies** (2 causal), `q3`–`q4`, 2 of 2 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Ren S 2026](https://doi.org/10.3389/fpsyg.2026.1926110) | q3 · causal · r2 | i3; i1; i?; i2 | this claim; [A brief metacognitive reflection prompt reduces acceptance of incorrect AI advice compared](reflection-reduces-incorrect-ai-advice-acceptance.md) (supports); [Reflection produced selective rather than blanket rejection of AI: alignment with correct ](reflection-selective-not-blanket-ai-rejection.md) (supports); [Open ChatGPT support produces stronger self-serving attribution bias than ChatGPT support ](chatgpt-support-attribution-bias.md) (supports); [Open ChatGPT support increases college students' final decision confidence relative to ind](chatgpt-support-increases-final-confidence.md) (supports) |
| [Ates 2026](https://doi.org/10.1186/s41239-026-00614-9) | q4 · causal · r3 | i1 | [Reflective and hybrid feedback outperform direct GenAI feedback on delayed AI-free transfe](agentic-designs-delayed-ai-free-transfer.md) (supports); [Hybrid feedback outperforms direct GenAI feedback on conceptual learning; the reflective–d](hybrid-feedback-conceptual-learning-advantage.md) (qualifies); [Direct GenAI-supported feedback improves immediate argument-quality gain over peer feedbac](genai-feedback-design-argument-quality-gain.md) (supports) |
<!-- synthesis:end -->

## Discussion

## Related Claims

- [Access to AI advice roughly doubled reported confidence in answers in one experiment](ai-access-inflates-confidence.md) — the general claim this finding bears on, with the studies behind it

- [Self Assessment Accuracy Is Low Without Training](self-assessment-accuracy-is-low-without-training.md) — the general claim this finding bears on, with the studies behind it

- [Evidence suggests over-reliance on generative AI may negatively affect students' self-regulated learning behaviors, potentially harming retention and transfer to novel contexts](genai-overreliance-harms-self-regulated-learning.md) — the general claim this finding bears on, with the studies behind it
- [Better awareness calibration co-occurs with lower incorrect-advice acceptance and lower attribution bias, interpreted associationally only](calibration-negatively-associated-overreliance.md) — related
- [Open ChatGPT support produces stronger self-serving attribution bias than ChatGPT support with reflection](chatgpt-support-attribution-bias.md) — related
- [Open ChatGPT support increases college students' final decision confidence relative to independent decision-making, and reflection attenuates the boost](chatgpt-support-increases-final-confidence.md) — related
- [ChatGPT recommendation accuracy was comparable between the open-support and reflection conditions, ruling out unequal exposure to erroneous advice](comparable-chatgpt-recommendation-accuracy.md) — related
- [A brief metacognitive reflection prompt reduces acceptance of incorrect AI advice compared with open ChatGPT support alone](reflection-reduces-incorrect-ai-advice-acceptance.md) — related
- [Teachers' self-assessed reflection skill exceeds their externally assessed reflection level, with only a low correlation between the two](teacher-reflection-self-external-assessment-gap.md) — related
- [Reflection produced selective rather than blanket rejection of AI: alignment with correct advice stayed high while alignment with incorrect advice dropped](reflection-selective-not-blanket-ai-rejection.md) — related
- [Trust and reliance can diverge, and self-reported reliance measures cannot classify calibration without output-quality ground truth](trust-reliance-divergence-measures-not-calibrated.md) — related
- [Students frequently accepted misleading AI recommendations (overreliance) while rarely rejecting correct ones (underreliance)](overreliance-frequent-underreliance-rare.md) — related
