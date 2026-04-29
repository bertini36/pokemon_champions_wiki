# Tipos — Fuente

Datos extraídos de op.gg Pokémon Champions Type Effectiveness.

- URL: https://op.gg/es/pokemon-champions/type-effectiveness
- Total tipos: 18 (Normal, Fuego, Agua, Eléctrico, Planta, Hielo, Lucha, Veneno, Tierra, Volador, Psíquico, Bicho, Roca, Fantasma, Dragón, Siniestro, Acero, Hada)

## Cómo descargar los datos

La página tiene una tabla de matriz 18x18 + un panel "Detalles del Tipo" que se actualiza al clicar cada pastilla. El panel muestra dos secciones por tipo: "Atacando con [TIPO]" y "Defendiendo como [TIPO]", cada una con tres niveles: 2x, 0.5x, 0x.

### 1. Abrir la página y harvestear los 18 paneles

Navega a https://op.gg/es/pokemon-champions/type-effectiveness y, en la consola del navegador, ejecuta:

```js
const TYPES_ES = ['Normal','Fuego','Agua','Eléctrico','Planta','Hielo',
                  'Lucha','Veneno','Tierra','Volador','Psíquico','Bicho',
                  'Roca','Fantasma','Dragón','Siniestro','Acero','Hada'];

const buttons = Array.from(document.querySelectorAll('button'))
  .filter(b => TYPES_ES.includes(b.textContent.trim()) && b.querySelector('img'));

const sleep = ms => new Promise(r => setTimeout(r, ms));
const result = {};

for (const btn of buttons) {
  const tipo = btn.textContent.trim();
  btn.click();
  await sleep(250);  // espera a que React re-renderice el panel

  const grid = document.querySelector('div.grid.gap-6.md\\:grid-cols-2');
  const [atkPanel, defPanel] = grid.children;

  const parsePanel = panel => {
    const groups = {'2x': [], '0.5x': [], '0x': []};
    for (const sec of panel.querySelectorAll('div.space-y-4 > div')) {
      const label = sec.querySelector('p')?.textContent || '';
      const key = /2x/.test(label) ? '2x'
                : /0\.5x/.test(label) ? '0.5x'
                : /0x/.test(label) ? '0x' : null;
      if (!key) continue;
      groups[key] = Array.from(sec.querySelectorAll('span.capitalize'))
        .map(s => s.textContent.trim()).filter(Boolean);
    }
    return groups;
  };

  result[tipo] = {atk: parsePanel(atkPanel), def: parsePanel(defPanel)};
}

copy(JSON.stringify(result, null, 2));
console.log('tipos:', Object.keys(result).length);  // 18
```

Pega el contenido en `scripts/tipos_data.json`.

### 2. Estructura de cada entrada

```json
{
  "Fuego": {
    "atk": {
      "2x":   ["Planta", "Hielo", "Bicho", "Acero"],
      "0.5x": ["Fuego", "Agua", "Roca", "Dragón"],
      "0x":   []
    },
    "def": {
      "2x":   ["Agua", "Tierra", "Roca"],
      "0.5x": ["Fuego", "Planta", "Hielo", "Bicho", "Acero", "Hada"],
      "0x":   []
    }
  }
}
```

- `atk` = al atacar con TIPO → multiplicador contra defensores de los tipos listados
- `def` = al defender como TIPO → multiplicador contra ataques de los tipos listados

### 3. Generar markdown raw/tipos/<slug>.md

`scripts/gen_tipos.py` lee `scripts/tipos_data.json` y produce un `.md` por tipo con dos tablas: "Atacando con [TIPO]" y "Defendiendo como [TIPO]". Cada tipo enlazado con `[[wikilink]]`. Slug en español sin acentos.

| Tipo | filename |
|---|---|
| Eléctrico | `electrico.md` |
| Psíquico | `psiquico.md` |
| Dragón | `dragon.md` |

## Notas

- Los multiplicadores 0x sólo aparecen cuando hay inmunidad (ej. Fantasma vs Normal en `atk`, Tierra vs Eléctrico en `def`).
- La matriz de la tabla principal es derivable a partir de las 18 entradas atk → def, así que no se duplica.
