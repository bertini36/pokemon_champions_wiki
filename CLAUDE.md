# Pokemon Champions Wiki System — Rules for Claude

## Purpose
This wiki is a competitive Pokémon knowledge base for **Pokémon Champions** (Nintendo Switch). Goal: build VGC tournament teams for both **singles** and **doubles** formats.

- Domain: VGC competitive battling (team building, matchup analysis, meta trends, move/ability/item synergies, role archetypes).
- Data source: op.gg/es/pokemon-champions/* (pokédex, moves, abilities, items, types) + curated build pages.
- Meta usage data: pokemon-zone.com/champions/pokemon/ (ranked usage rates, top Pokémon by usage). See `raw/meta/_source.md` for ingestion instructions.
- Lifecycle: raw/ ingested incrementally as the game evolves and the meta shifts. Re-ingestion is expected; pipelines are idempotent.
- Optimize wiki structure for: team composition, threat coverage, speed tiers, role coverage (sweeper/setter/pivot/support), and core/synergy detection.

## Language
- **Always answer in Spanish.**
- Use the **Spanish (Spain) names** from the Spanish version of the game for Pokémon, moves, abilities, items, and types (e.g. *Charizard* → *Charizard*, *Thunderbolt* → *Rayo*, *Intimidate* → *Intimidación*, *Choice Scarf* → *Pañuelo Elegido*, *Leftovers* → *Restos*).
- English slugs are kept in frontmatter / file paths only for cross-referencing op.gg; never surface them in answers.
- Mechanic terms (VGC, sweeper, pivot, setter, lead, switch, spread, BST) may stay in English when standard in the competitive community.

## Structure
- `raw/` → raw sources. Claude does NOT edit here.
- `wiki/` → processed knowledge. Claude writes and updates here.
- `wiki/index.md` → master index. Read ALWAYS before searching.
- `wiki/sources/` (8) → páginas resumen por fuente externa.
- `wiki/concepts/` (18) → mecánicas, ítems y análisis derivado (damage matrix, threat list, defensive cores, etc.).
- `wiki/entities/` → 18 tipos en root + subcarpetas:
  - `pokemon/` (265 + `_index.md`)
  - `ataques/` (919 + `_index.md`)
  - `habilidades/` (309 + `_index.md`)
  - `objetos/` (138 + `_index.md`)
- `wiki/synthesis/` (3) → cross-cutting (flujo construcción equipo, items vs meta clásico, cobertura vs tipos defensivos).
- `log.md` → history. Write after each structural operation.

Total wiki: 1683 ficheros .md.

## Writing conventions
- File names: lowercase with hyphens (`concept-name.md`)
- Dates: `YYYY-MM-DD` format
- All internal links with `[[double brackets]]`
- Each file ends with a `## 🔗 Related` section with links to connected pages
- Mandatory frontmatter in each file:
  ```yaml
  ---
  title: Concept name
  date: YYYY-MM-DD
  type: concept | entity | source | synthesis
  tags: [tag1, tag2]
  ---
  ```

## How to navigate the wiki (to avoid burning tokens)
1. Read `wiki/index.md` → identify relevant pages by category.
2. For an individual Pokémon / ataque / habilidad / objeto: resolve the slug directly under `wiki/entities/<categoria>/<slug>.md`. The `_index.md` of each subcarpeta lista todos los slugs disponibles.
3. For mecánicas o análisis derivado: leer `wiki/concepts/<concept>.md`.
4. For cross-domain answers: consultar `wiki/synthesis/`.
5. Read only the necessary pages, not the entire vault.
6. Never read files from `raw/` except during re-ingestion.

## Ingestion process

### Bulk entities (pokemon / ataques / habilidades / objetos)

Las entidades individuales se generan masivamente desde `raw/` con:

```bash
python3 scripts/build_wiki_entities.py
```

El script es **idempotente** y sobreescribe `wiki/entities/{pokemon,ataques,habilidades,objetos}/<slug>.md` con frontmatter (title, date, type=entity, tags, slug), body con `[[wikilinks]]` inyectados a tipos canónicos en celdas de tabla y sección `## 🔗 Related` cross-referenciando sources/concepts. También regenera `_index.md` por categoría.

Re-ejecutar tras cualquier cambio en `raw/{pokemon,ataques,habilidades,objetos}/`.

### Spine + síntesis (sources, concepts, synthesis)

Para sources, concepts y synthesis se sigue el flujo manual one-at-a-time:

1. Process sources **one at a time**, in order. Do not batch.
2. For each source: read in full, extract key concepts/entities/ideas, then create or update pages in `wiki/concepts/`, `wiki/sources/`, `wiki/synthesis/`.
3. Add bidirectional `[[]]` links between every related pair.
4. Update `wiki/index.md` with the new pages, placed under the right category.
5. Append `INGEST` entry to `log.md`.
6. Do NOT delete files from `raw/` after processing them.

## Query process
1. Read `wiki/index.md` first; identify candidate pages.
2. Read only relevant pages; follow `[[]]` outward only when needed.
3. Answer with citations to the pages used.
4. If the answer produces a non-trivial new connection, file it back as a `wiki/synthesis/` page and link bidirectionally.
5. Append `QUERY` entry to `log.md`.

## Meta analysis process

1. Read `raw/meta/_source.md` to understand the data source and ingestion format.
2. Ingest the latest usage snapshot from pokemon-zone.com into `raw/meta/usage-YYYY-MM-DD.md`.
3. Cross-reference the top Pokémon against `raw/calculos/damage-matrix.md` and `raw/calculos/threat-list.md`.
4. Create or update `wiki/concepts/meta-actual.md` with the current tier list and usage rates.
5. If counter-strategy analysis is requested, create `wiki/synthesis/counter-meta-YYYY-MM-DD.md` with: top threats, recommended counters, and suggested cores.
6. Append `INGEST` entry to `log.md`.

## Maintenance process (linting)
1. Orphan pages (no incoming links).
2. Missing cross-references and bidirectional gaps.
3. Contradictions between pages.
4. Outdated information.
5. Duplicate pages → consolidate.
6. Data gaps (thin content) → flag for further ingestion.
7. Index sync.
8. Append `LINT` entry to `log.md`.
