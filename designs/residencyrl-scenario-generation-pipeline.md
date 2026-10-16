---
type: design
id: residencyrl-scenario-generation-pipeline
title: Four-stage scenario generation pipeline with demographic sampling, quality verification, and adversarial extension packs
description: "The scenario generation pipeline synthesizes and curates diverse clinical scenarios through four stages: demographic and behavioral attribute sampling from US population distributions including Big Five personality tr..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: liévin-2026
    resource: "https://arxiv.org/abs/2608.07418"
    title: "Liévin, V., Schmidgall, S., Strother, T., Bijamov, A., Goel, A., Palepu, A., Park, C., Balazadeh, V., Sun, M. W., Guerard, M., Chen, J., Steiner, D., Dhillon, V., Azar, I., Mehta, A., Spetsieris, N., Shah, S., Abdelrahim, M., Dahiya, A., Liu, Y., Chou, K., Matias, Y., Hassidim, A., Webster, D. R., Le, Q. V., Hadsell, R., Barral, J., Radebaugh, C., Faust, A., Azizi, S., Schaekermann, M., Chen, P.-H. C., Tu, T., Racz, D., & Yang, L. (2026). ResidencyRL: Reinforcement Learning in Simulated Clinical Environments. arXiv. https://arxiv.org/abs/2608.07418"
    author: "Liévin, V., Schmidgall, S., Strother, T., Bijamov, A., Goel, A., Palepu, A., Park, C., Balazadeh, V., Sun, M. W., Guerard, M., Chen, J., Steiner, D., Dhillon, V., Azar, I., Mehta, A., Spetsieris, N., Shah, S., Abdelrahim, M., Dahiya, A., Liu, Y., Chou, K., Matias, Y., Hassidim, A., Webster, D. R., Le, Q. V., Hadsell, R., Barral, J., Radebaugh, C., Faust, A., Azizi, S., Schaekermann, M., Chen, P.-H. C., Tu, T., Racz, D., & Yang, L"
---

# Four-stage scenario generation pipeline with demographic sampling, quality verification, and adversarial extension packs

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The scenario generation pipeline synthesizes and curates diverse clinical scenarios through four stages: demographic and behavioral attribute sampling from US population distributions including Big Five personality traits, condition-targeted LLM generation grounded in the DDXPlus evidence corpus, LLM-as-judge quality verification across five dimensions, and character-trigram TF-IDF deduplication. As the article states, "A generative proposer-judge pipeline synthesizes and curates diverse clinical scenarios based on targeted demographic and behavioral patient profiles." Two extension packs supplement the base scenarios: targeted history-taking scenarios across a four-domain taxonomy where critical information is withheld unless specifically prompted, and adversarial safety scenarios across a 9-category clinical safety taxonomy.

## Design Implications

### Context
#### Requirements
- Requires scenario quality verification because scenario quality strictly upper-bounds downstream policy performance
- Requires deduplication with cosine similarity threshold of 0.9 to prevent policy memorization of specific narratives
#### Constraints
- Sampling only common presentations may leave the model unprepared for unconventional case presentations where diagnostic error carries the highest clinical cost
- Demographic homogeneity has the potential to induce representation bias

### Target Learners
- Clinical AI agents (LLM-based diagnostic and management agents)

### Learning Goals
- Robust diagnostic reasoning across diverse patient presentations, proactive information elicitation, and safety-critical clinical decision-making

### Claims
- [Residencyrl Improves Adversarial Diagnostic Accuracy](../claims/residencyrl-improves-adversarial-diagnostic-accuracy.md) [+M]
- [Residencyrl Reduces Missed Red Flags](../claims/residencyrl-reduces-missed-red-flags.md) [+M]

## Related Designs

- [Transcript-derived patient profiles conditioning virtual patient behavior across seven dimensions](transcript-derived-virtual-patient-profiles.md)

## Examples
-

## Key Sources
- Liévin, V., Schmidgall, S., Strother, T., Bijamov, A., Goel, A., Palepu, A., Park, C., Balazadeh, V., Sun, M. W., Guerard, M., Chen, J., Steiner, D., Dhillon, V., Azar, I., Mehta, A., Spetsieris, N., Shah, S., Abdelrahim, M., Dahiya, A., Liu, Y., Chou, K., Matias, Y., Hassidim, A., Webster, D. R., Le, Q. V., Hadsell, R., Barral, J., Radebaugh, C., Faust, A., Azizi, S., Schaekermann, M., Chen, P.-H. C., Tu, T., Racz, D., & Yang, L. (2026). ResidencyRL: Reinforcement Learning in Simulated Clinical Environments. arXiv. https://arxiv.org/abs/2608.07418
