#!/usr/bin/env python3
"""Speed vs Pañuelo Elección cross table for Pokemon Champions.

For each available Pokémon, lists who outspeeds them in three regimes:
- Bare (0 PH, neutral nature)
- Optimized (32 PH Spe + +Spe nature)
- Scarfed (32 PH Spe + +Spe nature + Pañuelo Elección ×1.5)

Outputs:
- raw/calculos/speed-vs-scarf.json
- raw/calculos/speed-vs-scarf.md
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

LEVEL = 50
IV = 31
AP_TO_EV_RATIO = 7.875
MAX_STAT_AP = 32
SCARF_MULT = 1.5

ROOT = Path(__file__).resolve().parent.parent
POKEMON_DIR = ROOT / "raw" / "pokemon"
OUTPUT_DIR = ROOT / "raw" / "calculos"

FIELD_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$")


def calc_speed(base: int, ap: int, nature_mult: float) -> int:
    ev = math.floor(ap * AP_TO_EV_RATIO)
    raw = math.floor((2 * base + IV + math.floor(ev / 4)) * LEVEL / 100) + 5
    return math.floor(raw * nature_mult)


def parse_pokemon(md_path: Path) -> dict | None:
    title = None
    fields: dict[str, str] = {}
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
        m = FIELD_RE.match(line)
        if m:
            fields[m.group(1)] = m.group(2)
    if not fields.get("Velocidad", "").isdigit():
        return None
    return {
        "name": title or md_path.stem,
        "type1": fields.get("Tipo 1", ""),
        "type2": fields.get("Tipo 2", "-"),
        "available": fields.get("Disponible", "") == "Sí",
        "base_speed": int(fields["Velocidad"]),
    }


def speed_regimes(base: int) -> dict[str, int]:
    optimized = calc_speed(base, MAX_STAT_AP, 1.1)
    return {
        "bare":      calc_speed(base, 0, 1.0),
        "optimized": optimized,
        "scarfed":   math.floor(optimized * SCARF_MULT),
    }


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pokemons = []
    for f in POKEMON_DIR.glob("*.md"):
        if f.name.startswith("_"):
            continue
        p = parse_pokemon(f)
        if p:
            pokemons.append(p)

    available = [p for p in pokemons if p["available"]]
    print(f"Parsed {len(pokemons)} Pokémon ({len(available)} disponibles)")

    for p in available:
        p["speeds"] = speed_regimes(p["base_speed"])

    matrix = []
    for me in available:
        my_opt = me["speeds"]["optimized"]
        my_scarf = me["speeds"]["scarfed"]
        outspeeds_me_opt = []
        scarf_check_against_opt = []
        scarf_check_against_scarf = []
        for other in available:
            if other["name"] == me["name"]:
                continue
            other_opt = other["speeds"]["optimized"]
            other_scarf = other["speeds"]["scarfed"]
            if other_opt > my_opt:
                outspeeds_me_opt.append({
                    "name": other["name"],
                    "speed": other_opt,
                    "delta": other_opt - my_opt,
                })
            if other_scarf > my_opt:
                scarf_check_against_opt.append({
                    "name": other["name"],
                    "speed": other_scarf,
                    "delta": other_scarf - my_opt,
                })
            if other_scarf > my_scarf:
                scarf_check_against_scarf.append({
                    "name": other["name"],
                    "speed": other_scarf,
                    "delta": other_scarf - my_scarf,
                })
        outspeeds_me_opt.sort(key=lambda r: -r["speed"])
        scarf_check_against_opt.sort(key=lambda r: -r["speed"])
        scarf_check_against_scarf.sort(key=lambda r: -r["speed"])
        matrix.append({
            "name": me["name"],
            "type1": me["type1"],
            "type2": me["type2"],
            "base_speed": me["base_speed"],
            "speeds": me["speeds"],
            "outspeeds_me_opt_vs_opt": outspeeds_me_opt,
            "outspeeds_me_scarf_vs_opt": scarf_check_against_opt,
            "outspeeds_me_scarf_vs_scarf": scarf_check_against_scarf,
        })

    matrix.sort(key=lambda r: -r["speeds"]["optimized"])

    json_path = OUTPUT_DIR / "speed-vs-scarf.json"
    json_path.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        "# Speed vs Pañuelo Elección — Nv.50",
        "",
        "Análisis cruzado de velocidad para los Pokémon disponibles. Cada entrada lista:",
        "",
        "- Quién supera tu velocidad **optimizada** (32 PH Spe + +Spe naturaleza, sin Pañuelo)",
        "- Quién supera tu velocidad optimizada **si te ponen Pañuelo Elección** (Spe × 1.5)",
        "- Quién te supera **si tú también llevas Pañuelo**",
        "",
        "Pañuelo Elección multiplica Spe ×1.5 pero **bloquea al Pokémon en un único movimiento**.",
        "",
        "Generado por `scripts/build_speed_vs_scarf.py` desde `raw/pokemon/*.md`.",
        "",
        "## Tier global de velocidad (con/sin Pañuelo)",
        "",
        "| # | Pokémon | Tipos | Base Spe | Sin PH | Optimizada | Con Pañuelo |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, row in enumerate(matrix, start=1):
        types = row["type1"] if row["type2"] in ("-", "") else f"{row['type1']}/{row['type2']}"
        s = row["speeds"]
        md_lines.append(
            f"| {i} | {row['name']} | {types} | {row['base_speed']} | "
            f"{s['bare']} | {s['optimized']} | **{s['scarfed']}** |"
        )

    md_lines.extend([
        "",
        "## Análisis por Pokémon",
        "",
    ])
    for row in matrix:
        types = row["type1"] if row["type2"] in ("-", "") else f"{row['type1']}/{row['type2']}"
        s = row["speeds"]
        md_lines.append(f"### {row['name']} ({types})")
        md_lines.append("")
        md_lines.append(
            f"- **Base Spe**: {row['base_speed']} | **Optimizada**: {s['optimized']} | "
            f"**Con Pañuelo**: {s['scarfed']}"
        )
        md_lines.append("")
        md_lines.append("**Quién supera tu Spe optimizada (sin Pañuelo)**:")
        if row["outspeeds_me_opt_vs_opt"]:
            for r in row["outspeeds_me_opt_vs_opt"]:
                md_lines.append(f"- {r['name']} ({r['speed']}, +{r['delta']})")
        else:
            md_lines.append("- _Nadie. Eres el Pokémon más rápido del meta sin Pañuelo._")
        md_lines.append("")
        md_lines.append("**Quién te supera con Pañuelo (vs tu Spe optimizada)**:")
        if row["outspeeds_me_scarf_vs_opt"]:
            for r in row["outspeeds_me_scarf_vs_opt"]:
                md_lines.append(f"- {r['name']} (Pañuelo: {r['speed']}, +{r['delta']})")
        else:
            md_lines.append("- _Ningún Pokémon disponible te supera ni con Pañuelo._")
        md_lines.append("")
        md_lines.append("**Quién te supera si ambos lleváis Pañuelo**:")
        if row["outspeeds_me_scarf_vs_scarf"]:
            for r in row["outspeeds_me_scarf_vs_scarf"]:
                md_lines.append(f"- {r['name']} (Pañuelo: {r['speed']}, +{r['delta']})")
        else:
            md_lines.append("- _Nadie. Tu Pañuelo te asegura el primer turno._")
        md_lines.append("")

    md_lines.extend([
        "## Notas",
        "",
        "- Empates de velocidad se resuelven aleatoriamente turno a turno.",
        "- Bonus de velocidad por habilidades (Cuerpo Veloz, Velocidad Extrema, etc.) NO modelados.",
        "- Modos especiales que invierten orden (Trick Room) NO modelados.",
        "- Boost por Bromuro (+2 Spe) o Cambio de Marcha (+2 Spe) se aplica encima de la columna Optimizada.",
        "- Para usar bien Pañuelo: lockea en 1 movimiento. Mejor con atacantes con 1 STAB dominante (Cólera Ardiente, Hiperrayo, Garra Dragón).",
        "",
    ])

    md_path = OUTPUT_DIR / "speed-vs-scarf.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"  → {json_path.relative_to(ROOT)}")
    print(f"  → {md_path.relative_to(ROOT)}")
    print(f"\nTier global ordenado por Spe optimizada — top 3:")
    for r in matrix[:3]:
        s = r["speeds"]
        print(f"  {r['name']:25s}  opt={s['optimized']:3d}  scarf={s['scarfed']:3d}")


if __name__ == "__main__":
    main()
