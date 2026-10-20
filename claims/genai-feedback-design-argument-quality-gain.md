---
type: claim
title: Direct GenAI-supported feedback improves immediate argument-quality gain over peer feedback, while reflective and hybrid designs outperform direct GenAI feedback
description: Direct GenAI-supported feedback improves immediate argument-quality gain over peer feedback, while reflective and hybrid designs outperform direct GenAI feedback
id: genai-feedback-design-argument-quality-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: ates-2026
    resource: "https://doi.org/10.1186/s41239-026-00614-9"
    title: "Ates, H. (2026). Human-centered GenAI feedback design in higher education: a multisite experiment on direct, reflective, and hybrid approaches to scientific argumentation. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00614-9"
    author: Ates, H.
    q: 4
    i: 1
    kind: causal
    rigour: 3
---

# Direct GenAI-supported feedback improves immediate argument-quality gain over peer feedback, while reflective and hybrid designs outperform direct GenAI feedback

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r3` · `q4` · `i1` small

## Subclaims
`q4 i1` In a cluster-randomized multisite experiment, direct GenAI-supported feedback outperformed peer feedback on four-dimension argument-quality gain (Cohen's d = 0.25), and both reflective (d = 0.29) and hybrid (d = 0.40) feedback outperformed direct GenAI feedback. [→ Ates 2026](#ates-2026)

## Evidence

### Ates 2026

Ates, H. (2026). Human-centered GenAI feedback design in higher education: a multisite experiment on direct, reflective, and hybrid approaches to scientific argumentation. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00614-9

`q4 · i1` · `causal · r3`

Multisite cluster-randomized longitudinal field experiment with 1,176 first-year students in 48 course sections across four universities; mixed-effects model, F(3, 43.8) = 18.76, p < .001. Table 3 prints small Cohen's d effect sizes: d = 0.25 for Direct GenAI vs Peer, d = 0.29 for Reflective vs Direct GenAI, and d = 0.40 for Hybrid vs Direct GenAI.

> "direct GenAI-supported feedback outperformed peer feedback, and both reflective and hybrid feedback outperformed direct GenAI-supported feedback. The hybrid condition yielded the highest adjusted mean, but the hybrid–reflective contrast was not statistically significant."

## Studies bearing on this claim

<!-- synthesis:start -->
*Does AI feedback or AI support improve learners' arguments and justifications, and in which designs?* This table gathers the studies behind this claim and the 12 narrower claims that bear on it: **8 distinct studies** (3 causal, 2 theoretical, 2 qualitative, 1 design), `q1`–`q4`, 2 of 8 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Ates 2026](https://doi.org/10.1186/s41239-026-00614-9) | q4 · causal · r3 | i1 | this claim |
| [Chang 2026](https://doi.org/10.1186/s41239-026-00586-w) | q2 · causal · r1 | i? | [Argument quality gains favored the PS-GenAI-PF group over the PF group, while elaboration ](genai-peer-feedback-raises-argument-quality.md) (supports); [GenAI-supported peer feedback groups achieved higher structural complexity of argumentatio](genai-peer-feedback-raises-argument-structural-complexity.md) (supports); [Most individual argument structure and quality dimensions showed no significant difference](null-results-argument-dimensions-genai-peer-feedback.md) (qualifies); [The PS-GenAI-PF group outperformed the PF group on rebuttal data and warrant and on addres](ps-genai-pf-improves-rebuttals-and-opposing-view.md) (supports) |
| [Daniel M. Oppenheimer 2025](https://doi.org/10.1007/s40593-025-00521-6) | q1 / q2 · design · r2 | i? | [Students in a scaffolded LLM-collaboration course improved significantly on initial argume](argumentative-writing-gains-scaffolded-llm-assignments.md) (supports); [Students became better able to develop arguments even prior to interacting with LLMs, per ](argument-gains-without-llm-support.md) (qualifies) |
| [Kasneci 2023](https://doi.org/10.1016/j.lindif.2023.102274) | q2 · theoretical · r2 | i? | [Pre-service teachers who received NLP-based adaptive feedback were better able to justify ](adaptive-feedback-improves-diagnosis-justification.md) (supports) |
| [Ali Bicer 2026](https://doi.org/10.1007/s11858-026-01816-1) | q2 · qualitative · r3 | i? | [Progressive scaffold fading moved teachers from guided participation toward independent ju](ai-scaffold-fading-independent-justification.md) (supports) |
| [Matthias Stadler 2024](https://doi.org/10.1016/j.chb.2024.108386) | q2 / q3 · causal · r2 | i2; i? | [Students using Google produce higher-quality justifications in their final recommendations](web-search-higher-quality-justifications-than-llm.md) (counts against); [Germane cognitive load fully mediates the effect of information-search tool on justificati](germane-load-mediates-tool-effect-on-justification-quality.md) (qualifies) |
| [Voicu 2026](https://doi.org/10.61071/jdp.2665) | q2 · qualitative · r2 | i? | [Hybridization of authorship blends human and AI-generated content, often without learners'](hybridization-of-authorship-argumentation.md) (counts against) |
| [Mireia Vendrell 2026](https://doi.org/10.1016/j.caeai.2026.100572) | q1 · theoretical · r2 | i? | [Unstructured LLM use risks cognitive offloading that displaces effortful thought and weake](unstructured-llm-use-cognitive-offloading.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

## Related Claims

- [Reflection improves correspondence between perceived and behavioral reliance on ChatGPT](reflection-improves-awareness-calibration.md) — the general claim this finding bears on, with the studies behind it

- [Feedback improves learning by a medium amount on average, but its effect varies widely with the information it carries, and more than a third of feedback interventions reduce performance](feedback-improves-learning.md) — the general claim this finding bears on, with the studies behind it
- [Reflective and hybrid feedback outperform direct GenAI feedback on delayed AI-free transfer](agentic-designs-delayed-ai-free-transfer.md) — related
- [Hybrid feedback outperforms direct GenAI feedback on conceptual learning; the reflective–direct contrast is positive but non-significant](hybrid-feedback-conceptual-learning-advantage.md) — related
- Randomization produced baseline-equivalent conditions across the four feedback designs — related
- [Argument quality gains favored the PS-GenAI-PF group over the PF group, while elaboration gains favored the GenAI-PF group](genai-peer-feedback-raises-argument-quality.md) — related
- [The PS-GenAI-PF group outperformed the PF group on rebuttal data and warrant and on addressing the opposing view](ps-genai-pf-improves-rebuttals-and-opposing-view.md) — related
- [Most individual argument structure and quality dimensions showed no significant differences across the three peer feedback conditions](null-results-argument-dimensions-genai-peer-feedback.md) — related
- [GenAI-supported peer feedback groups achieved higher structural complexity of argumentation artifacts than peer-feedback-only groups](genai-peer-feedback-raises-argument-structural-complexity.md) — related
- [GenAI-supported peer feedback groups produced more suggestions and explanations and less positive affective feedback than the PF group](genai-peer-feedback-shifts-feedback-quality-profile.md) — related
- [GenAI-assisted education produces significantly higher academic achievement than non-GenAI-assisted approaches (g = 0.40)](genai-higher-academic-achievement-g040.md) — related
- [Pre-service teachers who received NLP-based adaptive feedback were better able to justify their diagnoses than those who received static feedback (reported from Sailer et al.)](adaptive-feedback-improves-diagnosis-justification.md) — related
- [Students bound their reliance on AI feedback and advocate a hybrid model assigning AI broad language concerns and instructors individualized relational guidance](bounded-reliance-hybrid-feedback-preference.md) — related
