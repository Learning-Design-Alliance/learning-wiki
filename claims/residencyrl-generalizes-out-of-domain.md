---
type: claim
title: Procedural competencies from simulation-based RL training generalize to out-of-domain benchmarks including AMIE Mx, AgentClinic, and CRAFT-MD
description: Procedural competencies from simulation-based RL training generalize to out-of-domain benchmarks including AMIE Mx, AgentClinic, and CRAFT-MD
id: residencyrl-generalizes-out-of-domain
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: liévin-2026
    resource: "https://arxiv.org/abs/2608.07418"
    title: "Liévin, V., Schmidgall, S., Strother, T., Bijamov, A., Goel, A., Palepu, A., Park, C., Balazadeh, V., Sun, M. W., Guerard, M., Chen, J., Steiner, D., Dhillon, V., Azar, I., Mehta, A., Spetsieris, N., Shah, S., Abdelrahim, M., Dahiya, A., Liu, Y., Chou, K., Matias, Y., Hassidim, A., Webster, D. R., Le, Q. V., Hadsell, R., Barral, J., Radebaugh, C., Faust, A., Azizi, S., Schaekermann, M., Chen, P.-H. C., Tu, T., Racz, D., & Yang, L. (2026). ResidencyRL: Reinforcement Learning in Simulated Clinical Environments. arXiv. https://arxiv.org/abs/2608.07418"
    author: "Liévin, V., Schmidgall, S., Strother, T., Bijamov, A., Goel, A., Palepu, A., Park, C., Balazadeh, V., Sun, M. W., Guerard, M., Chen, J., Steiner, D., Dhillon, V., Azar, I., Mehta, A., Spetsieris, N., Shah, S., Abdelrahim, M., Dahiya, A., Liu, Y., Chou, K., Matias, Y., Hassidim, A., Webster, D. R., Le, Q. V., Hadsell, R., Barral, J., Radebaugh, C., Faust, A., Azizi, S., Schaekermann, M., Chen, P.-H. C., Tu, T., Racz, D., & Yang, L."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: liévin-2026-2
    resource: "https://arxiv.org/abs/2608.07418"
    title: "Liévin, V., Schmidgall, S., Strother, T., Bijamov, A., Goel, A., Palepu, A., Park, C., Balazadeh, V., Sun, M. W., Guerard, M., Chen, J., Steiner, D., Dhillon, V., Azar, I., Mehta, A., Spetsieris, N., Shah, S., Abdelrahim, M., Dahiya, A., Liu, Y., Chou, K., Matias, Y., Hassidim, A., Webster, D. R., Le, Q. V., Hadsell, R., Barral, J., Radebaugh, C., Faust, A., Azizi, S., Schaekermann, M., Chen, P.-H. C., Tu, T., Racz, D., & Yang, L. (2026). ResidencyRL: Reinforcement Learning in Simulated Clinical Environments. arXiv. https://arxiv.org/abs/2608.07418"
    author: "Liévin, V., Schmidgall, S., Strother, T., Bijamov, A., Goel, A., Palepu, A., Park, C., Balazadeh, V., Sun, M. W., Guerard, M., Chen, J., Steiner, D., Dhillon, V., Azar, I., Mehta, A., Spetsieris, N., Shah, S., Abdelrahim, M., Dahiya, A., Liu, Y., Chou, K., Matias, Y., Hassidim, A., Webster, D. R., Le, Q. V., Hadsell, R., Barral, J., Radebaugh, C., Faust, A., Azizi, S., Schaekermann, M., Chen, P.-H. C., Tu, T., Racz, D., & Yang, L."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Procedural competencies from simulation-based RL training generalize to out-of-domain benchmarks including AMIE Mx, AgentClinic, and CRAFT-MD

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` On the AMIE Mx multi-visit benchmark, the agent outperforms the base model across all six evaluation categories, with the largest gains in management reasoning (80.1% to 88.4%) and patient communication (83.7% to 92.2%). [→ Liévin 2026](#lievin-2026)
`q2 i?` On AgentClinic and CRAFT-MD, benchmarks that expose premature closure and insufficient information gathering, the agent shows consistent directional improvements. [→ Liévin 2026 (2)](#lievin-2026-2)

## Evidence

### Liévin 2026

Liévin, V., Schmidgall, S., Strother, T., Bijamov, A., Goel, A., Palepu, A., Park, C., Balazadeh, V., Sun, M. W., Guerard, M., Chen, J., Steiner, D., Dhillon, V., Azar, I., Mehta, A., Spetsieris, N., Shah, S., Abdelrahim, M., Dahiya, A., Liu, Y., Chou, K., Matias, Y., Hassidim, A., Webster, D. R., Le, Q. V., Hadsell, R., Barral, J., Radebaugh, C., Faust, A., Azizi, S., Schaekermann, M., Chen, P.-H. C., Tu, T., Racz, D., & Yang, L. (2026). ResidencyRL: Reinforcement Learning in Simulated Clinical Environments. arXiv. https://arxiv.org/abs/2608.07418

`q2 · i?` · `design · r2`

Out-of-domain evaluation on the AMIE Mx multi-visit benchmark (120 cases, 360 visits), a longitudinal care setting never seen during training. The article reports the agent "outperforms the base model across all six evaluation categories" with printed gains for management reasoning and patient communication. No standardized effect size is printed.

> "on the AMIE Mx multi-visit benchmark (Liévin et al., 2026), the agent outperforms the base model across all six evaluation categories, with the largest gains in management reasoning (80.1% to 88.4%) and patient communication (83.7% to 92.2%)"

### Liévin 2026 (2)

Liévin, V., Schmidgall, S., Strother, T., Bijamov, A., Goel, A., Palepu, A., Park, C., Balazadeh, V., Sun, M. W., Guerard, M., Chen, J., Steiner, D., Dhillon, V., Azar, I., Mehta, A., Spetsieris, N., Shah, S., Abdelrahim, M., Dahiya, A., Liu, Y., Chou, K., Matias, Y., Hassidim, A., Webster, D. R., Le, Q. V., Hadsell, R., Barral, J., Radebaugh, C., Faust, A., Azizi, S., Schaekermann, M., Chen, P.-H. C., Tu, T., Racz, D., & Yang, L. (2026). ResidencyRL: Reinforcement Learning in Simulated Clinical Environments. arXiv. https://arxiv.org/abs/2608.07418

`q2 · i?` · `design · r2`

Out-of-domain evaluation on two external benchmarks: AgentClinic-MedQA (215 scenarios), AgentClinic-MIMIC-IV (200 scenarios), and CRAFT-MD (1,273 scenarios). The article reports "consistent improvements" on benchmarks designed to expose premature closure and insufficient information gathering. No standardized effect size is printed.

> "On AgentClinic (Schmidgall et al., 2024) and CRAFT-MD (Johri et al., 2025), which expose models’ tendency toward premature closure and insufficient information gathering, the agent shows consistent improvements."

## Discussion


## Related Claims
- [Multi-turn RL training in simulated clinical encounters improves diagnostic accuracy under adversarial conditions, raising rubric-based accuracy from 81.0% to 88.0%](residencyrl-improves-adversarial-diagnostic-accuracy.md) — related
