---
type: claim
title: LLM agreement with human examiners is limited in fast mode and improves in reasoning or thinking modes
description: LLM agreement with human examiners is limited in fast mode and improves in reasoning or thinking modes
id: llm-fast-mode-limited-thinking-mode-better-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: brevik-a-2026
    resource: "https://doi.org/10.3389/feduc.2026.1904452"
    title: "Brevik A, Jerpseth H and Lafontan SR (2026). Large language models as grading assistants in public health education: a method-comparison study of essay-style exam assessment. Front. Educ. 11:1904452. https://doi.org/10.3389/feduc.2026.1904452"
    author: Brevik A, Jerpseth H and Lafontan SR
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# LLM agreement with human examiners is limited in fast mode and improves in reasoning or thinking modes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`

## Subclaims
`q3 i?` Fast-mode LLM grading showed low weighted kappas with humans (0.070–0.287), while thinking mode raised agreement, most for ChatGPT (0.718). [→ Brevik A 2026](#brevik-a-2026)

## Evidence

### Brevik A 2026

Brevik A, Jerpseth H and Lafontan SR (2026). Large language models as grading assistants in public health education: a method-comparison study of essay-style exam assessment. Front. Educ. 11:1904452. https://doi.org/10.3389/feduc.2026.1904452

`q3 · i?` · `design · r2`

Single-file comparison of four LLMs against human grades on 32 submissions. Table 1 shows fast-mode kappas of 0.269 (ChatGPT), 0.287 (Gemini), 0.070 (LeChat), 0.227 (Kimi); thinking mode improved these, and "the LLMs utilized more of the full grading scale" in thinking mode.

> "The weighted Cohen's kappa measuring inter-rater reliability for grading method comparisons indicated that the agreement between human graders and fast LLM grading was not high."

## Discussion


## Related Claims
- [ChatGPT in thinking mode shows the strongest agreement with human examiners on essay-style exam grading (weighted kappa 0.718)](chatgpt-thinking-mode-strongest-human-grading-agreement.md) — a narrower finding that bears on this claim
- [Kimi shows reasonable but weaker agreement with human examiners than ChatGPT (weighted kappa 0.571)](kimi-reasonable-human-grading-agreement.md) — a narrower finding that bears on this claim
- [LLMs use fewer extreme grades than human examiners, with grade-dependent opposing biases compressing grades toward the middle](llm-central-tendency-grade-compression.md) — related
- [Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)](hint-prompts-raise-llm-scoring-agreement.md) — related
- [Prior non-LLM automated coding approaches yielded variable and often lower agreement with human coders on teacher knowledge measures, especially PCK](prior-automated-coding-variable-lower-agreement-pck.md) — related
- GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it — related
- [Human inter-rater agreement for FRISCO essay scoring was reliable, with mean kappa 0.78–0.84 and percentage of agreement above 75% in all six dimensions](frisco-rater-agreement-reliable.md) — related
- [LLM graders show model-specific precision/recall trade-offs, so a single metric is insufficient to judge grading quality](llm-grader-precision-recall-tradeoffs-single-metric-insufficient.md) — related
- [Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades](claude3-palm2-substantial-agreement-failing-grades.md) — related
- [Newer LLM generations do not consistently agree better with human essay graders](no-consistent-generational-improvement-llm-grading.md) — related
