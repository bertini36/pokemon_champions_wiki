---
title: op.gg Calculator (bundle JS)
date: 2026-04-29
type: source
tags: [op-gg, calculator, bundle, formula, mecanicas]
original-source: https://op.gg/es/pokemon-champions/calculator
---

# op.gg Calculator (bundle JS)

## Summary

Bundle minificado (~46 KB) `app-router/_next/static/chunks/app/[lang]/pokemon-champions/calculator/page-*.js` que contiene la lógica interna de stats y daño que op.gg ejecuta en el cliente. Es la fuente más fiable disponible mientras Game Freak no publique las fórmulas oficiales.

De aquí salen las constantes globales (`LEVEL=50`, `IV=31`, `MAX_TOTAL_AP=66`, `MAX_STAT_AP=32`, `AP_TO_EV_RATIO=7.875`), las dos fórmulas (stats + daño), las 25 naturalezas, los 4 presets de rol, las 21 habilidades modeladas y los 6 sets de moves por categoría.

## Key concepts

- [[formula-stats]]: Nv.50 fijo, IV=31 fijo, PH 0-32 + naturaleza ±10%
- [[formula-dano]]: Math.floor en cada paso intermedio, roll 0.85 → 1.0 (sin 16 valores Gen-style)
- [[ph-puntos-habilidad]]: 32 PH = 252 EV equivalentes (factor 7.875)
- [[naturaleza]]: 25 (5 neutrales + 20 ±10%)
- [[preset-rol]]: 4 spreads (Sweeper, Physical, Tank, SpD Tank)
- [[habilidades-modeladas]]: 21 con efecto en cálculo de daño
- [[type-booster]]: NO modelados por op.gg (gap conocido)

## Mentioned entities

- 6 ficheros en `raw/mecanicas/` derivados del bundle
- Bundle hash cambia con cada despliegue: re-extracción periódica

## Highlighted ideas

> La calculadora **no modela**: objetos, clima, terreno, críticos, multi-hit, multi-target, burn, boost stages, ni los 16 valores de roll Gen-style. Para uso VGC serio extender el modelo.

> Las habilidades pinch (`blaze`/`torrent`/`overgrow`/`swarm`) en op.gg activan **siempre**, no a HP ≤ 1/3 como dicta el juego.

> La fórmula stat usa el bonus +50+10 para HP y +5 para el resto, aplicado **antes** del multiplicador de naturaleza.

## 🔗 Related

- [[formula-stats]]
- [[formula-dano]]
- [[ph-puntos-habilidad]]
- [[naturaleza]]
- [[preset-rol]]
- [[habilidades-modeladas]]
- [[type-booster]]
