---
type: claim
title: GPT-2 outperformed an LSTM-based RNN on word perplexity, readability, and cosine-similarity coherence when generating MOOC forum replies
description: GPT-2 outperformed an LSTM-based RNN on word perplexity, readability, and cosine-similarity coherence when generating MOOC forum replies
id: gpt2-outperformed-rnn-mooc-nlg
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: chenglu-li-wanli-xing-2021
    resource: "https://doi.org/10.1007/s40593-020-00235-x"
    title: "Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x"
    author: "Chenglu Li & Wanli Xing"
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: chenglu-li-wanli-xing-2021-2
    resource: "https://doi.org/10.1007/s40593-020-00235-x"
    title: "Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x"
    author: "Chenglu Li & Wanli Xing"
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: chenglu-li-wanli-xing-2021-3
    resource: "https://doi.org/10.1007/s40593-020-00235-x"
    title: "Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x"
    author: "Chenglu Li & Wanli Xing"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-2 outperformed an LSTM-based RNN on word perplexity, readability, and cosine-similarity coherence when generating MOOC forum replies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-2 achieved lower word perplexity (37.94 vs 151.41) than the RNN model on the testing set. [→ Chenglu Li & Wanli Xing 2021](#chenglu-li-wanli-xing-2021)
`q2 i?` GPT-2's average F-K grade level (10.10) was much closer to original replies (8.73) than RNN's (22.68). [→ Chenglu Li & Wanli Xing 2021 (2)](#chenglu-li-wanli-xing-2021-2)
`q2 i?` GPT-2's average cosine similarity with posts (0.57) was closer to original replies (0.58) than RNN's (0.52). [→ Chenglu Li & Wanli Xing 2021 (3)](#chenglu-li-wanli-xing-2021-3)

## Evidence

### Chenglu Li & Wanli Xing 2021

Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x

`q2 · i?` · `design · r2`

Quantitative evaluation of the two trained NLG models on the 2770-post testing set, reported in Results with Table 3. The description notes lower perplexity is preferred: "lower word perplexity is preferred as it suggests a model is more confident".

> "The word perplexity of 37.94 of GPT-2 suggests the GPT-2 model is much more confident in predicting the next word given a context, compared to the word perplexity of 151.41 of the RNN model."

### Chenglu Li & Wanli Xing 2021 (2)

Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x

`q2 · i?` · `design · r2`

Results-section comparison of F-K grade levels computed with the textstat package; original replies served as the benchmark. GPT-2's scores concentrated in the favorable 3-13 range while RNN showed more extreme scores.

> "Compared with the RNN model 's average F-K grade level of 22.68 ( SD =2 2 . 0 1 ) , the GPT-2 model has an average F-K grade level of 10.10 (SD = 13.40). The average F-K grade level of GPT-2 is much closer to that of the original replies ( M =8 . 7 3 ,SD = 9.20)."

### Chenglu Li & Wanli Xing 2021 (3)

Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x

`q2 · i?` · `design · r2`

Results-section cosine-similarity evaluation using BERT word embeddings; GPT-2 averaged 0.57 (SD = 0.22) versus RNN's 0.52 (SD = 0.17) and original replies' 0.58 (SD = 0.18).

> "Therefore, the GPT-2 model is considered capable of generating more coherent replies than the RNN model, since the average cosine similarity of GPT-2 is closer to that of the original replies."

## Discussion


## Related Claims
- [The special issue reports that a GPT-2 model could provide supportive and contextual replies to MOOC learners to a similar extent as humans](gpt2-mooc-forum-replies-similar-to-humans.md) — related
- [A small validation survey found the trained GPT-2 model generated supportive, contextual replies comparable to humans and generalizable to a new similar MOOC](gpt2-survey-validation-generalizable.md) — related
- [Gemma and LLaMA produce higher-quality responses than GPT-2 by TIGERSCORE, with accuracy and comprehension gaps remaining](gemma-llama-outperform-gpt2-tigerscore.md) — related
