---
type: research-method
id: confidence-aware-selective-automated-scoring-framework
title: Confidence-aware selective automated scoring framework
description: The framework adapts a pretrained ViT with LoRA and derives a response-level confidence score from the stability of predictions under semantic-preserving test-time perturbations (crops, rotations).
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Confidence-aware selective automated scoring framework

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (1 associational, 1 design), `q2` · 1 of 2 report an effect size · 5 claims rest on one study

## Description
The framework adapts a pretrained ViT with LoRA and derives a response-level confidence score from the stability of predictions under semantic-preserving test-time perturbations (crops, rotations). The article states that "automated scoring systems must decide not only what score to assign, but also whether that score can be trusted." A Top-η test-time selection step retains only the most decisive perturbed views before aggregating the final prediction and confidence. Varying the threshold τ controls the trade-off between automated coverage and scoring risk.

## Accounts
<!-- How each source describes or uses the method -->
- **Confidence-aware selective automated scoring framework**: The framework adapts a pretrained ViT with LoRA and derives a response-level confidence score from the stability of predictions under semantic-preserving test-time perturbations (crops, rotations). The article states that "automated scoring systems must decide not only what score to assign, but also whether that score can be trusted." A Top-η test-time selection step retains only the most decisive perturbed views before aggregating the final prediction and confidence. Varying the threshold τ controls the trade-off between automated coverage and scoring risk. (Fang et al. (2026))
- **Similarity-threshold autograding architecture with teacher-controlled error constraints and a human-deferred uncertainty zone**: The article proposes an autograding framework in which fine-tuned multilingual transformer models embed question-answer pairs and score similarity to the correct answer. "Using two thresholds on the score, we can place a question-answer pair into one of three categories" — likely correct, uncertain, or likely incorrect — with uncertain pairs deferred to a human. Teachers specify minimum accuracy levels (maximum false-negative and false-positive rates), from which thresholds are computed to maximize the fraction of samples autograded while honoring the constraints. A validation procedure then compares accuracy on manually and automatically graded answers per exam. (Johannes Schneider et al. (2023))

### Claims
- [Confidence-aware selective test-time scoring achieves the best average agreement with expert rubric scoring across six NGSS drawing items](../claims/ca-selective-best-average-agreement-drawings.md) [+M]
- [The response-level confidence score correlates positively and significantly with scoring accuracy](../claims/confidence-score-correlates-scoring-accuracy.md) [+M]
- [Fine-tuned LaBSE achieves about 86.5% accuracy classifying all answers as correct or incorrect on a large multilingual dataset](../claims/finetuned-labse-86-5-percent-autograding-accuracy.md) [+M]
- [Deferring difficult question-answer pairs to humans raises grading accuracy, with 62% of samples classified at 92% accuracy](../claims/deferring-difficult-answers-raises-accuracy-92-percent.md) [+M]
- [Targeting zero false negatives and 98% accuracy leaves about a 10% teacher workload reduction with accuracy slightly above 98%](../claims/zero-false-negative-target-yields-10-percent-workload-reduction.md) [+M]

## Related Research Methods
-

## Key Sources
- Fang, L., Zhang, Y., Park, J., Wang, Z., Ma, P., Zhai, X. (2026). Confidence-Aware Automated Assessment of Student-Drawn Scientific Models. https://arxiv.org/abs/2606.20264. [doi:10.48550/arxiv.2606.20264](https://doi.org/10.48550/arxiv.2606.20264)
- Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z
