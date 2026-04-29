# Presets de Rol — Pokémon Champions

4 spreads oficiales que sugiere op.gg/calculator como punto de partida para roles VGC. Los 66 PH se distribuyen siempre como **32 + 32 + 2** (cap por stat = 32).

Fuente: bundle JS de https://op.gg/es/pokemon-champions/calculator (`{label:"Sweeper",points:{...}}`).

## Tabla de spreads

| Preset | HP | Atk | Def | SpA | SpD | Spe | Total |
|---|---|---|---|---|---|---|---|
| **Sweeper**  | 0 | 0 | 0 | **32** | 2 | **32** | 66 |
| **Physical** | 0 | **32** | 0 | 0 | 2 | **32** | 66 |
| **Tank**     | **32** | 0 | **32** | 0 | 2 | 0 | 66 |
| **SpD Tank** | **32** | 0 | 2 | 0 | **32** | 0 | 66 |

## Naturaleza recomendada por preset

| Preset | Naturaleza típica | Por qué |
|---|---|---|
| Sweeper  | **Tímida** (+Spe -Atk) o **Modesta** (+SpA -Atk) | Atacante especial que outspeed o pega más fuerte |
| Physical | **Alegre** (+Spe -SpA) o **Firme** (+Atk -SpA) | Atacante físico, perder SpA no duele |
| Tank     | **Osada** (+Def -Atk) | Pared física que no usa Atk |
| SpD Tank | **Cauta** (+SpD -SpA) | Pared especial que no usa SpA |

## Cuándo usar cada preset (heurística VGC)

### Sweeper (SpA + Spe)
- Atacantes especiales con base SpA ≥ 100 y base Spe ≥ 90
- Ejemplos: Dragapult (Especial), Iron Bundle, Hydreigon, Latios, Espathra
- Naturaleza preferida: **Tímida** salvo que ya superes el speed tier objetivo
- Movimientos: 4 ataques o 3 ataques + 1 pivot/setup

### Physical (Atk + Spe)
- Atacantes físicos rápidos (sweepers físicos clásicos)
- Ejemplos: Garchomp, Dragapult (Físico), Urshifu, Iron Jugulis físico, Roaring Moon
- Naturaleza preferida: **Alegre**; **Firme** si tienes prioridad o asistencia de speed control
- Movimientos: 3-4 ataques físicos, posible Bote/Doble Filo

### Tank (HP + Def)
- Pivots/walls físicos que absorben hits y disparan utilidad
- Ejemplos: Cresselia, Indeedee-F, Amoonguss, Clodsire, Toxapex
- Naturaleza preferida: **Osada**
- Movimientos: status (Bostezo, Espora, Truco), pivot (Cambiazo, Volt-Turn), apoyo (Asista, Trick Room)

### SpD Tank (HP + SpD)
- Walls especiales contra meta de atacantes especiales o Choice Specs
- Ejemplos: Tyranitar (con Tormenta de Arena), Heatran defensivo, Blissey/Chansey, Hydrapple
- Naturaleza preferida: **Cauta**
- Movimientos: status, pivot, ataques de utilidad (Roca Afilada de Tyranitar tras CC)

## Limitaciones de los presets

Son **plantillas universales**, no spreads optimizados. Para VGC competitivo deberías:

1. **Calcular benchmarks** específicos: ¿cuántos PH de SpD necesita para sobrevivir Lanzallamas Modesta máx de Heatran?
2. **Ajustar speed creep**: a veces 28 PH Spe basta y los 4 sobrantes van a HP/SpD
3. **Considerar EV mixto**: a veces 16 Atk + 20 SpA para cubrir Foul Play / Misty Explosion
4. **Pensar en el item**: con Pañuelo Elegido el Sweeper no necesita Tímida → puedes usar Modesta
5. **Diseñar contra un meta**: el preset Tank no sirve igual contra meta físico vs meta especial

## Spread de referencia avanzado (no en op.gg)

Algunos spreads VGC reales que la calc no ofrece:

| Nombre informal | Distribución | Caso de uso |
|---|---|---|
| Bulky Attacker | 16 HP / 32 Atk / 8 Def / 0 SpA / 6 SpD / 4 Spe | Outspeed básico + supervivencia clave |
| Trick Room Attacker | 32 HP / 32 Atk / 0 Def / 2 SpA / 0 SpD / 0 Spe | TR setter o atacante TR |
| Mixed Wall | 32 HP / 0 / 16 Def / 0 / 16 SpD / 2 Spe | Pared mixta |
| Speed Creep Sweeper | 0 / 24 / 4 / 32 / 4 / 2 PH... | Optimizar para benchmarks específicos |

Estos spreads se generan caso a caso con `damage_calc` + `speed_tier`. Plantillas op.gg solo cubren el 70% de casos.

## JSON estructurado

```json
{
  "sweeper":   {"hp": 0,  "attack": 0,  "defense": 0,  "spAttack": 32, "spDefense": 2,  "speed": 32},
  "physical":  {"hp": 0,  "attack": 32, "defense": 0,  "spAttack": 0,  "spDefense": 2,  "speed": 32},
  "tank":      {"hp": 32, "attack": 0,  "defense": 32, "spAttack": 0,  "spDefense": 2,  "speed": 0},
  "spd_tank":  {"hp": 32, "attack": 0,  "defense": 2,  "spAttack": 0,  "spDefense": 32, "speed": 0}
}
```

## Notas

- Los 4 presets siempre suman 66 (= MAX_TOTAL_AP) y nunca exceden 32 por stat (= MAX_STAT_AP).
- El **2 sobrante** se asigna a SpD (Sweeper, Physical) o Def (SpD Tank) por convención op.gg, pero podría ir a cualquier stat.
- En español, los presets podrían rebrandeados en el wiki como "Barredor / Físico / Pared / Pared Especial" si queremos consistencia ES total.
