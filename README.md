# Python CLI Template

Dieses Repository ist ein modernes, leichtgewichtiges Template für Python-CLI-Projekte.

Kurz: Klonen, anpassen, loslegen.

Schnellstart

1. Klone das Template lokal:

   git clone https://github.com/yourname/python-cli-template.git my-project
   cd my-project

2. Erstelle ein virtuelles Environment und installiere Abhängigkeiten:

   python -m venv .venv
   source .venv/bin/activate
   pip install -e .

3. Ausführen:

   python -m python_cli --help

Was dieses Template enthält

- Modernes `pyproject.toml` (PEP 621)
- Paketstruktur unter `src/`
- Einfache `argparse`-basierte CLI in `src/python_cli/cli.py`
- `README.md`, `LICENSE`, `.gitignore`
- Grundlegende `tests/` sowie eine GitHub Actions CI-Konfiguration

Anpassen

Ersetze `python-cli-template` und Autorenangaben in `pyproject.toml` und in den Docstrings.

Lizenz

MIT
