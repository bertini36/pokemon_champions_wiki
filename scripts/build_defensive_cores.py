#!/usr/bin/env python3
"""Defensive cores generator for Pokemon Champions.

Para cada par (A, B) de Pokémon disponibles, calcula la cobertura defensiva
conjunta: cuántos tipos atacantes hay que ningún miembro del par sea débil a
ellos.

Outputs:
- raw/calculos/defensive-cores.json
- raw/calculos/defensive-cores.md
"""

from __future__ import annotations

import json
import re
import unicodedata
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POKEMON_DIR = ROOT / "raw" / "pokemon"
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


def weakness_profile(pokemon: dict, chart: dict) -> dict[str, float]:
    """Multiplicador defensivo para cada tipo atacante incidente."""
    def_types = [t for t in (pokemon["type1"], pokemon["type2"]) if t and t != "-"]
    profile = {}
    for atk_type in ALL_TYPES_ES:
        atk_norm = normalize(atk_type)
        mult = 1.0
        for dt in def_types:
            mult *= chart.get(atk_norm, {}).get(normalize(dt), 1.0)
        profile[atk_type] = mult
    return profile


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pokemons = []
    for f in POKEMON_DIR.glob("*.md"):
        if f.name.startswith("_"):
            continue
        p = parse_pokemon(f)
        if p:
            pokemons.append(p)

    chart = parse_type_chart()
    available = [p for p in pokemons if p["available"]]
    print(f"Parsed {len(pokemons)} Pokémon ({len(available)} disponibles)")

    profiles = {p["name"]: weakness_profile(p, chart) for p in available}

    cores = []
    for a, b in combinations(available, 2):
        prof_a = profiles[a["name"]]
        prof_b = profiles[b["name"]]
        # For each attacking type, the pair is "covered" if at least one member is NOT weak (mult <= 1)
        weaknesses_a = {t for t, m in prof_a.items() if m > 1}
        weaknesses_b = {t for t, m in prof_b.items() if m > 1}
        shared_weak = weaknesses_a & weaknesses_b
        # Resistencias compartidas (ambos resisten ese tipo)
        shared_resist = {t for t in ALL_TYPES_ES if prof_a[t] < 1 and prof_b[t] < 1}
        # Inmunidades cubiertas por al menos uno
        immunities = {t for t in ALL_TYPES_ES if prof_a[t] == 0 or prof_b[t] == 0}

        cores.append({
            "a": a["name"],
            "a_types": [t for t in (a["type1"], a["type2"]) if t and t != "-"],
            "b": b["name"],
            "b_types": [t for t in (b["type1"], b["type2"]) if t and t != "-"],
            "shared_weaknesses": sorted(shared_weak),
            "shared_resists": sorted(shared_resist),
            "immunities_in_pair": sorted(immunities),
            "shared_weak_count": len(shared_weak),
            "shared_resist_count": len(shared_resist),
            "immunity_count": len(immunities),
            "score": len(shared_resist) + len(immunities) - 2 * len(shared_weak),
        })

    cores.sort(key=lambda c: -c["score"])

    json_path = OUTPUT_DIR / "defensive-cores.json"
    json_path.write_text(json.dumps(cores, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        "# Defensive Cores",
        "",
        "Pares de Pokémon disponibles ranqueados por **score defensivo conjunto**:",
        "",
        "```",
        "score = |resistencias compartidas| + |inmunidades del par| - 2 * |debilidades compartidas|",
        "```",
        "",
        "Score alto = los dos miembros se complementan: cubren las debilidades del otro y",
        "comparten muchas resistencias / inmunidades.",
        "Score bajo (negativo) = comparten debilidades = mal core defensivo.",
        "",
        "Generado por `scripts/build_defensive_cores.py` desde `raw/pokemon/*.md` y `raw/tipos/*.md`.",
        "",
        "## Top cores defensivos",
        "",
        "| # | Core | Tipos | Score | Resists | Immune | Shared Weak |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, c in enumerate(cores[:20], start=1):
        types = f"{'/'.join(c['a_types'])} + {'/'.join(c['b_types'])}"
        md_lines.append(
            f"| {i} | {c['a']} + {c['b']} | {types} | **{c['score']}** | "
            f"{c['shared_resist_count']} | {c['immunity_count']} | "
            f"{c['shared_weak_count']} |"
        )

    md_lines.extend(["", "## Detalle top 10", ""])
    for i, c in enumerate(cores[:10], start=1):
        types_a = "/".join(c["a_types"])
        types_b = "/".join(c["b_types"])
        md_lines.append(f"### {i}. {c['a']} ({types_a}) + {c['b']} ({types_b}) — score {c['score']}")
        md_lines.append("")
        md_lines.append(f"- **Resistencias compartidas** ({c['shared_resist_count']}): " + (", ".join(c["shared_resists"]) or "_ninguna_"))
        md_lines.append(f"- **Inmunidades en el par** ({c['immunity_count']}): " + (", ".join(c["immunities_in_pair"]) or "_ninguna_"))
        md_lines.append(f"- **Debilidades compartidas** ({c['shared_weak_count']}): " + (", ".join(c["shared_weaknesses"]) or "_ninguna ✅_"))
        md_lines.append("")

    md_lines.extend(["", "## Anti-cores (peores combinaciones)", ""])
    md_lines.append("| # | Core | Tipos | Score | Shared Weak |")
    md_lines.append("|---|---|---|---|---|")
    for i, c in enumerate(cores[-10:][::-1], start=1):
        types = f"{'/'.join(c['a_types'])} + {'/'.join(c['b_types'])}"
        md_lines.append(
            f"| {i} | {c['a']} + {c['b']} | {types} | **{c['score']}** | "
            f"{', '.join(c['shared_weaknesses']) or '—'} |"
        )

    md_path = OUTPUT_DIR / "defensive-cores.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"  → {json_path.relative_to(ROOT)}")
    print(f"  → {md_path.relative_to(ROOT)}")
    print(f"\nPares analizados: {len(cores)}")
    print("\nTop 3 cores:")
    for c in cores[:3]:
        print(f"  score={c['score']:+3d}  {c['a']} + {c['b']}")


if __name__ == "__main__":
    main()
