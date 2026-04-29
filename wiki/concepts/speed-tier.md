---
title: Speed Tier (Nv.50)
date: 2026-04-29
type: concept
tags: [stat, speed, spe, tier]
---

# Speed Tier (Nv.50)

## Definition

Velocidad final de un Pokémon a Nivel 50, calculada con [[formula-stats]] desde base Spe + PH Spe + naturaleza. Cuatro escenarios canónicos:

| Escenario | PH Spe | Naturaleza | Mult |
|---|---|---|---|
| **Spe (+Nat)** | 32 | + Spe | 1.1 |
| **Spe neutral** | 32 | neutral | 1.0 |
| **Spe (-Nat)** | 0 | - Spe | 0.9 |
| **Spe Pañuelo** | 32 | + Spe | 1.1 × 1.5 |

## Why it matters

En Pokémon Champions, **outspeed = inicia turno = control**. Decisiones clave:

- ¿Subo a Tímida (+Spe -Atk) o me quedo con Modesta (+SpA -Atk)?
- ¿Llevo Pañuelo Elección (×1.5 Spe pero lock) o type booster (×1.2 power)?
- ¿Cuántos PH Spe basta para superar al benchmark del meta (Garchomp Spe 102 → 162 con +Nat 32 PH)?

## Speed creep

Caso típico: si el meta corre con 32 PH Spe + Tímida en Garchomp (162), un rival opta por 28 PH Spe en otro Pokémon de base 100 para llegar a 161 — pierde la carrera. Subir 32 garantiza, 28 ahorra 4 PH para HP/SpD pero arriesga.

## Análisis cruzado

`scripts/build_speed_tiers.py` tabula los 15 Pokémon disponibles en los 4 escenarios. `scripts/build_speed_vs_scarf.py` añade el cruce con [[panuelo-eleccion]].

## Connections

Output directo de [[formula-stats]] aplicado a `speed`. Input de [[scarf-candidate]] (cuántos enemigos extra outspeed con Pañuelo) y de cualquier [[spread-optimizer]] que necesite mantener un benchmark Spe.

## Sources

- `raw/calculos/speed-tiers-l50.md`
- `raw/calculos/speed-vs-scarf.md`

## 🔗 Related

- [[formula-stats]]
- [[naturaleza]]
- [[ph-puntos-habilidad]]
- [[panuelo-eleccion]]
- [[scarf-candidate]]
