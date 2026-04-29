# Naturalezas — Pokémon Champions

25 naturalezas extraídas del bundle de op.gg/calculator. Mismo conjunto que juegos clásicos.

- **Neutrales** (5): no afectan stats
- **Stat-boosting** (20): +10% a una stat, -10% a otra

Multiplicador: 1.1 (incrementada) / 0.9 (decreased) / 1.0 (resto).
HP nunca se ve afectado por naturaleza.

## Tabla completa

| Clave EN | Nombre ES | +Stat | -Stat |
|---|---|---|---|
| `hardy`    | Fuerte   | — | — |
| `docile`   | Dócil    | — | — |
| `serious`  | Seria    | — | — |
| `bashful`  | Tímida   | — | — |
| `quirky`   | Rara     | — | — |
| `lonely`   | Huraña   | Atk | Def |
| `brave`    | Audaz    | Atk | Spe |
| `adamant`  | Firme    | Atk | SpA |
| `naughty`  | Pícara   | Atk | SpD |
| `bold`     | Osada    | Def | Atk |
| `relaxed`  | Plácida  | Def | Spe |
| `impish`   | Agitada  | Def | SpA |
| `lax`      | Floja    | Def | SpD |
| `modest`   | Modesta  | SpA | Atk |
| `mild`     | Afable   | SpA | Def |
| `quiet`    | Mansa    | SpA | Spe |
| `rash`     | Alocada  | SpA | SpD |
| `calm`     | Serena   | SpD | Atk |
| `gentle`   | Amable   | SpD | Def |
| `sassy`    | Grosera  | SpD | Spe |
| `careful`  | Cauta    | SpD | Atk |
| `timid`    | Miedosa  | Spe | Atk |
| `hasty`    | Activa   | Spe | Def |
| `jolly`    | Alegre   | Spe | SpA |
| `naive`    | Ingenua  | Spe | SpD |

## JSON estructurado

```json
[
  {"key": "hardy",   "name_es": "Fuerte",   "increased": null,        "decreased": null},
  {"key": "docile",  "name_es": "Dócil",    "increased": null,        "decreased": null},
  {"key": "serious", "name_es": "Seria",    "increased": null,        "decreased": null},
  {"key": "bashful", "name_es": "Tímida",   "increased": null,        "decreased": null},
  {"key": "quirky",  "name_es": "Rara",     "increased": null,        "decreased": null},
  {"key": "lonely",  "name_es": "Huraña",   "increased": "attack",    "decreased": "defense"},
  {"key": "brave",   "name_es": "Audaz",    "increased": "attack",    "decreased": "speed"},
  {"key": "adamant", "name_es": "Firme",    "increased": "attack",    "decreased": "spAttack"},
  {"key": "naughty", "name_es": "Pícara",   "increased": "attack",    "decreased": "spDefense"},
  {"key": "bold",    "name_es": "Osada",    "increased": "defense",   "decreased": "attack"},
  {"key": "relaxed", "name_es": "Plácida",  "increased": "defense",   "decreased": "speed"},
  {"key": "impish",  "name_es": "Agitada",  "increased": "defense",   "decreased": "spAttack"},
  {"key": "lax",     "name_es": "Floja",    "increased": "defense",   "decreased": "spDefense"},
  {"key": "modest",  "name_es": "Modesta",  "increased": "spAttack",  "decreased": "attack"},
  {"key": "mild",    "name_es": "Afable",   "increased": "spAttack",  "decreased": "defense"},
  {"key": "quiet",   "name_es": "Mansa",    "increased": "spAttack",  "decreased": "speed"},
  {"key": "rash",    "name_es": "Alocada",  "increased": "spAttack",  "decreased": "spDefense"},
  {"key": "calm",    "name_es": "Serena",   "increased": "spDefense", "decreased": "attack"},
  {"key": "gentle",  "name_es": "Amable",   "increased": "spDefense", "decreased": "defense"},
  {"key": "sassy",   "name_es": "Grosera",  "increased": "spDefense", "decreased": "speed"},
  {"key": "careful", "name_es": "Cauta",    "increased": "spDefense", "decreased": "attack"},
  {"key": "timid",   "name_es": "Miedosa",  "increased": "speed",     "decreased": "attack"},
  {"key": "hasty",   "name_es": "Activa",   "increased": "speed",     "decreased": "defense"},
  {"key": "jolly",   "name_es": "Alegre",   "increased": "speed",     "decreased": "spAttack"},
  {"key": "naive",   "name_es": "Ingenua",  "increased": "speed",     "decreased": "spDefense"}
]
```

## Naturalezas más usadas en VGC

| Naturaleza | Cuándo usar |
|---|---|
| **Modesta** (+SpA -Atk) | Atacante especial puro sin Foul Play en su contra |
| **Tímida** (+Spe -Atk) | Atacante especial que necesita superar a Garchomp/Dragapult |
| **Firme** (+Atk -SpA) | Atacante físico puro (la mayoría) |
| **Alegre** (+Spe -SpA) | Atacante físico que necesita velocidad (sin Foul Play preocupante) |
| **Osada** (+Def -Atk) | Wall físico que no usa Atk (Toxapex, Cresselia, Amoonguss) |
| **Cauta** (+SpD -SpA) | Wall especial físico-atacante (Tyranitar, Heatran físico) |
| **Audaz** (+Atk -Spe) | Trick Room atacante físico |
| **Mansa** (+SpA -Spe) | Trick Room atacante especial |

## Notas

- En el bundle, los stats internos son: `attack`, `defense`, `spAttack`, `spDefense`, `speed`. HP nunca aparece como `increased`/`decreased`.
- Las 5 naturalezas neutrales son intercambiables en gameplay (efecto idéntico). Diferencia solo cosmética y para cumplimiento de "naturaleza preferida" en algunos eventos.
- Los nombres ES están tomados de la UI oficial en español de op.gg, alineados con la traducción de Game Freak.
