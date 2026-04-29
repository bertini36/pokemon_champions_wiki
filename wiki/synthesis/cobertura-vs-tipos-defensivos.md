---
title: Cobertura ofensiva vs Tipos defensivos óptimos
date: 2026-04-29
type: synthesis
tags: [coverage, types, defensive, sintesis]
---

# Cobertura ofensiva vs Tipos defensivos óptimos

## Idea central

Cruzar [[coverage-matrix]] con la matriz defensiva de [[op-gg-types]] revela:

1. Qué Pokémon ofensivos cubren más de 17 tipos SE (max 18) — útiles como atacantes "universales"
2. Qué tipos defensivos resisten más golpes a la vez
3. Qué cores combinan ambos: atacante con coverage 18/18 + defensor con resists múltiples → equipo dominante

## Atacantes con coverage máximo

Del pool disponible (Champions launch):

| Pokémon | Tipos | SE coverage |
|---|---|---|
| Greninja | Agua/Siniestro | 18/18 |
| Garchomp | Dragón/Tierra | 18/18 |

Coverage 18/18 = tienen un movimiento STAB o de tipo cubriente para cada tipo defensivo. Su único filtro es daño bruto y matchup velocidad.

## Tipos defensivos top (resist count)

Del [[op-gg-types]], ranking puro de resistencias:

| Tipo | Resiste (×0.5) | Inmune (×0) | Total mitigado |
|---|---|---|---|
| [[Acero]] | 10 | 1 (Veneno) | 11 |
| [[Agua]] | 4 | 0 | 4 |
| [[Fuego]] | 6 | 0 | 6 |
| [[Hada]] | 3 | 1 (Dragón) | 4 |
| [[Volador]] | 3 | 1 (Tierra) | 4 |

[[Acero]] domina como ancla defensiva: 10 resistencias + inmunidad a veneno. Único contra debilidad ×4 contra Acero (hay solo 3: Fuego/Lucha/Tierra).

## Combinación ofensivo + defensivo

Un equipo robusto típicamente combina:

- 1 atacante con coverage 18/18 (Greninja o Garchomp)
- 1 ancla defensiva tipo [[Acero]] o doble pivot con [[Fuego]]/[[Agua]] complementarios
- 1-2 atacantes secundarios para cubrir gaps que el tipo defensivo del ancla deja expuestos

[[defensive-core]] genera los pares; este wiki cruza el ranking ofensivo de coverage con el defensivo de tipos para sugerir las parejas más sólidas.

## Connections

Cruce de [[coverage-matrix]], [[op-gg-types]], [[defensive-core]] y las 18 entidades de tipo. Útil cuando se pide "qué Pokémon cubre más" o "qué core defensivo puro merece la pena".

## 🔗 Related

- [[coverage-matrix]]
- [[op-gg-types]]
- [[defensive-core]]
- [[Acero]]
- [[Fuego]]
- [[Agua]]
- [[Hada]]
- [[Volador]]
- [[damage-matrix]]
- [[flujo-construccion-equipo]]
