---
type: claim
title: Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs
description: Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs
id: llm-high-test-retest-reliability-summary-statement-scoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-03
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: stadler-p-2026
    resource: "https://doi.org/10.2196/94666"
    title: "Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J. (2026). Test-Retest Reliability of Large Language Models and Their Concordance With Human Experts in Rubric-Based Scoring of Clinical Summary Statements: Experimental Comparative Study. JMIR Medical Education. https://doi.org/10.2196/94666"
    author: Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Large closed-weights models (Claude, GPT-4o, Mistral Large) showed high test-retest reliability (ICC≥0.92; Fleiss κ=0.59-1.00) across 5 repeated runs. [→ Stadler P 2026](#stadler-p-2026)

## Evidence

### Stadler P 2026

Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J. (2026). Test-Retest Reliability of Large Language Models and Their Concordance With Human Experts in Rubric-Based Scoring of Clinical Summary Statements: Experimental Comparative Study. JMIR Medical Education. https://doi.org/10.2196/94666

`q2 · i?` · `design · r2`

Experimental comparative study running each of 4 LLMs 5 times per prompting condition on 122 rubric-scored summary statements; reliability assessed with ICCs and Fleiss kappa. The study reports "high test-retest reliability (ICC≥0.92; Fleiss κ=0.59‐1.00)" for the three large models.

> "Large closed-weights models (Claude, GPT-4o, and Mistral Large) showed high test-retest reliability (ICC≥0.92; Fleiss κ=0.59‐1.00)."

## Discussion


## Related Claims
- [Mistral 7B shows high ICCs but low Fleiss kappa when scoring summary statements](mistral-7b-high-icc-low-fleiss-kappa.md) — related
- [In one study of repeated LLM scoring of 60 IELTS essays, Gemini 2.5 Flash was moderately reliable (ICC 0.63-0.75) while Claude Sonnet 4 and DeepSeek R1 stayed below 0.70 in most dimensions](llm-essay-scoring-reliability-stratification.md) — related
- [The best prompt showed excellent test-retest reliability (intrarater consistency ICC = 0.89) when rerun in ChatGPT 3.5](llm-grading-excellent-intrarater-consistency.md) — related
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
- [Temporal reliability over a 1-week interval varied across LLMs: Claude 4.5 Sonnet showed very good consistency (kappa = 0.872) while Grok-4 and ChatGPT-5 showed moderate agreement](claude-sonnet-superior-temporal-reliability-radiology-questions.md) — related
