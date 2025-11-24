"""
Test that all Jupyter notebooks in the repository execute without errors.
"""

import subprocess
from pathlib import Path

import pytest


def find_notebooks():
    """Find all .ipynb files in the repository, excluding executed output notebooks."""
    root = Path(__file__).parent.parent
    notebooks = []

    # Excluded notebooks
    excluded_notebooks = {
        "bedrock-example.ipynb"  # Requires special IAM role assumption
    }

    for nb_path in root.rglob("*.ipynb"):
        # Skip notebooks that are execution outputs or in hidden directories
        if "_executed" not in nb_path.name and not any(
            part.startswith(".") for part in nb_path.parts
        ):
            # Skip explicitly excluded notebooks
            if nb_path.name not in excluded_notebooks:
                notebooks.append(nb_path)
    return notebooks


@pytest.mark.parametrize("notebook_path", find_notebooks())
def test_notebook_execution(notebook_path, tmp_path):
    """
    Test that a notebook can be executed without errors.

    Args:
        notebook_path: Path to the notebook to test
        tmp_path: Temporary directory provided by pytest
    """
    output_path = tmp_path / f"{notebook_path.stem}_executed.ipynb"

    # Execute the notebook
    result = subprocess.run(
        [
            "python",
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            str(notebook_path),
            "--output",
            str(output_path),
        ],
        capture_output=True,
        text=True,
    )

    # Check that execution was successful
    assert result.returncode == 0, (
        f"Notebook {notebook_path.name} failed to execute.\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )

    # Verify output file was created
    assert output_path.exists(), f"Output notebook was not created for {notebook_path.name}"
