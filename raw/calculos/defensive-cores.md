# Defensive Cores

Pares de Pokémon disponibles ranqueados por **score defensivo conjunto**:

```
score = |resistencias compartidas| + |inmunidades del par| - 2 * |debilidades compartidas|
```

Score alto = los dos miembros se complementan: cubren las debilidades del otro y
comparten muchas resistencias / inmunidades.
Score bajo (negativo) = comparten debilidades = mal core defensivo.

Generado por `scripts/build_defensive_cores.py` desde `raw/pokemon/*.md` y `raw/tipos/*.md`.

## Top cores defensivos

| # | Core | Tipos | Score | Resists | Immune | Shared Weak |
|---|---|---|---|---|---|---|
| 1 | Corviknight + Typhlosion de Hisui | Volador/Acero + Fuego/Fantasma | **10** | 6 | 4 | 0 |
| 2 | Gengar + Corviknight | Fantasma/Veneno + Volador/Acero | **9** | 5 | 4 | 0 |
| 3 | Zoroark de Hisui + Corviknight | Normal/Fantasma + Volador/Acero | **8** | 3 | 5 | 0 |
| 4 | Charizard + Gengar | Fuego/Volador + Fantasma/Veneno | **7** | 4 | 3 | 0 |
| 5 | Incineroar + Corviknight | Fuego/Siniestro + Volador/Acero | **6** | 3 | 3 | 0 |
| 6 | Charizard + Zoroark de Hisui | Fuego/Volador + Normal/Fantasma | **6** | 2 | 4 | 0 |
| 7 | Gengar + Dragonite | Fantasma/Veneno + Dragon/Volador | **6** | 3 | 3 | 0 |
| 8 | Zoroark de Hisui + Dragonite | Normal/Fantasma + Dragon/Volador | **6** | 2 | 4 | 0 |
| 9 | Greninja + Typhlosion de Hisui | Agua/Siniestro + Fuego/Fantasma | **6** | 3 | 3 | 0 |
| 10 | Corviknight + Delphox | Volador/Acero + Fuego/Psiquico | **6** | 4 | 2 | 0 |
| 11 | Emboar + Greninja | Fuego/Lucha + Agua/Siniestro | **5** | 4 | 1 | 0 |
| 12 | Emboar + Corviknight | Fuego/Lucha + Volador/Acero | **5** | 3 | 2 | 0 |
| 13 | Incineroar + Zoroark de Hisui | Fuego/Siniestro + Normal/Fantasma | **5** | 1 | 4 | 0 |
| 14 | Incineroar + Greninja | Fuego/Siniestro + Agua/Siniestro | **5** | 6 | 1 | 1 |
| 15 | Incineroar + Slowking | Fuego/Siniestro + Agua/Psiquico | **5** | 4 | 1 | 0 |
| 16 | Charizard + Corviknight | Fuego/Volador + Volador/Acero | **5** | 5 | 2 | 1 |
| 17 | Charizard + Whimsicott | Fuego/Volador + Planta/Hada | **5** | 3 | 2 | 0 |
| 18 | Charizard + Typhlosion de Hisui | Fuego/Volador + Fuego/Fantasma | **5** | 6 | 3 | 2 |
| 19 | Gengar + Zoroark de Hisui | Fantasma/Veneno + Normal/Fantasma | **5** | 4 | 3 | 1 |
| 20 | Gengar + Whimsicott | Fantasma/Veneno + Planta/Hada | **5** | 2 | 3 | 0 |

## Detalle top 10

### 1. Corviknight (Volador/Acero) + Typhlosion de Hisui (Fuego/Fantasma) — score 10

- **Resistencias compartidas** (6): Acero, Bicho, Hada, Normal, Planta, Veneno
- **Inmunidades en el par** (4): Lucha, Normal, Tierra, Veneno
- **Debilidades compartidas** (0): _ninguna ✅_

### 2. Gengar (Fantasma/Veneno) + Corviknight (Volador/Acero) — score 9

- **Resistencias compartidas** (5): Bicho, Hada, Normal, Planta, Veneno
- **Inmunidades en el par** (4): Lucha, Normal, Tierra, Veneno
- **Debilidades compartidas** (0): _ninguna ✅_

### 3. Zoroark de Hisui (Normal/Fantasma) + Corviknight (Volador/Acero) — score 8

- **Resistencias compartidas** (3): Bicho, Normal, Veneno
- **Inmunidades en el par** (5): Fantasma, Lucha, Normal, Tierra, Veneno
- **Debilidades compartidas** (0): _ninguna ✅_

### 4. Charizard (Fuego/Volador) + Gengar (Fantasma/Veneno) — score 7

- **Resistencias compartidas** (4): Bicho, Hada, Lucha, Planta
- **Inmunidades en el par** (3): Lucha, Normal, Tierra
- **Debilidades compartidas** (0): _ninguna ✅_

### 5. Incineroar (Fuego/Siniestro) + Corviknight (Volador/Acero) — score 6

- **Resistencias compartidas** (3): Acero, Planta, Psiquico
- **Inmunidades en el par** (3): Psiquico, Tierra, Veneno
- **Debilidades compartidas** (0): _ninguna ✅_

### 6. Charizard (Fuego/Volador) + Zoroark de Hisui (Normal/Fantasma) — score 6

- **Resistencias compartidas** (2): Bicho, Lucha
- **Inmunidades en el par** (4): Fantasma, Lucha, Normal, Tierra
- **Debilidades compartidas** (0): _ninguna ✅_

### 7. Gengar (Fantasma/Veneno) + Dragonite (Dragon/Volador) — score 6

- **Resistencias compartidas** (3): Bicho, Lucha, Planta
- **Inmunidades en el par** (3): Lucha, Normal, Tierra
- **Debilidades compartidas** (0): _ninguna ✅_

### 8. Zoroark de Hisui (Normal/Fantasma) + Dragonite (Dragon/Volador) — score 6

- **Resistencias compartidas** (2): Bicho, Lucha
- **Inmunidades en el par** (4): Fantasma, Lucha, Normal, Tierra
- **Debilidades compartidas** (0): _ninguna ✅_

### 9. Greninja (Agua/Siniestro) + Typhlosion de Hisui (Fuego/Fantasma) — score 6

- **Resistencias compartidas** (3): Acero, Fuego, Hielo
- **Inmunidades en el par** (3): Lucha, Normal, Psiquico
- **Debilidades compartidas** (0): _ninguna ✅_

### 10. Corviknight (Volador/Acero) + Delphox (Fuego/Psiquico) — score 6

- **Resistencias compartidas** (4): Acero, Hada, Planta, Psiquico
- **Inmunidades en el par** (2): Tierra, Veneno
- **Debilidades compartidas** (0): _ninguna ✅_


## Anti-cores (peores combinaciones)

| # | Core | Tipos | Score | Shared Weak |
|---|---|---|---|---|
| 1 | Espathra + Slowking | Psiquico + Agua/Psiquico | **-4** | Bicho, Fantasma, Siniestro |
| 2 | Dragonite + Garchomp | Dragon/Volador + Dragon/Tierra | **-3** | Dragon, Hada, Hielo |
| 3 | Delphox + Typhlosion de Hisui | Fuego/Psiquico + Fuego/Fantasma | **-2** | Agua, Fantasma, Roca, Siniestro, Tierra |
| 4 | Espathra + Delphox | Psiquico + Fuego/Psiquico | **-2** | Fantasma, Siniestro |
| 5 | Gengar + Delphox | Fantasma/Veneno + Fuego/Psiquico | **-1** | Fantasma, Siniestro, Tierra |
| 6 | Gengar + Slowking | Fantasma/Veneno + Agua/Psiquico | **-1** | Fantasma, Siniestro |
| 7 | Espathra + Typhlosion de Hisui | Psiquico + Fuego/Fantasma | **-1** | Fantasma, Siniestro |
| 8 | Espathra + Gengar | Psiquico + Fantasma/Veneno | **-1** | Fantasma, Siniestro |
| 9 | Blastoise + Slowking | Agua + Agua/Psiquico | **0** | Eléctrico, Planta |
| 10 | Greninja + Slowking | Agua/Siniestro + Agua/Psiquico | **0** | Bicho, Eléctrico, Planta |