# Objetos — Fuente

Datos extraídos de op.gg Pokémon Champions Items.

- URL: https://op.gg/es/pokemon-champions/items
- Detalle por objeto: https://op.gg/es/pokemon-champions/items/<slug>
- Total objetos: 138

## Categorías

- Objetos para Sostener (30)
- Piedras Mega (60)
- Bayas (28)
- Misceláneos (20)

## Cómo descargar los datos

La página renderiza todas las cards de objetos como `<a href="/es/pokemon-champions/items/<slug>">` directamente en el DOM (sin virtualización). Cada card contiene nombre, categoría, descripción y tags de obtención (Shop, VP, Beginning, Achievements, etc.).

### 1. Abrir la página y harvestear todas las cards

Navega a https://op.gg/es/pokemon-champions/items y, en la consola del navegador, ejecuta:

```js
const cards = Array.from(document.querySelectorAll('a[href*="/items/"]'))
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
    cat:  a.querySelector('h3 + span')?.textContent.trim() || '',
    desc: a.querySelector('p')?.textContent.trim() || '',
    tags: Array.from(a.querySelectorAll('div.mt-1 span'))
            .map(s => s.textContent.trim())
  });
}

copy(JSON.stringify(items, null, 2));
console.log('objetos:', items.length);  // 138
```

Pega el contenido en `scripts/objetos_data.json`.

### 2. Estructura de cada entrada

```json
{
  "slug": "leftovers",
  "name": "Restos",
  "cat":  "Objetos para Sostener",
  "desc": "Este objeto restaura gradualmente durante el combate los PS del Pokémon que lo lleva.",
  "tags": ["Beginning"]
}
```

```json
{
  "slug": "charizardite-y",
  "name": "Charizardita Y",
  "cat":  "Piedras Mega",
  "desc": "Una de las misteriosas Megapiedras. Permite megaevolucionar a Charizard en combate.",
  "tags": ["Shop", "2000 VP"]
}
```

`tags` puede ser:
- `["Shop", "<N> VP"]` → comprable en tienda al precio indicado
- `["Beginning"]` → entregado al inicio
- `["Mega Evolution Tutorial"]` → recompensa del tutorial
- `["Achievements"]` → desbloqueable por logros
- `["Deposit <Pokémon> from Pokemon Legends: Z-A"]` → vinculación con otro juego

### 3. Generar markdown raw/objetos/<slug>.md

`scripts/gen_objetos.py` lee `scripts/objetos_data.json` y produce un `.md` por objeto con tabla Datos (Categoría, Slug, Fuente, Coste) y sección Descripción. Filename en español slugificado sin acentos.

| op.gg slug | filename |
|---|---|
| `leftovers` | `restos.md` |
| `charizardite-y` | `charizardita-y.md` |
| `yache-berry` | `baya-rimoya.md` |
| `bug-type-affinity-ticket` | `bug-type-affinity-ticket.md` |

## Notas

- Items con descripción en inglés (sin traducir aún en op.gg) se conservan tal cual: principalmente Megas Gen 9 (Glimmoraita, Scovillainite) y todos los Type Affinity Tickets.
- El campo `Coste` se separa de `Fuente` cuando los tags llegan en formato `["Shop", "<N> VP"]`. Para tags únicos se rellena `Coste | -`.
