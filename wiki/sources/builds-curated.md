---
title: Builds VGC curadas
date: 2026-04-29
type: source
tags: [builds, vgc, curated, manual]
original-source: raw/builds/
---

# Builds VGC curadas

## Summary

12 builds VGC del launch meta de Pokémon Champions, mantenidas manualmente (no extraídas automáticamente de op.gg). Cada build tiene Datos (Pokémon, Formato, Objeto, Naturaleza, EVs, IVs), Movimientos (4), Compañeros recomendados (texto libre), y Estrategia (HABILIDAD + TIPS).

EVs se mantienen en formato legacy (252/stat, 510 total). Conversión a PH: `PH = floor(EV/7.875)`. 252 EV ≈ 32 PH (cap stat). 66 PH totales = 252+252+12 EV ≈ 32+32+2 PH.

`scripts/build_builds_summary.py` valida cross-reference contra `raw/pokemon/`, `raw/ataques/`, `raw/objetos/`, `raw/habilidades/`. Detectó 5 nombres incorrectos en builds; ya parcheados.

## Key concepts

- [[ph-puntos-habilidad]]: conversión EV→PH es 1:1 funcional al respetar el cap 252
- [[preset-rol]]: builds curadas no siguen presets universales — usan benchmarks específicos
- [[damage-matrix]]: builds reales validan output de la matriz contra meta real
- [[scarf-candidate]]: builds top suelen ir Pañuelo o type booster

## Mentioned entities

- 12 builds en `raw/builds/`
- Pokémon cubiertos: Arcanine, Garchomp, Whimsicott, otros tier-1 launch meta

## Highlighted ideas

> Builds tier-1 priorizan benchmarks (sobrevivir un hit clave, outspeed un tier concreto) sobre presets universales como Sweeper/Tank.

> El formato de TIPS legacy no usa acentos — aceptable pero re-extraer si se reescribe.

## 🔗 Related

- [[ph-puntos-habilidad]]
- [[preset-rol]]
- [[panuelo-eleccion]]
- [[type-booster]]
- [[damage-matrix]]
- [[scarf-candidate]]
