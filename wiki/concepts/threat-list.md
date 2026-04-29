---
title: Threat List por defensor
date: 2026-04-29
type: concept
tags: [analisis, threat, vulnerability, defense]
---

# Threat List por defensor

## Definition

Para cada Pokémon disponible, lista qué atacantes le hacen daño y cuántos le OHKOean / 2HKOean. Vista **inversa** de [[damage-matrix]]. Ordenado por número de OHKOs recibidos (los más vulnerables primero).

Generado por `scripts/build_threat_list.py` desde `raw/calculos/damage-matrix.json`.

## Why it matters

Identifica los Pokémon más vulnerables del pool disponible y los principales atacantes que les amenazan. Input directo de:

1. [[spread-optimizer]] — PH mínimos en HP+Def(SpD) para sobrevivir top 8 amenazas
2. [[defensive-core]] — qué Pokémon necesita pareja para cubrir su lista de amenazas
3. [[counter-meta]] — qué counters propone el meta actual contra los top atacantes

## Estructura del output

```
Defensor (Tipos, HP) → OHKOs recibidos / 2HKOs / total atacantes que dañan
  Top atacantes con OHKO: [...]
  Top atacantes con 2HKO: [...]
```

Whimsicott (Planta/Hada, 167 HP) lidera en vulnerabilidad: 3 OHKOs, 5 2HKOs, 14 atacantes le dañan.

## Connections

Input: [[damage-matrix]]. Outputs: [[spread-optimizer]], [[defensive-core]], [[counter-meta]].

## Sources

- `raw/calculos/threat-list.md` (343 líneas)

## 🔗 Related

- [[damage-matrix]]
- [[spread-optimizer]]
- [[defensive-core]]
- [[counter-meta]]
