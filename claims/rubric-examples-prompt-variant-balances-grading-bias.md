---
type: claim
title: "Prompt composition shifts LLM grading bias: rubric-only prompts yield stricter grading, examples-only prompts more lenient grading, and combining both produces the best results"
description: "Prompt composition shifts LLM grading bias: rubric-only prompts yield stricter grading, examples-only prompts more lenient grading, and combining both produces the best results"
id: rubric-examples-prompt-variant-balances-grading-bias
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
source_checked: 2026-11-21
recheck_by: 2028
sources:
  - id: pavlin-g-poliˇcar-2025
    resource: "https://doi.org/10.1093/bioinformatics/btaf196"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: pavlin-g-poliˇcar-2025-2
    resource: "https://doi.org/10.1093/bioinformatics/btaf196"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: pavlin-g-poliˇcar-2025-3
    resource: "https://doi.org/10.1093/bioinformatics/btaf196"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Prompt composition shifts LLM grading bias: rubric-only prompts yield stricter grading, examples-only prompts more lenient grading, and combining both produces the best results

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-11-21 (automated, 3 of 3 entries) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Rubric-only prompts led to stricter grading with fewer matched criteria. [→ Pavlin G. Poliˇcar 2025](#pavlin-g-policar-2025)
`q2 i?` Including both grading rubric and grading examples produced the best results, a middle ground between the two single-component variants. [→ Pavlin G. Poliˇcar 2025 (2)](#pavlin-g-policar-2025-2)
`q2 i?` Examples alone were satisfactory for simpler questions but showed a marked performance drop on harder and open-ended questions, where a rubric is essential. [→ Pavlin G. Poliˇcar 2025 (3)](#pavlin-g-policar-2025-3)

## Evidence

### Pavlin G. Poliˇcar 2025

Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)

`q2 · i?` · `causal · r2`

Prompt-ablation analysis of grading bias relative to TA grades across the six LLMs: prompts that 'included only grading rubrics led to stricter grading, with LLMs less likely to match grading criteria.'

> "Prompts that included only grading rubrics led to stricter grading, with LLMs less likely to match grading criteria (Fig. 4.a)."

### Pavlin G. Poliˇcar 2025 (2)

Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)

`q2 · i?` · `causal · r2`

Same ablation study: combining components 'produced the best results, achieving a middle ground between the two individual results,' while examples-only prompts made LLMs overly generous.

> "Including both the grading rubric and grading examples produced the best results, achieving a middle ground between the two individual results."

### Pavlin G. Poliˇcar 2025 (3)

Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)

`q2 · i?` · `causal · r2`

Difficulty-stratified ablation: with examples alone, 'for harder and open-ended questions, we observe a marked drop in performance,' which the authors attribute to greater variability in student responses on such questions.

> "The results from Fig. 4.b indicate that, for simpler questions, LLMs achieve satisfactory performance using grading examples alone. However, for harder and open-ended questions, we observe a marked drop in performance."

## Discussion


## Related Claims
- [Providing a mark scheme substantially improves LLM grading accuracy and consistency, with GPT-4 shifting closest to human grades](mark-scheme-improves-llm-grading.md) — related
- [Fine-grained rubric grading of entire problems exceeds LLM bookkeeping capabilities, while parts-based grading is more reliable but misses nuances](rubric-granularity-affects-ai-grading-reliability.md) — related
- [More complex prompts tend to elicit superior results with advanced LLM versions (authors' observation)](complex-prompts-elicit-better-llm-results.md) — related
- [Students without teaching experience graded the English papers more leniently than teachers, by 5.2 and 5.7 points.](inexperienced-students-grade-more-leniently.md) — related
