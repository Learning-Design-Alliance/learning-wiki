---
type: claim
title: Gold answer leakage in generated hints is low for the main tutor model but higher for low-resource languages
description: Gold answer leakage in generated hints is low for the main tutor model but higher for low-resource languages
id: gold-answer-leakage-low-lrl-higher
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: junior-cedric-tonga-2026
    resource: "https://doi.org/10.18653/2026.mathnlp-main.16"
    title: "Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar. (2026). Simulating Student-Tutor Interactions with LLMs for Multilingual Math Feedback. arXiv. Originally published 2025. [doi:10.18653/2026.mathnlp-main.16](https://doi.org/10.18653/2026.mathnlp-main.16)"
    author: Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Gold answer leakage in generated hints is low for the main tutor model but higher for low-resource languages

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Regex-based leakage detection found roughly 2% leakage for LLaMA-3.3-70B versus about 8% for the smaller tutor, with leakage rates higher for low-resource languages. [→ Junior Cedric Tonga 2026](#junior-cedric-tonga-2026)

## Evidence

### Junior Cedric Tonga 2026

Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar. (2026). Simulating Student-Tutor Interactions with LLMs for Multilingual Math Feedback. arXiv. Originally published 2025. [doi:10.18653/2026.mathnlp-main.16](https://doi.org/10.18653/2026.mathnlp-main.16)

`q2 · i?` · `causal · r2`

Gold Answer Leakage test using regex detection over hints generated across four strategies and both tutors; the authors report "The highest observed answer leakage was approximately 8% for LLaMA-3.3-8B and around 2% for LLaMA-3.3-70B," and note leakage is higher for low-resource languages.

> "The highest observed answer leakage was approximately 8% for LLaMA-3.3-8B and around 2% for LLaMA-3.3-70B."

## Discussion


## Related Claims
- [A larger tutor model (LLaMA-3.3-70B) yields greater student gains than a smaller one, especially for low-resource languages](larger-tutor-model-greater-student-gains.md) — related
- [Hint language substantially impacts student gains, with English hints generally most effective from larger tutors but native-language hints competitive in specific cases](hint-language-impacts-student-gains.md) — related
- [Single-turn tutors disclose answers pervasively while challenge scores are near zero across every model and subject](single-turn-answer-disclosure-challenge-near-zero.md) — related
