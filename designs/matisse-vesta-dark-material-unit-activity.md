---
type: design
id: matisse-vesta-dark-material-unit-activity
title: MATISSE webtool and Vesta dark-material-unit analysis activity
description: "MATISSE (Multi-purpose Advanced Tool for the Instruments for the Solar System Exploration) is \"the webtool developed at SSDC to find, visualize and analyse data from planetary exploration missions directly inside a we..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: zinzi-a-2020
    resource: "https://tools.ssdc.asi.it/matisse.jsp"
    title: "Zinzi A., Pittori C., Tagliamonte R., Nichelli E. (2020). ASI Space Science Data Center participation to high-school outreach program. https://tools.ssdc.asi.it/matisse.jsp"
    author: Zinzi A., Pittori C., Tagliamonte R., Nichelli E
---

# MATISSE webtool and Vesta dark-material-unit analysis activity

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
MATISSE (Multi-purpose Advanced Tool for the Instruments for the Solar System Exploration) is "the webtool developed at SSDC to find, visualize and analyse data from planetary exploration missions directly inside a web browser", with 3D projection onto the target's shape. Students used it to retrieve Dawn-VIR observations of Vesta, extracting reflectance at 1.2 microns, radiance at 5 microns, band depth II, and band centers I and II, then analysed FITS files with the JS9 reader to identify dark material units and infer HED classification and darkening-agent abundance following Palomba et al. (2014).

## Design Implications

### Context
#### Requirements
- Access to the public "VIR IR" and "VIR Spectral Parameters" datasets via MATISSE; a curated list of VIR observations was provided because a full geographical query "would have been an unfeasible work for a light-trained student in only a morning activity"
#### Constraints
- Students worked from a pre-selected subset of the 123 dark material units found by Palomba et al. (2014), not the full catalogue

### Target Learners
- upper secondary (high-school) students in the Alternanza Scuola-Lavoro program

### Learning Goals
- infrared spectroscopy and planetary surface mineralogy
- quantitative analysis of real spacecraft data

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Zinzi A., Pittori C., Tagliamonte R., Nichelli E. (2020). ASI Space Science Data Center participation to high-school outreach program. https://tools.ssdc.asi.it/matisse.jsp
