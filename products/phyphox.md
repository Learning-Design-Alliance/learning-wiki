---
type: product
id: phyphox
title: phyphox
description: phyphox is a free cross-platform smartphone-sensor application developed by Staacks et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
---

# phyphox

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
phyphox is a free cross-platform smartphone-sensor application developed by Staacks et al. for conducting, remotely controlling, observing, and analyzing physics experiments.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **phyphox network interface for automated submission and exchange of experiment data**: A generic network interface for phyphox, defined in the same XML format, allowing easy exchange of experiment data by students. It can send sensor data, user input, or analysis results, and receive and display network data; metadata such as device model, phyphox version, or a uniquely generated user id can be submitted. HTTP and MQTT protocols are implemented, with privacy notices shown to users before submission. (S Staacks et al. (2022))
- **Phyphox app for smartphone-based physics experiments**: Phyphox is one of the general-purpose sensor apps tabulated in Table 2 and is among those the letter highlights "for their multiplatform character, abilities to download files to the cloud, set up the sampling frequencies, documentation, and support availability." A cited paper states that "Phyphox was specifically designed to improve the usefulness of smartphones in a wide range of physics experiments," describing features including remote access, data analysis, and web-based programmable customization. (Martín Monteiro et al. (2021))
- **Smartphone magnetometer sensors with the Phyphox app used as scientific measurement instruments**: The central instructional element of both experiments is the magnetic field sensor built into ordinary smartphones and tablets, accessed through the Phyphox app's Raw Sensor Magnetometer mode (written by RWTH Aachen University) plus a simple compass app for orientation. Students record raw three-axis field data, use the app's Pick data tool to extract single points and differences between two points, and export screenshots of plots and analyses into their reports. The article's stated motivation is to help students realize their phones "can be used as sensors for scientific measurements" and to make experiments relevant to everyday life. (Glen D. Gillen et al. (2021))
- **Generic Bluetooth Low Energy interface in phyphox for external sensors as input or output**: phyphox's experiment configurations are XML files defining data sources, analysis steps and visualization elements; the BLE support extends this format so a Bluetooth device can act as an input like a regular sensor or as an output. The interface identifies devices by advertised name or service UUID, reads characteristics with conversion functions, and can configure peripherals after connecting. The authors report that incorporating BLE devices this way allowed combining data from external and internal sensors, as demonstrated by Dorsel et al. (2022). (Staacks et al. (2023))
- **phyphox Arduino library encapsulating BLE and XML configuration into three lines of code**: An open Arduino library, distributed through the Arduino IDE Library Manager, encapsulates all technical prerequisites of the generic BLE interface: it generates the XML configuration, sets up the GATT server, services and characteristics, advertises the phyphox-specific service UUID, and handles binary encoding. A minimal example generates random numbers and plots them in phyphox with only three additional commands beyond the default Arduino structure. The library also exposes most of the phyphox XML format through objects for graphs, displays, buttons and text boxes so users can build custom labeled interfaces. (Staacks et al. (2023))
- **phyphox MicroPython library for students learning programming in Python**: Because Python is increasingly used in introductory programming courses for science students while the Arduino language can confuse novices, the authors ported the library to MicroPython. The minimal example is logically identical to the Arduino random-numbers example, with minor differences: modules must be imported explicitly and the PhyphoxBLE class must be instantiated rather than using static function calls. This gives students who start learning a programming language a version in a syntactically easier language while retaining the same few-lines-of-code integration with phyphox. (Staacks et al. (2023))
- **Released phyphox Arduino and MicroPython library source code under LGPL v3.0**: Both libraries are released as open-source artifacts: the Arduino library is distributed through the Arduino IDE Library Manager and the MicroPython module through its repository. The article states the Arduino library state at submission "has been archived under the DOI https://doi.org/10.5281/zenodo.10849073" and the MicroPython module under https://doi.org/10.5281/zenodo.10849061, both under the GNU Lesser General Public Licence v3.0, with latest versions on the phyphox GitHub pages. Documentation and examples are available on the respective web pages. (Staacks et al. (2023))

### Claims

- [In-app automated data analysis shifts an experiment's instructional focus, e.g. from teaching data analysis to teaching basic kinematics](../claims/in-app-analysis-shifts-experiment-focus.md) [+W]
- [Requiring computer-based data analysis after smartphone experiments poses extraneous cognitive load that may hinder physics learning](../claims/smartphone-experiment-data-analysis-extraneous-load.md) [+W]

## Related Products and Programmes

- [iMecaProf](imecaprof.md)
- [SmartPhysics: Rotation Lab](smartphysics-rotation-lab.md)

## Key Sources
- Staacks, S., Hütz, S., Heinke, H., & Stampfer, C. (2018). Advanced tools for smartphone-based experiments: phyphox. arXiv. https://arxiv.org/abs/1804.06239. [doi:10.1088/1361-6552/aac05e](https://doi.org/10.1088/1361-6552/aac05e)
- S Staacks, D Dorsel, S Hütz, F Stallmach, T Splith, H Heinke, C Stampfer. (2022). Collaborative smartphone experiments for large audiences with phyphox. https://doi.org/10.1088/1361-6404/ac7830
- Martín Monteiro and Arturo C. Martí. (2021). Resource Letter MDS-1: Mobile Devices and Sensors for Physics Teaching. https://aapt.scitation.org/journal/ajp
- Glen D. Gillen and Katharina Gillen. (2021). Magnetic Field Experiments Using a Phone. Physics Department, California Polytechnic State University, San Luis Obispo. https://www.ngdc.noaa.gov/geomag/magfield.shtml
- Staacks, S., Dorsel, D., Krampe, A., Hagedorn, M., Leier, E., Heinke, H., & Stampfer, C. (2023). Bluetooth sensors in phyphox with Arduino and MicroPython – Paving the way from an idea to an experiment for teachers and learners. https://github.com/phyphox/phyphox-arduino
