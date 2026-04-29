# Pañuelo Elección — Ranking de Candidatos

Pokémon disponibles ranqueados como candidatos a llevar **Pañuelo Elección** según:

```
score = spe_opt * 0.05
      + scarf_jump * 4    (enemigos extra que outspeed con Pañuelo)
      + ohkos * 6         (OHKOs ya conseguidos con su mejor STAB)
      + twohkos * 2
      + se_count * 1.5    (versatilidad SE)
      - 15 si ya outspeed a todos sin Pañuelo
```

Generado por `scripts/build_scarf_candidates.py` desde `speed-vs-scarf.json`,
`coverage-matrix.json` y `damage-matrix.json`.

## Limitaciones

- Pañuelo lockea al Pokémon en 1 movimiento durante todo el combate.
- Score asume que el move 'mejor STAB' que usa damage-matrix será el move bloqueado.
- No considera coverage físico vs especial mixto (un Sweeper bloqueado en move físico pierde su Mansa/Modesta SpA).
- Score no penaliza explícitamente sustituibilidad por type booster ×1.2 (Pañuelo no boostea power, solo Spe).

## Ranking

| # | Pokémon | Tipos | Spe opt | Spe scarf | Salto | OHKOs | 2HKOs | SE | Mejor STAB | Score |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Corviknight | Volador/Acero | 130 | **195** | +11 | 2 | 14 | 11 | Ataque Aéreo (140) | **107.0** |
| 2 | Emboar | Fuego/Lucha | 128 | **192** | +12 | 2 | 6 | 17 | Puño Certero (150) | **103.9** |
| 3 | Typhlosion de Hisui | Fuego/Fantasma | 161 | **241** | +8 | 4 | 6 | 18 | Estallido (150) | **103.0** |
| 4 | Greninja | Agua/Siniestro | 191 | **286** | +0 | 7 | 11 | 18 | Hidrocañón (150) | **85.5** |
| 5 | Garchomp | Dragon/Tierra | 169 | **253** | +6 | 1 | 10 | 18 | Cometa Draco (130) | **85.5** |
| 6 | Incineroar | Fuego/Siniestro | 123 | **184** | +11 | 0 | 6 | 12 | Desahogo (75) | **80.2** |
| 7 | Zoroark de Hisui | Normal/Fantasma | 178 | **267** | +3 | 1 | 11 | 17 | Hiperrayo (150) | **74.4** |
| 8 | Dragonite | Dragon/Volador | 145 | **217** | +9 | 0 | 2 | 14 | Vasto Impacto (60) | **68.2** |
| 9 | Charizard | Fuego/Volador | 167 | **250** | +7 | 1 | 4 | 10 | Cólera Ardiente (75) | **65.3** |
| 10 | Blastoise | Agua | 143 | **214** | +10 | 0 | 5 | 3 | Chilling Water (50) | **61.6** |
| 11 | Espathra | Psiquico | 172 | **258** | +4 | 0 | 2 | 16 | Psíquico (90) | **52.6** |
| 12 | Whimsicott | Planta/Hada | 184 | **276** | +1 | 2 | 3 | 11 | Rayo Solar (120) | **47.7** |
| 13 | Slowking | Agua/Psiquico | 90 | **135** | +3 | 0 | 5 | 8 | Hidroariete (85) | **38.5** |
| 14 | Delphox | Fuego/Psiquico | 171 | **256** | +5 | 0 | 2 | 2 | Psicorruido (75) | **35.5** |
| 15 | Gengar | Fantasma/Veneno | 178 | **267** | +3 | 0 | 0 | 2 | Tera Blast (80) | **23.9** |

## Análisis top 5

### 1. Corviknight (Volador/Acero) — score 107.0

- **Spe optimizada**: 130 → con Pañuelo **195** (outspeed 3 → 14, salto +11)
- **Move bloqueado**: Ataque Aéreo (Volador, 140 BP)
- **OHKOs/2HKOs**: 2 / 14  |  **SE coverage**: 11/18

### 2. Emboar (Fuego/Lucha) — score 103.9

- **Spe optimizada**: 128 → con Pañuelo **192** (outspeed 2 → 14, salto +12)
- **Move bloqueado**: Puño Certero (Lucha, 150 BP)
- **OHKOs/2HKOs**: 2 / 6  |  **SE coverage**: 17/18

### 3. Typhlosion de Hisui (Fuego/Fantasma) — score 103.0

- **Spe optimizada**: 161 → con Pañuelo **241** (outspeed 6 → 14, salto +8)
- **Move bloqueado**: Estallido (Fuego, 150 BP)
- **OHKOs/2HKOs**: 4 / 6  |  **SE coverage**: 18/18

### 4. Greninja (Agua/Siniestro) — score 85.5

- **Spe optimizada**: 191 → con Pañuelo **286** (outspeed 14 → 14, salto +0)
- **Move bloqueado**: Hidrocañón (Agua, 150 BP)
- **OHKOs/2HKOs**: 7 / 11  |  **SE coverage**: 18/18

### 5. Garchomp (Dragon/Tierra) — score 85.5

- **Spe optimizada**: 169 → con Pañuelo **253** (outspeed 8 → 14, salto +6)
- **Move bloqueado**: Cometa Draco (Dragón, 130 BP)
- **OHKOs/2HKOs**: 1 / 10  |  **SE coverage**: 18/18
