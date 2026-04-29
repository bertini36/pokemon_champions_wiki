#!/usr/bin/env python3
"""Builds summary generator for Pokemon Champions.

Parsea raw/builds/*.md y produce un índice consolidado con validación
cruzada contra raw/pokemon, raw/ataques, raw/objetos.

Outputs:
- raw/calculos/builds-summary.json
- raw/calculos/builds-summary.md
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILDS_DIR = ROOT / "raw" / "builds"
POKEMON_DIR = ROOT / "raw" / "pokemon"
MOVES_DIR = ROOT / "raw" / "ataques"
ITEMS_DIR = ROOT / "raw" / "objetos"
OUTPUT_DIR = ROOT / "raw" / "calculos"

FIELD_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$")


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


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


def parse_section(md_path: Path, header: str) -> list[str]:
    lines = []
    in_section = False
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.startswith(f"## {header}"):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section:
            lines.append(line)
    return lines


def parse_movepool_build(md_path: Path) -> list[str]:
    moves = []
    for line in parse_section(md_path, "Movimientos"):
        if line.startswith("|") and not line.startswith("|---") and not line.startswith("| #"):
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) >= 2 and parts[0].isdigit():
                moves.append(parts[1])
    return moves


def parse_strategy(md_path: Path) -> dict:
    section = parse_section(md_path, "Estrategia")
    text = "\n".join(section).strip()
    ability = None
    tips = []
    in_tips = False
    for line in section:
        line = line.strip()
        if line.startswith("HABILIDAD:"):
            ability = line.replace("HABILIDAD:", "").strip()
        if line.startswith("TIPS:"):
            in_tips = True
            continue
        if in_tips and line.startswith("- "):
            tips.append(line[2:].strip())
    return {"ability_es": ability, "tips": tips, "raw": text}


def parse_build(md_path: Path) -> dict:
    title, fields = parse_md_table(md_path)
    moves = parse_movepool_build(md_path)
    strategy = parse_strategy(md_path)
    teammates = "\n".join(parse_section(md_path, "Compañeros recomendados")).strip()
    return {
        "filename": md_path.name,
        "title": title,
        "pokemon": fields.get("Pokémon", ""),
        "format": fields.get("Formato", ""),
        "item": fields.get("Objeto", ""),
        "nature": fields.get("Naturaleza", ""),
        "evs": fields.get("EVs", ""),
        "ivs": fields.get("IVs", ""),
        "moves": moves,
        "strategy": strategy,
        "teammates": teammates,
    }


def index_files(directory: Path, key: str = "title") -> dict[str, Path]:
    """Index files by their H1 title (lowercased, accent-stripped)."""
    idx = {}
    for f in directory.glob("*.md"):
        if f.name.startswith("_"):
            continue
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                idx[slugify(title)] = f
                idx[slugify(f.stem)] = f
                break
    return idx


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pokemon_idx = index_files(POKEMON_DIR)
    move_idx = index_files(MOVES_DIR)
    item_idx = index_files(ITEMS_DIR)

    builds = []
    for f in sorted(BUILDS_DIR.glob("*.md")):
        if f.name.startswith("_"):
            continue
        b = parse_build(f)
        warnings = []
        if slugify(b["pokemon"]) not in pokemon_idx:
            warnings.append(f"pokemon-not-found: {b['pokemon']}")
        for m in b["moves"]:
            # Strip parenthetical glosses like "Triturar (Crunch)"
            move_name = re.sub(r"\s*\([^)]+\)\s*$", "", m).strip()
            if slugify(move_name) not in move_idx:
                warnings.append(f"move-not-found: {move_name}")
        item_clean = b["item"].split("(")[0].strip()
        if item_clean and slugify(item_clean) not in item_idx:
            warnings.append(f"item-not-found: {b['item']}")
        b["warnings"] = warnings
        builds.append(b)

    json_path = OUTPUT_DIR / "builds-summary.json"
    json_path.write_text(json.dumps(builds, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        "# Builds VGC — Resumen",
        "",
        f"Total builds curadas: **{len(builds)}**",
        "",
        "Generado por `scripts/build_builds_summary.py`. Validación cruzada contra",
        "`raw/pokemon/`, `raw/ataques/` y `raw/objetos/`.",
        "",
        "## Índice",
        "",
        "| # | Build | Pokémon | Item | Naturaleza | Habilidad | Warnings |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, b in enumerate(builds, start=1):
        warn_label = f"⚠️ {len(b['warnings'])}" if b["warnings"] else "—"
        ability = b["strategy"]["ability_es"] or "—"
        md_lines.append(
            f"| {i} | [{b['title']}](../builds/{b['filename']}) | {b['pokemon']} | "
            f"{b['item']} | {b['nature']} | {ability} | {warn_label} |"
        )

    md_lines.extend(["", "## Detalle por build", ""])
    for b in builds:
        md_lines.append(f"### {b['title']}")
        md_lines.append("")
        md_lines.append(f"- **Pokémon**: {b['pokemon']}")
        md_lines.append(f"- **Formato**: {b['format']}")
        md_lines.append(f"- **Item**: {b['item']}")
        md_lines.append(f"- **Naturaleza**: {b['nature']}")
        md_lines.append(f"- **EVs**: {b['evs']}")
        md_lines.append(f"- **Habilidad**: {b['strategy']['ability_es'] or '—'}")
        md_lines.append(f"- **Movimientos**: {', '.join(b['moves'])}")
        if b["teammates"]:
            md_lines.append(f"- **Compañeros**: {b['teammates']}")
        if b["warnings"]:
            md_lines.append(f"- **⚠️ Warnings**:")
            for w in b["warnings"]:
                md_lines.append(f"  - {w}")
        if b["strategy"]["tips"]:
            md_lines.append("- **Tips**:")
            for t in b["strategy"]["tips"]:
                md_lines.append(f"  - {t}")
        md_lines.append("")

    md_path = OUTPUT_DIR / "builds-summary.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"  → {json_path.relative_to(ROOT)}")
    print(f"  → {md_path.relative_to(ROOT)}")
    total_warns = sum(len(b["warnings"]) for b in builds)
    print(f"\n{len(builds)} builds parseadas, {total_warns} warnings totales")
    if total_warns:
        for b in builds:
            if b["warnings"]:
                print(f"  {b['filename']}: {len(b['warnings'])} warnings")


if __name__ == "__main__":
    main()
