---
title: PH (Puntos de Habilidad)
date: 2026-04-29
type: concept
tags: [mecanica, ph, ev, stats]
---

# PH (Puntos de Habilidad)

## Definition

Sistema de inversión de stats de Pokémon Champions. Cada Pokémon tiene **66 PH totales**, máximo **32 PH por stat individual**. Un PH equivale a 7.875 EV de juegos clásicos: 32 PH = 252 EV (exactamente el cap clásico).

```
LEVEL            = 50      # Nivel fijo en todos los combates
IV               = 31      # Valor individual fijo todas las stats
MAX_TOTAL_AP     = 66      # PH totales por Pokémon
MAX_STAT_AP      = 32      # PH máximos por stat
AP_TO_EV_RATIO   = 7.875   # 1 PH = 7.875 EV
```

## Why it matters

Distribución típica VGC: **32 + 32 + 2** (cap dos stats principales, sobra 2). Las builds clásicas con spread 252/252/4 son directamente convertibles a 32/32/0 (los 4 EV sobrantes < 7.875 = 0 PH efectivo).

`floor(ev/4)` redondea hacia abajo: invertir 1 PH no siempre incrementa el stat final. Granularidad práctica ≈ 4 EV.

## Connections

Es la base de cualquier construcción de equipo. Multiplica con [[naturaleza]] (±10%) y luego con habilidades modeladas en [[habilidades-modeladas]] o items como [[type-booster]] para definir output ofensivo y supervivencia.

## Sources

- [[op-gg-calculator]] — bundle JS de la calculadora oficial
- [[builds-curated]] — formato EV legacy convertible 1:1 a PH

## 🔗 Related

- [[formula-stats]]
- [[naturaleza]]
- [[preset-rol]]
- [[spread-optimizer]]
- [[builds-curated]]
