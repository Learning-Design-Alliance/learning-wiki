---
type: product
id: automated-error-detection-system-aeds
title: Automated Error Detection System (AEDS)
description: A hardware-plus-display system developed by Luo Yitian et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-06
---

# Automated Error Detection System (AEDS)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 7 claims (7 for) · 2 studies (1 causal, 1 design), `q2`–`q3` · 0 of 2 report an effect size · 7 claims rest on one study

## Description
A hardware-plus-display system developed by Luo Yitian et al. that detects conductive ring-to-rail contact errors during laparoscopic box-trainer practice and provides real-time and post-training performance feedback.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Automated Error Detection System (AEDS) for laparoscopic box training**: AEDS is a hardware-plus-display add-on to a conventional laparoscopic ring-and-rail box trainer, with two components as the article defines them: "One is the automatic embedded contact device, which can collect the operator mistakes in training and record the corresponding number of errors", and an error feedback system adding an on-screen interface showing "the cumulative number of current operational errors as well as the total duration of the operation". After training, it exports tables of error times and a line-chart analysis. Error detection exploits the model's conductivity and binary circuit switching, enabling real-time mistouch feedback during practice. (Luo Yitian et al. (2025))
- **SANN-based explainable framework for automated logical error identification from program correctness alone**: The article presents a scalable framework built on a modified Subtree-based Attention Neural Network that embeds programs from their Abstract Syntax Trees and uses attention weights over subtrees to locate logical errors. Unlike prior approaches, it works 'without relying on external rubrics or test cases', training solely on binary correctness labels. The modified attention uses sigmoid activation plus an entropy regularization term so multiple errors can receive high attention while false positives are reduced. (Muntasir Hoq et al. (2025))

### Claims
- [Novice trainees' recorded operational errors fell from 78.1 to 59.4 from pre-test to post-test within Group A during laparoscopic simulation practice after AEDS activation](../claims/aeds-real-time-feedback-reduces-laparoscopic-errors-within-group.md) [+M]
- [Novices trained with AEDS feedback make fewer recorded laparoscopic errors than novices trained the same total time without AEDS feedback](../claims/aeds-group-lower-errors-than-traditional-training-group.md) [+M]
- [Novice trainees systematically underestimate their own laparoscopic error counts relative to AEDS-recorded errors](../claims/novices-underestimate-laparoscopic-errors-versus-aeds-recorded.md) [+W]
- [AEDS training produces larger confidence gains than traditional training of equal duration](../claims/aeds-confidence-gains-exceed-traditional-training.md) [+W]
- [Novice trainees' confidence in laparoscopic skill rose from pre-test to post-test within Group A after training with AEDS real-time feedback](../claims/aeds-feedback-increases-novice-confidence.md) [+W]
- [Modified SANN outperforms baseline models in predicting program correctness](../claims/sann-outperforms-baselines-correctness-prediction.md) [+M]
- [Expert evaluation shows high recall and precision for SANN-identified logical errors across five problems](../claims/sann-high-recall-precision-logical-errors.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Luo Yitian, Wang Jingjie, Yan Zongting, He Jingjing, Fu Liye, Wang Shenghan, Han Ying, Fu Yaoyu, Wang Xiandi, Li Kang, Yin Rong, Pu Dan. (2025). Enhancing laparoscopic surgery training: a comparative study of traditional models and automated error detection system. BMC Medical Education. https://doi.org/10.1186/s12909-025-07242-3
- Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. https://arxiv.org/abs/2505.10913
