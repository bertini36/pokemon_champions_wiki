#!/usr/bin/env python3
"""Spread optimizer for Pokemon Champions.

For each defender, finds minimum PH spread (HP + Def for physical / HP + SpD
for special) needed to survive each top threat from the damage matrix.

Outputs:
- raw/calculos/spread-optimizer.json
- raw/calculos/spread-optimizer.md

Requires raw/calculos/damage-matrix.json (run build_damage_matrix.py first).
"""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_damage_matrix import calc_damage, type_es_to_en  # noqa: E402

LEVEL = 50
IV = 31
AP_TO_EV_RATIO = 7.875
MAX_STAT_AP = 32
MAX_TOTAL_AP = 66

POKEMON_DIR = ROOT / "raw" / "pokemon"
MATRIX_PATH = ROOT / "raw" / "calculos" / "damage-matrix.json"
OUTPUT_DIR = ROOT / "raw" / "calculos"

FIELD_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$")


def calc_stat(base: int, ap: int, nature_mult: float) -> int:
    ev = math.floor(ap * AP_TO_EV_RATIO)
    raw = math.floor((2 * base + IV + math.floor(ev / 4)) * LEVEL / 100) + 5
    return math.floor(raw * nature_mult)


def calc_hp(base: int, ap: int) -> int:
    ev = math.floor(ap * AP_TO_EV_RATIO)
    return math.floor((2 * base + IV + math.floor(ev / 4)) * LEVEL / 100) + LEVEL + 10


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
    abilities_en = [a.strip() for a in fields.get("Habilidades (en)", "").split(",") if a.strip()]
    return {
        "name": title or md_path.stem,
        "available": fields.get("Disponible", "") == "Sí",
        "stats": {
            "hp":        int(fields["PS"]),
            "attack":    int(fields["Ataque"]),
            "defense":   int(fields["Defensa"]),
            "spAttack":  int(fields["Ataque Especial"]),
            "spDefense": int(fields["Defensa Especial"]),
            "speed":     int(fields["Velocidad"]),
        },
        "abilities": abilities_en,
    }


def find_min_spread(
    defender_base_stats: dict,
    attacker_stats: dict,
    attacker_ability: str | None,
    move: dict,
    type_eff: float, is_stab: bool,
) -> tuple[int, int, int] | None:
    """Return (hp_ph, def_ph, hp_final) needed to survive max_dmg, or None if impossible."""
    is_physical = move["category"] == "physical"
    def_stat_key = "defense" if is_physical else "spDefense"

    for total in range(0, MAX_TOTAL_AP + 1):
        for hp_ph in range(0, min(MAX_STAT_AP, total) + 1):
            def_ph = total - hp_ph
            if def_ph > MAX_STAT_AP:
                continue
            hp_final = calc_hp(defender_base_stats["hp"], hp_ph)
            def_stats = {
                "hp": hp_final,
                "attack": calc_stat(defender_base_stats["attack"], 0, 0.9),
                "defense": calc_stat(defender_base_stats["defense"], def_ph if is_physical else 0, 1.1 if is_physical else 1.0),
                "spAttack": calc_stat(defender_base_stats["spAttack"], 0, 1.0),
                "spDefense": calc_stat(defender_base_stats["spDefense"], def_ph if not is_physical else 0, 1.1 if not is_physical else 1.0),
                "speed": calc_stat(defender_base_stats["speed"], 0, 1.0),
            }
            _, max_dmg, _ = calc_damage(
                attacker_stats, def_stats,
                move, is_stab, type_eff,
                item_type_boost=True,
                attacker_ability=attacker_ability,
            )
            if max_dmg < hp_final:
                return (hp_ph, def_ph, hp_final)
    return None


def main() -> None:
    if not MATRIX_PATH.exists():
        print(f"missing {MATRIX_PATH} — run scripts/build_damage_matrix.py first")
        return

    matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

    pokemons_by_name: dict[str, dict] = {}
    for f in POKEMON_DIR.glob("*.md"):
        if f.name.startswith("_"):
            continue
        p = parse_pokemon(f)
        if p:
            pokemons_by_name[p["name"]] = p

    available_names = {row["attacker"] for row in matrix}

    # For each defender, find top threats from the matrix
    threats_by_defender: dict[str, list] = {}
    for atk_row in matrix:
        for cell in atk_row["vs"]:
            defender = cell["defender"]
            if defender == atk_row["attacker"]:
                continue
            if cell["max_pct"] < 50:
                continue
            threats_by_defender.setdefault(defender, []).append({
                "attacker": atk_row["attacker"],
                "attacker_stats": atk_row["attacker_stats"],
                "attacker_ability": atk_row.get("attacker_ability"),
                "move": atk_row["move"],
                "move_type": atk_row["move_type"],
                "move_power": atk_row["move_power"],
                "move_category": atk_row["move_category"],
                "stab": atk_row["stab"],
                "type_eff": cell["type_eff"],
                "max_pct_default": cell["max_pct"],
                "ohko_default": cell["ohko"],
            })

    for defender_name, threats in threats_by_defender.items():
        threats.sort(key=lambda t: -t["max_pct_default"])
        # Cap to top 8 threats per defender
        threats_by_defender[defender_name] = threats[:8]

    results = []
    for defender_name in sorted(threats_by_defender.keys()):
        defender = pokemons_by_name.get(defender_name)
        if not defender:
            continue
        threats = threats_by_defender[defender_name]
        spread_results = []
        for t in threats:
            move = {
                "name": t["move"],
                "type": t["move_type"],
                "type_en": type_es_to_en(t["move_type"]),
                "power": t["move_power"],
                "category": t["move_category"],
            }
            spread = find_min_spread(
                defender["stats"],
                t["attacker_stats"],
                t["attacker_ability"],
                move,
                t["type_eff"], t["stab"],
            )
            spread_results.append({
                "threat": t,
                "spread": spread,
            })
        results.append({
            "defender": defender_name,
            "base_hp": defender["stats"]["hp"],
            "base_def": defender["stats"]["defense"],
            "base_spdef": defender["stats"]["spDefense"],
            "spread_results": spread_results,
        })

    json_path = OUTPUT_DIR / "spread-optimizer.json"
    json_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        "# Spread Optimizer",
        "",
        "Para cada defensor, calcula los **PH mínimos en HP + Def/SpD** necesarios para sobrevivir cada amenaza top de la damage matrix (atacantes que le hacen ≥50% por defecto).",
        "",
        "Naturaleza defensiva asumida: **Osada** (+Def -Atk) para hits físicos, **Cauta** (+SpD -SpA) para hits especiales.",
        "",
        "Generado por `scripts/build_spread_optimizer.py` desde `raw/calculos/damage-matrix.json` y `raw/pokemon/`.",
        "",
        "## Limitaciones",
        "",
        "- Asume PH Spe = 0 (defensor lento). Si quieres mantener velocidad, resta PH del HP/Def disponibles.",
        "- Type booster del atacante = ×1.2 fijo. Sin Pañuelo / Vidas / críticos / clima.",
        "- El defensor no usa baya tipo en este cálculo (worst case). Una baya tipo divide el daño SE entre 2.",
        "- 'No sobrevive' = ni con 32 PH HP + 32 PH Def consigue tankear (necesitaría buff de habilidad como Multiescamas o reducción extra).",
        "",
        "## Detalle por defensor",
        "",
    ]

    for r in results:
        md_lines.append(f"### {r['defender']} — base HP {r['base_hp']} / Def {r['base_def']} / SpD {r['base_spdef']}")
        md_lines.append("")
        if not r["spread_results"]:
            md_lines.append("- _Ningún atacante le hace ≥50% por defecto._")
            md_lines.append("")
            continue
        md_lines.append("| Amenaza | Move (BP, tipo) | Eff | %HP default | PH HP | PH Def/SpD | HP final |")
        md_lines.append("|---|---|---|---|---|---|---|")
        for sr in r["spread_results"]:
            t = sr["threat"]
            spread = sr["spread"]
            eff_label = f"×{t['type_eff']:g}" if t["type_eff"] != 1.0 else "—"
            move_label = f"{t['move']} ({t['move_power']}, {t['move_type']})"
            if spread is None:
                spread_label = "no sobrevive (32/32 insuficiente)"
                hp_label = "—"
                ph_hp = ph_def = "—"
            else:
                ph_hp, ph_def, hp_final = spread
                spread_label = f"PH HP={ph_hp}, {'Def' if t['move_category']=='physical' else 'SpD'}={ph_def}"
                hp_label = str(hp_final)
            md_lines.append(
                f"| {t['attacker']} | {move_label} | {eff_label} | "
                f"{t['max_pct_default']}% | {ph_hp if isinstance(ph_hp, int) else ph_hp} | "
                f"{ph_def if isinstance(ph_def, int) else ph_def} | {hp_label} |"
            )
        md_lines.append("")

    md_path = OUTPUT_DIR / "spread-optimizer.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"  → {json_path.relative_to(ROOT)}")
    print(f"  → {md_path.relative_to(ROOT)}")
    survives = sum(1 for r in results for sr in r["spread_results"] if sr["spread"] is not None)
    impossible = sum(1 for r in results for sr in r["spread_results"] if sr["spread"] is None)
    print(f"\nDefensores: {len(results)} | spreads encontrados: {survives} | imposibles (32/32 insuficiente): {impossible}")


if __name__ == "__main__":
    main()
