---
type: design
id: residencyrl-practice-based-clinical-mastery
title: Practice-based clinical mastery through progressively challenging simulated encounters
description: "The article's organizing premise is that clinical competence, for AI as for physicians, is developed through practice rather than acquired through static knowledge testing alone."
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

# Practice-based clinical mastery through progressively challenging simulated encounters

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article's organizing premise is that clinical competence, for AI as for physicians, is developed through practice rather than acquired through static knowledge testing alone. As the authors state, "ResidencyRL is built on a simple premise: clinical mastery, for AI as for physicians, is developed through practice." The framework draws a direct analogy to medical residency, where trainees convert academic knowledge into clinical expertise through years of supervised encounters with diverse feedback and progressively greater autonomy. It holds that a trainee who scores perfectly on examinations may still fail when presentations are atypical, and that the gap is a failure of clinical process rather than medical knowledge — a process that can be optimized through multi-turn RL in simulation.

## Design Implications

### Context
#### Requirements
- Requires simulated environments with sufficient fidelity that competencies trained in simulation transfer to real clinical settings
- Requires a curriculum spanning routine, targeted history-taking, and adversarial scenario types to develop distinct clinical competencies
#### Constraints
- Prospective validation with real-world workflows remains necessary to establish clinical utility
- The competence ceiling of simulation-based training is bounded by environment fidelity

### Target Learners
- Clinical AI agents
- Medical trainees (by analogy to residency education)

### Learning Goals
- Sequential clinical reasoning, diagnostic accuracy, management quality, patient-centered communication, and safety-critical decision-making under uncertainty

### Claims
- [Residencyrl Improves Adversarial Diagnostic Accuracy](../claims/residencyrl-improves-adversarial-diagnostic-accuracy.md) [+M]
- [Residencyrl Generalizes Out Of Domain](../claims/residencyrl-generalizes-out-of-domain.md) [+M]
- [Residencyrl Reduces Missed Red Flags](../claims/residencyrl-reduces-missed-red-flags.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Liévin, V., Schmidgall, S., Strother, T., Bijamov, A., Goel, A., Palepu, A., Park, C., Balazadeh, V., Sun, M. W., Guerard, M., Chen, J., Steiner, D., Dhillon, V., Azar, I., Mehta, A., Spetsieris, N., Shah, S., Abdelrahim, M., Dahiya, A., Liu, Y., Chou, K., Matias, Y., Hassidim, A., Webster, D. R., Le, Q. V., Hadsell, R., Barral, J., Radebaugh, C., Faust, A., Azizi, S., Schaekermann, M., Chen, P.-H. C., Tu, T., Racz, D., & Yang, L. (2026). ResidencyRL: Reinforcement Learning in Simulated Clinical Environments. arXiv. https://arxiv.org/abs/2608.07418
