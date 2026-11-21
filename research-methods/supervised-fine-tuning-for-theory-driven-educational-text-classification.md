---
type: research-method
id: supervised-fine-tuning-for-theory-driven-educational-text-classification
title: Supervised fine-tuning for theory-driven educational text classification
description: The article recommends that physics education researchers use LLMs in supervised, fine-tuned analyses of education datasets instead of relying on zero-shot or few-shot prompting alone.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# Supervised fine-tuning for theory-driven educational text classification

> **Research Method** · [All research methods](index.md)
> **Evidence** · 10 claims (6 for, 4 against) · 8 studies (4 design, 3 causal, 1 associational), `q2`–`q3` · 1 of 8 report an effect size · 10 claims rest on one study

## Description
The article recommends that physics education researchers use LLMs in supervised, fine-tuned analyses of education datasets instead of relying on zero-shot or few-shot prompting alone. It reports that "models fine-tuned with training data significantly outperformed the few-shot model", a result holding across bag of words, BERT, and LLaMA. Model choice should weigh performance against resources, since higher-resource models often but not always perform better.

## Accounts
<!-- How each source describes or uses the method -->
- **For theory-driven classification tasks in PER, use supervised fine-tuned models rather than relying on prompt engineering alone**: The article recommends that physics education researchers use LLMs in supervised, fine-tuned analyses of education datasets instead of relying on zero-shot or few-shot prompting alone. It reports that "models fine-tuned with training data significantly outperformed the few-shot model", a result holding across bag of words, BERT, and LLaMA. Model choice should weigh performance against resources, since higher-resource models often but not always perform better. (Rebeckah K. Fussell et al. (2025))
- **Fine-tuned RoBERTa-large classifier for recipient and nature of educator attention**: The article builds computational classification models of the recipient and nature of attention, tuned on 1,200 labeled utterances with preceding context. The annotated data was split 7:1:2 for train:validation:test, and a RoBERTa-large model was fine-tuned with a class-balanced loss and hyper-parameter search. "This final SoS classification model achieved a test F1 score of 71.8, and test accuracy of 72.5." The model was applied to label all 1,157,970 tutor utterances for the downstream analyses, and the article reports it outperforms most alternatives including heuristic name-detection and k-shot prompting with Claude and GPT-4, while being more cost-effective. (Qingyang Zhang et al. (2025))

### Claims
- [Few-shot LLaMA significantly underperforms even the traditional bag of words approach for skill classification](../claims/few-shot-llama-underperforms-trained-models.md) [+M]
- [Fine-tuned LLaMA models outperform bag of words and BERT across performance metrics for the QC code](../claims/llama-outperforms-bow-bert-qc-code.md) [+M]
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](../claims/gpt4-zero-shot-comparable-finetuned-classifiers.md) [-W]
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](../claims/supervised-bloom-classifiers-degrade-cross-dataset.md) [-W]
- [Zero-shot GPT-4 remains effective on imbalanced rare labels because its performance does not depend on label frequency in training data, unlike fine-tuned models.](../claims/zero-shot-gpt4-effective-on-imbalanced-rare-labels.md) [-W]
- [Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B](../claims/finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics.md) [+W]
- [Epi2Diff achieves the best performance across all four item-difficulty test sets and all reported metrics, outperforming SLM fine-tuning, LLM prompting, and supervised LLM adaptation baselines](../claims/epi2diff-best-across-four-difficulty-benchmarks.md) [+W]
- [In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task](../claims/sft-less-effective-than-prompting-for-feedback-generation.md) [-W]
- [Educators provide more individual attention to lower-achieving students than their higher-achieving peers in paired tutoring](../claims/tutors-attend-more-to-lower-achieving-students.md) [+M]
- [In mixed-gender pairs, lower-achieving female students receive less attention than higher-achieving male peers, while lower-achieving male students receive substantially more](../claims/achievement-priority-reversed-for-girls-mixed-gender.md) [+M]

## Related Research Methods
-

## Key Sources
- Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes. (2025). Comparing Large Language Models for supervised analysis of students’ lab notes. https://arxiv.org/abs/2412.10610
- Qingyang Zhang, Rose E. Wang, Ana T. Ribeiro, Dora Demszky, Susanna Loeb. (2025). Educator Attention: How computational tools can systematically identify the distribution of a key resource for students. https://arxiv.org/abs/2502.20135
