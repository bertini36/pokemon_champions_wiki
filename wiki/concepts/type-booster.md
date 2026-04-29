---
title: Type Booster (×1.2)
date: 2026-04-29
type: concept
tags: [item, objeto, type-booster, damage-mod]
---

# Type Booster (×1.2)

## Definition

18 ítems "Objetos para Sostener" que multiplican × 1.2 el power de movimientos del tipo correspondiente. Cobertura completa: **18 / 18 tipos**.

| Nombre ES | Slug EN | Tipo |
|---|---|---|
| Carbón | `charcoal` | Fuego |
| Agua Mística | `mystic-water` | Agua |
| Semilla Milagro | `miracle-seed` | Planta |
| Imán | `magnet` | Eléctrico |
| Antiderretir | `never-melt-ice` | Hielo |
| Cinturón Negro | `black-belt` | Lucha |
| Flecha Venenosa | `poison-barb` | Veneno |
| Arena Fina | `soft-sand` | Tierra |
| Pico Afilado | `sharp-beak` | Volador |
| Cuchara Torcida | `twisted-spoon` | Psíquico |
| Polvo Plata | `silver-powder` | Bicho |
| Piedra Dura | `hard-stone` | Roca |
| Hechizo | `spell-tag` | Fantasma |
| Colmillo Dragón | `dragon-fang` | Dragón |
| Gafas de Sol | `black-glasses` | Siniestro |
| Revest. Metálico | `metal-coat` | Acero |
| Fairy Feather | `fairy-feather` | Hada |
| Pañuelo de Seda | `silk-scarf` | Normal |

## Why it matters

Choice Band/Specs/Life Orb/Expert Belt **NO existen en Pokémon Champions**. El meta favorece type boosters fijos × 1.2 (sin lock-in) frente al all-in de Choice items.

Atacantes deben confiar en SpA/Atk inflada vía Modesta/Firme + 32 PH + type booster ×1.2. La calculadora op.gg **no modela** type boosters; `scripts/build_damage_matrix.py` los aplica por defecto al atacante.

Apila multiplicativamente con habilidades (Adaptability, Iron Fist, etc.) y STAB.

## Aplicación

```python
if item.type_booster and move.type == item.type_booster.type:
    atk_mods.powerModifier *= 1.2
```

## Connections

Modificador de power aplicado en [[formula-dano]]. [[damage-matrix]] lo usa por defecto en el atacante. Compite con [[panuelo-eleccion]] y [[baya-tipo]] como item slot.

## Sources

- [[op-gg-items]] — 18 cards "Objetos para Sostener"
- `raw/mecanicas/objetos-calc.md`

## 🔗 Related

- [[formula-dano]]
- [[damage-matrix]]
- [[panuelo-eleccion]]
- [[baya-tipo]]
