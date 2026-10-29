---
type: claim
title: On CK items, GradeOpt showed near-perfect alignment with human codes (κ = .88 and .85; QWK = .89 and .94), comparable to human–human agreement
description: On CK items, GradeOpt showed near-perfect alignment with human codes (κ = .88 and .85; QWK = .89 and .94), comparable to human–human agreement
id: gradeopt-near-perfect-ck-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: copur-gencturk-2026
    resource: "https://doi.org/10.1007/s11858-026-01796-2"
    title: "Copur-Gencturk, Y., Moreno, K., Chu, Y., Li, H., & Tang, J. (2026). Automated coding of content and pedagogical content knowledge of mathematics using a multi-agent large language model. ZDM – Mathematics Education. https://doi.org/10.1007/s11858-026-01796-2"
    author: "Copur-Gencturk, Y., Moreno, K., Chu, Y., Li, H., & Tang, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On CK items, GradeOpt showed near-perfect alignment with human codes (κ = .88 and .85; QWK = .89 and .94), comparable to human–human agreement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GradeOpt outperformed all other automated models on both CK items and the CK scale across all three metrics, with exact agreement exceeding 90% on both items. [→ Copur-Gencturk 2026](#copur-gencturk-2026)

## Evidence

### Copur-Gencturk 2026

Copur-Gencturk, Y., Moreno, K., Chu, Y., Li, H., & Tang, J. (2026). Automated coding of content and pedagogical content knowledge of mathematics using a multi-agent large language model. ZDM – Mathematics Education. https://doi.org/10.1007/s11858-026-01796-2

`q2 · i?` · `design · r2`

Results for the two open-ended CK items on proportional reasoning, coded with a 3-point rubric. The article states GradeOpt's performance was "comparable to that observed between the two human coders on the CK items," whose pre-adjudicated agreement was .91–.93.

> "GradeOpt outperformed all other automated coding models at both the item and scale levels across all three metrics. Specifically, the EA between GradeOpt and the human agreed-on codes exceeded 90% for both items. Similarly, Cohen's κ and QWK indicated high levels of agreement, with GradeOpt demonstrating near perfect alignment with human codes ( κ = .88 and .85; QWK = .89 and .94)."

## Discussion


## Related Claims
- [The multi-agent LLM GradeOpt achieved substantial agreement with human coders on overall PCK items (κ = .68, QWK = .79) and outperformed RoBERTa, SBERT, and naïve GPT-4o prompting](gradeopt-substantial-agreement-pck-outperforms-baselines.md) — related
- [Gaps between Cohen's κ and QWK indicate GradeOpt often assigned codes adjacent to human codes rather than entirely discrepant ones](kappa-qwk-gaps-adjacent-codes.md) — related
- [DSPy prompt optimization improves all radiotelephony evaluators, with the largest gain in accuracy (+7.9%)](dspy-optimization-communication-evaluator-gains.md) — related
- [In an AI-guided PD program, rural teachers engaged with mathematical creativity, content knowledge, and PCK as interconnected forms of reasoning rather than isolated domains](ai-guided-pd-integrated-mc-ck-pck-engagement.md) — related
- [In classroom video labeling, high raw agreement (often exceeding 90%) co-occurred with low chance-corrected κ due to temporal misalignment](raw-agreement-kappa-paradox-classroom-video.md) — related
- [Prior non-LLM automated coding approaches yielded variable and often lower agreement with human coders on teacher knowledge measures, especially PCK](prior-automated-coding-variable-lower-agreement-pck.md) — related
- [All automated models, including GradeOpt, were most challenged by knowledge of teaching mathematics items (GradeOpt κ = .59) and least challenged by knowledge of students' mathematical thinking (κ = .79)](pck-subdomain-variation-ktm-hardest.md) — related
- [AI systems perform poorly at identifying Shulman CK, PCK and GPK categories in line-by-line coding](ai-poor-shulman-coding-accuracy.md) — reports the opposite
- [GPT-3 classified students' open-ended responses about teaching practices with reliability similar to that of human coders](gpt3-coding-reliability-similar-to-humans.md) — related
