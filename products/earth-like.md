---
type: product
id: earth-like
title: Earth-Like
description: Earth-Like is a web-based planetary climate model that simulates the carbon-silicate cycle and surface temperature for science learning by school students and the general public.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
---

# Earth-Like

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Earth-Like is a web-based planetary climate model that simulates the carbon-silicate cycle and surface temperature for science learning by school students and the general public.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Three-box carbon-silicate cycle climate model**: Earth-Like computes global surface temperature with a box model of the carbon-silicate cycle, circulating carbon between atmosphere, ocean and sediment reservoirs via weathering (Fw), sedimentation (Fsed) and degassing (Fvol) fluxes solved by mass-balance integration. Silicate weathering acts as a negative feedback that operates faster at higher temperatures, regulating atmospheric CO2 and defining the classical habitable zone boundaries. Weathering depends on land fraction γ, atmospheric CO2 and surface temperature, with β = 0.165 and k = 10 K; albedo is parameterised to rise from 0.3 to 0.6 as the planet freezes. The model is normalised to present-day Earth values. (Elizabeth J. Tasker et al. (2020))
- **GAN-based planet visualisation generator**: Earth-Like renders an animated globe from the chosen parameters and calculated temperature to increase engagement. A pixelated map is built with a friends-of-friends land scheme, terrain colours drawn from a Gaussian centred on the degassing factor, and an arctic zone sized by surface temperature. "The neural network is a conditional Generative Adver- sarial Network (GAN) constructed along the lines of the pix2pix model", with a U-Net Generator (one octave, five layers) and a five-octave VGG-like Discriminator using a Relativistic LSGAN loss, trained on 3250 downsampled satellite-image patches of 128 x 128 pixels in batches of 15. Only the Generator is used in the application. (Elizabeth J. Tasker et al. (2020))
- **Earth-Like website and @earthlikeworld Twitter bot**: Earth-Like is an interactive education and outreach tool at earthlike.world and on Twitter as @earthlikeworld. It "allows users to explore changes in the average global surface temperature of an Earth-like planet" by varying land fraction, degassing rate and habitable-zone position through a web interface or by tweeting parameters at the bot. The website returns the surface temperature, an interactive plot of the three carbon reservoirs' evolution, a downloadable .csv of the data (available for five minutes), and a GAN-rendered planet animation; an advanced toolkit adds stellar type and distance selection. (Elizabeth J. Tasker et al. (2020))

### Claims
- [A user survey suggests Earth-Like successfully communicates that minor changes in planetary properties can strongly impact the surface environment](../claims/earth-like-survey-communicates-planet-diversity.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Elizabeth J. Tasker, Kana Ishimaru, Nicholas Guttenberg and Julien Foriel. (2020). Earth-Like: An education & outreach tool for exploring the diversity of planets like our own. https://arxiv.org/abs/2001.01438
