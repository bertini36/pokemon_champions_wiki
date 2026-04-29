---
title: Defensive Core
date: 2026-04-29
type: concept
tags: [analisis, defensa, core, sinergia]
---

# Defensive Core

## Definition

Pares de Pokémon disponibles ranqueados por **score defensivo conjunto**:

```
score = |resistencias compartidas|
      + |inmunidades del par|
      - 2 * |debilidades compartidas|
```

- **Score alto** → los dos miembros se complementan: cubren las debilidades del otro y comparten muchas resistencias / inmunidades.
- **Score bajo (negativo)** → comparten debilidades = mal core defensivo.

Generado por `scripts/build_defensive_cores.py`.

## Why it matters

Construir un equipo VGC empieza por elegir el **doble pivot** sólido. Un core defensivo top reduce el espacio de equipo restante: solo necesitas 4 picks ofensivos / situacionales en lugar de 4 picks que también tengan que tapar agujeros.

El opuesto, **anti-cores** (score muy negativo), señalan combinaciones que la matriz de tipos castiga: dos Pokémon que comparten debilidades se mueren al mismo SE.

## Heurística de construcción

1. Top cores → escoger el par base
2. [[threat-list]] del par → identificar amenazas que aún les dañan
3. Picks 3-6 → atacantes que neutralicen esas amenazas + utilidades

## Connections

Cruza [[op-gg-pokedex]] (tipos por Pokémon) con [[op-gg-types]] (eficacia). Aporta input a flujos como [[counter-meta]]. Las habilidades defensivas reales (Intimidación, Multiescamas, absorbedoras de tipo, Pararrayos) las modela `damage-matrix.py` extendida pero **no entran en el score** — extender si se quiere ranking más fiel.

## Sources

- `raw/calculos/defensive-cores.md` (116 líneas)

## 🔗 Related

- [[op-gg-types]]
- [[threat-list]]
- [[damage-matrix]]
- [[counter-meta]]
