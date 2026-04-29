#!/usr/bin/env python3
"""Damage matrix generator for Pokemon Champions.

For each attacker (top movepool STAB) vs each defender, compute damage
using formula from raw/mecanicas/formula-dano.md plus type booster x1.2.

Inputs:
- raw/pokemon/*.md       (stats, types, available, moves)
- raw/ataques/*.md       (move type/category/power)
- raw/tipos/*.md         (type effectiveness chart)

Outputs:
- raw/calculos/damage-matrix.json
- raw/calculos/damage-matrix.md
"""

from __future__ import annotations

import json
import math
import re
import unicodedata
from pathlib import Path

LEVEL = 50
IV = 31
AP_TO_EV_RATIO = 7.875
MAX_STAT_AP = 32

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

TYPE_ES_TO_EN: dict[str, str] = {
    "normal": "normal", "fuego": "fire", "agua": "water", "electrico": "electric",
    "planta": "grass", "hielo": "ice", "lucha": "fighting", "veneno": "poison",
    "tierra": "ground", "volador": "flying", "psiquico": "psychic", "bicho": "bug",
    "roca": "rock", "fantasma": "ghost", "dragon": "dragon", "siniestro": "dark",
    "acero": "steel", "hada": "fairy",
}


def type_es_to_en(t: str) -> str:
    norm = unicodedata.normalize("NFD", t).encode("ascii", "ignore").decode().lower()
    return TYPE_ES_TO_EN.get(norm, norm)

# Damage-modifying abilities from raw/mecanicas/habilidades-calc.md.
# Each entry: (kind, value, condition).
# Conditions:
#   "always" → always apply
#   "stab" → applies to STAB moves
#   "type:<type>" → applies if move type matches (en lowercase)
#   "power_lte_60" → applies if move power <= 60
ABILITY_MODS: dict[str, dict] = {
    # Atacantes — power/atk/STAB
    "adaptability":   {"kind": "stab_mult",      "value": 2.0,  "cond": "stab"},
    "technician":     {"kind": "power_mult",     "value": 1.5,  "cond": "power_lte_60"},
    "huge-power":     {"kind": "atk_mult",       "value": 2.0,  "cond": "always"},
    "pure-power":     {"kind": "atk_mult",       "value": 2.0,  "cond": "always"},
    "hustle":         {"kind": "atk_mult",       "value": 1.5,  "cond": "always"},
    "gorilla-tactics":{"kind": "atk_mult",       "value": 1.5,  "cond": "always"},
    "blaze":          {"kind": "power_mult",     "value": 1.5,  "cond": "type:fire"},
    "torrent":        {"kind": "power_mult",     "value": 1.5,  "cond": "type:water"},
    "overgrow":       {"kind": "power_mult",     "value": 1.5,  "cond": "type:grass"},
    "swarm":          {"kind": "power_mult",     "value": 1.5,  "cond": "type:bug"},
    "tinted-lens":    {"kind": "nve_boost",      "value": 2.0,  "cond": "incoming_nve"},
    # Defensores — reduction
    "filter":         {"kind": "se_reduction",   "value": 0.75, "cond": "incoming_se"},
    "solid-rock":     {"kind": "se_reduction",   "value": 0.75, "cond": "incoming_se"},
    "prism-armor":    {"kind": "se_reduction",   "value": 0.75, "cond": "incoming_se"},
    "intimidate":     {"kind": "atk_drop",       "value": 0.66, "cond": "incoming_physical"},
    "multiscale":     {"kind": "all_reduction",  "value": 0.5,  "cond": "incoming_at_full_hp"},
    "shadow-shield":  {"kind": "all_reduction",  "value": 0.5,  "cond": "incoming_at_full_hp"},
    # Inmunidades de tipo
    "lightning-rod":  {"kind": "type_immune",    "value": 0.0,  "cond": "incoming_type:electric"},
    "motor-drive":    {"kind": "type_immune",    "value": 0.0,  "cond": "incoming_type:electric"},
    "volt-absorb":    {"kind": "type_immune",    "value": 0.0,  "cond": "incoming_type:electric"},
    "water-absorb":   {"kind": "type_immune",    "value": 0.0,  "cond": "incoming_type:water"},
    "storm-drain":    {"kind": "type_immune",    "value": 0.0,  "cond": "incoming_type:water"},
    "dry-skin":       {"kind": "type_immune",    "value": 0.0,  "cond": "incoming_type:water"},
    "flash-fire":     {"kind": "type_immune",    "value": 0.0,  "cond": "incoming_type:fire"},
    "sap-sipper":     {"kind": "type_immune",    "value": 0.0,  "cond": "incoming_type:grass"},
    "levitate":       {"kind": "type_immune",    "value": 0.0,  "cond": "incoming_type:ground"},
}

FIELD_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$")


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode()
    return s.lower().replace(" ", "-")


def calc_stat(base: int, ap: int, nature_mult: float) -> int:
    ev = math.floor(ap * AP_TO_EV_RATIO)
    raw = math.floor((2 * base + IV + math.floor(ev / 4)) * LEVEL / 100) + 5
    return math.floor(raw * nature_mult)


def calc_hp(base: int, ap: int) -> int:
    ev = math.floor(ap * AP_TO_EV_RATIO)
    return math.floor((2 * base + IV + math.floor(ev / 4)) * LEVEL / 100) + LEVEL + 10


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
    abilities_en = [a.strip() for a in fields.get("Habilidades (en)", "").split(",") if a.strip()]
    return {
        "name": title or md_path.stem,
        "type1": fields.get("Tipo 1", ""),
        "type2": fields.get("Tipo 2", "-"),
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
        "ability_es": fields.get("Habilidad 1", ""),
        "moves": parse_movepool(md_path),
    }


def parse_move(md_path: Path) -> dict | None:
    title, fields = parse_md_table(md_path)
    cat_es = fields.get("Categoría", "")
    power_str = fields.get("Potencia", "-")
    if cat_es == "Estado" or not power_str.isdigit():
        return None
    type_es = fields.get("Tipo", "")
    return {
        "name": title,
        "type": type_es,
        "type_en": type_es_to_en(type_es),
        "category": "physical" if cat_es == "Físico" else "special",
        "power": int(power_str),
    }


def parse_type_chart() -> dict[str, dict[str, float]]:
    """Build {atk_type: {def_type: multiplier}}.
    Reads "Atacando con X" sections of each tipo file.
    """
    chart: dict[str, dict[str, float]] = {}
    for tipo_file in TYPES_DIR.glob("*.md"):
        if tipo_file.name.startswith("_"):
            continue
        atk_type = tipo_file.stem.capitalize()
        # Normalize: file is "psiquico" → "Psiquico"; we want without accents
        atk_type = unicodedata.normalize("NFD", atk_type).encode("ascii", "ignore").decode()
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
                # Extract [[Tipo]] tokens
                for tipo in re.findall(r"\[\[([^\]]+)\]\]", line):
                    tipo_norm = unicodedata.normalize("NFD", tipo).encode("ascii", "ignore").decode()
                    chart[atk_type][tipo_norm] = mult
    return chart


def normalize_type(t: str) -> str:
    return unicodedata.normalize("NFD", t).encode("ascii", "ignore").decode()


def type_effectiveness(chart: dict, atk_type: str, def_types: list[str]) -> float:
    atk = normalize_type(atk_type)
    mult = 1.0
    for dt in def_types:
        if dt and dt != "-":
            mult *= chart.get(atk, {}).get(normalize_type(dt), 1.0)
    return mult


def apply_ability_mods(
    ability: str | None,
    side: str,
    move: dict,
    is_stab: bool,
    type_eff: float,
    defender_at_full_hp: bool = True,
) -> dict:
    """Return active modifiers for given ability on given side (attacker|defender)."""
    mods = {
        "power_mult": 1.0, "atk_mult": 1.0, "stab_mult": None, "eff_mult": 1.0,
        "atk_drop_mult": 1.0, "label": None,
    }
    if not ability:
        return mods
    spec = ABILITY_MODS.get(ability)
    if not spec:
        return mods
    cond = spec["cond"]
    move_type_en = move.get("type_en", "").lower()
    is_physical = move["category"] == "physical"
    matched = False
    match cond:
        case "always":
            matched = True
        case "stab":
            matched = is_stab and side == "attacker"
        case "power_lte_60":
            matched = move["power"] <= 60 and side == "attacker"
        case "incoming_se":
            matched = type_eff > 1 and side == "defender"
        case "incoming_nve":
            matched = 0 < type_eff < 1 and side == "attacker"
        case "incoming_physical":
            matched = is_physical and side == "defender"
        case "incoming_at_full_hp":
            matched = defender_at_full_hp and side == "defender"
        case _ if cond.startswith("type:"):
            matched = move_type_en == cond.split(":", 1)[1] and side == "attacker"
        case _ if cond.startswith("incoming_type:"):
            matched = move_type_en == cond.split(":", 1)[1] and side == "defender"
    if not matched:
        return mods
    mods["label"] = ability
    match spec["kind"]:
        case "stab_mult":
            mods["stab_mult"] = spec["value"]
        case "power_mult":
            mods["power_mult"] *= spec["value"]
        case "atk_mult":
            mods["atk_mult"] *= spec["value"]
        case "se_reduction" | "nve_boost":
            mods["eff_mult"] *= spec["value"]
        case "atk_drop":
            mods["atk_drop_mult"] *= spec["value"]
        case "all_reduction":
            mods["eff_mult"] *= spec["value"]
        case "type_immune":
            mods["eff_mult"] = 0.0
    return mods


def calc_damage(
    attacker_stats: dict, defender_stats: dict,
    move: dict, is_stab: bool, type_eff: float,
    item_type_boost: bool = True,
    attacker_ability: str | None = None,
    defender_ability: str | None = None,
    defender_resist_berry: bool = False,
    attacker_burned: bool = False,
) -> tuple[int, int, list[str]]:
    if move["power"] <= 0:
        return (0, 0, [])
    atk_mods = apply_ability_mods(attacker_ability, "attacker", move, is_stab, type_eff)
    def_mods = apply_ability_mods(defender_ability, "defender", move, is_stab, type_eff)
    is_physical = move["category"] == "physical"
    raw_atk = attacker_stats["attack" if is_physical else "spAttack"]
    raw_def = defender_stats["defense" if is_physical else "spDefense"]
    burn_mult = 0.5 if (attacker_burned and is_physical) else 1.0
    intimidate_mult = def_mods["atk_drop_mult"]  # 0.66 = -1 stage approx
    atk = math.floor(raw_atk * atk_mods["atk_mult"] * burn_mult * intimidate_mult)
    defn = raw_def
    power_mod = (1.2 if item_type_boost else 1.0) * atk_mods["power_mult"]
    base = math.floor(
        math.floor(2 * LEVEL / 5 + 2)
        * math.floor(move["power"] * power_mod)
        * math.floor(atk / defn)
        / 50
    ) + 2
    if atk_mods["stab_mult"] is not None and is_stab:
        stab = atk_mods["stab_mult"]
    else:
        stab = 1.5 if is_stab else 1.0
    berry_mult = 0.5 if (defender_resist_berry and type_eff > 1) else 1.0
    final = base * type_eff * stab * def_mods["eff_mult"] * berry_mult
    notes = [m for m in (atk_mods["label"], def_mods["label"]) if m]
    if defender_resist_berry and type_eff > 1:
        notes.append("baya-tipo")
    if attacker_burned and is_physical:
        notes.append("burn")
    return (math.floor(0.85 * final), math.floor(final), notes)


def best_stab_move(pokemon: dict, moves_by_name: dict) -> dict | None:
    poke_types = {normalize_type(pokemon["type1"]), normalize_type(pokemon["type2"])}
    candidates = []
    for move_name in pokemon["moves"]:
        m = moves_by_name.get(move_name)
        if not m or normalize_type(m["type"]) not in poke_types:
            continue
        candidates.append(m)
    if not candidates:
        # fallback: highest power non-STAB
        for move_name in pokemon["moves"]:
            m = moves_by_name.get(move_name)
            if m:
                candidates.append(m)
    if not candidates:
        return None
    return max(candidates, key=lambda m: m["power"])


def build_attacker_setup(pokemon: dict, move: dict) -> dict:
    is_physical = move["category"] == "physical"
    if is_physical:
        nature = ("attack", "spAttack")
        stats = {
            "hp":        calc_hp(pokemon["stats"]["hp"], 0),
            "attack":    calc_stat(pokemon["stats"]["attack"], 32, 1.1),
            "defense":   calc_stat(pokemon["stats"]["defense"], 0, 1.0),
            "spAttack":  calc_stat(pokemon["stats"]["spAttack"], 0, 0.9),
            "spDefense": calc_stat(pokemon["stats"]["spDefense"], 2, 1.0),
            "speed":     calc_stat(pokemon["stats"]["speed"], 32, 1.0),
        }
        spread = "Physical (32 Atk / 32 Spe)"
        nat_es = "Firme"
    else:
        nature = ("spAttack", "attack")
        stats = {
            "hp":        calc_hp(pokemon["stats"]["hp"], 0),
            "attack":    calc_stat(pokemon["stats"]["attack"], 0, 0.9),
            "defense":   calc_stat(pokemon["stats"]["defense"], 0, 1.0),
            "spAttack":  calc_stat(pokemon["stats"]["spAttack"], 32, 1.1),
            "spDefense": calc_stat(pokemon["stats"]["spDefense"], 2, 1.0),
            "speed":     calc_stat(pokemon["stats"]["speed"], 32, 1.0),
        }
        spread = "Sweeper (32 SpA / 32 Spe)"
        nat_es = "Modesta"
    return {"stats": stats, "spread": spread, "nature": nat_es}


def build_defender_setup(pokemon: dict) -> dict:
    return {
        "stats": {
            "hp":        calc_hp(pokemon["stats"]["hp"], 32),
            "attack":    calc_stat(pokemon["stats"]["attack"], 0, 1.0),
            "defense":   calc_stat(pokemon["stats"]["defense"], 16, 1.0),
            "spAttack":  calc_stat(pokemon["stats"]["spAttack"], 0, 1.0),
            "spDefense": calc_stat(pokemon["stats"]["spDefense"], 16, 1.0),
            "speed":     calc_stat(pokemon["stats"]["speed"], 2, 1.0),
        },
        "spread": "Bulky (32 HP / 16 Def / 16 SpD)",
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

    moves_by_name = {}
    for f in MOVES_DIR.glob("*.md"):
        if f.name.startswith("_"):
            continue
        m = parse_move(f)
        if m:
            moves_by_name[m["name"]] = m

    chart = parse_type_chart()
    print(f"Parsed {len(pokemons)} Pokémon, {len(moves_by_name)} attacking moves, "
          f"{len(chart)} types in chart")

    available = [p for p in pokemons if p["available"]]
    print(f"Available: {len(available)}")

    matrix = []
    for atk_poke in available:
        move = best_stab_move(atk_poke, moves_by_name)
        if not move:
            continue
        atk_setup = build_attacker_setup(atk_poke, move)
        atk_types = [t for t in (atk_poke["type1"], atk_poke["type2"]) if t and t != "-"]
        is_stab = normalize_type(move["type"]) in {normalize_type(t) for t in atk_types}
        atk_ability = atk_poke["abilities"][0] if atk_poke["abilities"] else None
        atk_ability_es = atk_poke.get("ability_es", "")

        row = {
            "attacker": atk_poke["name"],
            "attacker_types": atk_types,
            "attacker_stats": atk_setup["stats"],
            "attacker_spread": atk_setup["spread"],
            "attacker_nature": atk_setup["nature"],
            "attacker_ability": atk_ability,
            "attacker_ability_es": atk_ability_es,
            "attacker_ability_active": atk_ability in ABILITY_MODS,
            "move": move["name"],
            "move_type": move["type"],
            "move_power": move["power"],
            "move_category": move["category"],
            "stab": is_stab,
            "item": "type-booster (×1.2)",
            "vs": [],
        }

        for def_poke in available:
            def_setup = build_defender_setup(def_poke)
            def_types = [t for t in (def_poke["type1"], def_poke["type2"]) if t and t != "-"]
            eff = type_effectiveness(chart, move["type"], def_types)
            def_ability = def_poke["abilities"][0] if def_poke["abilities"] else None
            min_dmg, max_dmg, ability_notes = calc_damage(
                atk_setup["stats"], def_setup["stats"],
                move, is_stab, eff,
                item_type_boost=True,
                attacker_ability=atk_ability,
                defender_ability=def_ability,
            )
            hp = def_setup["stats"]["hp"]
            min_pct = round(min_dmg / hp * 100, 1) if hp else 0
            max_pct = round(max_dmg / hp * 100, 1) if hp else 0
            ohko = max_dmg >= hp
            two_hko = max_dmg * 2 >= hp

            min_berry, max_berry, _ = calc_damage(
                atk_setup["stats"], def_setup["stats"],
                move, is_stab, eff,
                item_type_boost=True,
                attacker_ability=atk_ability,
                defender_ability=def_ability,
                defender_resist_berry=True,
            )
            min_burn, max_burn, _ = calc_damage(
                atk_setup["stats"], def_setup["stats"],
                move, is_stab, eff,
                item_type_boost=True,
                attacker_ability=atk_ability,
                defender_ability=def_ability,
                attacker_burned=True,
            )
            row["vs"].append({
                "defender": def_poke["name"],
                "defender_types": def_types,
                "defender_ability": def_ability,
                "ability_notes": ability_notes,
                "defender_hp": hp,
                "type_eff": eff,
                "min_dmg": min_dmg,
                "max_dmg": max_dmg,
                "min_pct": min_pct,
                "max_pct": max_pct,
                "ohko": ohko,
                "two_hko": two_hko,
                "with_berry": {
                    "min_dmg": min_berry, "max_dmg": max_berry,
                    "min_pct": round(min_berry / hp * 100, 1) if hp else 0,
                    "max_pct": round(max_berry / hp * 100, 1) if hp else 0,
                    "ohko": max_berry >= hp,
                    "applies": eff > 1,
                },
                "if_burned": {
                    "min_dmg": min_burn, "max_dmg": max_burn,
                    "min_pct": round(min_burn / hp * 100, 1) if hp else 0,
                    "max_pct": round(max_burn / hp * 100, 1) if hp else 0,
                    "ohko": max_burn >= hp,
                    "applies": move["category"] == "physical",
                },
            })
        matrix.append(row)

    json_path = OUTPUT_DIR / "damage-matrix.json"
    json_path.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        "# Damage Matrix — Nv.50",
        "",
        "Daño calculado para cada atacante disponible vs cada defensor disponible, usando:",
        "",
        "- **Atacante**: preset Sweeper o Physical (según mejor STAB) + naturaleza + type booster ×1.2 + STAB",
        "- **Defensor**: spread Bulky 32 HP / 16 Def / 16 SpD",
        "- **Movimiento**: el de mayor potencia entre los STAB del movepool del atacante",
        "- **Roll**: 0.85 → 1.00 (sin críticos)",
        "",
        "Generado por `scripts/build_damage_matrix.py` desde `raw/pokemon/`, `raw/ataques/`, `raw/tipos/`,",
        "constantes de `raw/mecanicas/formula-stats.md`, fórmula de `raw/mecanicas/formula-dano.md`,",
        "type boosters de `raw/mecanicas/objetos-calc.md`.",
        "",
        "## Limitaciones",
        "",
        "- Sin clima, terreno, críticos, multi-hit, spread reduction (doubles), boost stages, burn",
        "- Habilidades modeladas: solo las 14 con efecto en daño (ver `raw/mecanicas/habilidades-calc.md`).",
        "  Habilidades como Intimidación, Multiescamas, absorbedoras de tipo NO modeladas.",
        "- Sin Pañuelo Elección (no afecta daño directo, sí turn order — ver `raw/calculos/speed-vs-scarf.md`)",
        "- Columnas extra: **+ Baya** (defensor con baya tipo correspondiente, ×0.5 si SE), **Si quemado** (atacante quemado ×0.5 atk físico)",
        "- ⚠️ La columna **Si quemado** sufre colapso cuando `floor(atk/def) ≤ 1` (formula op.gg trunca la división). En esos casos el daño no refleja realismo VGC.",
        "- Setup defensivo es un único spread universal — no optimizado por matchup",
        "",
        "## Resumen por atacante",
        "",
    ]
    for row in matrix:
        types = "/".join(row["attacker_types"])
        md_lines.append(f"### {row['attacker']} ({types})")
        md_lines.append("")
        md_lines.append(f"- **Setup**: {row['attacker_spread']}, naturaleza {row['attacker_nature']}, type booster ×1.2")
        ability_label = row["attacker_ability_es"] or row["attacker_ability"] or "—"
        ability_active = " (modelada)" if row["attacker_ability_active"] else ""
        md_lines.append(f"- **Habilidad activa**: {ability_label}{ability_active}")
        md_lines.append(f"- **Movimiento**: {row['move']} ({row['move_type']}, {row['move_power']} BP, {row['move_category']})")
        md_lines.append(f"- **STAB activo**: {'sí' if row['stab'] else 'no'}")
        md_lines.append("")
        md_lines.append("| Defensor | Tipos | HP | Eff | Dmg | % HP | KO | + Baya | Si quemado | Notas |")
        md_lines.append("|---|---|---|---|---|---|---|---|---|---|")
        for cell in sorted(row["vs"], key=lambda c: -c["max_pct"]):
            types_d = "/".join(cell["defender_types"])
            ko_label = "**OHKO**" if cell["ohko"] else ("2HKO" if cell["two_hko"] else f"{math.ceil(cell['defender_hp'] / max(cell['max_dmg'], 1))}HKO")
            eff_label = f"×{cell['type_eff']:g}" if cell["type_eff"] != 1.0 else "—"
            ab_notes = ", ".join(cell["ability_notes"]) if cell["ability_notes"] else "—"
            berry = cell["with_berry"]
            burn = cell["if_burned"]
            berry_label = f"{berry['max_pct']}%" if berry["applies"] else "—"
            burn_label = f"{burn['max_pct']}%" if burn["applies"] else "—"
            md_lines.append(
                f"| {cell['defender']} | {types_d} | {cell['defender_hp']} | "
                f"{eff_label} | {cell['min_dmg']}-{cell['max_dmg']} | "
                f"{cell['min_pct']}–{cell['max_pct']}% | {ko_label} | {berry_label} | {burn_label} | {ab_notes} |"
            )
        md_lines.append("")

    md_path = OUTPUT_DIR / "damage-matrix.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"  → {json_path.relative_to(ROOT)}")
    print(f"  → {md_path.relative_to(ROOT)}")
    print(f"\nMatrix: {len(matrix)} atacantes × {len(available)} defensores = {len(matrix)*len(available)} celdas")


if __name__ == "__main__":
    main()
