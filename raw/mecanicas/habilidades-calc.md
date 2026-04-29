# Habilidades Modeladas en Calculadora — Pokémon Champions

21 habilidades que op.gg/calculator implementa con efecto medible en daño. Resto de habilidades del juego (>300 totales) existen pero no se reflejan en cálculo de daño.

Fuente: bundle JS `let d={adaptability:{...}, technician:{...}, ...}`.

## Tabla resumen

| Clave EN | Tipo | Modificador | Condición |
|---|---|---|---|
| `adaptability`  | STAB    | × 2.0 (en vez de 1.5) | Move STAB |
| `technician`    | Power   | × 1.5 | `move.power ≤ 60` |
| `iron-fist`     | Power   | × 1.2 | Movimiento de **puño** |
| `strong-jaw`    | Power   | × 1.5 | Movimiento de **mordisco** |
| `mega-launcher` | Power   | × 1.5 | Movimiento de **pulso/aura** |
| `reckless`      | Power   | × 1.2 | Movimiento de **retroceso** |
| `sheer-force`   | Power   | × 1.3 | Movimiento con **efecto secundario** (efecto se elimina) |
| `tough-claws`   | Power   | × 1.3 | Movimiento de **contacto** |
| `huge-power`    | Atk stat | × 2.0 | Siempre |
| `pure-power`    | Atk stat | × 2.0 | Siempre |
| `hustle`        | Atk stat | × 1.5 | Siempre (precisión reducida — no modelada) |
| `gorilla-tactics` | Atk stat | × 1.5 | Siempre (locked en 1 movimiento — no modelado) |
| `tinted-lens`   | Effectiveness | × 2.0 a NVE | Move es Poco Eficaz (× 0.5) |
| `filter`        | Effectiveness | × 0.75 a SE | Defensor recibe Súper Eficaz |
| `solid-rock`    | Effectiveness | × 0.75 a SE | Defensor recibe Súper Eficaz |
| `prism-armor`   | Effectiveness | × 0.75 a SE | Defensor recibe Súper Eficaz |
| `blaze`         | Power   | × 1.5 | Move tipo `fire` (HP bajo — no modelado, op.gg aplica siempre) |
| `torrent`       | Power   | × 1.5 | Move tipo `water` (HP bajo — no modelado) |
| `overgrow`      | Power   | × 1.5 | Move tipo `grass` (HP bajo — no modelado) |
| `swarm`         | Power   | × 1.5 | Move tipo `bug` (HP bajo — no modelado) |

**Nota crítica**: las habilidades de pinch (`blaze`/`torrent`/`overgrow`/`swarm`) op.gg las activa **siempre**, no a HP ≤ 1/3 como dicta el juego. Hay que descartar este modificador o filtrar manualmente para uso real.

## Sets de movimientos por categoría

### Puños (`iron-fist`, set `m`)

```
bullet-punch, comet-punch, dizzy-punch, drain-punch, dynamic-punch,
fire-punch, focus-punch, hammer-arm, ice-punch, mach-punch,
mega-punch, meteor-mash, power-up-punch, shadow-punch, sky-uppercut,
thunder-punch
```

Total: 16 movimientos.

### Mordiscos (`strong-jaw`, set `p`)

```
bite, crunch, fire-fang, fishious-rend, hyper-fang, ice-fang,
jaw-lock, poison-fang, psychic-fangs, thunder-fang
```

Total: 10 movimientos.

### Pulso / Aura (`mega-launcher`, set `x`)

```
aura-sphere, dark-pulse, dragon-pulse, heal-pulse, origin-pulse,
water-pulse
```

Total: 6 movimientos.

### Retroceso (`reckless`, set `u`)

```
brave-bird, double-edge, flare-blitz, head-charge, head-smash,
high-jump-kick, jump-kick, submission, take-down, volt-tackle,
wild-charge, wood-hammer
```

Total: 12 movimientos.

### Efecto secundario (`sheer-force`, set `f`)

```
air-slash, blizzard, body-slam, discharge, dragon-breath, fire-blast,
flamethrower, ice-beam, iron-head, play-rough, psychic, rock-slide,
scald, shadow-ball, sludge-bomb, thunderbolt, zen-headbutt
```

Total: 17 movimientos.

### Contacto (`tough-claws`, set `h`)

```
aqua-jet, body-slam, brave-bird, close-combat, crunch, double-edge,
dragon-claw, drain-punch, earthquake, extreme-speed, flare-blitz,
fly, giga-impact, ice-punch, iron-head, iron-tail, knock-off,
leaf-blade, outrage, play-rough, poison-jab, quick-attack, return,
shadow-claw, superpower, u-turn, volt-tackle, waterfall, wild-charge,
x-scissor, zen-headbutt
```

Total: 31 movimientos.

## JSON estructurado de habilidades

```json
{
  "adaptability":   {"type": "stab",          "value": 2.0,  "condition": "stab"},
  "technician":     {"type": "power",         "value": 1.5,  "condition": "power_lte_60"},
  "iron-fist":      {"type": "power",         "value": 1.2,  "condition": "punch_set"},
  "strong-jaw":     {"type": "power",         "value": 1.5,  "condition": "bite_set"},
  "mega-launcher":  {"type": "power",         "value": 1.5,  "condition": "pulse_set"},
  "reckless":       {"type": "power",         "value": 1.2,  "condition": "recoil_set"},
  "sheer-force":    {"type": "power",         "value": 1.3,  "condition": "secondary_effect_set"},
  "tough-claws":    {"type": "power",         "value": 1.3,  "condition": "contact_set"},
  "huge-power":     {"type": "atk_mult",      "value": 2.0,  "condition": "always"},
  "pure-power":     {"type": "atk_mult",      "value": 2.0,  "condition": "always"},
  "hustle":         {"type": "atk_mult",      "value": 1.5,  "condition": "always"},
  "gorilla-tactics":{"type": "atk_mult",      "value": 1.5,  "condition": "always"},
  "tinted-lens":    {"type": "nve_boost",     "value": 2.0,  "condition": "move_is_nve"},
  "filter":         {"type": "se_reduction",  "value": 0.75, "condition": "incoming_se"},
  "solid-rock":     {"type": "se_reduction",  "value": 0.75, "condition": "incoming_se"},
  "prism-armor":    {"type": "se_reduction",  "value": 0.75, "condition": "incoming_se"},
  "blaze":          {"type": "type_power",    "value": 1.5,  "condition": "type_fire"},
  "torrent":        {"type": "type_power",    "value": 1.5,  "condition": "type_water"},
  "overgrow":       {"type": "type_power",    "value": 1.5,  "condition": "type_grass"},
  "swarm":          {"type": "type_power",    "value": 1.5,  "condition": "type_bug"}
}
```

## Habilidades NO modeladas (pero relevantes para VGC)

La calculadora ignora muchas habilidades con impacto real. Lista parcial de las más críticas:

| Habilidad | Efecto omitido |
|---|---|
| **Intimidación** | -1 Atk al enemigo en switch-in |
| **Llamarada / Aguamanto / Absorbe Agua / Pararrayos** | Inmunidad y boost a tipos específicos |
| **Multiescamas / Coraza Multi** | × 0.5 daño a HP completo |
| **Magic Bounce / Manto Bueno** | Refleja status |
| **Desafiante / Trauma** | Anti-stat-drop, anti-debilitar |
| **Fuerza Bruta** | × 1.3 a moves contacto pero ignora secundarios |
| **Mojigato** | Inmune a status moves |
| **Garganta Acorazada** | Inmune a sound moves |
| **Cuerpo Puro / Especie Pura** | Inmune a stat drops |

Para uso VGC serio, extender el modelo de `damage_calc` con al menos: Intimidación, Multiescamas, absorbedoras de tipo, Cuerpo Puro.

## Notas

- Los **set names** (`m`, `p`, `x`, `u`, `f`, `h`) son arbitrarios del bundle — usamos los descriptivos en castellano.
- `blaze`/`torrent`/`overgrow`/`swarm` se activan **siempre** en op.gg (bug o simplificación). En el juego real solo a HP ≤ 1/3.
- `prism-armor` aparece como `prism_armor` en el bundle (con underscore) pero su `key` interno es `prism-armor`.
- Las habilidades con efectos en otros stats (`hustle` baja precisión, `gorilla-tactics` lockea move) tienen modelado parcial: solo el bonus, no el costo.
- Cuando construyamos `scripts/build_damage_matrix.py`, esta tabla es la fuente de verdad para los 21 modificadores activables.
