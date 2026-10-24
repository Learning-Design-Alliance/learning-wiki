---
type: claim
title: "Indirect prompt injections combining instruction manipulation, role-playing, and obfuscation altered AI-assigned grades with attack success rates of 94–100% while remaining undetected"
description: "Indirect prompt injections combining instruction manipulation, role-playing, and obfuscation altered AI-assigned grades with attack success rates of 94–100% while remaining undetected"
id: prompt-injection-alters-ai-grading-94-100-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: niklas-humble-2026
    resource: "https://doi.org/10.1007/s10805-026-09758-9"
    title: "Niklas Humble. (2026). Ethical Implications of Prompt Injection in AI-mediated Grading: An Adversarial Red-Team Evaluation. Journal of Academic Ethics. https://doi.org/10.1007/s10805-026-09758-9"
    author: Niklas Humble
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Indirect prompt injections combining instruction manipulation, role-playing, and obfuscation altered AI-assigned grades with attack success rates of 94–100% while remaining undetected

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a red-team adversarial evaluation of Microsoft Copilot grading a synthetic failing essay, a prompt injection hidden behind an image layer succeeded in 17 of 18 iterations, and a revised end-of-document injection succeeded in 9 of 9 iterations, changing the grade without detection. [→ Niklas Humble 2026](#niklas-humble-2026)

## Evidence

### Niklas Humble 2026

Niklas Humble. (2026). Ethical Implications of Prompt Injection in AI-mediated Grading: An Adversarial Red-Team Evaluation. Journal of Academic Ethics. https://doi.org/10.1007/s10805-026-09758-9

`q2 · i?` · `design · r2`

Adversarial security evaluation (attempt 5): the attempt-3 injection paragraph re-used behind an image layer succeeded in 17 of 18 iterations, "with 17 successes and 1 failure", raising the grade to pass or pass with distinction without Copilot warning the user.

> "In total, 18 iterations were conducted with the prompt injection hidden behind an image layer, with 17 successes and 1 failure"

## Discussion


## Related Claims
- [Basic prompt injection attempts failed or were detected: instruction manipulation alone failed in all 9 iterations, role-playing without concealment was detected in output, and metadata-hidden injections failed in all 9 iterations](basic-and-metadata-injections-fail.md) — related
- [Copilot's detection of one advanced injection did not persist: after reporting an embedded instruction once, the same file's injection succeeded in six subsequent iterations without warning](inconsistent-detection-false-security.md) — a narrower finding that bears on this claim
- [Injected provider failures produced recorded unavailability and zero fabricated hints, while valid and reentrant conditions stored 30 synthetic hints each](praxis-provider-failure-no-fabricated-hints.md) — related
- [A revised injection combining instruction manipulation and role-playing with an explicit do-not-mention instruction succeeded in all 9 iterations across docx, pdf, and htm formats](revised-injection-roleplay-undetected-all-formats.md) — possibly the same claim (merge candidate)
- [Asking the AI tool directly about hidden instructions exposed the prompt injection in all 6 security-check iterations, but the authors caution this is not a robust safeguard](direct-security-check-exposes-injection.md) — related
- [Prompt injection attacks on agents (OpenClaw walletdrain, EchoLeak) bypass the user entirely, and no public AI literacy curriculum addresses this vector](prompt-injection-attacks-bypass-user-literacy.md) — related
- [Deterrence layers failed because seeds changed parameters rather than task structure, scaffolding exposed solution steps, and hidden grading verified output consistency rather than authorship or understanding](why-qiskit-deterrence-layers-failed.md) — related
- [Learners rarely detect manipulation of offloaded information and may replace internal memory with altered external content](offloaded-memory-manipulation.md) — related
