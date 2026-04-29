# Habilidades — Fuente

Datos extraídos de op.gg Pokémon Champions Abilities.

- URL: https://op.gg/es/pokemon-champions/abilities
- Detalle por habilidad: https://op.gg/es/pokemon-champions/abilities/<slug>
- Total habilidades: 307

## Cómo descargar los datos

La página renderiza todas las cards de habilidades como `<a href="/es/pokemon-champions/abilities/<slug>">` directamente en el DOM (sin virtualización). Cada card contiene nombre en español, descripción y contador de Pokémon que la portan.

### 1. Abrir la página y harvestear todas las cards

Navega a https://op.gg/es/pokemon-champions/abilities y, en la consola del navegador, ejecuta:

```js
const cards = Array.from(document.querySelectorAll('a[href*="/abilities/"]'))
  .filter(a => a.querySelector('h3'));

const seen = new Set();
const items = [];
for (const a of cards) {
  const slug = a.getAttribute('href').split('/').pop();
  if (seen.has(slug)) continue;
  seen.add(slug);
  items.push({
    slug,
    name: a.querySelector('h3')?.textContent.trim(),
    desc: a.querySelector('p')?.textContent.trim() || '',
    pokemonCount: a.querySelector('span')?.textContent.trim() || '',
  });
}

copy(JSON.stringify(items, null, 2));
console.log('habilidades:', items.length);  // 307
```

Pega el contenido en `scripts/habilidades_data.json`.

### 2. Estructura de cada entrada

```json
{
  "slug": "intimidate",
  "name": "Intimidación",
  "desc": "Reduce el Ataque del rival al entrar en combate.",
  "pokemonCount": "12 Pokémon"
}
```

```json
{
  "slug": "drought",
  "name": "Sequía",
  "desc": "Activa el sol al entrar en combate durante 5 turnos.",
  "pokemonCount": "3 Pokémon"
}
```

- `slug` = identificador inglés (PokéAPI compatible)
- `name` = nombre en español tal como aparece en op.gg
- `desc` = descripción corta. Algunas habilidades aún están en inglés (no traducidas en op.gg)
- `pokemonCount` = nº de Pokémon del juego que tienen esta habilidad

### 3. Generar markdown raw/habilidades/<slug>.md

Pipeline (ver `scripts/`):

- `gen_habilidades.py` (a crear si se quiere regenerar todo) → produce un `.md` por habilidad. Filename = slug en español sin acentos.

Formato actual de cada `<slug>.md`:

```markdown
# Intimidación

**Categoría:** General
**Tier:** Alta
**API ID:** `intimidate`

## Descripción

Reduce el Ataque del rival al entrar en combate.
```

Los campos `Categoría` y `Tier` no vienen de op.gg. Se preservan los valores que ya existen en `raw/habilidades/` (proceden de la ingesta original desde Notion). Para nuevas habilidades sin metadata previa, dejar `-`.

### 4. Convención filename

Slug en español sin acentos:

| op.gg slug | name | filename |
|---|---|---|
| `intimidate` | Intimidación | `intimidacion.md` |
| `drought` | Sequía | `sequia.md` |
| `prankster` | Bromista | `bromista.md` |
| `mirror-armor` | Coraza Reflejo | `coraza-reflejo.md` |
| `beads-of-ruin` | Abalorio Debacle | `abalorio-debacle.md` |

## Notas

- `raw/habilidades/` contiene **309 habilidades** (.md) = 307 op.gg + 2 extras del Notion original (`opportunist`, `toxic-debris`) que op.gg no lista pero existen en el ecosistema Pokémon. Cobertura op.gg: **100%** (307/307).
- Las 136 habilidades añadidas en 2026-04-29 (gap original 173 → 309) tienen `Categoría: -` y `Tier: -` por no tener metadata previa. Las 173 originales conservan su `Categoría`/`Tier` de la ingesta Notion.
- Algunas descripciones en op.gg siguen en inglés (ej. "Lowers Sp.Def of all other Pokemon" para Abalorio Debacle). Conservar tal cual hasta traducción manual.
- El campo `API ID` enlaza con PokéAPI: `https://pokeapi.co/api/v2/ability/<slug>` para descripciones más completas.
- Caso especial colisión slug-ES: **Unidad Ecuestre** existe como dos habilidades distintas (`as-one-glastrier`, `as-one-spectrier`) con el mismo nombre español. Filenames diferenciados: `unidad-ecuestre-glastrier.md` y `unidad-ecuestre-spectrier.md`.
