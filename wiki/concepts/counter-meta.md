---
title: Counter-meta
date: 2026-04-29
type: concept
tags: [meta, counter, sintesis, vgc]
---

# Counter-meta

## Definition

Página guía para producir contra-estrategias específicas contra el [[meta-actual]]. Cada análisis concreto se materializa como `wiki/synthesis/counter-meta-YYYY-MM-DD.md` con:

- Top amenazas vigentes (desde snapshot de uso)
- Counters recomendados (desde [[damage-matrix]] inversa + [[threat-list]])
- Cores defensivos sugeridos contra el top (desde [[defensive-core]])

## Why it matters

Un equipo VGC competitivo no se diseña en abstracto, se diseña **contra el meta de la próxima semana**. El counter-meta es el puente entre:
- Qué Pokémon vas a encontrarte (estadística)
- Qué Pokémon, items, naturalezas y spreads les ganan (cálculo)

## Pipeline de generación

1. Leer snapshot vigente: `raw/meta/usage-YYYY-MM-DD.md`
2. Top N Pokémon (mínimo 10) → set de amenazas
3. Cruzar contra [[damage-matrix]]: ¿qué atacantes les hacen OHKO/2HKO?
4. Cruzar contra [[threat-list]] de cada amenaza: ¿qué les vence sin morir antes?
5. Cruzar contra [[defensive-core]]: ¿qué pares aguantan al top?
6. Materializar en `wiki/synthesis/counter-meta-YYYY-MM-DD.md`
7. Append `INGEST` a `log.md`

## Connections

Sintetiza [[meta-actual]], [[damage-matrix]], [[threat-list]] y [[defensive-core]] en una recomendación accionable.

## Sources

- [[pokemon-zone-meta]]
- [[damage-matrix]]
- [[threat-list]]
- [[defensive-core]]

## 🔗 Related

- [[meta-actual]]
- [[pokemon-zone-meta]]
- [[damage-matrix]]
- [[threat-list]]
- [[defensive-core]]
- [[scarf-candidate]]
- [[spread-optimizer]]
