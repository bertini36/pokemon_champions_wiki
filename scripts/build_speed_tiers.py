#!/usr/bin/env python3
"""Speed tier table generator for Pokemon Champions.

Reads raw/pokemon/*.md, extracts base speed, computes final Spe at L50
with three scenarios (max+nature, max neutral, 0 PH), outputs:
- raw/calculos/speed-tiers-l50.json
- raw/calculos/speed-tiers-l50.md
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

ROOT = Path(__file__).resolve().parent.parent
POKEMON_DIR = ROOT / "raw" / "pokemon"
OUTPUT_DIR = ROOT / "raw" / "calculos"


def calc_speed(base: int, ap: int, nature_mult: float) -> int:
    ev = math.floor(ap * AP_TO_EV_RATIO)
    raw = math.floor((2 * base + IV + math.floor(ev / 4)) * LEVEL / 100) + 5
    return math.floor(raw * nature_mult)


FIELD_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$")


def parse_pokemon(md_path: Path) -> dict | None:
    title = None
    fields: dict[str, str] = {}
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
        m = FIELD_RE.match(line)
        if m:
            fields[m.group(1)] = m.group(2)

    base_speed = fields.get("Velocidad")
    if not base_speed or not base_speed.isdigit():
        return None

    return {
        "name": title or md_path.stem,
        "slug": fields.get("Slug (en)", md_path.stem),
        "type1": fields.get("Tipo 1", ""),
        "type2": fields.get("Tipo 2", "-"),
        "available": fields.get("Disponible", "") == "Sí",
        "base_speed": int(base_speed),
    }


def build_tiers() -> list[dict]:
    rows = []
    for md_path in sorted(POKEMON_DIR.glob("*.md")):
        if md_path.name.startswith("_"):
            continue
        data = parse_pokemon(md_path)
        if not data:
            continue
        base = data["base_speed"]
        rows.append({
            **data,
            "spe_max_nature": calc_speed(base, MAX_STAT_AP, 1.1),
            "spe_max_neutral": calc_speed(base, MAX_STAT_AP, 1.0),
            "spe_min_neg_nature": calc_speed(base, 0, 0.9),
            "spe_zero_neutral": calc_speed(base, 0, 1.0),
        })
    rows.sort(key=lambda r: (-r["spe_max_nature"], r["name"]))
    return rows


def write_json(rows: list[dict]) -> Path:
    path = OUTPUT_DIR / "speed-tiers-l50.json"
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def write_markdown(rows: list[dict]) -> Path:
    path = OUTPUT_DIR / "speed-tiers-l50.md"
    lines = [
        "# Speed Tiers — Nv.50",
        "",
        "Velocidad final de cada Pokémon a Nivel 50 según escenario de PH y naturaleza.",
        "",
        "Generado por `scripts/build_speed_tiers.py` desde `raw/pokemon/*.md` + constantes",
        "de `raw/mecanicas/formula-stats.md`.",
        "",
        "## Escenarios",
        "",
        "| Columna | PH Spe | Naturaleza | Multiplicador |",
        "|---|---|---|---|",
        "| **Spe (+Nat)** | 32 | +Spe (Tímida/Alegre/Ingenua/Activa/Miedosa) | 1.1 |",
        "| Spe (Neutral) | 32 | Neutral | 1.0 |",
        "| Spe (0 PH) | 0 | Neutral | 1.0 |",
        "| Spe (-Nat) | 0 | -Spe (Audaz/Plácida/Mansa/Grosera/Serena) | 0.9 |",
        "",
        "Ordenado por **Spe (+Nat)** descendente. Solo Pokémon disponibles en el juego.",
        "",
        "## Tabla",
        "",
        "| # | Pokémon | Tipos | Base Spe | Spe (+Nat) | Spe (Neutral) | Spe (0 PH) | Spe (-Nat) |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate([row for row in rows if row["available"]], start=1):
        types = r["type1"] if r["type2"] in ("-", "") else f"{r['type1']}/{r['type2']}"
        lines.append(
            f"| {i} | {r['name']} | {types} | {r['base_speed']} | "
            f"**{r['spe_max_nature']}** | {r['spe_max_neutral']} | "
            f"{r['spe_zero_neutral']} | {r['spe_min_neg_nature']} |"
        )
    lines.extend([
        "",
        "## Notas",
        "",
        "- Speed tier = ranking 1ºer turno: quien tenga mayor Spe efectiva mueve antes (sin prioridad de movimiento).",
        "- Empates de Spe se resuelven aleatoriamente turno a turno.",
        "- Pañuelo Elegido (objeto, no modelado en estas columnas) multiplica Spe × 1.5.",
        "- En Trick Room, el orden se invierte: menor Spe ataca primero.",
        "- Bonus por Bromuro/Mejora/Cambio de Marcha y otros boosts: aplicar +1/+2/etc. sobre **Spe (+Nat)** antes de comparar.",
        "- Pokémon no disponibles (Forma Regional, Mega no liberada, etc.) excluidos de la tabla principal.",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = build_tiers()
    if not rows:
        print("No Pokémon parsed — abort")
        return
    json_path = write_json(rows)
    md_path = write_markdown(rows)
    available = sum(1 for r in rows if r["available"])
    print(f"Parsed {len(rows)} Pokémon ({available} disponibles)")
    print(f"  → {json_path.relative_to(ROOT)}")
    print(f"  → {md_path.relative_to(ROOT)}")
    fastest = rows[:5]
    slowest = sorted([r for r in rows if r["available"]], key=lambda r: r["spe_max_nature"])[:5]
    print("\nTop 5 más rápidos (Spe +Nat):")
    for r in fastest:
        print(f"  {r['spe_max_nature']:3d}  {r['name']}")
    print("\nTop 5 más lentos disponibles:")
    for r in slowest:
        print(f"  {r['spe_max_nature']:3d}  {r['name']}")


if __name__ == "__main__":
    main()
