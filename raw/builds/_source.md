# Builds — Fuente

Builds VGC curadas manualmente (no extraídas automáticamente de op.gg).

- Formato actual: VGC 2026 (Pokémon Champions launch meta)
- Lifecycle: actualización manual cuando aparezcan nuevas builds tier-1 en torneos / streams / comunidades

## Estructura de cada build

```markdown
# <Pokémon> — <Rol/Concepto>

## Datos

| Propiedad | Valor |
|---|---|
| Pokémon | <Nombre ES> |
| Formato | VGC 2026 |
| Objeto | <Item ES> |
| Naturaleza | <Naturaleza ES> |
| EVs | <PS - Atk - Def - SpA - SpD - Spe en formato legacy> |
| IVs | <31 / 31 / 31 / 31 / 31 / 31> |

## Movimientos

| # | Movimiento |
|---|---|
| 1 | <Move ES> |
| 2 | <Move ES> |
| 3 | <Move ES> |
| 4 | <Move ES> |

## Compañeros recomendados

<Texto libre con sinergias>

## Estrategia

HABILIDAD: <Habilidad ES>

TIPS:
- <Punto táctico>
- ...
```

## Notas sobre EVs vs PH

Las builds usan **EVs legacy** (252 max/stat, 510 total) en lugar de **PH de Pokémon Champions** (32 max/stat, 66 total). Conversión:

```
PH = floor(EV / 7.875)

252 EV  ≈  32 PH   (cap por stat)
128 EV  ≈  16 PH
60 EV   ≈   7 PH
4 EV    ≈   0 PH   (granularidad mínima ≈ 4 EV)
```

Total PH disponibles (66) = 252 + 252 + 12 EVs ≈ 32 + 32 + 2 PH.

Las builds existentes son **directamente convertibles** porque ya respetan el cap funcional de Pokémon Champions.

## Cómo añadir una build nueva

1. Verifica que el Pokémon está en `raw/pokemon/` (si no, ingestar primero)
2. Verifica que objeto, habilidad, naturaleza y movimientos existan en sus respectivos `raw/`
3. Crea `raw/builds/<pokemon>-<concepto>.md` siguiendo plantilla
4. Re-ejecuta `scripts/build_builds_summary.py` para regenerar el índice

## Cómo verificar consistencia con datos del juego

`scripts/build_builds_summary.py` valida que:
- El Pokémon de la build existe en `raw/pokemon/`
- Cada movimiento existe en `raw/ataques/`
- El objeto existe en `raw/objetos/`
- La habilidad declarada en HABILIDAD: pertenece al Pokémon

Si alguna referencia falta, se reporta como warning en el output.

## Builds actuales

Ver `raw/calculos/builds-summary.md` para el índice generado (creado por
`scripts/build_builds_summary.py`).

## Notas de formato

- Acentos ausentes en TIPS (no usar) por ser legacy. Aceptable. Re-extraer si se reescribe.
- Algunos movimientos llevan glosa en inglés entre paréntesis: `Triturar (Crunch)` — aceptable, sirve para mapping op.gg.
- Sección **Compañeros recomendados** es texto libre, no estructurado.
