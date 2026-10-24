---
type: claim
title: "Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)"
description: "Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)"
id: judge-anchoring-raises-human-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: cogevol-team-2026
    resource: "https://doi.org/10.48550/arxiv.2608.30968"
    title: "CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968 [doi:10.48550/arxiv.2608.30968](https://doi.org/10.48550/arxiv.2608.30968)"
    author: "CogEvol Team, CogEvol Inc. & Tsinghua University"
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: cogevol-team-2026-2
    resource: "https://arxiv.org/abs/2608.30968"
    title: "CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968"
    author: "CogEvol Team, CogEvol Inc. & Tsinghua University"
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the quality-judges-only configuration over 128 rated pages, the current prompts raise Pearson r from 0.609 to 0.715 and Spearman ρ from 0.672 to 0.741; the full pipeline raises ρ further to 0.749. [→ CogEvol Team 2026](#cogevol-team-2026)
`q2 i?` Of the 18 pages zeroed by the hard-fail gate, the human rater assigned nonzero scores to 13 (group mean 0.32 of 5) — a divergence the report states is by design. [→ CogEvol Team 2026 (2)](#cogevol-team-2026-2)

## Evidence

### CogEvol Team 2026

CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968 [doi:10.48550/arxiv.2608.30968](https://doi.org/10.48550/arxiv.2608.30968)

`q2 · i?` · `design · r2`

Human-agreement study: 128 generated pages independently rated on a 0–5 holistic scale with no access to reward outputs, spanning eight prompts and two model scales; anchored prompts replaced drifting unanchored judges whose scores "pile up near the top of the scale".

> "On the quality-judges-only configuration, the current prompts raise Pearson r from 0.609 to 0.715 and Spearman ρ from 0.672 to 0.741."

### CogEvol Team 2026 (2)

CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968

`q2 · i?` · `design · r3`

Systematic divergence analysis on the 128-page rated sample: the report calls the disagreement "by design", describing the gate as a gradient-suppression mechanism, not a quality metric, to prevent the policy collecting reward on non-functional pages.

> "Of the 18 pages zeroed by the hard-fail gate, the rater assigned nonzero scores to 13, with a group mean of 0.32 out of 5."

## Discussion


## Related Claims
- [On the report's internal suites CogEvol-27B scores 83.7 on slides and 63.7 on HTML-500 with zero hard failures, while no external flagship leads both modalities](cogevol-benchmark-no-flagship-leads-both-modalities.md) — related
- [An LLM-based analogy judge validated against expert judgments shows moderate-to-strong agreement and screens most generated analogies as meeting baseline adequacy](anvil-llm-judge-analogy-screening.md) — related
- [Fine-tuned PLMs measure high-inference teaching practices better when the variable requires less pedagogical expertise, matching human-rater agreement on lexical variables but degrading on inference-heavy ones](plm-performance-depends-on-pedagogical-expertise-required.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- LLM-human agreement is highest for identifying whether students listed a concept and lowest for judging definition correctness — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [A screenshot-only reward was reward-hacked into producing visually convincing but unplayable games; hardening the reward with an interactivity probe and hard-fail gate reversed the collapse](reward-hacking-games-interactivity-probe.md) — related
- [The LLM-judge scoring pipeline for the two metrics aligns with human labels and human raters](llm-judge-pipeline-validated-against-human-raters.md) — related
- [Using a trained StudentSim as the reward for chess tutor RL yields a tutor that expert human raters score best on accuracy, guidance quality, and personalization among the rewards studied](studentsim-reward-yields-best-rated-chess-tutor.md) — related
- [Independent LLM evaluators agreed on agent rankings but differed markedly in leniency, with ceiling effects compressing between-agent discrimination](llm-evaluator-leniency-ceiling-effects.md) — related
