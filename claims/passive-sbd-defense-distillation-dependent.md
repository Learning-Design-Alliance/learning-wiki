---
type: claim
title: Passive backdoor defense (SBD) effectiveness is distillation-dependent, degrading under persona-centric abstraction
description: Passive backdoor defense (SBD) effectiveness is distillation-dependent, degrading under persona-centric abstraction
id: passive-sbd-defense-distillation-dependent
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

# Passive backdoor defense (SBD) effectiveness is distillation-dependent, degrading under persona-centric abstraction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Semantic-level Backdoor Injection achieves high detection rates under Direct and three-stage Distill but drops sharply under Colleague Distill. [→ Yongli Xiang 2026](#yongli-xiang-2026)

## Evidence

### Yongli Xiang 2026

Yongli Xiang, Zhifang Zhang, Bojun Yang, Ziming Hong, Lei Feng, Miao Xu, Tongliang Liu. (2026). When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills. arXiv. https://arxiv.org/abs/2608.03700

`q2 · i?` · `design · r2`

Passive defense evaluation on GPT 5.4 in Table 2, measuring static (ASR-S) and behavioral (ASR-B) attack success rates. Under three-stage Distill, "online/post-hoc injection reaches 98.0/98.0 ASR-S and 82.6/52.4 ASR-B"; under Direct Distill, "100.0/96.0 ASR-S and 46.1/40.4 ASR-B". Descriptive percentages; no effect sizes printed.

> "Incontrast,underCol- leagueDistill,theonlinebackdoorreachesonly40.0ASR-S and 0.0 ASR-B, with post-hoc backdoor following the same pattern (30.0 ASR-S, 0.0 ASR-B)."

## Discussion


## Related Claims
- [Persona-skill distillation encodes substantial private information into skill artifacts, persisting across agent backbones and distillation protocols](persona-skill-distillation-privacy-leakage-persists.md) — related
- [Active defenses (Privacy Sanitization, Adversarial Obfuscation) reduce but do not eliminate persona-skill leakage, leaving personality and background exposed](active-defenses-limited-partial-protection.md) — related
- [Skill-equipped agents reproduce target users' attributes and language, enabling impersonation across unseen contexts](agent-level-impersonation-qa-acc-vocabgain.md) — related
- [Skill-level leakage is strongest for communication style and personality, not explicit demographics](leakage-strongest-communication-personality.md) — related
- [Consistency degrades under multi-strategy evaluation for all personas, driven mainly by tone instability rather than logical contradiction](consistency-degradation-tone-instability.md) — related
- [Multi-strategy adversarial evaluation lowers RPLA robustness scores by 0.174–0.203 points relative to a single-strategy baseline across three personas](multi-strategy-adversarial-testing-lowers-rpla-robustness.md) — related
