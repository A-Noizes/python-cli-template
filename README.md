
# Python CLI Template

This repository is a modern, lightweight template for Python CLI projects.

Quick start

1. Clone the template locally:

   git clone https://github.com/yourname/python-cli-template.git my-project
   cd my-project

2. Create a Conda environment and install dependencies:

   conda env create -f environment.yml
   conda activate python-cli-template
   pip install -e .

If you prefer a virtualenv instead of Conda, you can still use:

   python -m venv .venv
   source .venv/bin/activate
   pip install -e .

3. Run the CLI:

   python -m python_cli --help

What this template includes

- A modern `pyproject.toml` (PEP 621)
- `src/` package layout
- A simple `argparse`-based CLI in `src/python_cli/cli.py`
- `README.md`, `LICENSE`, `.gitignore`
- Basic `tests/` and a GitHub Actions CI workflow

Extending with submodules

This template includes a `modules` subpackage at `src/python_cli/modules`.
Place additional submodules there (for example, `example.py`). They can be
imported as `python_cli.modules.example` and hooked into the CLI.

Customization

Replace `python-cli-template` and author information in `pyproject.toml` and the module docstrings.

License

MIT
