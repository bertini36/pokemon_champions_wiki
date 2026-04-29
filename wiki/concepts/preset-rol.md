---
title: Preset de Rol
date: 2026-04-29
type: concept
tags: [mecanica, preset, sweeper, tank, spread]
---

# Preset de Rol

## Definition

4 spreads oficiales que sugiere op.gg/calculator como punto de partida. Los 66 PH se distribuyen siempre 32+32+2 (cap por stat = 32).

| Preset | HP | Atk | Def | SpA | SpD | Spe |
|---|---|---|---|---|---|---|
| **Sweeper** | 0 | 0 | 0 | 32 | 2 | 32 |
| **Physical** | 0 | 32 | 0 | 0 | 2 | 32 |
| **Tank** | 32 | 0 | 32 | 0 | 2 | 0 |
| **SpD Tank** | 32 | 0 | 2 | 0 | 32 | 0 |

## Why it matters

Plantilla universal. Sirve como punto de partida; rara vez es óptimo. Para VGC competitivo:

1. **Calcular benchmarks** específicos contra amenazas reales (ver [[spread-optimizer]])
2. **Ajustar speed creep**: a veces 28 PH Spe basta y los 4 sobrantes van a HP/SpD
3. **Considerar EV mixto**: 16 Atk + 20 SpA para cubrir Foul Play
4. **Pensar en el item**: con Pañuelo el Sweeper puede usar Modesta en vez de Tímida
5. **Diseñar contra meta concreto**

### Naturaleza recomendada por preset

| Preset | Naturaleza |
|---|---|
| Sweeper | Tímida o Modesta |
| Physical | Alegre o Firme |
| Tank | Osada |
| SpD Tank | Cauta |

### Cuándo usar cada uno

- **Sweeper**: SpA ≥ 100 y Spe ≥ 90 (Dragapult-Especial, Iron Bundle, Hydreigon, Latios, Espathra)
- **Physical**: Atk + Spe (Garchomp, Dragapult-Físico, Urshifu, Roaring Moon)
- **Tank**: pivots/walls físicos (Cresselia, Indeedee-F, Amoonguss, Toxapex)
- **SpD Tank**: walls especiales (Tyranitar arena, Heatran, Hydrapple)

## Connections

Plantilla más usada en construcción inicial. [[damage-matrix]] aplica Sweeper o Physical según mejor STAB. [[scarf-candidate]] mezcla con [[panuelo-eleccion]] para outspeed.

## Sources

- [[op-gg-calculator]] — `{label:"Sweeper",points:{...}}` en bundle JS
- [[builds-curated]] — builds reales rara vez siguen presets puros

## 🔗 Related

- [[ph-puntos-habilidad]]
- [[naturaleza]]
- [[spread-optimizer]]
- [[damage-matrix]]
- [[scarf-candidate]]
