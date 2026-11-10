---
type: design
id: off-shelf-doppler-apparatus-kit
title: "Off-the-shelf Doppler measurement apparatus: PC, directional microphone, digital voice recorder, and GNU Octave spectrum analysis"
description: "A low-cost laboratory kit for quantitative Doppler measurements: a sound source (a digital voice recorder playing a synthesized steady tone, fs = 3.520 kHz) is dropped or swung, and a microphone attached to a PC runni..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-10
sources:
  - id: kenichiro-aoki-2009
    resource: "https://arxiv.org/abs/0911.3819"
    title: "Kenichiro Aoki, Takahisa Mitsui and Yuki Yamamoto. (2009). Direct quantitative measurements of Doppler effects for sound sources with gravitational acceleration. https://arxiv.org/abs/0911.3819"
    author: Kenichiro Aoki, Takahisa Mitsui and Yuki Yamamoto
---

# Off-the-shelf Doppler measurement apparatus: PC, directional microphone, digital voice recorder, and GNU Octave spectrum analysis

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A low-cost laboratory kit for quantitative Doppler measurements: a sound source (a digital voice recorder playing a synthesized steady tone, fs = 3.520 kHz) is dropped or swung, and a microphone attached to a PC running spectrum analyzer software records the signal. The article states "The experiments can be easily set up from “oﬀ the shelf” componen ts only" and provides a GNU Octave script for extracting spectra. Simple buzzers were tested but none could emit a steady enough frequency in motion.

## Design Implications

### Context
#### Requirements
- A sound source emitting a distinct frequency steadily (a digital voice recorder; tested buzzers were not steady enough in motion)
- A microphone, preferably with high directivity, attached to a PC with spectrum analysis software
- Sampling rate R higher than twice the frequency of interest, with N chosen to balance Δf = 1/T against the peak-existence criterion
#### Constraints
- Source velocity is at most a few percent of c due to practical considerations including safety
- The setup uses an audible sound source for clarity of exposition and because generic components are not guaranteed outside the audible range

### Target Learners
- undergraduate students, including non-science majors

### Learning Goals
- quantitative measurement of the Doppler effect
- introduction to spectral methods and Fourier analysis

### Claims
- [Free Fall Doppler G Within 10 Percent](../claims/free-fall-doppler-g-within-10-percent.md) [+M]
- [Pendulum Doppler G One Percent](../claims/pendulum-doppler-g-one-percent.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Kenichiro Aoki, Takahisa Mitsui and Yuki Yamamoto. (2009). Direct quantitative measurements of Doppler effects for sound sources with gravitational acceleration. https://arxiv.org/abs/0911.3819
