# Pokémon — Fuente

Datos extraídos de op.gg Pokémon Champions Pokédex.

- URL: https://op.gg/es/pokemon-champions/pokedex
- Detalle por Pokémon: https://op.gg/es/pokemon-champions/pokedex/<slug>
- Total entradas: 258 (incluye Megas y formas regionales)

## Cómo descargar las fichas

La tabla de la web es virtualizada (sólo ~15 filas en DOM a la vez). El listado completo viaja en el payload de React Server Components inline en la página. Pasos:

### 1. Abrir la página y capturar el payload RSC

Navega a https://op.gg/es/pokemon-champions/pokedex y, en la consola del navegador (DevTools > Console), ejecuta:

```js
const scripts = Array.from(document.querySelectorAll('script'));
const big = scripts.find(s => !s.src && s.textContent.includes('venusaur'));

// Reejecuta el script interceptando self.__next_f.push para capturar el payload.
const captured = [];
const orig = self.__next_f.push;
self.__next_f.push = function(arg) { captured.push(arg); return arg; };
try { new Function('self', big.textContent)(self); } finally { self.__next_f.push = orig; }

let combined = '';
for (const c of captured) if (Array.isArray(c) && typeof c[1] === 'string') combined += c[1];

// Extrae el array `pokemon` por escaneo de corchetes balanceados.
const idx = combined.indexOf('"pokemon":[');
let i = idx + '"pokemon":'.length;
let depth = 0, end = -1;
for (; i < combined.length; i++) {
  if (combined[i] === '[') depth++;
  else if (combined[i] === ']') { depth--; if (depth === 0) { end = i; break; } }
}
const arr = combined.slice(idx + '"pokemon":'.length, end + 1);
copy(JSON.stringify(JSON.parse(arr), null, 2));   // copia al portapapeles
console.log('count:', JSON.parse(arr).length);    // 258
```

Pega el contenido en `scripts/pokedex_data.json`.

### 2. Estructura de cada entrada

```json
{
  "id": 6,
  "key": "charizard",
  "name": "Charizard",
  "generation": 1,
  "types": ["fire", "flying"],
  "abilities": ["blaze", "solar-power"],
  "stats": {"hp": 78, "attack": 84, "defense": 78,
            "spAttack": 109, "spDefense": 85, "speed": 100},
  "moves": ["mega-punch", "fire-punch", ...]
}
```

### 3. Generar markdown raw/pokemon/<slug>.md

Pipeline (ver `scripts/`):

- `gen_missing_pokemon.py` → genera `<slug>.md` para entradas presentes en `pokedex_data.json` y faltantes en `raw/pokemon/`. Traduce slugs de habilidades y movimientos al español usando `raw/habilidades/` y `raw/ataques/` como diccionario.
- `validate_pokemon.py` → cruza stats/tipos/BST/N.º Pokédex contra `pokedex_data.json`.
- `enrich_pokemon.py` → añade rows op.gg al Datos table (Slug en, Op.gg URL, Habilidades en, Total movimientos op.gg). Idempotente.

### 4. Convención de filenames

| op.gg key | filename |
|---|---|
| `charizard` | `charizard.md` |
| `mega-charizard-x` | `charizard-mega-x.md` |
| `mega-venusaur` | `venusaur-mega.md` |
| `raichu-alolan` | `raichu-de-alola.md` |
| `arcanine-hisui` | `arcanine-de-hisui.md` |
| `tauros-paldean` | `tauros-de-paldea.md` |
| `slowbro-galarian` | `slowbro-de-galar.md` |
| `mr.-rime` | `mr-rime.md` |

## Limitaciones

- Lycanroc (3 formas) y Rotom (5 formas) no diferenciados en op.gg; raw conserva las variantes locales mapeadas al base.
- Lista de Movimientos en español depende de cobertura de `raw/ataques/`. Slug inglés en fallback si no hay traducción.
