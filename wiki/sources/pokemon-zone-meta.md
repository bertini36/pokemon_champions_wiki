---
title: pokemon-zone.com/champions/pokemon (uso del meta)
date: 2026-04-29
type: source
tags: [meta, usage, pokemon-zone, tier-list]
original-source: https://www.pokemon-zone.com/champions/pokemon/
---

# pokemon-zone.com/champions/pokemon

## Summary

Ranking de Pokémon más usados en partidas rankeadas de Pokémon Champions. Aporta tasa de uso (%) por Pokémon y posición global en el ranking. Sirve para identificar el meta actual, construir contra-estrategias y validar picks propios contra respaldo estadístico.

Frecuencia de re-ingestión: parche de balance, +2 semanas desde último snapshot, o detección de desfase entre meta documentado y partidas reales. Snapshots viven en `raw/meta/usage-YYYY-MM-DD.md`. Aún no se ha ingestado el primer snapshot.

## Key concepts

- [[meta-actual]]: tier list y uso vigente, derivado de cada snapshot
- [[counter-meta]]: cruce entre top usage + damage matrix + threat list para sugerir counters
- [[damage-matrix]]: amenazas top del meta entran como atacantes prioritarios
- [[threat-list]]: ranking de vulnerabilidad inverso, filtrado por top usage

## Mentioned entities

- Pendiente: `raw/meta/usage-YYYY-MM-DD.md` (no creado todavía)

## Highlighted ideas

> El meta de Pokémon Champions cambia con cada parche. Mantener `wiki/concepts/meta-actual.md` como capa volátil que se invalida con cada snapshot.

> El cruce con `damage-matrix` y `threat-list` debería materializarse en `wiki/synthesis/counter-meta-YYYY-MM-DD.md` cada vez que se pida análisis de counters.

## 🔗 Related

- [[meta-actual]]
- [[counter-meta]]
- [[damage-matrix]]
- [[threat-list]]
- [[defensive-core]]
