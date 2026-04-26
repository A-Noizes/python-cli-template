"""
A small example of a CLI application.

Description:
    This module implements a simple command-line interface using `argparse`.
    It serves as a starting point for modern Python CLI projects.

Arguments (example):
    --name NAME      : Optional name used for a greeting.
    --verbose        : Enables verbose output.
    --version        : Prints the version and exits.

Execution (example):
    python -m python_cli --name Alice

Explanation:
    `main()` parses the arguments and performs the requested action. This
    template is intentionally simple and should be adapted to project-specific
    requirements.

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
