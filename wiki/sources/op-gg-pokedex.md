---
title: op.gg Pokédex
date: 2026-04-29
type: source
tags: [op-gg, pokedex, pokemon, base-stats, abilities, moves]
original-source: https://op.gg/es/pokemon-champions/pokedex
---

# op.gg Pokédex

## Summary

Catálogo oficial de todos los Pokémon de Pokémon Champions: 258 entradas (incluye Megas y formas regionales). Cada ficha aporta tipos, stats base, habilidades disponibles y movepool completo. Es la base de identidad para cualquier análisis: stats finales, speed tiers, daño, cores y cobertura de tipos cuelgan de aquí.

La página principal usa una tabla virtualizada, pero el listado completo viaja en el payload de React Server Components inline. La ingesta intercepta `self.__next_f.push` para capturar el array `pokemon`.

## Key concepts

- [[ph-puntos-habilidad]]: stats finales se calculan con base stats de aquí + PH
- [[formula-stats]]: usa los `stats.{hp,attack,defense,spAttack,spDefense,speed}` de cada entrada
- [[damage-matrix]]: atacante y defensor se construyen desde fichas Pokédex
- [[coverage-matrix]]: movepool de cada Pokémon define cobertura SE
- [[speed-tier]]: base Spe + naturaleza + PH dan tier final

## Mentioned entities

- 258 entradas Pokémon (raw `pokedex_data.json`)
- 7 formas regionales y Mega adicionales en `raw/pokemon/` (Lycanroc 3, Rotom 6 → mapeadas al base op.gg)

## Highlighted ideas

> Pokédex op.gg es la fuente más fiel a Pokémon Champions disponible públicamente. PokéAPI clásica desfasa stats, abilities y movepool del juego.

> Los slugs en español sin acentos son la convención de filename; slug inglés en frontmatter para cross-reference op.gg.

## 🔗 Related

- [[op-gg-moves]]
- [[op-gg-abilities]]
- [[op-gg-types]]
- [[op-gg-calculator]]
- [[ph-puntos-habilidad]]
- [[formula-stats]]
