---
type: claim
title: Effective AI help-seeking is itself a skill unevenly distributed among students, and access to an assistant is not equivalent to effective help-seeking
description: Effective AI help-seeking is itself a skill unevenly distributed among students, and access to an assistant is not equivalent to effective help-seeking
id: ai-help-seeking-is-a-skill
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-17
recheck_by: 2031
sources:
  - id: qusay-h-mahmoud-2026
    resource: "https://doi.org/10.48550/arxiv.2609.29473"
    title: "Qusay H. Mahmoud. (2026). Judgment-Centred Software Engineering Education: A Post-Hype Review and Framework for AI-Augmented Learning. Preprint, September 2026. https://arxiv.org/abs/2609.29473 [doi:10.48550/arxiv.2609.29473](https://doi.org/10.48550/arxiv.2609.29473)"
    author: Qusay H. Mahmoud
    q: 2
    i: "?"
    kind: review
    rigour: 2
  - id: qusay-h-mahmoud-2026-2
    resource: "https://arxiv.org/abs/2609.29473"
    title: "Qusay H. Mahmoud. (2026). Judgment-Centred Software Engineering Education: A Post-Hype Review and Framework for AI-Augmented Learning. Preprint, September 2026. https://arxiv.org/abs/2609.29473"
    author: Qusay H. Mahmoud
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Effective AI help-seeking is itself a skill unevenly distributed among students, and access to an assistant is not equivalent to effective help-seeking

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-17 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2031: baselines and conditions change

## Subclaims
`q2 i?` In an ACE 2024 survey of 47 computing students with eight interviews, GenAI had not displaced traditional help resources; preferences varied with task, quality, latency, and trustworthiness. [→ Qusay H. Mahmoud 2026](#qusay-h-mahmoud-2026)
`q2 i?` In a 12-week deployment with 52 students, most of more than 2,500 queries sought immediate assignment help and students often supplied minimal contextual information. [→ Qusay H. Mahmoud 2026 (2)](#qusay-h-mahmoud-2026-2)

## Evidence

### Qusay H. Mahmoud 2026

Qusay H. Mahmoud. (2026). Judgment-Centred Software Engineering Education: A Post-Hype Review and Framework for AI-Augmented Learning. Preprint, September 2026. https://arxiv.org/abs/2609.29473 [doi:10.48550/arxiv.2609.29473](https://doi.org/10.48550/arxiv.2609.29473)

`q2 · i?` · `review · r2`

The review reports Hou et al.'s ACE 2024 study combining a survey of 47 computing students with eight interviews: "GenAI had not displaced traditional help resources", with preliminary evidence that effective AI help-seeking is itself a skill unevenly distributed.

> "Hou et al. [2024a] found that GenAI had not displaced traditional help resources; preferences varied with the task and with perceived quality, latency, and trustworthiness."

### Qusay H. Mahmoud 2026 (2)

Qusay H. Mahmoud. (2026). Judgment-Centred Software Engineering Education: A Post-Hype Review and Framework for AI-Augmented Learning. Preprint, September 2026. https://arxiv.org/abs/2609.29473

`q2 · i?` · `associational · r1`

The review reports Sheese et al.'s 12-week deployment with 52 students and more than 2,500 queries: most sought immediate assignment help, fewer pursued conceptual understanding, and "students often supplied minimal contextual information".

> "A complementary 12-week deployment of an LLM-powered programming assistant with 52 students captured more than 2,500 queries: most sought immediate help with programming assignments, fewer pursued broader conceptual understanding, and students often supplied minimal contextual information"

## Studies bearing on this claim

<!-- synthesis:start -->
*Do learners ask for on-demand help when they need it, and can that be taught?* This table gathers the studies behind this claim and the 4 narrower claims that bear on it: **5 distinct studies** (2 associational, 2 causal, 1 review), `q2`–`q3`, 1 of 5 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Qusay H. Mahmoud 2026](https://doi.org/10.48550/arxiv.2609.29473) | q2 · review · r2 | i? | this claim |
| [Andy Gray 2026](https://doi.org/10.48550/arxiv.2609.21600) | q2 · associational · r1 | i? | [Undergraduate computing students report help-seeking avoidance and anxiety, with 62.5% som](students-avoid-help-seeking-despite-need.md) (supports) |
| Kai 2018 | q2 · associational · r2 | i? | [Not requesting any hints in at least one problem is related to greater wheel-spinning, con](hint-avoidance-related-greater-wheel-spinning.md) (supports) |
| [Azimi 2026](https://doi.org/10.48550/arxiv.2609.16784) | q2 · causal · r1 | i? | [The Coach's hint budget was managed poorly: students split into early-spenders and savers,](hint-budget-mismanaged-two-patterns.md) (supports) |
| [Hyoungwook Jin 2026](https://doi.org/10.48550/arxiv.2609.28918) | q3 · causal · r2 | i3 | [HelpCoach led to greater knowledge retention one week later than pre-task help-seeking tra](helpcoach-greater-knowledge-retention-one-week.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims

- [Post-training GenAI use patterns were unevenly distributed: efficient collaborators were the largest profile (47.5%), followed by over-revisers (26.2%) and mixed users (21.2%)](uneven-post-training-genai-use-patterns.md) — related
- Students shifted AI usage toward debugging and concept explanation over the semester, with 31 of 89 reporting more debugging use — related
- [Student-agent interaction produced far more help-seeking but a non-uniform cognitive distribution dominated by lower-order engagement (54.52%), unlike the balanced distribution of student-instructor interaction](agent-context-lower-order-dominance.md) — related
- [More than half of participants' ChatGPT queries sought knowledge or advice, with methodological knowledge and classroom management the largest prompt categories](chatgpt-queries-sought-knowledge-advice.md)
- [HelpCoach led to greater knowledge retention one week later than pre-task help-seeking training alone](helpcoach-greater-knowledge-retention-one-week.md) — related
- [Not requesting any hints in at least one problem is related to greater wheel-spinning, consistent with help avoidance](hint-avoidance-related-greater-wheel-spinning.md) — related
- [The Coach's hint budget was managed poorly: students split into early-spenders and savers, and within the Coach condition only those with a deliberate hint strategy scored higher](hint-budget-mismanaged-two-patterns.md) — related
- [Students' critical examination of AI-generated outputs increased across learning cycles, though unevenly, with some participants continuing to seek confirmation from AI](critical-evaluation-of-ai-outputs-increased-unevenly.md) — related
- [Undergraduate computing students report help-seeking avoidance and anxiety, with 62.5% sometimes avoiding asking for help even when needed and 75% reporting anxiety when not understanding a topic](students-avoid-help-seeking-despite-need.md) — related
