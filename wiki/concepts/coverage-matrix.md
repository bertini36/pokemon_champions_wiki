---
title: Coverage Matrix
date: 2026-04-29
type: concept
tags: [analisis, coverage, movepool, se]
---

# Coverage Matrix

## Definition

Para cada Pokémon disponible: qué tipos defensivos puede pegar SE con su movepool y dónde tiene gaps. Generado por `scripts/build_coverage_matrix.py` desde `raw/pokemon/`, `raw/ataques/`, `raw/tipos/`.

## Why it matters

Mide la **completitud ofensiva** de un Pokémon individual. Un atacante con coverage 18/18 pega SE a cualquier defensor; uno con 12/18 deja huecos que el equipo debe cubrir con compañeros.

Top coverage en el pool disponible:

| # | Pokémon | Tipos | Tipos SE | Sin efecto |
|---|---|---|---|---|
| 1 | Greninja | Agua/Siniestro | 18 | 0 |
| 2 | Garchomp | Dragón/Tierra | 18 | 0 |

## Output por Pokémon

- Tipos cubiertos SE
- Gaps (tipos donde no pega SE)
- Mejor move por tipo atacante (cuál usar para cada matchup)

## Connections

Cruza [[op-gg-pokedex]] (movepool), [[op-gg-moves]] (type + power), [[op-gg-types]] (eficacia). Complementa [[damage-matrix]] (que solo mira mejor STAB) considerando todo el movepool.

## Sources

- `raw/calculos/coverage-matrix.md` (402 líneas)

## 🔗 Related

- [[damage-matrix]]
- [[op-gg-moves]]
- [[op-gg-types]]
- [[scarf-candidate]]
