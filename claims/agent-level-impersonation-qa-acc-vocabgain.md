---
type: claim
title: "Skill-equipped agents reproduce target users' attributes and language, enabling impersonation across unseen contexts"
description: "Skill-equipped agents reproduce target users' attributes and language, enabling impersonation across unseen contexts"
id: agent-level-impersonation-qa-acc-vocabgain
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

# Skill-equipped agents reproduce target users' attributes and language, enabling impersonation across unseen contexts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Agents equipped with distilled persona skills reveal target-user attributes under direct queries (Field QA accuracy) and reproduce target-user language in persona-relevant scenarios (VocabGain). [→ Yongli Xiang 2026](#yongli-xiang-2026)

## Evidence

### Yongli Xiang 2026

Yongli Xiang, Zhifang Zhang, Bojun Yang, Ziming Hong, Lei Feng, Miao Xu, Tongliang Liu. (2026). When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills. arXiv. https://arxiv.org/abs/2608.03700

`q2 · i?` · `design · r2`

Agent-level impersonation evaluation in Table 1, with skill-equipped agents answering field questions and generating persona-relevant text judged against ground-truth profiles. Gemini 3.6 Flash reaches "up to 48.4 QA Acc and 40.0 VocabGain overall", and Claude Haiku 4.5 reaches "up to 52.5 QA Acc and 19.9 VocabGain overall". Descriptive percentages; no effect sizes printed.

> "GPT 5.4 with three-stage Distill reaches 56.0 overall QA Acc, recovering demographics (32.6), background (49.1), personality (48.1), and especially communication traits (75.9). Its VocabGain is also positive across all four dimensions (22.3, 37.1, 17.6, 87.7), showing that generated queries move closer to target-user outputs."

## Discussion


## Related Claims
- [Active defenses (Privacy Sanitization, Adversarial Obfuscation) reduce but do not eliminate persona-skill leakage, leaving personality and background exposed](active-defenses-limited-partial-protection.md) — related
- [Persona-skill distillation encodes substantial private information into skill artifacts, persisting across agent backbones and distillation protocols](persona-skill-distillation-privacy-leakage-persists.md) — a broader claim this one bears on
- [Skill-level leakage is strongest for communication style and personality, not explicit demographics](leakage-strongest-communication-personality.md) — related
- [Passive backdoor defense (SBD) effectiveness is distillation-dependent, degrading under persona-centric abstraction](passive-sbd-defense-distillation-dependent.md) — related
