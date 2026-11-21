---
type: design
id: minimal-i2c-sensor-set-weather-station
title: Minimal four-quantity sensor set (light, pressure, humidity/temperature) on an I²C bus with LCD display for long-term school measurement
description: "A reusable hardware design pattern for school measurement devices: a small set of I²C sensors and a four-line LCD connected to a low-cost microcontroller, mounted in a box with a transparent cover for outdoor placement."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: m-hruška-and-m-plesch-2025
    resource: "https://doi.org/10.1088/1742-6596/3155/1/012015"
    title: "M Hruška and M Plesch. (2025). The use of a simple digital weather station (not only) in teaching physics. Journal of Physics: Conference Series 3155 (2025) 012015. https://doi.org/10.1088/1742-6596/3155/1/012015"
    author: M Hruška and M Plesch
---

# Minimal four-quantity sensor set (light, pressure, humidity/temperature) on an I²C bus with LCD display for long-term school measurement

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A reusable hardware design pattern for school measurement devices: a small set of I²C sensors and a four-line LCD connected to a low-cost microcontroller, mounted in a box with a transparent cover for outdoor placement. The authors found that "the combination of a four-line LCD and three sensors yielded the best results": the BH1750 measures light intensity in lux, the BMP180 or BMP280 measures barometric pressure, and the HTU21D records relative humidity and air temperature. Data is logged about once per minute and recorded to a text file via USB.

## Design Implications

### Context
#### Requirements
- All sensors and the LCD share the I²C serial interface and a 3.3 V DC supply; each device is identified by its unique I²C address
- Sensors can be mounted on a printed circuit board with 0.1" (2.54 mm) contact-hole spacing in a mounting box with a transparent cover
#### Constraints
- Deliberately limited to temperature, pressure, humidity, and light intensity to keep the station technically simple and inexpensive

### Target Learners
- secondary school students learning sensor principles, I²C communication, and microcontroller programming

### Learning Goals
- understanding sensor and display operation
- I²C communication
- microcontroller programming
- long-term measurement of physical quantities

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- M Hruška and M Plesch. (2025). The use of a simple digital weather station (not only) in teaching physics. Journal of Physics: Conference Series 3155 (2025) 012015. https://doi.org/10.1088/1742-6596/3155/1/012015
