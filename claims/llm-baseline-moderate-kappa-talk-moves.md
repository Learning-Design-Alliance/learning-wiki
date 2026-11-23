---
type: claim
title: "Unadjusted foundation models achieve only moderate agreement (Cohen's κ = 0.38–0.58) with expert annotations when classifying instructional moves in authentic classroom transcripts"
description: "Unadjusted foundation models achieve only moderate agreement (Cohen's κ = 0.38–0.58) with expert annotations when classifying instructional moves in authentic classroom transcripts"
id: llm-baseline-moderate-kappa-talk-moves
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-11-22
recheck_by: 2029
sources:
  - id: kirk-vanacore-and-rené-f-kizilcec-2026
    resource: "https://doi.org/10.1145/3774398.3811605"
    title: "Kirk Vanacore and René F. Kizilcec. (2026). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. Originally published 2025. [doi:10.1145/3774398.3811605](https://doi.org/10.1145/3774398.3811605)"
    author: Kirk Vanacore and René F. Kizilcec
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Unadjusted foundation models achieve only moderate agreement (Cohen's κ = 0.38–0.58) with expert annotations when classifying instructional moves in authentic classroom transcripts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-11-22 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across six models and four prompting strategies, Cohen's κ ranged from 0.38 to 0.58 against expert-coded Talk Move annotations, indicating moderate but limited out-of-the-box interpretive capacity. [→ Kirk Vanacore and René F. Kizilcec 2026](#kirk-vanacore-and-rene-f-kizilcec-2026)

## Evidence

### Kirk Vanacore and René F. Kizilcec 2026

Kirk Vanacore and René F. Kizilcec. (2026). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. Originally published 2025. [doi:10.1145/3774398.3811605](https://doi.org/10.1145/3774398.3811605)

`q2 · i?` · `causal · r2`

Benchmark experiment applying six foundation models under zero-, one-, and few-shot prompting to expert-annotated K–12 mathematics transcripts. The article reports "moderate classification accuracy, with Cohen's κ ranging from 0.38 to 0.58 across all model-prompt combinations"; no effect size is printed.

> "Overall, foundation models demonstrated moderate classification accuracy, with Cohen's κ ranging from 0.38 to 0.58 across all model-prompt combinations."

## Discussion


## Related Claims
- [Few-shot prompting substantially improves Talk Move classification for some models (Claude 4.5 Opus κ 0.48→0.58; Gemini 2.5 Pro 0.38→0.57) but yields minimal gains for GPT-5 and o3](few-shot-prompting-gains-heterogeneous-llm.md) — a narrower finding that bears on this claim
- [Only two EduBehaviors configurations reach macro-F1 comparable to the fine-tuned RoBERTa encoder (0.76) trained on expert-labelled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
- [RoBERTa classifiers detect annotated discourse moves in math classroom transcripts with moderate to high accuracy, best for on vs off task instruction](roberta-classifiers-discourse-moves-moderate-high-accuracy.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [The LLM-as-a-judge production scorer achieves substantial agreement with human rater majority vote (Cohen's kappa = 0.746, accuracy 92.3%)](l2-bench-judge-validation-kappa-0746.md) — related
- Foundation models succeed zero-shot on object-identification skills but fail on skills requiring abstract knowledge and complex reasoning — related
