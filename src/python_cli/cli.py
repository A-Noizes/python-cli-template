"""
Ein kleines Beispiel für eine CLI-Anwendung.

Beschreibung:
  Dieses Modul implementiert eine einfache Kommandozeilenoberfläche mit
  `argparse`. Es dient als Ausgangspunkt für moderne Python-CLI-Projekte.

Argumente (Beispiel):
  --name NAME      : Optionaler Name, wird zur Begrüßung verwendet.
  --verbose        : Aktiviert ausführliche Ausgabe.
  --version        : Zeigt die Versionsnummer an und beendet das Programm.

Ausführung (Beispiel):
  python -m python_cli --name Alice

Erklärung:
  `main()` parst die Argumente und führt die gewünschte Aktion aus. Diese
  Vorlage ist bewusst einfach gehalten und sollte an projekt-spezifische
  Anforderungen angepasst werden.

Author: Your Name
Created: 2026-04-26
Version: 0.1.0
"""

from __future__ import annotations

import argparse
import sys
from typing import Optional

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python-cli-template",
        description="Beispiel-CLI (Template)",
    )
    parser.add_argument("--name", type=str, help="Name für die Begrüßung", default=None)
    parser.add_argument("--verbose", action="store_true", help="Ausführliche Ausgabe")
    parser.add_argument("--version", action="store_true", help="Version anzeigen und beenden")
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(__version__)
        return 0

    if args.name:
        if args.verbose:
            print(f"[VERBOSE] Begrüße {args.name}")
        print(f"Hallo, {args.name}!")
    else:
        if args.verbose:
            print("[VERBOSE] Keine Namen-Option angegeben")
        print("Hallo! Verwende --name NAME für eine persönliche Begrüßung.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
