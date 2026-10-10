---
type: product
id: edu-qurating-pipeline-and-edu-qurater-scorers
title: Edu-QuRating pipeline and Edu-QuRater scorers
description: A software and trained-model package developed by Garrod et al.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Edu-QuRating pipeline and Edu-QuRater scorers

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A software and trained-model package developed by Garrod et al. that uses rubric-guided LLM preference supervision to score and curate educational text for corpus filtering, language-model training, and educational-material support.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Edu-QuRating pipeline and released Edu-QuRater scorers, rubrics, code, and models**: Edu-QuRating is a data-curation pipeline that samples text pairs from an education-rich corpus, obtains soft LLM-judge preference labels under criterion-specific rubrics, and distils them into single-text Edu-QuRater score layers with a neural Bradley–Terry objective. The core model produces six criterion-specific scores per text, with additional student- and teacher-facing foundational-literacy scorers. The article releases rubrics, source code, a nanotron fork, and trained models on Hugging Face, stating the scorers are "deployed for corpus filtering, small-language-model pre-training mixtures, and response-level GRPO rewards." (Garrod et al. (2026))

### Claims
- [Edu-QuRaters recover held-out GPT-4.1-mini pairwise educational preferences from single-text scores, with mean accuracy rising from 0.895 (Sheared-LLaMA-1.3B) to 0.917 (Gemma-3-4B-PT)](../claims/edu-quraters-distill-pairwise-educational-preferences.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425
