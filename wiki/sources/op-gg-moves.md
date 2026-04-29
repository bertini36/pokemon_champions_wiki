---
title: op.gg Moves
date: 2026-04-29
type: source
tags: [op-gg, moves, ataques, power, accuracy, pp]
original-source: https://op.gg/es/pokemon-champions/moves
---

# op.gg Moves

## Summary

Catálogo de los 919 ataques de Pokémon Champions. Cada card aporta nombre ES, tipo, categoría (Físico/Especial/Estado), potencia, precisión, PP y descripción. Las cards no virtualizan: harvest directo del DOM con un querySelector contra `a[href*="/moves/"]`.

raw conserva PP legacy en juegos clásicos; op.gg refleja PP actual de Pokémon Champions. Ambos valores se preservan en cada `<slug>.md` (`PP` y `PP (op.gg)`). Power y Accuracy coinciden 1:1 en los 655 originales; PP discrepa en 246.

## Key concepts

- [[formula-dano]]: usa `move.power`, `move.category`, `move.type` para calcular daño
- [[damage-matrix]]: el move STAB de mayor potencia define el atacante
- [[coverage-matrix]]: el movepool entero define qué tipos puede pegar SE un Pokémon
- [[habilidades-modeladas]]: sets de moves (puños, mordiscos, pulso, retroceso, secondary, contacto) habilitan los modificadores ×1.2/×1.3/×1.5 de habilidades como Iron Fist, Strong Jaw, Mega Launcher

## Mentioned entities

- 919 movimientos en `raw/ataques/` (655 enriquecidos + 264 generados desde op.gg)
- Categoría: 3 valores (`Físico`, `Especial`, `Estado`)

## Highlighted ideas

> El PP de movimientos ha cambiado en Pokémon Champions vs gens anteriores. Mantener ambos valores es necesario para no perder la información histórica ni la actual.

> Algunas descripciones de moves recientes (Z-Moves, Max Moves de tutoriales, gimmicks Gen 9) llegan en inglés desde op.gg sin traducir.

## 🔗 Related

- [[op-gg-pokedex]]
- [[op-gg-types]]
- [[formula-dano]]
- [[damage-matrix]]
- [[coverage-matrix]]
- [[habilidades-modeladas]]
