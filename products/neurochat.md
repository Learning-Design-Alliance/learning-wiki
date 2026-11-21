---
type: product
id: neurochat
title: NeuroChat
description: NeuroChat is a research-developed neuroadaptive AI chatbot that uses wearable EEG engagement estimates to steer GPT-4-turbo tutoring responses for adult self-directed learners.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# NeuroChat

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
NeuroChat is a research-developed neuroadaptive AI chatbot that uses wearable EEG engagement estimates to steer GPT-4-turbo tutoring responses for adult self-directed learners.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Closed-loop neuroadaptive LLM tutoring: real-time EEG engagement scores embedded in prompts to steer LLM response adaptation**: NeuroChat operationalizes a closed-loop adaptation mechanism in which a wearable EEG headband's engagement index, E = β/(α+θ), is computed each second over a 15-second sliding window, normalized against per-participant calibration bounds, and inserted into each query to GPT-4-turbo. A system prompt provides "heuristics for tailoring responses based on the user's real-time engagement score", reframing engagement as a proxy for cognitive load and directing the model to modulate depth, specificity, response format, and conversational style. The article positions this as the first integration of EEG-based cognitive state tracking with generative AI chatbot interaction in real time, overcoming pre-scripted-content limits of prior neuroadaptive systems. (NeuroChat: A Neuroadaptive AI Chatbot for Customizing Learning Experiences)
- **NeuroChat web app: browser-based neuroadaptive LLM tutor with Muse 2 EEG headband**: NeuroChat is a fully browser-based web app that connects to a 4-channel Muse 2 EEG headband (256 Hz sampling, electrodes at Fpz, AF7, AF8, TP9, TP10) via Web Bluetooth and the open-source MuseJS library. It preprocesses EEG with a 1–30 Hz bandpass filter and 60 Hz notch filter, computes power spectral density via FFT, and derives the engagement index from beta, alpha, and theta band powers. Its UI includes a Brain Connect Widget, calibration modal, ChatGPT-like chat interface, and a settings sidebar with Mood Mode and Debug Mode toggles, storing chats and EEG data in the browser's IndexedDB. (NeuroChat: A Neuroadaptive AI Chatbot for Customizing Learning Experiences)

### Claims
- [NeuroChat elicited significantly higher EEG-measured engagement than a non-adaptive control chatbot when controlling for task order](../claims/neurochat-higher-eeg-engagement-than-control.md) [+M]
- [NeuroChat produced no significant difference in short-term learning outcomes (quiz and essay scores) compared to the control chatbot](../claims/neurochat-no-learning-outcome-difference.md) [~M]

## Related Products and Programmes
-

## Key Sources
- Dünya Baradari, Nataliya Kosmyna, Oscar Petrov, Rebecah Kaplun, and Pattie Maes. 2025. NeuroChat: A Neuroadaptive AI Chatbot for Customizing Learning Experiences. In Proceedings of the 7th ACM Conference on Conversational User Interfaces (CUI '25). https://doi.org/10.1145/3719160.3736623
