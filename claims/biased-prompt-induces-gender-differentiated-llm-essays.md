---
type: claim
title: A gender-biased system prompt induces large gender-differentiated language in LLM-generated career essays, while a neutral prompt does not
description: A gender-biased system prompt induces large gender-differentiated language in LLM-generated career essays, while a neutral prompt does not
id: biased-prompt-induces-gender-differentiated-llm-essays
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: ariyan-hossain-2026
    resource: "https://arxiv.org/abs/2606.15914"
    title: "Ariyan Hossain, Kazi Kamruzzaman Rabbi, Farig Sadeque, S M Taiabul Haque. (2026). Contaminated Collaboration: Measuring Gender Bias Transfer in LLM-Assisted Student Writing. arXiv preprint. https://arxiv.org/abs/2606.15914"
    author: Ariyan Hossain, Kazi Kamruzzaman Rabbi, Farig Sadeque, S M Taiabul Haque
    q: 2
    i: 3
    kind: causal
    rigour: 2
---

# A gender-biased system prompt induces large gender-differentiated language in LLM-generated career essays, while a neutral prompt does not

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` The biased LLM produced an agentic gap of Δ=0.343 (d=1.903, p<.001) versus Δ=0.019 (d=0.115, p=.105) for the neutral LLM, validating the bias stimulus. [→ Ariyan Hossain 2026](#ariyan-hossain-2026)

## Evidence

### Ariyan Hossain 2026

Ariyan Hossain, Kazi Kamruzzaman Rabbi, Farig Sadeque, S M Taiabul Haque. (2026). Contaminated Collaboration: Measuring Gender Bias Transfer in LLM-Assisted Student Writing. arXiv preprint. https://arxiv.org/abs/2606.15914

`q2 · i3` · `causal · r2`

Validation phase generating 1,600 LLM career essays (400 per gender per condition) with llama-3.3-70b-instruct at temperature 1.0; Welch's t-tests on per-essay agency scores. The biased LLM also yielded higher SCR (0.740 vs. 0.351; OR=5.26, p<.001, h=0.80).

> "The bi- ased LLM produced a large, significant agentic gap (∆ = 0.343 , d= 1.903 , p < .001), while the neutral LLM produced a small, non-significant gap ( ∆ = 0.019 , d= 0.115 , p=.105 )"

## Discussion


## Related Claims
- [Bias transfer is asymmetric: prompt condition affects agency in female-target essays but not male-target essays, suppressing female agency while male writing remains stable](asymmetric-female-agency-suppression-bias-transfer.md) — related
- [Students exposed to the biased LLM showed no awareness of its influence, reporting lower perceived AI influence than neutral-condition participants despite larger bias effects](bias-transfer-without-awareness-llm-writing.md) — related
- [Students assisted by a gender-biased LLM produce career-plan essays with a significantly larger male-female agentic gap than students in neutral-LLM and no-AI control conditions](biased-llm-assistance-increases-agentic-gap-student-essays.md) — related
- [Biased LLM assistance increases students' gender-stereotypic occupational recommendations: 71.4% of biased-condition essays recommended a gender-stereotypic occupation versus 45.0% (control) and 39.0% (neutral)](biased-llm-assistance-raises-stereotype-congruence-career-choices.md) — related
- [A neutrally configured LLM assistant produced the lowest rate of gender-stereotypic occupation suggestions, below even the no-AI control condition](neutral-llm-assistant-attenuates-baseline-stereotyping.md) — related
