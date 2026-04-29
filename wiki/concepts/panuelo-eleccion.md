---
title: Pañuelo Elección
date: 2026-04-29
type: concept
tags: [item, objeto, choice-scarf, speed]
---

# Pañuelo Elección

## Definition

Item "Objetos para Sostener" (`choice-scarf`). Multiplica Spe ×1.5 pero **bloquea al Pokémon en un único movimiento** durante todo el switch.

Categoría obtención: Beginning (entregado al inicio).

## Why it matters

En un meta sin Choice Band/Specs, el Pañuelo es la única forma de ganar speed brusco. Convierte atacantes mid-tier (90-110 base Spe) en outspeeders del top tier.

`scripts/build_speed_vs_scarf.py` cruza speed-tiers + scarf jump:
- Quién supera tu Spe optimizada (32 PH + naturaleza, sin Pañuelo)
- Quién supera tu Spe **si te ponen Pañuelo** (Spe × 1.5)
- Quién te supera **si tú también llevas Pañuelo**

## Trade-off

Lock movement = el Pokémon no puede cambiar de move sin switchear. Penaliza picks con utility (status moves, pivot moves) y obliga a planear el primer movimiento.

[[scarf-candidate]] ranquea Pokémon disponibles por candidato a Pañuelo:

```
score = spe_opt * 0.05
      + scarf_jump * 4
      + ohkos * 6
      + twohkos * 2
      + se_count * 1.5
      - 15 si ya outspeed a todos sin Pañuelo
```

## Connections

No afecta daño directo, sí turn order. [[damage-matrix]] no la modela. [[speed-vs-scarf]] cruza speed tiers con Pañuelo activado en ambos lados.

## Sources

- [[op-gg-items]] — `choice-scarf`
- `raw/mecanicas/objetos-calc.md`

## 🔗 Related

- [[speed-tier]]
- [[scarf-candidate]]
- [[type-booster]]
- [[baya-tipo]]
