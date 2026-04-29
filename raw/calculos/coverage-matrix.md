# Coverage Matrix

Para cada Pokémon disponible: qué tipos defensivos puede pegar SE con su movepool y dónde tiene gaps.

Generado por `scripts/build_coverage_matrix.py` desde `raw/pokemon/*.md`, `raw/ataques/*.md`, `raw/tipos/*.md`.

## Resumen ranking SE coverage

| # | Pokémon | Tipos | Tipos SE | Sin efecto | Atacando con |
|---|---|---|---|---|---|
| 1 | Greninja | Agua/Siniestro | **18** | 0 | Agua, Bicho, Fantasma, Hielo, Lucha, Normal, Planta, Psiquico, Roca, Siniestro, Tierra, Veneno, Volador |
| 2 | Garchomp | Dragon/Tierra | **18** | 0 | Acero, Agua, Dragon, Electrico, Fantasma, Fuego, Lucha, Normal, Roca, Siniestro, Tierra, Veneno, Volador |
| 3 | Typhlosion de Hisui | Fuego/Fantasma | **18** | 0 | Acero, Electrico, Fantasma, Fuego, Hada, Lucha, Normal, Planta, Psiquico, Roca, Tierra, Volador |
| 4 | Emboar | Fuego/Lucha | **17** | 0 | Acero, Agua, Electrico, Fuego, Lucha, Normal, Planta, Psiquico, Roca, Siniestro, Tierra, Veneno |
| 5 | Zoroark de Hisui | Normal/Fantasma | **17** | 0 | Bicho, Fantasma, Fuego, Hielo, Lucha, Normal, Psiquico, Siniestro, Tierra, Veneno, Volador |
| 6 | Espathra | Psiquico | **16** | 0 | Acero, Bicho, Fantasma, Hada, Normal, Planta, Psiquico, Siniestro, Tierra, Volador |
| 7 | Dragonite | Dragon/Volador | **14** | 0 | Agua, Dragon, Hielo, Lucha, Normal, Tierra, Volador |
| 8 | Incineroar | Fuego/Siniestro | **12** | 0 | Fuego, Normal, Planta, Siniestro, Tierra |
| 9 | Corviknight | Volador/Acero | **11** | 0 | Acero, Bicho, Lucha, Normal, Siniestro, Volador |
| 10 | Whimsicott | Planta/Hada | **11** | 0 | Bicho, Fantasma, Hada, Normal, Planta, Psiquico, Siniestro, Volador |
| 11 | Charizard | Fuego/Volador | **10** | 0 | Dragon, Fuego, Normal, Tierra, Volador |
| 12 | Slowking | Agua/Psiquico | **8** | 0 | Agua, Dragon, Normal, Psiquico, Tierra |
| 13 | Blastoise | Agua | **3** | 0 | Agua |
| 14 | Gengar | Fantasma/Veneno | **2** | 0 | Normal, Psiquico |
| 15 | Delphox | Fuego/Psiquico | **2** | 0 | Normal, Psiquico |

## Detalle por Pokémon

### Greninja (Agua/Siniestro)

- **SE coverage** (18/18): Acero, Agua, Bicho, Dragon, Eléctrico, Fantasma, Fuego, Hada, Hielo, Lucha, Normal, Planta, Psiquico, Roca, Siniestro, Tierra, Veneno, Volador

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×2 | Demolición | Lucha | 75 |
| Fuego | ×2 | Hidrocañón | Agua | 150 |
| Agua | ×2 | Trailblaze | Planta | 50 |
| Eléctrico | ×2 | Excavar | Tierra | 80 |
| Planta | ×2 | Ventisca | Hielo | 110 |
| Hielo | ×2 | Avalancha | Roca | 75 |
| Lucha | ×2 | Paranormal | Psíquico | 80 |
| Veneno | ×2 | Excavar | Tierra | 80 |
| Tierra | ×2 | Ventisca | Hielo | 110 |
| Volador | ×2 | Ventisca | Hielo | 110 |
| Psiquico | ×2 | Sombra Vil | Fantasma | 40 |
| Bicho | ×2 | Avalancha | Roca | 75 |
| Roca | ×2 | Hidrocañón | Agua | 150 |
| Fantasma | ×2 | Sombra Vil | Fantasma | 40 |
| Dragon | ×2 | Ventisca | Hielo | 110 |
| Siniestro | ×2 | Demolición | Lucha | 75 |
| Acero | ×2 | Excavar | Tierra | 80 |
| Hada | ×2 | Lanzamugre | Veneno | 120 |

### Garchomp (Dragon/Tierra)

- **SE coverage** (18/18): Acero, Agua, Bicho, Dragon, Eléctrico, Fantasma, Fuego, Hada, Hielo, Lucha, Normal, Planta, Psiquico, Roca, Siniestro, Tierra, Veneno, Volador

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×2 | Demolición | Lucha | 75 |
| Fuego | ×2 | Surf | Agua | 90 |
| Agua | ×2 | Colmillo Rayo | Eléctrico | 65 |
| Eléctrico | ×2 | Terremoto | Tierra | 100 |
| Planta | ×2 | Llamarada | Fuego | 110 |
| Hielo | ×2 | Llamarada | Fuego | 110 |
| Lucha | ×2 | Golpe Aéreo | Volador | 60 |
| Veneno | ×2 | Terremoto | Tierra | 100 |
| Tierra | ×2 | Surf | Agua | 90 |
| Volador | ×2 | Roca Afilada | Roca | 100 |
| Psiquico | ×2 | Triturar | Siniestro | 80 |
| Bicho | ×2 | Llamarada | Fuego | 110 |
| Roca | ×2 | Surf | Agua | 90 |
| Fantasma | ×2 | Triturar | Siniestro | 80 |
| Dragon | ×2 | Cometa Draco | Dragón | 130 |
| Siniestro | ×2 | Demolición | Lucha | 75 |
| Acero | ×2 | Llamarada | Fuego | 110 |
| Hada | ×2 | Cola Férrea | Acero | 100 |

### Typhlosion de Hisui (Fuego/Fantasma)

- **SE coverage** (18/18): Acero, Agua, Bicho, Dragon, Eléctrico, Fantasma, Fuego, Hada, Hielo, Lucha, Normal, Planta, Psiquico, Roca, Siniestro, Tierra, Veneno, Volador

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×2 | Puño Certero | Lucha | 150 |
| Fuego | ×2 | Terremoto | Tierra | 100 |
| Agua | ×2 | Voltio Cruel | Eléctrico | 90 |
| Eléctrico | ×2 | Terremoto | Tierra | 100 |
| Planta | ×2 | Estallido | Fuego | 150 |
| Hielo | ×2 | Estallido | Fuego | 150 |
| Lucha | ×2 | Golpe Aéreo | Volador | 60 |
| Veneno | ×2 | Terremoto | Tierra | 100 |
| Tierra | ×2 | Rayo Solar | Planta | 120 |
| Volador | ×2 | Voltio Cruel | Eléctrico | 90 |
| Psiquico | ×2 | Poltergeist | Fantasma | 110 |
| Bicho | ×2 | Estallido | Fuego | 150 |
| Roca | ×2 | Rayo Solar | Planta | 120 |
| Fantasma | ×2 | Poltergeist | Fantasma | 110 |
| Dragon | ×2 | Carantoña | Hada | 90 |
| Siniestro | ×2 | Puño Certero | Lucha | 150 |
| Acero | ×2 | Estallido | Fuego | 150 |
| Hada | ×2 | Cola Férrea | Acero | 100 |

### Emboar (Fuego/Lucha)

- **SE coverage** (17/18): Acero, Agua, Bicho, Eléctrico, Fantasma, Fuego, Hada, Hielo, Lucha, Normal, Planta, Psiquico, Roca, Siniestro, Tierra, Veneno, Volador

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×2 | Puño Certero | Lucha | 150 |
| Fuego | ×2 | Terremoto | Tierra | 100 |
| Agua | ×2 | Voltio Cruel | Eléctrico | 90 |
| Eléctrico | ×2 | Terremoto | Tierra | 100 |
| Planta | ×2 | Anillo Ígneo | Fuego | 150 |
| Hielo | ×2 | Anillo Ígneo | Fuego | 150 |
| Lucha | ×2 | Cabezazo Zen | Psíquico | 80 |
| Veneno | ×2 | Terremoto | Tierra | 100 |
| Tierra | ×2 | Rayo Solar | Planta | 120 |
| Volador | ×2 | Voltio Cruel | Eléctrico | 90 |
| Psiquico | ×2 | Golpe Bajo | Siniestro | 70 |
| Bicho | ×2 | Anillo Ígneo | Fuego | 150 |
| Roca | ×2 | Rayo Solar | Planta | 120 |
| Fantasma | ×2 | Golpe Bajo | Siniestro | 70 |
| Dragon | ×1 | Hiperrayo | Normal | 150 |
| Siniestro | ×2 | Puño Certero | Lucha | 150 |
| Acero | ×2 | Anillo Ígneo | Fuego | 150 |
| Hada | ×2 | Puya Nociva | Veneno | 80 |

### Zoroark de Hisui (Normal/Fantasma)

- **SE coverage** (17/18): Acero, Bicho, Dragon, Eléctrico, Fantasma, Fuego, Hada, Hielo, Lucha, Normal, Planta, Psiquico, Roca, Siniestro, Tierra, Veneno, Volador

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×2 | Puño Certero | Lucha | 150 |
| Fuego | ×2 | Excavar | Tierra | 80 |
| Agua | ×1 | Hiperrayo | Normal | 150 |
| Eléctrico | ×2 | Excavar | Tierra | 80 |
| Planta | ×2 | Lanzallamas | Fuego | 90 |
| Hielo | ×2 | Lanzallamas | Fuego | 90 |
| Lucha | ×2 | Psíquico | Psíquico | 90 |
| Veneno | ×2 | Excavar | Tierra | 80 |
| Tierra | ×2 | Viento Hielo | Hielo | 55 |
| Volador | ×2 | Viento Hielo | Hielo | 55 |
| Psiquico | ×2 | Juego Sucio | Siniestro | 95 |
| Bicho | ×2 | Lanzallamas | Fuego | 90 |
| Roca | ×2 | Excavar | Tierra | 80 |
| Fantasma | ×2 | Juego Sucio | Siniestro | 95 |
| Dragon | ×2 | Viento Hielo | Hielo | 55 |
| Siniestro | ×2 | Puño Certero | Lucha | 150 |
| Acero | ×2 | Lanzallamas | Fuego | 90 |
| Hada | ×2 | Bomba Lodo | Veneno | 90 |

### Espathra (Psiquico)

- **SE coverage** (16/18): Acero, Agua, Bicho, Dragon, Eléctrico, Fantasma, Fuego, Hada, Hielo, Lucha, Planta, Psiquico, Roca, Siniestro, Tierra, Veneno

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×1 | Hiperrayo | Normal | 150 |
| Fuego | ×2 | Bofetón Lodo | Tierra | 20 |
| Agua | ×2 | Energibola | Planta | 90 |
| Eléctrico | ×2 | Bofetón Lodo | Tierra | 20 |
| Planta | ×2 | Pájaro Osado | Volador | 120 |
| Hielo | ×2 | Foco Resplandor | Acero | 80 |
| Lucha | ×2 | Psíquico | Psíquico | 90 |
| Veneno | ×2 | Psíquico | Psíquico | 90 |
| Tierra | ×2 | Energibola | Planta | 90 |
| Volador | ×1 | Hiperrayo | Normal | 150 |
| Psiquico | ×2 | Juego Sucio | Siniestro | 95 |
| Bicho | ×2 | Pájaro Osado | Volador | 120 |
| Roca | ×2 | Bofetón Lodo | Tierra | 20 |
| Fantasma | ×2 | Juego Sucio | Siniestro | 95 |
| Dragon | ×2 | Brillo Mágico | Hada | 80 |
| Siniestro | ×2 | Ida y Vuelta | Bicho | 70 |
| Acero | ×2 | Bofetón Lodo | Tierra | 20 |
| Hada | ×2 | Foco Resplandor | Acero | 80 |

### Dragonite (Dragon/Volador)

- **SE coverage** (14/18): Acero, Bicho, Dragon, Eléctrico, Fuego, Hielo, Lucha, Normal, Planta, Roca, Siniestro, Tierra, Veneno, Volador

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×2 | Plancha Corporal | Lucha | 80 |
| Fuego | ×2 | Pataleta | Tierra | 75 |
| Agua | ×1 | Pataleta | Tierra | 75 |
| Eléctrico | ×2 | Pataleta | Tierra | 75 |
| Planta | ×2 | Ala Bis | Volador | 40 |
| Hielo | ×2 | Plancha Corporal | Lucha | 80 |
| Lucha | ×2 | Ala Bis | Volador | 40 |
| Veneno | ×2 | Pataleta | Tierra | 75 |
| Tierra | ×2 | Ice Spinner | Hielo | 80 |
| Volador | ×2 | Ice Spinner | Hielo | 80 |
| Psiquico | ×1 | Pataleta | Tierra | 75 |
| Bicho | ×2 | Ala Bis | Volador | 40 |
| Roca | ×2 | Pataleta | Tierra | 75 |
| Fantasma | ×1 | Pataleta | Tierra | 75 |
| Dragon | ×2 | Vasto Impacto | Dragón | 60 |
| Siniestro | ×2 | Plancha Corporal | Lucha | 80 |
| Acero | ×2 | Pataleta | Tierra | 75 |
| Hada | ×1 | Pataleta | Tierra | 75 |

### Incineroar (Fuego/Siniestro)

- **SE coverage** (12/18): Acero, Agua, Bicho, Eléctrico, Fantasma, Fuego, Hielo, Planta, Psiquico, Roca, Tierra, Veneno

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×1 | Cólera Ardiente | Fuego | 75 |
| Fuego | ×2 | Arenas Ardientes | Tierra | 70 |
| Agua | ×2 | Trailblaze | Planta | 50 |
| Eléctrico | ×2 | Arenas Ardientes | Tierra | 70 |
| Planta | ×2 | Cólera Ardiente | Fuego | 75 |
| Hielo | ×2 | Cólera Ardiente | Fuego | 75 |
| Lucha | ×1 | Cólera Ardiente | Fuego | 75 |
| Veneno | ×2 | Arenas Ardientes | Tierra | 70 |
| Tierra | ×2 | Trailblaze | Planta | 50 |
| Volador | ×1 | Cólera Ardiente | Fuego | 75 |
| Psiquico | ×2 | Desahogo | Siniestro | 75 |
| Bicho | ×2 | Cólera Ardiente | Fuego | 75 |
| Roca | ×2 | Arenas Ardientes | Tierra | 70 |
| Fantasma | ×2 | Desahogo | Siniestro | 75 |
| Dragon | ×1 | Desahogo | Siniestro | 75 |
| Siniestro | ×1 | Cólera Ardiente | Fuego | 75 |
| Acero | ×2 | Cólera Ardiente | Fuego | 75 |
| Hada | ×1 | Cólera Ardiente | Fuego | 75 |

### Corviknight (Volador/Acero)

- **SE coverage** (11/18): Acero, Bicho, Fantasma, Hada, Hielo, Lucha, Normal, Planta, Psiquico, Roca, Siniestro

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×2 | Plancha Corporal | Lucha | 80 |
| Fuego | ×1 | Ataque Aéreo | Volador | 140 |
| Agua | ×1 | Ataque Aéreo | Volador | 140 |
| Eléctrico | ×1 | Hiperrayo | Normal | 150 |
| Planta | ×2 | Ataque Aéreo | Volador | 140 |
| Hielo | ×2 | Metaláser | Acero | 140 |
| Lucha | ×2 | Ataque Aéreo | Volador | 140 |
| Veneno | ×1 | Ataque Aéreo | Volador | 140 |
| Tierra | ×1 | Ataque Aéreo | Volador | 140 |
| Volador | ×1 | Ataque Aéreo | Volador | 140 |
| Psiquico | ×2 | Ladrón | Siniestro | 60 |
| Bicho | ×2 | Ataque Aéreo | Volador | 140 |
| Roca | ×2 | Metaláser | Acero | 140 |
| Fantasma | ×2 | Ladrón | Siniestro | 60 |
| Dragon | ×1 | Ataque Aéreo | Volador | 140 |
| Siniestro | ×2 | Plancha Corporal | Lucha | 80 |
| Acero | ×2 | Plancha Corporal | Lucha | 80 |
| Hada | ×2 | Metaláser | Acero | 140 |

### Whimsicott (Planta/Hada)

- **SE coverage** (11/18): Agua, Bicho, Dragon, Fantasma, Lucha, Planta, Psiquico, Roca, Siniestro, Tierra, Veneno

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×1 | Vendaval | Volador | 110 |
| Fuego | ×1 | Vendaval | Volador | 110 |
| Agua | ×2 | Rayo Solar | Planta | 120 |
| Eléctrico | ×1 | Hiperrayo | Normal | 150 |
| Planta | ×2 | Vendaval | Volador | 110 |
| Hielo | ×1 | Vendaval | Volador | 110 |
| Lucha | ×2 | Vendaval | Volador | 110 |
| Veneno | ×2 | Comesueños | Psíquico | 100 |
| Tierra | ×2 | Rayo Solar | Planta | 120 |
| Volador | ×1 | Vendaval | Volador | 110 |
| Psiquico | ×2 | Desarme | Siniestro | 65 |
| Bicho | ×2 | Vendaval | Volador | 110 |
| Roca | ×2 | Rayo Solar | Planta | 120 |
| Fantasma | ×2 | Desarme | Siniestro | 65 |
| Dragon | ×2 | Fuerza Lunar | Hada | 95 |
| Siniestro | ×2 | Ida y Vuelta | Bicho | 70 |
| Acero | ×1 | Desarme | Siniestro | 65 |
| Hada | ×1 | Vendaval | Volador | 110 |

### Charizard (Fuego/Volador)

- **SE coverage** (10/18): Acero, Bicho, Dragon, Eléctrico, Fuego, Hielo, Lucha, Planta, Roca, Veneno

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×1 | Vasto Impacto | Dragón | 60 |
| Fuego | ×2 | Arenas Ardientes | Tierra | 70 |
| Agua | ×1 | Vasto Impacto | Dragón | 60 |
| Eléctrico | ×2 | Arenas Ardientes | Tierra | 70 |
| Planta | ×2 | Ala Bis | Volador | 40 |
| Hielo | ×2 | Cólera Ardiente | Fuego | 75 |
| Lucha | ×2 | Ala Bis | Volador | 40 |
| Veneno | ×2 | Arenas Ardientes | Tierra | 70 |
| Tierra | ×1 | Vasto Impacto | Dragón | 60 |
| Volador | ×1 | Vasto Impacto | Dragón | 60 |
| Psiquico | ×1 | Vasto Impacto | Dragón | 60 |
| Bicho | ×2 | Ala Bis | Volador | 40 |
| Roca | ×2 | Arenas Ardientes | Tierra | 70 |
| Fantasma | ×1 | Vasto Impacto | Dragón | 60 |
| Dragon | ×2 | Vasto Impacto | Dragón | 60 |
| Siniestro | ×1 | Vasto Impacto | Dragón | 60 |
| Acero | ×2 | Arenas Ardientes | Tierra | 70 |
| Hada | ×1 | Ala Bis | Volador | 40 |

### Slowking (Agua/Psiquico)

- **SE coverage** (8/18): Acero, Dragon, Eléctrico, Fuego, Lucha, Roca, Tierra, Veneno

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×1 | Tera Blast | Normal | 80 |
| Fuego | ×2 | Hidroariete | Agua | 85 |
| Agua | ×1 | Tera Blast | Normal | 80 |
| Eléctrico | ×2 | Terratemblor | Tierra | 60 |
| Planta | ×1 | Tera Blast | Normal | 80 |
| Hielo | ×1 | Tera Blast | Normal | 80 |
| Lucha | ×2 | Vasta Fuerza | Psíquico | 80 |
| Veneno | ×2 | Vasta Fuerza | Psíquico | 80 |
| Tierra | ×2 | Hidroariete | Agua | 85 |
| Volador | ×1 | Tera Blast | Normal | 80 |
| Psiquico | ×1 | Tera Blast | Normal | 80 |
| Bicho | ×1 | Tera Blast | Normal | 80 |
| Roca | ×2 | Hidroariete | Agua | 85 |
| Fantasma | ×1 | Vasta Fuerza | Psíquico | 80 |
| Dragon | ×2 | Cola Dragón | Dragón | 60 |
| Siniestro | ×1 | Tera Blast | Normal | 80 |
| Acero | ×2 | Terratemblor | Tierra | 60 |
| Hada | ×1 | Tera Blast | Normal | 80 |

### Blastoise (Agua)

- **SE coverage** (3/18): Fuego, Roca, Tierra

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×1 | Chilling Water | Agua | 50 |
| Fuego | ×2 | Chilling Water | Agua | 50 |
| Agua | ×0.5 | Chilling Water | Agua | 50 |
| Eléctrico | ×1 | Chilling Water | Agua | 50 |
| Planta | ×0.5 | Chilling Water | Agua | 50 |
| Hielo | ×1 | Chilling Water | Agua | 50 |
| Lucha | ×1 | Chilling Water | Agua | 50 |
| Veneno | ×1 | Chilling Water | Agua | 50 |
| Tierra | ×2 | Chilling Water | Agua | 50 |
| Volador | ×1 | Chilling Water | Agua | 50 |
| Psiquico | ×1 | Chilling Water | Agua | 50 |
| Bicho | ×1 | Chilling Water | Agua | 50 |
| Roca | ×2 | Chilling Water | Agua | 50 |
| Fantasma | ×1 | Chilling Water | Agua | 50 |
| Dragon | ×0.5 | Chilling Water | Agua | 50 |
| Siniestro | ×1 | Chilling Water | Agua | 50 |
| Acero | ×1 | Chilling Water | Agua | 50 |
| Hada | ×1 | Chilling Water | Agua | 50 |

### Gengar (Fantasma/Veneno)

- **SE coverage** (2/18): Lucha, Veneno

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×1 | Tera Blast | Normal | 80 |
| Fuego | ×1 | Tera Blast | Normal | 80 |
| Agua | ×1 | Tera Blast | Normal | 80 |
| Eléctrico | ×1 | Tera Blast | Normal | 80 |
| Planta | ×1 | Tera Blast | Normal | 80 |
| Hielo | ×1 | Tera Blast | Normal | 80 |
| Lucha | ×2 | Psicorruido | Psíquico | 75 |
| Veneno | ×2 | Psicorruido | Psíquico | 75 |
| Tierra | ×1 | Tera Blast | Normal | 80 |
| Volador | ×1 | Tera Blast | Normal | 80 |
| Psiquico | ×1 | Tera Blast | Normal | 80 |
| Bicho | ×1 | Tera Blast | Normal | 80 |
| Roca | ×1 | Psicorruido | Psíquico | 75 |
| Fantasma | ×1 | Psicorruido | Psíquico | 75 |
| Dragon | ×1 | Tera Blast | Normal | 80 |
| Siniestro | ×1 | Tera Blast | Normal | 80 |
| Acero | ×0.5 | Tera Blast | Normal | 80 |
| Hada | ×1 | Tera Blast | Normal | 80 |

### Delphox (Fuego/Psiquico)

- **SE coverage** (2/18): Lucha, Veneno

| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |
|---|---|---|---|---|
| Normal | ×1 | Tera Blast | Normal | 80 |
| Fuego | ×1 | Tera Blast | Normal | 80 |
| Agua | ×1 | Tera Blast | Normal | 80 |
| Eléctrico | ×1 | Tera Blast | Normal | 80 |
| Planta | ×1 | Tera Blast | Normal | 80 |
| Hielo | ×1 | Tera Blast | Normal | 80 |
| Lucha | ×2 | Psicorruido | Psíquico | 75 |
| Veneno | ×2 | Psicorruido | Psíquico | 75 |
| Tierra | ×1 | Tera Blast | Normal | 80 |
| Volador | ×1 | Tera Blast | Normal | 80 |
| Psiquico | ×1 | Tera Blast | Normal | 80 |
| Bicho | ×1 | Tera Blast | Normal | 80 |
| Roca | ×1 | Psicorruido | Psíquico | 75 |
| Fantasma | ×1 | Psicorruido | Psíquico | 75 |
| Dragon | ×1 | Tera Blast | Normal | 80 |
| Siniestro | ×1 | Tera Blast | Normal | 80 |
| Acero | ×0.5 | Tera Blast | Normal | 80 |
| Hada | ×1 | Tera Blast | Normal | 80 |
