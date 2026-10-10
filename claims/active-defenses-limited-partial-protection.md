---
type: claim
title: Active defenses (Privacy Sanitization, Adversarial Obfuscation) reduce but do not eliminate persona-skill leakage, leaving personality and background exposed
description: Active defenses (Privacy Sanitization, Adversarial Obfuscation) reduce but do not eliminate persona-skill leakage, leaving personality and background exposed
id: active-defenses-limited-partial-protection
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

# Active defenses (Privacy Sanitization, Adversarial Obfuscation) reduce but do not eliminate persona-skill leakage, leaving personality and background exposed

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Online Privacy Sanitization reduces Skill Coverage, QA Acc, and VocabGain but personality and background information remain hard to remove; post-hoc Adversarial Obfuscation yields smaller reductions. [→ Yongli Xiang 2026](#yongli-xiang-2026)

## Evidence

### Yongli Xiang 2026

Yongli Xiang, Zhifang Zhang, Bojun Yang, Ziming Hong, Lei Feng, Miao Xu, Tongliang Liu. (2026). When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills. arXiv. https://arxiv.org/abs/2608.03700

`q2 · i?` · `design · r2`

Defense evaluation on GPT 5.4 in Table 2. Online PS reduces Skill Coverage, QA Acc, and VocabGain "to 51.7, 40.6, and 9.0 under Direct Distill", with mitigation most pronounced for communication-style signals (communication VocabGain drops from 87.3 to 6.5). Descriptive percentages; no effect sizes printed.

> "In con- trast, personality and background information are harder to remove,withpersonalitySkillCoverageremaininghighafter OnlinePSunderbothDirectDistill(70.0)andColleagueDis- till (68.3). Post-hoc ADV yields smaller reductions, leaving communication Skill Coverage high and, under Colleague Distill, even increasing overall VocabGain to 20.9."

## Discussion


## Related Claims
- [Skill-equipped agents reproduce target users' attributes and language, enabling impersonation across unseen contexts](agent-level-impersonation-qa-acc-vocabgain.md) — related
- [Persona-skill distillation encodes substantial private information into skill artifacts, persisting across agent backbones and distillation protocols](persona-skill-distillation-privacy-leakage-persists.md) — a broader claim this one bears on
- [Skill-level leakage is strongest for communication style and personality, not explicit demographics](leakage-strongest-communication-personality.md) — related
- [Passive backdoor defense (SBD) effectiveness is distillation-dependent, degrading under persona-centric abstraction](passive-sbd-defense-distillation-dependent.md) — related
