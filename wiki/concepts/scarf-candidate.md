---
title: Scarf Candidate
date: 2026-04-29
type: concept
tags: [analisis, panuelo, scarf, speed]
---

# Scarf Candidate

## Definition

Pokémon disponibles ranqueados como candidatos a llevar [[panuelo-eleccion]] según:

```
score = spe_opt * 0.05
      + scarf_jump * 4    (enemigos extra que outspeed con Pañuelo)
      + ohkos * 6         (OHKOs ya con su mejor STAB)
      + twohkos * 2
      + se_count * 1.5    (versatilidad SE)
      - 15 si ya outspeed a todos sin Pañuelo
```

Generado por `scripts/build_scarf_candidates.py`.

## Why it matters

Un Pañuelo solo merece slot si:

1. El Pokémon **gana enemigos** que sin Pañuelo no superaba (`scarf_jump > 0`).
2. Tiene **buen daño** (OHKOs y 2HKOs en el meta) — Pañuelo en un atacante débil no escala.
3. Tiene **versatilidad SE** ya que el lock le impedirá pivotar.

La penalty `-15 si ya outspeed a todos` filtra Pokémon que ya van bien con type booster: Pañuelo ahí pierde damage por nada.

## Trade-off ofensivo

Pañuelo en un Pokémon con type booster ya equipado **no apila**. Eliges:
- Pañuelo (Spe ×1.5, lock, sin damage boost) → outspeed
- Type booster (power ×1.2 sin lock) → más daño, free moves

[[damage-matrix]] aplica type booster por defecto al atacante. La columna Pañuelo en `speed-vs-scarf.md` se usa para construir el ranking.

## Connections

Combina [[speed-tier]] (spe optimizada vs Pañuelo enemigo), [[damage-matrix]] (OHKO/2HKO count), [[coverage-matrix]] (SE count), [[panuelo-eleccion]] (lock cost).

## Sources

- `raw/calculos/scarf-candidates.md` (74 líneas)
- `raw/calculos/speed-vs-scarf.md` (598 líneas)

## 🔗 Related

- [[panuelo-eleccion]]
- [[speed-tier]]
- [[damage-matrix]]
- [[coverage-matrix]]
- [[type-booster]]
