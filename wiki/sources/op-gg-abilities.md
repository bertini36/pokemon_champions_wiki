---
title: op.gg Abilities
date: 2026-04-29
type: source
tags: [op-gg, abilities, habilidades]
original-source: https://op.gg/es/pokemon-champions/abilities
---

# op.gg Abilities

## Summary

Listado completo de las 307 habilidades de Pokémon Champions con descripción ES y contador de Pokémon que la portan. raw/habilidades/ contiene 309 entradas: 307 op.gg + 2 extras del Notion original (`opportunist`, `toxic-debris`). Cobertura op.gg: 100% (307/307).

Las 173 habilidades originales conservan `Categoría` y `Tier` de la ingesta Notion; las 136 añadidas desde op.gg en abril 2026 quedan con `Categoría: -` y `Tier: -`. Algunas descripciones siguen en inglés en op.gg.

Caso especial colisión slug-ES: **Unidad Ecuestre** existe como dos habilidades distintas (`as-one-glastrier`, `as-one-spectrier`) con el mismo nombre. Filenames diferenciados con sufijo.

## Key concepts

- [[habilidades-modeladas]]: solo 21 de 307 tienen efecto modelado en cálculo de daño
- [[formula-dano]]: las 21 modeladas se aplican vía `AbilityMods` (atk, spA, def, spD, powerModifier, stabModifier, effectivenessModifier)
- [[damage-matrix]]: aplica habilidad principal del Pokémon por defecto
- [[defensive-core]]: habilidades como Intimidación, Multiescamas, Pararrayos cambian profundamente el cálculo defensivo (no modeladas en op.gg)

## Mentioned entities

- 309 habilidades en `raw/habilidades/`
- 21 habilidades modeladas en `raw/mecanicas/habilidades-calc.md`

## Highlighted ideas

> >280 habilidades del juego no se reflejan en cálculo de daño op.gg. Para uso VGC serio hay que extender el modelo: Intimidación, Multiescamas, absorbedoras de tipo, Cuerpo Puro, Magic Bounce, etc.

> El slug inglés (clave PokéAPI) es la identidad estable. Filename ES sin acentos es solo de presentación.

## 🔗 Related

- [[op-gg-pokedex]]
- [[op-gg-calculator]]
- [[habilidades-modeladas]]
- [[formula-dano]]
