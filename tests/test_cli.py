"""Grundlegende Tests für das CLI-Template."""

import importlib


def test_import_package():
    pkg = importlib.import_module("python_cli")
    assert hasattr(pkg, "__version__")
