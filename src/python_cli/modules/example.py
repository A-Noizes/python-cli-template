"""
Example submodule for the `modules` package.

This module shows how to structure additional submodules that the CLI can
discover or import dynamically.

Author: Your Name
Created: 2026-04-26
Version: 0.1.0
"""

def run_example(name: str | None = None) -> str:
    """Return a greeting message for the example module.

    Args:
        name: Optional name to include in the greeting.

    Returns:
        A greeting string.
    """
    if name:
        return f"Example says hello to {name}!"
    return "Example says hello!"
