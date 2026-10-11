---
type: claim
title: A revised injection combining instruction manipulation and role-playing with an explicit do-not-mention instruction succeeded in all 9 iterations across docx, pdf, and htm formats
description: A revised injection combining instruction manipulation and role-playing with an explicit do-not-mention instruction succeeded in all 9 iterations across docx, pdf, and htm formats
id: revised-injection-roleplay-undetected-all-formats
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: niklas-humble-2026
    resource: "https://doi.org/10.1007/s10805-026-09758-9"
    title: "Niklas Humble. (2026). Ethical Implications of Prompt Injection in AI-mediated Grading: An Adversarial Red-Team Evaluation. Journal of Academic Ethics. https://doi.org/10.1007/s10805-026-09758-9"
    author: Niklas Humble
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# A revised injection combining instruction manipulation and role-playing with an explicit do-not-mention instruction succeeded in all 9 iterations across docx, pdf, and htm formats

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Attempt 3, which added an instruction not to mention the hidden instructions, succeeded in raising the grade to pass and avoiding detection in all 9 iterations, though some outputs leaked the phrase 'revised submission' as a soft signal. [→ Niklas Humble 2026](#niklas-humble-2026)

## Evidence

### Niklas Humble 2026

Niklas Humble. (2026). Ethical Implications of Prompt Injection in AI-mediated Grading: An Adversarial Red-Team Evaluation. Journal of Academic Ethics. https://doi.org/10.1007/s10805-026-09758-9

`q2 · i?` · `causal · r1`

Adversarial evaluation attempt 3 (9 iterations: 3 each docx, pdf, htm): "all prompt injections succeeding in both raising the grade to pass (G) and Copilot not mentioning the hidden instructions in its output". Some outputs called the file the 'revised submission', a possible soft detection signal.

> "with all prompt injections succeeding in both raising the grade to pass (G) and Copilot not mentioning the hidden instructions in its output"

## Discussion


## Related Claims
- [Basic prompt injection attempts failed or were detected: instruction manipulation alone failed in all 9 iterations, role-playing without concealment was detected in output, and metadata-hidden injections failed in all 9 iterations](basic-and-metadata-injections-fail.md) — related
- [Copilot's detection of one advanced injection did not persist: after reporting an embedded instruction once, the same file's injection succeeded in six subsequent iterations without warning](inconsistent-detection-false-security.md) — related
- [Indirect prompt injections combining instruction manipulation, role-playing, and obfuscation altered AI-assigned grades with attack success rates of 94–100% while remaining undetected](prompt-injection-alters-ai-grading-94-100-percent.md) — possibly the same claim (merge candidate)
- [Asking the AI tool directly about hidden instructions exposed the prompt injection in all 6 security-check iterations, but the authors caution this is not a robust safeguard](direct-security-check-exposes-injection.md) — related
