---
type: claim
title: Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits
description: Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits
id: prompting-limited-uneven-proficiency-control-writing-simulation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: heejin-do-2026
    resource: "https://doi.org/10.48550/arxiv.2609.03215"
    title: "Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215 [doi:10.48550/arxiv.2609.03215](https://doi.org/10.48550/arxiv.2609.03215)"
    author: Heejin Do, Jakub Kontak, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across prompting configurations, content-oriented traits (Content, Prompt Adherence, Language, Narrativity) consistently achieve substantially higher QWK alignment than form-oriented traits (Organization, Word Choice, Sentence Fluency, Conventions). [→ Heejin Do 2026](#heejin-do-2026)
`q2 i?` Even the best proprietary prompting configuration reaches only 0.695 average QWK on content-oriented traits versus 0.458 on form-oriented traits, with Conventions weakest under every prompting setting. [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215 [doi:10.48550/arxiv.2609.03215](https://doi.org/10.48550/arxiv.2609.03215)

`q2 · i?` · `causal · r2`

Automated evaluation of eight prompting configurations for two proprietary LLMs on ASAP/ASAP++, scoring generated essays with a frozen multi-trait AES verifier and reporting QWK. The text reports Claude's best configuration reaching "only 0.458 on form-oriented traits" and that "Conventions remains the weakest trait under every prompting setting."

> "on content-oriented traits but only 0.458 on form-oriented traits. Likewise,Conventions remains the weakest trait under every prompting setting."

## Discussion


## Related Claims
- [Models reproduce high-proficiency writing more faithfully than authentic low-proficiency linguistic form, with distinct failure modes by method](low-proficiency-linguistic-form-bottleneck.md) — related
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — related
- [Structured developmental annotation (CLARA) achieves stronger alignment with developmental references than readability-based and direct prompting baselines](clara-outperforms-readability-and-prompting-baselines.md) — related
- [GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt](grpo-par-improves-alignment-across-all-traits.md) — related
- Empirical gains from AI tools in Arab EL2 classrooms are most consistent for surface-level outcomes, while higher-order writing quality and speaking proficiency show mixed results contingent on teacher mediation — related
- [PsyScore-AES achieves a state-of-the-art average QWK of 0.747 on ASAP++, surpassing the strongest baseline SaMRL-large (0.722) and ranking first on 6 of 8 prompts](psyscore-aes-sota-qwk-0-747-asap.md) — related
- [LearnLens's modular pipeline outperforms direct-prompt baselines on scoring quality while matching latency and cost on 100 authentic student answers](learnlens-modular-pipeline-beats-baselines-scoring.md) — related
