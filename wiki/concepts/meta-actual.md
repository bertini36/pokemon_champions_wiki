---
title: Meta actual (Pokémon Champions VGC)
date: 2026-05-01
type: concept
tags: [meta, usage, tier-list, vgc]
---

# Meta actual (Pokémon Champions VGC)

## Definition

Tier list y tasas de uso vigentes del meta competitivo de Pokémon Champions. Página **volátil**: se invalida con cada parche y con cada nuevo snapshot de [[pokemon-zone-meta]].

## Snapshot vigente

**Fuente:** `raw/meta/usage-2026-04-30.md`
**Regulación:** M-A (Doubles VGC)
**Muestra:** 121 torneos comunidad + ladder rankeado, 12.354 equipos, 207 Pokémon ranqueados.

### Top 20 doubles

| Rank | Pokémon | Uso (%) | Win Rate (%) |
|------|---------|---------|--------------|
| 1 | Sneasler | 52.1 | 52.1 |
| 2 | Incineroar | 46.2 | 51.4 |
| 3 | Garchomp (incl. Mega) | 40.4 | 51.8 |
| 4 | Kingambit | 34.6 | 52.4 |
| 5 | Sinistcha | 28.8 | 53.2 |
| 6 | Basculegion | 25.5 | 52.8 |
| 7 | Aerodactyl | 23.3 | 51.7 |
| 8 | Charizard (incl. Mega) | 21.1 | 51.6 |
| 9 | Rotom-Lavado | 18.9 | 51.6 |
| 10 | Whimsicott | 16.7 | 49.6 |
| 11 | Pelipper | 15.5 | 51.2 |
| 12 | Floette Flor Eterna | 14.6 | 53.8 |
| 13 | Tyranitar | 13.7 | 51.8 |
| 14 | Farigiraf | 12.8 | 52.6 |
| 15 | Archaludon | 11.9 | 53.4 |
| 16 | Milotic | 11.0 | 51.8 |
| 17 | Dragonite | 10.3 | 49.8 |
| 18 | Froslass | 9.6 | 54.2 |
| 19 | Venusaur (incl. Mega) | 8.9 | 52.4 |
| 20 | Talonflame | 8.2 | 54.5 |

### Cores / arquetipos top

- **Goodstuffs Intimidación:** Incineroar + Kingambit (priority Siniestro post-Intimidación).
- **Tailwind:** Whimsicott + Mega Garchomp (Bromista Viento Afín dobla Vel a Garchomp 4 turnos).
- **Lluvia:** Pelipper (Llovizna) + Basculegion (Adaptabilidad Lanzaolas).
- **Arena:** Mega Tyranitar (Tiranitarita Arena) + Mega Garchomp (Tirano de Arena post-mega).
- **Hadas overperformers:** Floette Flor Eterna y Sinistcha tienen los win rate más altos del top 12.

## Discrepancia con el wiki

> [!warning] El campo `Disponible` en `wiki/entities/pokemon/*.md` está **desactualizado**. Solo 15 fichas marcan `Disponible: Sí`, pero el meta real usa al menos los 207 Pokémon del snapshot. Las decisiones de team building deben basarse en este meta-actual y no en el filtro `Disponible: Sí`. **Acción:** re-ejecutar `scripts/build_wiki_entities.py` con datos actualizados de op.gg, o aceptar el desfase y usar este snapshot como fuente de verdad sobre disponibilidad.

## Why it matters

El meta dicta:

1. Qué Pokémon vas a encontrarte → priorizar [[counter-meta]]
2. Qué Pokémon valida tu pick → si está en top, hay respaldo estadístico
3. Qué amenazas debe sobrevivir tu equipo → input crítico de [[spread-optimizer]] y [[threat-list]]

## Frecuencia de actualización

Re-ingestar snapshot cuando:
- Hay parche de balance.
- Han pasado más de 2 semanas desde el último snapshot.
- Detectas desfase entre el meta documentado y el de partidas reales.

## Connections

Página derivada de [[pokemon-zone-meta]]. Cruza con [[damage-matrix]], [[threat-list]] y [[defensive-core]] para producir [[counter-meta]] cuando se pida análisis explícito.

## Sources

- [[pokemon-zone-meta]] — fuente de uso ranked (apuntada por agregadores)
- `raw/meta/usage-2026-04-30.md` — snapshot literal

## 🔗 Related

- [[pokemon-zone-meta]]
- [[counter-meta]]
- [[damage-matrix]]
- [[threat-list]]
- [[defensive-core]]
