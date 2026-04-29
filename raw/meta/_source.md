---
title: Fuente de uso del meta — pokemon-zone.com
date: 2026-04-29
type: source
tags: [meta, usage, pokemon-zone, tier-list]
---

# Fuente de uso del meta

**URL:** https://www.pokemon-zone.com/champions/pokemon/

## Qué contiene

Ranking de Pokémon más usados en partidas rankeadas de Pokémon Champions. Incluye:

- Tasa de uso (%) por Pokémon
- Posición en el ranking global

## Para qué sirve

1. **Identificar el meta actual:** los Pokémon con mayor uso son los que más vas a encontrarte en partidas rankeadas.
2. **Construir contra-estrategias:** saber quién domina el meta permite elegir Pokémon, movimientos, objetos y cores que los contraresten.
3. **Validar picks propios:** si tu equipo incluye un Pokémon del top, tiene más respaldo estadístico de que es viable.

## Proceso de ingestión

1. Navegar a https://www.pokemon-zone.com/champions/pokemon/
2. Copiar el listado de Pokémon ordenado por uso (mínimo top 30).
3. Crear o actualizar `raw/meta/usage-YYYY-MM-DD.md` con la tabla de uso.
4. Ingestar hacia `wiki/concepts/meta-actual.md` siguiendo el proceso estándar.
5. Cruzar contra `raw/calculos/damage-matrix.md` y `raw/calculos/threat-list.md` para generar `wiki/synthesis/counter-meta-YYYY-MM-DD.md`.

## Formato esperado del archivo de uso

```markdown
---
title: Uso del meta — YYYY-MM-DD
date: YYYY-MM-DD
type: source
tags: [meta, usage, snapshot]
---

| Rank | Pokémon | Uso (%) |
|------|---------|---------|
| 1    | Nombre  | XX.X%   |
| ...  | ...     | ...     |
```

## Frecuencia de actualización

El meta de Pokémon Champions cambia con cada parche. Re-ingestar cuando:
- Hay un parche de balance.
- Han pasado más de 2 semanas desde el último snapshot.
- El usuario detecta un desfase entre el meta documentado y el que encuentra en partidas.

## 🔗 Related

- [[wiki/concepts/meta-actual]]
- [[wiki/synthesis/counter-meta]]
- [[raw/calculos/threat-list.md]]
- [[raw/calculos/damage-matrix.md]]
- [[raw/calculos/defensive-cores.md]]
