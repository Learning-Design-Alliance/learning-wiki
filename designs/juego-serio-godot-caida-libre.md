---
type: design
id: juego-serio-godot-caida-libre
title: "Juego serio en Godot para la caída libre: seis escenas, cuatro niveles con retos de tiempo-distancia y cuestionarios de opción múltiple"
description: "Juego serio desarrollado por los estudiantes en el entorno Godot, definido en el artículo como un videojuego que \"integra intenciones pedagógicas, informativas e interactivas orientadas a educar\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: pacheco-gonzález-2024
    resource: "https://godotengine.org"
    title: "Pacheco-González, Alberto. (2024). Juego serio para Física como estrategia de aprendizaje activa y lúdica. TecNM campus Chihuahua. https://godotengine.org"
    author: Pacheco-González, Alberto
---

# Juego serio en Godot para la caída libre: seis escenas, cuatro niveles con retos de tiempo-distancia y cuestionarios de opción múltiple

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Juego serio desarrollado por los estudiantes en el entorno Godot, definido en el artículo como un videojuego que "integra intenciones pedagógicas, informativas e interactivas orientadas a educar". Consta de "seis escenas principales": pantalla inicial, cuatro niveles de juego y pantalla final con puntuación. Los niveles 1 y 3 presentan retos de tiempo y distancia con un objeto rígido en caída libre, un peldaño móvil y un barril; los niveles 2 y 4 son cuestionarios con preguntas al azar sobre cinemática y caída libre. Cada nivel incluye imagen de fondo, regleta, personaje, peldaño móvil, flecha, barril y piso.

## Design Implications

### Context
#### Requirements
- Un motor de juego con motor de física (controlador de fuerzas, objetos y colisiones), como el entorno Godot, y sesiones semanales de programación en vivo supervisada según el plan de la Tabla 1
#### Constraints
- Se observó que con muchas aplicaciones abiertas existía un pequeño desfase en la mayor distancia de hasta d=8.9u para t=3s, por lo que se recomendó cerrar aplicaciones al calibrar

### Target Learners
- estudiantes universitarios de un curso introductorio de Física sin experiencia previa de programación
- estudiantes de Física de nivel medio superior (uso futuro pretendido)

### Learning Goals
- matematizar los principios de la caída libre de objetos partiendo del reposo
- deducir inductivamente la relación tiempo-distancia y la constante de la aceleración gravitacional

### Claims
- Calibracion Godot Replica Mediciones Galileo [+M]
- [Diez Estudiantes Terminan Juego Serio Fisica](../claims/diez-estudiantes-terminan-juego-serio-fisica.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Pacheco-González, Alberto. (2024). Juego serio para Física como estrategia de aprendizaje activa y lúdica. TecNM campus Chihuahua. https://godotengine.org
