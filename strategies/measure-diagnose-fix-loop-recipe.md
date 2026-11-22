---
type: strategy
id: measure-diagnose-fix-loop-recipe
title: "Measure-diagnose-fix loop: drive scripted personas through the live system, record each rejection's stated reason, and fix failures by cause"
description: "The article offers its calibration method as a reusable recipe: acceptance gates define pass/fail criteria; scripted personas (earnest-but-stuck, answer-seeker, gate-evader, injector) drive the live pipeline; a strong..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: yusuf-pisan-2026
    resource: "https://arxiv.org/abs/2608.12292"
    title: "Yusuf Pisan. (2026). Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior. https://arxiv.org/abs/2608.12292"
    author: Yusuf Pisan
---

# Measure-diagnose-fix loop: drive scripted personas through the live system, record each rejection's stated reason, and fix failures by cause

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article offers its calibration method as a reusable recipe: acceptance gates define pass/fail criteria; scripted personas (earnest-but-stuck, answer-seeker, gate-evader, injector) drive the live pipeline; a stronger auditing model re-judges every turn; and each rejection's stated reason is recorded so failures are fixed by cause. As the abstract puts it, "We offer the measure, diagnose, and fix loop as a reusable recipe for any LLM agent that must refuse a capability it has." Sorting rejections by cause (withholding failure, pedagogy-quality issue, grounding issue) turned an ambiguous pass rate into a precise signal.

## Design Implications

### Context
#### Requirements
- Scoring must be separated from billed driving so only turn-driving spends money
- The loop must run against a throwaway database with non-admin synthetic students and a printed cost ledger
- Rejections must be sorted by cause and the judge's reason recorded, not just its verdict
#### Constraints
- The evaluation uses no human subjects and does not substitute for real student traffic
- Three classes of reveal are missed by the offline simulation by design (split-fence, plain-prose, cross-language)

### Target Learners
- undergraduate data structures students

### Target Learning Goals
- reliable Socratic answer-withholding under adversarial pressure

## Claims

- [Half of the apparent ceiling violations in the first run were auditor grounding rejections, not over-help; real ceiling compliance was about 77%](../claims/auditor-artifact-real-compliance-77.md) [+W]
- [The first billed calibration run failed both pedagogy gates badly, with a 43% earnest revise rate and 54% reported hint-ceiling compliance](../claims/first-run-failed-pedagogy-gates.md) [+W]
- [An automated calibration loop drove a deployed LLM tutor to full compliance on all four acceptance gates, reaching a 0% earnest revise rate and 100% hint-ceiling compliance](../claims/llm-tutor-full-compliance-four-gates.md) [+W]
- [Withholding failures of a capable LLM tutor form a descending over-help ladder, from blatant solution leaks to naming the exact bug to over-citing general facts](../claims/over-help-ladder-gross-to-subtle.md) [+W]

## Related Strategies

- [Constrain an LLM to inquiry-only questioning via negative system-prompt constraints plus strict JSON schemas](negative-constraint-prompting-inquiry-only-llm.md)

## Examples
-

## Key Sources
- Yusuf Pisan. (2026). Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior. https://arxiv.org/abs/2608.12292
