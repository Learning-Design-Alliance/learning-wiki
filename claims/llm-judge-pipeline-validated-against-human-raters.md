---
type: claim
title: The LLM-judge scoring pipeline for the two metrics aligns with human labels and human raters
description: The LLM-judge scoring pipeline for the two metrics aligns with human labels and human raters
id: llm-judge-pipeline-validated-against-human-raters
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: neagu-2026
    resource: "https://doi.org/10.48550/arxiv.2606.15766"
    title: "Neagu, A., Wong, J. T. H., Messer, M., Nelson, R., & Johnson, P. B. (2026). Rethinking Scaffolding in LLM Tutors: The Interactional Mismatch Between Benchmarks and Real-World Deployments. Pluralistic Alignment Workshop @ ICML 2026. https://arxiv.org/abs/2606.15766 [doi:10.48550/arxiv.2606.15766](https://doi.org/10.48550/arxiv.2606.15766)"
    author: "Neagu, A., Wong, J. T. H., Messer, M., Nelson, R., & Johnson, P. B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: neagu-2026-2
    resource: "https://doi.org/10.48550/arxiv.2606.15766"
    title: "Neagu, A., Wong, J. T. H., Messer, M., Nelson, R., & Johnson, P. B. (2026). Rethinking Scaffolding in LLM Tutors: The Interactional Mismatch Between Benchmarks and Real-World Deployments. Pluralistic Alignment Workshop @ ICML 2026. https://arxiv.org/abs/2606.15766. [doi:10.48550/arxiv.2606.15766](https://doi.org/10.48550/arxiv.2606.15766)"
    author: "Neagu, A., Wong, J. T. H., Messer, M., Nelson, R., & Johnson, P. B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The LLM-judge scoring pipeline for the two metrics aligns with human labels and human raters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The GPT-5-mini judge distinguishes high and low scaffolding with 93.8% accuracy against MathTutorBench's human-labelled reward-model data. [→ Neagu 2026](#neagu-2026)
`q2 i?` Two human raters reviewing 282 stratified chats agreed with the judge's per-chat uptake scoring on average 78.9% of the time, with moderate inter-rater reliability. [→ Neagu 2026 (2)](#neagu-2026-2)

## Evidence

### Neagu 2026

Neagu, A., Wong, J. T. H., Messer, M., Nelson, R., & Johnson, P. B. (2026). Rethinking Scaffolding in LLM Tutors: The Interactional Mismatch Between Benchmarks and Real-World Deployments. Pluralistic Alignment Workshop @ ICML 2026. https://arxiv.org/abs/2606.15766 [doi:10.48550/arxiv.2606.15766](https://doi.org/10.48550/arxiv.2606.15766)

`q2 · i?` · `associational · r2`

Validation of the Chatbot Scaffolding metric in Section 3.3 against a random 15% sample (550 chats) of MathTutorBench's pedagogical reward-model training data, where "the LLM judge distinguishes with a 93.8% accuracy".

> "This dataset contains human-labelled examples of high and low scaffolding in tutor responses, which the LLM judge distinguishes with a 93.8% accuracy."

### Neagu 2026 (2)

Neagu, A., Wong, J. T. H., Messer, M., Nelson, R., & Johnson, P. B. (2026). Rethinking Scaffolding in LLM Tutors: The Interactional Mismatch Between Benchmarks and Real-World Deployments. Pluralistic Alignment Workshop @ ICML 2026. https://arxiv.org/abs/2606.15766. [doi:10.48550/arxiv.2606.15766](https://doi.org/10.48550/arxiv.2606.15766)

`q2 · i?` · `associational · r2`

Initial validation of the Student Uptake metric in Section 3.3: two human raters reviewed 282 chats stratified by rounded per-chat mean scores, and "raters agreed with 78.9% of the judge's scores", with Gwet's AC1 = 0.580 inter-rater reliability.

> "On average, raters agreed with 78.9% of the judge's scores."

## Discussion


## Related Claims
- [Back-translation evaluation outperforms LLM-as-a-Judge (code+image) in agreement with human raters across four models](backtranslation-outperforms-llm-judge-diagram-agreement.md) — related
- [Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)](judge-anchoring-raises-human-agreement.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Gemini-2.5-Pro can effectively replicate human expert judgments when answering SLM-generated MCQs](gemini-surrogate-judge-replicates-human-answers.md) — related
- [The emergent LLM coding pipeline reaches substantial agreement with expert human coding (Cohen's κ = 0.78, raw agreement 84%) on a stratified 10% sample](llm-discourse-coding-kappa-078-expert-agreement.md) — related
- [AI tutor benchmark datasets show essentially no correlation between chatbot scaffolding and student uptake](no-scaffolding-uptake-correlation-in-benchmarks.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [Using a trained StudentSim as the reward for chess tutor RL yields a tutor that expert human raters score best on accuracy, guidance quality, and personalization among the rewards studied](studentsim-reward-yields-best-rated-chess-tutor.md) — related
- [GPT-4-Turbo as an LLM Judge reliably selects better scaffolds and mitigates hallucination errors, while weaker LLM Judges do not](gpt4-turbo-judge-mitigates-hallucinations-weaker-judges-do-not.md) — related
