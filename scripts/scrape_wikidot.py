#!/usr/bin/env python3
"""Scrape D&D 5e class and subclass text from dnd5e.wikidot.com using trafilatura."""

import sys
import time
from pathlib import Path

import trafilatura

BASE_URL = "https://dnd5e.wikidot.com"
OUT_DIR = Path(__file__).parent.parent / "scraped_data" / "classes-and-subclasses"

# (display_name, wikidot_slug)
CLASSES: dict[str, tuple[str, list[tuple[str, str]]]] = {
    "Artificer": (
        "artificer",
        [
            ("Alchemist", "alchemist"),
            ("Armorer", "armorer"),
            ("Artillerist", "artillerist"),
            ("Battle Smith", "battle-smith"),
        ],
    ),
    "Barbarian": (
        "barbarian",
        [
            ("Path of the Ancestral Guardian", "ancestral-guardian"),
            ("Path of the Battlerager", "battlerager"),
            ("Path of the Beast", "beast"),
            ("Path of the Berserker", "berserker"),
            ("Path of the Giant", "giant"),
            ("Path of the Storm Herald", "storm-herald"),
            ("Path of the Totem Warrior", "totem-warrior"),
            ("Path of the Zealot", "zealot"),
            ("Path of Wild Magic", "wild-magic"),
        ],
    ),
    "Bard": (
        "bard",
        [
            ("College of Creation", "creation"),
            ("College of Eloquence", "eloquence"),
            ("College of Glamour", "glamour"),
            ("College of Lore", "lore"),
            ("College of Spirits", "spirits"),
            ("College of Swords", "swords"),
            ("College of Valor", "valor"),
            ("College of Whispers", "whispers"),
        ],
    ),
    "Cleric": (
        "cleric",
        [
            ("Arcana Domain", "arcana"),
            ("Death Domain", "death"),
            ("Forge Domain", "forge"),
            ("Grave Domain", "grave"),
            ("Knowledge Domain", "knowledge"),
            ("Life Domain", "life"),
            ("Light Domain", "light"),
            ("Nature Domain", "nature"),
            ("Order Domain", "order"),
            ("Peace Domain", "peace"),
            ("Tempest Domain", "tempest"),
            ("Trickery Domain", "trickery"),
            ("Twilight Domain", "twilight"),
            ("War Domain", "war"),
        ],
    ),
    "Druid": (
        "druid",
        [
            ("Circle of Dreams", "dreams"),
            ("Circle of Spores", "spores"),
            ("Circle of Stars", "stars"),
            ("Circle of the Land", "land"),
            ("Circle of the Moon", "moon"),
            ("Circle of the Shepherd", "shepherd"),
            ("Circle of Wildfire", "wildfire"),
        ],
    ),
    "Fighter": (
        "fighter",
        [
            ("Banneret", "banneret"),
            ("Battle Master", "battle-master"),
            ("Cavalier", "cavalier"),
            ("Champion", "champion"),
            ("Echo Knight", "echo-knight"),
            ("Eldritch Knight", "eldritch-knight"),
            ("Psi Warrior", "psi-warrior"),
            ("Rune Knight", "rune-knight"),
            ("Samurai", "samurai"),
        ],
    ),
    "Monk": (
        "monk",
        [
            ("Way of Mercy", "mercy"),
            ("Way of Shadow", "shadow"),
            ("Way of the Ascendant Dragon", "ascendant-dragon"),
            ("Way of the Astral Self", "astral-self"),
            ("Way of the Drunken Master", "drunken-master"),
            ("Way of the Four Elements", "four-elements"),
            ("Way of the Kensei", "kensei"),
            ("Way of the Long Death", "long-death"),
            ("Way of the Open Hand", "open-hand"),
            ("Way of the Sun Soul", "sun-soul"),
        ],
    ),
    "Paladin": (
        "paladin",
        [
            ("Oathbreaker", "oathbreaker"),
            ("Oath of Conquest", "conquest"),
            ("Oath of Devotion", "devotion"),
            ("Oath of Glory", "glory"),
            ("Oath of Redemption", "redemption"),
            ("Oath of the Ancients", "ancients"),
            ("Oath of the Crown", "crown"),
            ("Oath of the Watchers", "watchers"),
            ("Oath of Vengeance", "vengeance"),
        ],
    ),
    "Ranger": (
        "ranger",
        [
            ("Beast Master Conclave", "beast-master"),
            ("Drakewarden", "drakewarden"),
            ("Fey Wanderer", "fey-wanderer"),
            ("Gloom Stalker Conclave", "gloom-stalker"),
            ("Horizon Walker Conclave", "horizon-walker"),
            ("Hunter Conclave", "hunter"),
            ("Monster Slayer Conclave", "monster-slayer"),
        ],
    ),
    "Rogue": (
        "rogue",
        [
            ("Arcane Trickster", "arcane-trickster"),
            ("Assassin", "assassin"),
            ("Inquisitive", "inquisitive"),
            ("Mastermind", "mastermind"),
            ("Phantom", "phantom"),
            ("Scout", "scout"),
            ("Soulknife", "soulknife"),
            ("Swashbuckler", "swashbuckler"),
            ("Thief", "thief"),
        ],
    ),
    "Sorcerer": (
        "sorcerer",
        [
            ("Aberrant Mind", "aberrant-mind"),
            ("Clockwork Soul", "clockwork-soul"),
            ("Divine Soul", "divine-soul"),
            ("Draconic Bloodline", "draconic-bloodline"),
            ("Lunar Sorcery", "lunar-sorcery"),
            ("Shadow Magic", "shadow-magic"),
            ("Storm Sorcery", "storm-sorcery"),
            ("Wild Magic", "wild-magic"),
        ],
    ),
    "Warlock": (
        "warlock",
        [
            ("Archfey", "archfey"),
            ("Celestial", "celestial"),
            ("Fathomless", "fathomless"),
            ("Fiend", "fiend"),
            ("Great Old One", "great-old-one"),
            ("Hexblade", "hexblade"),
            ("The Genie", "the-genie"),
            ("Undead", "undead"),
            ("Undying", "undying"),
        ],
    ),
    "Wizard": (
        "wizard",
        [
            ("Order of Scribes", "order-of-scribes"),
            ("School of Abjuration", "abjuration"),
            ("School of Bladesinging", "bladesinging"),
            ("School of Chronurgy", "chronurgy"),
            ("School of Conjuration", "conjuration"),
            ("School of Divination", "divination"),
            ("School of Enchantment", "enchantment"),
            ("School of Evocation", "evocation"),
            ("School of Graviturgy", "graviturgy"),
            ("School of Illusion", "illusion"),
            ("School of Necromancy", "necromancy"),
            ("School of Transmutation", "transmutation"),
            ("School of War Magic", "war-magic"),
        ],
    ),
}


def fetch_text(url: str) -> str | None:
    html = trafilatura.fetch_url(url)
    if html is None:
        return None
    return trafilatura.extract(html, include_tables=True, include_links=False)


def scrape_page(url: str, out_path: Path, label: str, skip_existing: bool) -> bool:
    if skip_existing and out_path.exists():
        sys.stdout.write(f"  SKIP {label}\n")
        return True
    text = fetch_text(url)
    if text is None:
        sys.stderr.write(f"  WARN: no content for {label} ({url})\n")
        return False
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    sys.stdout.write(f"  OK  {label}\n")
    return True


def main() -> None:
    skip_existing = "--force" not in sys.argv
    if not skip_existing:
        sys.stdout.write("--force: re-fetching all pages\n")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for class_name, (class_slug, subclasses) in CLASSES.items():
        class_url = f"{BASE_URL}/{class_slug}"
        class_out = OUT_DIR / f"{class_name}.txt"

        sys.stdout.write(f"\n[{class_name}]\n")
        scrape_page(class_url, class_out, class_name, skip_existing)
        time.sleep(0.5)

        subclass_dir = OUT_DIR / class_name
        for subclass_name, sub_slug in subclasses:
            sub_url = f"{BASE_URL}/{class_slug}:{sub_slug}"
            sub_out = subclass_dir / f"{subclass_name}.txt"
            scrape_page(
                sub_url, sub_out, f"{class_name} / {subclass_name}", skip_existing
            )
            time.sleep(0.5)

    sys.stdout.write("\nDone.\n")


if __name__ == "__main__":
    main()
