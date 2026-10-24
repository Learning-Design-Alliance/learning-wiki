---
type: claim
title: "On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives"
description: "On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives"
id: pangram-outperforms-tools-fully-ai-generated-deep-research
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

# On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Pangram was the only tool that performed well on fully AI-generated papers, with strict accuracy of 65% and inclusive accuracy of 97.5%. [→ Marijke Van Vlasselaer 2026](#marijke-van-vlasselaer-2026)
`q2 i?` Turnitin, GPTZero and Copyleaks completely failed to detect the fully AI-generated content, classifying 100%, 70% and 75% of papers as false negatives respectively. [→ Marijke Van Vlasselaer 2026 (2)](#marijke-van-vlasselaer-2026-2)

## Evidence

### Marijke Van Vlasselaer 2026

Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt. (2026). Who wrote this? Evaluating the reliability of AI detection tools in higher education. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00226-w

`q2 · i?` · `causal · r2`

Classification accuracy analysis of the synthetic dataset (n = 40 fully AI-generated papers generated with ChatGPT Deep Research mode, ground truth = 100% AI), scored against predefined accuracy scales from Weber-Wulff et al. The article reports "a strict accuracy of 65% and an inclusive accuracy of 97.5%" for Pangram.

> "Pangram was the only tool that performed well, with a strict accuracy of 65% and an inclusive accuracy of 97.5%, leaving only one case misclassified."

### Marijke Van Vlasselaer 2026 (2)

Marijke Van Vlasselaer, Filip Van Droogenbroeck and Bram Spruyt. (2026). Who wrote this? Evaluating the reliability of AI detection tools in higher education. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00226-w

`q2 · i?` · `design · r2`

Same classification accuracy analysis of the 40 fully AI-generated papers. The article reports Turnitin classified "100% of the Fully AI generated papers as False Negatives" and Copyleaks had 75% False Negatives and 25% Partially False Negatives; no effect size is printed.

> "Turnitin classified 100% of the Fully AI generated papers as False Negatives (scores between 0 and 20%) while GPTzero classified 70% as False Negatives and 30% as Partially False Negatives (score between 20 and 40%)."

## Discussion


## Related Claims
- [A linear mixed-effects model of detection error showed significant paper type, tool, and interaction effects, with underestimation largest for fully AI-generated papers and Pangram consistently producing the smallest errors](mixed-model-detection-error-underestimation.md) — related
- [Applied to 1,163 real master's theses, Pangram flagged 529 (45.5%) as containing AI-generated content, mostly at low-to-moderate levels](pangram-flagged-45-percent-real-theses.md) — related
- [On hybrid and humanised AI papers, Pangram correctly identified AI content in 37 of 40 cases while GPTZero and Copyleaks performed poorly and Turnitin declined on humanised texts](pangram-robust-hybrid-humanised-texts.md) — related
- [After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero](humanization-drives-detection-below-4-percent.md) — reports the opposite
- [No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low](no-threshold-satisfies-all-three-error-rates.md) — related
- [In a single-institution study, the joint system of Turnitin detection plus faculty judgement formally reported only 54.5 per cent of AI-generated submissions](turnitin-joint-system-54-5-percent-reporting.md) — related
- [Blinded review identified 68% of ChatGPT-generated abstracts as chatbot-produced while 14% of authentic abstracts were misclassified as chatbot-generated](chatgpt-abstract-detection-68-14-percent.md) — related
- [Popular plagiarism detection tools detect plagiarism in AI-assisted essays in less than 15% of cases](plagiarism-detectors-below-15-percent-ai-essays.md) — related
- [The system's error detection recall rate for complex rhythm errors was 91.2% ± 1.8%](rhythm-error-detection-recall-91-2.md) — related
- [Light AI-assisted edits to human-written abstracts are flagged by commercial detectors at 64–80% (Pangram) and 38–49% (GPTZero) rates](light-ai-edits-flagged-at-high-rates.md) — related
- [MOSS detected far fewer suspicious cases in Spring 2026 than in prior offerings, as LLM-assisted submissions lack similarity signals](moss-detection-declined-spring-2026.md) — related
- [Both detectors achieved substantially lower accuracy on scientific writing than on humanities texts](detectors-lower-accuracy-scientific-writing.md) — related
