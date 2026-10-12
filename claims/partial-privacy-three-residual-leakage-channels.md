---
type: claim
title: "Privacy protection in the framework is partial: three residual leakage channels remain open"
description: "Privacy protection in the framework is partial: three residual leakage channels remain open"
id: partial-privacy-three-residual-leakage-channels
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
sources:
  - id: fuan-xiao-2026
    resource: "https://doi.org/10.1186/s41239-026-00618-5"
    title: "Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li. (2026). Integrating LLM with consortium blockchain for personalized and verifiable online education in higher education. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00618-5"
    author: Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Privacy protection in the framework is partial: three residual leakage channels remain open

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` The authors acknowledge that log anonymization and zero-knowledge summaries cannot completely eliminate three residual leakage channels: metadata side channels, on-chain linkability among transactions associated with the same DID, and transient contextual information retained by the LLM service. [→ Fuan Xiao 2026](#fuan-xiao-2026)

## Evidence

### Fuan Xiao 2026

Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li. (2026). Integrating LLM with consortium blockchain for personalized and verifiable online education in higher education. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00618-5

`q1 · i?` · `design · r2`

Authors' own analysis in the Discussion marking Privacy Leakage as Partial: anonymization and zero-knowledge summaries leave "three residual leakage channels" open, signalling a trade-off between full privacy and the auditability the accountability goals require.

> "although log anonymization and zero-knowledge summaries conceal the content, they cannot completely eliminate three residual leakage channels: metadata side channels, on-chain linkability among transactions associated with the same DID, and transient contextual information retained by the LLM service itself."

## Discussion


## Related Claims
- [Active defenses (Privacy Sanitization, Adversarial Obfuscation) reduce but do not eliminate persona-skill leakage, leaving personality and background exposed](active-defenses-limited-partial-protection.md) — related
- [Persona-skill distillation encodes substantial private information into skill artifacts, persisting across agent backbones and distillation protocols](persona-skill-distillation-privacy-leakage-persists.md) — related
- [Skill-level leakage is strongest for communication style and personality, not explicit demographics](leakage-strongest-communication-personality.md) — related
- [Skill-equipped agents reproduce target users' attributes and language, enabling impersonation across unseen contexts](agent-level-impersonation-qa-acc-vocabgain.md) — related
- [Under defense-in-depth, all 171 multi-layer bypass events are rated severity S0 (no impact) because the tutor system prompt and provider filter absorbed residual leakage](defense-in-depth-critical-bypass-zero.md) — related
