---
type: strategy
id: medicao-frequencia-ldr-arduino
title: Medir a frequência de rotação do motor indiretamente com sensor LDR e Arduino, evitando o osciloscópio
description: "Estratégia de calibração de baixo custo: um sensor LDR posicionado atrás do motor e hélice, iluminado por uma fonte de luz, registra sombras a cada passagem da hélice; o Arduino adquire o sinal pela porta analógica us..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: hugo-luna-e-daniel-avila-2024
    resource: "https://www.revistas.unc.edu.ar/index.php/revistaEF"
    title: "Hugo Luna e Daniel Avila. (2024). Utilizando o captador de guitarra como sensor: Construindo um kit para abordar a Lei de Faraday em sala de aula. Revista de Ensino de Física. https://www.revistas.unc.edu.ar/index.php/revistaEF"
    author: Hugo Luna e Daniel Avila
---

# Medir a frequência de rotação do motor indiretamente com sensor LDR e Arduino, evitando o osciloscópio

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Estratégia de calibração de baixo custo: um sensor LDR posicionado atrás do motor e hélice, iluminado por uma fonte de luz, registra sombras a cada passagem da hélice; o Arduino adquire o sinal pela porta analógica usando a função millis. O artigo explica que "A cada vez que uma hélice se alinha ao LDR, uma sombra é projetada, fazendo com que a leitura da saída seja alterada". Com o período medido, calculam-se as frequências linear e angular concomitantemente à medida do Vrms no multímetro, evitando o osciloscópio, instrumento de alto custo pouco acessível às escolas brasileiras.

## Design Implications

### Context
#### Requirements
- Sensor LDR, fonte de luz, placa Arduino para aquisição e armazenamento do sinal
#### Constraints
- O osciloscópio é descrito como de alto custo e de operação que poderia representar nível de dificuldade adicional para os alunos

### Target Learners
- estudantes do ensino médio e superior em escolas sem laboratório equipado

### Target Learning Goals
- medir frequência de rotação e relacioná-la à taxa de variação do fluxo magnético

## Related Strategies
- 

## Examples
-

## Key Sources
- Hugo Luna e Daniel Avila. (2024). Utilizando o captador de guitarra como sensor: Construindo um kit para abordar a Lei de Faraday em sala de aula. Revista de Ensino de Física. https://www.revistas.unc.edu.ar/index.php/revistaEF
