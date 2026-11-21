---
type: claim
title: LLM quality metrics do not predict human learning outcomes from explanations
description: LLM quality metrics do not predict human learning outcomes from explanations
id: llm-quality-metrics-do-not-predict-human-learning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: lun-ai-2025
    resource: "https://doi.org/10.48550/arXiv.2509.00961"
    title: "Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)"
    author: Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# LLM quality metrics do not predict human learning outcomes from explanations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Despite being rated as higher quality by LLM judges, pipeline-generated explanations provided no learning advantage over self-learning, revealing a systematic gap between LLM quality metrics and human learning outcomes. [→ Lun Ai 2025](#lun-ai-2025)

## Evidence

### Lun Ai 2025

Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)

`q3 · i?` · `causal · r2`

Combined interpretation of the pipeline validation (LLM-judged scores favoring the pipeline) and the human trial (no learning advantage); the article concludes "LLM judges failed to predict the human learning outcomes based on the explanations". The article's text contains the typo 'empircal'.

> "Together with empircal results from the human study, these findings suggest that LLM judges failed to predict the human learning outcomes based on the explanations."

## Discussion


## Related Claims
- [Pipeline-generated LLM explanations of an ILP-learned active learning strategy do not improve human task performance over self-learning in any of three domains](llm-pipeline-explanations-no-advantage-over-self-learning.md) — related
- [LLM judges rate pipeline-generated explanations higher than direct prompting and hand-crafted templates across USML domains](llm-judges-rate-pipeline-explanations-higher.md) — related
- [The LLM-judge scoring pipeline for the two metrics aligns with human labels and human raters](llm-judge-pipeline-validated-against-human-raters.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — a broader claim this one bears on
- [Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding](agreement-quality-divergence-human-consensus-bias.md) — related
- [Automated metrics and LLM judges can misalign with expert human preferences in non-verifiable educational evaluation](non-verifiability-crisis-llm-judges-misalign.md) — a broader claim this one bears on
- [Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)](judge-anchoring-raises-human-agreement.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — a broader claim this one bears on
