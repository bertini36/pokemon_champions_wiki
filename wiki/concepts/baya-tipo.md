---
title: Baya tipo (resist berry)
date: 2026-04-29
type: concept
tags: [item, objeto, berry, baya, defense]
---

# Baya tipo (resist berry)

## Definition

18 bayas que reducen ×0.5 el primer hit super-eficaz del tipo concreto. Se consumen al activarse. Cobertura: **18 / 18 tipos**.

| Baya | Slug EN | Tipo que resiste |
|---|---|---|
| Baya Anjiro | `chople-berry` | Lucha |
| Baya Bariba | `babiri-berry` | Acero |
| Baya Caoca | `kasib-berry` | Fantasma |
| Baya Caquic | `kebia-berry` | Veneno |
| Baya Chilan | `chilan-berry` | Normal |
| Baya Dillo | `passho-berry` | Agua |
| Baya Drasi | `roseli-berry` | Hada |
| Baya Gualot | `tanga-berry` | Bicho |
| Baya Hibis | `occa-berry` | Fuego |
| Baya Kebia | `payapa-berry` | Psíquico |
| Baya Meloc | `wacan-berry` | Eléctrico |
| Baya Pasio | `coba-berry` | Volador |
| Baya Pomaro | `colbur-berry` | Siniestro |
| Baya Rimoya | `yache-berry` | Hielo |
| Baya Tamar | `charti-berry` | Roca |
| Baya Yecana | `haban-berry` | Dragón |
| Baya Zanama | `shuca-berry` | Tierra |
| Baya Zidra | `rindo-berry` | Planta |

## Why it matters

Una baya bien elegida convierte un OHKO previsible en un 2HKO, abriendo turnos clave: Tera Blast no las saca del meta porque Tera no existe en Pokémon Champions launch.

Aplicación turn-1: si quieres que tu Pokémon resista un primer ataque SE específico, baya. Si la pelea va a 2HKO sin SE, type booster vence.

## Aplicación

```python
if (item.type_resist_berry
    and move.type == item.type_resist_berry.resist_type
    and type_effectiveness > 1):
    final *= 0.5
    item.consumed = True
```

## Bayas no-resist (utilidad)

- `sitrus-berry` (Aranja) — recupera 25% HP a HP ≤ 50%
- `lum-berry` (Atania) — cura cualquier status
- `salac-berry` — +1 Spe a HP ≤ 25%
- `liechi-berry` — +1 Atk a HP ≤ 25%
- `petaya-berry` — +1 SpA a HP ≤ 25%

No afectan damage matrix.

## Connections

Modificador defensivo aplicado al final de [[formula-dano]]. [[damage-matrix]] tiene columna **+ Baya** que muestra el daño con la baya tipo correspondiente activada. Compite con [[type-booster]] y [[panuelo-eleccion]] como item slot.

## Sources

- [[op-gg-items]] — categoría Bayas (28 entradas, 18 son resist tipo)

## 🔗 Related

- [[formula-dano]]
- [[damage-matrix]]
- [[type-booster]]
- [[panuelo-eleccion]]
- [[spread-optimizer]]
