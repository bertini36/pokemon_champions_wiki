---
title: Naturaleza
date: 2026-04-29
type: concept
tags: [mecanica, naturaleza, nature, stat-mult]
---

# Naturaleza

## Definition

25 naturalezas: 5 neutrales (efecto idéntico, cosmética) + 20 stat-boosting (+10% una stat, -10% otra). Multiplicador 1.1 / 0.9 / 1.0. **HP nunca afectado**.

## Tabla completa

| Clave EN | Nombre ES | +Stat | -Stat |
|---|---|---|---|
| `hardy` | Fuerte | — | — |
| `docile` | Dócil | — | — |
| `serious` | Seria | — | — |
| `bashful` | Tímida | — | — |
| `quirky` | Rara | — | — |
| `lonely` | Huraña | Atk | Def |
| `brave` | Audaz | Atk | Spe |
| `adamant` | Firme | Atk | SpA |
| `naughty` | Pícara | Atk | SpD |
| `bold` | Osada | Def | Atk |
| `relaxed` | Plácida | Def | Spe |
| `impish` | Agitada | Def | SpA |
| `lax` | Floja | Def | SpD |
| `modest` | Modesta | SpA | Atk |
| `mild` | Afable | SpA | Def |
| `quiet` | Mansa | SpA | Spe |
| `rash` | Alocada | SpA | SpD |
| `calm` | Serena | SpD | Atk |
| `gentle` | Amable | SpD | Def |
| `sassy` | Grosera | SpD | Spe |
| `careful` | Cauta | SpD | Atk |
| `timid` | Miedosa | Spe | Atk |
| `hasty` | Activa | Spe | Def |
| `jolly` | Alegre | Spe | SpA |
| `naive` | Ingenua | Spe | SpD |

## Why it matters

Las naturalezas más usadas en VGC son las que minimizan la stat irrelevante:

| Naturaleza | Cuándo usar |
|---|---|
| **Modesta** (+SpA -Atk) | Atacante especial puro sin Foul Play en su contra |
| **Tímida** (+Spe -Atk) | Atacante especial que necesita superar a Garchomp/Dragapult |
| **Firme** (+Atk -SpA) | Atacante físico puro |
| **Alegre** (+Spe -SpA) | Atacante físico que necesita Spe |
| **Osada** (+Def -Atk) | Wall físico que no usa Atk |
| **Cauta** (+SpD -SpA) | Wall especial físico-atacante |
| **Audaz** (+Atk -Spe) | Trick Room atacante físico |
| **Mansa** (+SpA -Spe) | Trick Room atacante especial |

## Connections

Multiplicador final aplicado al stat ya redondeado en [[formula-stats]]. Las 5 neutrales son intercambiables salvo cumplimiento "naturaleza preferida" en eventos.

## Sources

- [[op-gg-calculator]] — `let N=[{key:"hardy"...}]` en bundle JS

## 🔗 Related

- [[formula-stats]]
- [[ph-puntos-habilidad]]
- [[preset-rol]]
- [[speed-tier]]
