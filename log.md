# System Log

2026-04-26T23:39 INIT — wiki re-initialized; CLAUDE.md + wiki/index.md regenerated (wiki/ subdirs were empty; raw/ retained)

## 2026-04-26 — Initialization
- Wiki system initialized
- Folder structure created
- CLAUDE.md generated
- Master index created

## 2026-04-26 — Raw ingestion
- Source: op.gg Pokémon Champions (pokedex, moves, abilities, items, types) + curated VGC builds
- raw/pokemon/ — 265 entries (200 base + 65 missing/mega added) + _source.md
- raw/ataques/ — 919 moves (655 enriched + 264 created from op.gg) + _source.md
- raw/habilidades/ — 173 abilities + _source.md (op.gg lists 307; 134 gap pending)
- raw/objetos/ — 138 items: Sostener (30), Piedras Mega (60), Bayas (28), Misceláneos (20) + _source.md
- raw/tipos/ — 18 type pages (Atacando + Defendiendo tables) + _source.md
- raw/builds/ — 12 VGC build markdown files

## 2026-04-28 — Mecánicas (calculadora)
- Source: bundle JS de op.gg/es/pokemon-champions/calculator
- raw/mecanicas/ — 6 ficheros: _source.md, formula-stats.md, formula-dano.md, naturalezas.md, presets-rol.md, habilidades-calc.md
- Constantes extraídas: LEVEL=50, IV=31, MAX_TOTAL_AP=66, MAX_STAT_AP=32, AP_TO_EV_RATIO=7.875
- Naturalezas: 25 (5 neutrales + 20 stat-boosting) con clave EN, nombre ES, ±stat
- Presets oficiales: Sweeper, Physical, Tank, SpD Tank (32+32+2 PH cada uno)
- Habilidades modeladas: 21 con modificadores damage + 6 sets de moves por categoría (puños=16, mordiscos=10, pulso=6, retroceso=12, secondary=17, contacto=31)
- Gaps documentados: objetos, clima/terreno, críticos, multi-hit, spread reduction, burn, boost stages, roll 16-valores, intimidación, multiescamas
- scripts/build_speed_tiers.py — primer script de cálculo offline (265 Pokémon parseados, 15 disponibles tabulados)
- raw/calculos/ — speed-tiers-l50.json + speed-tiers-l50.md (4 escenarios PH/naturaleza)
- raw/mecanicas/objetos-calc.md — 18 type boosters (×1.2 todos los tipos), Pañuelo Elección, Bola Luminosa, 17 bayas tipo + items NO presentes en PC (Choice Band/Specs, Life Orb, Expert Belt...)
- scripts/build_damage_matrix.py — fórmula damage + items + tipos + STAB
- raw/calculos/damage-matrix.json + .md — 15×15 = 225 celdas (preset Sweeper/Physical vs Bulky 32 HP / 16 Def / 16 SpD), KO ranges + OHKO/2HKO labels
- README.md raíz creado con flujo update raw/ → scripts/ → wiki/ (modelado en abacum-io/engine-wiki)
- damage-matrix.py extendida con 14 habilidades modeladas (adaptability, blaze/torrent/overgrow/swarm, technician, huge-power/pure-power/hustle/gorilla-tactics, tinted-lens, filter/solid-rock/prism-armor); habilidad principal del Pokémon aplicada por defecto; columna "Habilidades" en tabla output
- scripts/build_speed_vs_scarf.py — análisis cruzado Spe optimizada vs Pañuelo Elección (×1.5); raw/calculos/speed-vs-scarf.json + .md con tier global + análisis por Pokémon (quién supera optimizada, quién supera con Pañuelo enemigo, quién supera con Pañuelo mutuo)
- scripts/build_coverage_matrix.py — para cada Pokémon disponible: tipos cubiertos SE, gaps, mejor move por tipo atacante
- scripts/build_threat_list.py — vista inversa de damage matrix; OHKOs/2HKOs por defensor; ranking vulnerabilidad
- damage-matrix.py extendido: columnas + Baya (×0.5 baya tipo SE) + Si quemado (×0.5 atk físico, advertencia colapso floor)
- scripts/build_spread_optimizer.py — PH HP/Def(SpD) mínimos para sobrevivir top 8 amenazas por defensor (con habilidades atacante aplicadas vía import calc_damage)


## 2026-04-29 — Wiki bulk entity ingest (1631 entities)

2026-04-29T23:35 INGEST — full bulk ingest of raw/{pokemon,ataques,habilidades,objetos}/ via scripts/build_wiki_entities.py.

- wiki/entities/pokemon/ — 265 fichas + _index
- wiki/entities/ataques/ — 919 moves + _index
- wiki/entities/habilidades/ — 309 abilities + _index
- wiki/entities/objetos/ — 138 items + _index
- Cada entidad lleva frontmatter (title, date, type=entity, tags, slug), body con [[wikilinks]] inyectados a tipos canónicos en celdas de tabla, y sección 🔗 Related con cross-refs a sources/concepts relevantes.
- Idempotente: re-ejecutar `python3 scripts/build_wiki_entities.py` sobreescribe.
- wiki/index.md actualizado: secciones de Pokémon/Ataques/Habilidades/Items apuntan a _index por categoría, no listan 1.6k entradas inline.
- Total wiki tras esta pasada: 1683 ficheros .md (45 spine + 18 tipos + 1631 entities + 4 _index + index.md).

## 2026-04-29 — Wiki spine ingest (sources + concepts + tipo entities + synthesis)

2026-04-29T22:55 INGEST — first wiki/ build pass: spine completed (concepts + tipo entities + 8 source pages + 3 synthesis). raw/ untouched.

- wiki/sources/ (8): op-gg-pokedex, op-gg-moves, op-gg-abilities, op-gg-items, op-gg-types, op-gg-calculator, builds-curated, pokemon-zone-meta
- wiki/concepts/ (16): ph-puntos-habilidad, formula-stats, formula-dano, naturaleza, preset-rol, habilidades-modeladas, type-booster, baya-tipo, panuelo-eleccion, speed-tier, damage-matrix, threat-list, coverage-matrix, defensive-core, spread-optimizer, scarf-candidate, meta-actual, counter-meta
- wiki/entities/ (18 tipos): normal, fuego, agua, electrico, planta, hielo, lucha, veneno, tierra, volador, psiquico, bicho, roca, fantasma, dragon, siniestro, acero, hada
- wiki/synthesis/ (3): flujo-construccion-equipo, items-vs-meta-clasico, cobertura-vs-tipos-defensivos
- wiki/index.md — regenerated with categorized sections (Mecánicas, Items, Análisis, Meta, Tipos, Sources, Synthesis)
- Pendiente bajo demanda: ingestar entidades individuales — 266 pokemon + 920 ataques + 309 habilidades + 138 objetos
- Total ficheros wiki creados: 45 + index regenerado

## 2026-04-29 — Habilidades defensivas + cores + scarf + builds + audit raw/ vs op.gg
- damage-matrix.py extendido con 14 habilidades defensivas (intimidate, multiscale, shadow-shield, type-immunity: water-absorb/volt-absorb/flash-fire/sap-sipper/levitate/lightning-rod/storm-drain/motor-drive/dry-skin, fluffy fire-vuln). 28 abilities totales modeladas
- scripts/build_defensive_cores.py — para cada par (A,B) de Pokémon disponibles: shared resists/immunities/weaknesses, score = resists + immunities − 2·shared_weak. Top cores ranked + anti-cores
- scripts/build_scarf_candidates.py — combina speed-vs-scarf + coverage-matrix + damage-matrix; score = spe_opt·0.05 + scarf_jump·4 + ohkos·6 + twohkos·2 + se_count·1.5; penalty −15 si ya outspeed sin Pañuelo
- raw/builds/_source.md — formato build documentado, conversión EV→PH (252 EV ≈ 32 PH), pipeline alta builds
- scripts/build_builds_summary.py — parser builds con cross-validation contra raw/pokemon/, raw/ataques/, raw/objetos/. Detectó 5 moves con nombres incorrectos
- raw/builds/ — 4 ficheros parcheados a nombres canónicos raw/ataques: Velocidad Extrema → Veloc. Extrema, Colmillo Roca → Roca Afilada (Garchomp), Ola de Calor → Onda Ígnea, Calor Foco → Onda Certera. Validación final 0 warnings
- **Audit completitud raw/ vs op.gg/es/pokemon-champions** (Pokédex 258, Moves 919, Items 138, Abilities 307):
  - raw/pokemon/ — 265 = 258 op.gg + 7 forms enriquecidas (Lycanroc 3, Rotom 6) → ✅ 100%
  - raw/ataques/ — 919/919 → ✅ 100%
  - raw/objetos/ — 138/138 → ✅ 100%
  - raw/habilidades/ — gap detectado: 173 originales vs 307 op.gg. Generadas 136 stubs nuevos vía chrome-devtools harvest del DOM (articles + h3 + p). Total final 309 = 307 + 2 extras Notion (`opportunist`, `toxic-debris`). ✅ 100%
  - Caso especial: `as-one-glastrier` y `as-one-spectrier` colisionan en slug español "Unidad Ecuestre"; filenames diferenciados con sufijo glastrier/spectrier
- raw/habilidades/_source.md actualizado con notas de cobertura y caso colisión

## 2026-05-01 — INGEST + QUERY

- INGEST: snapshot meta `raw/meta/usage-2026-04-30.md` (Reg M-A doubles, top 20). Fuentes: pikalytics + championslab + pokemon-zone (parcial).
- INGEST: actualizado `wiki/concepts/meta-actual.md` con tier list real.
- INGEST: creado `wiki/synthesis/counter-meta-2026-05-01.md` con counters por amenaza top 5.
- QUERY: equipo VGC doubles sorpresa. Output: `output/equipo-doubles-sombras-de-hisui.md` (v2 revisada con meta).
- HALLAZGO: campo `Disponible: Sí` en `wiki/entities/pokemon/*.md` está obsoleto (15 marcados, meta usa 207). Pendiente re-ejecutar `scripts/build_wiki_entities.py`.
- HALLAZGO: Megapiedras existen como ítems comprables (Tienda 2000 VP) pero todas las Mega-formas marcan `Disponible: -`. Probable obsolescencia del wiki vs meta real (Mega Garchomp 55.2% WR en torneo).

## 2026-05-01 — QUERY (revisión Mega)

- Usuario confirma que Megapiedras están activas en el juego. El campo `Disponible: -` del wiki para Mega-formas está obsoleto.
- QUERY: equipo v3 con Mega Garchomp + Tyranitar (sand archetype). Output actualizado en `output/equipo-doubles-sombras-de-hisui.md`.
- Decisión Plan B (Mega Garchomp + Tyranitar) sobre Plan A (Mega Charizard Y) por WR proven 55.2%.
- HALLAZGO: Sinistcha sale del equipo. Tyranitar entra como sand setter para activar Poder Arena de Mega Garchomp.

## 2026-05-01 — QUERY (v4 final)

- Reescrito equipo en v4: Mega Charizard Y + Sneasler + Z-Hisui Ilusión.
- Drop sand archetype (Tyranitar + Mega Garchomp). Solución: sin self-chip, sin friendly fire de Terremoto, contra-lluvia con Sequía.
- Output reescrito en castellano completo + explicación de cada objeto + chuleta paso a paso para novato.
- Output: `output/equipo-doubles-sombras-de-hisui.md`.
