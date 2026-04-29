# Ataques — Fuente

Datos extraídos de op.gg Pokémon Champions Moves.

- URL: https://op.gg/es/pokemon-champions/moves
- Detalle por ataque: https://op.gg/es/pokemon-champions/moves/<slug>
- Total ataques: 919

## Cómo descargar los datos

La página renderiza todas las cards de ataques como `<a href="/es/pokemon-champions/moves/<slug>">` directamente en el DOM (sin virtualización). Cada card contiene nombre en español, tipo, categoría, potencia, precisión, PP y descripción.

### 1. Abrir la página y harvestear todas las cards

Navega a https://op.gg/es/pokemon-champions/moves y, en la consola del navegador, ejecuta:

```js
const cards = Array.from(document.querySelectorAll('a[href*="/moves/"]'))
  .filter(a => a.querySelector('h3'));

const seen = new Set();
const items = [];
for (const a of cards) {
  const slug = a.getAttribute('href').split('/').pop();
  if (seen.has(slug)) continue;
  seen.add(slug);

  const headerRow = a.querySelector('div.flex.items-center.justify-between');
  const type = headerRow?.querySelector('span')?.textContent.trim() || '';
  const metaRow = a.querySelectorAll('div.flex.flex-wrap')[0];
  const metaSpans = Array.from(metaRow?.children || []).map(s => s.textContent.trim());
  const get = (idx, prefix) => {
    const s = metaSpans[idx] || '';
    return s.replace(new RegExp('^' + prefix + ':\\s*'), '').replace(/^—$/, '-');
  };

  items.push({
    slug,
    name: a.querySelector('h3')?.textContent.trim(),
    type,
    category: metaSpans[0] || '',     // Físico / Especial / Estado
    power:    get(1, 'Poder'),
    accuracy: get(2, 'Prec'),
    pp:       get(3, 'PP'),
    desc:     a.querySelector('p')?.textContent.trim() || '',
  });
}

copy(JSON.stringify(items, null, 2));
console.log('ataques:', items.length);  // 919
```

Pega el contenido en `scripts/moves_data.json`.

### 2. Estructura de cada entrada

```json
{
  "slug": "close-combat",
  "name": "A Bocajarro",
  "type": "Lucha",
  "category": "Físico",
  "power": "120",
  "accuracy": "100%",
  "pp": "8",
  "desc": "Lucha abiertamente contra el objetivo sin protegerse. También reduce la Defensa y la Defensa Especial del usuario."
}
```

```json
{
  "slug": "worry-seed",
  "name": "Abatidoras",
  "type": "Planta",
  "category": "Estado",
  "power": "-",
  "accuracy": "100%",
  "pp": "12",
  "desc": "Planta una semilla en el objetivo que le causa pesar..."
}
```

- `category` es uno de `Físico`, `Especial` o `Estado`
- `power`, `accuracy` son `-` para movimientos sin valor numérico (ej. estados)
- `pp` es el PP actualizado de Pokémon Champions (puede diferir del PP histórico de gens anteriores)

### 3. Generar markdown raw/ataques/<slug>.md

`scripts/sync_ataques.py` cubre dos casos en una sola pasada idempotente:

- **Enriquecer existentes** → añade row `Op.gg` (URL) y row `PP (op.gg)` cuando el PP difiere del raw
- **Crear faltantes** → produce un `.md` por ataque presente en op.gg pero no en raw, con tabla Datos y sección Efecto

Formato actual de cada `<slug>.md`:

```markdown
# A Bocajarro

## Datos

| Propiedad | Valor |
|---|---|
| Tipo | Lucha |
| Categoría | Físico |
| Potencia | 120 |
| Precisión | 100 |
| PP | 5 |
| Slug | close-combat |
| Op.gg | [close-combat](https://op.gg/es/pokemon-champions/moves/close-combat) |
| PP (op.gg) | 8 |

## Efecto

Lucha abiertamente contra el objetivo sin protegerse...

## Pokémon que lo aprenden

Total: 30
| 1 | Palafin |
...
```

### 4. Convención filename

Slug en español slugificado sin acentos. Para colisiones de nombre, fallback al slug en inglés.

| op.gg slug | name | filename |
|---|---|---|
| `close-combat` | A Bocajarro | `a-bocajarro.md` |
| `aeroblast` | Aerochorro | `aerochorro.md` |
| `worry-seed` | Abatidoras | `abatidoras.md` |
| `helping-hand` | Refuerzo | `refuerzo.md` |
| `flare-blitz` | Envite Ígneo | `envite-igneo.md` |

## Notas

- Power y Accuracy raw vs op.gg coinciden 1:1 en los 655 originales.
- PP discrepa en 246 casos: raw conserva PP legacy (gens anteriores), op.gg refleja PP actual de Pokémon Champions. Ambos valores se preservan en el markdown (`PP` y `PP (op.gg)`).
- Los nuevos ataques creados (264) llegan con `Pokémon que lo aprenden | Total: 0`. La lista se rellena cuando un Pokémon de `raw/pokemon/` añada el ataque a sus Movimientos.
- Las descripciones de ataques recientes (Z-Moves, Max Moves de tutoriales, gimmicks Gen 9) pueden venir en inglés desde op.gg.
