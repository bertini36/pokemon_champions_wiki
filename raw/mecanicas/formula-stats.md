# Fórmula de Stats — Pokémon Champions

Fuente: bundle JS de https://op.gg/es/pokemon-champions/calculator

## Constantes

```
LEVEL            = 50      # Nivel fijo en todos los combates
IV               = 31      # Valor individual fijo para todos los Pokémon
MAX_TOTAL_AP     = 66      # PH (Puntos de Habilidad) totales por Pokémon
MAX_STAT_AP      = 32      # PH máximos por stat individual
AP_TO_EV_RATIO   = 7.875   # 1 PH = 7.875 EV equivalentes
```

## Diferencias vs juegos clásicos

| Aspecto | Gen 1-9 | Pokémon Champions |
|---|---|---|
| Nivel | 1–100 | **50 fijo** |
| IVs | 0–31 por stat (variables) | **31 fijo** todas las stats |
| EVs | 252 máx/stat, 510 total | **PH: 32 máx/stat, 66 total** |
| Naturalezas | 25, ±10% | 25, ±10% (igual) |
| Stats finales | Variables por nivel | Calculadas siempre a Nv.50 |

Los EVs equivalentes de los 32 PH máximos son `floor(32 * 7.875) = 252`, exactamente el cap clásico.

## Fórmula HP

```python
def calc_hp(base_hp: int, ap_hp: int) -> int:
    ev = math.floor(ap_hp * 7.875)
    return math.floor((2 * base_hp + 31 + math.floor(ev / 4)) * 50 / 100) + 50 + 10
```

El `+50 + 10` agrupa el bonus por nivel (50) y el bonus fijo de HP (10).

## Fórmula resto de stats (Atk, Def, SpA, SpD, Spe)

```python
def calc_stat(base: int, ap: int, nature_inc: str | None,
              nature_dec: str | None, stat_name: str) -> int:
    ev = math.floor(ap * 7.875)
    raw = math.floor((2 * base + 31 + math.floor(ev / 4)) * 50 / 100) + 5

    if nature_inc == stat_name:
        mult = 1.1
    elif nature_dec == stat_name:
        mult = 0.9
    else:
        mult = 1.0

    return math.floor(raw * mult)
```

## Implementación completa (Python)

```python
import math
from dataclasses import dataclass

LEVEL = 50
IV = 31
AP_TO_EV_RATIO = 7.875
MAX_TOTAL_AP = 66
MAX_STAT_AP = 32

STATS = ("hp", "attack", "defense", "spAttack", "spDefense", "speed")

@dataclass
class Nature:
    key: str            # "modest"
    increased: str | None   # "spAttack" o None si neutral
    decreased: str | None   # "attack" o None si neutral

def ap_to_ev(ap: int) -> int:
    return math.floor(ap * AP_TO_EV_RATIO)

def calc_hp(base: int, ap: int) -> int:
    return math.floor((2*base + IV + math.floor(ap_to_ev(ap)/4)) * LEVEL/100) + LEVEL + 10

def calc_stat(base: int, ap: int, nature: Nature, stat_name: str) -> int:
    raw = math.floor((2*base + IV + math.floor(ap_to_ev(ap)/4)) * LEVEL/100) + 5
    if nature.increased == stat_name:
        mult = 1.1
    elif nature.decreased == stat_name:
        mult = 0.9
    else:
        mult = 1.0
    return math.floor(raw * mult)

def calc_all(base_stats: dict, ap_spread: dict, nature: Nature) -> dict:
    return {
        "hp":        calc_hp(base_stats["hp"], ap_spread["hp"]),
        "attack":    calc_stat(base_stats["attack"],    ap_spread["attack"],    nature, "attack"),
        "defense":   calc_stat(base_stats["defense"],   ap_spread["defense"],   nature, "defense"),
        "spAttack":  calc_stat(base_stats["spAttack"],  ap_spread["spAttack"],  nature, "spAttack"),
        "spDefense": calc_stat(base_stats["spDefense"], ap_spread["spDefense"], nature, "spDefense"),
        "speed":     calc_stat(base_stats["speed"],     ap_spread["speed"],     nature, "speed"),
    }
```

## Validación

Casos manuales contra la calculadora oficial para verificar exactitud bit a bit:

| Pokémon | base | PH | Naturaleza | Stat esperado |
|---|---|---|---|---|
| Charizard SpA=109 | 109 | 32 | Modesta (+SpA) | (2·109 + 31 + floor(252/4)) · 0.5 + 5 = 161 → 161·1.1 = 177 |
| Tyranitar HP=100 | 100 | 32 | (cualquiera) | (2·100 + 31 + 63) · 0.5 + 50 + 10 = 207 |
| Dragapult Spe=142 | 142 | 32 | Tímida (+Spe) | (2·142 + 31 + 63) · 0.5 + 5 = 194 → 194·1.1 = 213 |

Probar contra la calc UI antes de generar matrices.

## Notas

- `math.floor` en Python ≡ `Math.floor` en JS para enteros positivos.
- El `floor(ev/4)` redondea hacia abajo: invertir 1 PH no siempre incrementa el stat final (mínima granularidad práctica ≈ 4 EV).
- El multiplicador de naturaleza se aplica sobre el resultado **ya redondeado**.
