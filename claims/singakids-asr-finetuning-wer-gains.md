---
type: claim
title: "Fine-tuning Whisper on local Malay and Tamil speech data lowers WER, especially on children's speech"
description: "Fine-tuning Whisper on local Malay and Tamil speech data lowers WER, especially on children's speech"
id: singakids-asr-finetuning-wer-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: zhengyuan-liu-2025
    resource: "https://doi.org/10.18653/v1/2025.acl-industry.86"
    title: "Zhengyuan Liu, Geyu Lin, Hui Li Tan, Huayun Zhang, Yanfeng Lu, Xiaoxue Gao, Stella Xin Yin, He Sun, Hock Huan Goh, Lung Hsiang Wong, Nancy F. Chen. (2025). SingaKids: A Multilingual Multimodal Dialogic Tutor for Language Learning. arXiv preprint. [doi:10.18653/v1/2025.acl-industry.86](https://doi.org/10.18653/v1/2025.acl-industry.86)"
    author: Zhengyuan Liu, Geyu Lin, Hui Li Tan, Huayun Zhang, Yanfeng Lu, Xiaoxue Gao, Stella Xin Yin, He Sun, Hock Huan Goh, Lung Hsiang Wong, Nancy F. Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuning Whisper on local Malay and Tamil speech data lowers WER, especially on children's speech

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fine-tuning Whisper-large-V3 with local Malay and Tamil data reduced word error rates across conversational and children speech test sets, with the largest gains on children's voices. [→ Zhengyuan Liu 2025](#zhengyuan-liu-2025)

## Evidence

### Zhengyuan Liu 2025

Zhengyuan Liu, Geyu Lin, Hui Li Tan, Huayun Zhang, Yanfeng Lu, Xiaoxue Gao, Stella Xin Yin, He Sun, Hock Huan Goh, Lung Hsiang Wong, Nancy F. Chen. (2025). SingaKids: A Multilingual Multimodal Dialogic Tutor for Language Learning. arXiv preprint. [doi:10.18653/v1/2025.acl-industry.86](https://doi.org/10.18653/v1/2025.acl-industry.86)

`q2 · i?` · `design · r2`

Technical evaluation comparing Whisper-large-V3 with the fine-tuned model on Malay data, using a local dataset of 2,800-hour Tamil and 1,000-hour Malay recordings from more than 1,000 native speakers. The quote's WER reductions are on Malay; Tamil WER also dropped, from 10.3% to 7.1% on Bloom Speech Tamil and 13.7% to 7.9% on children speech.

> "we achieved a lower WER from 40.5% to 28.4% on conversational speech and from 20.3% to 5.1% on children speech"

## Discussion


## Related Claims
- [Current multimodal LLMs underperform fine-tuned Whisper for spoken grammar correction: LoRA-tuned Qwen2-Audio reaches 13.7% WER (2.6% absolute worse than Whispergec) and zero-shot Voxtral scores F0.5 of 23.69 versus the 43.10 partial-cascaded baseline](multimodal-llms-underperform-whisper-sgec.md) — related
- [Educational multilingual TTS achieves MOS above 3.50 and recognition accuracy exceeding 90% for Malay and Tamil](singakids-multilingual-tts-evaluation.md) — related
- [Pseudo-labeled training data from over 2,500 hours of unlabeled learner speech improves small-model end-to-end SGEC, but offers limited benefit for large-v2 models once manual annotations are added](pseudo-labeled-data-sgec-model-size-moderates.md) — related
- [With the Whisper large-v2 backbone, the end-to-end SGEC model reduces WER by 6.9% relative on LNG and 5.6% on S&I versus the partial-cascaded system, surpassing both pipeline baselines](e2e-whisper-large-v2-sgec-outperforms-pipelines.md) — related
