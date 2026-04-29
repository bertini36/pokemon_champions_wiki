---
title: Habilidades modeladas (calculadora)
date: 2026-04-29
type: concept
tags: [mecanica, habilidad, ability, damage-mod]
---

# Habilidades modeladas (calculadora)

## Definition

21 habilidades con efecto medible en daño que op.gg/calculator implementa. Resto (>280 del juego) existe pero **no afecta cálculo**.

| Clave EN | Tipo | Modificador | Condición |
|---|---|---|---|
| `adaptability` | STAB | × 2.0 | Move STAB |
| `technician` | Power | × 1.5 | `power ≤ 60` |
| `iron-fist` | Power | × 1.2 | Move puño |
| `strong-jaw` | Power | × 1.5 | Move mordisco |
| `mega-launcher` | Power | × 1.5 | Move pulso/aura |
| `reckless` | Power | × 1.2 | Move retroceso |
| `sheer-force` | Power | × 1.3 | Move efecto secundario |
| `tough-claws` | Power | × 1.3 | Move contacto |
| `huge-power` | Atk stat | × 2.0 | Siempre |
| `pure-power` | Atk stat | × 2.0 | Siempre |
| `hustle` | Atk stat | × 1.5 | Siempre (precisión reducida no modelada) |
| `gorilla-tactics` | Atk stat | × 1.5 | Siempre (lock no modelado) |
| `tinted-lens` | Effectiveness | × 2.0 a NVE | Move es NVE |
| `filter` | Effectiveness | × 0.75 a SE | Recibe SE |
| `solid-rock` | Effectiveness | × 0.75 a SE | Recibe SE |
| `prism-armor` | Effectiveness | × 0.75 a SE | Recibe SE |
| `blaze`, `torrent`, `overgrow`, `swarm` | Power | × 1.5 | Tipo del move (op.gg activa siempre, juego real solo a HP ≤ 1/3) |

### Sets de moves

- **Puños** (16): bullet-punch, comet-punch, dizzy-punch, drain-punch, dynamic-punch, fire-punch, focus-punch, hammer-arm, ice-punch, mach-punch, mega-punch, meteor-mash, power-up-punch, shadow-punch, sky-uppercut, thunder-punch
- **Mordiscos** (10): bite, crunch, fire-fang, fishious-rend, hyper-fang, ice-fang, jaw-lock, poison-fang, psychic-fangs, thunder-fang
- **Pulso** (6): aura-sphere, dark-pulse, dragon-pulse, heal-pulse, origin-pulse, water-pulse
- **Retroceso** (12): brave-bird, double-edge, flare-blitz, head-charge, head-smash, high-jump-kick, jump-kick, submission, take-down, volt-tackle, wild-charge, wood-hammer
- **Secundario** (17): air-slash, blizzard, body-slam, discharge, dragon-breath, fire-blast, flamethrower, ice-beam, iron-head, play-rough, psychic, rock-slide, scald, shadow-ball, sludge-bomb, thunderbolt, zen-headbutt
- **Contacto** (31): aqua-jet, body-slam, brave-bird, close-combat, crunch, double-edge, dragon-claw, drain-punch, earthquake, extreme-speed, flare-blitz, fly, giga-impact, ice-punch, iron-head, iron-tail, knock-off, leaf-blade, outrage, play-rough, poison-jab, quick-attack, return, shadow-claw, superpower, u-turn, volt-tackle, waterfall, wild-charge, x-scissor, zen-headbutt

## Why it matters

Estas 21 son la única lente con la que [[damage-matrix]] modifica daño. El resto de habilidades (Intimidación, Multiescamas, absorbedoras de tipo, Cuerpo Puro, Magic Bounce) hay que **modelarlas a mano** si se quiere análisis VGC realista.

`scripts/build_damage_matrix.py` extiende a 28 abilities (las 21 de op.gg + 7 defensivas custom: intimidate, multiscale, shadow-shield, water-absorb, volt-absorb, flash-fire, sap-sipper, levitate, lightning-rod, storm-drain, motor-drive, dry-skin, fluffy).

## Connections

Aplicado vía `AbilityMods` en [[formula-dano]]. [[damage-matrix]] aplica habilidad principal del Pokémon por defecto.

## Sources

- [[op-gg-calculator]] — `let d={adaptability:{...}}` en bundle JS
- [[op-gg-abilities]] — listado completo de 307 abilities

## 🔗 Related

- [[formula-dano]]
- [[damage-matrix]]
- [[op-gg-abilities]]
