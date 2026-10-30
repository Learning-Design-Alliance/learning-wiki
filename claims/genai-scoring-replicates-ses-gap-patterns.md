---
type: claim
title: SES gap patterns in PISA-like items are robust to scoring responses with generative AI instead of hand-coding
description: SES gap patterns in PISA-like items are robust to scoring responses with generative AI instead of hand-coding
id: genai-scoring-replicates-ses-gap-patterns
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: guilherme-lichand-2026
    resource: "https://doi.org/10.1038/s41539-026-00404-y"
    title: "Guilherme Lichand, Lêticia Lopes, Sachin Allums. (2026). Reading ability conflates SES creativity gaps. npj Science of Learning. https://doi.org/10.1038/s41539-026-00404-y"
    author: Guilherme Lichand, Lêticia Lopes, Sachin Allums
    q: 2
    i: 0
    kind: causal
    rigour: 2
---

# SES gap patterns in PISA-like items are robust to scoring responses with generative AI instead of hand-coding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i0` negligible
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When responses in Study 3 are scored by GenAI (ChatGPT with item-specific PISA-derived prompts) instead of hand-coded scores, the pattern matches Study 2: high-SES students outperform low-SES ones only when reading requirements are present. [→ Guilherme Lichand 2026](#guilherme-lichand-2026)

## Evidence

### Guilherme Lichand 2026

Guilherme Lichand, Lêticia Lopes, Sachin Allums. (2026). Reading ability conflates SES creativity gaps. npj Science of Learning. https://doi.org/10.1038/s41539-026-00404-y

`q2 · i0` · `causal · r2`

Robustness analysis reported in the Supplementary Materials of Study 3, rescoring student responses with generative AI using item-specific prompts containing PISA evaluation criteria and credit-level examples; no effect sizes are printed in the main text.

> "Supplementary Materials further show that, when using GenAI instead of hand-coded scores, the patterns of SES gaps match precisely those documented in Study 2: high-SES students only outperform low-SES ones in the presence of reading requirements."

## Discussion


## Related Claims
- [In PISA 2022-like creativity items, the SES gap reverses in favor of low-SES students when enumerators read the prompts](pisa-items-ses-gap-reverses-without-reading.md) — related
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — a broader claim this one bears on
- [Experimentally removing reading requirements eliminates the SES gap in standard creativity measures: high-SES students outperform low-SES ones only when they read the prompts themselves](rct-reading-requirements-eliminate-ses-gap.md) — possibly the same claim (merge candidate)
