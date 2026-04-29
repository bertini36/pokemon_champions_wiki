---
title: Fórmula de Stats
date: 2026-04-29
type: concept
tags: [mecanica, stats, formula, hp, atk, def, spa, spd, spe]
---

# Fórmula de Stats

## Definition

Cómo se calculan los 6 stats finales (HP, Atk, Def, SpA, SpD, Spe) a Nivel 50 en Pokémon Champions desde base stat + PH + naturaleza.

### HP

```python
def calc_hp(base_hp: int, ap_hp: int) -> int:
    ev = math.floor(ap_hp * 7.875)
    return math.floor((2 * base_hp + 31 + math.floor(ev / 4)) * 50 / 100) + 50 + 10
```

El bonus `+50+10` agrupa el bonus por nivel (50) y el bonus fijo de HP (10).

### Resto (Atk, Def, SpA, SpD, Spe)

```python
def calc_stat(base, ap, nature, stat_name):
    ev = math.floor(ap * 7.875)
    raw = math.floor((2 * base + 31 + math.floor(ev / 4)) * 50 / 100) + 5
    if nature.increased == stat_name: mult = 1.1
    elif nature.decreased == stat_name: mult = 0.9
    else: mult = 1.0
    return math.floor(raw * mult)
```

## Why it matters

Determina cualquier benchmark VGC: speed tiers, HP final para sobrevivir hits clave, output ofensivo. La fórmula es **idéntica** a Gen 1-9 — la única diferencia es que `LEVEL=50`, `IV=31` y EV pasa por el factor `7.875` desde PH.

HP nunca recibe multiplicador de naturaleza. La naturaleza se aplica sobre el resultado **ya redondeado**.

## Validación contra calc UI

| Pokémon | base | PH | Naturaleza | Stat |
|---|---|---|---|---|
| Charizard SpA=109 | 109 | 32 | Modesta (+SpA) | 177 |
| Tyranitar HP=100 | 100 | 32 | (cualquiera) | 207 |
| Dragapult Spe=142 | 142 | 32 | Tímida (+Spe) | 213 |

## Connections

Punto de partida de [[damage-matrix]], [[speed-tier]] y [[spread-optimizer]]. Usa base stats de [[op-gg-pokedex]] y constantes/factor de [[ph-puntos-habilidad]].

## Sources

- [[op-gg-calculator]] — `function E(e,s,t)` en bundle JS

## 🔗 Related

- [[ph-puntos-habilidad]]
- [[naturaleza]]
- [[formula-dano]]
- [[speed-tier]]
- [[damage-matrix]]
