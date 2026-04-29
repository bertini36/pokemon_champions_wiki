#!/usr/bin/env python3
"""Threat list generator for Pokemon Champions.

Inverse view of damage-matrix.json: for each defender, lists who threatens it.

Outputs:
- raw/calculos/threat-list.json
- raw/calculos/threat-list.md

Requires raw/calculos/damage-matrix.json (run build_damage_matrix.py first).
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT_PATH = ROOT / "raw" / "calculos" / "damage-matrix.json"
OUTPUT_DIR = ROOT / "raw" / "calculos"


def main() -> None:
    if not INPUT_PATH.exists():
        print(f"missing {INPUT_PATH} — run scripts/build_damage_matrix.py first")
        return

    matrix = json.loads(INPUT_PATH.read_text(encoding="utf-8"))

    # Build inverse: defender → list of (attacker, move, damage info)
    threats_by_defender: dict[str, dict] = {}
    for atk_row in matrix:
        for cell in atk_row["vs"]:
            defender = cell["defender"]
            if defender == atk_row["attacker"]:
                continue
            entry = threats_by_defender.setdefault(defender, {
                "defender_types": cell["defender_types"],
                "defender_hp": cell["defender_hp"],
                "attackers": [],
            })
            entry["attackers"].append({
                "attacker": atk_row["attacker"],
                "attacker_types": atk_row["attacker_types"],
                "move": atk_row["move"],
                "move_type": atk_row["move_type"],
                "move_power": atk_row["move_power"],
                "stab": atk_row["stab"],
                "type_eff": cell["type_eff"],
                "min_dmg": cell["min_dmg"],
                "max_dmg": cell["max_dmg"],
                "min_pct": cell["min_pct"],
                "max_pct": cell["max_pct"],
                "ohko": cell["ohko"],
                "two_hko": cell["two_hko"],
                "ability_notes": cell.get("ability_notes", []),
            })

    # Sort attackers by max_pct desc
    for entry in threats_by_defender.values():
        entry["attackers"].sort(key=lambda a: -a["max_pct"])
        entry["ohko_count"] = sum(1 for a in entry["attackers"] if a["ohko"])
        entry["two_hko_count"] = sum(1 for a in entry["attackers"] if a["two_hko"])

    # Sort defenders by danger (most OHKOs received first)
    sorted_defenders = sorted(
        threats_by_defender.items(),
        key=lambda kv: (-kv[1]["ohko_count"], -kv[1]["two_hko_count"]),
    )

    json_path = OUTPUT_DIR / "threat-list.json"
    json_path.write_text(json.dumps(dict(sorted_defenders), ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        "# Threat List por Defensor",
        "",
        "Para cada Pokémon disponible, lista qué atacantes le hacen daño y cuántos le OHKOean / 2HKOean.",
        "Ordenado por **número de OHKOs recibidos** (los más vulnerables primero).",
        "",
        "Generado por `scripts/build_threat_list.py` desde `raw/calculos/damage-matrix.json`.",
        "",
        "## Resumen — vulnerabilidad",
        "",
        "| # | Defensor | Tipos | HP | OHKOs | 2HKOs | Atacantes |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, (defender, entry) in enumerate(sorted_defenders, start=1):
        types_d = "/".join(entry["defender_types"])
        md_lines.append(
            f"| {i} | {defender} | {types_d} | {entry['defender_hp']} | "
            f"**{entry['ohko_count']}** | {entry['two_hko_count']} | "
            f"{len(entry['attackers'])} |"
        )

    md_lines.extend(["", "## Detalle por defensor", ""])
    for defender, entry in sorted_defenders:
        types_d = "/".join(entry["defender_types"])
        md_lines.append(f"### {defender} ({types_d}) — HP {entry['defender_hp']}")
        md_lines.append("")
        md_lines.append(
            f"- **Riesgo**: {entry['ohko_count']} OHKOs, {entry['two_hko_count']} 2HKOs, "
            f"de {len(entry['attackers'])} atacantes evaluados"
        )
        md_lines.append("")
        md_lines.append("| Atacante | Move | Tipo | Eff | % HP | KO | Notas |")
        md_lines.append("|---|---|---|---|---|---|---|")
        for a in entry["attackers"]:
            ko_label = "**OHKO**" if a["ohko"] else ("2HKO" if a["two_hko"] else f"{a['max_pct']}%")
            eff_label = f"×{a['type_eff']:g}" if a["type_eff"] != 1.0 else "—"
            stab_label = "STAB" if a["stab"] else ""
            ab_label = ", ".join(a["ability_notes"]) if a["ability_notes"] else ""
            notes = ", ".join(filter(None, [stab_label, ab_label])) or "—"
            md_lines.append(
                f"| {a['attacker']} | {a['move']} | {a['move_type']} | "
                f"{eff_label} | {a['min_pct']}–{a['max_pct']}% | {ko_label} | {notes} |"
            )
        md_lines.append("")

    md_path = OUTPUT_DIR / "threat-list.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"  → {json_path.relative_to(ROOT)}")
    print(f"  → {md_path.relative_to(ROOT)}")
    print("\nTop 3 más vulnerables (más OHKOs recibidos):")
    for defender, entry in sorted_defenders[:3]:
        print(f"  {defender:25s}  OHKOs={entry['ohko_count']:2d}  2HKOs={entry['two_hko_count']:2d}")


if __name__ == "__main__":
    main()
