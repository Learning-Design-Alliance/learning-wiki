---
type: claim
title: In system cold-start scenarios, CLST outperformed every baseline KT model across all five datasets, with the largest gains at 8 training students
description: In system cold-start scenarios, CLST outperformed every baseline KT model across all five datasets, with the largest gains at 8 training students
id: clst-outperforms-baselines-cold-start
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: heeseok-jung-2025
    resource: "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    title: "Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    author: Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In system cold-start scenarios, CLST outperformed every baseline KT model across all five datasets, with the largest gains at 8 training students

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` CLST achieved higher AUC than traditional, DL-based, NLP-enhanced, global-KC, and LLM-based baselines in cold-start training sets of 8-64 students, with the margin shrinking as training students increased. [→ Heeseok Jung 2025](#heeseok-jung-2025)

## Evidence

### Heeseok Jung 2025

Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

`q2 · i?` · `design · r2`

Cold-start benchmark experiments on NIPS34, Algebra05, Assist09, Science, and Social Studies datasets, training on 8-64 students with first 50 interactions each, evaluated by AUC over five random splits. The article reports CLST "outperformed the second-best model by up to 24.52%" at 8 students, with gains decreasing to 8.71% at 64 students.

> "CLST outperformed the second-best model by up to 24.52%, 14.66%, 12.31%, and 8.71% for a training set containing 8, 16, 32, and 64 students, respectively."

## Discussion


## Related Claims
- [Fine-tuning CLST on KTLP-formatted data improved predictive performance across all datasets, with gains growing with training students](fine-tuning-improves-clst-auc.md) — related
- [Representing exercises by KC name descriptions outperformed ID-based representation when aligning an LLM to knowledge tracing](description-based-representation-beats-id-based-llm-kt.md) — related
- [BKTransformer rivals or surpasses deep KT baselines (DKT, SAKT) and BKT-EM in AUC, but DKT outperforms it on one dataset](bktransformer-rivals-deep-kt-auc.md) — related
- [DynEmb outperforms BMF and DKT baselines in future response prediction across five tutoring datasets, with AUC improvement up to 5.43% in the New User setting](dynemb-outperforms-dkt-and-bmf-baselines.md) — related
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) — related
- [On seven of eight real-world datasets, the novel BKT extensions achieve prediction performance within 0.04 AUC-ROC points of state-of-the-art models](bkt-extensions-close-to-state-of-art-auc.md) — related
- [Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.](existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial.md) — related
- [SAKT underperforms DKT on all nine datasets, contradicting previously reported results](sakt-underperforms-dkt-all-datasets.md) — related
- [Fine-tuning on KTLP data improved CLST output calibration, moving predictions closer to the ideal diagonal](fine-tuning-improves-clst-calibration.md) — related
