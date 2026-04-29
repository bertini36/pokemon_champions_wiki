#!/usr/bin/env python3
"""Coverage matrix generator for Pokemon Champions.

For each available Pokémon, lists:
- Tipos que cubre con SE en su movepool (ataques disponibles)
- Tipos que NO cubre (gaps)
- Movimiento por tipo en su movepool (mejor BP)

Outputs:
- raw/calculos/coverage-matrix.json
- raw/calculos/coverage-matrix.md
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POKEMON_DIR = ROOT / "raw" / "pokemon"
MOVES_DIR = ROOT / "raw" / "ataques"
TYPES_DIR = ROOT / "raw" / "tipos"
OUTPUT_DIR = ROOT / "raw" / "calculos"

ALL_TYPES_ES = [
    "Normal", "Fuego", "Agua", "Eléctrico", "Planta", "Hielo",
    "Lucha", "Veneno", "Tierra", "Volador", "Psiquico", "Bicho",
    "Roca", "Fantasma", "Dragon", "Siniestro", "Acero", "Hada",
]

FIELD_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$")


def normalize(t: str) -> str:
    return unicodedata.normalize("NFD", t).encode("ascii", "ignore").decode()


def parse_md_table(md_path: Path) -> tuple[str | None, dict[str, str]]:
    title = None
    fields: dict[str, str] = {}
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
        m = FIELD_RE.match(line)
        if m:
            fields[m.group(1)] = m.group(2)
    return title, fields


def parse_movepool(md_path: Path) -> list[str]:
    moves = []
    in_section = False
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Movimientos"):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section and line.startswith("|") and not line.startswith("|---") and not line.startswith("| #"):
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) >= 2 and parts[0].isdigit():
                moves.append(parts[1])
    return moves


def parse_pokemon(md_path: Path) -> dict | None:
    title, fields = parse_md_table(md_path)
    if not fields.get("Velocidad", "").isdigit():
        return None
    return {
        "name": title or md_path.stem,
        "type1": fields.get("Tipo 1", ""),
        "type2": fields.get("Tipo 2", "-"),
        "available": fields.get("Disponible", "") == "Sí",
        "moves": parse_movepool(md_path),
    }


def parse_move(md_path: Path) -> dict | None:
    title, fields = parse_md_table(md_path)
    cat_es = fields.get("Categoría", "")
    power_str = fields.get("Potencia", "-")
    if cat_es == "Estado" or not power_str.isdigit():
        return None
    return {
        "name": title,
        "type": fields.get("Tipo", ""),
        "category": "physical" if cat_es == "Físico" else "special",
        "power": int(power_str),
    }


def parse_type_chart() -> dict[str, dict[str, float]]:
    chart: dict[str, dict[str, float]] = {}
    for tipo_file in TYPES_DIR.glob("*.md"):
        if tipo_file.name.startswith("_"):
            continue
        atk_type = normalize(tipo_file.stem.capitalize())
        chart[atk_type] = {dt: 1.0 for dt in ALL_TYPES_ES}
        in_atk = False
        for line in tipo_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("## Atacando"):
                in_atk = True
                continue
            if in_atk and line.startswith("## "):
                break
            if in_atk and "|" in line:
                if "Súper" in line or "Superefic" in line:
                    mult = 2.0
                elif "Poco" in line:
                    mult = 0.5
                elif "Sin efecto" in line:
                    mult = 0.0
                else:
                    continue
                for tipo in re.findall(r"\[\[([^\]]+)\]\]", line):
                    chart[atk_type][normalize(tipo)] = mult
    return chart


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pokemons = []
    for f in POKEMON_DIR.glob("*.md"):
        if f.name.startswith("_"):
            continue
        p = parse_pokemon(f)
        if p:
            pokemons.append(p)

    moves_by_name = {}
    for f in MOVES_DIR.glob("*.md"):
        if f.name.startswith("_"):
            continue
        m = parse_move(f)
        if m:
            moves_by_name[m["name"]] = m

    chart = parse_type_chart()
    available = [p for p in pokemons if p["available"]]
    print(f"Parsed {len(pokemons)} Pokémon ({len(available)} disponibles), {len(moves_by_name)} moves")

    matrix = []
    for poke in available:
        # Best move per attacking type
        best_per_type: dict[str, dict] = {}
        for move_name in poke["moves"]:
            m = moves_by_name.get(move_name)
            if not m:
                continue
            mtype = normalize(m["type"])
            cur = best_per_type.get(mtype)
            if not cur or m["power"] > cur["power"]:
                best_per_type[mtype] = m

        # Coverage: for each defender type, find best multiplier achievable
        coverage: dict[str, dict] = {}
        for def_type in ALL_TYPES_ES:
            def_norm = normalize(def_type)
            best_mult = 0.0
            best_move = None
            for atk_type, m in best_per_type.items():
                mult = chart.get(atk_type, {}).get(def_norm, 1.0)
                if mult > best_mult:
                    best_mult = mult
                    best_move = m
            coverage[def_type] = {
                "best_mult": best_mult,
                "best_move": best_move["name"] if best_move else None,
                "best_move_type": best_move["type"] if best_move else None,
                "best_move_power": best_move["power"] if best_move else 0,
            }

        se_types = [t for t, c in coverage.items() if c["best_mult"] >= 2]
        nve_or_neutral = [t for t, c in coverage.items() if 0 < c["best_mult"] < 2]
        no_effect_types = [t for t, c in coverage.items() if c["best_mult"] == 0]

        matrix.append({
            "name": poke["name"],
            "type1": poke["type1"],
            "type2": poke["type2"],
            "movepool_attacking_types": sorted(best_per_type.keys()),
            "coverage": coverage,
            "se_types": sorted(se_types),
            "nve_or_neutral_types": sorted(nve_or_neutral),
            "no_effect_types": sorted(no_effect_types),
            "se_count": len(se_types),
            "no_effect_count": len(no_effect_types),
        })

    matrix.sort(key=lambda r: -r["se_count"])

    json_path = OUTPUT_DIR / "coverage-matrix.json"
    json_path.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        "# Coverage Matrix",
        "",
        "Para cada Pokémon disponible: qué tipos defensivos puede pegar SE con su movepool y dónde tiene gaps.",
        "",
        "Generado por `scripts/build_coverage_matrix.py` desde `raw/pokemon/*.md`, `raw/ataques/*.md`, `raw/tipos/*.md`.",
        "",
        "## Resumen ranking SE coverage",
        "",
        "| # | Pokémon | Tipos | Tipos SE | Sin efecto | Atacando con |",
        "|---|---|---|---|---|---|",
    ]
    for i, row in enumerate(matrix, start=1):
        types = row["type1"] if row["type2"] in ("-", "") else f"{row['type1']}/{row['type2']}"
        attacking = ", ".join(row["movepool_attacking_types"])
        md_lines.append(
            f"| {i} | {row['name']} | {types} | **{row['se_count']}** "
            f"| {row['no_effect_count']} | {attacking} |"
        )

    md_lines.extend(["", "## Detalle por Pokémon", ""])
    for row in matrix:
        types = row["type1"] if row["type2"] in ("-", "") else f"{row['type1']}/{row['type2']}"
        md_lines.append(f"### {row['name']} ({types})")
        md_lines.append("")
        if row["se_types"]:
            md_lines.append(f"- **SE coverage** ({row['se_count']}/18): " + ", ".join(row["se_types"]))
        else:
            md_lines.append("- **SE coverage**: ninguno")
        if row["no_effect_types"]:
            md_lines.append(f"- **Sin efecto contra**: " + ", ".join(row["no_effect_types"]))
        md_lines.append("")
        md_lines.append("| Tipo defensor | Mejor mult | Movimiento | Tipo move | BP |")
        md_lines.append("|---|---|---|---|---|")
        for def_type in ALL_TYPES_ES:
            c = row["coverage"][def_type]
            mult_label = f"×{c['best_mult']:g}"
            move_label = c["best_move"] or "—"
            mt_label = c["best_move_type"] or "—"
            bp_label = c["best_move_power"] or "—"
            md_lines.append(f"| {def_type} | {mult_label} | {move_label} | {mt_label} | {bp_label} |")
        md_lines.append("")

    md_path = OUTPUT_DIR / "coverage-matrix.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"  → {json_path.relative_to(ROOT)}")
    print(f"  → {md_path.relative_to(ROOT)}")
    print("\nTop 3 SE coverage:")
    for r in matrix[:3]:
        print(f"  {r['name']:25s}  SE={r['se_count']:2d}  ataca con={','.join(r['movepool_attacking_types'])}")


if __name__ == "__main__":
    main()
