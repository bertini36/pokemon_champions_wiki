---
title: Flujo de construcción de equipo VGC
date: 2026-04-29
type: synthesis
tags: [vgc, team-building, workflow, sintesis]
---

# Flujo de construcción de equipo VGC

## Idea central

Construir un equipo VGC para Pokémon Champions sigue una secuencia repetible que combina datos del meta + cálculo + cobertura. Cada paso usa una página concreta del wiki como output principal.

## Secuencia

```
1. Meta snapshot          → [[meta-actual]]      (pokemon-zone usage)
2. Top amenazas           → [[threat-list]]      (vista inversa damage)
3. Core defensivo base    → [[defensive-core]]   (par con score top)
4. Spread defensivo       → [[spread-optimizer]] (PH min vs amenazas)
5. Atacante principal     → [[damage-matrix]]    (OHKO/2HKO contra meta)
6. Cobertura ofensiva     → [[coverage-matrix]]  (gaps SE del atacante)
7. Speed control          → [[speed-tier]]       (qué outspeed)
8. Pañuelo / Booster      → [[scarf-candidate]]  (item slot decisivo)
9. Validar build          → [[builds-curated]]   (formato canónico)
```

## Heurística por paso

### Paso 1-2: meta + amenazas
Mira el top 10-15 del snapshot vigente. Saca de [[threat-list]] el subset que solapa con el top usage; esos son tus *threats reales*.

### Paso 3-4: doble pivot defensivo
Top score de [[defensive-core]] que **además** sobreviva a los threats reales del paso 2 con el [[spread-optimizer]].

### Paso 5-7: atacantes
Picks 3-6 con [[damage-matrix]] OHKO/2HKO contra los threats. Validar [[coverage-matrix]] para no compartir gap. Cuadrar [[speed-tier]] para no perder turns clave.

### Paso 8: item slot
- ¿El atacante ya outspeed el meta sin Pañuelo? → [[type-booster]] ×1.2 (mejor damage permanente).
- ¿Necesita 1 turno mítico contra X? → [[panuelo-eleccion]] (Spe ×1.5, lock OK porque 1 movimiento basta).
- ¿El atacante muere a 1 SE específico? → [[baya-tipo]] (×0.5 ese hit).
- Penalty `-15 si ya outspeed a todos sin Pañuelo` en [[scarf-candidate]] confirma cuándo Pañuelo no merece slot.

### Paso 9: build canónica
Cada Pokémon final → `raw/builds/<pokemon>-<concepto>.md`. Re-ejecutar `scripts/build_builds_summary.py` para validar consistencia con [[op-gg-pokedex]], [[op-gg-moves]], [[op-gg-items]].

## Trade-offs típicos

| Decisión | A favor de | En contra de |
|---|---|---|
| Sweeper Modesta vs Tímida | Modesta = más SpA | Tímida = supera +Spe del meta |
| 32 PH HP vs 28 PH HP + 4 Spe | HP máximo | Speed creep posible |
| Pañuelo vs type booster | Pañuelo = outspeed | Booster = +20% power permanente |
| Baya tipo vs type booster | Baya = sobrevives 1 SE | Booster = no se consume |
| Tank universal vs spread vs amenazas | Universal = simple | Tuning = mejor en partidas reales |

## Inputs y outputs

Esta página sintetiza casi todo el wiki. Usar como guía cada vez que se pida "armar equipo VGC con X" o "build alrededor de Y".

## 🔗 Related

- [[meta-actual]]
- [[counter-meta]]
- [[damage-matrix]]
- [[threat-list]]
- [[defensive-core]]
- [[spread-optimizer]]
- [[coverage-matrix]]
- [[scarf-candidate]]
- [[speed-tier]]
- [[type-booster]]
- [[panuelo-eleccion]]
- [[baya-tipo]]
- [[builds-curated]]
- [[ph-puntos-habilidad]]
- [[naturaleza]]
- [[preset-rol]]
