# Spread Optimizer

Para cada defensor, calcula los **PH mínimos en HP + Def/SpD** necesarios para sobrevivir cada amenaza top de la damage matrix (atacantes que le hacen ≥50% por defecto).

Naturaleza defensiva asumida: **Osada** (+Def -Atk) para hits físicos, **Cauta** (+SpD -SpA) para hits especiales.

Generado por `scripts/build_spread_optimizer.py` desde `raw/calculos/damage-matrix.json` y `raw/pokemon/`.

## Limitaciones

- Asume PH Spe = 0 (defensor lento). Si quieres mantener velocidad, resta PH del HP/Def disponibles.
- Type booster del atacante = ×1.2 fijo. Sin Pañuelo / Vidas / críticos / clima.
- El defensor no usa baya tipo en este cálculo (worst case). Una baya tipo divide el daño SE entre 2.
- 'No sobrevive' = ni con 32 PH HP + 32 PH Def consigue tankear (necesitaría buff de habilidad como Multiescamas o reducción extra).

## Detalle por defensor

### Blastoise — base HP 79 / Def 100 / SpD 105

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Whimsicott | Rayo Solar (120, Planta) | ×2 | 104.8% | 0 | 5 | 154 |
| Emboar | Puño Certero (150, Lucha) | — | 65.1% | 0 | 0 | 154 |
| Zoroark de Hisui | Hiperrayo (150, Normal) | — | 65.1% | 0 | 0 | 154 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 60.2% | 0 | 0 | 154 |
| Garchomp | Cometa Draco (130, Dragón) | — | 56.5% | 0 | 0 | 154 |

### Charizard — base HP 78 / Def 78 / SpD 85

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón (150, Agua) | ×2 | 194.6% | — | — | — |
| Slowking | Hidroariete (85, Agua) | ×2 | 74.6% | 0 | 0 | 153 |
| Blastoise | Chilling Water (50, Agua) | ×2 | 66.5% | 0 | 0 | 153 |
| Zoroark de Hisui | Hiperrayo (150, Normal) | — | 65.4% | 0 | 0 | 153 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 60.5% | 0 | 0 | 153 |
| Garchomp | Cometa Draco (130, Dragón) | — | 56.8% | 0 | 0 | 153 |

### Corviknight — base HP 98 / Def 105 / SpD 85

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Typhlosion de Hisui | Estallido (150, Fuego) | ×2 | 175.6% | — | — | — |
| Charizard | Cólera Ardiente (75, Fuego) | ×2 | 89.3% | 11 | 0 | 184 |
| Greninja | Hidrocañón (150, Agua) | — | 87.8% | 8 | 0 | 181 |
| Emboar | Puño Certero (150, Lucha) | — | 59.0% | 0 | 0 | 173 |

### Delphox — base HP 75 / Def 72 / SpD 100

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón (150, Agua) | ×2 | 197.8% | — | — | — |
| Slowking | Hidroariete (85, Agua) | ×2 | 75.8% | 0 | 0 | 150 |
| Incineroar | Desahogo (75, Siniestro) | ×2 | 67.6% | 0 | 0 | 150 |
| Blastoise | Chilling Water (50, Agua) | ×2 | 67.6% | 0 | 0 | 150 |
| Zoroark de Hisui | Hiperrayo (150, Normal) | — | 66.5% | 0 | 0 | 150 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 61.5% | 0 | 0 | 150 |
| Garchomp | Cometa Draco (130, Dragón) | — | 57.7% | 0 | 0 | 150 |

### Dragonite — base HP 91 / Def 95 / SpD 100

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Garchomp | Cometa Draco (130, Dragón) | ×2 | 106.1% | 0 | 13 | 166 |
| Zoroark de Hisui | Hiperrayo (150, Normal) | — | 61.1% | 0 | 0 | 166 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 56.6% | 0 | 0 | 166 |

### Emboar — base HP 110 / Def 65 / SpD 65

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón (150, Agua) | ×2 | 165.9% | — | — | — |
| Corviknight | Ataque Aéreo (140, Volador) | ×2 | 103.7% | — | — | — |
| Espathra | Psíquico (90, Psíquico) | ×2 | 67.7% | 0 | 0 | 185 |
| Slowking | Hidroariete (85, Agua) | ×2 | 63.6% | 0 | 0 | 185 |
| Blastoise | Chilling Water (50, Agua) | ×2 | 56.7% | 0 | 0 | 185 |
| Delphox | Psicorruido (75, Psíquico) | ×2 | 56.7% | 0 | 0 | 185 |
| Zoroark de Hisui | Hiperrayo (150, Normal) | — | 55.8% | 0 | 5 | 185 |

### Espathra — base HP 95 / Def 60 / SpD 60

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Zoroark de Hisui | Hiperrayo (150, Normal) | — | 118.8% | 0 | 10 | 170 |
| Greninja | Hidrocañón (150, Agua) | — | 89.1% | 11 | 0 | 181 |
| Typhlosion de Hisui | Estallido (150, Fuego) | — | 89.1% | 11 | 7 | 181 |
| Incineroar | Desahogo (75, Siniestro) | ×2 | 60.9% | 0 | 4 | 170 |
| Emboar | Puño Certero (150, Lucha) | ×0.5 | 59.4% | 0 | 0 | 170 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 55.4% | 0 | 0 | 170 |
| Garchomp | Cometa Draco (130, Dragón) | — | 52.0% | 0 | 0 | 170 |

### Garchomp — base HP 108 / Def 95 / SpD 85

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón (150, Agua) | — | 83.7% | 0 | 0 | 183 |
| Emboar | Puño Certero (150, Lucha) | — | 56.3% | 0 | 0 | 183 |
| Zoroark de Hisui | Hiperrayo (150, Normal) | — | 56.3% | 0 | 0 | 183 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 52.1% | 0 | 0 | 183 |

### Gengar — base HP 60 / Def 60 / SpD 75

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón (150, Agua) | — | 107.8% | — | — | — |
| Typhlosion de Hisui | Estallido (150, Fuego) | — | 107.8% | — | — | — |
| Espathra | Psíquico (90, Psíquico) | ×2 | 88.0% | 13 | 0 | 148 |
| Incineroar | Desahogo (75, Siniestro) | ×2 | 73.7% | 0 | 4 | 135 |
| Delphox | Psicorruido (75, Psíquico) | ×2 | 73.7% | 0 | 0 | 135 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 67.1% | 0 | 0 | 135 |
| Garchomp | Cometa Draco (130, Dragón) | — | 62.9% | 0 | 0 | 135 |
| Dragonite | Vasto Impacto (60, Dragón) | — | 58.1% | 0 | 0 | 135 |

### Greninja — base HP 72 / Def 67 / SpD 71

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Emboar | Puño Certero (150, Lucha) | ×2 | 135.8% | — | — | — |
| Whimsicott | Rayo Solar (120, Planta) | ×2 | 108.9% | — | — | — |
| Zoroark de Hisui | Hiperrayo (150, Normal) | — | 67.6% | 0 | 0 | 147 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 62.6% | 0 | 0 | 147 |
| Garchomp | Cometa Draco (130, Dragón) | — | 58.7% | 0 | 0 | 147 |
| Typhlosion de Hisui | Estallido (150, Fuego) | ×0.5 | 50.3% | 0 | 0 | 147 |

### Incineroar — base HP 95 / Def 90 / SpD 90

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón (150, Agua) | ×2 | 178.2% | — | — | — |
| Emboar | Puño Certero (150, Lucha) | ×2 | 120.3% | — | — | — |
| Slowking | Hidroariete (85, Agua) | ×2 | 68.3% | 0 | 0 | 170 |
| Blastoise | Chilling Water (50, Agua) | ×2 | 60.9% | 0 | 0 | 170 |
| Zoroark de Hisui | Hiperrayo (150, Normal) | — | 59.9% | 0 | 0 | 170 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 55.4% | 0 | 0 | 170 |
| Garchomp | Cometa Draco (130, Dragón) | — | 52.0% | 0 | 0 | 170 |

### Slowking — base HP 95 / Def 80 / SpD 110

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Incineroar | Desahogo (75, Siniestro) | ×2 | 60.9% | 0 | 0 | 170 |
| Zoroark de Hisui | Hiperrayo (150, Normal) | — | 59.9% | 0 | 0 | 170 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 55.4% | 0 | 0 | 170 |

### Typhlosion de Hisui — base HP 73 / Def 78 / SpD 85

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón (150, Agua) | ×2 | 200.0% | — | — | — |
| Slowking | Hidroariete (85, Agua) | ×2 | 76.7% | 0 | 0 | 148 |
| Incineroar | Desahogo (75, Siniestro) | ×2 | 68.3% | 0 | 0 | 148 |
| Blastoise | Chilling Water (50, Agua) | ×2 | 68.3% | 0 | 0 | 148 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 62.2% | 0 | 0 | 148 |
| Garchomp | Cometa Draco (130, Dragón) | — | 58.3% | 0 | 0 | 148 |

### Whimsicott — base HP 60 / Def 85 / SpD 75

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Typhlosion de Hisui | Estallido (150, Fuego) | ×2 | 215.6% | — | — | — |
| Corviknight | Ataque Aéreo (140, Volador) | ×2 | 134.7% | — | — | — |
| Charizard | Cólera Ardiente (75, Fuego) | ×2 | 109.6% | 0 | 32 | 135 |
| Zoroark de Hisui | Hiperrayo (150, Normal) | — | 72.5% | 0 | 0 | 135 |
| Greninja | Hidrocañón (150, Agua) | ×0.5 | 53.9% | 0 | 0 | 135 |

### Zoroark de Hisui — base HP 55 / Def 60 / SpD 60

| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón (150, Agua) | — | 111.1% | — | — | — |
| Typhlosion de Hisui | Estallido (150, Fuego) | — | 111.1% | — | — | — |
| Incineroar | Desahogo (75, Siniestro) | ×2 | 75.9% | 0 | 4 | 130 |
| Corviknight | Ataque Aéreo (140, Volador) | — | 69.1% | 0 | 0 | 130 |
| Garchomp | Cometa Draco (130, Dragón) | — | 64.8% | 0 | 0 | 130 |
| Dragonite | Vasto Impacto (60, Dragón) | — | 59.9% | 0 | 0 | 130 |
| Whimsicott | Rayo Solar (120, Planta) | — | 59.9% | 0 | 0 | 130 |
| Charizard | Cólera Ardiente (75, Fuego) | — | 56.2% | 0 | 0 | 130 |
