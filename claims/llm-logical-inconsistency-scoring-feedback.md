---
type: claim
title: "Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive"
description: "Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive"
id: llm-logical-inconsistency-scoring-feedback
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: cohn-2026
    resource: "https://doi.org/10.48550/arxiv.2504.02323"
    title: "Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G. (2026). CoTAL: Human-in-the-Loop Prompt Engineering for Generalizable Formative Assessment Scoring and Feedback. arXiv preprint. https://arxiv.org/abs/2504.02323 [doi:10.48550/arxiv.2504.02323](https://doi.org/10.48550/arxiv.2504.02323)"
    author: "Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G."
    q: 1
    i: "?"
    kind: qualitative
    rigour: 1
---

# Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r1` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In the Rules Task evaluation, the LLM sometimes cited the relevant student text and applicable rubric directive yet still failed to award the appropriate point, a case the authors term logical inconsistency. [→ Cohn 2026](#cohn-2026)

## Evidence

### Cohn 2026

Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G. (2026). CoTAL: Human-in-the-Loop Prompt Engineering for Generalizable Formative Assessment Scoring and Feedback. arXiv preprint. https://arxiv.org/abs/2504.02323 [doi:10.48550/arxiv.2504.02323](https://doi.org/10.48550/arxiv.2504.02323)

`q1 · i?` · `qualitative · r1`

Qualitative constant comparative analysis of GPT-4's reasoning chains during the Rules Task evaluation, examining scoring justifications. The authors present an example where the LLM "acknowledged the applicable rubric directive, yet still failed to award the appropriate point," labeling it "a clear case oflogical inconsistency."

> "The LLM correctly cited the relevant portion of the student’s response, acknowledged the applicable rubric directive, yet still failed to award the appropriate point. This is a clear case oflogical inconsistency"

## Discussion

## Related Claims

- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — the general claim this finding bears on, with the studies behind it
- [CoTAL improves GPT-4 scoring agreement with human scorers on the Rules Task, raising average subscore QWK from 0.826 to 0.916 (a 10.9% gain) over a non-prompt-engineered baseline](cotal-rules-task-qwk-gain.md) — related
- [Rubric-enhanced prompting (Variant 2) raises LLM assigned scores relative to the no-rubric baseline, with model-specific gaps at particular taxonomy levels](rubric-prompting-raises-llm-assigned-scores.md) — related
- [All four evaluated LLMs produce strongly bimodal item-level score distributions on bash exams, and rubric-enhanced prompts amplify the near-perfect-score peak](llm-bash-score-distributions-bimodal-v2-amplifies.md) — related
- [Using AI to evaluate AI outputs was often challenging because AI act as yes people and humans struggled to agree on evaluation rubrics](ai-evaluating-ai-outputs-challenging.md) — related
- [LLM-based assessment can replace similarity-based methods because it needs no ground-truth response and no correctness threshold](llm-assessment-needs-no-ground-truth-or-threshold.md) — related
- [GPT-4 generated detailed per-response feedback that was useful for identifying scoring errors and could support personalized student feedback](gpt4-feedback-useful-for-error-identification.md) — related
- [Accurate LLM solution diagnosis does not reliably produce pedagogically actionable feedback, with lowest rubric scores on error identification and actionability](accurate-diagnosis-not-actionable-feedback.md) — related
- [Systematic prompting of an LLM can generate cognitively activating formative feedback aligned with research-based scaffold types (demonstrated, not yet empirically validated)](leap-prompt-design-generates-cognitively-activating-feedback.md) — related
- [GPT-4 scoring errors clustered on multiple possible answers, unrecognized vocabulary, and missed incorrect or missing answers, while faculty were overly generous graders](gpt4-faculty-error-patterns-oeq-scoring.md) — related
- [On the Debugging Task, CoTAL raised average subscore QWK from 0.567 to 0.706 (24.5% improvement) and Total Score QWK by 0.218 (a 38.9% gain) over the Baseline](cotal-debugging-task-qwk-gain.md) — related
- [Dominant logical fallacies in LLM mathematical explanations shift from family to family and across prompting modes](llm-math-explanation-fallacies-vary-by-family.md) — related
- [Behavioral similarity between LLMs and learners does not guarantee mechanistic similarity](llm-behavioral-similarity-not-mechanistic-similarity.md) — related
- [GPT-4's chain-of-thought reasoning, captured via structured output, was consistently reliable and appeared to provide logical, context-grounded justification usable for prompt tuning and end-user insight](gpt4-cot-reasoning-reliable-transparent.md) — reports the opposite
- [AI models inconsistently capture expert feedback points across generation attempts](ai-feedback-inconsistent-across-attempts.md) — related
