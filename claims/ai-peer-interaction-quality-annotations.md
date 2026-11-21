---
type: claim
title: "Expert annotation found nearly 20% of AI interactions contained a definitively incorrect statement, yet 86% of students accepted the AI explanation"
description: "Expert annotation found nearly 20% of AI interactions contained a definitively incorrect statement, yet 86% of students accepted the AI explanation"
id: ai-peer-interaction-quality-annotations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: weijers-2025
    resource: "https://doi.org/10.48550/arXiv.2504.00408"
    title: "Weijers, R., Wu, D., Betts, H., Jacod, T., Guan, L. Y., Sujaya, V., Dev, K., Goel, T., Delooze, W., Rabbany, R., Wu, Y., Godbout, J.-F., & Pelrine, K. (2025). From Intuition to Understanding: Using AI Peers to Overcome Physics Misconceptions. [doi:10.48550/arXiv.2504.00408](https://doi.org/10.48550/arXiv.2504.00408)"
    author: "Weijers, R., Wu, D., Betts, H., Jacod, T., Guan, L. Y., Sujaya, V., Dev, K., Goel, T., Delooze, W., Rabbany, R., Wu, Y., Godbout, J.-F., & Pelrine, K."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Expert annotation found nearly 20% of AI interactions contained a definitively incorrect statement, yet 86% of students accepted the AI explanation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly
> **Design limits** · Weijers 2025: no comparison group (read from the study by two models, 2026-11-21)

## Subclaims
`q2 i?` Six physics graduate students grading all 822 treatment interactions found the AI made inaccurate or misleading statements in a substantial share of interactions, while most students accepted its explanations. [→ Weijers 2025](#weijers-2025)

## Evidence

### Weijers 2025

Weijers, R., Wu, D., Betts, H., Jacod, T., Guan, L. Y., Sujaya, V., Dev, K., Goel, T., Delooze, W., Rabbany, R., Wu, Y., Godbout, J.-F., & Pelrine, K. (2025). From Intuition to Understanding: Using AI Peers to Overcome Physics Misconceptions. [doi:10.48550/arXiv.2504.00408](https://doi.org/10.48550/arXiv.2504.00408)

`q2 · i?` · `causal · r2`

Human annotation of 822 interactions (2,395 dialogue turns) by six physics graduate students against 6 criteria: 55% of interactions explained the key concept clearly, 11% explained it inaccurately; 36% contained at least one ambiguous or misleading statement; 86% of students accepted the explanation. "Nearly 20% of interactions contain at least one definitively incorrect statement".

> "Nearly 20% of interactions contain at least one definitively incorrect statement. Furthermore, we also analyzed whether the AI made ambiguous or misleading statements"

## Discussion


## Related Claims
- [GPT-4 grading feedback sounds plausible but frequently contains incorrect or misleading statements](gpt4-feedback-plausible-but-misleading.md) — related
- [General-purpose LLMs show accuracy and reliability limits, including hallucinations and task-specific accuracy below perfect, making them risky as expert advice sources](llm-accuracy-hallucination-coaching-risk.md) — a broader claim this one bears on
- [Post-test performance was approximately equal regardless of AI explanation quality, suggesting the dialogue process rather than explanation correctness drives the gain](post-test-performance-independent-of-ai-explanation-quality.md) — related
- [GPT-4 tends to assume feedback is correct when it sounds convincing but incorrectly identifies the student error or provides an invalid suggestion, and has a high false positive rate on the diagnostic label.](gpt4-feedback-evaluation-shortcomings.md) — related
- [The author judges 26 of GPT-4's free-response explanations entirely correct at the expert level, while GPT-3.5's wrong-answer explanations erred randomly or self-inconsistently](gpt4-free-responses-expert-level.md) — related
