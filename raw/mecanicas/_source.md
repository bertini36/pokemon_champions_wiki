# Mecánicas — Fuente

Datos extraídos del bundle JS de la calculadora oficial de op.gg para Pokémon Champions.

- URL calculadora: https://op.gg/es/pokemon-champions/calculator
- Bundle JS: `app-router/_next/static/chunks/app/[lang]/pokemon-champions/calculator/page-*.js`
- Tamaño: ~46 KB minificado

Esta calculadora reproduce la lógica interna del juego para stats y daño. Es la fuente más fiable disponible mientras Game Freak no publique las fórmulas oficiales.

## Cómo extraer los datos del bundle

### 1. Localizar el bundle activo

```js
// En consola del navegador, tras cargar la calculadora
const scripts = performance.getEntriesByType('resource')
  .filter(r => r.name.includes('calculator/page-') && r.name.endsWith('.js'))
  .map(r => r.name);
console.log(scripts);
```

El bundle cambia de hash con cada despliegue, pero el path siempre incluye `calculator/page-*.js`.

### 2. Descargar el bundle

```bash
curl -sSL "https://s-stats-platform-cdn.op.gg/app-router/_next/static/chunks/app/%5Blang%5D/pokemon-champions/calculator/page-<HASH>.js" \
  -o /tmp/calc_bundle.js
```

### 3. Patrones a buscar

| Patrón | Qué contiene |
|---|---|
| `LEVEL:50,IV:31,MAX_TOTAL_AP:66,MAX_STAT_AP:32,AP_TO_EV_RATIO:7.875` | Constantes globales |
| `function T(e,s,t,a){return Math.floor(...)` | Fórmula stat genérica |
| `function E(e,s,t)` | Fórmula stats completas (HP + 5 stats) |
| `b="physical"===i.category` | Inicio de fórmula de daño |
| `let N=[{key:"hardy"` | Lista 25 naturalezas |
| `let d={adaptability:` | 21 habilidades modeladas |
| `m=new Set(["bullet-punch"` | Sets de moves por categoría (puños, mordiscos, pulso, retroceso, secondary-effect, contacto) |
| `{label:"Sweeper",points:` | 4 presets oficiales de spread PH |

### 4. Re-extracción

Cuando op.gg actualice el bundle:

1. Verificar que las constantes (`LEVEL`, `IV`, `AP_TO_EV_RATIO`, caps) siguen iguales
2. Ver si añaden nuevas habilidades a `let d={...}` (compararlas con `raw/mecanicas/habilidades-calc.md`)
3. Ver si modifican sets de moves por categoría
4. Confirmar que la fórmula de daño no cambia constantes (`2*S/5+2`, `/50`, `+2`, `0.85`)

## Ficheros generados a partir de este bundle

- `formula-stats.md` — Fórmula stats Nv.50
- `formula-dano.md` — Fórmula daño + roll + gaps no modelados
- `naturalezas.md` — 25 naturalezas con clave EN, nombre ES, ±stat
- `presets-rol.md` — 4 spreads oficiales (Sweeper / Physical / Tank / SpD Tank)
- `habilidades-calc.md` — 21 habilidades modeladas + 6 sets de moves por categoría

## Notas

- La calculadora **no modela** objetos, clima, terreno, críticos, multi-hit, multi-target, burn, boost stages ni los 16 valores de roll Gen-style. Usa rango simple 0.85 → 1.00 (ver `formula-dano.md`, sección Gaps).
- IV es **fijo en 31** para todos los Pokémon: simplificación oficial de Pokémon Champions vs juegos clásicos.
- AP (Ability Points en interno op.gg = PH Puntos de Habilidad en UI ES) se convierte a EV equivalente vía factor `7.875`. 32 PH ≈ 252 EV de juegos clásicos.
