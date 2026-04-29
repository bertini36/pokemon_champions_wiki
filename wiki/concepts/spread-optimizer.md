---
title: Spread Optimizer
date: 2026-04-29
type: concept
tags: [analisis, spread, ph, ev, defensive]
---

# Spread Optimizer

## Definition

Para cada defensor, calcula los **PH mínimos en HP + Def/SpD** necesarios para sobrevivir cada amenaza top de la [[damage-matrix]] (atacantes que le hacen ≥50% por defecto).

Naturaleza defensiva asumida: **Osada** (+Def -Atk) para hits físicos, **Cauta** (+SpD -SpA) para hits especiales.

Generado por `scripts/build_spread_optimizer.py` desde `raw/calculos/damage-matrix.json` y `raw/pokemon/`.

## Why it matters

Convierte el preset universal Tank/SpD Tank en spreads **específicos contra meta**: en lugar de 32 HP / 32 Def, da spreads como "20 HP / 18 Def" suficientes para sobrevivir las top 8 amenazas, con los PH restantes libres para Spe/Atk/SpA.

## Output por defensor

Para cada amenaza relevante:
- Atacante + move + daño base
- PH HP/Def(SpD) mínimos para que `max_dmg < HP`
- Sobrante de PH disponibles para el resto

## Limitaciones

- Asume PH Spe = 0 (defensor lento). Si quieres mantener velocidad, resta PH del HP/Def disponibles.
- Type booster del atacante = ×1.2 fijo. Sin Pañuelo / Vidas / críticos / clima.
- Sin habilidades defensivas que cambian el cálculo (Intimidación rebaja el atk antes de calcular). El optimizer usa daño "base" sin Intimidación.
- Sin [[baya-tipo]] — si el defensor lleva baya tipo SE, el spread necesario baja.

## Connections

Cruce de [[damage-matrix]] (output) y [[threat-list]] (defensores ordenados por vulnerabilidad). Output útil para construir builds reales en [[builds-curated]]. Apila con [[baya-tipo]] o [[type-booster]] defensivo.

## Sources

- `raw/calculos/spread-optimizer.md` (177 líneas)

## 🔗 Related

- [[damage-matrix]]
- [[threat-list]]
- [[ph-puntos-habilidad]]
- [[naturaleza]]
- [[preset-rol]]
- [[baya-tipo]]
