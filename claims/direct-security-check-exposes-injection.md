---
type: claim
title: Asking the AI tool directly about hidden instructions exposed the prompt injection in all 6 security-check iterations, but the authors caution this is not a robust safeguard
description: Asking the AI tool directly about hidden instructions exposed the prompt injection in all 6 security-check iterations, but the authors caution this is not a robust safeguard
id: direct-security-check-exposes-injection
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

# Asking the AI tool directly about hidden instructions exposed the prompt injection in all 6 security-check iterations, but the authors caution this is not a robust safeguard

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A basic security check re-using attempt-5 files found and reported the hidden instructions in all 6 iterations (3 docx, 3 pdf), yet the authors state self-checking is not a robust security strategy and may come too late for critical attacks. [→ Niklas Humble 2026](#niklas-humble-2026)

## Evidence

### Niklas Humble 2026

Niklas Humble. (2026). Ethical Implications of Prompt Injection in AI-mediated Grading: An Adversarial Red-Team Evaluation. Journal of Academic Ethics. https://doi.org/10.1007/s10805-026-09758-9

`q2 · i?` · `design · r2`

Security check (6 iterations re-using attempt-5 files): Copilot found and reported the hidden instructions "in all instances (Fig. 6)". The authors caution self-checking "is not a robust security strategy" and may not work against all tools or advanced attacks.

> "with Copilot finding and reporting the hidden instructions in all instances (Fig. 6). However, it should be noted that prompting an AI-tool to self‑check for successful or attempted prompt injection attacks is not a robust security strategy"

## Discussion


## Related Claims
- [Basic prompt injection attempts failed or were detected: instruction manipulation alone failed in all 9 iterations, role-playing without concealment was detected in output, and metadata-hidden injections failed in all 9 iterations](basic-and-metadata-injections-fail.md) — related
- [Copilot's detection of one advanced injection did not persist: after reporting an embedded instruction once, the same file's injection succeeded in six subsequent iterations without warning](inconsistent-detection-false-security.md) — related
- [Indirect prompt injections combining instruction manipulation, role-playing, and obfuscation altered AI-assigned grades with attack success rates of 94–100% while remaining undetected](prompt-injection-alters-ai-grading-94-100-percent.md) — related
- [A revised injection combining instruction manipulation and role-playing with an explicit do-not-mention instruction succeeded in all 9 iterations across docx, pdf, and htm formats](revised-injection-roleplay-undetected-all-formats.md) — related
