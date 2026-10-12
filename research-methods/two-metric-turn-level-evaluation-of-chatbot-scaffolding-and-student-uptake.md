---
type: research-method
id: two-metric-turn-level-evaluation-of-chatbot-scaffolding-and-student-uptake
title: Two-metric turn-level evaluation of chatbot scaffolding and student uptake
description: An evaluation pipeline that scores both sides of student-chatbot interactions at the turn level.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Two-metric turn-level evaluation of chatbot scaffolding and student uptake

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 causal, 1 associational), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
An evaluation pipeline that scores both sides of student-chatbot interactions at the turn level. As the article defines them, "We define two turn-levels metrics:Chatbot Scaffoldingas how much scaffolding the chatbot provides andStudent Uptakeas how much the student takes up the scaffolding". GPT-5-mini acts as an ordinal classifier on a 1-5 scale per turn, with turn-level scores aggregated to per-chat means; uptake is mapped onto a signed -1 to +1 scale showing who drives the chat flow. It was applied across nine datasets totalling 9,490 valid chats.

## Accounts
<!-- How each source describes or uses the method -->
- **Two-metric turn-level evaluation pipeline: Chatbot Scaffolding and Student Uptake**: An evaluation pipeline that scores both sides of student-chatbot interactions at the turn level. As the article defines them, "We define two turn-levels metrics:Chatbot Scaffoldingas how much scaffolding the chatbot provides andStudent Uptakeas how much the student takes up the scaffolding". GPT-5-mini acts as an ordinal classifier on a 1-5 scale per turn, with turn-level scores aggregated to per-chat means; uptake is mapped onto a signed -1 to +1 scale showing who drives the chat flow. It was applied across nine datasets totalling 9,490 valid chats. (Neagu et al. (2026))
- **SE and CD: outcome-oriented evaluation metrics for closed-loop Socratic tutoring assessment**: The article introduces two evaluation metrics for Socratic tutoring beyond surface fluency. Scaffolding Effectiveness (SE) measures the proportion of test questions where the tutor guides a simulated student to self-express the core concept without uttering any keyword in Ki, over up to four dialogue rounds. Conversation Depth (CD) measures the fraction of consecutive guide–student turn pairs whose Sentence-BERT embeddings have cosine similarity below 0.70, indicating semantic progression. The article notes "novelty alone does not guarantee successful scaffolding", so CD is reported with SE and leakage. The student simulator was validated against held-out real follow-ups with mean SBERT similarity 0.449±0.220. (Xiaokun Wang et al. (2026))

### Claims
- [The LLM-judge scoring pipeline for the two metrics aligns with human labels and human raters](../claims/llm-judge-pipeline-validated-against-human-raters.md) [+M]
- [GRPO alignment without the directness reward raises Socratic scaffolding effectiveness from 0.300 to 0.633 and cuts keyword leakage from 26.7% to 13.3% on held-out questions](../claims/grpo-without-directness-raises-socratic-scaffolding-effectiveness.md) [+M]
- [The best GRPO variant also achieves the highest Conversation Depth (0.722), suggesting stronger scaffolding accompanies deeper semantic progression](../claims/grpo-without-directness-highest-conversation-depth.md) [+M]

## Related Research Methods
-

## Key Sources
- Neagu, A., Wong, J. T. H., Messer, M., Nelson, R., & Johnson, P. B. (2026). Rethinking Scaffolding in LLM Tutors: The Interactional Mismatch Between Benchmarks and Real-World Deployments. Pluralistic Alignment Workshop @ ICML 2026. https://arxiv.org/abs/2606.15766
- Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996
