---
type: claim
title: "MELD analysis found no completion matched the MRCP sample paper at 95% or more, suggesting ChatGPT-4 was unlikely trained on it"
description: "MELD analysis found no completion matched the MRCP sample paper at 95% or more, suggesting ChatGPT-4 was unlikely trained on it"
id: meld-analysis-suggests-no-mrcp-training-data-memorisation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-31
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: vij-o-2024
    resource: "https://doi.org/10.1371/journal.pone.0307372"
    title: "Vij O, Calver H, Myall N, Dey M, Kouranloo K. (2024). Evaluating the competency of ChatGPT in MRCP Part 1 and a systematic literature review of its capabilities in postgraduate medical assessments. PLOS ONE. https://doi.org/10.1371/journal.pone.0307372"
    author: Vij O, Calver H, Myall N, Dey M, Kouranloo K.
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# MELD analysis found no completion matched the MRCP sample paper at 95% or more, suggesting ChatGPT-4 was unlikely trained on it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Applying the memorisation effects Levenshtein detector (MELD) with GPT-4's API at temperature 0, none of GPT-4's completions shared a 95% or greater overlap with the MRCP sample questions. [→ Vij O 2024](#vij-o-2024)

## Evidence

### Vij O 2024

Vij O, Calver H, Myall N, Dey M, Kouranloo K. (2024). Evaluating the competency of ChatGPT in MRCP Part 1 and a systematic literature review of its capabilities in postgraduate medical assessments. PLOS ONE. https://doi.org/10.1371/journal.pone.0307372

`q1 · i?` · `design · r2`

Algorithmic memorisation check in which all 197 sample questions and answers were tokenised, split into pairs, and the first half inserted into GPT-4 with output matched to the second half; no completion exceeded a 95% match. The code was released on GitHub.

> "Following the implementation of MELD, none of GPT-4's completions had greater than a 95% match with the MRCP (UK) Part 1 sample paper questions, indicating that it is unlikely ChatGPT-4 was trained on this data set."

## Discussion


## Related Claims
- [ChatGPT-3.5 and ChatGPT-4 both score significantly above the historical MRCP Part 1 pass mark on the sample paper](chatgpt-scores-above-mrcp-part1-pass-mark.md) — related
- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](bootstrapping-self-consistency-flags-incorrect-answers.md) — related
- [Self-consistency did not improve GPT-4's answer accuracy on these exams, unlike in chain-of-thought tasks](self-consistency-no-accuracy-gain-reading-exams.md) — related
