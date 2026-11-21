---
type: claim
title: ParLD (GPT-4.1) outperforms traditional knowledge-tracing baselines on final-turn performance prediction on MathDial and CoMTA
description: ParLD (GPT-4.1) outperforms traditional knowledge-tracing baselines on final-turn performance prediction on MathDial and CoMTA
id: parld-outperforms-kt-baselines-performance-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: fangzhou-yao-2026
    resource: "https://doi.org/10.1609/aaai.v40i40.40736"
    title: "Fangzhou Yao, Sheng Chang, Weibo Gao, Qi Liu. (2026). Conversational Learning Diagnosis via Reasoning Multi-Turn Interactive Learning. [doi:10.1609/aaai.v40i40.40736](https://doi.org/10.1609/aaai.v40i40.40736)"
    author: Fangzhou Yao, Sheng Chang, Weibo Gao, Qi Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ParLD (GPT-4.1) outperforms traditional knowledge-tracing baselines on final-turn performance prediction on MathDial and CoMTA

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the MathDial dataset, ParLD (GPT-4.1) surpasses the best-performing KT baseline (DKT) by a margin of 10% in accuracy, and achieves state-of-the-art accuracy and F1 on both MathDial and CoMTA. [→ Fangzhou Yao 2026](#fangzhou-yao-2026)

## Evidence

### Fangzhou Yao 2026

Fangzhou Yao, Sheng Chang, Weibo Gao, Qi Liu. (2026). Conversational Learning Diagnosis via Reasoning Multi-Turn Interactive Learning. [doi:10.1609/aaai.v40i40.40736](https://doi.org/10.1609/aaai.v40i40.40736)

`q2 · i?` · `design · r2`

Comparison experiment (RQ1) on MathDial (2,861 dialogues) and a curated 116-conversation CoMTA subset, comparing ParLD against DKT, AKT, DKVMN, SAINT and SimpleKT using accuracy and F1 at the final turn. Table 1 reports ParLD (GPT-4.1) at 68.72 ACC on MathDial and 57.26 on CoMTA, with the article stating it "outperforming all traditional KT models".

> "Table 1 demonstrates that ParLD (GPT-4.1) achieves state-of-the-art performance on both the Mathdial and CoMTA datasets, outperforming all traditional KT models."

## Discussion


## Related Claims
- [LLMKT outperforms existing knowledge tracing methods at predicting student turn correctness in the CoMTA and MathDial tutoring dialogue datasets, and generally outperforms DKT-Sem.](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md) — related
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) — related
- [An IRT-based difficulty-aware conversational KT framework improves AUC over the LLMKT baseline on both QATD2k and MathDial](irt-difficulty-aware-kt-beats-llmkt-auc.md) — related
- [DKT-Sem, a DKT variant using semantic text embeddings, performs better than existing KT methods on tutoring dialogues, with a smaller margin on the larger MathDial dataset.](dkt-sem-outperforms-existing-kt-methods-most-with-little-training-data.md) — related
- [Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.](existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial.md) — related
- [Among deep learning KT models, simpler DKT performs comparably to complex architectures under limited dialogue data](dkt-comparable-to-complex-kt-architectures.md) — related
- [ParLD-guided tutoring instructions raise simulated students' correct-answer rate to 72.22% versus 56.48% for Direct Respond on MathDial](parld-tutoring-simulation-higher-correct-rate.md) — related
