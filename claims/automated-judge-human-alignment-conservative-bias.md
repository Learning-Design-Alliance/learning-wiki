---
type: claim
title: Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans
description: Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans
id: automated-judge-human-alignment-conservative-bias
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: saqib-shouqi-2026
    resource: "https://doi.org/10.48550/arxiv.2608.03166"
    title: "Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis. (2026). Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation. ADScAI Conference, University of Moratuwa, Sri Lanka. https://arxiv.org/abs/2608.03166 [doi:10.48550/arxiv.2608.03166](https://doi.org/10.48550/arxiv.2608.03166)"
    author: Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Pearson correlations between mean human scores and automated scores were r = 0.82 for RF, r = 0.78 for ED, and r = 0.75 for CS (all p < 0.001), with inter-annotator agreement of Fleiss' kappa = 0.71. [→ Saqib Shouqi 2026](#saqib-shouqi-2026)

## Evidence

### Saqib Shouqi 2026

Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis. (2026). Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation. ADScAI Conference, University of Moratuwa, Sri Lanka. https://arxiv.org/abs/2608.03166 [doi:10.48550/arxiv.2608.03166](https://doi.org/10.48550/arxiv.2608.03166)

`q2 · i3` · `design · r2`

A human validation study had three domain experts independently score a stratified sample of 60 conversation turns (20 per persona) on RF, ED, and CS using the same rubrics as the automated judge; the printed correlation was "r = 0.82 for RF," with Fleiss' kappa = 0.71 among humans.

> "Pearson correlation between mean human scores and automated scores was 𝑟= 0.82for RF ( 𝑝< 0.001),𝑟= 0.78for ED ( 𝑝< 0.001), and𝑟= 0.75for CS (𝑝< 0.001), indicating strong alignment."

## Discussion


## Related Claims

- Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts — related
- [Multi-strategy adversarial evaluation lowers RPLA robustness scores by 0.174–0.203 points relative to a single-strategy baseline across three personas](multi-strategy-adversarial-testing-lowers-rpla-robustness.md) — related
- [RPLA failures are temporally distributed: ethical violations are rare in the first three turns and become significantly more frequent after turn 6](rpla-failure-onset-second-half-of-dialogue.md) — related
- [The automated scoring system's agreement with human raters varied widely by dimension, with information fidelity showing a weak, non-significant correlation](yunyi-human-agreement-varies-by-dimension.md) — related
- [LLM-as-judge evaluation scored CyberAGENTS highest on domain grounding (4.46) and agent role fidelity (4.35)](cyberagents-llm-judge-high-domain-grounding.md) — related
- [Inter-annotator agreement was moderate (combined mean Fleiss's κ of 0.62 across 23 groups), yet most students reported having reached consensus](moderate-kappa-versus-perceived-consensus-gap.md) — related
- [Small language models used as automated judges exhibit severe leniency bias against tutoring responses](slm-judges-show-severe-leniency-bias.md) — reports the opposite
- [The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding](educlaw-bench-judge-panel-human-validation.md) — related
- [AI scoring shows a systematic conservative bias, under-grading writing so 15.3% (2024) and 16.5% (2025) of human-passing tests would fail under AI scoring](ai-scoring-systematic-under-grading-bias-pass-fail.md) — related
- [In one reviewed study, GPT-4 automated essay scoring showed score inflation, with AI–human rating discrepancies exceeding 1.5 standard deviations in 38% of graduate-level bibliographies](gpt4-essay-score-inflation.md) — related
- [LLM-as-a-judge ratings found only small, incremental differences between systems, with ceiling effects on several criteria](llm-judge-small-incremental-differences-ceiling.md) — related
- [In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range](llm-essay-scoring-systematic-underestimation.md) — related
- [The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain](judge-calibration-labels-strong-severity-uneven.md)
- [High agreement between two LLM screeners indicates consistency among outputs, not accuracy, because models may exhibit correlated failure patterns](llm-agreement-is-consistency-not-accuracy.md) — related
- [Five judges classifying 63 test units reached average inter-judge correlation of 0.542 ± 0.019 on the two scales](judge-agreement-classifying-test-units-scales.md) — related
- [Independent grading by eight judges of 34 specimens showed average deviations below the 10-point scale spacing (average 6.1), supporting the scale's objectivity](ayres-scale-interjudge-consistency.md) — related
- [Three expert coders reached 77.15% overall agreement (Fleiss' κ = 0.763) on the LCT MOOC sample, and over half of their disagreements lay between Exploration and Integration](coder-agreement-exploration-integration-disagreements.md) — related
