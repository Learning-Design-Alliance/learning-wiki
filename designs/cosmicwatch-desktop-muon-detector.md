---
type: design
id: cosmicwatch-desktop-muon-detector
title: CosmicWatch desktop muon detector used by school research teams
description: "CosmicWatch (CW) is a \"small and inexpensive desktop cosmic ray muon detector\" that many Tan-Q research groups use."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: takeshi-nakamori-2021
    resource: "https://arxiv.org/abs/2108.02163"
    title: "Takeshi Nakamori, Mika Takanashi, Rikako Kono, Ryuta Saito, Kyoka Ozaki, Haruki Nakadai, Kazuo S. Tanaka, Ana Beatriz Prieto, Marianela Pepe, Juan Wehinger, Lucio Martinez, Chizuru Nose, Haruhi Enomoto, Ryosuke Kita, Kyoka Maruta. (2021). Collaboration between high schools in Japan and Argentina for cosmic-ray research using CosmicWatches. 37th International Cosmic Ray Conference (ICRC 2021). https://arxiv.org/abs/2108.02163"
    author: Takeshi Nakamori, Mika Takanashi, Rikako Kono, Ryuta Saito, Kyoka Ozaki, Haruki Nakadai, Kazuo S. Tanaka, Ana Beatriz Prieto, Marianela Pepe, Juan Wehinger, Lucio Martinez, Chizuru Nose, Haruhi Enomoto, Ryosuke Kita, Kyoka Maruta
---

# CosmicWatch desktop muon detector used by school research teams

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
CosmicWatch (CW) is a "small and inexpensive desktop cosmic ray muon detector" that many Tan-Q research groups use. It "consists of a plastic scintillator of 5  5  1cm3 and a silicon photomultiplier," with an Arduino Nano handling data acquisition triggered when pulse height exceeds a threshold; pulse height, time stamp, and environmental data such as temperature are recorded per event. PCB pattern and Arduino image files are open source. Tan-Q distributes detectors assembled by mentors to interested schools, and some schools modify the scintillator and acquisition programs for their own topics.

## Design Implications

### Context
#### Requirements
- Assembly by mentors or provision of assembled units
- connection to a Windows PC via USB to read data
- data-cleaning cuts (ADC pulse-height cut, removal of acquisition-failure periods) for accurate rate measurements
#### Constraints
- The article notes that with only one CW per location, muons striking near the scintillator edges are "difficult to distinguish from thermal noise triggers," and that connecting two units in coincidence mode is stated to significantly improve the muon signal-to-noise ratio at the hardware level

### Target Learners
- junior and senior high school students

### Learning Goals
- measuring cosmic-ray muon flux
- hands-on particle-physics experimentation and data analysis

### Claims
- Cosmicwatch Temperature Stable Adc Cut [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Takeshi Nakamori, Mika Takanashi, Rikako Kono, Ryuta Saito, Kyoka Ozaki, Haruki Nakadai, Kazuo S. Tanaka, Ana Beatriz Prieto, Marianela Pepe, Juan Wehinger, Lucio Martinez, Chizuru Nose, Haruhi Enomoto, Ryosuke Kita, Kyoka Maruta. (2021). Collaboration between high schools in Japan and Argentina for cosmic-ray research using CosmicWatches. 37th International Cosmic Ray Conference (ICRC 2021). https://arxiv.org/abs/2108.02163
