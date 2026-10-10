---
type: theory
title: Three-model architecture of automatic speech recognition (acoustic, phonetic and language models)
description: "The article describes how ASR recognizes speech: a waveform is split into utterances by silences, and all possible word combinations are tested and matched against the audio."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
sources:
  - id: ali-2016
    resource: "https://doi.org/10.14705/rpnet.2016.eurocall2016.530"
    title: "Ali, S. (2016). Towards the development of a comprehensive pedagogical framework for pronunciation training based on adapted automatic speech recognition systems. In S. Papadima-Sophocleous, L. Bradley & S. Thouësny (Eds), CALL communities and culture – short papers from EUROCALL 2016 (pp. 7-13). Research-publishing.net. https://doi.org/10.14705/rpnet.2016.eurocall2016.530"
    author: Ali, S
---

# Three-model architecture of automatic speech recognition (acoustic, phonetic and language models)

> **Theory** · [All theories](index.md)
> **Evidence** · 8 claims (6 for, 2 mixed) · 3 studies (1 causal, 1 quant-synthesis, 1 design), `q2`–`q3` · 2 of 3 report an effect size · 4 claims rest on one study

## Description
The article describes how ASR recognizes speech: a waveform is split into utterances by silences, and all possible word combinations are tested and matched against the audio. Three models complete the matching: "the acoustic model (acoustic properties for each phoneme of the target language), the phonetic model or phonetic dictionary (with the mapping from word to phone) and a language model (defining which word can follow another and restrict possible combinations)." This architecture is the base the project intends to enrich with prosodic information at the acoustic-model level.

## Design Implications

### Context
#### Requirements
- An ASR system requires the three models — acoustic, phonetic/dictionary and language — to complete the speech matching process.
#### Constraints
- The description concerns the common approach to speech recognition as stated in the article; prosodic enrichment is proposed, not yet implemented.

### Target Learners
- adult learners of English (French university students)

### Target Learning Objectives
- English pronunciation accuracy
- phoneme production
- prosody

### Claims

- [CAPT software shows promising results for segmental pronunciation, while prosodic features and fluency still require further research and development](../claims/capt-strong-segmentals-weak-prosody.md) [+W]
- [The Fluspeak ASR-based pronunciation software gave good results with beginners focusing on phoneme production but poor results overall for advanced learners seeking fluency](../claims/fluspeak-good-beginners-poor-advanced.md) [+W]
- [Whether individual or peer practice works better with ASR-based pronunciation training is unsettled: one study found individual work best, a meta-analysis found peer practice gave larger effects](../claims/individual-work-best-asr-pronunciation-training.md) [+W]
- [ASR transcription serves as a diagnostic tool identifying individual learners' pronunciation errors, with function words most commonly mispronounced](../claims/asr-diagnostic-identification-pronunciation-errors.md) [+W]
- [Guided ASR practice improves overall pronunciation accuracy of Korean EFL learners more than ordinary classroom pronunciation practice alone](../claims/asr-guided-practice-improves-overall-pronunciation-accuracy.md) [+W]
- [Guided ASR practice did not produce statistically significant improvement in any specific pronunciation error type, with some errors unimproved or regressed](../claims/asr-specific-error-types-no-significant-gains.md) [~W]
- [Students responded positively to ASR pronunciation training and the Rainbow passage, but were mixed on technical aspects of recording and voice typing](../claims/positive-student-response-asr-pronunciation-training.md) [+W]
- [Amount of ASR practice (days per week, session length) showed no observable difference in pronunciation improvement](../claims/no-dose-response-asr-practice-time.md) [~W]

## Related Theories
- 

## Examples

- [Rainbow passage with ASR transcription and segmental error rate (SER) as a pronunciation diagnostic instrument](../products/rainbow-passage-with-asr-transcription-and-segmental-error-rate-ser.md)
- [ASR read-aloud compare-and-repeat self-study strategy for pronunciation practice](../strategies/asr-read-aloud-compare-repeat-strategy.md)
- [Use ASR confidence as a proxy for listening difficulty to drive segment-level playback speed](../strategies/asr-confidence-proxy-for-listening-difficulty.md)

## Key Sources
- Ali, S. (2016). Towards the development of a comprehensive pedagogical framework for pronunciation training based on adapted automatic speech recognition systems. In S. Papadima-Sophocleous, L. Bradley & S. Thouësny (Eds), CALL communities and culture – short papers from EUROCALL 2016 (pp. 7-13). Research-publishing.net. https://doi.org/10.14705/rpnet.2016.eurocall2016.530
