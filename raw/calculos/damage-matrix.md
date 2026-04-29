# Damage Matrix — Nv.50

Daño calculado para cada atacante disponible vs cada defensor disponible, usando:

- **Atacante**: preset Sweeper o Physical (según mejor STAB) + naturaleza + type booster ×1.2 + STAB
- **Defensor**: spread Bulky 32 HP / 16 Def / 16 SpD
- **Movimiento**: el de mayor potencia entre los STAB del movepool del atacante
- **Roll**: 0.85 → 1.00 (sin críticos)

Generado por `scripts/build_damage_matrix.py` desde `raw/pokemon/`, `raw/ataques/`, `raw/tipos/`,
constantes de `raw/mecanicas/formula-stats.md`, fórmula de `raw/mecanicas/formula-dano.md`,
type boosters de `raw/mecanicas/objetos-calc.md`.

## Limitaciones

- Sin clima, terreno, críticos, multi-hit, spread reduction (doubles), boost stages, burn
- Habilidades modeladas: solo las 14 con efecto en daño (ver `raw/mecanicas/habilidades-calc.md`).
  Habilidades como Intimidación, Multiescamas, absorbedoras de tipo NO modeladas.
- Sin Pañuelo Elección (no afecta daño directo, sí turn order — ver `raw/calculos/speed-vs-scarf.md`)
- Columnas extra: **+ Baya** (defensor con baya tipo correspondiente, ×0.5 si SE), **Si quemado** (atacante quemado ×0.5 atk físico)
- ⚠️ La columna **Si quemado** sufre colapso cuando `floor(atk/def) ≤ 1` (formula op.gg trunca la división). En esos casos el daño no refleja realismo VGC.
- Setup defensivo es un único spread universal — no optimizado por matchup

## Resumen por atacante

### Emboar (Fuego/Lucha)

- **Setup**: Physical (32 Atk / 32 Spe), naturaleza Firme, type booster ×1.2
- **Habilidad activa**: Mar Llamas (modelada)
- **Movimiento**: Puño Certero (Lucha, 150 BP, physical)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Greninja | Agua/Siniestro | 179 | ×2 | 206-243 | 115.1–135.8% | **OHKO** | 67.6% | 3.4% | — |
| Incineroar | Fuego/Siniestro | 202 | ×2 | 206-243 | 102.0–120.3% | **OHKO** | 59.9% | 3.0% | — |
| Blastoise | Agua | 186 | — | 103-121 | 55.4–65.1% | 2HKO | — | 1.6% | — |
| Espathra | Psiquico | 202 | ×0.5 | 102-120 | 50.5–59.4% | 2HKO | — | 29.7% | — |
| Corviknight | Volador/Acero | 205 | — | 103-121 | 50.2–59.0% | 2HKO | — | 1.5% | — |
| Garchomp | Dragon/Tierra | 215 | — | 103-121 | 47.9–56.3% | 2HKO | — | 1.4% | — |
| Emboar | Fuego/Lucha | 217 | — | 103-121 | 47.5–55.8% | 2HKO | — | 1.4% | — |
| Whimsicott | Planta/Hada | 167 | ×0.5 | 51-60 | 30.5–35.9% | 3HKO | — | 0.6% | — |
| Delphox | Fuego/Psiquico | 182 | ×0.5 | 51-60 | 28.0–33.0% | 4HKO | — | 0.5% | — |
| Charizard | Fuego/Volador | 185 | ×0.5 | 51-60 | 27.6–32.4% | 4HKO | — | 0.5% | — |
| Dragonite | Dragon/Volador | 198 | ×0.5 | 51-60 | 25.8–30.3% | 4HKO | — | 0.5% | — |
| Slowking | Agua/Psiquico | 202 | ×0.5 | 51-60 | 25.2–29.7% | 4HKO | — | 0.5% | — |
| Gengar | Fantasma/Veneno | 167 | ×0 | 0-0 | 0.0–0.0% | 167HKO | — | 0.0% | — |
| Zoroark de Hisui | Normal/Fantasma | 162 | ×0 | 0-0 | 0.0–0.0% | 162HKO | — | 0.0% | — |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | ×0 | 0-0 | 0.0–0.0% | 180HKO | — | 0.0% | — |

### Incineroar (Fuego/Siniestro)

- **Setup**: Physical (32 Atk / 32 Spe), naturaleza Firme, type booster ×1.2
- **Habilidad activa**: Mar Llamas (modelada)
- **Movimiento**: Desahogo (Siniestro, 75 BP, physical)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Zoroark de Hisui | Normal/Fantasma | 162 | ×2 | 104-123 | 64.2–75.9% | 2HKO | 37.7% | 3.7% | — |
| Gengar | Fantasma/Veneno | 167 | ×2 | 104-123 | 62.3–73.7% | 2HKO | 36.5% | 3.6% | — |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | ×2 | 104-123 | 57.8–68.3% | 2HKO | 33.9% | 3.3% | — |
| Delphox | Fuego/Psiquico | 182 | ×2 | 104-123 | 57.1–67.6% | 2HKO | 33.5% | 3.3% | — |
| Espathra | Psiquico | 202 | ×2 | 104-123 | 51.5–60.9% | 2HKO | 30.2% | 3.0% | — |
| Slowking | Agua/Psiquico | 202 | ×2 | 104-123 | 51.5–60.9% | 2HKO | 30.2% | 3.0% | — |
| Charizard | Fuego/Volador | 185 | — | 52-61 | 28.1–33.0% | 4HKO | — | 1.6% | — |
| Blastoise | Agua | 186 | — | 52-61 | 28.0–32.8% | 4HKO | — | 1.6% | — |
| Dragonite | Dragon/Volador | 198 | — | 52-61 | 26.3–30.8% | 4HKO | — | 1.5% | — |
| Corviknight | Volador/Acero | 205 | — | 52-61 | 25.4–29.8% | 4HKO | — | 1.5% | — |
| Garchomp | Dragon/Tierra | 215 | — | 52-61 | 24.2–28.4% | 4HKO | — | 1.4% | — |
| Whimsicott | Planta/Hada | 167 | ×0.5 | 26-30 | 15.6–18.0% | 6HKO | — | 0.6% | — |
| Greninja | Agua/Siniestro | 179 | ×0.5 | 26-30 | 14.5–16.8% | 6HKO | — | 0.6% | — |
| Incineroar | Fuego/Siniestro | 202 | ×0.5 | 26-30 | 12.9–14.9% | 7HKO | — | 0.5% | — |
| Emboar | Fuego/Lucha | 217 | ×0.5 | 26-30 | 12.0–13.8% | 8HKO | — | 0.5% | — |

### Espathra (Psiquico)

- **Setup**: Sweeper (32 SpA / 32 Spe), naturaleza Modesta, type booster ×1.2
- **Habilidad activa**: Oportunista
- **Movimiento**: Psíquico (Psíquico, 90 BP, special)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Gengar | Fantasma/Veneno | 167 | ×2 | 124-147 | 74.3–88.0% | 2HKO | 43.7% | — | — |
| Emboar | Fuego/Lucha | 217 | ×2 | 124-147 | 57.1–67.7% | 2HKO | 33.6% | — | — |
| Zoroark de Hisui | Normal/Fantasma | 162 | — | 62-73 | 38.3–45.1% | 3HKO | — | — | — |
| Whimsicott | Planta/Hada | 167 | — | 62-73 | 37.1–43.7% | 3HKO | — | — | — |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | — | 62-73 | 34.4–40.6% | 3HKO | — | — | — |
| Charizard | Fuego/Volador | 185 | — | 62-73 | 33.5–39.5% | 3HKO | — | — | — |
| Blastoise | Agua | 186 | — | 62-73 | 33.3–39.2% | 3HKO | — | — | — |
| Dragonite | Dragon/Volador | 198 | — | 62-73 | 31.3–36.9% | 3HKO | — | — | — |
| Garchomp | Dragon/Tierra | 215 | — | 62-73 | 28.8–34.0% | 3HKO | — | — | — |
| Delphox | Fuego/Psiquico | 182 | ×0.5 | 31-36 | 17.0–19.8% | 6HKO | — | — | — |
| Espathra | Psiquico | 202 | ×0.5 | 31-36 | 15.3–17.8% | 6HKO | — | — | — |
| Slowking | Agua/Psiquico | 202 | ×0.5 | 31-36 | 15.3–17.8% | 6HKO | — | — | — |
| Corviknight | Volador/Acero | 205 | ×0.5 | 31-36 | 15.1–17.6% | 6HKO | — | — | — |
| Incineroar | Fuego/Siniestro | 202 | ×0 | 0-0 | 0.0–0.0% | 202HKO | — | — | — |
| Greninja | Agua/Siniestro | 179 | ×0 | 0-0 | 0.0–0.0% | 179HKO | — | — | — |

### Charizard (Fuego/Volador)

- **Setup**: Physical (32 Atk / 32 Spe), naturaleza Firme, type booster ×1.2
- **Habilidad activa**: Mar Llamas (modelada)
- **Movimiento**: Cólera Ardiente (Fuego, 75 BP, physical)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Whimsicott | Planta/Hada | 167 | ×2 | 155-183 | 92.8–109.6% | **OHKO** | 54.5% | 3.6% | blaze |
| Corviknight | Volador/Acero | 205 | ×2 | 155-183 | 75.6–89.3% | 2HKO | 44.4% | 2.9% | blaze |
| Zoroark de Hisui | Normal/Fantasma | 162 | — | 77-91 | 47.5–56.2% | 2HKO | — | 1.9% | blaze |
| Gengar | Fantasma/Veneno | 167 | — | 77-91 | 46.1–54.5% | 2HKO | — | 1.8% | blaze |
| Espathra | Psiquico | 202 | — | 77-91 | 38.1–45.0% | 3HKO | — | 1.5% | blaze |
| Greninja | Agua/Siniestro | 179 | ×0.5 | 38-45 | 21.2–25.1% | 4HKO | — | 0.6% | blaze |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | ×0.5 | 38-45 | 21.1–25.0% | 4HKO | — | 0.6% | blaze |
| Delphox | Fuego/Psiquico | 182 | ×0.5 | 38-45 | 20.9–24.7% | 5HKO | — | 0.5% | blaze |
| Charizard | Fuego/Volador | 185 | ×0.5 | 38-45 | 20.5–24.3% | 5HKO | — | 0.5% | blaze |
| Blastoise | Agua | 186 | ×0.5 | 38-45 | 20.4–24.2% | 5HKO | — | 0.5% | blaze |
| Dragonite | Dragon/Volador | 198 | ×0.5 | 38-45 | 19.2–22.7% | 5HKO | — | 0.5% | blaze |
| Incineroar | Fuego/Siniestro | 202 | ×0.5 | 38-45 | 18.8–22.3% | 5HKO | — | 0.5% | blaze |
| Slowking | Agua/Psiquico | 202 | ×0.5 | 38-45 | 18.8–22.3% | 5HKO | — | 0.5% | blaze |
| Garchomp | Dragon/Tierra | 215 | ×0.5 | 38-45 | 17.7–20.9% | 5HKO | — | 0.5% | blaze |
| Emboar | Fuego/Lucha | 217 | ×0.5 | 38-45 | 17.5–20.7% | 5HKO | — | 0.5% | blaze |

### Gengar (Fantasma/Veneno)

- **Setup**: Sweeper (32 SpA / 32 Spe), naturaleza Modesta, type booster ×1.2
- **Habilidad activa**: Cuerpo Maldito
- **Movimiento**: Tera Blast (Normal, 80 BP, special)
- **STAB activo**: no

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Espathra | Psiquico | 202 | — | 73-86 | 36.1–42.6% | 3HKO | — | — | — |
| Whimsicott | Planta/Hada | 167 | — | 37-44 | 22.2–26.3% | 4HKO | — | — | — |
| Greninja | Agua/Siniestro | 179 | — | 37-44 | 20.7–24.6% | 5HKO | — | — | — |
| Delphox | Fuego/Psiquico | 182 | — | 37-44 | 20.3–24.2% | 5HKO | — | — | — |
| Charizard | Fuego/Volador | 185 | — | 37-44 | 20.0–23.8% | 5HKO | — | — | — |
| Blastoise | Agua | 186 | — | 37-44 | 19.9–23.7% | 5HKO | — | — | — |
| Dragonite | Dragon/Volador | 198 | — | 37-44 | 18.7–22.2% | 5HKO | — | — | — |
| Incineroar | Fuego/Siniestro | 202 | — | 37-44 | 18.3–21.8% | 5HKO | — | — | — |
| Slowking | Agua/Psiquico | 202 | — | 37-44 | 18.3–21.8% | 5HKO | — | — | — |
| Garchomp | Dragon/Tierra | 215 | — | 37-44 | 17.2–20.5% | 5HKO | — | — | — |
| Emboar | Fuego/Lucha | 217 | — | 37-44 | 17.1–20.3% | 5HKO | — | — | — |
| Corviknight | Volador/Acero | 205 | ×0.5 | 18-22 | 8.8–10.7% | 10HKO | — | — | — |
| Gengar | Fantasma/Veneno | 167 | ×0 | 0-0 | 0.0–0.0% | 167HKO | — | — | — |
| Zoroark de Hisui | Normal/Fantasma | 162 | ×0 | 0-0 | 0.0–0.0% | 162HKO | — | — | — |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | ×0 | 0-0 | 0.0–0.0% | 180HKO | — | — | — |

### Zoroark de Hisui (Normal/Fantasma)

- **Setup**: Sweeper (32 SpA / 32 Spe), naturaleza Modesta, type booster ×1.2
- **Habilidad activa**: Ilusión
- **Movimiento**: Hiperrayo (Normal, 150 BP, special)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Espathra | Psiquico | 202 | — | 204-240 | 101.0–118.8% | **OHKO** | — | — | — |
| Whimsicott | Planta/Hada | 167 | — | 103-121 | 61.7–72.5% | 2HKO | — | — | — |
| Greninja | Agua/Siniestro | 179 | — | 103-121 | 57.5–67.6% | 2HKO | — | — | — |
| Delphox | Fuego/Psiquico | 182 | — | 103-121 | 56.6–66.5% | 2HKO | — | — | — |
| Charizard | Fuego/Volador | 185 | — | 103-121 | 55.7–65.4% | 2HKO | — | — | — |
| Blastoise | Agua | 186 | — | 103-121 | 55.4–65.1% | 2HKO | — | — | — |
| Dragonite | Dragon/Volador | 198 | — | 103-121 | 52.0–61.1% | 2HKO | — | — | — |
| Incineroar | Fuego/Siniestro | 202 | — | 103-121 | 51.0–59.9% | 2HKO | — | — | — |
| Slowking | Agua/Psiquico | 202 | — | 103-121 | 51.0–59.9% | 2HKO | — | — | — |
| Garchomp | Dragon/Tierra | 215 | — | 103-121 | 47.9–56.3% | 2HKO | — | — | — |
| Emboar | Fuego/Lucha | 217 | — | 103-121 | 47.5–55.8% | 2HKO | — | — | — |
| Corviknight | Volador/Acero | 205 | ×0.5 | 51-60 | 24.9–29.3% | 4HKO | — | — | — |
| Gengar | Fantasma/Veneno | 167 | ×0 | 0-0 | 0.0–0.0% | 167HKO | — | — | — |
| Zoroark de Hisui | Normal/Fantasma | 162 | ×0 | 0-0 | 0.0–0.0% | 162HKO | — | — | — |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | ×0 | 0-0 | 0.0–0.0% | 180HKO | — | — | — |

### Greninja (Agua/Siniestro)

- **Setup**: Sweeper (32 SpA / 32 Spe), naturaleza Modesta, type booster ×1.2
- **Habilidad activa**: Torrente (modelada)
- **Movimiento**: Hidrocañón (Agua, 150 BP, special)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Typhlosion de Hisui | Fuego/Fantasma | 180 | ×2 | 306-360 | 170.0–200.0% | **OHKO** | 100.0% | — | torrent |
| Delphox | Fuego/Psiquico | 182 | ×2 | 306-360 | 168.1–197.8% | **OHKO** | 98.9% | — | torrent |
| Charizard | Fuego/Volador | 185 | ×2 | 306-360 | 165.4–194.6% | **OHKO** | 97.3% | — | torrent |
| Incineroar | Fuego/Siniestro | 202 | ×2 | 306-360 | 151.5–178.2% | **OHKO** | 89.1% | — | torrent |
| Emboar | Fuego/Lucha | 217 | ×2 | 306-360 | 141.0–165.9% | **OHKO** | 82.9% | — | torrent |
| Zoroark de Hisui | Normal/Fantasma | 162 | — | 153-180 | 94.4–111.1% | **OHKO** | — | — | torrent |
| Gengar | Fantasma/Veneno | 167 | — | 153-180 | 91.6–107.8% | **OHKO** | — | — | torrent |
| Espathra | Psiquico | 202 | — | 153-180 | 75.7–89.1% | 2HKO | — | — | torrent |
| Corviknight | Volador/Acero | 205 | — | 153-180 | 74.6–87.8% | 2HKO | — | — | torrent |
| Garchomp | Dragon/Tierra | 215 | — | 153-180 | 71.2–83.7% | 2HKO | — | — | torrent |
| Whimsicott | Planta/Hada | 167 | ×0.5 | 76-90 | 45.5–53.9% | 2HKO | — | — | torrent |
| Greninja | Agua/Siniestro | 179 | ×0.5 | 76-90 | 42.5–50.3% | 2HKO | — | — | torrent |
| Blastoise | Agua | 186 | ×0.5 | 76-90 | 40.9–48.4% | 3HKO | — | — | torrent |
| Dragonite | Dragon/Volador | 198 | ×0.5 | 76-90 | 38.4–45.5% | 3HKO | — | — | torrent |
| Slowking | Agua/Psiquico | 202 | ×0.5 | 76-90 | 37.6–44.6% | 3HKO | — | — | torrent |

### Corviknight (Volador/Acero)

- **Setup**: Physical (32 Atk / 32 Spe), naturaleza Firme, type booster ×1.2
- **Habilidad activa**: Presión
- **Movimiento**: Ataque Aéreo (Volador, 140 BP, physical)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Whimsicott | Planta/Hada | 167 | ×2 | 191-225 | 114.4–134.7% | **OHKO** | 67.1% | 3.6% | — |
| Emboar | Fuego/Lucha | 217 | ×2 | 191-225 | 88.0–103.7% | **OHKO** | 51.6% | 2.8% | — |
| Zoroark de Hisui | Normal/Fantasma | 162 | — | 95-112 | 58.6–69.1% | 2HKO | — | 1.9% | — |
| Gengar | Fantasma/Veneno | 167 | — | 95-112 | 56.9–67.1% | 2HKO | — | 1.8% | — |
| Greninja | Agua/Siniestro | 179 | — | 95-112 | 53.1–62.6% | 2HKO | — | 1.7% | — |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | — | 95-112 | 52.8–62.2% | 2HKO | — | 1.7% | — |
| Delphox | Fuego/Psiquico | 182 | — | 95-112 | 52.2–61.5% | 2HKO | — | 1.6% | — |
| Charizard | Fuego/Volador | 185 | — | 95-112 | 51.4–60.5% | 2HKO | — | 1.6% | — |
| Blastoise | Agua | 186 | — | 95-112 | 51.1–60.2% | 2HKO | — | 1.6% | — |
| Dragonite | Dragon/Volador | 198 | — | 95-112 | 48.0–56.6% | 2HKO | — | 1.5% | — |
| Incineroar | Fuego/Siniestro | 202 | — | 95-112 | 47.0–55.4% | 2HKO | — | 1.5% | — |
| Espathra | Psiquico | 202 | — | 95-112 | 47.0–55.4% | 2HKO | — | 1.5% | — |
| Slowking | Agua/Psiquico | 202 | — | 95-112 | 47.0–55.4% | 2HKO | — | 1.5% | — |
| Garchomp | Dragon/Tierra | 215 | — | 95-112 | 44.2–52.1% | 2HKO | — | 1.4% | — |
| Corviknight | Volador/Acero | 205 | ×0.5 | 47-56 | 22.9–27.3% | 4HKO | — | 0.5% | — |

### Blastoise (Agua)

- **Setup**: Sweeper (32 SpA / 32 Spe), naturaleza Modesta, type booster ×1.2
- **Habilidad activa**: Torrente (modelada)
- **Movimiento**: Chilling Water (Agua, 50 BP, special)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Typhlosion de Hisui | Fuego/Fantasma | 180 | ×2 | 104-123 | 57.8–68.3% | 2HKO | 33.9% | — | torrent |
| Delphox | Fuego/Psiquico | 182 | ×2 | 104-123 | 57.1–67.6% | 2HKO | 33.5% | — | torrent |
| Charizard | Fuego/Volador | 185 | ×2 | 104-123 | 56.2–66.5% | 2HKO | 33.0% | — | torrent |
| Incineroar | Fuego/Siniestro | 202 | ×2 | 104-123 | 51.5–60.9% | 2HKO | 30.2% | — | torrent |
| Emboar | Fuego/Lucha | 217 | ×2 | 104-123 | 47.9–56.7% | 2HKO | 28.1% | — | torrent |
| Zoroark de Hisui | Normal/Fantasma | 162 | — | 52-61 | 32.1–37.7% | 3HKO | — | — | torrent |
| Gengar | Fantasma/Veneno | 167 | — | 52-61 | 31.1–36.5% | 3HKO | — | — | torrent |
| Espathra | Psiquico | 202 | — | 52-61 | 25.7–30.2% | 4HKO | — | — | torrent |
| Corviknight | Volador/Acero | 205 | — | 52-61 | 25.4–29.8% | 4HKO | — | — | torrent |
| Garchomp | Dragon/Tierra | 215 | — | 52-61 | 24.2–28.4% | 4HKO | — | — | torrent |
| Whimsicott | Planta/Hada | 167 | ×0.5 | 26-30 | 15.6–18.0% | 6HKO | — | — | torrent |
| Greninja | Agua/Siniestro | 179 | ×0.5 | 26-30 | 14.5–16.8% | 6HKO | — | — | torrent |
| Blastoise | Agua | 186 | ×0.5 | 26-30 | 14.0–16.1% | 7HKO | — | — | torrent |
| Dragonite | Dragon/Volador | 198 | ×0.5 | 26-30 | 13.1–15.2% | 7HKO | — | — | torrent |
| Slowking | Agua/Psiquico | 202 | ×0.5 | 26-30 | 12.9–14.9% | 7HKO | — | — | torrent |

### Slowking (Agua/Psiquico)

- **Setup**: Physical (32 Atk / 32 Spe), naturaleza Firme, type booster ×1.2
- **Habilidad activa**: Despiste
- **Movimiento**: Hidroariete (Agua, 85 BP, physical)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Typhlosion de Hisui | Fuego/Fantasma | 180 | ×2 | 117-138 | 65.0–76.7% | 2HKO | 38.3% | 3.3% | — |
| Delphox | Fuego/Psiquico | 182 | ×2 | 117-138 | 64.3–75.8% | 2HKO | 37.9% | 3.3% | — |
| Charizard | Fuego/Volador | 185 | ×2 | 117-138 | 63.2–74.6% | 2HKO | 37.3% | 3.2% | — |
| Incineroar | Fuego/Siniestro | 202 | ×2 | 117-138 | 57.9–68.3% | 2HKO | 34.2% | 3.0% | — |
| Emboar | Fuego/Lucha | 217 | ×2 | 117-138 | 53.9–63.6% | 2HKO | 31.8% | 2.8% | — |
| Zoroark de Hisui | Normal/Fantasma | 162 | — | 58-69 | 35.8–42.6% | 3HKO | — | 1.9% | — |
| Gengar | Fantasma/Veneno | 167 | — | 58-69 | 34.7–41.3% | 3HKO | — | 1.8% | — |
| Espathra | Psiquico | 202 | — | 58-69 | 28.7–34.2% | 3HKO | — | 1.5% | — |
| Garchomp | Dragon/Tierra | 215 | — | 58-69 | 27.0–32.1% | 4HKO | — | 1.4% | — |
| Whimsicott | Planta/Hada | 167 | ×0.5 | 29-34 | 17.4–20.4% | 5HKO | — | 0.6% | — |
| Greninja | Agua/Siniestro | 179 | ×0.5 | 29-34 | 16.2–19.0% | 6HKO | — | 0.6% | — |
| Blastoise | Agua | 186 | ×0.5 | 29-34 | 15.6–18.3% | 6HKO | — | 0.5% | — |
| Dragonite | Dragon/Volador | 198 | ×0.5 | 29-34 | 14.6–17.2% | 6HKO | — | 0.5% | — |
| Slowking | Agua/Psiquico | 202 | ×0.5 | 29-34 | 14.4–16.8% | 6HKO | — | 0.5% | — |
| Corviknight | Volador/Acero | 205 | — | 2-3 | 1.0–1.5% | 69HKO | — | 1.5% | — |

### Dragonite (Dragon/Volador)

- **Setup**: Physical (32 Atk / 32 Spe), naturaleza Firme, type booster ×1.2
- **Habilidad activa**: Foco Interno
- **Movimiento**: Vasto Impacto (Dragón, 60 BP, physical)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Zoroark de Hisui | Normal/Fantasma | 162 | — | 82-97 | 50.6–59.9% | 2HKO | — | 30.2% | — |
| Gengar | Fantasma/Veneno | 167 | — | 82-97 | 49.1–58.1% | 2HKO | — | 29.3% | — |
| Dragonite | Dragon/Volador | 198 | ×2 | 84-99 | 42.4–50.0% | 2HKO | 24.7% | 3.0% | — |
| Espathra | Psiquico | 202 | — | 82-97 | 40.6–48.0% | 3HKO | — | 24.3% | — |
| Garchomp | Dragon/Tierra | 215 | ×2 | 84-99 | 39.1–46.0% | 3HKO | 22.8% | 2.8% | — |
| Emboar | Fuego/Lucha | 217 | — | 82-97 | 37.8–44.7% | 3HKO | — | 22.6% | — |
| Greninja | Agua/Siniestro | 179 | — | 42-49 | 23.5–27.4% | 4HKO | — | 1.7% | — |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | — | 42-49 | 23.3–27.2% | 4HKO | — | 1.7% | — |
| Delphox | Fuego/Psiquico | 182 | — | 42-49 | 23.1–26.9% | 4HKO | — | 1.6% | — |
| Charizard | Fuego/Volador | 185 | — | 42-49 | 22.7–26.5% | 4HKO | — | 1.6% | — |
| Blastoise | Agua | 186 | — | 42-49 | 22.6–26.3% | 4HKO | — | 1.6% | — |
| Incineroar | Fuego/Siniestro | 202 | — | 42-49 | 20.8–24.3% | 5HKO | — | 1.5% | — |
| Slowking | Agua/Psiquico | 202 | — | 42-49 | 20.8–24.3% | 5HKO | — | 1.5% | — |
| Corviknight | Volador/Acero | 205 | ×0.5 | 21-24 | 10.2–11.7% | 9HKO | — | 0.5% | — |
| Whimsicott | Planta/Hada | 167 | ×0 | 0-0 | 0.0–0.0% | 167HKO | — | 0.0% | — |

### Delphox (Fuego/Psiquico)

- **Setup**: Sweeper (32 SpA / 32 Spe), naturaleza Modesta, type booster ×1.2
- **Habilidad activa**: Mar Llamas (modelada)
- **Movimiento**: Psicorruido (Psíquico, 75 BP, special)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Gengar | Fantasma/Veneno | 167 | ×2 | 104-123 | 62.3–73.7% | 2HKO | 36.5% | — | — |
| Emboar | Fuego/Lucha | 217 | ×2 | 104-123 | 47.9–56.7% | 2HKO | 28.1% | — | — |
| Zoroark de Hisui | Normal/Fantasma | 162 | — | 52-61 | 32.1–37.7% | 3HKO | — | — | — |
| Whimsicott | Planta/Hada | 167 | — | 52-61 | 31.1–36.5% | 3HKO | — | — | — |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | — | 52-61 | 28.9–33.9% | 3HKO | — | — | — |
| Charizard | Fuego/Volador | 185 | — | 52-61 | 28.1–33.0% | 4HKO | — | — | — |
| Blastoise | Agua | 186 | — | 52-61 | 28.0–32.8% | 4HKO | — | — | — |
| Dragonite | Dragon/Volador | 198 | — | 52-61 | 26.3–30.8% | 4HKO | — | — | — |
| Garchomp | Dragon/Tierra | 215 | — | 52-61 | 24.2–28.4% | 4HKO | — | — | — |
| Delphox | Fuego/Psiquico | 182 | ×0.5 | 26-30 | 14.3–16.5% | 7HKO | — | — | — |
| Espathra | Psiquico | 202 | ×0.5 | 26-30 | 12.9–14.9% | 7HKO | — | — | — |
| Slowking | Agua/Psiquico | 202 | ×0.5 | 26-30 | 12.9–14.9% | 7HKO | — | — | — |
| Corviknight | Volador/Acero | 205 | ×0.5 | 26-30 | 12.7–14.6% | 7HKO | — | — | — |
| Incineroar | Fuego/Siniestro | 202 | ×0 | 0-0 | 0.0–0.0% | 202HKO | — | — | — |
| Greninja | Agua/Siniestro | 179 | ×0 | 0-0 | 0.0–0.0% | 179HKO | — | — | — |

### Whimsicott (Planta/Hada)

- **Setup**: Sweeper (32 SpA / 32 Spe), naturaleza Modesta, type booster ×1.2
- **Habilidad activa**: Bromista
- **Movimiento**: Rayo Solar (Planta, 120 BP, special)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Greninja | Agua/Siniestro | 179 | ×2 | 165-195 | 92.2–108.9% | **OHKO** | 54.2% | — | — |
| Blastoise | Agua | 186 | ×2 | 165-195 | 88.7–104.8% | **OHKO** | 52.2% | — | — |
| Zoroark de Hisui | Normal/Fantasma | 162 | — | 82-97 | 50.6–59.9% | 2HKO | — | — | — |
| Espathra | Psiquico | 202 | — | 82-97 | 40.6–48.0% | 3HKO | — | — | — |
| Garchomp | Dragon/Tierra | 215 | — | 82-97 | 38.1–45.1% | 3HKO | — | — | — |
| Gengar | Fantasma/Veneno | 167 | ×0.5 | 41-48 | 24.6–28.7% | 4HKO | — | — | — |
| Whimsicott | Planta/Hada | 167 | ×0.5 | 41-48 | 24.6–28.7% | 4HKO | — | — | — |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | ×0.5 | 41-48 | 22.8–26.7% | 4HKO | — | — | — |
| Delphox | Fuego/Psiquico | 182 | ×0.5 | 41-48 | 22.5–26.4% | 4HKO | — | — | — |
| Incineroar | Fuego/Siniestro | 202 | ×0.5 | 41-48 | 20.3–23.8% | 5HKO | — | — | — |
| Emboar | Fuego/Lucha | 217 | ×0.5 | 41-48 | 18.9–22.1% | 5HKO | — | — | — |
| Charizard | Fuego/Volador | 185 | ×0.25 | 20-24 | 10.8–13.0% | 8HKO | — | — | — |
| Dragonite | Dragon/Volador | 198 | ×0.25 | 20-24 | 10.1–12.1% | 9HKO | — | — | — |
| Corviknight | Volador/Acero | 205 | ×0.25 | 20-24 | 9.8–11.7% | 9HKO | — | — | — |
| Slowking | Agua/Psiquico | 202 | ×2 | 5-6 | 2.5–3.0% | 34HKO | 1.5% | — | — |

### Garchomp (Dragon/Tierra)

- **Setup**: Sweeper (32 SpA / 32 Spe), naturaleza Modesta, type booster ×1.2
- **Habilidad activa**: Velo Arena
- **Movimiento**: Cometa Draco (Dragón, 130 BP, special)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Dragonite | Dragon/Volador | 198 | ×2 | 178-210 | 89.9–106.1% | **OHKO** | 53.0% | — | — |
| Garchomp | Dragon/Tierra | 215 | ×2 | 178-210 | 82.8–97.7% | 2HKO | 48.8% | — | — |
| Zoroark de Hisui | Normal/Fantasma | 162 | — | 89-105 | 54.9–64.8% | 2HKO | — | — | — |
| Gengar | Fantasma/Veneno | 167 | — | 89-105 | 53.3–62.9% | 2HKO | — | — | — |
| Greninja | Agua/Siniestro | 179 | — | 89-105 | 49.7–58.7% | 2HKO | — | — | — |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | — | 89-105 | 49.4–58.3% | 2HKO | — | — | — |
| Delphox | Fuego/Psiquico | 182 | — | 89-105 | 48.9–57.7% | 2HKO | — | — | — |
| Charizard | Fuego/Volador | 185 | — | 89-105 | 48.1–56.8% | 2HKO | — | — | — |
| Blastoise | Agua | 186 | — | 89-105 | 47.8–56.5% | 2HKO | — | — | — |
| Incineroar | Fuego/Siniestro | 202 | — | 89-105 | 44.1–52.0% | 2HKO | — | — | — |
| Espathra | Psiquico | 202 | — | 89-105 | 44.1–52.0% | 2HKO | — | — | — |
| Emboar | Fuego/Lucha | 217 | — | 89-105 | 41.0–48.4% | 3HKO | — | — | — |
| Corviknight | Volador/Acero | 205 | ×0.5 | 44-52 | 21.5–25.4% | 4HKO | — | — | — |
| Slowking | Agua/Psiquico | 202 | — | 2-3 | 1.0–1.5% | 68HKO | — | — | — |
| Whimsicott | Planta/Hada | 167 | ×0 | 0-0 | 0.0–0.0% | 167HKO | — | — | — |

### Typhlosion de Hisui (Fuego/Fantasma)

- **Setup**: Sweeper (32 SpA / 32 Spe), naturaleza Modesta, type booster ×1.2
- **Habilidad activa**: Mar Llamas (modelada)
- **Movimiento**: Estallido (Fuego, 150 BP, special)
- **STAB activo**: sí

| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |
|---|---|---|---|---|---|---|---|---|---|
| Whimsicott | Planta/Hada | 167 | ×2 | 306-360 | 183.2–215.6% | **OHKO** | 107.8% | — | blaze |
| Corviknight | Volador/Acero | 205 | ×2 | 306-360 | 149.3–175.6% | **OHKO** | 87.8% | — | blaze |
| Zoroark de Hisui | Normal/Fantasma | 162 | — | 153-180 | 94.4–111.1% | **OHKO** | — | — | blaze |
| Gengar | Fantasma/Veneno | 167 | — | 153-180 | 91.6–107.8% | **OHKO** | — | — | blaze |
| Espathra | Psiquico | 202 | — | 153-180 | 75.7–89.1% | 2HKO | — | — | blaze |
| Greninja | Agua/Siniestro | 179 | ×0.5 | 76-90 | 42.5–50.3% | 2HKO | — | — | blaze |
| Typhlosion de Hisui | Fuego/Fantasma | 180 | ×0.5 | 76-90 | 42.2–50.0% | 2HKO | — | — | blaze |
| Delphox | Fuego/Psiquico | 182 | ×0.5 | 76-90 | 41.8–49.5% | 3HKO | — | — | blaze |
| Charizard | Fuego/Volador | 185 | ×0.5 | 76-90 | 41.1–48.6% | 3HKO | — | — | blaze |
| Blastoise | Agua | 186 | ×0.5 | 76-90 | 40.9–48.4% | 3HKO | — | — | blaze |
| Dragonite | Dragon/Volador | 198 | ×0.5 | 76-90 | 38.4–45.5% | 3HKO | — | — | blaze |
| Incineroar | Fuego/Siniestro | 202 | ×0.5 | 76-90 | 37.6–44.6% | 3HKO | — | — | blaze |
| Slowking | Agua/Psiquico | 202 | ×0.5 | 76-90 | 37.6–44.6% | 3HKO | — | — | blaze |
| Garchomp | Dragon/Tierra | 215 | ×0.5 | 76-90 | 35.3–41.9% | 3HKO | — | — | blaze |
| Emboar | Fuego/Lucha | 217 | ×0.5 | 76-90 | 35.0–41.5% | 3HKO | — | — | blaze |
