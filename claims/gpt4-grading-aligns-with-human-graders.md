---
type: claim
title: "GPT-4-based grading of open answers aligns moderately with expert human graders, with an average grade difference of 2.75%"
description: "GPT-4-based grading of open answers aligns moderately with expert human graders, with an average grade difference of 2.75%"
id: gpt4-grading-aligns-with-human-graders
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: borges-2024
    resource: "https://doi.org/10.1073/pnas.2414955121"
    title: "Borges, et al. (2024). Could ChatGPT get an Engineering Degree? Evaluating Higher Education Vulnerability to AI Assistants. [doi:10.1073/pnas.2414955121](https://doi.org/10.1073/pnas.2414955121)"
    author: Borges, et al
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4-based grading of open answers aligns moderately with expert human graders, with an average grade difference of 2.75%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 11 courses, human and GPT-4 grading of open-answer responses differ on average by only 2.75%, though per-course deviations average 8.5% and GPT-4 avoids labeling solutions Incorrect. [→ Borges 2024](#borges-2024)

## Evidence

### Borges 2024

Borges, et al. (2024). Could ChatGPT get an Engineering Degree? Evaluating Higher Education Vulnerability to AI Assistants. [doi:10.1073/pnas.2414955121](https://doi.org/10.1073/pnas.2414955121)

`q2 · i?` · `design · r2`

Human grading study with 28 expert annotators from 11 courses evaluating 933 questions (3,732 answers) generated with two prompting strategies (Figure 6). The article reports "a difference in average grade of only 2.75%" and course deviations averaging 8.5%. No effect size is printed.

> "upon comparing average grades assigned by human graders and GPT-4 across 11 courses, we find a difference in average grade of only 2.75%. However, we observe variations between courses, with an average course grade deviation of 8.5% (and the largest deviation for a course being 26%)"

## Discussion


## Related Claims
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — a broader claim this one bears on
- [Newer LLM generations such as GPT-4 generally outperform GPT-3.5 in short-answer grading accuracy, but this advantage is not consistent across all tasks and domains](gpt4-advantage-uneven-across-tasks.md) — related
- [LLMs perform worse on complex, open-ended, or subjective assignments than on short, clearly formulated answers](llm-struggle-open-ended-subjective-tasks.md) — related
- [Most faculty–GPT-4 scoring discrepancies were only one-point differences, shrinking across iterations](oeq-scoring-discrepancies-mostly-one-point.md) — related
- [LLM marking agrees with human markers on only about half of graded Physics answers, and assigns higher, less variable normalized scores than humans](llm-marking-concordance-with-humans-about-half.md) — related
- [AAG system scores align closely with human TA scores on open-ended statistics questions, with Pearson correlations of 0.75 and 0.82](aag-ta-score-correlation-open-ended.md) — related
