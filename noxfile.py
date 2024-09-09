"""This module implements our CI function calls."""

import nox


@nox.session(name="format")
def format(session):
    """Fix common convention problems automatically."""
    session.install("ruff")
    session.run("ruff", "format")


@nox.session(name="lint")
def lint(session):
    """Check code conventions."""
    session.install("ruff")
    session.run("ruff", "check")


@nox.session(name="typing")
def mypy(session):
    """Check type hints."""
    session.install("-r", "requirements.txt")
    session.install("mypy")
    session.run(
        "mypy",
        "--install-types",
        "--non-interactive",
        "--ignore-missing-imports",
        "--no-strict-optional",
        "--no-warn-return-any",
        "--implicit-reexport",
        "--allow-untyped-calls",
        "src",
    )


@nox.session(name="test")
def run_test(session):
    """Run pytest."""
    session.install(".[tests]")
    session.install("pytest")
    session.run("pytest")
