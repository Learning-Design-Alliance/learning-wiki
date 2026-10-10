---
type: claim
title: Skill-level leakage is strongest for communication style and personality, not explicit demographics
description: Skill-level leakage is strongest for communication style and personality, not explicit demographics
id: leakage-strongest-communication-personality
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: yongli-xiang-2026
    resource: "https://arxiv.org/abs/2608.03700"
    title: "Yongli Xiang, Zhifang Zhang, Bojun Yang, Ziming Hong, Lei Feng, Miao Xu, Tongliang Liu. (2026). When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills. arXiv. https://arxiv.org/abs/2608.03700"
    author: Yongli Xiang, Zhifang Zhang, Bojun Yang, Ziming Hong, Lei Feng, Miao Xu, Tongliang Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Skill-level leakage is strongest for communication style and personality, not explicit demographics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Leakage is not limited to explicit demographics; it is strongest for background, personality, and communication style dimensions. [→ Yongli Xiang 2026](#yongli-xiang-2026)

## Evidence

### Yongli Xiang 2026

Yongli Xiang, Zhifang Zhang, Bojun Yang, Ziming Hong, Lei Feng, Miao Xu, Tongliang Liu. (2026). When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills. arXiv. https://arxiv.org/abs/2608.03700

`q2 · i?` · `design · r2`

Main evaluation results in Table 1 on GPT 5.4 show communication coverage "stays between 88.0 and 92.0, while personality ranges from 69.0 to 75.7", while demographic coverage is far lower (e.g., 19.2 under three-stage Distill). Values are descriptive percentages with no effect sizes printed.

> "Leakage is not limited to explicit demographics; it is strongest for background,personality,andcommunicationstyle.ForGPT 5.4, overall Skill Coverage remains high across protocols, reaching66.2forthree-stage,63.6forDirectDistill,and55.2 for Colleague Distill."

## Discussion


## Related Claims
- [Active defenses (Privacy Sanitization, Adversarial Obfuscation) reduce but do not eliminate persona-skill leakage, leaving personality and background exposed](active-defenses-limited-partial-protection.md) — related
- [Skill-equipped agents reproduce target users' attributes and language, enabling impersonation across unseen contexts](agent-level-impersonation-qa-acc-vocabgain.md) — related
- [Persona-skill distillation encodes substantial private information into skill artifacts, persisting across agent backbones and distillation protocols](persona-skill-distillation-privacy-leakage-persists.md) — related
- [Passive backdoor defense (SBD) effectiveness is distillation-dependent, degrading under persona-centric abstraction](passive-sbd-defense-distillation-dependent.md) — related
