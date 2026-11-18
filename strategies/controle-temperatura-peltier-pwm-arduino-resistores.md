---
type: strategy
id: controle-temperatura-peltier-pwm-arduino-resistores
title: Controle da temperatura das pastilhas por PWM via Arduino ou por resistores de fio, com limitação de temperatura por segurança
description: "Dois circuitos alternativos controlam a temperatura de cada pastilha: \"O controle de temperatura da pastilha Peltier pode ser facilmente implementado utilizando Arduino..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: maurício-s-almeida-2019
    resource: "https://arxiv.org/abs/1904.10837"
    title: "Maurício S. Almeida, João N. M. Castro, Wilami T. Cruz, Rodrigo Q. Almeida. (2019). Construção de uma Maquete do Sistema Solar com Controle de Temperatura para Alunos com Deficiência Visual. Revista Brasileira de Ensino de Física. https://arxiv.org/abs/1904.10837"
    author: Maurício S. Almeida, João N. M. Castro, Wilami T. Cruz, Rodrigo Q. Almeida
---

# Controle da temperatura das pastilhas por PWM via Arduino ou por resistores de fio, com limitação de temperatura por segurança

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Dois circuitos alternativos controlam a temperatura de cada pastilha: "O controle de temperatura da pastilha Peltier pode ser facilmente implementado utilizando Arduino... através da técnica de PWM (Pulse Width Modulation)", com potenciômetro de 1 kΩ modulando a largura do pulso; ou resistores de fio de potência mínima de 5 W (valores de 40 a 120 Ω) controlando a corrente. Como se deseja apenas um efeito didático, "temperaturas elevadas poderiam causar desconforto ou até danos aos alunos", o que facilita o circuito.

## Design Implications

### Context
#### Requirements
- Sistema de dissipação de calor (cooler mais dissipador) nas pastilhas dos planetas frios; fonte de 12 V e 6 A
#### Constraints
- As pastilhas não precisam trabalhar em condições extremas; temperaturas elevadas poderiam causar desconforto ou danos aos alunos

### Target Learners
- Estudantes com deficiência visual que manuseiam a maquete

### Target Learning Goals
- Percepção térmica das temperaturas relativas dos planetas

## Related Strategies
- 

## Examples
-

## Key Sources
- Maurício S. Almeida, João N. M. Castro, Wilami T. Cruz, Rodrigo Q. Almeida. (2019). Construção de uma Maquete do Sistema Solar com Controle de Temperatura para Alunos com Deficiência Visual. Revista Brasileira de Ensino de Física. https://arxiv.org/abs/1904.10837
