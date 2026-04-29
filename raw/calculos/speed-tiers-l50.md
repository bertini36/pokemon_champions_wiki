# Speed Tiers — Nv.50

Velocidad final de cada Pokémon a Nivel 50 según escenario de PH y naturaleza.

Generado por `scripts/build_speed_tiers.py` desde `raw/pokemon/*.md` + constantes
de `raw/mecanicas/formula-stats.md`.

## Escenarios

| Columna | PH Spe | Naturaleza | Multiplicador |
|---|---|---|---|
| **Spe (+Nat)** | 32 | +Spe (Tímida/Alegre/Ingenua/Activa/Miedosa) | 1.1 |
| Spe (Neutral) | 32 | Neutral | 1.0 |
| Spe (0 PH) | 0 | Neutral | 1.0 |
| Spe (-Nat) | 0 | -Spe (Audaz/Plácida/Mansa/Grosera/Serena) | 0.9 |

Ordenado por **Spe (+Nat)** descendente. Solo Pokémon disponibles en el juego.

## Tabla

| # | Pokémon | Tipos | Base Spe | Spe (+Nat) | Spe (Neutral) | Spe (0 PH) | Spe (-Nat) |
|---|---|---|---|---|---|---|---|
| 1 | Greninja | Agua/Siniestro | 122 | **191** | 174 | 142 | 127 |
| 2 | Whimsicott | Planta/Hada | 116 | **184** | 168 | 136 | 122 |
| 3 | Gengar | Fantasma/Veneno | 110 | **178** | 162 | 130 | 117 |
| 4 | Zoroark de Hisui | Normal/Fantasma | 110 | **178** | 162 | 130 | 117 |
| 5 | Espathra | Psiquico | 105 | **172** | 157 | 125 | 112 |
| 6 | Delphox | Fuego/Psiquico | 104 | **171** | 156 | 124 | 111 |
| 7 | Garchomp | Dragon/Tierra | 102 | **169** | 154 | 122 | 109 |
| 8 | Charizard | Fuego/Volador | 100 | **167** | 152 | 120 | 108 |
| 9 | Typhlosion de Hisui | Fuego/Fantasma | 95 | **161** | 147 | 115 | 103 |
| 10 | Dragonite | Dragon/Volador | 80 | **145** | 132 | 100 | 90 |
| 11 | Blastoise | Agua | 78 | **143** | 130 | 98 | 88 |
| 12 | Corviknight | Volador/Acero | 67 | **130** | 119 | 87 | 78 |
| 13 | Emboar | Fuego/Lucha | 65 | **128** | 117 | 85 | 76 |
| 14 | Incineroar | Fuego/Siniestro | 60 | **123** | 112 | 80 | 72 |
| 15 | Slowking | Agua/Psiquico | 30 | **90** | 82 | 50 | 45 |

## Notas

- Speed tier = ranking 1ºer turno: quien tenga mayor Spe efectiva mueve antes (sin prioridad de movimiento).
- Empates de Spe se resuelven aleatoriamente turno a turno.
- Pañuelo Elegido (objeto, no modelado en estas columnas) multiplica Spe × 1.5.
- En Trick Room, el orden se invierte: menor Spe ataca primero.
- Bonus por Bromuro/Mejora/Cambio de Marcha y otros boosts: aplicar +1/+2/etc. sobre **Spe (+Nat)** antes de comparar.
- Pokémon no disponibles (Forma Regional, Mega no liberada, etc.) excluidos de la tabla principal.
