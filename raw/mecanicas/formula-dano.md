# Fórmula de Daño — Pokémon Champions

Fuente: bundle JS de https://op.gg/es/pokemon-champions/calculator

Replica exacta de la lógica que op.gg ejecuta en el cliente al usar la "Calculadora de Daño".

## Pseudocódigo de referencia (extraído del bundle, formateado)

```js
// b = es físico (true) o especial (false)
let isPhysical = move.category === "physical";

let attack = isPhysical
    ? Math.floor(attacker.stats.attack    * attackerAbilityMods.attack)
    : Math.floor(attacker.stats.spAttack  * attackerAbilityMods.spAttack);

let defense = isPhysical
    ? Math.floor(defender.stats.defense   * defenderAbilityMods.defense)
    : Math.floor(defender.stats.spDefense * defenderAbilityMods.spDefense);

let baseDamage =
    Math.floor(
        Math.floor(2 * 50 / 5 + 2)                                   // = 22
      * Math.floor(move.power * attackerAbilityMods.powerModifier)
      * Math.floor(attack / defense)
      / 50
    ) + 2;

let stab          = attackerAbilityMods.stabModifier;     // 1.5 default, 2.0 si Adaptabilidad
let typeEffect    = typeChart(move.type, defender.types); // 0, 0.25, 0.5, 1, 2, 4
let abilityEffect = defenderAbilityMods.effectivenessModifier; // 0.75 si Filter/SolidRock/PrismArmor a SE

let final = baseDamage * typeEffect * abilityEffect * stab;

let minDamage = Math.floor(0.85 * final);
let maxDamage = Math.floor(final);
```

## Implementación en Python

```python
import math
from dataclasses import dataclass

LEVEL = 50

@dataclass
class Move:
    name: str
    type: str           # "fire", "water", ...
    category: str       # "physical" | "special" | "status"
    power: int

@dataclass
class AbilityMods:
    attack: float = 1.0
    spAttack: float = 1.0
    defense: float = 1.0
    spDefense: float = 1.0
    powerModifier: float = 1.0
    stabModifier: float = 1.5            # default 1.5; Adaptabilidad → 2.0
    effectivenessModifier: float = 1.0   # Filter/SolidRock/PrismArmor → 0.75 a SE

def calc_damage(
    attacker_stats: dict,
    defender_stats: dict,
    move: Move,
    type_effectiveness: float,
    is_stab: bool,
    atk_mods: AbilityMods,
    def_mods: AbilityMods,
) -> tuple[int, int]:
    if move.category == "status" or not move.power:
        return (0, 0)

    is_physical = move.category == "physical"

    attack = math.floor(
        attacker_stats["attack" if is_physical else "spAttack"]
        * (atk_mods.attack if is_physical else atk_mods.spAttack)
    )
    defense = math.floor(
        defender_stats["defense" if is_physical else "spDefense"]
        * (def_mods.defense if is_physical else def_mods.spDefense)
    )

    base = math.floor(
        math.floor(2 * LEVEL / 5 + 2)                            # 22
        * math.floor(move.power * atk_mods.powerModifier)
        * math.floor(attack / defense)
        / 50
    ) + 2

    stab = atk_mods.stabModifier if is_stab else 1.0
    final = base * type_effectiveness * def_mods.effectivenessModifier * stab

    min_dmg = math.floor(0.85 * final)
    max_dmg = math.floor(final)
    return (min_dmg, max_dmg)
```

## Cálculo de OHKO/2HKO

```python
def hits_to_ko(max_damage: int, defender_hp: int) -> int:
    if max_damage <= 0:
        return 0
    return math.ceil(defender_hp / max_damage)

# OHKO si hits_to_ko == 1
# 2HKO si hits_to_ko == 2
```

Para porcentajes:

```python
min_pct = min_damage / defender_hp * 100
max_pct = max_damage / defender_hp * 100
```

## Roll de daño

La calculadora **no implementa** los 16 valores de variación clásicos (`0.85, 0.86, ..., 1.00`). Usa solo extremos:

- `min = floor(0.85 * final)`
- `max = floor(final)`

Para reportes tipo "X% de OHKO" (probabilidad), tendríamos que extender con los 16 rolls. Mientras tanto, asumir distribución uniforme entre `min` y `max`.

## Modificadores activos en orden de aplicación

1. **Stat de ataque** del atacante × `abilityMods.attack` (o `spAttack`)
2. **Stat de defensa** del defensor × `abilityMods.defense` (o `spDefense`)
3. **Power** del movimiento × `attacker.powerModifier`
4. **Base damage** se calcula con valores ya modificados
5. **STAB** (Same Type Attack Bonus): 1.5 o 2.0 (Adaptabilidad), aplicado solo si el tipo del move coincide con tipos del atacante
6. **Type effectiveness** (chart de tipos)
7. **Ability defense modifier** del defensor: 0.75 si Filter/SolidRock/PrismArmor reciben SE; 2.0 si Tinted Lens (atacante) le pega NVE

## Tabla de modificadores STAB y efectividad

| Caso | Multiplicador |
|---|---|
| STAB normal | × 1.5 |
| Adaptabilidad | × 2.0 |
| Súper eficaz | × 2 (× 4 si dual SE) |
| Eficacia normal | × 1 |
| Poco eficaz | × 0.5 (× 0.25 si dual NVE) |
| Sin efecto | × 0 |
| Filter / Solid Rock / Prism Armor reciben SE | resultado × 0.75 |
| Tinted Lens pega NVE | resultado × 2 (sube a normal) |

## Gaps no modelados

La calculadora omite mecánicas que sí impactan combate real. Antes de tomar decisiones VGC con estas matrices, considerar:

| No modelado | Impacto típico |
|---|---|
| **Objetos** (Pañuelo, Especialista, Vidas, Restos…) | × 1.2 a × 1.5 daño, swing decisivo |
| **Clima** (sol, lluvia, arena, nieve) | × 1.5 a moves del clima, × 0.5 al opuesto |
| **Terreno** (eléctrico, psíquico, herbáceo, místico) | × 1.3 a moves del terreno + bloqueos |
| **Críticos** | × 1.5 daño (probabilidad 1/24) |
| **Multi-hit** (Roca Afilada, Triple Patada) | golpes 2-5 |
| **Spread reduction (doubles)** | × 0.75 a moves multi-target |
| **Burn** | × 0.5 atk físico |
| **Boost stages** (+1, +2 hasta +6) | × 1.5, × 2, ..., × 4 |
| **Helping Hand** | × 1.5 daño aliado |
| **Refleflejo / Pantalla de Luz** | × 0.5 (× 2/3 en doubles) |
| **Z-moves / Dynamax / Tera** | mecánicas gimmick por gen |
| **Roll 16 valores** | distribución más fina dentro [0.85, 1.0] |

Para uso VGC serio, extender la fórmula con al menos: **objetos**, **clima/terreno**, **críticos**, **boost stages**, **spread reduction**.

## Validación

Compara salidas Python con la UI de op.gg/calculator antes de generar matrices masivas:

```python
# Ejemplo: Charizard Modesto 32 SpA, Lanzallamas vs Venusaur sin AP
# move: flamethrower (power=90, special, fire)
# Charizard tipos = ["fire","flying"] → STAB
# Venusaur tipos = ["grass","poison"] → 4× SE (fuego dobla a planta y a planta tipo veneno? Solo planta)
#   En realidad: fire vs grass = 2x, fire vs poison = 1x → final 2x
```

## Notas

- El `Math.floor` se aplica en cada paso intermedio: orden de operaciones es crítico.
- `move.power * powerModifier` también va dentro de `Math.floor` antes de multiplicar.
- `attack/defense` se redondea **antes** de multiplicar por power.
- STAB y type effectiveness son multiplicadores `*` puros sin redondeo intermedio.
