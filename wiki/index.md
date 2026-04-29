---
title: Wiki Master Index
date: 2026-04-29
---

# Master Index

> Read this file before any search in the wiki.

## Concepts

### Mecánicas

- [[ph-puntos-habilidad]] — Sistema PH (66 totales, 32 max/stat, factor 7.875 = EV)
- [[formula-stats]] — Cálculo HP/Atk/Def/SpA/SpD/Spe a Nv.50
- [[formula-dano]] — Replica daño op.gg + roll 0.85→1.0 + gaps no modelados
- [[naturaleza]] — 25 naturalezas (5 neutrales + 20 ±10%)
- [[preset-rol]] — 4 spreads canónicos (Sweeper, Physical, Tank, SpD Tank)
- [[habilidades-modeladas]] — 21 abilities con efecto en daño + 6 sets de moves

### Items / objetos

- [[type-booster]] — 18 ítems ×1.2 al tipo (cobertura completa)
- [[panuelo-eleccion]] — Spe ×1.5 + lock movimiento
- [[baya-tipo]] — 18 bayas ×0.5 a 1 hit SE específico

### Análisis derivado

- [[speed-tier]] — Velocidad final por escenario (PH + naturaleza + Pañuelo)
- [[damage-matrix]] — Matriz de daño atacantes × defensores
- [[threat-list]] — Vista inversa: qué amenaza a cada defensor
- [[coverage-matrix]] — SE coverage por movepool de cada Pokémon
- [[defensive-core]] — Pares ranqueados por score defensivo conjunto
- [[spread-optimizer]] — PH HP/Def(SpD) mínimos vs amenazas top
- [[scarf-candidate]] — Ranking de Pokémon que merecen Pañuelo

### Meta

- [[meta-actual]] — Tier list y uso vigentes (volátil; sin snapshot ingestado todavía)
- [[counter-meta]] — Pipeline de generación de contra-estrategias

## Entities

### Tipos (18)

[[Normal]] · [[Fuego]] · [[Agua]] · [[Eléctrico]] · [[Planta]] · [[Hielo]] · [[Lucha]] · [[Veneno]] · [[Tierra]] · [[Volador]] · [[Psíquico]] · [[Bicho]] · [[Roca]] · [[Fantasma]] · [[Dragón]] · [[Siniestro]] · [[Acero]] · [[Hada]]

### Pokémon individuales

265 fichas en `wiki/entities/pokemon/`. Índice completo: [[entities/pokemon/_index|_index]]. Lookup directo por slug: [[charizard]], [[garchomp]], [[dragapult]], [[whimsicott]], [[arcanine]], [[greninja]], etc.

### Ataques

919 movimientos en `wiki/entities/ataques/`. Índice completo: [[entities/ataques/_index|_index]]. Lookup directo: [[a-bocajarro]], [[lanzallamas]], [[onda-igenia]], [[veloc-extrema]], [[refuerzo]], etc.

### Habilidades

309 habilidades en `wiki/entities/habilidades/`. Índice completo: [[entities/habilidades/_index|_index]]. Las 21 modeladas en daño ya cubiertas en [[habilidades-modeladas]]. Lookup directo: [[intimidacion]], [[multiescamas]], [[bromista]], [[adaptabilidad]], etc.

### Items

138 objetos en `wiki/entities/objetos/`. Índice completo: [[entities/objetos/_index|_index]]. Categorías clave ya como conceptos: [[type-booster]], [[baya-tipo]], [[panuelo-eleccion]]. Lookup directo: [[restos]], [[panuelo-elegido]] o [[choice-scarf]], [[carbon]], [[baya-zidra]], etc.

## Processed sources

### op.gg/es/pokemon-champions

- [[op-gg-pokedex]] — 258 Pokémon (stats, tipos, abilities, movepool)
- [[op-gg-moves]] — 919 ataques (power, accuracy, PP, type, category)
- [[op-gg-abilities]] — 307 habilidades (309 con extras)
- [[op-gg-items]] — 138 objetos (4 categorías)
- [[op-gg-types]] — Type effectiveness 18×18
- [[op-gg-calculator]] — Bundle JS con fórmulas, naturalezas, presets, abilities modeladas

### Meta y builds

- [[builds-curated]] — 12 builds VGC del launch meta
- [[pokemon-zone-meta]] — Usage ranked (sin snapshot ingestado todavía)

## Synthesis

- [[flujo-construccion-equipo]] — Secuencia repetible meta→core→atacante→item para armar equipo VGC
- [[items-vs-meta-clasico]] — Cómo Pokémon Champions cambia la teoría de items vs VGC mainline
- [[cobertura-vs-tipos-defensivos]] — Atacantes 18/18 coverage + tipos defensivos top (Acero, Agua, Fuego)
