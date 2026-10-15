---
type: claim
title: Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement
description: Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement
id: human-llm-agreement-gap-jaccard
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: liu-2026
    resource: "https://doi.org/10.48550/arxiv.2607.28890"
    title: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890 [doi:10.48550/arxiv.2607.28890](https://doi.org/10.48550/arxiv.2607.28890)"
    author: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: liu-2026-2
    resource: "https://arxiv.org/abs/2607.28890"
    title: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890"
    author: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` Mean human-LLM Jaccard across five models was 0.30 versus approximately 0.52 for human-human pairs, a gap of roughly 0.22 Jaccard points. [→ Liu 2026](#liu-2026)
`q2 i?` Pairwise agreement among the five LLMs ranged from 0.37 to 0.68, comparable to human-human agreement and notably higher than human-LLM agreement, indicating models share interpretive tendencies that differ from human patterns. [→ Liu 2026 (2)](#liu-2026-2)

## Evidence

### Liu 2026

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890 [doi:10.48550/arxiv.2607.28890](https://doi.org/10.48550/arxiv.2607.28890)

`q2 · i?` · `design · r2`

Agreement analysis of the five focal LLMs and three human coders across 2,210 eligible messages, using Jaccard similarity between code sets. Human-LLM agreement (mean 0.30) sat roughly 0.22 Jaccard points below the human-human baseline of approximately 0.52 on the 284-message overlap set.

> "Mean human-LLM Jaccard across models was 0.30 (range 0.23 to 0.34), with exact match rates of 13.5% to 17.6%. On the overlap set of 284 messages coded by multiple humans, pairwise human-human Jaccard mean approximately 0.52, leaving a gap of roughly 0.22 Jaccard points between human-human and human-LLM agreement."

### Liu 2026 (2)

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i?` · `design · r2`

Same agreement analysis at the model level. LLM-LLM Jaccard ranged from 0.37 to 0.68; all three human coders showed the same relative ordering of model agreement, which the authors read as "a structural difference rather than idiosyncratic coder variation".

> "Pairwise agreement among the five LLMs ranged from 0.37 to 0.68, with Gemini Flash, GPT-5.5, and Claude Opus forming a high-agreement cluster and GPT-4o the most divergent model. LLM-LLM agreement is therefore comparable to human-human agreement and notably higher than human-LLM agreement, indicating that models share interpretive tendencies that differ from human patterns."

## Discussion


## Related Claims

- [Human-LLM agreement is moderated by code properties, multi-model consensus, and model-reported confidence](agreement-moderators-tiers-consensus-confidence.md) — related
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest](llm-within-configuration-reliability-high.md) — related
- [An LLM-based analogy judge validated against expert judgments shows moderate-to-strong agreement and screens most generated analogies as meeting baseline adequacy](anvil-llm-judge-analogy-screening.md) — related
- [CLARA achieves the highest agreement with blinded human developmental ranking judgments compared with readability and prompting baselines](clara-highest-human-ranking-agreement.md) — related
- [The LLM observation function's per-answer mastery evidence correlates with true mastery at r = 0.68 pooled, but only r ≈ 0.15 within the weak tier, making it least reliable for low-ability learners](collearn-observation-function-within-tier-reliability.md) — related
- [Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)](judge-anchoring-raises-human-agreement.md) — related
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — related
- [LLM-judge evaluation of tutoring sycophancy shows systematic self-judge blind spots and missed sycophancy even under judge consensus](llm-judge-reliability-tutoring-sycophancy.md) — related
- [The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding](educlaw-bench-judge-panel-human-validation.md) — reports the opposite
- [LLMs and instructors agree broadly on where feedback belongs but diverge on exact sentence spans, with span overlap strongly goal-dependent and LLMs highlighting more of each essay](llm-instructor-span-overlap-goal-dependent.md) — related
- [Feedback givers agree on exact urgency tiers only about a fifth of the time, with most disagreements off by a single tier](low-urgency-rank-agreement.md) — related
- [Gemini-2.5-Pro can effectively replicate human expert judgments when answering SLM-generated MCQs](gemini-surrogate-judge-replicates-human-answers.md) — related
- Multi-label intercoder agreement measured by Jaccard similarity reached a mean pairwise 0.52 at item level, with agreement rising at coarser granularity — related
- [Cosine similarity has opposing effects on LLM coding accuracy: lower similarity within codebooks helps, higher similarity within excerpts helps](claim-opposing-cosine-similarity-codebook-excerpt.md) — related
- An open-source Llama3 model reached substantial agreement with a human coder when sentiment-labeling pre-extracted student reflection quotes — a narrower finding that bears on this claim
- Human–human screening agreement on the coverage overlap was low (36/51; Cohen's κ=0.11; PABAK=0.41), and coverage labels do not recode the corpus — related
- [The LLM-judge scoring pipeline for the two metrics aligns with human labels and human raters](llm-judge-pipeline-validated-against-human-raters.md) — related
- [SHAP and LLM explanation methods show consistently low alignment, with mean top-10 Jaccard similarity of 0.085](low-alignment-shap-llm-sentence-selection.md) — related
- [The emergent LLM coding pipeline reaches substantial agreement with expert human coding (Cohen's κ = 0.78, raw agreement 84%) on a stratified 10% sample](llm-discourse-coding-kappa-078-expert-agreement.md) — related
- [Solutions from different LLM providers converged broadly on most CS1 labs, with cross-LLM MOSS match rates of about 88% pooled across labs but only 13.18–22.11% on Lab 10](cross-llm-convergence-task-dependent.md) — related
- [Most reported student–LLM matches involved short snippets, and raising the minimum match length rapidly reduced coverage, making it a key review-workload control](minimum-match-length-controls-coverage.md) — related
- [Off-the-shelf LLMs are systematically misaligned with human item-difficulty judgments and struggle to simulate lower-proficiency states](off-the-shelf-llms-misaligned-human-difficulty-judgments.md) — related
- [The star-to-sentiment labeling rule agrees with human review-level labels at Cohen's kappa 0.66 with 82% accuracy on 3,000 RateMyProfessor teacher reviews](star-label-rule-kappa-066-82-percent.md) — related
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
- [Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability](llm-grading-moderate-human-agreement-icc.md) — related
- [LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades](llm-high-consensus-agreement-circularity-risk.md) — related
- [The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain](judge-calibration-labels-strong-severity-uneven.md)
