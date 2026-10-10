---
type: product
id: lavac
title: LAVAC
description: LAVAC (Laboratoire Audio-Visuel Actif-Comparatif) is a networked multimedia language-laboratory system developed for language instruction, providing linked student terminals, courseware-authoring tools, multimedia courseware, and teacher tutoring controls.
product_kind: software
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: toma-2000
    resource: "https://eric.ed.gov/?id=ED444508"
    title: "Toma, Tony. (2000). Real-Time Courseware Design: The LAVAC Video Sequencer. https://eric.ed.gov/?id=ED444508"
    author: Toma, Tony
---

# LAVAC

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
LAVAC (Laboratoire Audio-Visuel Actif-Comparatif) is a networked multimedia language-laboratory system developed for language instruction, providing linked student terminals, courseware-authoring tools, multimedia courseware, and teacher tutoring controls.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **LAVAC computerized language laboratory toolkit**: LAVAC (Laboratoire Audio-Visuel Actif-Comparatif) is a networked multimedia language laboratory consisting of "a complete network of student terminals, plus a courseware-design workstation, all linked to a server". A LAVAC courseware is a set of numbered segments linked to sound, images, videos, texts and tutor zones, up to six media, designed mainly for oral comprehension and production with 24 listening modes. It was the first to use a teacher's console for presential or distance tutoring, and around 5 000 software programs are used in more than 150 university departments and high schools in France and abroad. (Toma (2000))
- **Virtual Recorder and Video Sequencer automatic segmenting devices**: Derived from LAVAC, the Virtual Recorder (1998) is an audio sequencer with a new student interface that spares teachers linking text or images to sound segments; the Video Sequencer (March 1999) extends this to video. "The video sequencer can complete real-time automatic segmenting of sound and images and automatically insert an answering time span after each sequence." Segmenting detects blanks or volume drops in the sound signal, with tunable thresholds (language-sound level 5-15 on a 1-127 scale, blank duration 0.2 to 8 seconds, answering span 10 to 999% of segment length). Coupled to IBM ViaVoice, the teacher's spoken transcript is written with 90% accuracy for deriving textual help. (Toma (2000))

### Claims
- [Visible sound-wave displays led students to speak louder and notice sounds they would otherwise have missed](../claims/sound-wave-display-prompts-louder-speech-and-sound-noticing.md) [+W]
- [Students are more attentive to the teacher's model track when they hear their own recording first](../claims/student-recording-first-increases-attention-to-model.md) [+W]
- [Students pause the video after a few sequences to consult a segment menu and judge workload by segment count](../claims/students-pause-video-to-view-segment-menu.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Toma, Tony. (2000). Real-Time Courseware Design: The LAVAC Video Sequencer. https://eric.ed.gov/?id=ED444508

<!-- merged 2026-10-10 from elements/lavac-language-laboratory-toolkit ("LAVAC computerized language laboratory toolkit"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# LAVAC computerized language laboratory toolkit

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
LAVAC (Laboratoire Audio-Visuel Actif-Comparatif) is a networked multimedia language laboratory consisting of "a complete network of student terminals, plus a courseware-design workstation, all linked to a server". A LAVAC courseware is a set of numbered segments linked to sound, images, videos, texts and tutor zones, up to six media, designed mainly for oral comprehension and production with 24 listening modes. It was the first to use a teacher's console for presential or distance tutoring, and around 5 000 software programs are used in more than 150 university departments and high schools in France and abroad.

## Design Implications

### Context
#### Requirements
- A server-linked network of student terminals and a courseware-design workstation; no programming is required for at least 99% of the functions.
#### Constraints
- The tool may have been designed too early: when introduced, few students knew how to use a computer and expensive slow machines (PC 386) with low-capacity disks (540 Mb) constrained wave-file playback over a Novell network.

### Target Learners
- University and high-school language students

### Target Learning Goals
- Oral comprehension and production in foreign language learning

## Claims

- [Visible sound-wave displays led students to speak louder and notice sounds they would otherwise have missed](../claims/sound-wave-display-prompts-louder-speech-and-sound-noticing.md) [+W]
- [Students are more attentive to the teacher's model track when they hear their own recording first](../claims/student-recording-first-increases-attention-to-model.md) [+W]
- [Students pause the video after a few sequences to consult a segment menu and judge workload by segment count](../claims/students-pause-video-to-view-segment-menu.md) [+W]

## Related Elements

- [Virtual Recorder and Video Sequencer automatic segmenting devices](lavac.md)

## Examples
-

## Key Sources
- Toma, Tony. (2000). Real-Time Courseware Design: The LAVAC Video Sequencer. https://eric.ed.gov/?id=ED444508
-->

<!-- merged 2026-10-10 from elements/virtual-recorder-video-sequencer-devices ("Virtual Recorder and Video Sequencer automatic segmenting devices"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

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

- [LAVAC computerized language laboratory toolkit](../products/lavac.md)

## Examples

- [Sequence five exercise types around automatic segmenting, from note taking to translation](../strategies/five-exercise-sequence-around-segmenting.md)

## Key Sources
- Toma, Tony. (2000). Real-Time Courseware Design: The LAVAC Video Sequencer. https://eric.ed.gov/?id=ED444508
-->
