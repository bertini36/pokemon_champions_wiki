# Threat List por Defensor

Para cada Pokémon disponible, lista qué atacantes le hacen daño y cuántos le OHKOean / 2HKOean.
Ordenado por **número de OHKOs recibidos** (los más vulnerables primero).

Generado por `scripts/build_threat_list.py` desde `raw/calculos/damage-matrix.json`.

## Resumen — vulnerabilidad

| # | Defensor | Tipos | HP | OHKOs | 2HKOs | Atacantes |
|---|---|---|---|---|---|---|
| 1 | Whimsicott | Planta/Hada | 167 | **3** | 5 | 14 |
| 2 | Gengar | Fantasma/Veneno | 167 | **2** | 9 | 14 |
| 3 | Zoroark de Hisui | Normal/Fantasma | 162 | **2** | 8 | 14 |
| 4 | Incineroar | Fuego/Siniestro | 202 | **2** | 7 | 14 |
| 5 | Emboar | Fuego/Lucha | 217 | **2** | 7 | 14 |
| 6 | Greninja | Agua/Siniestro | 179 | **2** | 6 | 14 |
| 7 | Espathra | Psiquico | 202 | **1** | 7 | 14 |
| 8 | Delphox | Fuego/Psiquico | 182 | **1** | 7 | 14 |
| 9 | Charizard | Fuego/Volador | 185 | **1** | 6 | 14 |
| 10 | Typhlosion de Hisui | Fuego/Fantasma | 180 | **1** | 6 | 14 |
| 11 | Blastoise | Agua | 186 | **1** | 5 | 14 |
| 12 | Corviknight | Volador/Acero | 205 | **1** | 4 | 14 |
| 13 | Dragonite | Dragon/Volador | 198 | **1** | 3 | 14 |
| 14 | Garchomp | Dragon/Tierra | 215 | **0** | 4 | 14 |
| 15 | Slowking | Agua/Psiquico | 202 | **0** | 3 | 14 |

## Detalle por defensor

### Whimsicott (Planta/Hada) — HP 167

- **Riesgo**: 3 OHKOs, 5 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Typhlosion de Hisui | Estallido | Fuego | ×2 | 183.2–215.6% | **OHKO** | STAB, blaze |
| Corviknight | Ataque Aéreo | Volador | ×2 | 114.4–134.7% | **OHKO** | STAB |
| Charizard | Cólera Ardiente | Fuego | ×2 | 92.8–109.6% | **OHKO** | STAB, blaze |
| Zoroark de Hisui | Hiperrayo | Normal | — | 61.7–72.5% | 2HKO | STAB |
| Greninja | Hidrocañón | Agua | ×0.5 | 45.5–53.9% | 2HKO | STAB, torrent |
| Espathra | Psíquico | Psíquico | — | 37.1–43.7% | 43.7% | STAB |
| Delphox | Psicorruido | Psíquico | — | 31.1–36.5% | 36.5% | STAB |
| Emboar | Puño Certero | Lucha | ×0.5 | 30.5–35.9% | 35.9% | STAB |
| Gengar | Tera Blast | Normal | — | 22.2–26.3% | 26.3% | — |
| Slowking | Hidroariete | Agua | ×0.5 | 17.4–20.4% | 20.4% | STAB |
| Incineroar | Desahogo | Siniestro | ×0.5 | 15.6–18.0% | 18.0% | STAB |
| Blastoise | Chilling Water | Agua | ×0.5 | 15.6–18.0% | 18.0% | STAB, torrent |
| Dragonite | Vasto Impacto | Dragón | ×0 | 0.0–0.0% | 0.0% | STAB |
| Garchomp | Cometa Draco | Dragón | ×0 | 0.0–0.0% | 0.0% | STAB |

### Gengar (Fantasma/Veneno) — HP 167

- **Riesgo**: 2 OHKOs, 9 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón | Agua | — | 91.6–107.8% | **OHKO** | STAB, torrent |
| Typhlosion de Hisui | Estallido | Fuego | — | 91.6–107.8% | **OHKO** | STAB, blaze |
| Espathra | Psíquico | Psíquico | ×2 | 74.3–88.0% | 2HKO | STAB |
| Incineroar | Desahogo | Siniestro | ×2 | 62.3–73.7% | 2HKO | STAB |
| Delphox | Psicorruido | Psíquico | ×2 | 62.3–73.7% | 2HKO | STAB |
| Corviknight | Ataque Aéreo | Volador | — | 56.9–67.1% | 2HKO | STAB |
| Garchomp | Cometa Draco | Dragón | — | 53.3–62.9% | 2HKO | STAB |
| Dragonite | Vasto Impacto | Dragón | — | 49.1–58.1% | 2HKO | STAB |
| Charizard | Cólera Ardiente | Fuego | — | 46.1–54.5% | 2HKO | STAB, blaze |
| Slowking | Hidroariete | Agua | — | 34.7–41.3% | 41.3% | STAB |
| Blastoise | Chilling Water | Agua | — | 31.1–36.5% | 36.5% | STAB, torrent |
| Whimsicott | Rayo Solar | Planta | ×0.5 | 24.6–28.7% | 28.7% | STAB |
| Emboar | Puño Certero | Lucha | ×0 | 0.0–0.0% | 0.0% | STAB |
| Zoroark de Hisui | Hiperrayo | Normal | ×0 | 0.0–0.0% | 0.0% | STAB |

### Zoroark de Hisui (Normal/Fantasma) — HP 162

- **Riesgo**: 2 OHKOs, 8 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón | Agua | — | 94.4–111.1% | **OHKO** | STAB, torrent |
| Typhlosion de Hisui | Estallido | Fuego | — | 94.4–111.1% | **OHKO** | STAB, blaze |
| Incineroar | Desahogo | Siniestro | ×2 | 64.2–75.9% | 2HKO | STAB |
| Corviknight | Ataque Aéreo | Volador | — | 58.6–69.1% | 2HKO | STAB |
| Garchomp | Cometa Draco | Dragón | — | 54.9–64.8% | 2HKO | STAB |
| Dragonite | Vasto Impacto | Dragón | — | 50.6–59.9% | 2HKO | STAB |
| Whimsicott | Rayo Solar | Planta | — | 50.6–59.9% | 2HKO | STAB |
| Charizard | Cólera Ardiente | Fuego | — | 47.5–56.2% | 2HKO | STAB, blaze |
| Espathra | Psíquico | Psíquico | — | 38.3–45.1% | 45.1% | STAB |
| Slowking | Hidroariete | Agua | — | 35.8–42.6% | 42.6% | STAB |
| Blastoise | Chilling Water | Agua | — | 32.1–37.7% | 37.7% | STAB, torrent |
| Delphox | Psicorruido | Psíquico | — | 32.1–37.7% | 37.7% | STAB |
| Emboar | Puño Certero | Lucha | ×0 | 0.0–0.0% | 0.0% | STAB |
| Gengar | Tera Blast | Normal | ×0 | 0.0–0.0% | 0.0% | — |

### Incineroar (Fuego/Siniestro) — HP 202

- **Riesgo**: 2 OHKOs, 7 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón | Agua | ×2 | 151.5–178.2% | **OHKO** | STAB, torrent |
| Emboar | Puño Certero | Lucha | ×2 | 102.0–120.3% | **OHKO** | STAB |
| Slowking | Hidroariete | Agua | ×2 | 57.9–68.3% | 2HKO | STAB |
| Blastoise | Chilling Water | Agua | ×2 | 51.5–60.9% | 2HKO | STAB, torrent |
| Zoroark de Hisui | Hiperrayo | Normal | — | 51.0–59.9% | 2HKO | STAB |
| Corviknight | Ataque Aéreo | Volador | — | 47.0–55.4% | 2HKO | STAB |
| Garchomp | Cometa Draco | Dragón | — | 44.1–52.0% | 2HKO | STAB |
| Typhlosion de Hisui | Estallido | Fuego | ×0.5 | 37.6–44.6% | 44.6% | STAB, blaze |
| Dragonite | Vasto Impacto | Dragón | — | 20.8–24.3% | 24.3% | STAB |
| Whimsicott | Rayo Solar | Planta | ×0.5 | 20.3–23.8% | 23.8% | STAB |
| Charizard | Cólera Ardiente | Fuego | ×0.5 | 18.8–22.3% | 22.3% | STAB, blaze |
| Gengar | Tera Blast | Normal | — | 18.3–21.8% | 21.8% | — |
| Espathra | Psíquico | Psíquico | ×0 | 0.0–0.0% | 0.0% | STAB |
| Delphox | Psicorruido | Psíquico | ×0 | 0.0–0.0% | 0.0% | STAB |

### Emboar (Fuego/Lucha) — HP 217

- **Riesgo**: 2 OHKOs, 7 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón | Agua | ×2 | 141.0–165.9% | **OHKO** | STAB, torrent |
| Corviknight | Ataque Aéreo | Volador | ×2 | 88.0–103.7% | **OHKO** | STAB |
| Espathra | Psíquico | Psíquico | ×2 | 57.1–67.7% | 2HKO | STAB |
| Slowking | Hidroariete | Agua | ×2 | 53.9–63.6% | 2HKO | STAB |
| Blastoise | Chilling Water | Agua | ×2 | 47.9–56.7% | 2HKO | STAB, torrent |
| Delphox | Psicorruido | Psíquico | ×2 | 47.9–56.7% | 2HKO | STAB |
| Zoroark de Hisui | Hiperrayo | Normal | — | 47.5–55.8% | 2HKO | STAB |
| Garchomp | Cometa Draco | Dragón | — | 41.0–48.4% | 48.4% | STAB |
| Dragonite | Vasto Impacto | Dragón | — | 37.8–44.7% | 44.7% | STAB |
| Typhlosion de Hisui | Estallido | Fuego | ×0.5 | 35.0–41.5% | 41.5% | STAB, blaze |
| Whimsicott | Rayo Solar | Planta | ×0.5 | 18.9–22.1% | 22.1% | STAB |
| Charizard | Cólera Ardiente | Fuego | ×0.5 | 17.5–20.7% | 20.7% | STAB, blaze |
| Gengar | Tera Blast | Normal | — | 17.1–20.3% | 20.3% | — |
| Incineroar | Desahogo | Siniestro | ×0.5 | 12.0–13.8% | 13.8% | STAB |

### Greninja (Agua/Siniestro) — HP 179

- **Riesgo**: 2 OHKOs, 6 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Emboar | Puño Certero | Lucha | ×2 | 115.1–135.8% | **OHKO** | STAB |
| Whimsicott | Rayo Solar | Planta | ×2 | 92.2–108.9% | **OHKO** | STAB |
| Zoroark de Hisui | Hiperrayo | Normal | — | 57.5–67.6% | 2HKO | STAB |
| Corviknight | Ataque Aéreo | Volador | — | 53.1–62.6% | 2HKO | STAB |
| Garchomp | Cometa Draco | Dragón | — | 49.7–58.7% | 2HKO | STAB |
| Typhlosion de Hisui | Estallido | Fuego | ×0.5 | 42.5–50.3% | 2HKO | STAB, blaze |
| Dragonite | Vasto Impacto | Dragón | — | 23.5–27.4% | 27.4% | STAB |
| Charizard | Cólera Ardiente | Fuego | ×0.5 | 21.2–25.1% | 25.1% | STAB, blaze |
| Gengar | Tera Blast | Normal | — | 20.7–24.6% | 24.6% | — |
| Slowking | Hidroariete | Agua | ×0.5 | 16.2–19.0% | 19.0% | STAB |
| Incineroar | Desahogo | Siniestro | ×0.5 | 14.5–16.8% | 16.8% | STAB |
| Blastoise | Chilling Water | Agua | ×0.5 | 14.5–16.8% | 16.8% | STAB, torrent |
| Espathra | Psíquico | Psíquico | ×0 | 0.0–0.0% | 0.0% | STAB |
| Delphox | Psicorruido | Psíquico | ×0 | 0.0–0.0% | 0.0% | STAB |

### Espathra (Psiquico) — HP 202

- **Riesgo**: 1 OHKOs, 7 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Zoroark de Hisui | Hiperrayo | Normal | — | 101.0–118.8% | **OHKO** | STAB |
| Greninja | Hidrocañón | Agua | — | 75.7–89.1% | 2HKO | STAB, torrent |
| Typhlosion de Hisui | Estallido | Fuego | — | 75.7–89.1% | 2HKO | STAB, blaze |
| Incineroar | Desahogo | Siniestro | ×2 | 51.5–60.9% | 2HKO | STAB |
| Emboar | Puño Certero | Lucha | ×0.5 | 50.5–59.4% | 2HKO | STAB |
| Corviknight | Ataque Aéreo | Volador | — | 47.0–55.4% | 2HKO | STAB |
| Garchomp | Cometa Draco | Dragón | — | 44.1–52.0% | 2HKO | STAB |
| Dragonite | Vasto Impacto | Dragón | — | 40.6–48.0% | 48.0% | STAB |
| Whimsicott | Rayo Solar | Planta | — | 40.6–48.0% | 48.0% | STAB |
| Charizard | Cólera Ardiente | Fuego | — | 38.1–45.0% | 45.0% | STAB, blaze |
| Gengar | Tera Blast | Normal | — | 36.1–42.6% | 42.6% | — |
| Slowking | Hidroariete | Agua | — | 28.7–34.2% | 34.2% | STAB |
| Blastoise | Chilling Water | Agua | — | 25.7–30.2% | 30.2% | STAB, torrent |
| Delphox | Psicorruido | Psíquico | ×0.5 | 12.9–14.9% | 14.9% | STAB |

### Delphox (Fuego/Psiquico) — HP 182

- **Riesgo**: 1 OHKOs, 7 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón | Agua | ×2 | 168.1–197.8% | **OHKO** | STAB, torrent |
| Slowking | Hidroariete | Agua | ×2 | 64.3–75.8% | 2HKO | STAB |
| Incineroar | Desahogo | Siniestro | ×2 | 57.1–67.6% | 2HKO | STAB |
| Blastoise | Chilling Water | Agua | ×2 | 57.1–67.6% | 2HKO | STAB, torrent |
| Zoroark de Hisui | Hiperrayo | Normal | — | 56.6–66.5% | 2HKO | STAB |
| Corviknight | Ataque Aéreo | Volador | — | 52.2–61.5% | 2HKO | STAB |
| Garchomp | Cometa Draco | Dragón | — | 48.9–57.7% | 2HKO | STAB |
| Typhlosion de Hisui | Estallido | Fuego | ×0.5 | 41.8–49.5% | 49.5% | STAB, blaze |
| Emboar | Puño Certero | Lucha | ×0.5 | 28.0–33.0% | 33.0% | STAB |
| Dragonite | Vasto Impacto | Dragón | — | 23.1–26.9% | 26.9% | STAB |
| Whimsicott | Rayo Solar | Planta | ×0.5 | 22.5–26.4% | 26.4% | STAB |
| Charizard | Cólera Ardiente | Fuego | ×0.5 | 20.9–24.7% | 24.7% | STAB, blaze |
| Gengar | Tera Blast | Normal | — | 20.3–24.2% | 24.2% | — |
| Espathra | Psíquico | Psíquico | ×0.5 | 17.0–19.8% | 19.8% | STAB |

### Charizard (Fuego/Volador) — HP 185

- **Riesgo**: 1 OHKOs, 6 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón | Agua | ×2 | 165.4–194.6% | **OHKO** | STAB, torrent |
| Slowking | Hidroariete | Agua | ×2 | 63.2–74.6% | 2HKO | STAB |
| Blastoise | Chilling Water | Agua | ×2 | 56.2–66.5% | 2HKO | STAB, torrent |
| Zoroark de Hisui | Hiperrayo | Normal | — | 55.7–65.4% | 2HKO | STAB |
| Corviknight | Ataque Aéreo | Volador | — | 51.4–60.5% | 2HKO | STAB |
| Garchomp | Cometa Draco | Dragón | — | 48.1–56.8% | 2HKO | STAB |
| Typhlosion de Hisui | Estallido | Fuego | ×0.5 | 41.1–48.6% | 48.6% | STAB, blaze |
| Espathra | Psíquico | Psíquico | — | 33.5–39.5% | 39.5% | STAB |
| Incineroar | Desahogo | Siniestro | — | 28.1–33.0% | 33.0% | STAB |
| Delphox | Psicorruido | Psíquico | — | 28.1–33.0% | 33.0% | STAB |
| Emboar | Puño Certero | Lucha | ×0.5 | 27.6–32.4% | 32.4% | STAB |
| Dragonite | Vasto Impacto | Dragón | — | 22.7–26.5% | 26.5% | STAB |
| Gengar | Tera Blast | Normal | — | 20.0–23.8% | 23.8% | — |
| Whimsicott | Rayo Solar | Planta | ×0.25 | 10.8–13.0% | 13.0% | STAB |

### Typhlosion de Hisui (Fuego/Fantasma) — HP 180

- **Riesgo**: 1 OHKOs, 6 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón | Agua | ×2 | 170.0–200.0% | **OHKO** | STAB, torrent |
| Slowking | Hidroariete | Agua | ×2 | 65.0–76.7% | 2HKO | STAB |
| Incineroar | Desahogo | Siniestro | ×2 | 57.8–68.3% | 2HKO | STAB |
| Blastoise | Chilling Water | Agua | ×2 | 57.8–68.3% | 2HKO | STAB, torrent |
| Corviknight | Ataque Aéreo | Volador | — | 52.8–62.2% | 2HKO | STAB |
| Garchomp | Cometa Draco | Dragón | — | 49.4–58.3% | 2HKO | STAB |
| Espathra | Psíquico | Psíquico | — | 34.4–40.6% | 40.6% | STAB |
| Delphox | Psicorruido | Psíquico | — | 28.9–33.9% | 33.9% | STAB |
| Dragonite | Vasto Impacto | Dragón | — | 23.3–27.2% | 27.2% | STAB |
| Whimsicott | Rayo Solar | Planta | ×0.5 | 22.8–26.7% | 26.7% | STAB |
| Charizard | Cólera Ardiente | Fuego | ×0.5 | 21.1–25.0% | 25.0% | STAB, blaze |
| Emboar | Puño Certero | Lucha | ×0 | 0.0–0.0% | 0.0% | STAB |
| Gengar | Tera Blast | Normal | ×0 | 0.0–0.0% | 0.0% | — |
| Zoroark de Hisui | Hiperrayo | Normal | ×0 | 0.0–0.0% | 0.0% | STAB |

### Blastoise (Agua) — HP 186

- **Riesgo**: 1 OHKOs, 5 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Whimsicott | Rayo Solar | Planta | ×2 | 88.7–104.8% | **OHKO** | STAB |
| Emboar | Puño Certero | Lucha | — | 55.4–65.1% | 2HKO | STAB |
| Zoroark de Hisui | Hiperrayo | Normal | — | 55.4–65.1% | 2HKO | STAB |
| Corviknight | Ataque Aéreo | Volador | — | 51.1–60.2% | 2HKO | STAB |
| Garchomp | Cometa Draco | Dragón | — | 47.8–56.5% | 2HKO | STAB |
| Greninja | Hidrocañón | Agua | ×0.5 | 40.9–48.4% | 48.4% | STAB, torrent |
| Typhlosion de Hisui | Estallido | Fuego | ×0.5 | 40.9–48.4% | 48.4% | STAB, blaze |
| Espathra | Psíquico | Psíquico | — | 33.3–39.2% | 39.2% | STAB |
| Incineroar | Desahogo | Siniestro | — | 28.0–32.8% | 32.8% | STAB |
| Delphox | Psicorruido | Psíquico | — | 28.0–32.8% | 32.8% | STAB |
| Dragonite | Vasto Impacto | Dragón | — | 22.6–26.3% | 26.3% | STAB |
| Charizard | Cólera Ardiente | Fuego | ×0.5 | 20.4–24.2% | 24.2% | STAB, blaze |
| Gengar | Tera Blast | Normal | — | 19.9–23.7% | 23.7% | — |
| Slowking | Hidroariete | Agua | ×0.5 | 15.6–18.3% | 18.3% | STAB |

### Corviknight (Volador/Acero) — HP 205

- **Riesgo**: 1 OHKOs, 4 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Typhlosion de Hisui | Estallido | Fuego | ×2 | 149.3–175.6% | **OHKO** | STAB, blaze |
| Charizard | Cólera Ardiente | Fuego | ×2 | 75.6–89.3% | 2HKO | STAB, blaze |
| Greninja | Hidrocañón | Agua | — | 74.6–87.8% | 2HKO | STAB, torrent |
| Emboar | Puño Certero | Lucha | — | 50.2–59.0% | 2HKO | STAB |
| Incineroar | Desahogo | Siniestro | — | 25.4–29.8% | 29.8% | STAB |
| Blastoise | Chilling Water | Agua | — | 25.4–29.8% | 29.8% | STAB, torrent |
| Zoroark de Hisui | Hiperrayo | Normal | ×0.5 | 24.9–29.3% | 29.3% | STAB |
| Garchomp | Cometa Draco | Dragón | ×0.5 | 21.5–25.4% | 25.4% | STAB |
| Espathra | Psíquico | Psíquico | ×0.5 | 15.1–17.6% | 17.6% | STAB |
| Delphox | Psicorruido | Psíquico | ×0.5 | 12.7–14.6% | 14.6% | STAB |
| Dragonite | Vasto Impacto | Dragón | ×0.5 | 10.2–11.7% | 11.7% | STAB |
| Whimsicott | Rayo Solar | Planta | ×0.25 | 9.8–11.7% | 11.7% | STAB |
| Gengar | Tera Blast | Normal | ×0.5 | 8.8–10.7% | 10.7% | — |
| Slowking | Hidroariete | Agua | — | 1.0–1.5% | 1.5% | STAB |

### Dragonite (Dragon/Volador) — HP 198

- **Riesgo**: 1 OHKOs, 3 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Garchomp | Cometa Draco | Dragón | ×2 | 89.9–106.1% | **OHKO** | STAB |
| Zoroark de Hisui | Hiperrayo | Normal | — | 52.0–61.1% | 2HKO | STAB |
| Corviknight | Ataque Aéreo | Volador | — | 48.0–56.6% | 2HKO | STAB |
| Greninja | Hidrocañón | Agua | ×0.5 | 38.4–45.5% | 45.5% | STAB, torrent |
| Typhlosion de Hisui | Estallido | Fuego | ×0.5 | 38.4–45.5% | 45.5% | STAB, blaze |
| Espathra | Psíquico | Psíquico | — | 31.3–36.9% | 36.9% | STAB |
| Incineroar | Desahogo | Siniestro | — | 26.3–30.8% | 30.8% | STAB |
| Delphox | Psicorruido | Psíquico | — | 26.3–30.8% | 30.8% | STAB |
| Emboar | Puño Certero | Lucha | ×0.5 | 25.8–30.3% | 30.3% | STAB |
| Charizard | Cólera Ardiente | Fuego | ×0.5 | 19.2–22.7% | 22.7% | STAB, blaze |
| Gengar | Tera Blast | Normal | — | 18.7–22.2% | 22.2% | — |
| Slowking | Hidroariete | Agua | ×0.5 | 14.6–17.2% | 17.2% | STAB |
| Blastoise | Chilling Water | Agua | ×0.5 | 13.1–15.2% | 15.2% | STAB, torrent |
| Whimsicott | Rayo Solar | Planta | ×0.25 | 10.1–12.1% | 12.1% | STAB |

### Garchomp (Dragon/Tierra) — HP 215

- **Riesgo**: 0 OHKOs, 4 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Greninja | Hidrocañón | Agua | — | 71.2–83.7% | 2HKO | STAB, torrent |
| Emboar | Puño Certero | Lucha | — | 47.9–56.3% | 2HKO | STAB |
| Zoroark de Hisui | Hiperrayo | Normal | — | 47.9–56.3% | 2HKO | STAB |
| Corviknight | Ataque Aéreo | Volador | — | 44.2–52.1% | 2HKO | STAB |
| Dragonite | Vasto Impacto | Dragón | ×2 | 39.1–46.0% | 46.0% | STAB |
| Whimsicott | Rayo Solar | Planta | — | 38.1–45.1% | 45.1% | STAB |
| Typhlosion de Hisui | Estallido | Fuego | ×0.5 | 35.3–41.9% | 41.9% | STAB, blaze |
| Espathra | Psíquico | Psíquico | — | 28.8–34.0% | 34.0% | STAB |
| Slowking | Hidroariete | Agua | — | 27.0–32.1% | 32.1% | STAB |
| Incineroar | Desahogo | Siniestro | — | 24.2–28.4% | 28.4% | STAB |
| Blastoise | Chilling Water | Agua | — | 24.2–28.4% | 28.4% | STAB, torrent |
| Delphox | Psicorruido | Psíquico | — | 24.2–28.4% | 28.4% | STAB |
| Charizard | Cólera Ardiente | Fuego | ×0.5 | 17.7–20.9% | 20.9% | STAB, blaze |
| Gengar | Tera Blast | Normal | — | 17.2–20.5% | 20.5% | — |

### Slowking (Agua/Psiquico) — HP 202

- **Riesgo**: 0 OHKOs, 3 2HKOs, de 14 atacantes evaluados

| Atacante | Move | Tipo | Eff | % HP | KO | Notas |
|---|---|---|---|---|---|---|
| Incineroar | Desahogo | Siniestro | ×2 | 51.5–60.9% | 2HKO | STAB |
| Zoroark de Hisui | Hiperrayo | Normal | — | 51.0–59.9% | 2HKO | STAB |
| Corviknight | Ataque Aéreo | Volador | — | 47.0–55.4% | 2HKO | STAB |
| Greninja | Hidrocañón | Agua | ×0.5 | 37.6–44.6% | 44.6% | STAB, torrent |
| Typhlosion de Hisui | Estallido | Fuego | ×0.5 | 37.6–44.6% | 44.6% | STAB, blaze |
| Emboar | Puño Certero | Lucha | ×0.5 | 25.2–29.7% | 29.7% | STAB |
| Dragonite | Vasto Impacto | Dragón | — | 20.8–24.3% | 24.3% | STAB |
| Charizard | Cólera Ardiente | Fuego | ×0.5 | 18.8–22.3% | 22.3% | STAB, blaze |
| Gengar | Tera Blast | Normal | — | 18.3–21.8% | 21.8% | — |
| Espathra | Psíquico | Psíquico | ×0.5 | 15.3–17.8% | 17.8% | STAB |
| Blastoise | Chilling Water | Agua | ×0.5 | 12.9–14.9% | 14.9% | STAB, torrent |
| Delphox | Psicorruido | Psíquico | ×0.5 | 12.9–14.9% | 14.9% | STAB |
| Whimsicott | Rayo Solar | Planta | ×2 | 2.5–3.0% | 3.0% | STAB |
| Garchomp | Cometa Draco | Dragón | — | 1.0–1.5% | 1.5% | STAB |
