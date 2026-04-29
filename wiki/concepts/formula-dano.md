---
title: Fórmula de Daño
date: 2026-04-29
type: concept
tags: [mecanica, dano, damage, stab, formula]
---

# Fórmula de Daño

## Definition

Replica de la lógica que op.gg ejecuta al calcular daño físico/especial.

```python
is_physical = move.category == "physical"
attack  = floor(attacker.stats[atk_key]  * mods.attack_or_spA)
defense = floor(defender.stats[def_key]  * mods.defense_or_spD)
base = floor(
    floor(2 * 50 / 5 + 2)                    # = 22
  * floor(move.power * mods.powerModifier)
  * floor(attack / defense)
  / 50
) + 2
final = base * type_effect * def_mods.effectivenessModifier * stab
min_dmg = floor(0.85 * final)
max_dmg = floor(final)
```

## Why it matters

`Math.floor` se aplica en **cada paso intermedio**. Orden de operaciones es crítico: `move.power * powerModifier` también va dentro de `floor` antes de multiplicar; `attack/defense` se redondea **antes** de multiplicar por power.

STAB y type effectiveness son multiplicadores `*` puros sin redondeo intermedio.

### Modificadores activos

| Caso | Multiplicador |
|---|---|
| STAB normal | × 1.5 |
| Adaptabilidad | × 2.0 |
| Súper eficaz | × 2 (× 4 si dual SE) |
| Eficacia normal | × 1 |
| Poco eficaz | × 0.5 (× 0.25 si dual NVE) |
| Sin efecto | × 0 |
| Filter / Solid Rock / Prism Armor reciben SE | × 0.75 |
| Tinted Lens pega NVE | × 2 (sube a normal) |

### Roll

La calculadora **no implementa** los 16 valores Gen-style. Solo extremos `floor(0.85*final)` y `floor(final)`. Para reportes "X% OHKO" hay que extender.

## Gaps no modelados

| No modelado | Impacto |
|---|---|
| Objetos (Pañuelo, Vidas...) | × 1.2 a × 1.5 |
| Clima | × 1.5 / × 0.5 |
| Terreno | × 1.3 + bloqueos |
| Críticos | × 1.5 (1/24) |
| Multi-hit | golpes 2-5 |
| Spread reduction (doubles) | × 0.75 |
| Burn | × 0.5 atk físico |
| Boost stages | × 1.5 a × 4 |
| Helping Hand | × 1.5 |
| Reflejo / Pantalla de Luz | × 0.5 (× 2/3 doubles) |

## Connections

Núcleo de [[damage-matrix]], [[threat-list]], [[spread-optimizer]] y [[scarf-candidate]]. Recibe inputs de [[formula-stats]] (atk/def stats), [[habilidades-modeladas]] (ability mods), [[type-booster]] (powerModifier ×1.2), [[baya-tipo]] (×0.5 SE recibido).

## Sources

- [[op-gg-calculator]] — `b="physical"===i.category` en bundle JS

## 🔗 Related

- [[formula-stats]]
- [[habilidades-modeladas]]
- [[type-booster]]
- [[baya-tipo]]
- [[damage-matrix]]
- [[threat-list]]
- [[spread-optimizer]]
