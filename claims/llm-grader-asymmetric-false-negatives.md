---
type: claim
title: "In a matched-pair grading protocol, open-weight LLM graders show demographically asymmetric false-negative behaviour against second-language variants, with the most affected grader rejecting 5% of correct second-language answers it accepts in Standard English"
description: "In a matched-pair grading protocol, open-weight LLM graders show demographically asymmetric false-negative behaviour against second-language variants, with the most affected grader rejecting 5% of correct second-langu..."
id: llm-grader-asymmetric-false-negatives
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: firuz-kamalov-2026
    resource: "https://doi.org/10.48550/arXiv.2610.31041"
    title: "Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. [doi:10.48550/arXiv.2610.31041](https://doi.org/10.48550/arXiv.2610.31041)"
    author: Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# In a matched-pair grading protocol, open-weight LLM graders show demographically asymmetric false-negative behaviour against second-language variants, with the most affected grader rejecting 5% of correct second-language answers it accepts in Standard English

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Qwen2.5-7B-Instruct rejects 5% of correct second-language answers accepted in Standard English (Cohen's h = +0.45), and its confidence is lower for the second-language variant on 95% of items. [→ Firuz Kamalov 2026](#firuz-kamalov-2026)
`q2 i?` The asymmetry is grader-dependent: two of the three graders produced no hard false negatives on the bank, though their confidence was also lower for the second-language variant. [→ Firuz Kamalov 2026](#firuz-kamalov-2026)

## Evidence

### Firuz Kamalov 2026

Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. [doi:10.48550/arXiv.2610.31041](https://doi.org/10.48550/arXiv.2610.31041)

`q2 · i?` · `theoretical · r3`

Matched-pair grading protocol on 3 open-weight instruction-tuned models (4–7B class) with 40 correct and 20 incorrect free-text answers, three instruction phrasings, modal verdicts, greedy generation. The measured asymmetry for the most affected grader coincides with the simulation baseline ϵ = 0.05; the exact McNemar test on the 5-point asymmetry was not significant (p = 0.5).

> "Qwen2.5-7B-Instruct rejects 5% of the correct second-language answers that it accepts in Standard English ( ˆϵ= 0.05, Cohen’s h = +0.45), while its calibrated probability of CORRECT is lower for the second-language variant on 95% of items (paired difference ∆ P = +0.055, p = 0.043)"

## Discussion


## Related Claims
- [In a reduced mean-field model, an adaptive policy targeting a fixed success rate exhibits a bifurcation under asymmetric false-negative noise: below a critical threshold the protected group is served easier content but still learns, above it ability decays geometrically](algorithmic-drift-bifurcation-trapping-threshold.md) — related
- [GPT-4 scoring errors clustered on multiple possible answers, unrecognized vocabulary, and missed incorrect or missing answers, while faculty were overly generous graders](gpt4-faculty-error-patterns-oeq-scoring.md) — related
- [A short strict-grader preamble knocks 14 of 17 open-weights LLM graders out of the graded band on a computer-vision exam, with three stopping grading outright](llm-grader-strict-persona-collapse.md) — related
- [Surface Formatting Changes Shift LLM Grades, With No Consistent Penalty Detected](surface-formatting-changes-shift-llm-grades-without-penalising-them.md) — related
