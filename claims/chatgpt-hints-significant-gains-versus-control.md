---
type: claim
title: Learners receiving ChatGPT-generated hints showed statistically significant learning gains compared to a no-hint control in an online mathematics tutoring experiment
description: Learners receiving ChatGPT-generated hints showed statistically significant learning gains compared to a no-hint control in an online mathematics tutoring experiment
id: chatgpt-hints-significant-gains-versus-control
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2024
source_checked: 2026-10-17
sources:
  - id: pardos-za-2024
    title: Pardos ZA 2024
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Learners receiving ChatGPT-generated hints showed statistically significant learning gains compared to a no-hint control in an online mathematics tutoring experiment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2024 · checked against its sources 2026-10-17 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q3 i?` The ChatGPT hint condition produced statistically significantly greater learning gains than the no-hint control (Dunn's test p = 0.011), with a 17% gain versus the control's 1.85%. [→ Pardos ZA 2024](#pardos-za-2024)

## Evidence

### Pardos ZA 2024

Pardos ZA, Bhandari S (2024) ChatGPT-generated help produces learning gains equivalent to human tutor-authored help on mathematics skills. PLoS ONE 19(5): e0304013. https://doi.org/10.1371/journal.pone.0304013

`q3 · i?` · `causal · r2`

Randomized online experiment (N = 274 Mechanical Turk participants) with a 3x4 design in the OATutor system; post-hoc Dunn's test on ranked learning gains. The article reports "statistically significantly greater learning gains (p = 0.011)" for ChatGPT hints over control; no observed effect size is printed for this comparison (the Cohen's d of 0.5 in the article is the effect size assumed for its power analyses).

> "From this test, we found that compared to the 1.85% gain of the control condition (i.e., “no hints”), learners in the ChatGPT condition exhibited statistically significantly greater learning gains (p = 0.011)."

## Studies bearing on this claim

<!-- synthesis:start -->
*Do hints given on demand at the step where the learner is stuck improve learning over working without them?* This table gathers the studies behind this claim and the 10 narrower claims that bear on it: **7 distinct studies** (3 causal, 2 design, 1 review, 1 associational), `q2`–`q3`, 0 of 7 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Pardos ZA 2024](https://doi.org/10.1371/journal.pone.0304013) | q3 · causal · r2 | i? | this claim; [Learning gains from ChatGPT-generated hints were not statistically significantly different](chatgpt-gains-equivalent-human-tutor-hints.md) (supports); [Learning gains showed significant main effects of hint condition and subject, with no sign](condition-subject-main-effects-no-interaction.md) (qualifies); [Both hint conditions took more time-on-task than control, but ChatGPT and human tutor cond](hint-conditions-time-on-task.md) (qualifies); [ChatGPT 3.5 produced low-quality hints for 32% of problems, reducible to near 0% for algeb](chatgpt-hint-error-rate-self-consistency.md) (qualifies) |
| [Kirk Vanacore 2026](https://doi.org/10.48550/arxiv.2602.19303) | q2 · review · r2 | i? | [Generative AI-generated hints can be as effective as human-generated hints for mathematics](genai-hints-effective-but-require-validation.md) (supports) |
| [Reddig 2025](https://doi.org/10.1007/s40593-025-00505-6) | q2 · design · r2 | i? | [GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints a](gpt4-feedback-66-percent-targeted-35-percent-flawed.md) (qualifies) |
| [Malikova Z 2026](https://doi.org/10.3389/feduc.2026.1964629) | q2 · associational · r1 | i? | [AI-generated homework hints were positively associated with exam performance only when exa](ai-hints-aligned-exam-performance-only.md) (qualifies) |
| [Bastani Hamsa 2025](https://doi.org/10.1073/pnas.2422633122) | q3 · causal · r3 | i? | [A guardrailed GPT-4 tutor with teacher-designed hints improves assisted practice performan](gpt-tutor-improves-practice-more-than-gpt-base.md) (supports) |
| [Tsvetomila Mihaylova 2026](https://doi.org/10.48550/arxiv.2605.16933) | q2 · causal · r2 | i? | [Advanced students showed reduced attempts with all hint types, while novices did not clear](advanced-students-attempt-reduction-novices-not.md) (qualifies) |
| [hints-1](https://doi.org/10.48550/arxiv.2605.17857) | q2 · design · r? | i? | [K-12 learners preferred incremental hints and multiple attempts over immediately revealed ](learners-prefer-incremental-hints-over-solutions.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [Learning gains from ChatGPT-generated hints were not statistically significantly different from human tutor-authored hints, though ChatGPT gains were numerically higher in all subjects](chatgpt-gains-equivalent-human-tutor-hints.md) — related
- [Both hint conditions took more time-on-task than control, but ChatGPT and human tutor conditions did not differ in session time](hint-conditions-time-on-task.md) — related
- [Learning gains showed significant main effects of hint condition and subject, with no significant condition-by-subject interaction](condition-subject-main-effects-no-interaction.md) — a broader claim this one bears on
- [Students who teach a ChatGPT teachable agent in natural language achieve greater knowledge gains than students who learn the same material from online videos](chatgpt-teachable-agent-knowledge-gains.md) — related
- [AI multimodal feedback produces post-test learning gains equivalent to educator feedback after controlling for pre-test performance](ai-multimodal-feedback-equivalent-learning-gains.md) — related
- [Students receiving instructor feedback showed significantly greater improvements in lab assignment scores than students receiving AI-generated feedback, after controlling for initial knowledge](instructor-feedback-greater-lab-score-improvements-than-ai-feedback.md) — related
- [AI-generated homework hints were positively associated with exam performance only when exam questions closely matched the homework content](ai-hints-aligned-exam-performance-only.md) — related
- [Feedback source (human tutor vs GPT-4) had no significant effect on ENL students' posttest writing scores](feedback-source-no-posttest-effect-enl.md) — related
- [AIfred and ChatGPT produce comparable math scores while assistance is available](aifred-chatgpt-comparable-assisted-math.md) — related
- [K-12 learners preferred incremental hints and multiple attempts over immediately revealed solutions](learners-prefer-incremental-hints-over-solutions.md) — related
- [Generative AI-generated hints can be as effective as human-generated hints for mathematics performance, but ensuring accuracy requires validation procedures that discard a substantial share of generated hints](genai-hints-effective-but-require-validation.md) — a broader claim this one bears on
