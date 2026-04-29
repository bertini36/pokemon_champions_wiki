---
title: Damage Matrix
date: 2026-04-29
type: concept
tags: [analisis, damage, matrix, ohko, 2hko]
---

# Damage Matrix

## Definition

Matriz N × N de daño calculado para cada atacante disponible vs cada defensor disponible. Cada celda contiene min/max damage, % HP, KO label (OHKO / 2HKO / 3HKO+).

Generado por `scripts/build_damage_matrix.py`.

### Setup canónico

- **Atacante**: preset Sweeper o Physical (según mejor STAB) + naturaleza + type booster ×1.2 + STAB
- **Defensor**: spread Bulky 32 HP / 16 Def / 16 SpD
- **Movimiento**: el de mayor potencia entre los STAB del movepool del atacante
- **Roll**: 0.85 → 1.00 (sin críticos)
- **Habilidad**: principal del Pokémon aplicada por defecto (28 abilities modeladas)

### Columnas extras

- **+ Baya**: defensor con baya tipo correspondiente activada (×0.5 si SE)
- **Si quemado**: atacante quemado (×0.5 atk físico) — ⚠️ colapsa cuando `floor(atk/def) ≤ 1`

## Why it matters

Resume en una vista cuántos OHKO/2HKO existen en el meta disponible. Punto de partida para [[threat-list]] (vista inversa por defensor) y [[spread-optimizer]] (PH mínimos para sobrevivir top amenazas).

## Limitaciones

- Sin clima, terreno, críticos, multi-hit, spread reduction (doubles), boost stages
- Sin [[panuelo-eleccion]] (no afecta daño directo, sí turn order)
- Setup defensivo único universal — no optimizado por matchup
- Habilidades no modeladas (Intimidación, Multiescamas no aparecen aquí salvo extensión custom)
- Para análisis VGC serio: cruzar con [[speed-tier]], [[panuelo-eleccion]], [[defensive-core]]

## Connections

Núcleo del sistema analítico. Inputs: [[op-gg-pokedex]] (stats + movepool), [[op-gg-moves]] (power + type), [[op-gg-types]] (eficacia), [[habilidades-modeladas]], [[type-booster]], [[formula-stats]], [[formula-dano]]. Outputs: [[threat-list]], [[spread-optimizer]], [[scarf-candidate]] (parcialmente).

## Sources

- `raw/calculos/damage-matrix.md` (399 líneas, 225 celdas en setup actual 15×15)
- `raw/calculos/damage-matrix.json`

## 🔗 Related

- [[formula-dano]]
- [[formula-stats]]
- [[habilidades-modeladas]]
- [[type-booster]]
- [[threat-list]]
- [[spread-optimizer]]
- [[coverage-matrix]]
