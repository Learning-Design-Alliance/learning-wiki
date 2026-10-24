---
type: claim
title: LLM graders show model-specific precision/recall trade-offs, so a single metric is insufficient to judge grading quality
description: LLM graders show model-specific precision/recall trade-offs, so a single metric is insufficient to judge grading quality
id: llm-grader-precision-recall-tradeoffs-single-metric-insufficient
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: fuan-xiao-2026
    resource: "https://doi.org/10.1186/s41239-026-00618-5"
    title: "Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li. (2026). Integrating LLM with consortium blockchain for personalized and verifiable online education in higher education. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00618-5"
    author: Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM graders show model-specific precision/recall trade-offs, so a single metric is insufficient to judge grading quality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The six evaluated LLMs exhibit differing precision/recall tendencies—e.g., deepseek-coder-6.7b-instruct shows higher Precision (0.5808) than Recall (0.5373) while Qwen2-7B-Instruct shows higher Recall (0.5000) but lower Precision (0.2866)—implying the same answer can receive inconsistent judgments across models. [→ Fuan Xiao 2026](#fuan-xiao-2026)

## Evidence

### Fuan Xiao 2026

Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li. (2026). Integrating LLM with consortium blockchain for personalized and verifiable online education in higher education. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00618-5

`q2 · i?` · `design · r2`

Authors' interpretation of the Table 2 benchmark results: model-specific biases in thresholding, output style, and uncertainty mean "a single metric is insufficient to judge quality". The Precision/Recall trade-offs imply inconsistent judgments across models and decoding setups.

> "These differences highlight meaningful, model-specific biases in thresholding, output style, and uncertainty; consequently, a single metric is insufficient to judge quality, and F1 should be considered alongside the application's tolerance for errors."

## Discussion


## Related Claims
- [On the RiceChem ALAG grading benchmark GLM-4-9B-chat leads six LLMs (Accuracy 0.6492, F1 0.6054)](glm4-leads-ricechem-grading-benchmark.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [Automated metrics and LLM judges can misalign with expert human preferences in non-verifiable educational evaluation](non-verifiability-crisis-llm-judges-misalign.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [LLM agreement with human examiners is limited in fast mode and improves in reasoning or thinking modes](llm-fast-mode-limited-thinking-mode-better-agreement.md) — related
- [LLMs differ systematically in grading strictness, forming liberal, restrictive, and balanced grading styles on programming assignments](llms-differ-liberal-restrictive-balanced-grading-styles.md) — a broader claim this one bears on
- [Unanimous-fail panels alone reduced benchmark activation by approximately 40% on average for three Critical evaluators, but were insufficient on their own](unanimous-panels-40-percent-activation-reduction.md) — related
