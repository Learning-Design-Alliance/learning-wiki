---
type: claim
title: "Basic prompt injection attempts failed or were detected: instruction manipulation alone failed in all 9 iterations, role-playing without concealment was detected in output, and metadata-hidden injections failed in all 9 iterations"
description: "Basic prompt injection attempts failed or were detected: instruction manipulation alone failed in all 9 iterations, role-playing without concealment was detected in output, and metadata-hidden injections failed in all..."
id: basic-and-metadata-injections-fail
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
    kind: causal
    rigour: 1
---

# Basic prompt injection attempts failed or were detected: instruction manipulation alone failed in all 9 iterations, role-playing without concealment was detected in output, and metadata-hidden injections failed in all 9 iterations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Attempt 1 (instruction manipulation only) failed in all 9 iterations, with Copilot disabling the chat without reporting the attempt; attempt 2 changed the grade but referenced the hidden injection in its output; attempt 4 (metadata-hidden) failed in all 9 iterations. [→ Niklas Humble 2026](#niklas-humble-2026)

## Evidence

### Niklas Humble 2026

Niklas Humble. (2026). Ethical Implications of Prompt Injection in AI-mediated Grading: An Adversarial Red-Team Evaluation. Journal of Academic Ethics. https://doi.org/10.1007/s10805-026-09758-9

`q2 · i?` · `causal · r1`

Adversarial evaluation attempt 4: injections hidden as file comments, split between metadata and document end, and as html comments all failed; "all prompt injections failing". Copilot graded fail (U) with no mention of the attempts. Attempts 1 and 2 also failed per the Results section.

> "In total, 9 iterations were made at hiding the prompt injection in different parts of file metadata, with all prompt injections failing"

## Discussion


## Related Claims
- [A revised injection combining instruction manipulation and role-playing with an explicit do-not-mention instruction succeeded in all 9 iterations across docx, pdf, and htm formats](revised-injection-roleplay-undetected-all-formats.md) — related
- [Indirect prompt injections combining instruction manipulation, role-playing, and obfuscation altered AI-assigned grades with attack success rates of 94–100% while remaining undetected](prompt-injection-alters-ai-grading-94-100-percent.md) — related
- [Copilot's detection of one advanced injection did not persist: after reporting an embedded instruction once, the same file's injection succeeded in six subsequent iterations without warning](inconsistent-detection-false-security.md) — related
- [Asking the AI tool directly about hidden instructions exposed the prompt injection in all 6 security-check iterations, but the authors caution this is not a robust safeguard](direct-security-check-exposes-injection.md) — related
- [Deterrence layers failed because seeds changed parameters rather than task structure, scaffolding exposed solution steps, and hidden grading verified output consistency rather than authorship or understanding](why-qiskit-deterrence-layers-failed.md) — related
