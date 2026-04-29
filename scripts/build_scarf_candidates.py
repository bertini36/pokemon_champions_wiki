#!/usr/bin/env python3
"""Pañuelo Elección candidate ranker for Pokemon Champions.

Combina speed-vs-scarf + coverage-matrix + damage-matrix para puntuar
candidatos a Pañuelo Elección.

Score factors:
- Spe optimizada (más rápido = más útil con Pañuelo en general)
- Speed jump al ponerle Pañuelo (cuántos enemigos pasa a outspeed)
- Coverage SE (Pañuelo lockea 1 move, queremos que ese move pegue mucho)
- OHKOs/2HKOs que ya hace (potencia ofensiva)
- Single-type focused (mejor candidato si su STAB principal cubre ya bien)

Outputs:
- raw/calculos/scarf-candidates.json
- raw/calculos/scarf-candidates.md
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CALC_DIR = ROOT / "raw" / "calculos"
OUTPUT_DIR = CALC_DIR

REQUIRED = [
    CALC_DIR / "speed-vs-scarf.json",
    CALC_DIR / "coverage-matrix.json",
    CALC_DIR / "damage-matrix.json",
]


def main() -> None:
    for p in REQUIRED:
        if not p.exists():
            print(f"missing {p} — run dependency scripts first")
            return

    speed_data = {r["name"]: r for r in json.loads(REQUIRED[0].read_text(encoding="utf-8"))}
    coverage_data = {r["name"]: r for r in json.loads(REQUIRED[1].read_text(encoding="utf-8"))}
    damage_matrix = json.loads(REQUIRED[2].read_text(encoding="utf-8"))

    candidates = []
    for atk_row in damage_matrix:
        name = atk_row["attacker"]
        speed = speed_data.get(name)
        coverage = coverage_data.get(name)
        if not speed or not coverage:
            continue

        spe_opt = speed["speeds"]["optimized"]
        spe_scarf = speed["speeds"]["scarfed"]
        # How many enemies it outspeeds with vs without Pañuelo (vs their optimized)
        outspeed_normal = sum(
            1 for other in speed_data.values()
            if other["name"] != name and other["speeds"]["optimized"] < spe_opt
        )
        outspeed_scarf = sum(
            1 for other in speed_data.values()
            if other["name"] != name and other["speeds"]["optimized"] < spe_scarf
        )
        scarf_jump = outspeed_scarf - outspeed_normal

        ohkos = sum(1 for c in atk_row["vs"] if c["ohko"] and c["defender"] != name)
        twohkos = sum(1 for c in atk_row["vs"] if c["two_hko"] and c["defender"] != name)
        se_count = coverage["se_count"]

        # Score weighting
        score = (
            spe_opt * 0.05            # raw speed
            + scarf_jump * 4          # cuántos enemigos pasa a outspeed con Pañuelo
            + ohkos * 6               # cada OHKO vale más
            + twohkos * 2
            + se_count * 1.5          # versatilidad ofensiva
        )

        # Penalty si ya outspeed a todo sin Pañuelo (no necesita Pañuelo)
        if outspeed_normal == len(speed_data) - 1:
            score -= 15

        candidates.append({
            "name": name,
            "types": atk_row["attacker_types"],
            "spe_opt": spe_opt,
            "spe_scarf": spe_scarf,
            "outspeed_normal": outspeed_normal,
            "outspeed_scarf": outspeed_scarf,
            "scarf_jump": scarf_jump,
            "se_count": se_count,
            "ohkos": ohkos,
            "twohkos": twohkos,
            "best_move": atk_row["move"],
            "best_move_type": atk_row["move_type"],
            "best_move_power": atk_row["move_power"],
            "score": round(score, 1),
        })

    candidates.sort(key=lambda c: -c["score"])

    json_path = OUTPUT_DIR / "scarf-candidates.json"
    json_path.write_text(json.dumps(candidates, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        "# Pañuelo Elección — Ranking de Candidatos",
        "",
        "Pokémon disponibles ranqueados como candidatos a llevar **Pañuelo Elección** según:",
        "",
        "```",
        "score = spe_opt * 0.05",
        "      + scarf_jump * 4    (enemigos extra que outspeed con Pañuelo)",
        "      + ohkos * 6         (OHKOs ya conseguidos con su mejor STAB)",
        "      + twohkos * 2",
        "      + se_count * 1.5    (versatilidad SE)",
        "      - 15 si ya outspeed a todos sin Pañuelo",
        "```",
        "",
        "Generado por `scripts/build_scarf_candidates.py` desde `speed-vs-scarf.json`,",
        "`coverage-matrix.json` y `damage-matrix.json`.",
        "",
        "## Limitaciones",
        "",
        "- Pañuelo lockea al Pokémon en 1 movimiento durante todo el combate.",
        "- Score asume que el move 'mejor STAB' que usa damage-matrix será el move bloqueado.",
        "- No considera coverage físico vs especial mixto (un Sweeper bloqueado en move físico pierde su Mansa/Modesta SpA).",
        "- Score no penaliza explícitamente sustituibilidad por type booster ×1.2 (Pañuelo no boostea power, solo Spe).",
        "",
        "## Ranking",
        "",
        "| # | Pokémon | Tipos | Spe opt | Spe scarf | Salto | OHKOs | 2HKOs | SE | Mejor STAB | Score |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, c in enumerate(candidates, start=1):
        types = "/".join(c["types"])
        md_lines.append(
            f"| {i} | {c['name']} | {types} | {c['spe_opt']} | "
            f"**{c['spe_scarf']}** | +{c['scarf_jump']} | {c['ohkos']} | "
            f"{c['twohkos']} | {c['se_count']} | "
            f"{c['best_move']} ({c['best_move_power']}) | **{c['score']}** |"
        )

    md_lines.extend(["", "## Análisis top 5", ""])
    for i, c in enumerate(candidates[:5], start=1):
        types = "/".join(c["types"])
        md_lines.append(f"### {i}. {c['name']} ({types}) — score {c['score']}")
        md_lines.append("")
        md_lines.append(
            f"- **Spe optimizada**: {c['spe_opt']} → con Pañuelo **{c['spe_scarf']}** "
            f"(outspeed {c['outspeed_normal']} → {c['outspeed_scarf']}, salto +{c['scarf_jump']})"
        )
        md_lines.append(
            f"- **Move bloqueado**: {c['best_move']} ({c['best_move_type']}, "
            f"{c['best_move_power']} BP)"
        )
        md_lines.append(f"- **OHKOs/2HKOs**: {c['ohkos']} / {c['twohkos']}  |  **SE coverage**: {c['se_count']}/18")
        md_lines.append("")

    md_path = OUTPUT_DIR / "scarf-candidates.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"  → {json_path.relative_to(ROOT)}")
    print(f"  → {md_path.relative_to(ROOT)}")
    print("\nTop 5 candidatos Pañuelo:")
    for c in candidates[:5]:
        print(f"  score={c['score']:5.1f}  {c['name']:25s}  spe={c['spe_opt']}→{c['spe_scarf']}  ohkos={c['ohkos']}")


if __name__ == "__main__":
    main()
