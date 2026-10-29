---
type: claim
title: GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions
description: GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions
id: gpt4-almost-perfect-irr-after-rubric-engineering
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: olvet-dm-2026
    resource: "https://doi.org/10.1007/s40670-026-02638-2"
    title: "Olvet DM, Kruidering M, Fulton TB, Truong B, Endo K, Lucito R, Willey JM. (2026). Can Generative Artificial Intelligence Reliably Score Open-Ended Question Assessments in Undergraduate Medical Education? Medical Science Educator 36:1539–1552. https://doi.org/10.1007/s40670-026-02638-2"
    author: Olvet DM, Kruidering M, Fulton TB, Truong B, Endo K, Lucito R, Willey JM
    q: 3
    i: "?"
    kind: design
    rigour: 3
---

# GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q3`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` After rubric refinement across iterations, weighted kappa between faculty and GPT-4 reached almost perfect agreement for questions 1A (kw=0.94) and 2A (kw=0.88) with the analytic rubric and question 2H (kw=0.89) with the holistic rubric. [→ Olvet DM 2026](#olvet-dm-2026)

## Evidence

### Olvet DM 2026

Olvet DM, Kruidering M, Fulton TB, Truong B, Endo K, Lucito R, Willey JM. (2026). Can Generative Artificial Intelligence Reliably Score Open-Ended Question Assessments in Undergraduate Medical Education? Medical Science Educator 36:1539–1552. https://doi.org/10.1007/s40670-026-02638-2

`q3 · i?` · `design · r3`

Results of the three-iteration scoring study at ZSOM and UCSF, where faculty scores were compared to GPT-4 scores using Cohen's weighted kappa with quadratic weighting. The article reports "almost perfect agreement" for both analytic-rubric questions by iteration 3, with the printed kappas and percent agreement.

> "After refining scoring rubrics, the IRR increased to almost perfect agreement for both questions on iteration 2 (question 1A: kw=0.88, 95% CI: 0.81–0.96, 83% agreement; question 2A: kw=0.85, 95% CI: 0.78–0.92, 68% agreement) and iteration 3 (question 1A: kw=0.94, 95% CI: 0.91–0.98, 86% agreement; question 2A: kw=0.88, 95% CI: 0.81–0.94, 74% agreement)."

## Discussion

## Related Claims

- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — the general claim this finding bears on, with the studies behind it
- [The most challenging holistic-rubric question reached only moderate inter-rater reliability (kw=0.54) after three iterations](holistic-hardest-question-moderate-reliability.md) — related
- [Most faculty–GPT-4 scoring discrepancies were only one-point differences, shrinking across iterations](oeq-scoring-discrepancies-mostly-one-point.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — a broader claim this one bears on
- [Adding a model answer to the GPT-4 prompt was counterproductive, lowering scoring reliability](model-answer-in-prompt-lowered-reliability.md) — related
- [Sentence embedding models reach only moderate agreement and need human supervision for open-ended grading](embedding-models-moderate-agreement-need-supervision.md) — related
- [Automated essay scoring can achieve high agreement with human raters but faces calibration constraints](aes-high-agreement-calibration-constraint.md) — related
- [DSPy prompt optimization improves all radiotelephony evaluators, with the largest gain in accuracy (+7.9%)](dspy-optimization-communication-evaluator-gains.md) — related
- [GPT models achieved high polarity agreement with instructors only for positive feedback on the Topic aspect, and could not reliably assess the other rubric aspects](gpt-polarity-agreement-low-except-topic.md) — related
- [Human inter-rater agreement for FRISCO essay scoring was reliable, with mean kappa 0.78–0.84 and percentage of agreement above 75% in all six dimensions](frisco-rater-agreement-reliable.md) — related
- [GPT-3 classified students' open-ended responses about teaching practices with reliability similar to that of human coders](gpt3-coding-reliability-similar-to-humans.md) — related
