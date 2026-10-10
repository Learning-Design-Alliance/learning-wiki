---
type: claim
title: Teaching a ChatGPT agent yields significantly higher code clearness and readability scores than learning from online videos, but not higher code correctness
description: Teaching a ChatGPT agent yields significantly higher code clearness and readability scores than learning from online videos, but not higher code correctness
id: chatgpt-teachable-agent-code-clearness-readability
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: angxuan-chen-2024
    resource: "https://arxiv.org/abs/2412.15226"
    title: "Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang. (2024). Learning-by-Teaching with ChatGPT: The Effect of Teachable ChatGPT Agent on Programming Education. arXiv. https://arxiv.org/abs/2412.15226"
    author: Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang
    q: 2
    i: 3
    kind: causal
    rigour: 1
  - id: angxuan-chen-2024-2
    resource: "https://arxiv.org/abs/2412.15226"
    title: "Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang. (2024). Learning-by-Teaching with ChatGPT: The Effect of Teachable ChatGPT Agent on Programming Education. arXiv. https://arxiv.org/abs/2412.15226"
    author: Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang
    q: 2
    i: 3
    kind: causal
    rigour: 1
---

# Teaching a ChatGPT agent yields significantly higher code clearness and readability scores than learning from online videos, but not higher code correctness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2` · `i3` large

## Subclaims
`q2 i3` The experimental group scored significantly higher than the control group on code clearness and readability in the pseudocode test (F = 7.39, η2 = 0.37). [→ Angxuan Chen 2024](#angxuan-chen-2024)
`q2 i3` A second significant dimension contrast in Table 3 also favored the experimental group (F = 4.32, η2 = 0.26), though the table mislabels this row as Clearness. [→ Angxuan Chen 2024 (2)](#angxuan-chen-2024-2)

## Evidence

### Angxuan Chen 2024

Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang. (2024). Learning-by-Teaching with ChatGPT: The Effect of Teachable ChatGPT Agent on Programming Education. arXiv. https://arxiv.org/abs/2412.15226

`q2 · i3` · `causal · r1`

ANCOVA on pseudocode-test scores assigned by two experienced scorers; the experimental group "scored significantly higher in code clearness and readability compared to the control group" (F = 7.39, p < 0.01, η2 = 0.37).

> "The ANCOV A results (See Table 3) revealed that participants in the experimental group, who learned programming with the teachable agent, scored significantly higher in code clearness and readability compared to the control group, which learned through online videos (F = 7.39, p < 0.01, η2 = 0.37)."

### Angxuan Chen 2024 (2)

Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang. (2024). Learning-by-Teaching with ChatGPT: The Effect of Teachable ChatGPT Agent on Programming Education. arXiv. https://arxiv.org/abs/2412.15226

`q2 · i3` · `causal · r1`

Table 3's third scored dimension shows a significant group difference (F = 4.32, η2 = 0.26); the table labels this row Clearness, duplicating the first row's label, an apparent typo for the readability dimension described in the text.

> "Clearness EG 20 2.91 1.23 2.95 0.03 4.32** 0.26CG 21 2.81 0.58 2.83 0.02"

## Discussion


## Related Claims
- [Teaching a ChatGPT agent does not significantly improve code correctness compared with writing code independently from videos](chatgpt-teachable-agent-no-correctness-gain.md) — related
- [Students who teach a ChatGPT teachable agent in natural language achieve greater knowledge gains than students who learn the same material from online videos](chatgpt-teachable-agent-knowledge-gains.md) — related
- [Teaching a ChatGPT agent does not significantly change students' test anxiety](chatgpt-teaching-test-anxiety-no-difference.md) — related
