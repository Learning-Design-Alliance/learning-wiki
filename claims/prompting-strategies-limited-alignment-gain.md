---
type: claim
title: Prompting with category information or few-shot examples yields limited improvement in distribution alignment, with zero-shot closest for most models
description: Prompting with category information or few-shot examples yields limited improvement in distribution alignment, with zero-shot closest for most models
id: prompting-strategies-limited-alignment-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: norah-almousa-2026
    resource: "https://doi.org/10.48550/arxiv.2609.28026"
    title: "Norah Almousa, Shayan Peyghambari Oskoui, Raquel Coelho, Gayle Rogers, Xiang Lorraine Li, Diane Litman. (2026). Evaluating Feedback Focus and Pedagogical Adaptivity in LLM-Generated Feedback on Student Writing. arXiv preprint. https://arxiv.org/abs/2609.28026 [doi:10.48550/arxiv.2609.28026](https://doi.org/10.48550/arxiv.2609.28026)"
    author: Norah Almousa, Shayan Peyghambari Oskoui, Raquel Coelho, Gayle Rogers, Xiang Lorraine Li, Diane Litman
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Prompting with category information or few-shot examples yields limited improvement in distribution alignment, with zero-shot closest for most models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Applying category-information or few-shot prompting strategies yields limited improvement in alignment with teacher feedback distributions; Prompt 2 increases JSD for most models and Prompt 3 improves alignment only for Mistral-7B. [→ Norah Almousa 2026](#norah-almousa-2026)

## Evidence

### Norah Almousa 2026

Norah Almousa, Shayan Peyghambari Oskoui, Raquel Coelho, Gayle Rogers, Xiang Lorraine Li, Diane Litman. (2026). Evaluating Feedback Focus and Pedagogical Adaptivity in LLM-Generated Feedback on Student Writing. arXiv preprint. https://arxiv.org/abs/2609.28026 [doi:10.48550/arxiv.2609.28026](https://doi.org/10.48550/arxiv.2609.28026)

`q2 · i?` · `design · r2`

Comparison of six LLMs prompted under zero-shot, zero-shot with category names and definitions, and few-shot with examples, evaluated by JSD against the teacher distribution. The study finds "limited improvement" from prompting changes, with the zero-shot baseline remaining closest for most models.

> "Applying different prompting strategies yields limited improvement. Prompt 2 increases JSD for most models, while Prompt 3 improves alignment only for Mistral-7B (0.2398). In both cases, the zero-shot baseline remains the closest to the teacher feedback focus type distribution for most models."

## Discussion


## Related Claims
- [LLMs cover most teacher feedback focus types but fail to match teacher feedback focus distributions, with LearnLM closest](llms-cover-types-but-mismatch-teacher-distributions.md) — related
- [Reasoning-capable model variants and chain-of-thought prompting yield no measurable improvement in either alignment axis for classroom evaluation](reasoning-variants-no-alignment-improvement.md) — related
- Zero-shot prompt type has minimal impact on LLM-human coding concordance — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting outperform zero-shot across datasets](in-context-examples-improve-bloom-classification.md) — related
- GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it — related
- [Chain-of-thought prompting yields higher-quality GenAI feedback on argumentative essays than Zero-shot prompting and teacher feedback](cot-prompting-higher-feedback-quality-than-zero-shot-and-teacher.md) — related
- [Few-shot prompting modestly improves LLM-human score agreement, inconsistently across datasets and models](few-shot-prompting-inconsistent-grading-gains.md) — related
- [Teachers adapt feedback focus across draft stages in five types while the best model shows significant changes in only three](teacher-draft-stage-adaptivity-exceeds-llms.md) — related
