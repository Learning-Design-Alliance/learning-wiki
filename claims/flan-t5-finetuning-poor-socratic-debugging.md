---
type: claim
title: Fine-tuned Flan-T5 models perform very poorly on held-out Socratic debugging dialogues
description: Fine-tuned Flan-T5 models perform very poorly on held-out Socratic debugging dialogues
id: flan-t5-finetuning-poor-socratic-debugging
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: erfan-al-hossami-2024
    resource: "https://doi.org/10.1145/3626252.3630799"
    title: "Erfan Al-Hossami, Razvan Bunescu, Justin Smith and Ryan Teehan. (2024). Can Language Models Employ the Socratic Method? Experiments with Code Debugging. arXiv. Originally published 2023. [doi:10.1145/3626252.3630799](https://doi.org/10.1145/3626252.3630799)"
    author: Erfan Al-Hossami, Razvan Bunescu, Justin Smith and Ryan Teehan
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned Flan-T5 models perform very poorly on held-out Socratic debugging dialogues

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Fine-tuned Flan-T5 (small, base, large) performed very poorly on a held-out test set of 16 dialogues around unseen programming exercises. [→ Erfan Al-Hossami 2024](#erfan-al-hossami-2024)

## Evidence

### Erfan Al-Hossami 2024

Erfan Al-Hossami, Razvan Bunescu, Justin Smith and Ryan Teehan. (2024). Can Language Models Employ the Socratic Method? Experiments with Code Debugging. arXiv. Originally published 2023. [doi:10.1145/3626252.3630799](https://doi.org/10.1145/3626252.3630799)

`q1 · i?` · `design · r2`

Fine-tuning experiment with Flan-T5 models (learning rate 1e-5, Adam optimizer, effective batch size 32, 20 epochs). The authors attribute the low performance to low prior exposure of Flan-T5 to code dialogues and Socratic questioning.

> "How ever, the ﬁne-tuned LMs performed very poorly on a held-out test se t of 16 dialogues around unseen programming exercises."

## Discussion


## Related Claims
- [Supervised fine-tuning on SocraticEdu provides the largest single-step SE gain (+0.200) but still leaks target terms in 26.7% of dialogues](sft-largest-single-step-gain-but-still-leaks.md) — related
- [Multilingual XLM-Longformer fine-tuning fails on Basque and Spanish science corpora while the English Longformer succeeds](xlm-longformer-fails-basque-spanish.md) — related
- [Zero-shot GPT-4 with iterative prompt engineering achieves 77.30% dialogue act recognition accuracy, outperforming fine-tuned T5, CRF, and BLSTM baselines on a held-out test set.](gpt4-zero-shot-dialogue-act-recognition-outperforms-t5-baselines.md) — reports the opposite
- [GPT-4 outperforms fine-tuned T5 by a normalized accuracy improvement of 5.73% for dialogue act recognition on the same held-out test set.](gpt4-normalized-accuracy-improvement-5-73-percent-over-t5.md) — reports the opposite
- [Prompt refinements targeting inter-label confusion yield superior recall rates for challenging dialogue act labels, including Command (F1 raised to 0.75) and Other (GPT-4 recall 0.67 vs. T5 0.54).](prompt-refinements-improve-recall-challenging-dialogue-acts.md) — related
- [Zero-shot GPT-4 remains effective on imbalanced rare labels because its performance does not depend on label frequency in training data, unlike fine-tuned models.](zero-shot-gpt4-effective-on-imbalanced-rare-labels.md) — reports the opposite
- [Grading skill transfers across exams: an adapter fine-tuned on one exam improves grading on the unseen other, though transfer stops short of in-domain performance](grading-skill-transfers-across-exams.md) — related
- [Iterative prompt engineering stages progressively improve GPT-3.5 dialogue act recognition accuracy from 0.369 to 0.631 on the training set.](iterative-prompt-engineering-improves-gpt-dialogue-act-accuracy.md) — related
- [GPT-4 performs exceptionally well on coding tasks and simple single-step problems, but poorly on multi-step problems, longer prose, and interdisciplinary problems.](gpt4-strong-coding-weak-multistep-prose.md) — related
- [The fine-tuned model generalized to out-of-domain lessons with 77% overall accuracy](fine-tuned-model-out-of-domain-77.md) — related
