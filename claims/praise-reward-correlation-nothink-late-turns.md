---
type: claim
title: The positive correlation between tutor Praise rate and total reward is concentrated in NoThink dialogs and localized to closing turns, with null or negative effects under Think variants
description: The positive correlation between tutor Praise rate and total reward is concentrated in NoThink dialogs and localized to closing turns, with null or negative effects under Think variants
id: praise-reward-correlation-nothink-late-turns
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: unggi-lee-2026
    resource: "https://doi.org/10.48550/arXiv.2605.27088"
    title: "Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon. (2026). LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring. arXiv preprint. [doi:10.48550/arXiv.2605.27088](https://doi.org/10.48550/arXiv.2605.27088)"
    author: Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon
    q: 2
    i: 1
    kind: design
    rigour: 2
---

# The positive correlation between tutor Praise rate and total reward is concentrated in NoThink dialogs and localized to closing turns, with null or negative effects under Think variants

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i1` small
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i1` Across 22,126 labeled dialogs, dialog-level Praise rate correlates positively with Rtotal in the NoThink condition (ρ = +0.106, p < 10−15) while Think variants show null or slightly negative effects, with the effect localized to T4+ turns (ρ(Rtotal) = +0.110). [→ Unggi Lee 2026](#unggi-lee-2026)

## Evidence

### Unggi Lee 2026

Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon. (2026). LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring. arXiv preprint. [doi:10.48550/arXiv.2605.27088](https://doi.org/10.48550/arXiv.2605.27088)

`q2 · i1` · `design · r2`

Appendix C.11 Spearman correlation analysis over n = 22,126 labeled dialogs, decomposed by reasoning condition and turn position (Tables 13–14), with Benjamini-Hochberg correction. NoThink ρ(Rtotal) = +0.106 is a small printed effect size; T4+ ρ(Rtotal) = +0.110.

> "the positive correlation between Praise rate and Rtotal is concentrated in the NoThink condition, while Think variants show null or slightly negative effects."

## Discussion


## Related Claims
- [Pedagogical prompting increases mathematical problem-solving content and reduces excessive praise in tutor responses](pedagogical-prompting-shifts-tutor-behavior.md) — related
- [Enabling internal thinking dramatically improves LLM tutor performance in simulated mathematics tutoring (+134% Delta Solve Rate, +306% Helpful Rate)](thinking-capability-improves-llm-tutoring.md) — related
- [A 1970 teacher self-analysis programme asserts, without data, that teacher responses including verbal rewards can close off pupil thinking](teacher-responses-can-close-off-pupil-thinking.md) — related
- [Within high-performance methods, successful tutoring dialogs deploy fewer step-by-step instructions and more exploratory questions, with praise reserved for late turns](successful-dialogs-fewer-stepwise-more-exploratory.md) — related
- [In speech-augmented demonstrations, mean pitch correlates with reward magnitude: higher-pitch \"yes\" utterances accompany higher returns and higher-pitch \"no\" utterances lower returns](pitch-correlates-reward-magnitude-demonstrations.md) — related
