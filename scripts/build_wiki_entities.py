"""Generate wiki/entities/{pokemon,ataques,habilidades,objetos}/<slug>.md from raw/.

Idempotent: overwrites. Adds frontmatter, injects [[wikilinks]] for known tipos,
appends a Related section, and writes per-category _index.md.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
WIKI = ROOT / "wiki"
DATE = "2026-04-29"

TIPOS_ES = {
    "Normal", "Fuego", "Agua", "Eléctrico", "Planta", "Hielo",
    "Lucha", "Veneno", "Tierra", "Volador", "Psíquico", "Bicho",
    "Roca", "Fantasma", "Dragón", "Siniestro", "Acero", "Hada",
}

TYPE_BOOSTER_ITEMS = {
    "carbon", "agua-mistica", "semilla-milagro", "iman", "antiderretir",
    "cinturon-negro", "flecha-venenosa", "arena-fina", "pico-afilado",
    "cuchara-torcida", "polvo-plata", "piedra-dura", "hechizo",
    "colmillo-dragon", "gafas-de-sol", "revest-metalico", "fairy-feather",
    "panuelo-de-seda",
}

RESIST_BERRIES = {
    "baya-anjiro", "baya-bariba", "baya-caoca", "baya-caquic",
    "baya-chilan", "baya-dillo", "baya-drasi", "baya-gualot",
    "baya-hibis", "baya-kebia", "baya-meloc", "baya-pasio",
    "baya-pomaro", "baya-rimoya", "baya-tamar", "baya-yecana",
    "baya-zanama", "baya-zidra",
}


def link_tipo_in_cell(value: str) -> str:
    """Wrap a tipo name in [[ ]] if it matches a canonical tipo."""
    v = value.strip()
    if v in TIPOS_ES:
        return f"[[{v}]]"
    return value


def read_h1(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def parse_datos_table(text: str) -> dict[str, str]:
    """Parse the `## Datos` markdown table into key/value pairs."""
    out: dict[str, str] = {}
    in_table = False
    for line in text.splitlines():
        if line.strip().startswith("## Datos"):
            in_table = True
            continue
        if in_table:
            if line.strip().startswith("##"):
                break
            m = re.match(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", line)
            if m and not m.group(1).startswith("-") and m.group(1).strip() != "Propiedad":
                out[m.group(1).strip()] = m.group(2).strip()
    return out


def inject_tipo_links(text: str) -> str:
    """Replace tipo names that appear as standalone cell values in tables."""
    def repl(match: re.Match) -> str:
        cell = match.group(1).strip()
        if cell in TIPOS_ES:
            return f"| [[{cell}]] "
        return match.group(0)

    return re.sub(
        r"\|\s*([A-Za-zÁÉÍÓÚáéíóúÑñ]+)\s*(?=\|)",
        repl,
        text,
    )


def write_entity(out_path: Path, frontmatter: dict, body: str, related: list[str]) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fm = "---\n"
    for k, v in frontmatter.items():
        if isinstance(v, list):
            fm += f"{k}: [{', '.join(v)}]\n"
        else:
            fm += f"{k}: {v}\n"
    fm += "---\n\n"

    related_lines = "\n".join(f"- {item}" for item in related)
    related_section = f"\n\n## 🔗 Related\n\n{related_lines}\n" if related else ""

    if "## 🔗 Related" not in body:
        body = body.rstrip() + related_section

    out_path.write_text(fm + body, encoding="utf-8")


def process_pokemon() -> int:
    src = RAW / "pokemon"
    dst = WIKI / "entities" / "pokemon"
    count = 0
    for f in sorted(src.glob("*.md")):
        if f.name == "_source.md":
            continue
        text = f.read_text(encoding="utf-8")
        title = read_h1(text)
        datos = parse_datos_table(text)
        tipos = [datos.get("Tipo 1", ""), datos.get("Tipo 2", "")]
        tipos = [t for t in tipos if t and t != "-"]

        body = inject_tipo_links(text)

        related = []
        for t in tipos:
            related.append(f"[[{t}]]")
        for c in ("[[op-gg-pokedex]]", "[[damage-matrix]]", "[[coverage-matrix]]",
                  "[[speed-tier]]", "[[formula-stats]]"):
            related.append(c)

        gen = datos.get("Generación", "").lower().split(" - ")[0].replace("gen ", "gen-").strip()
        tags = ["pokemon"] + ([gen] if gen else []) + [t.lower() for t in tipos]

        fm = {
            "title": title,
            "date": DATE,
            "type": "entity",
            "tags": tags,
            "slug": f.stem,
        }
        write_entity(dst / f.name, fm, body, related)
        count += 1
    return count


def process_ataques() -> int:
    src = RAW / "ataques"
    dst = WIKI / "entities" / "ataques"
    count = 0
    for f in sorted(src.glob("*.md")):
        if f.name == "_source.md":
            continue
        text = f.read_text(encoding="utf-8")
        title = read_h1(text)
        datos = parse_datos_table(text)
        tipo = datos.get("Tipo", "")
        categoria = datos.get("Categoría", "")

        body = inject_tipo_links(text)

        related = []
        if tipo and tipo in TIPOS_ES:
            related.append(f"[[{tipo}]]")
        for c in ("[[op-gg-moves]]", "[[damage-matrix]]", "[[formula-dano]]",
                  "[[coverage-matrix]]"):
            related.append(c)

        tags = ["ataque"] + ([tipo.lower()] if tipo else []) + ([categoria.lower()] if categoria else [])

        fm = {
            "title": title,
            "date": DATE,
            "type": "entity",
            "tags": tags,
            "slug": f.stem,
        }
        write_entity(dst / f.name, fm, body, related)
        count += 1
    return count


def process_habilidades() -> int:
    src = RAW / "habilidades"
    dst = WIKI / "entities" / "habilidades"
    count = 0
    for f in sorted(src.glob("*.md")):
        if f.name == "_source.md":
            continue
        text = f.read_text(encoding="utf-8")
        title = read_h1(text)

        related = ["[[op-gg-abilities]]", "[[habilidades-modeladas]]", "[[formula-dano]]"]

        fm = {
            "title": title,
            "date": DATE,
            "type": "entity",
            "tags": ["habilidad"],
            "slug": f.stem,
        }
        write_entity(dst / f.name, fm, text, related)
        count += 1
    return count


def process_objetos() -> int:
    src = RAW / "objetos"
    dst = WIKI / "entities" / "objetos"
    count = 0
    for f in sorted(src.glob("*.md")):
        if f.name == "_source.md":
            continue
        text = f.read_text(encoding="utf-8")
        title = read_h1(text)
        datos = parse_datos_table(text)
        categoria = datos.get("Categoría", "")

        related = ["[[op-gg-items]]"]
        slug = f.stem
        if slug in TYPE_BOOSTER_ITEMS:
            related.append("[[type-booster]]")
        elif slug in RESIST_BERRIES:
            related.append("[[baya-tipo]]")
        elif slug == "panuelo-eleccion":
            related.append("[[panuelo-eleccion]]")

        if "Mega" in categoria or "Mega" in title:
            related.append("Piedra Mega — afecta forma del Pokémon, no daño")

        related.append("[[damage-matrix]]")

        tags = ["objeto"] + ([categoria.lower().replace(" ", "-")] if categoria else [])

        fm = {
            "title": title,
            "date": DATE,
            "type": "entity",
            "tags": tags,
            "slug": slug,
        }
        write_entity(dst / f.name, fm, text, related)
        count += 1
    return count


def write_category_index(category: str, count: int, dst: Path, brief: str) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in dst.glob("*.md") if p.name != "_index.md")
    lines = [
        "---",
        f"title: Índice — {category}",
        f"date: {DATE}",
        "type: index",
        f"tags: [{category}, index]",
        "---",
        "",
        f"# Índice — {category}",
        "",
        brief,
        "",
        f"Total: **{count}** entradas.",
        "",
        "## Lista",
        "",
    ]
    for f in files:
        title = read_h1(f.read_text(encoding="utf-8").split("---", 2)[-1])
        lines.append(f"- [[{f.stem}|{title}]]")
    lines.append("")
    lines.extend([
        "## 🔗 Related",
        "",
        "- [[../../index|Master Index]]",
    ])
    (dst / "_index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    print("Pokemon:    ", n := process_pokemon())
    write_category_index(
        "Pokémon", n, WIKI / "entities" / "pokemon",
        "Fichas individuales de Pokémon disponibles en Pokémon Champions. "
        "Origen: [[op-gg-pokedex]]. Stats finales se calculan con [[formula-stats]] y [[ph-puntos-habilidad]].",
    )
    print("Ataques:    ", n := process_ataques())
    write_category_index(
        "Ataques", n, WIKI / "entities" / "ataques",
        "Movimientos del juego. Origen: [[op-gg-moves]]. "
        "Daño se calcula con [[formula-dano]] sobre [[damage-matrix]].",
    )
    print("Habilidades:", n := process_habilidades())
    write_category_index(
        "Habilidades", n, WIKI / "entities" / "habilidades",
        "Abilities del juego. Origen: [[op-gg-abilities]]. "
        "Solo 21 modeladas en daño en [[habilidades-modeladas]] (op.gg) + 7 defensivas custom.",
    )
    print("Objetos:    ", n := process_objetos())
    write_category_index(
        "Objetos", n, WIKI / "entities" / "objetos",
        "Items del juego. Origen: [[op-gg-items]]. "
        "Categorías clave: [[type-booster]] (×1.2 al tipo), [[baya-tipo]] (×0.5 a 1 SE), "
        "[[panuelo-eleccion]] (Spe ×1.5 + lock).",
    )


if __name__ == "__main__":
    main()
