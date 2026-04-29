# Objetos con Efecto en Daño — Pokémon Champions

Subconjunto de `raw/objetos/` que afectan al cálculo de daño. La calculadora oficial op.gg **NO modela ninguno** de estos objetos. Tabla diseñada para alimentar `scripts/build_damage_matrix.py`.

Categorías:
- **Type Booster** (×1.2): 18 ítems, uno por tipo
- **Stat Modifier**: Pañuelo Elección (Spe), Bola Luminosa (Pikachu)
- **Cinturón Maestro / Vidas / Bandas / Gafas Elección**: NO existen en Pokémon Champions
- **Bayas tipo**: 17 bayas que reducen ×0.5 un golpe SE de un tipo concreto

## Type Boosters (×1.2 al tipo correspondiente)

Todos van en categoría "Objetos para Sostener". Multiplicador de power × 1.2.

| Nombre ES | Slug EN | Tipo afectado |
|---|---|---|
| Carbón | `charcoal` | Fuego |
| Agua Mística | `mystic-water` | Agua |
| Semilla Milagro | `miracle-seed` | Planta |
| Imán | `magnet` | Eléctrico |
| Antiderretir | `never-melt-ice` | Hielo |
| Cinturón Negro | `black-belt` | Lucha |
| Flecha Venenosa | `poison-barb` | Veneno |
| Arena Fina | `soft-sand` | Tierra |
| Pico Afilado | `sharp-beak` | Volador |
| Cuchara Torcida | `twisted-spoon` | Psíquico |
| Polvo Plata | `silver-powder` | Bicho |
| Piedra Dura | `hard-stone` | Roca |
| Hechizo | `spell-tag` | Fantasma |
| Colmillo Dragón | `dragon-fang` | Dragón |
| Gafas de Sol | `black-glasses` | Siniestro |
| Revest. Metálico | `metal-coat` | Acero |
| Fairy Feather | `fairy-feather` | Hada |
| Pañuelo de Seda | `silk-scarf` | Normal |

Cobertura: **18 / 18 tipos**.

## Stat Modifiers

| Objeto | Slug | Efecto | Coste |
|---|---|---|---|
| **Pañuelo Elección** | `choice-scarf` | Spe × 1.5 (lockea en 1 movimiento) | Beginning |
| **Bola Luminosa** | `light-ball` | Atk × 2, SpA × 2 (solo **Pikachu**) | varía |

## Survival / Utility (sin efecto en cálculo de daño emitido)

Útiles para análisis "¿sobrevive?" pero no cambian damage roll:

| Objeto | Slug | Efecto |
|---|---|---|
| Cinta Focus | `focus-band` | 10% chance sobrevive a 1 PS (no garantizado) |
| Banda Focus | `focus-sash` | Sobrevive a 1 PS si HP=máx (1 vez) |
| Restos | `leftovers` | +1/16 HP por turno |
| Cascabel Concha | `shell-bell` | Recupera 1/8 del daño infligido |
| Periscopio | `scope-lens` | +1 stage crit ratio |
| Roca del Rey | `kings-rock` | +chance flinch |
| Garra Rápida | `quick-claw` | 20% chance prioridad +1 |
| Polvo Brillo | `bright-powder` | -10% precisión enemiga |
| Hierba Blanca | `white-herb` | Reset stat drops (1 vez) |
| Hierba Mental | `mental-herb` | Cura status mental (1 vez) |

## Bayas tipo (resistencia a SE)

Reducen × 0.5 el primer hit super-eficaz del tipo concreto. Se consumen al activarse.

| Baya | Slug EN | Tipo que resiste |
|---|---|---|
| Baya Anjiro | `chople-berry` | Lucha |
| Baya Bariba | `babiri-berry` | Acero |
| Baya Caoca | `kasib-berry` | Fantasma |
| Baya Caquic | `kebia-berry` | Veneno |
| Baya Chilan | `chilan-berry` | Normal |
| Baya Dillo | `passho-berry` | Agua |
| Baya Drasi | `roseli-berry` | Hada |
| Baya Gualot | `tanga-berry` | Bicho |
| Baya Hibis | `occa-berry` | Fuego |
| Baya Kebia | `payapa-berry` | Psíquico |
| Baya Kouba | `kebia-berry` | (verificar — colisión nombre) |
| Baya Meloc | `wacan-berry` | Eléctrico |
| Baya Pasio | `coba-berry` | Volador |
| Baya Payapa | `chilan-berry` | (verificar — colisión nombre) |
| Baya Pomaro | `colbur-berry` | Siniestro |
| Baya Rimoya | `yache-berry` | Hielo |
| Baya Tamar | `charti-berry` | Roca |
| Baya Yecana | `haban-berry` | Dragón |
| Baya Zanama | `shuca-berry` | Tierra |
| Baya Zidra | `rindo-berry` | Planta |

Cobertura: **18 / 18 tipos** (con un par de slugs ES por confirmar mapping exacto).

Otras bayas comunes (no resistencia tipo):
- `sitrus-berry` (Baya Aranja) — recupera 25% HP a HP ≤ 50%
- `lum-berry` (Baya Atania) — cura cualquier status
- `salac-berry` (Baya Caoca?) — +1 Spe a HP ≤ 25%
- `liechi-berry` — +1 Atk a HP ≤ 25%
- `petaya-berry` — +1 SpA a HP ≤ 25%

Para damage matrix solo importa el modificador × 0.5 SE.

## Items NO presentes en Pokémon Champions

Items clásicos de mainline que NO están en `raw/objetos/`:

| Item clásico | Efecto que falta |
|---|---|
| **Choice Band** | Atk × 1.5 (lock) |
| **Choice Specs** | SpA × 1.5 (lock) |
| **Life Orb** | × 1.3 daño + 10% HP self-damage |
| **Expert Belt** | × 1.2 a movimientos SE |
| **Assault Vest** | SpD × 1.5 (no status moves) |
| **Wise Glasses** | SpA-moves × 1.1 |
| **Muscle Band** | Atk-moves × 1.1 |
| **Throat Spray** | +1 SpA al usar sound move |
| **Eviolite** | Def × 1.5, SpD × 1.5 a no-evolved |
| **Heavy Duty Boots** | inmune a hazards |

**Implicación VGC**: el meta de Pokémon Champions favorece **type boosters fijos × 1.2** (sin lock-in) frente al "all-in" de Choice items de mainline. Cambia profundamente la teoría de equipos. Los Atacantes especiales sin Gafas/Pañuelo Especialista deben confiar en SpA inflada vía Modesta + 32 PH SpA + type booster ×1.2.

## JSON estructurado (para `damage_matrix.py`)

```json
{
  "type_boosters": {
    "charcoal":      {"name_es": "Carbón",           "type": "fire",     "mult": 1.2},
    "mystic-water":  {"name_es": "Agua Mística",     "type": "water",    "mult": 1.2},
    "miracle-seed":  {"name_es": "Semilla Milagro",  "type": "grass",    "mult": 1.2},
    "magnet":        {"name_es": "Imán",             "type": "electric", "mult": 1.2},
    "never-melt-ice":{"name_es": "Antiderretir",     "type": "ice",      "mult": 1.2},
    "black-belt":    {"name_es": "Cinturón Negro",   "type": "fighting", "mult": 1.2},
    "poison-barb":   {"name_es": "Flecha Venenosa",  "type": "poison",   "mult": 1.2},
    "soft-sand":     {"name_es": "Arena Fina",       "type": "ground",   "mult": 1.2},
    "sharp-beak":    {"name_es": "Pico Afilado",     "type": "flying",   "mult": 1.2},
    "twisted-spoon": {"name_es": "Cuchara Torcida",  "type": "psychic",  "mult": 1.2},
    "silver-powder": {"name_es": "Polvo Plata",      "type": "bug",      "mult": 1.2},
    "hard-stone":    {"name_es": "Piedra Dura",      "type": "rock",     "mult": 1.2},
    "spell-tag":     {"name_es": "Hechizo",          "type": "ghost",    "mult": 1.2},
    "dragon-fang":   {"name_es": "Colmillo Dragón",  "type": "dragon",   "mult": 1.2},
    "black-glasses": {"name_es": "Gafas de Sol",     "type": "dark",     "mult": 1.2},
    "metal-coat":    {"name_es": "Revest. Metálico", "type": "steel",    "mult": 1.2},
    "fairy-feather": {"name_es": "Fairy Feather",    "type": "fairy",    "mult": 1.2},
    "silk-scarf":    {"name_es": "Pañuelo de Seda",  "type": "normal",   "mult": 1.2}
  },
  "stat_modifiers": {
    "choice-scarf":  {"name_es": "Pañuelo Elección", "spe_mult": 1.5, "locked": true},
    "light-ball":    {"name_es": "Bola Luminosa",    "atk_mult": 2.0, "spa_mult": 2.0, "only": "pikachu"}
  },
  "type_resist_berries": {
    "occa-berry":    {"name_es": "Baya Hibis",  "resist_type": "fire",     "mult": 0.5, "consumed": true},
    "passho-berry":  {"name_es": "Baya Dillo",  "resist_type": "water",    "mult": 0.5, "consumed": true},
    "wacan-berry":   {"name_es": "Baya Meloc",  "resist_type": "electric", "mult": 0.5, "consumed": true},
    "rindo-berry":   {"name_es": "Baya Zidra",  "resist_type": "grass",    "mult": 0.5, "consumed": true},
    "yache-berry":   {"name_es": "Baya Rimoya", "resist_type": "ice",      "mult": 0.5, "consumed": true},
    "chople-berry":  {"name_es": "Baya Anjiro", "resist_type": "fighting", "mult": 0.5, "consumed": true},
    "kebia-berry":   {"name_es": "Baya Caquic", "resist_type": "poison",   "mult": 0.5, "consumed": true},
    "shuca-berry":   {"name_es": "Baya Zanama", "resist_type": "ground",   "mult": 0.5, "consumed": true},
    "coba-berry":    {"name_es": "Baya Pasio",  "resist_type": "flying",   "mult": 0.5, "consumed": true},
    "payapa-berry":  {"name_es": "Baya Kebia",  "resist_type": "psychic",  "mult": 0.5, "consumed": true},
    "tanga-berry":   {"name_es": "Baya Gualot", "resist_type": "bug",      "mult": 0.5, "consumed": true},
    "charti-berry":  {"name_es": "Baya Tamar",  "resist_type": "rock",     "mult": 0.5, "consumed": true},
    "kasib-berry":   {"name_es": "Baya Caoca",  "resist_type": "ghost",    "mult": 0.5, "consumed": true},
    "haban-berry":   {"name_es": "Baya Yecana", "resist_type": "dragon",   "mult": 0.5, "consumed": true},
    "colbur-berry":  {"name_es": "Baya Pomaro", "resist_type": "dark",     "mult": 0.5, "consumed": true},
    "babiri-berry":  {"name_es": "Baya Bariba", "resist_type": "steel",    "mult": 0.5, "consumed": true},
    "roseli-berry":  {"name_es": "Baya Drasi",  "resist_type": "fairy",    "mult": 0.5, "consumed": true},
    "chilan-berry":  {"name_es": "Baya Chilan", "resist_type": "normal",   "mult": 0.5, "consumed": true}
  }
}
```

## Cómo se aplica al pipeline de daño

Extiende `formula-dano.md`:

```python
# Atacante con type booster
if item.type_booster and move.type == item.type_booster.type:
    atk_mods.powerModifier *= 1.2

# Atacante con Pañuelo Elección
if item.slug == "choice-scarf":
    attacker_speed *= 1.5  # solo afecta turn order, no daño directo

# Defensor con baya tipo y recibe SE
if (item.type_resist_berry and
    move.type == item.type_resist_berry.resist_type and
    type_effectiveness > 1):
    final *= 0.5
    item.consumed = True
```

## Notas

- Type Boosters apilan multiplicativamente con habilidades (`adaptability`, `iron-fist`, etc.) y STAB.
- `light-ball` solo activa con Pikachu como holder. Verificar en `pokemon.name == "Pikachu"`.
- Las bayas tipo **se gastan tras el primer SE recibido**: para análisis turn-1 sí cuentan, para 2HKO depende.
- En doubles, **Helping Hand** (no item) suma × 1.5 adicional. No modelado aquí.
- Nombres ES de bayas tienen alguna colisión potencial (Kebia/Caquic, Chilan/Payapa). Verificar mapping definitivo en re-extracción.
