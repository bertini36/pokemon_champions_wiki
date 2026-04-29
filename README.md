# 🎮 pokemon-master-brain

> 🏆 Base de conocimiento VGC persistente para **Pokémon Champions** (Nintendo).

El meta competitivo de Pokémon Champions va evolucionando con cada actualización:
nuevos Pokémon, nuevos objetos, nuevos resultados de torneos. Leer datos en
crudo desde op.gg cada vez es lento y ruidoso. Esta wiki cubre ese hueco:
una única fuente de verdad para **stats, movesets, habilidades, objetos,
matchups de tipo, fórmula de daño, speed tiers y síntesis de team-building**.

🧪 Construida siguiendo el [método de wiki personal de Andrej
Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
un vault de Obsidian curado por LLM donde las fuentes en crudo se ingestan
en páginas de conocimiento enlazadas y consultables por agentes. El [skill
`wiki-karpathy`](.claude/skills/wiki-karpathy/SKILL.md) dirige la ingestión
y el mantenimiento.

## 🚀 Cómo usarlo

```bash
git clone <repo-url> ~/pokemon_champions_brain
cd ~/pokemon_champions_brain
```

Abre el vault con [Obsidian](https://obsidian.md) para navegación humana, o
con Claude Code para consultas agentificadas.

Para actualizarlo:

```bash
git pull
```

## 📦 Qué vive aquí

Conocimiento curado y destilado en tres capas:

```
raw/                    Datos crudos extraídos de op.gg (Claude NO edita)
├── pokemon/            265 fichas de Pokémon (stats, tipos, habilidades, movepool)
├── ataques/            919 movimientos (tipo, categoría, potencia, PP, descripción)
├── habilidades/        309 habilidades del juego
├── objetos/            138 objetos (Sostener, Megas, Bayas, Misc)
├── tipos/              18 fichas de tipo (Atacando + Defendiendo)
├── builds/             Builds VGC curadas
├── mecanicas/          Fórmulas
└── calculos/           Tablas precomputadas (speed tiers, damage matrix)

wiki/                   Conocimiento procesado (Claude escribe aquí)
├── index.md            Índice maestro categorizado (leer SIEMPRE primero)
├── sources/            8 páginas: pokédex, ataques, habilidades, objetos, tipos y calculadora de op.gg + builds + uso de pokemon-zone
├── concepts/           18 conceptos: PH, fórmulas, naturaleza, preset, habilidades-modeladas,
│                       type-booster, baya-tipo, panuelo-eleccion, speed-tier,
│                       damage/threat/coverage matrix, defensive-core,
│                       spread-optimizer, scarf-candidate, meta-actual, counter-meta
├── entities/
│   ├── (raíz)          18 tipos canónicos (Normal..Hada) con tablas atacando/defendiendo
│   ├── pokemon/        265 fichas individuales (metadatos YAML + tipos enlazados con [[ ]])
│   ├── ataques/        919 ataques con tipo enlazado con [[ ]] + Pokémon que lo aprenden
│   ├── habilidades/    309 habilidades con descripción + categoría + nivel
│   ├── objetos/        138 objetos con enlace a [[type-booster]]/[[baya-tipo]]/[[panuelo-eleccion]]
│   └── _index.md       Índice por categoría dentro de cada subcarpeta
└── synthesis/          3 páginas: flujo-construccion-equipo + items-vs-meta-clasico + cobertura-vs-tipos-defensivos

Total wiki: 1683 archivos .md.

scripts/                Pipelines idempotentes Python
├── build_speed_tiers.py        # Tabla velocidades Nv.50 (4 escenarios PH/naturaleza)
├── build_damage_matrix.py      # Matriz daño 15×15 (con habilidades, objetos, bayas, quemado)
├── build_speed_vs_scarf.py     # Spe optimizada vs Pañuelo Elección
├── build_coverage_matrix.py    # Cobertura ofensiva por Pokémon
├── build_threat_list.py        # Vista inversa: amenazas por defensor
├── build_spread_optimizer.py   # PH HP/Def mínimos para sobrevivir top amenazas
├── build_defensive_cores.py    # Pares de Pokémon con sinergia defensiva
├── build_scarf_candidates.py   # Ranking candidatos a Pañuelo Elección
├── build_builds_summary.py     # Índice de raw/builds/ con cross-validation
└── build_wiki_entities.py      # Genera wiki/entities/{pokemon,ataques,habilidades,objetos}/ desde raw/

CLAUDE.md               Reglas operativas de Claude (lenguaje ES, navegación, ingestión)
log.md                  Historial INGEST / QUERY / LINT
README.md               Este fichero
```

Cada subdirectorio bajo `raw/` contiene un `_source.md` con la **receta exacta
de extracción** desde op.gg (URL + snippet de consola navegador + esquema de
salida). Esto hace el pipeline reproducible cuando el meta cambie.

## 👥 Dos audiencias

### 1. 🧑‍💻 Constructor VGC humano
Camino rápido desde una pregunta competitiva ("¿qué resiste a Greninja
Pañuelo?", "¿quién supera 169 Spe?") hasta una respuesta con fuente
verificable.

### 2. 🤖 Agente de Claude
Consume la wiki **antes** de razonar. Flujo:

1. Leer `wiki/index.md` (categorizado: Mecánicas, Objetos, Análisis, Meta, Tipos, Fuentes, Síntesis).
2. Resolver entidades por enlace `[[ ]]`: `[[charizard]]`, `[[a-bocajarro]]`, `[[intimidacion]]`, `[[restos]]`.
3. Cruzar contra páginas de `wiki/concepts/` cuando la consulta toca mecánicas (PH, fórmulas, niveles de velocidad, matriz de daño).
4. Las páginas de `wiki/synthesis/` resuelven preguntas inter-dominio (flujo de construcción de equipo, objetos vs meta clásico, cobertura vs tipos defensivos).

`raw/` solo se lee en re-ingestión, nunca para responder consultas. Las entidades wiki ya llevan metadatos YAML + enlaces `[[ ]]` inyectados.

## 🧠 Skill `pokemon-champions-brain` — consultas dirigidas

El repo incluye un skill en
[`.claude/skills/pokemon-champions-brain/SKILL.md`](.claude/skills/pokemon-champions-brain/SKILL.md)
que se activa **solo** cuando preguntas algo específico de Pokémon Champions
VGC. Evita que Claude use memoria genérica de juegos clásicos y le obliga a
leer `raw/` y `raw/calculos/` antes de responder.

**Cuándo se dispara:**
- Invocación explícita: *"contesta X usando Pokemon Champion Brain"*, *"consulta el brain"*, *"según el wiki"*
- Team building: *"ayúdame a montar un equipo competitivo basado en Garchomp"*, *"qué core defensivo va con Corviknight"*
- Análisis competitivo: *"build de Charizard para VGC"*, *"qué resiste a Greninja"*, *"quién supera 169 Spe"*

**Cuándo NO se dispara:**
- Trivia genérica de Pokémon (anime, lore, Pokédex sin contexto competitivo)
- Mecánicas de juegos clásicos (Gen 1-9) sin enmarcar como comparación con PC
- Preguntas no Pokémon

El skill enrutará la pregunta al fichero `raw/calculos/*.md` correcto en lugar
de derivar de memoria, citando siempre las fuentes consultadas.

## 🔄 Cómo actualizar `raw/` cuando el meta cambie

Cuando se añadan Pokémon, ítems, movimientos o se ajuste stats, sigue
estos pasos. **Cada subdirectorio bajo `raw/` tiene su propia receta** en su
`_source.md`.

### 1. 📥 Re-extraer datos desde op.gg

Abre Claude Code en este repo y lánzale uno de estos prompts:

> **Pokédex:** Re-extrae `raw/pokemon/` siguiendo `raw/pokemon/_source.md`.
> Detecta entradas nuevas vs lo ya existente. Para cada Pokémon nuevo crea su
> `.md`. Para los existentes con stats/movepool actualizados, enriquece sin
> sobrescribir secciones manuales.

> **Movimientos:** Re-extrae `raw/ataques/` siguiendo `raw/ataques/_source.md`.
> Compara con el dataset actual. Crea movimientos nuevos. Actualiza PP y
> descripciones que hayan cambiado.

> **Habilidades:** Re-extrae `raw/habilidades/` siguiendo
> `raw/habilidades/_source.md`. Mismo patrón: nuevas + actualizadas.

> **Objetos:** Re-extrae `raw/objetos/` siguiendo `raw/objetos/_source.md`.

> **Tipos:** Re-extrae `raw/tipos/` siguiendo `raw/tipos/_source.md` (raro que
> cambien, pero por si acaso).

> **Mecánicas / Calculadora:** Re-extrae `raw/mecanicas/` siguiendo
> `raw/mecanicas/_source.md`. Verifica que las constantes (`LEVEL=50`,
> `IV=31`, `MAX_TOTAL_AP=66`, `MAX_STAT_AP=32`, `AP_TO_EV_RATIO=7.875`) no
> hayan cambiado. Verifica habilidades y presets de rol.

Cada `_source.md` documenta:
- URL exacta de op.gg
- Snippet de consola navegador para descargar JSON
- Esquema de cada entrada
- Convención de filenames
- Notas de casos límite (entradas en inglés sin traducir, formas regionales, etc.)

### 2. 🧮 Re-ejecutar scripts de cálculo

Después de cualquier cambio en `raw/pokemon/`, `raw/ataques/`, `raw/tipos/`
o `raw/mecanicas/`, ejecutar el pipeline en orden de dependencias:

```bash
python3 scripts/build_speed_tiers.py        # base
python3 scripts/build_damage_matrix.py      # base
python3 scripts/build_speed_vs_scarf.py     # depende de speed-tiers
python3 scripts/build_coverage_matrix.py    # depende de damage-matrix
python3 scripts/build_threat_list.py        # depende de damage-matrix
python3 scripts/build_spread_optimizer.py   # depende de damage-matrix
python3 scripts/build_defensive_cores.py    # base (tipos)
python3 scripts/build_scarf_candidates.py   # depende de speed-vs-scarf + coverage + damage
python3 scripts/build_builds_summary.py     # depende de raw/builds/
```

Salidas regeneradas en `raw/calculos/`:
- `speed-tiers-l50.{json,md}`
- `damage-matrix.{json,md}`
- `speed-vs-scarf.{json,md}`
- `coverage-matrix.{json,md}`
- `threat-list.{json,md}`
- `spread-optimizer.{json,md}`
- `defensive-cores.{json,md}`
- `scarf-candidates.{json,md}`
- `builds-summary.{json,md}`

Los scripts son **idempotentes**: re-ejecutar sin cambios produce diff vacío.

### 3. 🧹 Regenerar wiki/entities/ + mantenimiento

Una vez `raw/` está actualizado, regenerar las 1631 fichas wiki de pokémon/ataques/habilidades/objetos:

```bash
python3 scripts/build_wiki_entities.py
```

Idempotente: lee `raw/{pokemon,ataques,habilidades,objetos}/` y sobreescribe `wiki/entities/{pokemon,ataques,habilidades,objetos}/<slug>.md` con metadatos YAML + cuerpo con enlaces `[[ ]]` inyectados a tipos canónicos + sección de enlaces relacionados. También regenera `_index.md` por categoría.

Después, para refrescar el esqueleto + mantenimiento:

> Hacer mantenimiento del wiki.

El skill [`wiki-karpathy`](.claude/skills/wiki-karpathy/SKILL.md):

- Refresca páginas del esqueleto en `wiki/sources/`, `wiki/concepts/`, `wiki/synthesis/` cuando una fuente cambia significativamente.
- Revisa huérfanos, contradicciones, duplicados, lagunas de datos.
- Sincroniza `wiki/index.md`.
- Añade `INGEST` / `LINT` a `log.md`.

Crea una confirmación (o PR) con el resultado.

## 🛠️ Herramientas

- 🟣 **[Obsidian](https://obsidian.md)** — navegación humana (vista de grafo, enlaces inversos, búsqueda por etiqueta)
- 🤖 **[Claude Code](https://docs.anthropic.com/claude-code)** — ingestión, consultas, mantenimiento
- 🧠 **[skill wiki-karpathy](.claude/skills/wiki-karpathy/SKILL.md)** — flujo de ingestión Karpathy
- 🎯 **[skill pokemon-champions-brain](.claude/skills/pokemon-champions-brain/SKILL.md)** — motor de consultas para preguntas VGC dirigidas
- 🌐 **[Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)** — extracción asistida desde op.gg
- 🐍 **Python 3.10+** — scripts de cálculo (sin dependencias externas)
- 📊 **[op.gg/es/pokemon-champions/*](https://op.gg/es/pokemon-champions)** — fuente de datos primaria

## 📊 Estado actual del corpus

### raw/ (fuentes inmutables)

| Recurso | Cantidad | Cobertura op.gg |
|---|---|---|
| Pokémon | 265 (15 disponibles en juego actual) | 100% (258 op.gg + 7 formas enriquecidas) |
| Ataques | 919 | 100% catálogo |
| Habilidades | 309 | 100% (307 op.gg + 2 extras de Notion) |
| Objetos | 138 | 100% |
| Tipos | 18 | 100% |
| Mecánicas (calculadora) | 6 documentos | constantes + fórmula + naturalezas + presets + 28 habilidades modeladas + 18 potenciadores de tipo + 17 bayas tipo |
| Builds VGC curadas | 12 | manual (sin fuente op.gg) |
| Capturas de uso del meta | 0 | pendiente primera ingesta desde pokemon-zone.com |
| Niveles de velocidad Nv.50 | 4 escenarios × 265 Pokémon | precomputado |
| Matriz de daño | 15 × 15 = 225 celdas | atacantes disponibles contra defensores disponibles, con habilidades + objetos + bayas + estado quemado |
| Núcleos defensivos | 105 pares | clasificación + anti-núcleos |
| Candidatos a Pañuelo | 15 ranqueados | puntuación combinada de Velocidad + cobertura + daño |

### wiki/ (procesado por Claude)

| Capa | Páginas | Contenido |
|---|---|---|
| `wiki/sources/` | 8 | pokédex, ataques, habilidades, objetos, tipos y calculadora de op.gg + builds + uso de pokemon-zone |
| `wiki/concepts/` | 18 | mecánicas + análisis derivado (PH, fórmulas, naturaleza, preset, habilidades modeladas, potenciador de tipo, baya, Pañuelo, niveles de velocidad, matriz de daño/amenazas/cobertura, núcleo defensivo, optimizador de spread, candidato a Pañuelo, meta actual, contra-meta) |
| `wiki/entities/` (raíz) | 18 | tipos canónicos con tablas atacando/defendiendo y enlaces `[[ ]]` cruzados |
| `wiki/entities/pokemon/` | 265 + _index | fichas individuales con metadatos YAML (slug, etiquetas, generación) + tipos enlazados con `[[ ]]` |
| `wiki/entities/ataques/` | 919 + _index | ataques con tipo enlazado con `[[ ]]` y Pokémon que lo aprenden |
| `wiki/entities/habilidades/` | 309 + _index | habilidades con descripción + categoría + nivel |
| `wiki/entities/objetos/` | 138 + _index | objetos con enlace a [[type-booster]]/[[baya-tipo]]/[[panuelo-eleccion]] |
| `wiki/synthesis/` | 3 | flujo-construccion-equipo, items-vs-meta-clasico, cobertura-vs-tipos-defensivos |
| **Total wiki** | **1683** | índice maestro + esqueleto + entidades + síntesis |

---
