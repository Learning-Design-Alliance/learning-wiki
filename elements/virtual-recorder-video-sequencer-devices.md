---
type: element
id: virtual-recorder-video-sequencer-devices
title: Virtual Recorder and Video Sequencer automatic segmenting devices
description: Derived from LAVAC, the Virtual Recorder (1998) is an audio sequencer with a new student interface that spares teachers linking text or images to sound segments; the Video Sequencer (March 1999) extends this to video.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-02
sources:
  - id: toma-2000
    resource: "https://eric.ed.gov/?id=ED444508"
    title: "Toma, Tony. (2000). Real-Time Courseware Design: The LAVAC Video Sequencer. https://eric.ed.gov/?id=ED444508"
    author: Toma, Tony
---

# Virtual Recorder and Video Sequencer automatic segmenting devices

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Derived from LAVAC, the Virtual Recorder (1998) is an audio sequencer with a new student interface that spares teachers linking text or images to sound segments; the Video Sequencer (March 1999) extends this to video. "The video sequencer can complete real-time automatic segmenting of sound and images and automatically insert an answering time span after each sequence." Segmenting detects blanks or volume drops in the sound signal, with tunable thresholds (language-sound level 5-15 on a 1-127 scale, blank duration 0.2 to 8 seconds, answering span 10 to 999% of segment length). Coupled to IBM ViaVoice, the teacher's spoken transcript is written with 90% accuracy for deriving textual help.

## Design Implications

### Context
#### Requirements
- A quiet recording room for ViaVoice transcription (silence must be total); a 100 Mbit Windows NT network; MJPEG compression (about 7 times) of the AVI file for network transfer.
#### Constraints
- Background music on some videos keeps sound volume constant, which had to be overcome because automatic segmenting relies on detecting blanks or volume drops; at a segmenting level of 30, words must be pronounced loud or they may be interpreted as noise.

### Target Learners
- Language students in university departments and high schools

### Target Learning Goals
- Aural comprehension, note taking, repetition and oral production

## Claims

- [Students pause the video after a few sequences to consult a segment menu and judge workload by segment count](../claims/students-pause-video-to-view-segment-menu.md) [+W]
- [Visible sound-wave displays led students to speak louder and notice sounds they would otherwise have missed](../claims/sound-wave-display-prompts-louder-speech-and-sound-noticing.md) [+W]
- [Students are more attentive to the teacher's model track when they hear their own recording first](../claims/student-recording-first-increases-attention-to-model.md) [+W]

## Related Elements

- [LAVAC computerized language laboratory toolkit](lavac-language-laboratory-toolkit.md)

## Examples

- [Sequence five exercise types around automatic segmenting, from note taking to translation](../strategies/five-exercise-sequence-around-segmenting.md)

## Key Sources
- Toma, Tony. (2000). Real-Time Courseware Design: The LAVAC Video Sequencer. https://eric.ed.gov/?id=ED444508
