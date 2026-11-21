---
type: claim
title: "In a real classroom, all six evaluated LLMs except Llama-8B graded student text answers with classification accuracy between 85% and 90% against TA gold-standard grades"
description: "In a real classroom, all six evaluated LLMs except Llama-8B graded student text answers with classification accuracy between 85% and 90% against TA gold-standard grades"
id: llm-graders-match-ta-grading-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: pavlin-g-poliˇcar-2025
    resource: "https://doi.org/10.1093/bioinformatics/btaf196"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In a real classroom, all six evaluated LLMs except Llama-8B graded student text answers with classification accuracy between 85% and 90% against TA gold-standard grades

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` LLMs except Llama-8B achieved average classification accuracy of 85-90% in matching grading criteria, with Llama-8B at 75%. [→ Pavlin G. Poliˇcar 2025](#pavlin-g-policar-2025)

## Evidence

### Pavlin G. Poliˇcar 2025

Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)

`q2 · i?` · `design · r2`

Classroom evaluation in the 2024/25 Introduction to Bioinformatics course using 670 TA-graded submissions across 36 text-based exercises as gold standard, with criterion matching treated as binary classification. LLMs 'achieve strong performance, with average CA scores ranging between 85% and 90%,' while Llama-8B reached 75%.

> "Overall, LLMs achieve strong performance, with average CA scores ranging between 85% and 90%. One notable exception is Llama-8B, which achieves a relatively poor CA of 75%."

## Discussion


## Related Claims
- [LLM grading bias relative to TAs varies with question difficulty: near-zero on trivial and easy questions, mildly stringent on medium, and more generous than TAs on hard questions](llm-grading-bias-varies-by-question-difficulty.md) — related
- [LLM grading performance generally correlates with parameter count, and 4-bit quantization has negligible effect on grading performance](llm-grading-performance-scales-with-parameters.md) — related
- [Students showed no significant overall preference between LLM and TA feedback, preferred LLM feedback on correctly answered questions, and disliked only Nvidia-70B feedback on incorrect answers](students-no-significant-preference-llm-vs-ta-feedback.md) — related
