---
type: product
id: edukoi
title: Edukoi
description: Edukoi is an interactive educational sonification tool developed by Guiotto Nai Fovino et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# Edukoi

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 2 studies (2 design), `q1`–`q3` · 1 of 2 report an effect size · 4 claims rest on one study

## Description
Edukoi is an interactive educational sonification tool developed by Guiotto Nai Fovino et al. that maps image colours and saturation to spatialised natural sounds for exploring astronomical images with sighted and blind or visually impaired learners.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Interactive image sonification for inclusive science learning: a motion-aware tool pattern for exploring visual data through sound**: The pattern is a motion-sensing sonification tool in which a camera-tracked hand position is re-projected onto image pixels and the visual properties of touched pixels are converted into sound properties in real time. The authors apply it to astronomical images so that sighted and BVI students can explore data through sound, challenging the perception of astronomy as a purely visual science. They note such tools serve dissemination to broader audiences and image exploration by BVI people beyond audio description. (Guiotto Nai Fovino et al. (2023))
- **Edukoi motion-sensing sonification tool**: Edukoi is an adaptation of the open-source software Herakoi; both are motion-sensing sonification tools that "convert images into sound in real-time" using the MediaPipe Hand Landmarker model to track 21 hand-knuckle coordinates via webcam. Users explore images with hand movements; the touched pixel region's visual properties are converted into sound properties of a chosen MIDI instrument. Edukoi maps RGB colours to natural sounds (fire for red, water bubbles for blue, birds and rustling leaves for green) with stereo panning, designed to be memorable with minimal training for educational use, including by visually impaired learners. (Lucrezia Guiotto Nai Fovino et al. (2024))

### Claims
- [During a first middle-school test of Edukoi, classes maintained high attention and reported enjoyment, but found counting stars by sound very difficult.](../claims/edukoi-classroom-test-qualitative-feedback.md) [+M]
- [A BVI student found it very difficult to locate sonified areas because no spatial reference showed where the camera and screen were.](../claims/edukoi-bvi-student-spatial-reference-difficulty.md) [-W] — (also cited [~W])
- [Middle-school students recognise colours through Edukoi sonification at near-ceiling accuracy with minimal training](../claims/edukoi-colour-recognition-effective.md) [+M]
- [Shape recognition through Edukoi sonification is above chance but less robust than colour recognition](../claims/edukoi-shape-recognition-above-chance.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Guiotto Nai Fovino, L., Ginolfi, M., Grassi, M., Di Mascolo, L., & Zanella, A. (2023). Edukoi: Developing an interactive sonification tool for astronomy between entertainment and education. The 28th International Conference on Auditory Display (ICAD 2023). https://github.com/lucadimascolo/edukoi
- Lucrezia Guiotto Nai Fovino, Anita Zanella, Luca Di Mascolo, Michele Ginolfi, Nicolò Carpita, Francesco Trovato Manuncola, Massimo Grassi. (2024). Evaluating the effectiveness of sonification in science education using Edukoi. Personal and Ubiquitous Computing. https://doi.org/10.1007/s00779-024-01809-5
