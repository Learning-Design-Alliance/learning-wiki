---
type: claim
title: The AI text classifier flagged more ChatGPT-group essays as likely AI-generated, but also produced false positives in the control group
description: The AI text classifier flagged more ChatGPT-group essays as likely AI-generated, but also produced false positives in the control group
id: ai-classifier-flags-more-gpt-essays-false-positives
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: željana-bašić-2023
    resource: "https://doi.org/10.35542/osf.io/n5m7s"
    title: "Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković. (2023). Better by You, better than Me? ChatGPT-3 as writing assistance in students' essays. University Department of Forensic Sciences, University of Split. [doi:10.35542/osf.io/n5m7s](https://doi.org/10.35542/osf.io/n5m7s)"
    author: Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: željana-bašić-2023-2
    resource: "https://doi.org/10.35542/osf.io/n5m7s"
    title: "Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković. (2023). Better by You, better than Me? ChatGPT-3 as writing assistance in students' essays. University Department of Forensic Sciences, University of Split. [doi:10.35542/osf.io/n5m7s](https://doi.org/10.35542/osf.io/n5m7s)"
    author: Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The AI text classifier flagged more ChatGPT-group essays as likely AI-generated, but also produced false positives in the control group

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the ChatGPT group, three essays were rated possibly and five likely AI-produced, whereas the control group had two possibly, one likely, two unlikely and four unclear — but the detector also misclassified control-group texts. [→ Željana Bašić 2023](#zeljana-basic-2023)
`q2 i?` The available ChatGPT text detector performed poorly, giving false positive results on control-group (human-written) essays. [→ Željana Bašić 2023 (2)](#zeljana-basic-2023-2)

## Evidence

### Željana Bašić 2023

Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković. (2023). Better by You, better than Me? ChatGPT-3 as writing assistance in students' essays. University Department of Forensic Sciences, University of Split. [doi:10.35542/osf.io/n5m7s](https://doi.org/10.35542/osf.io/n5m7s)

`q2 · i?` · `causal · r1`

An AI text classifier scored each essay as very unlikely, unlikely, unclear, possibly, or likely AI-generated. The article reports the ChatGPT group "had three possible and five cases likely produced by AI"; these are printed counts, not effect sizes, so impact is coded i? (no magnitude reported; not a null effect).

> "The ChatGPT group  had three possible and five cases likely produced by AI, while one case was labeled as unclear."

### Željana Bašić 2023 (2)

Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković. (2023). Better by You, better than Me? ChatGPT-3 as writing assistance in students' essays. University Department of Forensic Sciences, University of Split. [doi:10.35542/osf.io/n5m7s](https://doi.org/10.35542/osf.io/n5m7s)

`q2 · i?` · `causal · r1`

The authors' evaluation of the OpenAI AI text classifier on the Croatian-language essays. The article states it "did not perform well, giving false positive results in the control group"; no accuracy statistic is printed, so impact is coded i? (no magnitude reported; not a null effect).

> "The available ChatGPT text detector 25 did not perform well, giving false positive results in the control gro up."

## Discussion


## Related Claims
- [AI-text detectors misclassify authentic TOEFL essays by non-native English speakers at a mean false-positive rate of 61.3% across seven detectors, far more often than native-speaker essays](detector-61-3-percent-false-positives-non-native-toefl.md) — a broader claim this one bears on
- [A detector can achieve high aggregate accuracy while producing materially different over-detection rates across author groups](aggregate-accuracy-group-fairness-detectors.md) — a broader claim this one bears on
- [In a documented exploratory audit, one human-authored manuscript received materially different classifications from five commercial detectors, spanning 0% human to Human Generated](multi-tool-audit-cross-tool-inconsistency.md) — related
- [AI language polishing alone can flip human-authored scholarly texts from human-classified to AI-classified](polishing-flips-detector-classification.md) — related
- [AI detectors using perplexity disproportionately misclassify non-native English writers, and the mechanism plausibly extends to other low-perplexity writers](perplexity-bias-non-native-english-writers.md) — a broader claim this one bears on
- [AI-content detection tools achieve only marginally higher success than human reviewers, around 80% versus 78.4%](ai-detection-only-marginally-better-than-humans.md) — related
- [ChatGPT-assisted essays showed slightly higher text unauthenticity (11.87%) than control essays (9.96%)](chatgpt-essays-higher-unauthenticity.md) — related
- [Instructors and teaching assistants detect AI-generated code with only 69% accuracy and a 22% false positive rate, with large variability between raters](instructor-ai-detection-insufficient.md) — related
