---
title: op.gg Type Effectiveness
date: 2026-04-29
type: source
tags: [op-gg, types, tipos, type-chart, effectiveness]
original-source: https://op.gg/es/pokemon-champions/type-effectiveness
---

# op.gg Type Effectiveness

## Summary

Tabla de eficacia entre los 18 tipos. La página tiene matriz 18×18 + panel "Detalles del Tipo" con dos secciones: "Atacando con [TIPO]" y "Defendiendo como [TIPO]", cada una con tres niveles: 2x, 0.5x, 0x. La ingesta clica cada pastilla y harvestea los paneles vía `parsePanel`.

La matriz 18×18 derivada de las 18 entradas atk → def es idempotente: no se duplica.

## Key concepts

- [[formula-dano]]: `typeEffect` viene del type chart (0, 0.25, 0.5, 1, 2, 4)
- [[damage-matrix]]: cada celda usa eficacia de tipos para calcular el final
- [[coverage-matrix]]: ranking de cobertura SE por movepool
- [[defensive-core]]: cores se evalúan combinando resistencias e inmunidades de los dos miembros
- [[threat-list]]: vulnerabilidad inversa
- 18 entidades [[Normal]], [[Fuego]], [[Agua]], [[Eléctrico]], [[Planta]], [[Hielo]], [[Lucha]], [[Veneno]], [[Tierra]], [[Volador]], [[Psíquico]], [[Bicho]], [[Roca]], [[Fantasma]], [[Dragón]], [[Siniestro]], [[Acero]], [[Hada]]

## Mentioned entities

- 18 tipos canónicos en `raw/tipos/` y `wiki/entities/`

## Highlighted ideas

> Los multiplicadores 0x solo aparecen en inmunidades (Fantasma vs Normal en atk, Tierra vs Eléctrico en def).

> Acero defiende ×0.5 contra 10 tipos: el tipo defensivo más eficiente del juego en cobertura pura.

## 🔗 Related

- [[op-gg-pokedex]]
- [[op-gg-moves]]
- [[formula-dano]]
- [[damage-matrix]]
- [[coverage-matrix]]
- [[defensive-core]]
