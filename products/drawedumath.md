---
type: product
id: drawedumath
title: DrawEduMath
description: DrawEduMath is a benchmark dataset created by Li Lucy et al.
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# DrawEduMath

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
DrawEduMath is a benchmark dataset created by Li Lucy et al. that pairs authentic K–12 students’ handwritten mathematics responses with teacher captions and question–answer annotations for evaluating vision-language models.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **DrawEduMath benchmark of teacher-annotated student hand-drawn math responses**: DrawEduMath is an English-language benchmark pairing 2,030 images of real K-12 students' handwritten responses to math problems with three data types: 2.0k+ free-form teacher captions, 44.4k+ synthetic QA pairs, and 11.6k+ teacher-written QA pairs. It draws from the ASSISTments platform and a taxonomy the paper simplifies into image creation and medium, correctness & errors, and content description question types. The authors describe it as involving "noisy, naturalistic data pulled from an online learning platform," and use it to snapshot 11 VLMs' performance. (Li Lucy et al. (2026))

### Claims
- [VLMs achieve higher accuracy on non-erroneous than erroneous student math responses even when controlling for the math problem](../claims/vlms-underperform-on-erroneous-student-math-responses.md) [+M]
- [The performance gap between erroneous and non-erroneous student images persists after images are digitally redrawn to remove noise](../claims/error-gap-persists-after-image-cleanup.md) [+M]
- [Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models](../claims/binary-correctness-judgments-near-chance.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo. (2026). The Aftermath of DrawEduMath: Vision Language Models Underperform with Struggling Students and Misdiagnose Errors. https://arxiv.org/abs/2603.00925
