---
type: claim
title: Output-level Unicode soft barriers can achieve high copy-paste resistance, but effectiveness is highly model- and task-dependent
description: Output-level Unicode soft barriers can achieve high copy-paste resistance, but effectiveness is highly model- and task-dependent
id: soft-barriers-cpr-model-task-dependent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: cpr-results
    title: cpr-results
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Output-level Unicode soft barriers can achieve high copy-paste resistance, but effectiveness is highly model- and task-dependent

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across HumanEval and MBPP with four LLMs and four perturbation families, CPR varies from near zero to near perfect, so no universal Unicode barrier exists. [→ cpr-results](#cpr-results)

## Evidence

### cpr-results

Iyiola E. Olatunji, Alberick Euraste Djire, Jacques Klein, and Tegawendé F. Bissyandé. 2026. Do Not Copy/Paste: Soft Barriers for Copying in AI-Assisted Programming. Proceedings of the 41st IEEE/ACM International Conference on Automated Software Engineering (ASE '26). https://doi.org/10.1145/3832783.3834554

`q2 · i?` · `causal · r1`

Automated evaluation of four perturbation families across Claude Sonnet 4.5, DeepSeek-V3, GPT-5.2, and GPT-5.2 Codex on HumanEval and MBPP, reported in Table 3. The paper states "CPR varies widely, from near zero to near perfect" and concludes a combination of barriers would be more effective for deployment.

> "CPR varies widely, from near zero to near perfect, showing that soft-barrier effectiveness is highly dependent on the model and perturbation strategy."

## Discussion


## Related Claims
- [In an exploratory pilot, a soft barrier shifted participants from direct copying toward editing, understanding, and iterative resubmission without preventing task completion](soft-barrier-shifts-users-toward-editing.md) — a narrower finding that bears on this claim
- [Pass@1 is not a sufficient success metric for soft barriers because it conflates successful barriers with model generation failures](pass1-false-narrative-soft-barriers.md) — related
- [Automatically updating the flowchart and injecting generated code into editors drew participants away from explanations and toward direct code editing](auto-updates-drew-users-from-explanations.md) — related
